# DeepCoMP: Self-Learning Dynamic Multi-Cell Selection for Coordinated Multipoint (CoMP)

Deep reinforcement learning for dynamic multi-cell selection in CoMP scenarios.
Three variants: DeepCoMP (central agent), DD-CoMP (distributed agents using central policy), D3-CoMP (distributed agents with separate policies).

![example](https://github.com/CN-UPB/DeepCoMP/raw/master/docs/gifs/v10.gif)


## Setup

You need Python 3.8+.

### Simple Installation via PyPi

```
pip install deepcomp
```

### Manual Installation from Source

Clone the repository. Then install everything, following these steps:

```
# only on ubuntu
sudo apt update
sudo apt upgrade
sudo apt install cmake build-essential zlib1g-dev python3-dev

# install rllib manually up front
# details: https://github.com/ray-project/ray/issues/11274 (also, v1.1 throws an error with Python lists)
pip install ray[rllib]==1
# also install numpy 1.19.5 manually; since 1.20 leads to errors with TF 2.2
pip install numpy==1.19.5

# complete installation of remaining dependencies
python setup.py install
```

Tested on Ubuntu 20.04 and Windows 10 with Python 3.8.

For saving videos and gifs, you also need to install ffmpeg (not on Windows) and [ImageMagick](https://imagemagick.org/index.php). 
On Ubuntu:

```
sudo apt install ffmpeg imagemagick
```


## Usage

```
# get an overview of all options
deepcomp -h
```

For example: 

```
deepcomp --env medium --slow-ues 3 --agent central --workers 2 --train-steps 50000 --seed 42 --video both
```

To run DeepCoMP, use `--alg ppo --agent central`.
For DD-CoMP, use `--alg ppo --agent multi`, and for D3-CoMP, use `--alg ppo --agent multi --separate-agent-nns`.

Training logs, results, videos, and trained agents are saved in the `results` directory.

#### Accessing results remotely

When running remotely, you can serve the replay video by running:

```
cd results
python -m http.server
```

Then access at `<remote-ip>:8000`.

#### Tensorboard

To view learning curves (and other metrics) when training an agent, use Tensorboard:

```
tensorboard --logdir results/PPO/ (--host 0.0.0.0)
```

Tensorboard is available at http://localhost:6006


## Documentation

API documentation is on [https://cn-upb.github.io/DeepCoMP/](https://cn-upb.github.io/DeepCoMP/).

Documentation is generated based on docstrings using [pdoc3](https://pdoc3.github.io/pdoc/):

```
# from project root
pip install pdoc3
pdoc --force --html --output-dir docs deepcomp
# move files to be picked up by GitHub pages
mv docs/deepcomp/ docs/
# then manually adjust index.html to link to GitHub repo
```

## Contribution

Development: [@stefanbschneider](https://github.com/stefanbschneider/)

Feature requests, questions, issues, and pull requests via GitHub are welcome.
