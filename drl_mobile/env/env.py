import random

import gym
import gym.spaces
import structlog
import numpy as np
import matplotlib.pyplot as plt


# TODO: once this grows too large, split it into separate modules (base_env, extended_env, central_env, rllib_env,...)


class MobileEnv(gym.Env):
    """OpenAI Gym environment with multiple moving UEs and stationary BS on a map"""
    metadata = {'render.modes': ['human']}

    def __init__(self, episode_length, map, bs_list, ue_list, disable_interference=True):
        """
        Create a new environment object with an OpenAI Gym interface
        :param episode_length: Total number of simulation time steps in one episode
        :param map: Map object representing the playground
        :param bs_list: List of basestation objects in the environment
        :param ue_list: List of UE objects in the environment
        :param disable_interference: If true, disable all interference, ie, only use SNR, not SINR
        """
        super(gym.Env, self).__init__()
        self.time = 0
        self.episode_length = episode_length
        self.map = map
        self.disable_interference = disable_interference
        # disable interference for all BS (or not)
        self.bs_list = bs_list
        for bs in self.bs_list:
            bs.disable_interference = self.disable_interference
        # pass the env to all users (needed for movement; interference etc)
        self.ue_list = ue_list
        for ue in self.ue_list:
            ue.env = self
        # current observation
        self.obs = None
        # observation and action space are defined in the subclass --> different variants
        self.observation_space = None
        self.action_space = None

        # FIXME: leads to deep copy errors!
        self.log = structlog.get_logger()

    @property
    def num_bs(self):
        return len(self.bs_list)

    @property
    def num_ue(self):
        return len(self.ue_list)

    @property
    def active_bs(self):
        return [bs for bs in self.bs_list if bs.active]

    def seed(self, seed=None):
        random.seed(seed)

    def get_obs(self, ue):
        """Return the an observation of the current world for a given UE"""
        raise NotImplementedError('Implement in subclass')

    def calc_reward(self, ue, penalty):
        """
        Calculate and return reward for specific UE. Called before and after UE movement.
        High positive if connected with enough data rate, high negative if otherwise.
        Add penalty for undesired actions, eg, unsuccessful connection attempt; passed as arg.
        """
        reward = penalty
        # +10 if UE is connected such that its dr requirement is satisfied
        if ue.curr_dr >= ue.dr_req:
            reward += 10
        # -10 if not connected with sufficient data rate
        else:
            reward -= 10

        return reward

    def reset(self):
        """Reset environment by resetting time and all UEs (pos & movement) and their connections"""
        self.time = 0
        for ue in self.ue_list:
            ue.reset()
        for bs in self.bs_list:
            bs.reset()
        # TODO: this just returns the observation for the 1st UE
        self.obs = self.get_obs(self.ue_list[0])
        return self.obs

    def step(self, action: int):
        """
        Do 1 time step: Apply action and update UE position. Return new state, reward.
        Only update one UE at a time. With multiple UEs, select active UE using round robin.
        """
        penalty = 0
        # select active UE (to update in this step) using round robin
        ue = self.ue_list[self.time % self.num_ue]
        prev_obs = self.obs

        # apply action; 0 = no op
        if action > 0:
            bs = self.bs_list[action-1]
            # penalty of -3 for unsuccessful connection attempt
            penalty = -3 * (not ue.connect_to_bs(bs, disconnect=True))

        # check connections and reward before and after moving
        # TODO: usually before & after are the same anyways; so I can drop this if the simulator becomes too slow
        reward_before = self.calc_reward(ue, penalty)
        ue.move()
        self.time += 1
        reward_after = self.calc_reward(ue, penalty)

        # return next observation, reward, done, info
        # get obs of next UE
        next_ue = self.ue_list[self.time % self.num_ue]
        self.obs = self.get_obs(next_ue)
        # average reward
        reward = np.mean([reward_before, reward_after])
        done = self.time >= self.episode_length
        info = {}
        # self.log.info("Step", time=self.time, ue=ue, prev_obs=prev_obs, action=action, reward_before=reward_before,
        #               reward_after=reward_after, reward=reward, next_obs=self.obs, next_ue=next_ue, done=done)
        print(f"{self.time=}, {ue=}, {prev_obs=}, {action=}, {reward=}, {self.obs=}")
        return self.obs, reward, done, info

    def render(self, mode='human'):
        """Plot and visualize the current status of the world. Return the patch of actors for animation."""
        # list of matplotlib "artists", which can be used to create animations
        patch = []

        # map borders
        patch.extend(plt.plot(*self.map.shape.exterior.xy, color='gray'))
        # users & connections
        for ue in self.ue_list:
            patch.append(plt.scatter(*ue.pos.xy, label=ue.id, color=ue.color))
            for bs in ue.conn_bs:
                patch.extend(plt.plot([ue.pos.x, bs.pos.x], [ue.pos.y, bs.pos.y], color='orange'))
        # base stations
        for bs in self.bs_list:
            patch.append(plt.scatter(*bs.pos.xy, marker='^', c='black'))
            patch.extend(plt.plot(*bs.coverage.exterior.xy, color='black'))

        # title isn't redrawn in animation (out of box) --> static --> show time as text inside box, top-right corner
        patch.append(plt.title(type(self).__name__))
        patch.append(plt.text(0.9*self.map.width, 0.9*self.map.height, f"t={self.time}"))

        # legend doesn't change --> only draw once at the beginning
        if self.time == 0:
            plt.legend(loc='upper left')
        return patch


class BinaryMobileEnv(MobileEnv):
    """Subclass of the general Mobile Env that uses binary observations to indicate which BS are & can be connected"""
    def __init__(self, episode_length, map, bs_list, ue_list, **kwargs):
        super().__init__(episode_length, map, bs_list, ue_list, **kwargs)
        # observations: binary vector of BS availability (in range and dr >= req_dr) + already connected BS
        self.observation_space = gym.spaces.MultiBinary(2 * self.num_bs)
        # actions: select a BS to be connected to/disconnect from or noop
        self.action_space = gym.spaces.Discrete(self.num_bs + 1)

    def get_obs(self, ue):
        """
        Return the an observation of the current world for a given UE
        It consists of 2 binary vectors: BS availability and already connected BS
        """
        bs_availability = [int(ue.can_connect(bs)) for bs in self.bs_list]
        connected_bs = [int(bs in ue.conn_bs) for bs in self.bs_list]
        return np.array(bs_availability + connected_bs)


class JustConnectedObsMobileEnv(BinaryMobileEnv):
    """Dummy observations just contain binary info about which BS are connected. Nothing about availablility"""
    def __init__(self, episode_length, map, bs_list, ue_list, **kwargs):
        super().__init__(episode_length, map, bs_list, ue_list, **kwargs)
        # observations: just binary vector of already connected BS
        self.observation_space = gym.spaces.MultiBinary(self.num_bs)
        # same action space as binary env: select a BS to be connected to/disconnect from or noop

    def get_obs(self, ue):
        """Observation: Currently connected BS"""
        connected_bs = [int(bs in ue.conn_bs) for bs in self.bs_list]
        return np.array(connected_bs)


class DatarateMobileEnv(BinaryMobileEnv):
    """Subclass of the binary MobileEnv that uses the achievable data rate as observations"""
    def __init__(self, episode_length, map, bs_list, ue_list, dr_cutoff=200, sub_req_dr=False, **kwargs):
        """
        Env where the achievable data rate is passed as observations
        Special setting: dr_cutoff='auto' (sub_req_dr must be True) -->
            1. Subtract required data rate --> negative if data rate is too low
            2. Clip/cut off at req. dr --> symmetric range [-req_dr, +req_dr]; doesn't matter if dr is much higher
            3. Normalize by dividing by req_dr --> range [-1, 1] similar to other obs
        :param dr_cutoff: Any data rate above this value will be cut off --> help have obs in same range
        :param sub_req_dr: If true, subtract a UE's required data rate from the achievable dr --> neg obs if too little
        """
        super().__init__(episode_length, map, bs_list, ue_list, **kwargs)
        self.dr_cutoff = dr_cutoff
        self.sub_req_dr = sub_req_dr
        assert not (self.dr_cutoff == 'auto' and not self.sub_req_dr), "For dr_cutoff auto, sub_req_dr must be True."
        # observations: binary vector of BS availability (in range & free cap) + already connected BS
        # 1. Achievable data rate for given UE for all BS --> Box;
        # cut off dr at given dr level. here, dr is below 200 anyways --> default doesn't cut off
        max_dr_req = max([ue.dr_req for ue in self.ue_list])
        # self.log.info('Max dr req', max_dr_req=max_dr_req, dr_cutoff=self.dr_cutoff, sub_req_dr=self.sub_req_dr)
        assert dr_cutoff == 'auto' or max_dr_req < dr_cutoff, "dr_cutoff should be higher than max required dr. by UEs"

        # define observation space
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
        # 2. Connected BS --> MultiBinary
        conn_low = np.zeros(self.num_bs)
        conn_high = np.ones(self.num_bs)
        # Dict space would be most suitable but not supported by stable baselines 2 --> Box
        self.observation_space = gym.spaces.Box(low=np.concatenate([dr_low, conn_low]),
                                                high=np.concatenate([dr_high, conn_high]))
        # same action space as binary env: select a BS to be connected to/disconnect from or noop

    def get_obs(self, ue):
        """Observation: Achievable data rate per BS (processed) + currently connected BS (binary)"""
        if self.dr_cutoff == 'auto':
            # subtract req_dr and auto clip & normalize to [-1, 1]
            bs_dr = []
            for bs in self.bs_list:
                dr_sub = bs.data_rate(ue, self.active_bs) - ue.dr_req
                dr_clip = min(dr_sub, ue.dr_req)        # clipped to range [-dr_req, dr_req]
                dr_norm = dr_clip / ue.dr_req
                bs_dr.append(dr_norm)
        elif self.sub_req_dr:
            # subtract req_dr and cut off at dr_cutoff
            bs_dr = [min(bs.data_rate(ue, self.active_bs) - ue.dr_req, self.dr_cutoff) for bs in self.bs_list]
        else:
            # just cut off at dr_cutoff
            bs_dr = [min(bs.data_rate(ue, self.active_bs), self.dr_cutoff) for bs in self.bs_list]
        connected_bs = [int(bs in ue.conn_bs) for bs in self.bs_list]
        return np.array(bs_dr + connected_bs)


class CentralMultiUserEnv(MobileEnv):
    """
    Env where all UEs move, observe and act at all time steps, controlled by a single central agent.
    Otherwise similar to DatarateMobileEnv with auto dr_cutoff and sub_req_dr.
    """
    def __init__(self, episode_length, map, bs_list, ue_list, **kwargs):
        """Similar to DatarateMobileEnv but with multi-UEs controlled at once and fixed dr_cutoff, sub_req_dr"""
        super().__init__(episode_length, map, bs_list, ue_list, **kwargs)
        # observations: FOR EACH UE: binary vector of BS availability (in range & free cap) + already connected BS
        # 1. Achievable data rate for given UE for all BS (normalized to [-1, 1]) --> Box;
        dr_low = np.full(shape=(self.num_ue * self.num_bs,), fill_value=-1)
        dr_high = np.ones(self.num_ue * self.num_bs)
        # 2. Connected BS --> MultiBinary
        conn_low = np.zeros(self.num_ue * self.num_bs)
        conn_high = np.ones(self.num_ue * self.num_bs)
        # Dict space would be most suitable but not supported by stable baselines 2 --> Box
        self.observation_space = gym.spaces.Box(low=np.concatenate([dr_low, conn_low]),
                                                high=np.concatenate([dr_high, conn_high]))

        # actions: FOR EACH UE: select a BS to be connected to/disconnect from or noop
        self.action_space = gym.spaces.MultiDiscrete([self.num_bs + 1 for _ in range(self.num_ue)])

    def get_obs(self):
        """Observation: Available data rate + connected BS - FOR ALL UEs --> no ue arg"""
        bs_dr = []
        conn_bs = []
        for ue in self.ue_list:
            # subtract req_dr and auto clip & normalize to [-1, 1]
            ue_bs_dr = []
            for bs in self.bs_list:
                dr_sub = bs.data_rate(ue, self.active_bs) - ue.dr_req
                dr_clip = min(dr_sub, ue.dr_req)        # clipped to range [-dr_req, dr_req]
                dr_norm = dr_clip / ue.dr_req
                ue_bs_dr.append(dr_norm)
            bs_dr.extend(ue_bs_dr)
            # connected BS
            ue_conn_bs = [int(bs in ue.conn_bs) for bs in self.bs_list]
            conn_bs.extend(ue_conn_bs)
        return np.array(bs_dr + conn_bs)

    def calc_reward(self, penalty):
        """Calc reward for ALL UEs, similar to normal MobileEnv"""
        reward = penalty
        for ue in self.ue_list:
            reward += super().calc_reward(ue, penalty=0)
        return reward

    def reset(self):
        """Reset environment: Reset all UEs, BS"""
        self.time = 0
        for ue in self.ue_list:
            ue.reset()
        for bs in self.bs_list:
            bs.reset()
        self.obs = self.get_obs()
        return self.obs

    def step(self, action):
        """
        Do 1 time step: Apply action of all UEs and update their position.
        :param action: Array of actions to be applied for each UE
        :return: next observation, reward, done, info
        """
        penalty = 0
        prev_obs = self.obs

        # apply action for each UE; 0 = noop
        for i, ue in enumerate(self.ue_list):
            if action[i] > 0:
                bs = self.bs_list[action[i] - 1]
                # penalty of -3 for unsuccessful connection attempt
                penalty -= 3 * (not ue.connect_to_bs(bs, disconnect=True))

        # move all UEs
        # check connections and reward before and after moving; then avg
        # TODO: usually before & after are the same anyways; so I can drop this if the simulator becomes too slow
        reward_before = self.calc_reward(penalty)
        for ue in self.ue_list:
            ue.move()
        reward_after = self.calc_reward(penalty)

        self.time += 1

        # return next observation, reward, done, info
        self.obs = self.get_obs()
        reward = np.mean([reward_before, reward_after])
        done = self.time >= self.episode_length
        info = {}
        self.log.info("Step", time=self.time, prev_obs=prev_obs, action=action, reward_before=reward_before,
                      reward_after=reward_after, reward=reward, next_obs=self.obs, done=done)
        return self.obs, reward, done, info


class RLlibEnv(DatarateMobileEnv):
    """Wrapper class of the DatarateMobileEnv for RLlib"""
    def __init__(self, env_config):
        """Wrapper env for RLlib, in which all args are in the env_config dict"""
        # FIXME: issues with deepcopying; leads to "AttributeError: 'User' object has no attribute 'id'"

        super().__init__(env_config['episode_length'], env_config['map'], env_config['bs_list'],
                         env_config['ue_list'], env_config['dr_cutoff'], env_config['sub_req_dr'],
                         disable_interference=env_config['disable_interference'])
        super().seed(env_config['seed'])

        # self.log = structlog.getLogger()

        # TODO: try the Gym Dictspace for obs if it's supported by Ray (box for dr, binary for conn)
