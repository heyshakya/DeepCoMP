# example using rllib: https://docs.ray.io/en/latest/rllib.html#running-rllib
# https://docs.ray.io/en/latest/rllib-training.html#basic-python-api
# since rllib doesn't run on Windows, I set up PyCharm to use WSL: https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html#

import numpy as np
import gym
import gym.spaces
import ray
import ray.rllib.agents.ppo as ppo
from ray.tune.logger import pretty_print


# example for a custom env: https://github.com/ray-project/ray/blob/master/rllib/examples/custom_env.py
# start left & go left +1, go right until end of tunnel: +100; anything else: 0
# rather than just optimizing short-term reward (going left), the agent should learn to opitmize long-term rward (right)
class TunnelEnv(gym.Env):
    # must take a singe arg "env_config" that's a dict
    def __init__(self, env_config):
        self.len_tunnel = env_config['len_tunnel']
        self.pos = 0
        self.len_episode = env_config['len_episode']
        self.time = 0
        # actions: left & right
        self.action_space = gym.spaces.Discrete(2)
        # observation: pos in the tunnel (starting left at pos 0)
        self.observation_space = gym.spaces.Discrete(self.len_tunnel)

    def reset(self):
        self.pos = 0
        self.time = 0
        return self.pos

    def step(self, action):
        self.time += 1
        reward = 0
        # left
        if action == 0:
            # at starting pos: +1 reward, but don't move
            if self.pos == 0:
                reward = 1
            else:
                self.pos -= 1
        # right
        else:
            self.pos += 1
            # reached the right end: +100 & reset to start
            if self.pos >= self.len_tunnel - 1:
                reward = 100
                self.pos = 0

        # return obs, reward, done, info as usual
        done = self.time >= self.len_episode
        print(f"{self.time=}, {self.pos=}, {reward=}, {done=}")
        return self.pos, reward, done, {}


ray.init()

# env config
env_config = {'len_tunnel': 5, 'len_episode': 10}
# ray config
config = ppo.DEFAULT_CONFIG.copy()
config["num_gpus"] = 0
config["num_workers"] = 1
config["eager"] = False
config['env_config'] = env_config


# train on custom env
trainer = ppo.PPOTrainer(config=config, env=TunnelEnv)

for i in range(1):
    result = trainer.train()
    print(pretty_print(result))


# train on cartpole
# trainer = ppo.PPOTrainer(config=config, env="CartPole-v0")

# Can optionally call trainer.restore(path) to load a checkpoint.
# 10-20 training iterations (!= episodes) should be enough for optimal reward
# for i in range(10):
#    # Perform one iteration of training the policy with PPO
#    result = trainer.train()
#    print(pretty_print(result))
#
#    if i % 100 == 0:
#        checkpoint = trainer.save()
#        print("checkpoint saved at", checkpoint)

# Also, in case you have trained a model outside of ray/RLlib and have created
# an h5-file with weight values in it, e.g.
# my_keras_model_trained_outside_rllib.save_weights("model.h5")
# (see: https://keras.io/models/about-keras-models/)

# ... you can load the h5-weights into your Trainer's Policy's ModelV2
# (tf or torch) by doing:
# trainer.import_model("my_weights.h5")
# NOTE: In order for this to work, your (custom) model needs to implement
# the `import_from_h5` method.
# See https://github.com/ray-project/ray/blob/master/rllib/tests/test_model_imports.py
# for detailed examples for tf- and torch trainers/models.
