```
abhishek@abhishek-pc:~$ deepcomp -h
usage: deepcomp [-h] [--approach {deepcomp,ddcomp,d3comp}] [--agent {central,multi,single}] [--alg {brute-force,ppo,fixed,random,3gpp,fullcomp,dynamic,static}]
                [--epsilon EPSILON] [--cluster-size CLUSTER_SIZE] [--workers WORKERS] [--batch-size BATCH_SIZE] [--train-steps TRAIN_STEPS] [--train-iter TRAIN_ITER]
                [--target-reward TARGET_REWARD] [--target-utility TARGET_UTILITY] [--continue CONTINUE] [--separate-agent-nns] [--lstm] [--reward {sum,min,avg}]
                [--cluster] [--env {custom,medium,large,small}] [--num-bs NUM_BS] [--bs-dist BS_DIST] [--eps-length EPS_LENGTH] [--max-ues MAX_UES]
                [--static-ues STATIC_UES] [--slow-ues SLOW_UES] [--fast-ues FAST_UES] [--new-ue-interval NEW_UE_INTERVAL]
                [--ue-arrival {None,3up2down,largeupdown,updownupdown,updown,oneupdown}] [--sharing {proportional-fair,rate-fair,max-cap,mixed,resource-fair}]
                [--util {log,linear,step}] [--rand-train] [--cont-train] [--rand-test] [--fixed-rand-eval] [--test TEST] [--video {both,gif,html,None}] [--dashboard]
                [--ue-details] [--eval EVAL] [--seed SEED] [--result-dir RESULT_DIR] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  --approach {deepcomp,ddcomp,d3comp}
                        Which DRL approach to use: DeepCoMP, DD-CoMP, or D3-CoMP. Overrides --agent, --alg, and --separate-agent-nns. (default: None)
  --agent {central,multi,single}
                        Whether to use a single agent for 1 UE, a central agent, or multi agents (default: central)
  --alg {brute-force,ppo,fixed,random,3gpp,fullcomp,dynamic,static}
                        Algorithm (default: ppo)
  --epsilon EPSILON     Scaling factor for dynamic heuristic. (default: None)
  --cluster-size CLUSTER_SIZE
                        Cluster size for static clustering heuristic (1-3). (default: None)
  --workers WORKERS     Number of workers for training (one per CPU core) (default: 1)
  --batch-size BATCH_SIZE
                        Number of training iterations per training batch (default: 4000)
  --train-steps TRAIN_STEPS
                        Max. number of training time steps (if any) (default: None)
  --train-iter TRAIN_ITER
                        Max. number of training iterations (if any) (default: None)
  --target-reward TARGET_REWARD
                        Target mean episode reward for training (default: None)
  --target-utility TARGET_UTILITY
                        Target mean sum utility for training (default: None)
  --continue CONTINUE   Continue training agent at given path (loads last checkpoint (default: None)
  --separate-agent-nns  Only relevant for multi-agent RL. Use separate NNs for each agent instead of sharing. (default: False)
  --lstm                Whether or not to use an LSTM cell (default: False)
  --reward {sum,min,avg}
                        How to aggregate rewards from multiple UEs within a step. (default: avg)
  --cluster             Set this flag when running on a multi-node cluster. (default: False)
  --env {custom,medium,large,small}
                        Env/Map size (default: custom)
  --num-bs NUM_BS       Number of BS in large env (not supported by others). (default: None)
  --bs-dist BS_DIST     Distance between BS. Only supported by medium env. (default: 100)
  --eps-length EPS_LENGTH
                        Number of time steps per episode (default: 100)
  --max-ues MAX_UES     Expected max. number of UEs. Relevant for central agent's NN size. Derived automatically if not set. (default: None)
  --static-ues STATIC_UES
                        Number of static UEs in the environment (default: 0)
  --slow-ues SLOW_UES, --ues SLOW_UES
                        Number of (slow) UEs in the environment (default: 0)
  --fast-ues FAST_UES   Number of fast UEs in the environment (default: 0)
  --new-ue-interval NEW_UE_INTERVAL
                        Interval in number of steps after which a new UEs enter the environment periodically. (default: None)
  --ue-arrival {None,3up2down,largeupdown,updownupdown,updown,oneupdown}
                        UE arrival sequence (default: None)
  --sharing {proportional-fair,rate-fair,max-cap,mixed,resource-fair}
                        Sharing model used by BS to split resources and/or rate among connected UEs. (default: mixed)
  --util {log,linear,step}
                        UEs' utility function (default: log)
  --rand-train          Randomize training episodes. (default: False)
  --cont-train          Continuous training without resetting. (default: False)
  --rand-test           Randomize testing and evaluation episodes. (default: False)
  --fixed-rand-eval     Evaluate once with fixed episodes and then again with random episodes. (default: False)
  --test TEST           Test trained agent at given path (auto. loads last checkpoint) (default: None)
  --video {both,gif,html,None}
                        How (and whether) to render the testing video. (default: html)
  --dashboard           Render video in form of a dashboard (slow). (default: False)
  --ue-details          Show UEs' data rate and util in rendered video. (default: False)
  --eval EVAL           Number of evaluation episodes after testing (default: 0)
  --seed SEED           Seed for the RNG (algorithms and environment) (default: None)
  --result-dir RESULT_DIR
                        Optional path to where results should be stored.Default: <project_root>/results (default: None)
  --debug               Run in debug mode for use with a debugger. (default: False)
abhishek@abhishek-pc:~$ 
```




