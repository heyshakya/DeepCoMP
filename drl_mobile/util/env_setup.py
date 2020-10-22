"""Utility module for setting up different envs"""
import numpy as np
from shapely.geometry import Point
from ray.rllib.agents.ppo import DEFAULT_CONFIG
from ray.rllib.env.multi_agent_env import MultiAgentEnv

from drl_mobile.util.constants import SUPPORTED_ENVS, SUPPORTED_AGENTS
from drl_mobile.env.single_ue.variants import BinaryMobileEnv, DatarateMobileEnv, NormDrMobileEnv, RelNormEnv
from drl_mobile.env.multi_ue.central import CentralDrEnv, CentralNormDrEnv, CentralRelNormEnv
from drl_mobile.env.multi_ue.multi_agent import MultiAgentMobileEnv, SeqMultiAgentMobileEnv
from drl_mobile.env.entities.user import User
from drl_mobile.env.entities.station import Basestation
from drl_mobile.env.entities.map import Map
from drl_mobile.env.util.movement import UniformMovement, RandomWaypoint
from drl_mobile.util.callbacks import CustomMetricCallbacks


def get_env_class(env_type):
    """Return the env class corresponding to the string type (from CLI)"""
    assert env_type in SUPPORTED_AGENTS, f"Environment type was {env_type} but has to be one of {SUPPORTED_AGENTS}."

    if env_type == 'single':
        # return DatarateMobileEnv
        # return NormDrMobileEnv
        return RelNormEnv
    if env_type == 'central':
        # return CentralDrEnv
        # return CentralNormDrEnv
        return CentralRelNormEnv
    if env_type == 'multi':
        return MultiAgentMobileEnv


def create_small_map(sharing_model):
    """
    Create small map and 2 BS

    :returns: tuple (map, bs_list)
    """
    map = Map(width=150, height=100)
    bs1 = Basestation('A', Point(50, 50), sharing_model)
    bs2 = Basestation('B', Point(100, 50), sharing_model)
    bs_list = [bs1, bs2]
    return map, bs_list


def create_dyn_small_map(sharing_model, bs_dist=100, dist_to_border=10):
    """Small env with 2 BS and dynamic distance in between"""
    map = Map(width=2 * dist_to_border + bs_dist, height=2 * dist_to_border)
    bs1 = Basestation('A', Point(dist_to_border, dist_to_border), sharing_model)
    bs2 = Basestation('B', Point(dist_to_border + bs_dist, dist_to_border), sharing_model)
    return map, [bs1, bs2]


def create_medium_map(sharing_model):
    """
    Deprecated: Use dynamic medium env instead. Kept this to reproduce earlier results.
    Same as large env, but with map restricted to areas with coverage.
    Thus, optimal episode reward should be close to num_ues * eps_length * 10 (ie, all UEs are always connected)
    """
    map = Map(width=205, height=85)
    bs1 = Basestation('A', Point(45, 35), sharing_model)
    bs2 = Basestation('B', Point(160, 35), sharing_model)
    bs3 = Basestation('C', Point(100, 85), sharing_model)
    bs_list = [bs1, bs2, bs3]
    return map, bs_list


def create_dyn_medium_map(sharing_model, bs_dist=100, dist_to_border=10):
    """
    Create map with 3 BS at equal distance. Distance can be varied dynamically. Map is sized automatically.
    Keep the same layout as old medium env here: A, B on same horizontal axis. C above in the middle
    """
    # calculate vertical distance from A, B to C using Pythagoras
    y_dist = np.sqrt(bs_dist ** 2 - (bs_dist / 2) ** 2)
    # derive map size from BS distance and distance to border
    map_width = 2 * dist_to_border + bs_dist
    map_height = 2 * dist_to_border + y_dist

    map = Map(width=map_width, height=map_height)
    # BS A is located at bottom left corner with specified distance to border
    bs1 = Basestation('A', Point(dist_to_border, dist_to_border), sharing_model)
    # other BS positions are derived accordingly
    bs2 = Basestation('B', Point(dist_to_border + bs_dist, dist_to_border), sharing_model)
    bs3 = Basestation('C', Point(dist_to_border + (bs_dist / 2), dist_to_border + y_dist), sharing_model)
    return map, [bs1, bs2, bs3]


def create_large_map(sharing_model):
    """
    Create larger map with 7 BS that are arranged in a typical hexagonal structure.

    :returns: Tuple(map, bs_list)
    """
    map = Map(width=230, height=260)
    bs_list = [
        # center
        Basestation('A', Point(115, 130), sharing_model),
        # top left, counter-clockwise
        Basestation('B', Point(30, 80), sharing_model),
        Basestation('C', Point(115, 30), sharing_model),
        Basestation('D', Point(200, 80), sharing_model),
        Basestation('E', Point(200, 180), sharing_model),
        Basestation('F', Point(115, 230), sharing_model),
        Basestation('G', Point(30, 180), sharing_model),
    ]

    return map, bs_list


def create_ues(map, num_static_ues, num_slow_ues, num_fast_ues):
    """Create custom number of slow/fast UEs on the given map. Return UE list"""
    ue_list = []
    id = 1
    for i in range(num_static_ues):
        ue_list.append(User(str(id), map, pos_x='random', pos_y='random', movement=RandomWaypoint(map, velocity=0)))
        id += 1
    for i in range(num_slow_ues):
        ue_list.append(User(str(id), map, pos_x='random', pos_y='random', movement=RandomWaypoint(map, velocity='slow')))
        id += 1
    for i in range(num_fast_ues):
        ue_list.append(User(str(id), map, pos_x='random', pos_y='random', movement=RandomWaypoint(map, velocity='fast')))
        id += 1
    return ue_list


def create_custom_env(sharing_model):
    """Hand-created custom env. For demos or specific experiments."""
    map, bs_list = create_small_map(sharing_model)
    # 2 stationary UEs
    ue_list = [
        User(str(1), map, pos_x=70, pos_y=40, movement=UniformMovement(map)),
        User(str(2), map, pos_x=80, pos_y=60, movement=UniformMovement(map))
    ]
    return map, ue_list, bs_list


def get_env(map_size, bs_dist, num_static_ues, num_slow_ues, num_fast_ues, sharing_model):
    """Create and return the environment corresponding to the given map_size"""
    assert map_size in SUPPORTED_ENVS, f"Environment {map_size} is not one of {SUPPORTED_ENVS}."

    # create map and BS list
    map, bs_list = None, None
    if map_size == 'small':
        map, bs_list = create_small_map(sharing_model)
    elif map_size == 'medium':
        map, bs_list = create_dyn_medium_map(sharing_model, bs_dist=bs_dist)
    elif map_size == 'large':
        map, bs_list = create_large_map(sharing_model)
    # custom env also defines UEs --> return directly
    elif map_size == 'custom':
        return create_custom_env(sharing_model)

    # create UEs
    ue_list = create_ues(map, num_static_ues, num_slow_ues, num_fast_ues)

    return map, ue_list, bs_list


def create_env_config(agent, map_size, bs_dist, num_static_ues, num_slow_ues, num_fast_ues, sharing_model, eps_length,
                      num_workers=1, train_batch_size=1000, seed=None, agents_share_nn=True, use_lstm=False):
    """
    Create environment and RLlib config. Return config.

    :param agent: String indicating which environment version to use based on the agent type
    :param map_size: Size of the environment (as string)
    :param bs_dist: Distance between BS
    :param num_static_ues: Number of slow UEs in the env
    :param num_slow_ues: Number of slow UEs in the env
    :param num_fast_ues: Number of fast UEs in the env
    :param sharing_model: Sharing model used by the BS
    :param eps_length: Number of time steps per episode (parameter of the environment)
    :param num_workers: Number of RLlib workers for training. For longer training, num_workers = cpu_cores-1 makes sense
    :param train_batch_size: Number of sampled env steps in a single training iteration
    :param seed: Seed for reproducible results
    :param agents_share_nn: Whether all agents in a multi-agent env should share the same NN or have separate copies
    :return: The complete config for an RLlib agent, including the env & env_config
    """
    env_class = get_env_class(agent)
    map, ue_list, bs_list = get_env(map_size, bs_dist, num_static_ues, num_slow_ues, num_fast_ues, sharing_model)

    # this is for DrEnv and step utility
    # env_config = {
    #     'episode_length': eps_length, 'seed': seed,
    #     'map': map, 'bs_list': bs_list, 'ue_list': ue_list, 'dr_cutoff': 'auto', 'sub_req_dr': True,
    #     'curr_dr_obs': False, 'ues_at_bs_obs': False, 'dist_obs': False, 'next_dist_obs': False
    # }
    # this is for the custom NormEnv and log utility
    env_config = {
        'episode_length': eps_length, 'seed': seed, 'map': map, 'bs_list': bs_list, 'ue_list': ue_list,
        # if enabled log_metrics: log metrics even during training --> visible on tensorboard
        # if disabled: log just during testing --> probably slightly faster training with less memory
        'log_metrics': True
    }

    # create and return the config
    config = DEFAULT_CONFIG.copy()
    # 0 = no workers/actors at all --> low overhead for short debugging; 2+ workers to accelerate long training
    config['num_workers'] = num_workers
    config['seed'] = seed
    # write training stats to file under ~/ray_results (default: False)
    config['monitor'] = True
    config['train_batch_size'] = train_batch_size        # default: 4000; default in stable_baselines: 128
    # auto normalize obserations by subtracting mean and dividing by std (default: "NoFilter")
    # config['observation_filter'] = "MeanStdFilter"
    # NN settings: https://docs.ray.io/en/latest/rllib-models.html#built-in-model-parameters
    # configure the size of the neural network's hidden layers
    # config['model']['fcnet_hiddens'] = [100, 100]
    # LSTM settings
    config['model']['use_lstm'] = use_lstm
    # config['model']['lstm_use_prev_action_reward'] = True
    # config['log_level'] = 'INFO'    # ray logging default: warning
    config['env'] = env_class
    config['env_config'] = env_config
    # callback for monitoring custom metrics
    config['callbacks'] = CustomMetricCallbacks

    # for multi-agent env: https://docs.ray.io/en/latest/rllib-env.html#multi-agent-and-hierarchical
    if MultiAgentEnv in env_class.__mro__:
        # instantiate env to access obs and action space
        env = env_class(env_config)

        # all UEs use the same policy and NN
        if agents_share_nn:
            config['multiagent'] = {
                'policies': {'ue': (None, env.observation_space, env.action_space, {})},
                'policy_mapping_fn': lambda agent_id: 'ue'
            }
        # or: use separate policies (and NNs) for each agent
        else:
            config['multiagent'] = {
                # attention: ue.id needs to be a string! just casting it to str() here doesn't work;
                # needs to be consistent with obs keys --> easier, just use string IDs
                'policies': {ue.id: (None, env.observation_space, env.action_space, {}) for ue in ue_list},
                'policy_mapping_fn': lambda agent_id: agent_id
            }

    return config

