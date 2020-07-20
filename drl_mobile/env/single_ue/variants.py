"""Implementation variants of the basic single-UE & single-agent env with varying observations."""
import gym.spaces
import numpy as np

from drl_mobile.env.single_ue.base import MobileEnv


class BinaryMobileEnv(MobileEnv):
    """Subclass of the general Mobile Env that uses binary observations to indicate which BS are & can be connected"""
    def __init__(self, env_config):
        super().__init__(env_config)
        # observations: binary vector of BS availability (in range and dr >= req_dr) + already connected BS
        self.observation_space = gym.spaces.MultiBinary(2 * self.num_bs)
        # actions: select a BS to be connected to/disconnect from or noop
        self.action_space = gym.spaces.Discrete(self.num_bs + 1)

    def get_ue_obs(self, ue):
        """
        Return the an observation of the current world for a given UE
        It consists of 2 binary vectors: BS availability and already connected BS
        """
        bs_availability = [int(bs.can_connect(ue.pos)) for bs in self.bs_list]
        connected_bs = [int(bs in ue.bs_dr.keys()) for bs in self.bs_list]
        return np.array(bs_availability + connected_bs)


class JustConnectedObsMobileEnv(BinaryMobileEnv):
    """Dummy observations just contain binary info about which BS are connected. Nothing about availability"""
    def __init__(self, env_config):
        super().__init__(env_config)
        # observations: just binary vector of already connected BS
        self.observation_space = gym.spaces.MultiBinary(self.num_bs)
        # same action space as binary env: select a BS to be connected to/disconnect from or noop

    def get_ue_obs(self, ue):
        """Observation: Currently connected BS"""
        connected_bs = [int(bs in ue.bs_dr.keys()) for bs in self.bs_list]
        return np.array(connected_bs)


class DatarateMobileEnv(BinaryMobileEnv):
    """Subclass of the binary MobileEnv that uses the achievable data rate as observations"""
    def __init__(self, env_config):
        """
        Env where the achievable data rate is passed as observations
        Special setting: dr_cutoff='auto' (sub_req_dr must be True) -->
            1. Subtract required data rate --> negative if data rate is too low
            2. Clip/cut off at req. dr --> symmetric range [-req_dr, +req_dr]; doesn't matter if dr is much higher
            3. Normalize by dividing by req_dr --> range [-1, 1] similar to other obs

        These are highly tailored to a step utility functions where UEs have a fixed req. dr and flat utility.
        Not great for log utility function.

        Extra fields in the env_config:

        * dr_cutoff: Any data rate above this value will be cut off --> help have obs in same range
        * sub_req_dr: If true, subtract a UE's required data rate from the achievable dr --> neg obs if too little
        * curr_dr_obs: If true, add a UE's current total data rate (over all BS) to the observations
        * ues_at_bs_obs: If true, add obs showing the number of connected UEs at each BS. To help balance connections.
        """
        super().__init__(env_config)
        self.dr_cutoff = env_config['dr_cutoff']
        self.sub_req_dr = env_config['sub_req_dr']
        self.curr_dr_obs = env_config['curr_dr_obs']
        self.ues_at_bs_obs = env_config['ues_at_bs_obs']
        assert not (self.dr_cutoff == 'auto' and not self.sub_req_dr), "For dr_cutoff auto, sub_req_dr must be True."
        assert (not self.curr_dr_obs) or (self.dr_cutoff == 'auto' and self.sub_req_dr), \
            "Enable all processing to add extra obs"

        # observations: vector of dr to each BS + (optionally: total curr dr of UE) + already connected BS
        # cut off dr at given dr level. here, dr is below 200 anyways --> default doesn't cut off
        max_dr_req = max([ue.dr_req for ue in self.ue_list])
        self.log.info('Max dr req', max_dr_req=max_dr_req, dr_cutoff=self.dr_cutoff, sub_req_dr=self.sub_req_dr,
                      curr_dr_obs=self.curr_dr_obs)
        assert self.dr_cutoff == 'auto' or max_dr_req < self.dr_cutoff, \
            "dr_cutoff should be higher than max required dr. by UEs"
        obs_space = {}

        # 1. Achievable data rate for given UE for all BS --> Box;
        if self.dr_cutoff == 'auto':
            # normalized to [-1, 1]
            dr_low = np.full(shape=(self.num_bs,), fill_value=-1)
            dr_high = np.ones(self.num_bs)
        else:
            # if we subtract the required data rate, observations may become negative
            if self.sub_req_dr:
                dr_low = np.full(shape=(self.num_bs,), fill_value=-max_dr_req)
            else:
                dr_low = np.zeros(self.num_bs)
            dr_high = np.full(shape=(self.num_bs,), fill_value=self.dr_cutoff)
        obs_space['dr'] = gym.spaces.Box(low=dr_low, high=dr_high)

        # 2. Connected BS --> MultiBinary
        obs_space['connected'] = gym.spaces.MultiBinary(self.num_bs)

        # 3. Optional: total current dr of the UE over all BS connections. Normalized to [-1, 1]. 0 = exactly fulfilled
        if self.curr_dr_obs:
            obs_space['dr_total'] = gym.spaces.Box(low=-1, high=1, shape=(1,))

        # 4. Optional: Number of connected UEs per BS. Discrete: 0 up to all UEs
        if self.ues_at_bs_obs:
            obs_space['ues_at_bs'] = gym.spaces.MultiDiscrete([self.num_ue+1 for _ in range(self.num_bs)])

        self.observation_space = gym.spaces.Dict(obs_space)
        # same action space as binary env: select a BS to be connected to/disconnect from or noop

    def get_ue_obs(self, ue):
        """
        Observation: Achievable data rate per BS (processed) + currently connected BS (binary)
        + optionally: total curr dr + num UEs per BS
        """
        obs_dict = {}

        if self.dr_cutoff == 'auto':
            # subtract req_dr and auto clip & normalize to [-1, 1]
            bs_dr = []
            for bs in self.bs_list:
                dr_sub = bs.data_rate(ue) - ue.dr_req
                dr_clip = min(dr_sub, ue.dr_req)        # clipped to range [-dr_req, dr_req]
                dr_norm = dr_clip / ue.dr_req
                bs_dr.append(dr_norm)
        elif self.sub_req_dr:
            # subtract req_dr and cut off at dr_cutoff
            bs_dr = [min(bs.data_rate(ue) - ue.dr_req, self.dr_cutoff) for bs in self.bs_list]
        else:
            # just cut off at dr_cutoff
            bs_dr = [min(bs.data_rate(ue), self.dr_cutoff) for bs in self.bs_list]
        obs_dict['dr'] = bs_dr

        obs_dict['connected'] = [int(bs in ue.bs_dr.keys()) for bs in self.bs_list]

        if self.curr_dr_obs:
            total_dr = ue.curr_dr
            # process by subtracting dr_req, clipping to [-dr_req, dr_req], normalizing to [-1, 1]
            total_dr -= ue.dr_req
            total_dr = min(total_dr, ue.dr_req)
            total_dr = total_dr / ue.dr_req
            obs_dict['dr_total'] = [total_dr]

        if self.ues_at_bs_obs:
            obs_dict['ues_at_bs'] = [bs.num_conn_ues for bs in self.bs_list]

        return obs_dict


class NormDrMobileEnv(BinaryMobileEnv):
    """Similar to DatarateMobileEnv but with different data rate processing."""
    def __init__(self, env_config):
        super().__init__(env_config)
        # clip & normalize data rates according to utility.
        # we clip utility at +20, which is reached for a dr of 100
        self.dr_cutoff = 100
        obs_space = {
            'dr': gym.spaces.Box(low=0, high=1, shape=(self.num_bs,)),
            'connected': gym.spaces.MultiBinary(self.num_bs),
            # 'ues_at_bs': gym.spaces.MultiDiscrete([self.num_ue+1 for _ in range(self.num_bs)]),
            'ues_at_bs': gym.spaces.Box(low=0, high=1, shape=(self.num_bs,))
        }
        self.observation_space = gym.spaces.Dict(obs_space)

    def get_ue_obs(self, ue):
        """Obs: Data rate (cut off, but not further processed) & """
        # data rates: clipped and normalized according to dr_cutoff
        bs_dr = []
        for bs in self.bs_list:
            dr_clip = min(bs.data_rate(ue), self.dr_cutoff)
            dr_norm = dr_clip / self.dr_cutoff
            bs_dr.append(dr_norm)

        # connected BS
        bs_conn = [int(bs in ue.bs_dr.keys()) for bs in self.bs_list]

        # num connected UEs per BS
        # ues_at_bs = [bs.num_conn_ues for bs in self.bs_list]
        ues_at_bs = [bs.num_conn_ues / self.num_ue for bs in self.bs_list]

        return {'dr': bs_dr, 'connected': bs_conn, 'ues_at_bs': ues_at_bs}
