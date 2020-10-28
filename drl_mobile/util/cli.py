import argparse

import structlog

from drl_mobile.util.constants import SUPPORTED_ALGS, SUPPORTED_ENVS, SUPPORTED_AGENTS, SUPPORTED_RENDER, \
    SUPPORTED_SHARING


log = structlog.get_logger()


def setup_cli():
    """Create CLI parser and return parsed args"""
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # required args
    parser.add_argument('--agent', type=str, choices=SUPPORTED_AGENTS, required=True,
                        help="Whether to use a single agent for 1 UE, a central agent, or multi agents")
    # algorithm & training
    parser.add_argument('--alg', type=str, choices=SUPPORTED_ALGS, default='ppo', help="Algorithm")
    parser.add_argument('--workers', type=int, default=1, help="Number of workers for RLlib training and evaluation")
    parser.add_argument('--batch-size', type=int, default=4000, help="Number of training iterations per training batch")
    parser.add_argument('--train-steps', type=int, default=None, help="Max. number of training time steps (if any)")
    parser.add_argument('--train-iter', type=int, default=None, help="Max. number of training iterations (if any)")
    parser.add_argument('--target-reward', type=int, default=None, help="Target mean episode reward for training")
    parser.add_argument('--target-utility', type=int, default=None, help="Target mean sum utility for training")
    parser.add_argument('--continue', type=str, help="Continue training agent at given path (loads last checkpoint")
    parser.add_argument('--separate-agent-nns', action='store_true',
                        help="Only relevant for multi-agent RL. Use separate NNs for each agent instead of sharing.")
    parser.add_argument('--lstm', action='store_true', help="Whether or not to use an LSTM cell")
    # environment
    parser.add_argument('--env', type=str, choices=SUPPORTED_ENVS, default='small', help="Env/Map size")
    parser.add_argument('--bs-dist', type=int, default=100, help="Distance between BS. Only supported by medium env.")
    parser.add_argument('--eps-length', type=int, default=100, help="Number of time steps per episode")
    parser.add_argument('--static-ues', type=int, default=0, help="Number of static UEs in the environment")
    parser.add_argument('--slow-ues', type=int, default=0, help="Number of slow UEs in the environment")
    parser.add_argument('--fast-ues', type=int, default=0, help="Number of fast UEs in the environment")
    # could implement this simply by processing the number and increasing the static, slow, fast UEs correspondingly
    # before passing to env creation
    # parser.add_argument('--mixed-ues', type=int, default=0,
    #                     help="Number of UEs in the environment, equally mixed between different movement speeds")
    parser.add_argument('--new-ue-interval', type=int, default=None,
                        help="Interval in number of steps after which a new UEs enter the environment periodically.")
    parser.add_argument('--sharing', type=str, choices=SUPPORTED_SHARING, default='resource-fair',
                        help="Sharing model used by BS to split resources and/or rate among connected UEs.")
    # evaluation
    parser.add_argument('--rand-train', action='store_true', help="Randomize training episodes.")
    parser.add_argument('--cont-train', action='store_true', help="Continuous training without resetting.")
    parser.add_argument('--rand-test', action='store_true', help="Randomize testing and evaluation episodes.")
    parser.add_argument('--fixed-rand-eval', action='store_true',
                        help="Evaluate once with fixed episodes and then again with random episodes.")
    parser.add_argument('--test', type=str, help="Test trained agent at given path (auto. loads last checkpoint)")
    parser.add_argument('--video', type=str, choices=SUPPORTED_RENDER, default=None,
                        help="How (and whether) to render the testing video.")
    parser.add_argument('--eval', type=int, default=0, help="Number of evaluation episodes after testing")
    parser.add_argument('--seed', type=int, default=None, help="Seed for the RNG (algorithms and environment)")

    args = parser.parse_args()
    log.info('CLI args', args=args)

    assert getattr(args, 'continue') is None or args.test is None, "Use either --continue or --test, not both."
    assert args.rand_test is False or args.fixed_rand_eval is False, "Use either --rand-test or --fixed-rand-eval."
    assert not (args.cont_train and args.rand_train), "Either train continuously or with random episodes."
    return args
