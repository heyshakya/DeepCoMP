# deep-rl-mobility-management

Simple simulation of mobility management scenario to use with deep RL

![example](docs/gifs/v02.gif)

## Setup

Should work with Python 3.6+. Tested with Python 3.7. 
Tensorflow 1 doesn't work on Python 3.8 but is required by stable_baselines.

```
pip install -r requirements
```

For saving gifs, you also need to install [ImageMagick](https://imagemagick.org/index.php).

## Usage

Adjust and run `main.py` in `drl_mobile`:

```
cd drl_mobile
python main.py
```

## Todos

* Update reward calc to check connection at beginning and end of time step; not just beginning
* Eval with UE moving at different random speeds (fast, slow). Any impact on connections?
    * Data rate should help make the decision when to connect to new BS
    * Penalty for connecting to multiple BS?
* Multiple UEs: Test & debug; try adding ID of UE to which obs refers inside obs; or just obs of all UEs
* Add schedules/RBs to radio model as capacity? Once I consider multiple UEs
* As soon as centralized works: Move to distributed RL. Even before adding offloading.

## Findings

* Binary observations: [BS available?, BS connected?] work very well
* Replacing binary "BS available?" with achievable data rate by BS does not work at all
* Probably, because data rate is magnitudes larger (up to 150x) than "BS connected?" --> agent becomes blind to 2nd part of obs
* Just cutting the data rate off at some small value (eg, 3 Mbit/s) leads to much better results
* Agent keeps trying to connect to all BS, even if out of range. --> Subtracting req. dr by UE + higher penalty (both!) solves the issue
* Normalizing loses info about which BS has enough dr and connectivity --> does not work as well
