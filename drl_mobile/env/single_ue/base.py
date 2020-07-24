"""Base mobile environment. Implemented and extended by sublcasses."""
import random
import logging

import gym
import gym.spaces
import structlog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.patheffects as pe

from drl_mobile.util.logs import config_logging
from drl_mobile.env.util.utility import step_utility, log_utility


class MobileEnv(gym.Env):
    """
    Base environment class with moving UEs and stationary BS on a map. RLlib and OpenAI Gym-compatible.
    No observation or action space implemented. This needs to be done in subclasses.
    """
    metadata = {'render.modes': ['human']}

    def __init__(self, env_config):
        """
        Create a new environment object with an OpenAI Gym interface. Required fields in the env_config:

        * episode_length: Total number of simulation time steps in one episode
        * map: Map object representing the playground
        * bs_list: List of base station objects in the environment
        * ue_list: List of UE objects in the environment
        * seed: Seed for the RNG; for reproducibility. May be None.

        :param env_config: Dict containing all configuration options for the environment. Required by RLlib.
        """
        super(gym.Env, self).__init__()
        self.time = 0
        self.episode_length = env_config['episode_length']
        self.map = env_config['map']
        self.bs_list = env_config['bs_list']
        self.ue_list = env_config['ue_list']
        # seed the environment
        self.seed(env_config['seed'])

        # current observation
        self.obs = None
        # observation and action space are defined in the subclass --> different variants
        self.observation_space = None
        self.action_space = None

        # configure logging inside env to ensure it works in ray/rllib. https://github.com/ray-project/ray/issues/9030
        config_logging()
        self.log = structlog.get_logger()
        self.log.info('Env init', env_config=env_config)

    @property
    def num_bs(self):
        return len(self.bs_list)

    @property
    def num_ue(self):
        return len(self.ue_list)

    @property
    def total_dr(self):
        return sum([ue.curr_dr for ue in self.ue_list])

    @property
    def total_utility(self):
        return sum([ue.utility for ue in self.ue_list])

    def seed(self, seed=None):
        random.seed(seed)

    def set_log_level(self, log_dict):
        """
        Set a logging levels for a set of given logger. Needs to happen here, inside the env, for RLlib workers to work.
        :param dict log_dict: Dict with logger name --> logging level (eg, logging.INFO)
        """
        for logger_name, level in log_dict.items():
            logging.getLogger(logger_name).setLevel(level)

    def get_ue_obs(self, ue):
        """Return the an observation of the current world for a given UE"""
        raise NotImplementedError('Implement in subclass')

    def calc_reward(self, ue, penalty):
        """
        Calculate and return reward for specific UE: The UE's utility (based on its data rate) + penalty
        """
        # return ue.utility + penalty
        # normalize rewards to [-1,1] (clip first to avoid rewards < -20 due to penalties)
        # return np.clip(ue.utility + penalty, -20, 20) / 20

        # clip utility to -20, 20 to avoid -inf for 0 dr and cap at 100 dr
        clip_util = np.clip(ue.utility, -20, 20)
        # add a penalty for concurrent connections (overhead for joint transmission), ie, for any 2+ connections
        # tunable penalty weight representing the cost of concurrent connections
        weight = 0
        connections = len(ue.bs_dr)
        if connections > 1:
            penalty += weight * (connections - 1)
        # clip again to stay in range -20, 20
        return np.clip(clip_util + penalty, -20, 20)

    def reset(self):
        """Reset environment by resetting time and all UEs (pos & movement) and their connections"""
        self.time = 0
        for ue in self.ue_list:
            ue.reset()
        for bs in self.bs_list:
            bs.reset()
        return self.get_obs()

    def apply_ue_actions(self, action):
        """
        Apply actions of UEs. In this base case, just of one UE (selected based on current time).
        In extended env version, apply actions of all UEs.

        :param: Action to be applied (here: for a single UE)
        :return: Dict of num. unsuccessful connections attempts for each UE (at most one per UE)
        """
        assert self.action_space.contains(action), f"Action {action} does not fit action space {self.action_space}"
        unsucc_conn = {ue: 0 for ue in self.ue_list}
        # select active UE (to update in this step) using round robin
        ue = self.ue_list[self.time % self.num_ue]

        # apply action: try to connect to BS; or: 0 = no op
        if action > 0:
            bs = self.bs_list[action-1]
            unsucc_conn[ue] = not ue.connect_to_bs(bs, disconnect=True)

        return unsucc_conn

    def update_ue_drs_rewards(self, penalties, update_only=False):
        """
        Update cached data rates of all UE-BS connections.
        Calculate and return corresponding rewards based on given penalties.

        :param penalties: Dict of penalties for all UEs. Used for calculating rewards.
        :return: Dict of rewards: UE --> reward (incl. penalty)
        """
        rewards = dict()
        for ue in self.ue_list:
            ue.update_curr_dr()
            # calc and return reward if needed
            if update_only:
                # only update drs and return reward 0
                rewards[ue] = 0
            else:
                if penalties is None or ue not in penalties.keys():
                    rewards[ue] = self.calc_reward(ue, penalty=0)
                else:
                    rewards[ue] = self.calc_reward(ue, penalties[ue])
        return rewards

    def move_ues(self):
        """
        Move all UEs and return dict of penalties corresponding to number of lost connections.

        :return: Dict with num lost connections: UE --> num. lost connections
        """
        lost_conn = dict()
        for ue in self.ue_list:
            num_lost_conn = ue.move()
            # add penalty of -1 for each lost connection through movement (rather than actively disconnected)
            lost_conn[ue] = num_lost_conn
        return lost_conn

    def get_obs(self):
        """
        Return the current observation. Called to get the next observation after a step.
        Here, the obs for the next UE. Overwritten by env vars as needed.

        :returns: Next observation
        """
        next_ue = self.ue_list[self.time % self.num_ue]
        return self.get_ue_obs(next_ue)

    def step_reward(self, rewards):
        """
        Return the overall reward for the step (called at the end of a step). Overwritten by variants.

        :param rewards: Dict of avg rewards per UE (before and after movement)
        :returns: Reward for the step (depends on the env variant; here just for one UE)
        """
        # here: get reward for UE that applied the action (at time - 1)
        ue = self.ue_list[(self.time-1) % self.num_ue]
        return rewards[ue]

    def done(self):
        """
        Return whether the episode is done.

        :return: Whether the current episode is done or not
        """
        return self.time >= self.episode_length

    def info(self, unsucc_conn, lost_conn):
        """Return info dict that's returned after a step. Includes info about unsuccessful and lost connections."""
        info_dict = {
            'time': self.time,
            'dr': {ue: ue.curr_dr for ue in self.ue_list},
            'utility': {ue: ue.utility for ue in self.ue_list},
            'unsucc_conn': unsucc_conn,
            'lost_conn': lost_conn,
            # num UEs without any connection
            'num_ues_wo_conn': sum([1 if len(ue.bs_dr) == 0 else 0 for ue in self.ue_list])
        }
        return info_dict

    def step(self, action):
        """
        Environment step consisting of 1) Applying actions, 2) Updating data rates and rewards, 3) Moving UEs,
        4) Updating data rates and rewards again (avg with reward before), 5) Updating the observation

        In the base env here, only one UE applies actions per time step. This is overwritten in other env variants.

        :param action: Action to be applied. Here, for a single UE. In other env variants, for all UEs.
        :return: Tuple of next observation, reward, done, info
        """
        prev_obs = self.obs

        # perform step: apply action, move UEs, update data rates and rewards in between; increment time
        unsucc_conn = self.apply_ue_actions(action)
        # penalty of -1 for unsuccessful connection attempt
        # penalties = {ue: -1 * unsucc_conn[ue] for ue in self.ue_list}
        rewards_before = self.update_ue_drs_rewards(penalties=None)
        lost_conn = self.move_ues()
        # penalty of -1 for lost connections due to movement (rather than active disconnect)
        # penalties = {ue: -1 * lost_conn[ue] for ue in self.ue_list}
        # update of drs is needed even if we don't need the reward
        rewards_after = self.update_ue_drs_rewards(penalties=None, update_only=True)
        # rewards = {ue: np.mean([rewards_before[ue], rewards_after[ue]]) for ue in self.ue_list}
        rewards = rewards_before
        self.time += 1

        # get and return next obs, reward, done, info
        self.obs = self.get_obs()
        reward = self.step_reward(rewards)
        done = self.done()
        info = self.info(unsucc_conn, lost_conn)
        self.log.info("Step", time=self.time, prev_obs=prev_obs, action=action, reward=reward, next_obs=self.obs,
                      done=done)
        return self.obs, reward, done, info

    def render(self, mode='human'):
        """Plot and visualize the current status of the world. Return the patch of actors for animation."""
        # list of matplotlib "artists", which can be used to create animations
        patch = []

        # limit to map borders
        plt.xlim(0, self.map.width)
        plt.ylim(0, self.map.height)

        # users & connections
        # show utility as red to yellow to green. use color map for [0,1) --> normalize utility first
        colormap = cm.get_cmap('RdYlGn')
        norm = plt.Normalize(-20, 20)

        for ue in self.ue_list:
            # plot connections to all BS
            for bs, dr in ue.bs_dr.items():
                color = colormap(norm(log_utility(dr)))
                # add black background/borders for lines to make them better visible if the utility color is too light
                patch.extend(plt.plot([ue.pos.x, bs.pos.x], [ue.pos.y, bs.pos.y], color=color,
                                      path_effects=[pe.SimpleLineShadow(shadow_color='black'), pe.Normal()]))
                                      # path_effects=[pe.Stroke(linewidth=2, foreground='black'), pe.Normal()]))
            # plot UE
            patch.extend(ue.plot())

        # base stations
        for bs in self.bs_list:
            patch.extend(bs.plot())

        # title isn't redrawn in animation (out of box) --> static --> show time as text inside box, top-right corner
        patch.append(plt.title(type(self).__name__))
        # extra info: time step, total data rate & utility
        patch.append(plt.text(0.9*self.map.width, 0.95*self.map.height, f"t={self.time}"))
        patch.append(plt.text(0.9*self.map.width, 0.9*self.map.height, f"dr={self.total_dr:.2f}"))
        patch.append(plt.text(0.9*self.map.width, 0.85*self.map.height, f"util={self.total_utility:.2f}"))

        # legend doesn't change --> only draw once at the beginning
        # if self.time == 0:
        #     plt.legend(loc='upper left')
        return patch
