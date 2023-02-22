```
abhishek@abhishek-pc:~$ deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent central --workers 2 --dashboard --ue-details --eval 100 --train-steps 200000 --seed 42 --video both --result-dir /home/abhishek/cmc/result/DeepCoMP/good
2022-04-27 08:31:21,313	WARNING deprecation.py:33 -- DeprecationWarning: `monitor` has been deprecated. Use `record_env` instead. This will raise an error in the future!
== Status ==
Memory usage on this node: 3.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 PENDING)
+-----------------------------------+----------+-------+
| Trial name                        | status   | loc   |
|-----------------------------------+----------+-------|
| PPO_CentralRelNormEnv_50e5a_00000 | PENDING  |       |
+-----------------------------------+----------+-------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 4000
  custom_metrics:
    eps_sum_utility_max: -4604.335940579162
    eps_sum_utility_mean: -6109.31196109895
    eps_sum_utility_min: -7762.497251023287
    sum_utility_max: -9.181907918525676
    sum_utility_mean: -49.869562545094254
    sum_utility_min: -121.4704941854077
  date: 2022-04-27_08-32-28
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -29.09412394135115
  episode_reward_mean: -38.5913700235938
  episode_reward_min: -47.97170696172456
  episodes_this_iter: 40
  episodes_total: 40
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 16.605453491210938
          entropy_coeff: 0.0
          kl: 0.02993852086365223
          model: {}
          policy_loss: -0.10813218355178833
          total_loss: 60.30581283569336
          vf_explained_var: 0.21486933529376984
          vf_loss: 60.407955169677734
    num_agent_steps_sampled: 4000
    num_agent_steps_trained: 4000
    num_steps_sampled: 4000
    num_steps_trained: 4000
  iterations_since_restore: 1
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.531081081081076
    ram_util_percent: 59.81621621621621
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05899847060188777
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 21.676304517895623
    mean_inference_ms: 1.0345084615971434
    mean_raw_obs_processing_ms: 0.22174375525478837
  time_since_restore: 52.44395422935486
  time_this_iter_s: 52.44395422935486
  time_total_s: 52.44395422935486
  timers:
    learn_throughput: 741.884
    learn_time_ms: 5391.682
    load_throughput: 39894.27
    load_time_ms: 100.265
    sample_throughput: 85.331
    sample_time_ms: 46876.51
    update_time_ms: 3.937
  timestamp: 1651028548
  timesteps_since_restore: 0
  timesteps_total: 4000
  training_iteration: 1
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |   ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |      1 |           52.444 | 4000 | -38.5914 |             -29.0941 |             -47.9717 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 8000
  custom_metrics:
    eps_sum_utility_max: -4490.21349807869
    eps_sum_utility_mean: -6046.177389125779
    eps_sum_utility_min: -7762.497251023287
    sum_utility_max: 18.048373540605937
    sum_utility_mean: -50.8281850702052
    sum_utility_min: -121.77710421382605
  date: 2022-04-27_08-33-21
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -28.221536917239217
  episode_reward_mean: -38.20477135250439
  episode_reward_min: -47.97170696172456
  episodes_this_iter: 40
  episodes_total: 80
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 16.571773529052734
          entropy_coeff: 0.0
          kl: 0.029249481856822968
          model: {}
          policy_loss: -0.11311139911413193
          total_loss: 13.462821006774902
          vf_explained_var: 0.782815158367157
          vf_loss: 13.567158699035645
    num_agent_steps_sampled: 8000
    num_agent_steps_trained: 8000
    num_steps_sampled: 8000
    num_steps_trained: 8000
  iterations_since_restore: 2
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.15135135135135
    ram_util_percent: 60.08648648648648
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.059467083109308885
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 21.970100609288316
    mean_inference_ms: 1.0362618613982457
    mean_raw_obs_processing_ms: 0.22440627166731955
  time_since_restore: 105.9620771408081
  time_this_iter_s: 53.51812291145325
  time_total_s: 105.9620771408081
  timers:
    learn_throughput: 789.76
    learn_time_ms: 5064.831
    load_throughput: 75983.08
    load_time_ms: 52.643
    sample_throughput: 83.648
    sample_time_ms: 47819.595
    update_time_ms: 3.815
  timestamp: 1651028601
  timesteps_since_restore: 0
  timesteps_total: 8000
  training_iteration: 2
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |   ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |      2 |          105.962 | 8000 | -38.2048 |             -28.2215 |             -47.9717 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 12000
  custom_metrics:
    eps_sum_utility_max: -4290.134339859825
    eps_sum_utility_mean: -6022.762089362548
    eps_sum_utility_min: -7762.497251023287
    sum_utility_max: 18.048373540605937
    sum_utility_mean: -50.08735718761998
    sum_utility_min: -139.33231650288545
  date: 2022-04-27_08-34-19
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -27.746623392821036
  episode_reward_mean: -38.00493759322123
  episode_reward_min: -47.730309941700966
  episodes_this_iter: 40
  episodes_total: 120
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 16.543378829956055
          entropy_coeff: 0.0
          kl: 0.028349272906780243
          model: {}
          policy_loss: -0.11679110676050186
          total_loss: 7.51171875
          vf_explained_var: 0.8679159879684448
          vf_loss: 7.615753650665283
    num_agent_steps_sampled: 12000
    num_agent_steps_trained: 12000
    num_steps_sampled: 12000
    num_steps_trained: 12000
  iterations_since_restore: 3
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.571604938271605
    ram_util_percent: 60.18024691358025
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06035623172095828
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 22.491259715987844
    mean_inference_ms: 1.0454251794675649
    mean_raw_obs_processing_ms: 0.22842233641114518
  time_since_restore: 163.45055484771729
  time_this_iter_s: 57.48847770690918
  time_total_s: 163.45055484771729
  timers:
    learn_throughput: 796.107
    learn_time_ms: 5024.451
    load_throughput: 109633.987
    load_time_ms: 36.485
    sample_throughput: 80.99
    sample_time_ms: 49388.554
    update_time_ms: 3.919
  timestamp: 1651028659
  timesteps_since_restore: 0
  timesteps_total: 12000
  training_iteration: 3
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |      3 |          163.451 | 12000 | -38.0049 |             -27.7466 |             -47.7303 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 16000
  custom_metrics:
    eps_sum_utility_max: -4290.134339859825
    eps_sum_utility_mean: -5947.924445013126
    eps_sum_utility_min: -7527.481093640159
    sum_utility_max: 27.044947135067307
    sum_utility_mean: -45.601533552617255
    sum_utility_min: -139.33231650288545
  date: 2022-04-27_08-35-17
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -27.746623392821036
  episode_reward_mean: -37.59524751602417
  episode_reward_min: -46.85767841583622
  episodes_this_iter: 40
  episodes_total: 160
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 0.675000011920929
          cur_lr: 4.999999873689376e-05
          entropy: 16.512916564941406
          entropy_coeff: 0.0
          kl: 0.023906715214252472
          model: {}
          policy_loss: -0.11020143330097198
          total_loss: 4.4383955001831055
          vf_explained_var: 0.905062198638916
          vf_loss: 4.532459259033203
    num_agent_steps_sampled: 16000
    num_agent_steps_trained: 16000
    num_steps_sampled: 16000
    num_steps_trained: 16000
  iterations_since_restore: 4
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.91625
    ram_util_percent: 60.2
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06138998704877281
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 23.040756240064965
    mean_inference_ms: 1.0582197800115716
    mean_raw_obs_processing_ms: 0.23331087046733237
  time_since_restore: 221.4392499923706
  time_this_iter_s: 57.98869514465332
  time_total_s: 221.4392499923706
  timers:
    learn_throughput: 806.909
    learn_time_ms: 4957.186
    load_throughput: 140751.999
    load_time_ms: 28.419
    sample_throughput: 79.452
    sample_time_ms: 50345.061
    update_time_ms: 3.83
  timestamp: 1651028717
  timesteps_since_restore: 0
  timesteps_total: 16000
  training_iteration: 4
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |      4 |          221.439 | 16000 | -37.5952 |             -27.7466 |             -46.8577 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 20000
  custom_metrics:
    eps_sum_utility_max: -3525.8803680993356
    eps_sum_utility_mean: -5678.439248099426
    eps_sum_utility_min: -7527.481093640159
    sum_utility_max: 27.044947135067307
    sum_utility_mean: -45.685020554966016
    sum_utility_min: -127.85742259278885
  date: 2022-04-27_08-36-16
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -22.807167422100846
  episode_reward_mean: -35.955693338912745
  episode_reward_min: -46.85767841583622
  episodes_this_iter: 40
  episodes_total: 200
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.0125000476837158
          cur_lr: 4.999999873689376e-05
          entropy: 16.485401153564453
          entropy_coeff: 0.0
          kl: 0.019541705027222633
          model: {}
          policy_loss: -0.11060421913862228
          total_loss: 3.9054067134857178
          vf_explained_var: 0.9033710360527039
          vf_loss: 3.996225357055664
    num_agent_steps_sampled: 20000
    num_agent_steps_trained: 20000
    num_steps_sampled: 20000
    num_steps_trained: 20000
  iterations_since_restore: 5
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.42530120481928
    ram_util_percent: 60.22289156626507
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06212021345473859
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 23.499582669127705
    mean_inference_ms: 1.0686103715480233
    mean_raw_obs_processing_ms: 0.23688073913468283
  time_since_restore: 280.7967894077301
  time_this_iter_s: 59.3575394153595
  time_total_s: 280.7967894077301
  timers:
    learn_throughput: 800.979
    learn_time_ms: 4993.889
    load_throughput: 168628.794
    load_time_ms: 23.721
    sample_throughput: 78.254
    sample_time_ms: 51115.496
    update_time_ms: 3.761
  timestamp: 1651028776
  timesteps_since_restore: 0
  timesteps_total: 20000
  training_iteration: 5
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |      5 |          280.797 | 20000 | -35.9557 |             -22.8072 |             -46.8577 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 24000
  custom_metrics:
    eps_sum_utility_max: -3525.8803680993356
    eps_sum_utility_mean: -5374.986407163066
    eps_sum_utility_min: -7182.285293717688
    sum_utility_max: 27.044947135067307
    sum_utility_mean: -42.427919339992684
    sum_utility_min: -122.5310128244098
  date: 2022-04-27_08-37-16
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -22.807167422100846
  episode_reward_mean: -34.03758972287803
  episode_reward_min: -45.13783105625884
  episodes_this_iter: 40
  episodes_total: 240
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.0125000476837158
          cur_lr: 4.999999873689376e-05
          entropy: 16.454612731933594
          entropy_coeff: 0.0
          kl: 0.020498840138316154
          model: {}
          policy_loss: -0.11229497939348221
          total_loss: 3.899587392807007
          vf_explained_var: 0.896332323551178
          vf_loss: 3.9911272525787354
    num_agent_steps_sampled: 24000
    num_agent_steps_trained: 24000
    num_steps_sampled: 24000
    num_steps_trained: 24000
  iterations_since_restore: 6
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.10476190476191
    ram_util_percent: 60.22261904761907
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06255126532570093
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 23.853657808766737
    mean_inference_ms: 1.0745398952305336
    mean_raw_obs_processing_ms: 0.23906457937893644
  time_since_restore: 340.89443612098694
  time_this_iter_s: 60.097646713256836
  time_total_s: 340.89443612098694
  timers:
    learn_throughput: 806.203
    learn_time_ms: 4961.531
    load_throughput: 194219.705
    load_time_ms: 20.595
    sample_throughput: 77.206
    sample_time_ms: 51809.456
    update_time_ms: 3.753
  timestamp: 1651028836
  timesteps_since_restore: 0
  timesteps_total: 24000
  training_iteration: 6
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |      6 |          340.894 | 24000 | -34.0376 |             -22.8072 |             -45.1378 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 28000
  custom_metrics:
    eps_sum_utility_max: -3553.4499788208873
    eps_sum_utility_mean: -5058.310392665019
    eps_sum_utility_min: -6296.691906440198
    sum_utility_max: 20.724260772592242
    sum_utility_mean: -38.52593985180344
    sum_utility_min: -121.12441426618442
  date: 2022-04-27_08-38-18
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -22.739649466716894
  episode_reward_mean: -32.05034395716557
  episode_reward_min: -40.05932677286126
  episodes_this_iter: 40
  episodes_total: 280
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.42879867553711
          entropy_coeff: 0.0
          kl: 0.015590611845254898
          model: {}
          policy_loss: -0.10988456010818481
          total_loss: 4.190779209136963
          vf_explained_var: 0.8883253335952759
          vf_loss: 4.276986122131348
    num_agent_steps_sampled: 28000
    num_agent_steps_trained: 28000
    num_steps_sampled: 28000
    num_steps_trained: 28000
  iterations_since_restore: 7
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.01176470588236
    ram_util_percent: 60.2423529411765
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06288875290524955
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 24.17437594831101
    mean_inference_ms: 1.0797179322369184
    mean_raw_obs_processing_ms: 0.24087883319727077
  time_since_restore: 401.9779179096222
  time_this_iter_s: 61.083481788635254
  time_total_s: 401.9779179096222
  timers:
    learn_throughput: 809.191
    learn_time_ms: 4943.208
    load_throughput: 218583.849
    load_time_ms: 18.3
    sample_throughput: 76.276
    sample_time_ms: 52441.39
    update_time_ms: 3.709
  timestamp: 1651028898
  timesteps_since_restore: 0
  timesteps_total: 28000
  training_iteration: 7
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |      7 |          401.978 | 28000 | -32.0503 |             -22.7396 |             -40.0593 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 32000
  custom_metrics:
    eps_sum_utility_max: -3036.901290114757
    eps_sum_utility_mean: -4823.33805622884
    eps_sum_utility_min: -6247.5722136338245
    sum_utility_max: 20.724260772592242
    sum_utility_mean: -39.30827758502975
    sum_utility_min: -121.12441426618442
  date: 2022-04-27_08-39-19
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -19.590843641164227
  episode_reward_mean: -30.65474825519207
  episode_reward_min: -39.087509598061054
  episodes_this_iter: 40
  episodes_total: 320
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.400856018066406
          entropy_coeff: 0.0
          kl: 0.01602260023355484
          model: {}
          policy_loss: -0.10661901533603668
          total_loss: 4.016974449157715
          vf_explained_var: 0.876284122467041
          vf_loss: 4.099258899688721
    num_agent_steps_sampled: 32000
    num_agent_steps_trained: 32000
    num_steps_sampled: 32000
    num_steps_trained: 32000
  iterations_since_restore: 8
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.44823529411765
    ram_util_percent: 60.25411764705884
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06314084969884101
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 24.439118111296064
    mean_inference_ms: 1.0834044494050912
    mean_raw_obs_processing_ms: 0.2420883633578047
  time_since_restore: 463.2085998058319
  time_this_iter_s: 61.23068189620972
  time_total_s: 463.2085998058319
  timers:
    learn_throughput: 798.514
    learn_time_ms: 5009.302
    load_throughput: 243280.716
    load_time_ms: 16.442
    sample_throughput: 75.681
    sample_time_ms: 52853.6
    update_time_ms: 3.782
  timestamp: 1651028959
  timesteps_since_restore: 0
  timesteps_total: 32000
  training_iteration: 8
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |      8 |          463.209 | 32000 | -30.6547 |             -19.5908 |             -39.0875 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 36000
  custom_metrics:
    eps_sum_utility_max: -2976.308701976648
    eps_sum_utility_mean: -4481.553036259203
    eps_sum_utility_min: -6127.286473506822
    sum_utility_max: 26.512455382135805
    sum_utility_mean: -33.675136954818576
    sum_utility_min: -101.73664390536783
  date: 2022-04-27_08-40-20
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -18.488671259703253
  episode_reward_mean: -28.5291993940564
  episode_reward_min: -38.49904696523823
  episodes_this_iter: 40
  episodes_total: 360
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.37154197692871
          entropy_coeff: 0.0
          kl: 0.01507438626140356
          model: {}
          policy_loss: -0.10744023323059082
          total_loss: 2.926088333129883
          vf_explained_var: 0.8961629271507263
          vf_loss: 3.010634422302246
    num_agent_steps_sampled: 36000
    num_agent_steps_trained: 36000
    num_steps_sampled: 36000
    num_steps_trained: 36000
  iterations_since_restore: 9
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.54186046511628
    ram_util_percent: 60.231395348837225
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06327828224331661
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 24.669732177666663
    mean_inference_ms: 1.085424356150057
    mean_raw_obs_processing_ms: 0.24277917766093707
  time_since_restore: 524.5522105693817
  time_this_iter_s: 61.343610763549805
  time_total_s: 524.5522105693817
  timers:
    learn_throughput: 798.356
    learn_time_ms: 5010.299
    load_throughput: 264715.787
    load_time_ms: 15.111
    sample_throughput: 75.135
    sample_time_ms: 53237.283
    update_time_ms: 3.776
  timestamp: 1651029020
  timesteps_since_restore: 0
  timesteps_total: 36000
  training_iteration: 9
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |      9 |          524.552 | 36000 | -28.5292 |             -18.4887 |              -38.499 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 40000
  custom_metrics:
    eps_sum_utility_max: -2907.995749155958
    eps_sum_utility_mean: -4287.434288569881
    eps_sum_utility_min: -6087.808995167782
    sum_utility_max: 26.512455382135805
    sum_utility_mean: -28.673396182754665
    sum_utility_min: -98.21591571461653
  date: 2022-04-27_08-41-24
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -18.488671259703253
  episode_reward_mean: -27.304824511375635
  episode_reward_min: -38.64328310550956
  episodes_this_iter: 40
  episodes_total: 400
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.34206771850586
          entropy_coeff: 0.0
          kl: 0.015439440496265888
          model: {}
          policy_loss: -0.10771488398313522
          total_loss: 4.020259380340576
          vf_explained_var: 0.8534596562385559
          vf_loss: 4.104526042938232
    num_agent_steps_sampled: 40000
    num_agent_steps_trained: 40000
    num_steps_sampled: 40000
    num_steps_trained: 40000
  iterations_since_restore: 10
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.40674157303371
    ram_util_percent: 60.2561797752809
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06341278164661106
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 24.899641500089366
    mean_inference_ms: 1.0873350802425465
    mean_raw_obs_processing_ms: 0.2434223800362858
  time_since_restore: 588.4173376560211
  time_this_iter_s: 63.865127086639404
  time_total_s: 588.4173376560211
  timers:
    learn_throughput: 796.553
    learn_time_ms: 5021.64
    load_throughput: 286443.347
    load_time_ms: 13.964
    sample_throughput: 74.369
    sample_time_ms: 53785.893
    update_time_ms: 3.81
  timestamp: 1651029084
  timesteps_since_restore: 0
  timesteps_total: 40000
  training_iteration: 10
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     10 |          588.417 | 40000 | -27.3048 |             -18.4887 |             -38.6433 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 44000
  custom_metrics:
    eps_sum_utility_max: -2723.8386096921636
    eps_sum_utility_mean: -4080.7599527664906
    eps_sum_utility_min: -6087.808995167782
    sum_utility_max: 26.512455382135805
    sum_utility_mean: -24.701286972986917
    sum_utility_min: -99.59107647667797
  date: 2022-04-27_08-42-29
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -18.05124686666383
  episode_reward_mean: -26.035504203193142
  episode_reward_min: -38.64328310550956
  episodes_this_iter: 40
  episodes_total: 440
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.305723190307617
          entropy_coeff: 0.0
          kl: 0.01650354638695717
          model: {}
          policy_loss: -0.11299402266740799
          total_loss: 3.5389487743377686
          vf_explained_var: 0.8628097176551819
          vf_loss: 3.626878261566162
    num_agent_steps_sampled: 44000
    num_agent_steps_trained: 44000
    num_steps_sampled: 44000
    num_steps_trained: 44000
  iterations_since_restore: 11
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.20224719101124
    ram_util_percent: 60.298876404494386
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06356099720696384
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 25.129390782950935
    mean_inference_ms: 1.0893609651195941
    mean_raw_obs_processing_ms: 0.2442317675371256
  time_since_restore: 652.6799962520599
  time_this_iter_s: 64.26265859603882
  time_total_s: 652.6799962520599
  timers:
    learn_throughput: 790.145
    learn_time_ms: 5062.364
    load_throughput: 917289.01
    load_time_ms: 4.361
    sample_throughput: 72.803
    sample_time_ms: 54942.556
    update_time_ms: 3.843
  timestamp: 1651029149
  timesteps_since_restore: 0
  timesteps_total: 44000
  training_iteration: 11
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     11 |           652.68 | 44000 | -26.0355 |             -18.0512 |             -38.6433 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 48000
  custom_metrics:
    eps_sum_utility_max: -2643.13014285753
    eps_sum_utility_mean: -4013.79054165927
    eps_sum_utility_min: -6087.808995167782
    sum_utility_max: 21.672168605007016
    sum_utility_mean: -25.9684256655042
    sum_utility_min: -99.59107647667797
  date: 2022-04-27_08-43-33
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -17.37398097051279
  episode_reward_mean: -25.622710915296455
  episode_reward_min: -38.64328310550956
  episodes_this_iter: 40
  episodes_total: 480
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.276473999023438
          entropy_coeff: 0.0
          kl: 0.015781307592988014
          model: {}
          policy_loss: -0.11344888061285019
          total_loss: 3.7115495204925537
          vf_explained_var: 0.8633028268814087
          vf_loss: 3.8010306358337402
    num_agent_steps_sampled: 48000
    num_agent_steps_trained: 48000
    num_steps_sampled: 48000
    num_steps_trained: 48000
  iterations_since_restore: 12
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.596666666666664
    ram_util_percent: 60.314444444444455
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06374742224664967
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 25.35193381510481
    mean_inference_ms: 1.0922577648926428
    mean_raw_obs_processing_ms: 0.24475629544897498
  time_since_restore: 717.2599773406982
  time_this_iter_s: 64.5799810886383
  time_total_s: 717.2599773406982
  timers:
    learn_throughput: 787.565
    learn_time_ms: 5078.948
    load_throughput: 939684.218
    load_time_ms: 4.257
    sample_throughput: 71.387
    sample_time_ms: 56032.219
    update_time_ms: 3.778
  timestamp: 1651029213
  timesteps_since_restore: 0
  timesteps_total: 48000
  training_iteration: 12
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     12 |           717.26 | 48000 | -25.6227 |              -17.374 |             -38.6433 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 52000
  custom_metrics:
    eps_sum_utility_max: -2352.7273072619173
    eps_sum_utility_mean: -3677.022759327488
    eps_sum_utility_min: -5230.752837276721
    sum_utility_max: 29.06025910750276
    sum_utility_mean: -25.549301519067022
    sum_utility_min: -99.59107647667797
  date: 2022-04-27_08-44-38
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -14.669778544223696
  episode_reward_mean: -23.54080166133867
  episode_reward_min: -32.88922217337305
  episodes_this_iter: 40
  episodes_total: 520
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.241111755371094
          entropy_coeff: 0.0
          kl: 0.01597769372165203
          model: {}
          policy_loss: -0.11041979491710663
          total_loss: 2.1506688594818115
          vf_explained_var: 0.8868982195854187
          vf_loss: 2.236823081970215
    num_agent_steps_sampled: 52000
    num_agent_steps_trained: 52000
    num_steps_sampled: 52000
    num_steps_trained: 52000
  iterations_since_restore: 13
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.24444444444444
    ram_util_percent: 60.20888888888889
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06389196805636183
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 25.57067677543245
    mean_inference_ms: 1.0947229736442259
    mean_raw_obs_processing_ms: 0.24513464434731363
  time_since_restore: 781.9807932376862
  time_this_iter_s: 64.72081589698792
  time_total_s: 781.9807932376862
  timers:
    learn_throughput: 786.998
    learn_time_ms: 5082.603
    load_throughput: 917549.877
    load_time_ms: 4.359
    sample_throughput: 70.483
    sample_time_ms: 56751.653
    update_time_ms: 3.7
  timestamp: 1651029278
  timesteps_since_restore: 0
  timesteps_total: 52000
  training_iteration: 13
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     13 |          781.981 | 52000 | -23.5408 |             -14.6698 |             -32.8892 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 56000
  custom_metrics:
    eps_sum_utility_max: -2352.7273072619173
    eps_sum_utility_mean: -3457.2925765196997
    eps_sum_utility_min: -5003.8785815533765
    sum_utility_max: 29.06025910750276
    sum_utility_mean: -23.028164386187708
    sum_utility_min: -103.26081397308499
  date: 2022-04-27_08-45-42
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -14.669778544223696
  episode_reward_mean: -22.190728855973838
  episode_reward_min: -31.423596856491255
  episodes_this_iter: 40
  episodes_total: 560
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.196046829223633
          entropy_coeff: 0.0
          kl: 0.01567544974386692
          model: {}
          policy_loss: -0.11584111303091049
          total_loss: 2.4689087867736816
          vf_explained_var: 0.8694785833358765
          vf_loss: 2.5609426498413086
    num_agent_steps_sampled: 56000
    num_agent_steps_trained: 56000
    num_steps_sampled: 56000
    num_steps_trained: 56000
  iterations_since_restore: 14
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.13820224719101
    ram_util_percent: 60.233707865168554
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06397953569099825
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 25.75900592604281
    mean_inference_ms: 1.0961551765732462
    mean_raw_obs_processing_ms: 0.2454755383262393
  time_since_restore: 845.9470200538635
  time_this_iter_s: 63.96622681617737
  time_total_s: 845.9470200538635
  timers:
    learn_throughput: 783.65
    learn_time_ms: 5104.316
    load_throughput: 910227.161
    load_time_ms: 4.395
    sample_throughput: 69.775
    sample_time_ms: 57327.444
    update_time_ms: 3.762
  timestamp: 1651029342
  timesteps_since_restore: 0
  timesteps_total: 56000
  training_iteration: 14
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     14 |          845.947 | 56000 | -22.1907 |             -14.6698 |             -31.4236 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 60000
  custom_metrics:
    eps_sum_utility_max: -2011.7456652311726
    eps_sum_utility_mean: -3244.430651994639
    eps_sum_utility_min: -5003.8785815533765
    sum_utility_max: 25.0892161019968
    sum_utility_mean: -23.075798972953997
    sum_utility_min: -103.26081397308499
  date: 2022-04-27_08-46-48
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -12.615173235528358
  episode_reward_mean: -20.826579601020498
  episode_reward_min: -31.423596856491255
  episodes_this_iter: 40
  episodes_total: 600
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.154029846191406
          entropy_coeff: 0.0
          kl: 0.01657705381512642
          model: {}
          policy_loss: -0.11644744873046875
          total_loss: 2.35264253616333
          vf_explained_var: 0.8586877584457397
          vf_loss: 2.443913459777832
    num_agent_steps_sampled: 60000
    num_agent_steps_trained: 60000
    num_steps_sampled: 60000
    num_steps_trained: 60000
  iterations_since_restore: 15
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.31195652173913
    ram_util_percent: 60.247826086956536
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06403969054344325
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 25.931095855463187
    mean_inference_ms: 1.097122984856405
    mean_raw_obs_processing_ms: 0.24589020378020565
  time_since_restore: 911.8307864665985
  time_this_iter_s: 65.88376641273499
  time_total_s: 911.8307864665985
  timers:
    learn_throughput: 783.706
    learn_time_ms: 5103.955
    load_throughput: 925986.908
    load_time_ms: 4.32
    sample_throughput: 68.988
    sample_time_ms: 57980.69
    update_time_ms: 3.768
  timestamp: 1651029408
  timesteps_since_restore: 0
  timesteps_total: 60000
  training_iteration: 15
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     15 |          911.831 | 60000 | -20.8266 |             -12.6152 |             -31.4236 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 64000
  custom_metrics:
    eps_sum_utility_max: -1699.8326151315096
    eps_sum_utility_mean: -3062.7242067462885
    eps_sum_utility_min: -5003.8785815533765
    sum_utility_max: 25.0892161019968
    sum_utility_mean: -19.10913648305014
    sum_utility_min: -71.39020974574098
  date: 2022-04-27_08-47-55
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -11.322096519408921
  episode_reward_mean: -19.586507682880182
  episode_reward_min: -31.423596856491255
  episodes_this_iter: 40
  episodes_total: 640
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.118606567382812
          entropy_coeff: 0.0
          kl: 0.015700500458478928
          model: {}
          policy_loss: -0.11407758295536041
          total_loss: 2.6919105052948
          vf_explained_var: 0.8251709938049316
          vf_loss: 2.7821426391601562
    num_agent_steps_sampled: 64000
    num_agent_steps_trained: 64000
    num_steps_sampled: 64000
    num_steps_trained: 64000
  iterations_since_restore: 16
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.96195652173913
    ram_util_percent: 60.283695652173925
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06410136696910856
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 26.1005161222052
    mean_inference_ms: 1.0980588234238993
    mean_raw_obs_processing_ms: 0.24621770643463786
  time_since_restore: 978.1866538524628
  time_this_iter_s: 66.35586738586426
  time_total_s: 978.1866538524628
  timers:
    learn_throughput: 781.46
    learn_time_ms: 5118.621
    load_throughput: 936197.226
    load_time_ms: 4.273
    sample_throughput: 68.269
    sample_time_ms: 58591.737
    update_time_ms: 3.818
  timestamp: 1651029475
  timesteps_since_restore: 0
  timesteps_total: 64000
  training_iteration: 16
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     16 |          978.187 | 64000 | -19.5865 |             -11.3221 |             -31.4236 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 68000
  custom_metrics:
    eps_sum_utility_max: -1699.8326151315096
    eps_sum_utility_mean: -2820.539125008408
    eps_sum_utility_min: -4006.8323801262563
    sum_utility_max: 26.17532489790998
    sum_utility_mean: -13.497662132103219
    sum_utility_min: -77.74786760932417
  date: 2022-04-27_08-49-02
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -11.13403214496625
  episode_reward_mean: -18.082793473055027
  episode_reward_min: -25.696231335388493
  episodes_this_iter: 40
  episodes_total: 680
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.085830688476562
          entropy_coeff: 0.0
          kl: 0.015284296125173569
          model: {}
          policy_loss: -0.11280708014965057
          total_loss: 2.449057102203369
          vf_explained_var: 0.8356961607933044
          vf_loss: 2.5386509895324707
    num_agent_steps_sampled: 68000
    num_agent_steps_trained: 68000
    num_steps_sampled: 68000
    num_steps_trained: 68000
  iterations_since_restore: 17
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.11914893617021
    ram_util_percent: 60.28297872340427
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06417876341541723
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 26.28061225018364
    mean_inference_ms: 1.0992679705211597
    mean_raw_obs_processing_ms: 0.24655892465018048
  time_since_restore: 1045.5299265384674
  time_this_iter_s: 67.34327268600464
  time_total_s: 1045.5299265384674
  timers:
    learn_throughput: 779.693
    learn_time_ms: 5130.221
    load_throughput: 950356.641
    load_time_ms: 4.209
    sample_throughput: 67.561
    sample_time_ms: 59206.068
    update_time_ms: 3.804
  timestamp: 1651029542
  timesteps_since_restore: 0
  timesteps_total: 68000
  training_iteration: 17
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     17 |          1045.53 | 68000 | -18.0828 |              -11.134 |             -25.6962 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 72000
  custom_metrics:
    eps_sum_utility_max: -1616.2327883972746
    eps_sum_utility_mean: -2652.1745598261036
    eps_sum_utility_min: -4253.512146061782
    sum_utility_max: 26.17532489790998
    sum_utility_mean: -10.20915487391835
    sum_utility_min: -77.74786760932417
  date: 2022-04-27_08-50-09
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -10.525545978777185
  episode_reward_mean: -16.999229415865155
  episode_reward_min: -27.023223387462252
  episodes_this_iter: 40
  episodes_total: 720
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.058773040771484
          entropy_coeff: 0.0
          kl: 0.01576174423098564
          model: {}
          policy_loss: -0.11453977227210999
          total_loss: 2.4100139141082764
          vf_explained_var: 0.8225466012954712
          vf_loss: 2.5006158351898193
    num_agent_steps_sampled: 72000
    num_agent_steps_trained: 72000
    num_steps_sampled: 72000
    num_steps_trained: 72000
  iterations_since_restore: 18
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.93010752688172
    ram_util_percent: 60.28387096774194
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06423563689330346
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 26.450681441539377
    mean_inference_ms: 1.1002726930692865
    mean_raw_obs_processing_ms: 0.24685392861623243
  time_since_restore: 1112.5225377082825
  time_this_iter_s: 66.99261116981506
  time_total_s: 1112.5225377082825
  timers:
    learn_throughput: 787.717
    learn_time_ms: 5077.963
    load_throughput: 912082.808
    load_time_ms: 4.386
    sample_throughput: 66.851
    sample_time_ms: 59834.601
    update_time_ms: 3.725
  timestamp: 1651029609
  timesteps_since_restore: 0
  timesteps_total: 72000
  training_iteration: 18
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     18 |          1112.52 | 72000 | -16.9992 |             -10.5255 |             -27.0232 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 76000
  custom_metrics:
    eps_sum_utility_max: -1546.0102353185462
    eps_sum_utility_mean: -2494.2171942864397
    eps_sum_utility_min: -4253.512146061782
    sum_utility_max: 26.17532489790998
    sum_utility_mean: -7.003374282827641
    sum_utility_min: -77.74786760932417
  date: 2022-04-27_08-51-17
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -9.711862664447496
  episode_reward_mean: -15.999943879243487
  episode_reward_min: -27.023223387462252
  episodes_this_iter: 40
  episodes_total: 760
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 16.005695343017578
          entropy_coeff: 0.0
          kl: 0.015930866822600365
          model: {}
          policy_loss: -0.11401902139186859
          total_loss: 2.4024155139923096
          vf_explained_var: 0.8130586743354797
          vf_loss: 2.492239236831665
    num_agent_steps_sampled: 76000
    num_agent_steps_trained: 76000
    num_steps_sampled: 76000
    num_steps_trained: 76000
  iterations_since_restore: 19
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.039361702127664
    ram_util_percent: 60.29042553191491
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06428405991499109
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 26.611097459186084
    mean_inference_ms: 1.1011486449163284
    mean_raw_obs_processing_ms: 0.24714229568121177
  time_since_restore: 1180.0733969211578
  time_this_iter_s: 67.55085921287537
  time_total_s: 1180.0733969211578
  timers:
    learn_throughput: 789.621
    learn_time_ms: 5065.718
    load_throughput: 906974.592
    load_time_ms: 4.41
    sample_throughput: 66.151
    sample_time_ms: 60467.683
    update_time_ms: 3.696
  timestamp: 1651029677
  timesteps_since_restore: 0
  timesteps_total: 76000
  training_iteration: 19
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     19 |          1180.07 | 76000 | -15.9999 |             -9.71186 |             -27.0232 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 80000
  custom_metrics:
    eps_sum_utility_max: -1220.8837088535179
    eps_sum_utility_mean: -2432.4805716533633
    eps_sum_utility_min: -4253.512146061782
    sum_utility_max: 26.09065734945223
    sum_utility_mean: -7.37999237707308
    sum_utility_min: -65.26400738014922
  date: 2022-04-27_08-52-25
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -8.118890066808609
  episode_reward_mean: -15.606323334422491
  episode_reward_min: -27.023223387462252
  episodes_this_iter: 40
  episodes_total: 800
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.965943336486816
          entropy_coeff: 0.0
          kl: 0.01662955991923809
          model: {}
          policy_loss: -0.1198895126581192
          total_loss: 2.228921890258789
          vf_explained_var: 0.8134475946426392
          vf_loss: 2.3235554695129395
    num_agent_steps_sampled: 80000
    num_agent_steps_trained: 80000
    num_steps_sampled: 80000
    num_steps_trained: 80000
  iterations_since_restore: 20
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.24736842105263
    ram_util_percent: 60.29263157894737
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06432513638295174
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 26.764300634382238
    mean_inference_ms: 1.1019473394128645
    mean_raw_obs_processing_ms: 0.24739869014077737
  time_since_restore: 1248.49191904068
  time_this_iter_s: 68.4185221195221
  time_total_s: 1248.49191904068
  timers:
    learn_throughput: 791.907
    learn_time_ms: 5051.098
    load_throughput: 861846.239
    load_time_ms: 4.641
    sample_throughput: 65.641
    sample_time_ms: 60937.393
    update_time_ms: 3.66
  timestamp: 1651029745
  timesteps_since_restore: 0
  timesteps_total: 80000
  training_iteration: 20
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     20 |          1248.49 | 80000 | -15.6063 |             -8.11889 |             -27.0232 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 84000
  custom_metrics:
    eps_sum_utility_max: -1008.8242222351574
    eps_sum_utility_mean: -2281.961114066144
    eps_sum_utility_min: -3441.8377730006605
    sum_utility_max: 28.162582796740118
    sum_utility_mean: -9.7445202574493
    sum_utility_min: -74.04863333949531
  date: 2022-04-27_08-53-35
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -7.144105341630901
  episode_reward_mean: -14.677151358913585
  episode_reward_min: -21.609622857778906
  episodes_this_iter: 40
  episodes_total: 840
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.923330307006836
          entropy_coeff: 0.0
          kl: 0.015694258734583855
          model: {}
          policy_loss: -0.11770489811897278
          total_loss: 1.9479646682739258
          vf_explained_var: 0.8094993233680725
          vf_loss: 2.0418341159820557
    num_agent_steps_sampled: 84000
    num_agent_steps_trained: 84000
    num_steps_sampled: 84000
    num_steps_trained: 84000
  iterations_since_restore: 21
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.30408163265306
    ram_util_percent: 60.30510204081632
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06439398675532337
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 26.93238990453502
    mean_inference_ms: 1.1031048424066194
    mean_raw_obs_processing_ms: 0.24775097295604176
  time_since_restore: 1318.3830072879791
  time_this_iter_s: 69.8910882472992
  time_total_s: 1318.3830072879791
  timers:
    learn_throughput: 806.216
    learn_time_ms: 4961.449
    load_throughput: 867102.323
    load_time_ms: 4.613
    sample_throughput: 64.945
    sample_time_ms: 61590.185
    update_time_ms: 3.647
  timestamp: 1651029815
  timesteps_since_restore: 0
  timesteps_total: 84000
  training_iteration: 21
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     21 |          1318.38 | 84000 | -14.6772 |             -7.14411 |             -21.6096 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 88000
  custom_metrics:
    eps_sum_utility_max: -997.3132432065014
    eps_sum_utility_mean: -2034.9762824422842
    eps_sum_utility_min: -3108.221889299463
    sum_utility_max: 28.162582796740118
    sum_utility_mean: -11.24191600835242
    sum_utility_min: -74.04863333949531
  date: 2022-04-27_08-54-45
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -6.934746871356333
  episode_reward_mean: -13.104653605742087
  episode_reward_min: -20.45698574648659
  episodes_this_iter: 40
  episodes_total: 880
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.876197814941406
          entropy_coeff: 0.0
          kl: 0.015657497569918633
          model: {}
          policy_loss: -0.11382607370615005
          total_loss: 1.4769597053527832
          vf_explained_var: 0.8164904713630676
          vf_loss: 1.5670057535171509
    num_agent_steps_sampled: 88000
    num_agent_steps_trained: 88000
    num_steps_sampled: 88000
    num_steps_trained: 88000
  iterations_since_restore: 22
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.85208333333333
    ram_util_percent: 60.32083333333335
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06445847353362404
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 27.100565016436967
    mean_inference_ms: 1.1041570329950874
    mean_raw_obs_processing_ms: 0.2480391109427466
  time_since_restore: 1387.7370865345001
  time_this_iter_s: 69.354079246521
  time_total_s: 1387.7370865345001
  timers:
    learn_throughput: 806.161
    learn_time_ms: 4961.791
    load_throughput: 855526.455
    load_time_ms: 4.675
    sample_throughput: 64.446
    sample_time_ms: 62067.201
    update_time_ms: 3.683
  timestamp: 1651029885
  timesteps_since_restore: 0
  timesteps_total: 88000
  training_iteration: 22
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     22 |          1387.74 | 88000 | -13.1047 |             -6.93475 |              -20.457 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 92000
  custom_metrics:
    eps_sum_utility_max: -765.8818819983117
    eps_sum_utility_mean: -1899.5149072082288
    eps_sum_utility_min: -3094.6665829098893
    sum_utility_max: 28.317212658664985
    sum_utility_mean: -9.238587426217256
    sum_utility_min: -74.04863333949531
  date: 2022-04-27_08-55-55
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -4.768196005361965
  episode_reward_mean: -12.28655735814904
  episode_reward_min: -20.45698574648659
  episodes_this_iter: 40
  episodes_total: 920
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.833976745605469
          entropy_coeff: 0.0
          kl: 0.016191545873880386
          model: {}
          policy_loss: -0.11839981377124786
          total_loss: 1.2940984964370728
          vf_explained_var: 0.8242776989936829
          vf_loss: 1.3879075050354004
    num_agent_steps_sampled: 92000
    num_agent_steps_trained: 92000
    num_steps_sampled: 92000
    num_steps_trained: 92000
  iterations_since_restore: 23
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.04329896907217
    ram_util_percent: 60.3298969072165
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06451369040698844
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 27.25487673540553
    mean_inference_ms: 1.1049653527295216
    mean_raw_obs_processing_ms: 0.2482833474422703
  time_since_restore: 1457.4054598808289
  time_this_iter_s: 69.66837334632874
  time_total_s: 1457.4054598808289
  timers:
    learn_throughput: 804.955
    learn_time_ms: 4969.224
    load_throughput: 870887.695
    load_time_ms: 4.593
    sample_throughput: 63.944
    sample_time_ms: 62554.667
    update_time_ms: 3.71
  timestamp: 1651029955
  timesteps_since_restore: 0
  timesteps_total: 92000
  training_iteration: 23
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     23 |          1457.41 | 92000 | -12.2866 |              -4.7682 |              -20.457 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 96000
  custom_metrics:
    eps_sum_utility_max: -539.3112632671465
    eps_sum_utility_mean: -1717.4338299885121
    eps_sum_utility_min: -2988.5343388250803
    sum_utility_max: 28.317212658664985
    sum_utility_mean: -5.378300822021833
    sum_utility_min: -73.72962909432839
  date: 2022-04-27_08-57-05
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -4.059773038709864
  episode_reward_mean: -11.065677011138282
  episode_reward_min: -18.962090638932906
  episodes_this_iter: 40
  episodes_total: 960
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.789780616760254
          entropy_coeff: 0.0
          kl: 0.015627987682819366
          model: {}
          policy_loss: -0.11703118681907654
          total_loss: 1.8722047805786133
          vf_explained_var: 0.7550632953643799
          vf_loss: 1.9655009508132935
    num_agent_steps_sampled: 96000
    num_agent_steps_trained: 96000
    num_steps_sampled: 96000
    num_steps_trained: 96000
  iterations_since_restore: 24
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.50808080808081
    ram_util_percent: 60.315151515151534
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06454949942322703
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 27.398551529286397
    mean_inference_ms: 1.105543197185331
    mean_raw_obs_processing_ms: 0.24844712398573462
  time_since_restore: 1528.1722285747528
  time_this_iter_s: 70.76676869392395
  time_total_s: 1528.1722285747528
  timers:
    learn_throughput: 793.175
    learn_time_ms: 5043.026
    load_throughput: 872840.48
    load_time_ms: 4.583
    sample_throughput: 63.33
    sample_time_ms: 63160.916
    update_time_ms: 3.768
  timestamp: 1651030025
  timesteps_since_restore: 0
  timesteps_total: 96000
  training_iteration: 24
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     24 |          1528.17 | 96000 | -11.0657 |             -4.05977 |             -18.9621 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 100000
  custom_metrics:
    eps_sum_utility_max: -539.3112632671465
    eps_sum_utility_mean: -1500.614093553056
    eps_sum_utility_min: -2761.042916902794
    sum_utility_max: 26.336936341173335
    sum_utility_mean: -2.4081940100417816
    sum_utility_min: -58.70213543059241
  date: 2022-04-27_08-58-13
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -4.059773038709864
  episode_reward_mean: -9.720379888092808
  episode_reward_min: -17.046593601221495
  episodes_this_iter: 40
  episodes_total: 1000
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.75504207611084
          entropy_coeff: 0.0
          kl: 0.016421116888523102
          model: {}
          policy_loss: -0.12226471304893494
          total_loss: 1.3709489107131958
          vf_explained_var: 0.7582341432571411
          vf_loss: 1.4682741165161133
    num_agent_steps_sampled: 100000
    num_agent_steps_trained: 100000
    num_steps_sampled: 100000
    num_steps_trained: 100000
  iterations_since_restore: 25
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.04148936170212
    ram_util_percent: 60.20957446808514
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.0645409297669046
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 27.5194289584769
    mean_inference_ms: 1.105524080437281
    mean_raw_obs_processing_ms: 0.24846238078334273
  time_since_restore: 1595.7192153930664
  time_this_iter_s: 67.5469868183136
  time_total_s: 1595.7192153930664
  timers:
    learn_throughput: 796.062
    learn_time_ms: 5024.733
    load_throughput: 876126.856
    load_time_ms: 4.566
    sample_throughput: 63.146
    sample_time_ms: 63345.494
    update_time_ms: 3.788
  timestamp: 1651030093
  timesteps_since_restore: 0
  timesteps_total: 100000
  training_iteration: 25
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     25 |          1595.72 | 100000 | -9.72038 |             -4.05977 |             -17.0466 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 104000
  custom_metrics:
    eps_sum_utility_max: -494.48919747874356
    eps_sum_utility_mean: -1383.308843192823
    eps_sum_utility_min: -2761.042916902794
    sum_utility_max: 26.658568638664253
    sum_utility_mean: -0.49350686185405657
    sum_utility_min: -59.7464282664978
  date: 2022-04-27_08-59-24
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -3.105233177537344
  episode_reward_mean: -8.97171332857695
  episode_reward_min: -17.046593601221495
  episodes_this_iter: 40
  episodes_total: 1040
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.704716682434082
          entropy_coeff: 0.0
          kl: 0.015885908156633377
          model: {}
          policy_loss: -0.11796402186155319
          total_loss: 1.2652579545974731
          vf_explained_var: 0.7786950469017029
          vf_loss: 1.3590950965881348
    num_agent_steps_sampled: 104000
    num_agent_steps_trained: 104000
    num_steps_sampled: 104000
    num_steps_trained: 104000
  iterations_since_restore: 26
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.859595959595964
    ram_util_percent: 60.23333333333335
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06453489862953395
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 27.639558615496934
    mean_inference_ms: 1.1054359449732927
    mean_raw_obs_processing_ms: 0.24848954478755797
  time_since_restore: 1667.0446844100952
  time_this_iter_s: 71.32546901702881
  time_total_s: 1667.0446844100952
  timers:
    learn_throughput: 795.525
    learn_time_ms: 5028.123
    load_throughput: 861363.933
    load_time_ms: 4.644
    sample_throughput: 62.658
    sample_time_ms: 63839.027
    update_time_ms: 3.726
  timestamp: 1651030164
  timesteps_since_restore: 0
  timesteps_total: 104000
  training_iteration: 26
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     26 |          1667.04 | 104000 | -8.97171 |             -3.10523 |             -17.0466 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 108000
  custom_metrics:
    eps_sum_utility_max: -419.6161112322363
    eps_sum_utility_mean: -1300.5760160969487
    eps_sum_utility_min: -2253.0787859656475
    sum_utility_max: 27.26618012384132
    sum_utility_mean: 0.41063890543325293
    sum_utility_min: -59.7464282664978
  date: 2022-04-27_09-00-38
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -2.609975231599104
  episode_reward_mean: -8.452287155154812
  episode_reward_min: -14.409214354424764
  episodes_this_iter: 40
  episodes_total: 1080
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.654740333557129
          entropy_coeff: 0.0
          kl: 0.015519937500357628
          model: {}
          policy_loss: -0.11625758558511734
          total_loss: 1.487196683883667
          vf_explained_var: 0.7493281960487366
          vf_loss: 1.5798835754394531
    num_agent_steps_sampled: 108000
    num_agent_steps_trained: 108000
    num_steps_sampled: 108000
    num_steps_trained: 108000
  iterations_since_restore: 27
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.60873786407767
    ram_util_percent: 60.273786407767
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06456873734648363
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 27.779947046088054
    mean_inference_ms: 1.1059713505804234
    mean_raw_obs_processing_ms: 0.2486764208515934
  time_since_restore: 1740.649845123291
  time_this_iter_s: 73.6051607131958
  time_total_s: 1740.649845123291
  timers:
    learn_throughput: 784.189
    learn_time_ms: 5100.813
    load_throughput: 861231.283
    load_time_ms: 4.645
    sample_throughput: 62.119
    sample_time_ms: 64392.105
    update_time_ms: 3.876
  timestamp: 1651030238
  timesteps_since_restore: 0
  timesteps_total: 108000
  training_iteration: 27
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     27 |          1740.65 | 108000 | -8.45229 |             -2.60998 |             -14.4092 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 112000
  custom_metrics:
    eps_sum_utility_max: -130.54576046807728
    eps_sum_utility_mean: -1171.6230101016429
    eps_sum_utility_min: -2253.0787859656475
    sum_utility_max: 27.26618012384132
    sum_utility_mean: 1.2148799658309024
    sum_utility_min: -59.7464282664978
  date: 2022-04-27_09-01-58
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -1.1832323865889554
  episode_reward_mean: -7.598501794741882
  episode_reward_min: -14.409214354424764
  episodes_this_iter: 40
  episodes_total: 1120
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.62770938873291
          entropy_coeff: 0.0
          kl: 0.015200515277683735
          model: {}
          policy_loss: -0.11603234708309174
          total_loss: 1.1103147268295288
          vf_explained_var: 0.7372103333473206
          vf_loss: 1.2032612562179565
    num_agent_steps_sampled: 112000
    num_agent_steps_trained: 112000
    num_steps_sampled: 112000
    num_steps_trained: 112000
  iterations_since_restore: 28
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.60545454545454
    ram_util_percent: 60.31818181818183
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06469773016558249
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 27.978513077452703
    mean_inference_ms: 1.1081233962780361
    mean_raw_obs_processing_ms: 0.24922382976404525
  time_since_restore: 1820.4346632957458
  time_this_iter_s: 79.78481817245483
  time_total_s: 1820.4346632957458
  timers:
    learn_throughput: 770.699
    learn_time_ms: 5190.096
    load_throughput: 863465.242
    load_time_ms: 4.632
    sample_throughput: 60.993
    sample_time_ms: 65581.804
    update_time_ms: 3.938
  timestamp: 1651030318
  timesteps_since_restore: 0
  timesteps_total: 112000
  training_iteration: 28
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     28 |          1820.43 | 112000 |  -7.5985 |             -1.18323 |             -14.4092 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 116000
  custom_metrics:
    eps_sum_utility_max: -130.3692390140206
    eps_sum_utility_mean: -1031.036483511654
    eps_sum_utility_min: -1871.2377117782776
    sum_utility_max: 26.0706412460714
    sum_utility_mean: 1.3330895937431657
    sum_utility_min: -44.86247386800425
  date: 2022-04-27_09-03-13
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -1.1063248826566907
  episode_reward_mean: -6.72154216766229
  episode_reward_min: -12.342054235640925
  episodes_this_iter: 40
  episodes_total: 1160
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.569085121154785
          entropy_coeff: 0.0
          kl: 0.016810933127999306
          model: {}
          policy_loss: -0.11934120208024979
          total_loss: 0.7378215193748474
          vf_explained_var: 0.7986365556716919
          vf_loss: 0.8316311240196228
    num_agent_steps_sampled: 116000
    num_agent_steps_trained: 116000
    num_steps_sampled: 116000
    num_steps_trained: 116000
  iterations_since_restore: 29
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.57333333333333
    ram_util_percent: 60.337142857142865
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06484359449660777
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 28.18300987202304
    mean_inference_ms: 1.1106234753453894
    mean_raw_obs_processing_ms: 0.24982437226579018
  time_since_restore: 1895.8350789546967
  time_this_iter_s: 75.4004156589508
  time_total_s: 1895.8350789546967
  timers:
    learn_throughput: 762.263
    learn_time_ms: 5247.53
    load_throughput: 873403.925
    load_time_ms: 4.58
    sample_throughput: 60.324
    sample_time_ms: 66309.037
    update_time_ms: 4.018
  timestamp: 1651030393
  timesteps_since_restore: 0
  timesteps_total: 116000
  training_iteration: 29
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     29 |          1895.84 | 116000 | -6.72154 |             -1.10632 |             -12.3421 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 120000
  custom_metrics:
    eps_sum_utility_max: -130.3692390140206
    eps_sum_utility_mean: -925.4713178141715
    eps_sum_utility_min: -1864.5893599066676
    sum_utility_max: 28.163841551501747
    sum_utility_mean: 4.589559078673605
    sum_utility_min: -65.80047305666645
  date: 2022-04-27_09-04-30
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -1.1063248826566907
  episode_reward_mean: -6.05249142808452
  episode_reward_min: -12.342054235640925
  episodes_this_iter: 40
  episodes_total: 1200
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.51188850402832
          entropy_coeff: 0.0
          kl: 0.015565411187708378
          model: {}
          policy_loss: -0.1180601716041565
          total_loss: 0.7695146203041077
          vf_explained_var: 0.7649207711219788
          vf_loss: 0.8639349937438965
    num_agent_steps_sampled: 120000
    num_agent_steps_trained: 120000
    num_steps_sampled: 120000
    num_steps_trained: 120000
  iterations_since_restore: 30
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.46261682242991
    ram_util_percent: 60.33084112149534
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06498403682477179
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 28.378139287552646
    mean_inference_ms: 1.1130623180960755
    mean_raw_obs_processing_ms: 0.2504543704005511
  time_since_restore: 1972.3700273036957
  time_this_iter_s: 76.53494834899902
  time_total_s: 1972.3700273036957
  timers:
    learn_throughput: 763.304
    learn_time_ms: 5240.376
    load_throughput: 900964.267
    load_time_ms: 4.44
    sample_throughput: 59.588
    sample_time_ms: 67127.326
    update_time_ms: 4.001
  timestamp: 1651030470
  timesteps_since_restore: 0
  timesteps_total: 120000
  training_iteration: 30
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     30 |          1972.37 | 120000 | -6.05249 |             -1.10632 |             -12.3421 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 124000
  custom_metrics:
    eps_sum_utility_max: -93.89158494998489
    eps_sum_utility_mean: -794.9397422066414
    eps_sum_utility_min: -1736.2133577273355
    sum_utility_max: 29.18991785778003
    sum_utility_mean: 7.149572796521458
    sum_utility_min: -65.80047305666645
  date: 2022-04-27_09-05-42
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -0.8322704233592326
  episode_reward_mean: -5.220205165706805
  episode_reward_min: -11.759397410840439
  episodes_this_iter: 40
  episodes_total: 1240
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.480281829833984
          entropy_coeff: 0.0
          kl: 0.015179473906755447
          model: {}
          policy_loss: -0.11614754050970078
          total_loss: 0.9258369207382202
          vf_explained_var: 0.7195882201194763
          vf_loss: 1.0189305543899536
    num_agent_steps_sampled: 124000
    num_agent_steps_trained: 124000
    num_steps_sampled: 124000
    num_steps_trained: 124000
  iterations_since_restore: 31
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.75555555555555
    ram_util_percent: 60.32121212121212
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06505592193574852
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 28.5307554963439
    mean_inference_ms: 1.1143282869553006
    mean_raw_obs_processing_ms: 0.2507979025325165
  time_since_restore: 2044.097107887268
  time_this_iter_s: 71.72708058357239
  time_total_s: 2044.097107887268
  timers:
    learn_throughput: 763.978
    learn_time_ms: 5235.754
    load_throughput: 889768.929
    load_time_ms: 4.496
    sample_throughput: 59.422
    sample_time_ms: 67315.468
    update_time_ms: 3.938
  timestamp: 1651030542
  timesteps_since_restore: 0
  timesteps_total: 124000
  training_iteration: 31
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     31 |           2044.1 | 124000 | -5.22021 |             -0.83227 |             -11.7594 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 128000
  custom_metrics:
    eps_sum_utility_max: -93.89158494998489
    eps_sum_utility_mean: -718.5205686535651
    eps_sum_utility_min: -1736.2133577273355
    sum_utility_max: 29.18991785778003
    sum_utility_mean: 7.555080987356827
    sum_utility_min: -45.356470213608134
  date: 2022-04-27_09-06-56
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -0.8322704233592326
  episode_reward_mean: -4.775836222786612
  episode_reward_min: -11.759397410840439
  episodes_this_iter: 40
  episodes_total: 1280
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.43541431427002
          entropy_coeff: 0.0
          kl: 0.015376257710158825
          model: {}
          policy_loss: -0.11736913025379181
          total_loss: 0.802937388420105
          vf_explained_var: 0.7462323904037476
          vf_loss: 0.8969537615776062
    num_agent_steps_sampled: 128000
    num_agent_steps_trained: 128000
    num_steps_sampled: 128000
    num_steps_trained: 128000
  iterations_since_restore: 32
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.17572815533981
    ram_util_percent: 60.336893203883506
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.065085486403374
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 28.654854564327323
    mean_inference_ms: 1.114782555538995
    mean_raw_obs_processing_ms: 0.2509893844097295
  time_since_restore: 2118.131603002548
  time_this_iter_s: 74.03449511528015
  time_total_s: 2118.131603002548
  timers:
    learn_throughput: 751.921
    learn_time_ms: 5319.706
    load_throughput: 848405.36
    load_time_ms: 4.715
    sample_throughput: 59.085
    sample_time_ms: 67698.845
    update_time_ms: 4.013
  timestamp: 1651030616
  timesteps_since_restore: 0
  timesteps_total: 128000
  training_iteration: 32
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     32 |          2118.13 | 128000 | -4.77584 |             -0.83227 |             -11.7594 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 132000
  custom_metrics:
    eps_sum_utility_max: 114.67357575537663
    eps_sum_utility_mean: -649.916631296989
    eps_sum_utility_min: -1518.957497154855
    sum_utility_max: 29.18991785778003
    sum_utility_mean: 6.7241610959978
    sum_utility_min: -45.356470213608134
  date: 2022-04-27_09-08-13
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 0.6061125834103767
  episode_reward_mean: -4.308742771716267
  episode_reward_min: -9.421933271739052
  episodes_this_iter: 40
  episodes_total: 1320
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.378499984741211
          entropy_coeff: 0.0
          kl: 0.016047846525907516
          model: {}
          policy_loss: -0.12172240763902664
          total_loss: 0.8523741364479065
          vf_explained_var: 0.7195805907249451
          vf_loss: 0.9497239589691162
    num_agent_steps_sampled: 132000
    num_agent_steps_trained: 132000
    num_steps_sampled: 132000
    num_steps_trained: 132000
  iterations_since_restore: 33
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.64074074074074
    ram_util_percent: 60.334259259259255
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06512438687404684
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 28.78375027021653
    mean_inference_ms: 1.1154579828375981
    mean_raw_obs_processing_ms: 0.25119783471258095
  time_since_restore: 2195.211920261383
  time_this_iter_s: 77.08031725883484
  time_total_s: 2195.211920261383
  timers:
    learn_throughput: 745.169
    learn_time_ms: 5367.908
    load_throughput: 856526.662
    load_time_ms: 4.67
    sample_throughput: 58.487
    sample_time_ms: 68391.674
    update_time_ms: 4.098
  timestamp: 1651030693
  timesteps_since_restore: 0
  timesteps_total: 132000
  training_iteration: 33
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     33 |          2195.21 | 132000 | -4.30874 |             0.606113 |             -9.42193 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 136000
  custom_metrics:
    eps_sum_utility_max: 147.19165041762932
    eps_sum_utility_mean: -539.5021390489896
    eps_sum_utility_min: -1518.957497154855
    sum_utility_max: 28.246274707011146
    sum_utility_mean: 9.32731302996812
    sum_utility_min: -34.05001021325872
  date: 2022-04-27_09-09-32
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 0.8497836147851073
  episode_reward_mean: -3.6130225966732104
  episode_reward_min: -9.421933271739052
  episodes_this_iter: 40
  episodes_total: 1360
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.332825660705566
          entropy_coeff: 0.0
          kl: 0.01528665330260992
          model: {}
          policy_loss: -0.116086445748806
          total_loss: 0.58884197473526
          vf_explained_var: 0.7337973713874817
          vf_loss: 0.681711733341217
    num_agent_steps_sampled: 136000
    num_agent_steps_trained: 136000
    num_steps_sampled: 136000
    num_steps_trained: 136000
  iterations_since_restore: 34
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.015740740740746
    ram_util_percent: 60.354629629629635
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06520422834541734
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 28.94061372787092
    mean_inference_ms: 1.116853350055723
    mean_raw_obs_processing_ms: 0.25153435838075716
  time_since_restore: 2273.5281488895416
  time_this_iter_s: 78.31622862815857
  time_total_s: 2273.5281488895416
  timers:
    learn_throughput: 755.329
    learn_time_ms: 5295.706
    load_throughput: 876566.299
    load_time_ms: 4.563
    sample_throughput: 57.787
    sample_time_ms: 69219.206
    update_time_ms: 3.967
  timestamp: 1651030772
  timesteps_since_restore: 0
  timesteps_total: 136000
  training_iteration: 34
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     34 |          2273.53 | 136000 | -3.61302 |             0.849784 |             -9.42193 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 140000
  custom_metrics:
    eps_sum_utility_max: 329.59396272601197
    eps_sum_utility_mean: -441.3999441246724
    eps_sum_utility_min: -1358.1499473173592
    sum_utility_max: 28.246274707011146
    sum_utility_mean: 8.654793224120713
    sum_utility_min: -48.47557523601027
  date: 2022-04-27_09-10-44
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1.867347505331663
  episode_reward_mean: -2.9800973710824445
  episode_reward_min: -8.885467728769445
  episodes_this_iter: 40
  episodes_total: 1400
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.316096305847168
          entropy_coeff: 0.0
          kl: 0.014857589267194271
          model: {}
          policy_loss: -0.1141098365187645
          total_loss: 0.7099305987358093
          vf_explained_var: 0.6714085340499878
          vf_loss: 0.801475465297699
    num_agent_steps_sampled: 140000
    num_agent_steps_trained: 140000
    num_steps_sampled: 140000
    num_steps_trained: 140000
  iterations_since_restore: 35
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.116831683168314
    ram_util_percent: 60.35049504950495
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06524542344530229
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.07333455434268
    mean_inference_ms: 1.1176417401179934
    mean_raw_obs_processing_ms: 0.2516785685780536
  time_since_restore: 2345.6822350025177
  time_this_iter_s: 72.15408611297607
  time_total_s: 2345.6822350025177
  timers:
    learn_throughput: 755.521
    learn_time_ms: 5294.362
    load_throughput: 875861.572
    load_time_ms: 4.567
    sample_throughput: 57.404
    sample_time_ms: 69681.283
    update_time_ms: 3.952
  timestamp: 1651030844
  timesteps_since_restore: 0
  timesteps_total: 140000
  training_iteration: 35
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     35 |          2345.68 | 140000 |  -2.9801 |              1.86735 |             -8.88547 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 144000
  custom_metrics:
    eps_sum_utility_max: 425.0144960304199
    eps_sum_utility_mean: -319.4447373012246
    eps_sum_utility_min: -1070.5423693788925
    sum_utility_max: 28.246274707011146
    sum_utility_mean: 9.065094715575873
    sum_utility_min: -48.47557523601027
  date: 2022-04-27_09-11-58
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 2.968831222413214
  episode_reward_mean: -2.1929968704890475
  episode_reward_min: -7.177724373751839
  episodes_this_iter: 40
  episodes_total: 1440
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.261931419372559
          entropy_coeff: 0.0
          kl: 0.014972838573157787
          model: {}
          policy_loss: -0.11460887640714645
          total_loss: 0.5794163346290588
          vf_explained_var: 0.6969913244247437
          vf_loss: 0.6712852716445923
    num_agent_steps_sampled: 144000
    num_agent_steps_trained: 144000
    num_steps_sampled: 144000
    num_steps_trained: 144000
  iterations_since_restore: 36
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.935922330097085
    ram_util_percent: 60.337864077669906
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06524675031101651
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.183174617929208
    mean_inference_ms: 1.1177449345379946
    mean_raw_obs_processing_ms: 0.25167556124188983
  time_since_restore: 2419.873759508133
  time_this_iter_s: 74.19152450561523
  time_total_s: 2419.873759508133
  timers:
    learn_throughput: 757.427
    learn_time_ms: 5281.037
    load_throughput: 900181.139
    load_time_ms: 4.444
    sample_throughput: 57.158
    sample_time_ms: 69981.653
    update_time_ms: 3.914
  timestamp: 1651030918
  timesteps_since_restore: 0
  timesteps_total: 144000
  training_iteration: 36
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     36 |          2419.87 | 144000 |   -2.193 |              2.96883 |             -7.17772 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 148000
  custom_metrics:
    eps_sum_utility_max: 425.0144960304199
    eps_sum_utility_mean: -235.05687515171846
    eps_sum_utility_min: -1070.5423693788925
    sum_utility_max: 26.972411197884473
    sum_utility_mean: 11.680661481741774
    sum_utility_min: -48.47557523601027
  date: 2022-04-27_09-13-13
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 2.968831222413214
  episode_reward_mean: -1.6295580581135176
  episode_reward_min: -7.177724373751839
  episodes_this_iter: 40
  episodes_total: 1480
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.226832389831543
          entropy_coeff: 0.0
          kl: 0.015315565280616283
          model: {}
          policy_loss: -0.11186365783214569
          total_loss: 0.4960211217403412
          vf_explained_var: 0.7004239559173584
          vf_loss: 0.5846242308616638
    num_agent_steps_sampled: 148000
    num_agent_steps_trained: 148000
    num_steps_sampled: 148000
    num_steps_trained: 148000
  iterations_since_restore: 37
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.789320388349516
    ram_util_percent: 60.35533980582524
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06523596103030059
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.279812649444548
    mean_inference_ms: 1.1176274848322905
    mean_raw_obs_processing_ms: 0.25164625091947085
  time_since_restore: 2494.2360455989838
  time_this_iter_s: 74.36228609085083
  time_total_s: 2494.2360455989838
  timers:
    learn_throughput: 768.991
    learn_time_ms: 5201.621
    load_throughput: 894303.122
    load_time_ms: 4.473
    sample_throughput: 57.031
    sample_time_ms: 70137.29
    update_time_ms: 3.783
  timestamp: 1651030993
  timesteps_since_restore: 0
  timesteps_total: 148000
  training_iteration: 37
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     37 |          2494.24 | 148000 | -1.62956 |              2.96883 |             -7.17772 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 152000
  custom_metrics:
    eps_sum_utility_max: 509.4697055115432
    eps_sum_utility_mean: -164.46082648626682
    eps_sum_utility_min: -972.4655356371759
    sum_utility_max: 27.884852835933778
    sum_utility_mean: 12.355558163220557
    sum_utility_min: -36.40315126813498
  date: 2022-04-27_09-14-27
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 3.5454085619509463
  episode_reward_mean: -1.1402785570199228
  episode_reward_min: -6.131789858445727
  episodes_this_iter: 40
  episodes_total: 1520
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.153668403625488
          entropy_coeff: 0.0
          kl: 0.01604393869638443
          model: {}
          policy_loss: -0.11909158527851105
          total_loss: 0.4708636701107025
          vf_explained_var: 0.6598050594329834
          vf_loss: 0.5655885338783264
    num_agent_steps_sampled: 152000
    num_agent_steps_trained: 152000
    num_steps_sampled: 152000
    num_steps_trained: 152000
  iterations_since_restore: 38
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.97788461538461
    ram_util_percent: 60.338461538461544
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06523481508183329
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.379111980552334
    mean_inference_ms: 1.117679895387136
    mean_raw_obs_processing_ms: 0.2516552515311655
  time_since_restore: 2568.5372788906097
  time_this_iter_s: 74.30123329162598
  time_total_s: 2568.5372788906097
  timers:
    learn_throughput: 784.182
    learn_time_ms: 5100.855
    load_throughput: 895725.963
    load_time_ms: 4.466
    sample_throughput: 57.397
    sample_time_ms: 69689.961
    update_time_ms: 3.753
  timestamp: 1651031067
  timesteps_since_restore: 0
  timesteps_total: 152000
  training_iteration: 38
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     38 |          2568.54 | 152000 | -1.14028 |              3.54541 |             -6.13179 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 156000
  custom_metrics:
    eps_sum_utility_max: 509.4697055115432
    eps_sum_utility_mean: -81.84449103955313
    eps_sum_utility_min: -972.4655356371759
    sum_utility_max: 27.884852835933778
    sum_utility_mean: 11.433561465111415
    sum_utility_min: -26.321169249408747
  date: 2022-04-27_09-15-42
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 3.5454085619509463
  episode_reward_mean: -0.5890510852027724
  episode_reward_min: -5.934740240953666
  episodes_this_iter: 40
  episodes_total: 1560
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.120360374450684
          entropy_coeff: 0.0
          kl: 0.014923756942152977
          model: {}
          policy_loss: -0.1158115491271019
          total_loss: 0.4307622015476227
          vf_explained_var: 0.663394033908844
          vf_loss: 0.523908257484436
    num_agent_steps_sampled: 156000
    num_agent_steps_trained: 156000
    num_steps_sampled: 156000
    num_steps_trained: 156000
  iterations_since_restore: 39
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.152884615384615
    ram_util_percent: 60.3673076923077
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06523674328410663
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.476796846357164
    mean_inference_ms: 1.1177796914396723
    mean_raw_obs_processing_ms: 0.2516623522763641
  time_since_restore: 2643.5052366256714
  time_this_iter_s: 74.96795773506165
  time_total_s: 2643.5052366256714
  timers:
    learn_throughput: 791.394
    learn_time_ms: 5054.371
    load_throughput: 892400.36
    load_time_ms: 4.482
    sample_throughput: 57.394
    sample_time_ms: 69693.359
    update_time_ms: 3.693
  timestamp: 1651031142
  timesteps_since_restore: 0
  timesteps_total: 156000
  training_iteration: 39
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+-----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |    reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+-----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     39 |          2643.51 | 156000 | -0.589051 |              3.54541 |             -5.93474 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+-----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 160000
  custom_metrics:
    eps_sum_utility_max: 520.4538774988142
    eps_sum_utility_mean: -25.390932180083936
    eps_sum_utility_min: -678.7417995916609
    sum_utility_max: 27.85960855997483
    sum_utility_mean: 11.759726443923633
    sum_utility_min: -26.321169249408747
  date: 2022-04-27_09-16-57
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 3.3415384438040467
  episode_reward_mean: -0.2578481723883147
  episode_reward_min: -3.786553164708469
  episodes_this_iter: 40
  episodes_total: 1600
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.084065437316895
          entropy_coeff: 0.0
          kl: 0.014584328979253769
          model: {}
          policy_loss: -0.11435604840517044
          total_loss: 0.36569976806640625
          vf_explained_var: 0.7163110971450806
          vf_loss: 0.4579058289527893
    num_agent_steps_sampled: 160000
    num_agent_steps_trained: 160000
    num_steps_sampled: 160000
    num_steps_trained: 160000
  iterations_since_restore: 40
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.78173076923077
    ram_util_percent: 60.353846153846156
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.0652385584594713
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.57214777802135
    mean_inference_ms: 1.1178633635568587
    mean_raw_obs_processing_ms: 0.251709627743678
  time_since_restore: 2718.564076423645
  time_this_iter_s: 75.05883979797363
  time_total_s: 2718.564076423645
  timers:
    learn_throughput: 789.501
    learn_time_ms: 5066.494
    load_throughput: 861010.29
    load_time_ms: 4.646
    sample_throughput: 57.526
    sample_time_ms: 69534.132
    update_time_ms: 3.713
  timestamp: 1651031217
  timesteps_since_restore: 0
  timesteps_total: 160000
  training_iteration: 40
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+-----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |    reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+-----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     40 |          2718.56 | 160000 | -0.257848 |              3.34154 |             -3.78655 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+-----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 164000
  custom_metrics:
    eps_sum_utility_max: 546.4527618519451
    eps_sum_utility_mean: 53.35523845074811
    eps_sum_utility_min: -551.4652577028622
    sum_utility_max: 28.295331219393727
    sum_utility_mean: 15.512449153820471
    sum_utility_min: -25.544653845664964
  date: 2022-04-27_09-18-13
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 3.3415384438040467
  episode_reward_mean: 0.2077690299797204
  episode_reward_min: -3.6181350338280467
  episodes_this_iter: 40
  episodes_total: 1640
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.03648567199707
          entropy_coeff: 0.0
          kl: 0.014969990588724613
          model: {}
          policy_loss: -0.1166989728808403
          total_loss: 0.34413614869117737
          vf_explained_var: 0.6980826258659363
          vf_loss: 0.4380994737148285
    num_agent_steps_sampled: 164000
    num_agent_steps_trained: 164000
    num_steps_sampled: 164000
    num_steps_trained: 164000
  iterations_since_restore: 41
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.26320754716981
    ram_util_percent: 60.363207547169814
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.0652344655703701
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.66364010917974
    mean_inference_ms: 1.1178227212245033
    mean_raw_obs_processing_ms: 0.2517386618836212
  time_since_restore: 2794.3692450523376
  time_this_iter_s: 75.80516862869263
  time_total_s: 2794.3692450523376
  timers:
    learn_throughput: 774.745
    learn_time_ms: 5162.991
    load_throughput: 860639.277
    load_time_ms: 4.648
    sample_throughput: 57.269
    sample_time_ms: 69845.215
    update_time_ms: 3.799
  timestamp: 1651031293
  timesteps_since_restore: 0
  timesteps_total: 164000
  training_iteration: 41
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     41 |          2794.37 | 164000 | 0.207769 |              3.34154 |             -3.61814 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 168000
  custom_metrics:
    eps_sum_utility_max: 546.4527618519451
    eps_sum_utility_mean: 120.65468662139885
    eps_sum_utility_min: -420.1109832476842
    sum_utility_max: 28.295331219393727
    sum_utility_mean: 15.376582578059933
    sum_utility_min: -15.278855154786566
  date: 2022-04-27_09-19-30
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 3.3415384438040467
  episode_reward_mean: 0.6480297751303827
  episode_reward_min: -3.2309577750335787
  episodes_this_iter: 40
  episodes_total: 1680
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 15.005556106567383
          entropy_coeff: 0.0
          kl: 0.015045714564621449
          model: {}
          policy_loss: -0.11522527039051056
          total_loss: 0.2512408196926117
          vf_explained_var: 0.6929417848587036
          vf_loss: 0.3436153829097748
    num_agent_steps_sampled: 168000
    num_agent_steps_trained: 168000
    num_steps_sampled: 168000
    num_steps_trained: 168000
  iterations_since_restore: 42
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.36261682242991
    ram_util_percent: 60.40093457943925
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06523655646720627
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.760493892836063
    mean_inference_ms: 1.1179339607470404
    mean_raw_obs_processing_ms: 0.25176388789729914
  time_since_restore: 2871.3817842006683
  time_this_iter_s: 77.01253914833069
  time_total_s: 2871.3817842006683
  timers:
    learn_throughput: 782.906
    learn_time_ms: 5109.167
    load_throughput: 909526.458
    load_time_ms: 4.398
    sample_throughput: 56.982
    sample_time_ms: 70197.441
    update_time_ms: 3.782
  timestamp: 1651031370
  timesteps_since_restore: 0
  timesteps_total: 168000
  training_iteration: 42
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     42 |          2871.38 | 168000 |  0.64803 |              3.34154 |             -3.23096 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 172000
  custom_metrics:
    eps_sum_utility_max: 597.3348586438746
    eps_sum_utility_mean: 170.4039921067281
    eps_sum_utility_min: -404.5981165099473
    sum_utility_max: 28.201771128674586
    sum_utility_mean: 16.440701522987506
    sum_utility_min: -15.405031731447078
  date: 2022-04-27_09-20-47
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 3.724637045991196
  episode_reward_mean: 0.9696901529782126
  episode_reward_min: -2.6835122194253382
  episodes_this_iter: 40
  episodes_total: 1720
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 14.9456205368042
          entropy_coeff: 0.0
          kl: 0.014835200272500515
          model: {}
          policy_loss: -0.11345575749874115
          total_loss: 0.3656879961490631
          vf_explained_var: 0.6334649324417114
          vf_loss: 0.45661279559135437
    num_agent_steps_sampled: 172000
    num_agent_steps_trained: 172000
    num_steps_sampled: 172000
    num_steps_trained: 172000
  iterations_since_restore: 43
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.5626168224299
    ram_util_percent: 60.417757009345785
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.0652378649001342
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.855105698709238
    mean_inference_ms: 1.1180701543223375
    mean_raw_obs_processing_ms: 0.2517845603364559
  time_since_restore: 2948.6058044433594
  time_this_iter_s: 77.22402024269104
  time_total_s: 2948.6058044433594
  timers:
    learn_throughput: 763.898
    learn_time_ms: 5236.302
    load_throughput: 903433.726
    load_time_ms: 4.428
    sample_throughput: 57.074
    sample_time_ms: 70084.968
    update_time_ms: 3.678
  timestamp: 1651031447
  timesteps_since_restore: 0
  timesteps_total: 172000
  training_iteration: 43
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     43 |          2948.61 | 172000 |  0.96969 |              3.72464 |             -2.68351 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 176000
  custom_metrics:
    eps_sum_utility_max: 670.1680607049789
    eps_sum_utility_mean: 228.34996002611427
    eps_sum_utility_min: -404.5981165099473
    sum_utility_max: 28.201771128674586
    sum_utility_mean: 16.710202711940436
    sum_utility_min: -25.66425303239653
  date: 2022-04-27_09-22-05
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 4.086186972398015
  episode_reward_mean: 1.3306406946320348
  episode_reward_min: -2.6835122194253382
  episodes_this_iter: 40
  episodes_total: 1760
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 14.91672420501709
          entropy_coeff: 0.0
          kl: 0.015141165815293789
          model: {}
          policy_loss: -0.11416412144899368
          total_loss: 0.17629124224185944
          vf_explained_var: 0.7651747465133667
          vf_loss: 0.2674597501754761
    num_agent_steps_sampled: 176000
    num_agent_steps_trained: 176000
    num_steps_sampled: 176000
    num_steps_trained: 176000
  iterations_since_restore: 44
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.97383177570093
    ram_util_percent: 60.41308411214952
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06524371998168299
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.95058430172464
    mean_inference_ms: 1.1187373805467251
    mean_raw_obs_processing_ms: 0.2518022275427091
  time_since_restore: 3025.5710270404816
  time_this_iter_s: 76.96522259712219
  time_total_s: 3025.5710270404816
  timers:
    learn_throughput: 762.965
    learn_time_ms: 5242.702
    load_throughput: 884034.988
    load_time_ms: 4.525
    sample_throughput: 57.189
    sample_time_ms: 69943.322
    update_time_ms: 3.702
  timestamp: 1651031525
  timesteps_since_restore: 0
  timesteps_total: 176000
  training_iteration: 44
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     44 |          3025.57 | 176000 |  1.33064 |              4.08619 |             -2.68351 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 180000
  custom_metrics:
    eps_sum_utility_max: 715.3720388870037
    eps_sum_utility_mean: 305.597017019189
    eps_sum_utility_min: -341.57003935599636
    sum_utility_max: 27.88114633820187
    sum_utility_mean: 17.379963441873166
    sum_utility_min: -25.66425303239653
  date: 2022-04-27_09-23-22
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 4.235664753511351
  episode_reward_mean: 1.7673505718630873
  episode_reward_min: -2.2049499267544697
  episodes_this_iter: 40
  episodes_total: 1800
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 14.875986099243164
          entropy_coeff: 0.0
          kl: 0.014340859837830067
          model: {}
          policy_loss: -0.10825514048337936
          total_loss: 0.19397057592868805
          vf_explained_var: 0.7411310076713562
          vf_loss: 0.28044548630714417
    num_agent_steps_sampled: 180000
    num_agent_steps_trained: 180000
    num_steps_sampled: 180000
    num_steps_trained: 180000
  iterations_since_restore: 45
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.897222222222226
    ram_util_percent: 60.40648148148148
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.0652532654444207
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 30.044560353636534
    mean_inference_ms: 1.119398880694131
    mean_raw_obs_processing_ms: 0.25183679060489284
  time_since_restore: 3102.9081938266754
  time_this_iter_s: 77.33716678619385
  time_total_s: 3102.9081938266754
  timers:
    learn_throughput: 762.075
    learn_time_ms: 5248.828
    load_throughput: 887434.529
    load_time_ms: 4.507
    sample_throughput: 56.773
    sample_time_ms: 70455.442
    update_time_ms: 3.71
  timestamp: 1651031602
  timesteps_since_restore: 0
  timesteps_total: 180000
  training_iteration: 45
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     45 |          3102.91 | 180000 |  1.76735 |              4.23566 |             -2.20495 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 184000
  custom_metrics:
    eps_sum_utility_max: 866.0869498482514
    eps_sum_utility_mean: 360.10521625687574
    eps_sum_utility_min: -45.40415609895688
    sum_utility_max: 28.512940157204817
    sum_utility_mean: 16.885134336765713
    sum_utility_min: -16.58829579159893
  date: 2022-04-27_09-24-39
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 5.253502522080725
  episode_reward_mean: 2.129011168110037
  episode_reward_min: -0.8075073327043858
  episodes_this_iter: 40
  episodes_total: 1840
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 14.813103675842285
          entropy_coeff: 0.0
          kl: 0.014560787007212639
          model: {}
          policy_loss: -0.11040383577346802
          total_loss: 0.1747482568025589
          vf_explained_var: 0.7250895500183105
          vf_loss: 0.26303789019584656
    num_agent_steps_sampled: 184000
    num_agent_steps_trained: 184000
    num_steps_sampled: 184000
    num_steps_trained: 184000
  iterations_since_restore: 46
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.07943925233644
    ram_util_percent: 60.40654205607477
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.0652623475399283
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 30.13629029287171
    mean_inference_ms: 1.1200362122878087
    mean_raw_obs_processing_ms: 0.2518713731625346
  time_since_restore: 3180.030368089676
  time_this_iter_s: 77.12217426300049
  time_total_s: 3180.030368089676
  timers:
    learn_throughput: 751.298
    learn_time_ms: 5324.117
    load_throughput: 868597.226
    load_time_ms: 4.605
    sample_throughput: 56.599
    sample_time_ms: 70672.675
    update_time_ms: 3.819
  timestamp: 1651031679
  timesteps_since_restore: 0
  timesteps_total: 184000
  training_iteration: 46
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     46 |          3180.03 | 184000 |  2.12901 |               5.2535 |            -0.807507 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 188000
  custom_metrics:
    eps_sum_utility_max: 866.0869498482514
    eps_sum_utility_mean: 394.0417118609642
    eps_sum_utility_min: -45.40415609895688
    sum_utility_max: 28.512940157204817
    sum_utility_mean: 16.779715739669687
    sum_utility_min: -16.348843187956195
  date: 2022-04-27_09-25-59
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 5.253502522080725
  episode_reward_mean: 2.3511423085936807
  episode_reward_min: -0.3546386864866154
  episodes_this_iter: 40
  episodes_total: 1880
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 14.785492897033691
          entropy_coeff: 0.0
          kl: 0.014337786473333836
          model: {}
          policy_loss: -0.1114690825343132
          total_loss: 0.13109266757965088
          vf_explained_var: 0.7700640559196472
          vf_loss: 0.22078624367713928
    num_agent_steps_sampled: 188000
    num_agent_steps_trained: 188000
    num_steps_sampled: 188000
    num_steps_trained: 188000
  iterations_since_restore: 47
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.66160714285714
    ram_util_percent: 60.40892857142857
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06529095894321091
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 30.23752687414519
    mean_inference_ms: 1.1205319106046756
    mean_raw_obs_processing_ms: 0.2519707429495813
  time_since_restore: 3260.2052116394043
  time_this_iter_s: 80.1748435497284
  time_total_s: 3260.2052116394043
  timers:
    learn_throughput: 748.31
    learn_time_ms: 5345.377
    load_throughput: 865608.09
    load_time_ms: 4.621
    sample_throughput: 56.154
    sample_time_ms: 71232.36
    update_time_ms: 3.902
  timestamp: 1651031759
  timesteps_since_restore: 0
  timesteps_total: 188000
  training_iteration: 47
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     47 |          3260.21 | 188000 |  2.35114 |               5.2535 |            -0.354639 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 192000
  custom_metrics:
    eps_sum_utility_max: 832.1848021372749
    eps_sum_utility_mean: 419.2776254850068
    eps_sum_utility_min: 52.051140663802045
    sum_utility_max: 28.880265661216548
    sum_utility_mean: 17.39846017010235
    sum_utility_min: -45.36617840209533
  date: 2022-04-27_09-27-17
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 5.253502522080725
  episode_reward_mean: 2.517911031835937
  episode_reward_min: 0.13626085107668987
  episodes_this_iter: 40
  episodes_total: 1920
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 14.73082160949707
          entropy_coeff: 0.0
          kl: 0.015215080231428146
          model: {}
          policy_loss: -0.11372361332178116
          total_loss: 0.10054973512887955
          vf_explained_var: 0.7872873544692993
          vf_loss: 0.19116544723510742
    num_agent_steps_sampled: 192000
    num_agent_steps_trained: 192000
    num_steps_sampled: 192000
    num_steps_trained: 192000
  iterations_since_restore: 48
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.890654205607476
    ram_util_percent: 60.37570093457943
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06531911991822292
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 30.33614403537721
    mean_inference_ms: 1.1210291377648514
    mean_raw_obs_processing_ms: 0.2520764123218539
  time_since_restore: 3337.232128381729
  time_this_iter_s: 77.02691674232483
  time_total_s: 3337.232128381729
  timers:
    learn_throughput: 747.722
    learn_time_ms: 5349.584
    load_throughput: 882783.703
    load_time_ms: 4.531
    sample_throughput: 55.943
    sample_time_ms: 71500.787
    update_time_ms: 3.834
  timestamp: 1651031837
  timesteps_since_restore: 0
  timesteps_total: 192000
  training_iteration: 48
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     48 |          3337.23 | 192000 |  2.51791 |               5.2535 |             0.136261 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 196000
  custom_metrics:
    eps_sum_utility_max: 832.1848021372749
    eps_sum_utility_mean: 454.16505368997025
    eps_sum_utility_min: -206.41528425294257
    sum_utility_max: 28.880265661216548
    sum_utility_mean: 18.23170393025118
    sum_utility_min: -45.36617840209533
  date: 2022-04-27_09-28-35
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 5.145716249345292
  episode_reward_mean: 2.744225155488076
  episode_reward_min: -1.142439812907322
  episodes_this_iter: 40
  episodes_total: 1960
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 14.694319725036621
          entropy_coeff: 0.0
          kl: 0.014034293591976166
          model: {}
          policy_loss: -0.10586970299482346
          total_loss: 0.2526847720146179
          vf_explained_var: 0.6772597432136536
          vf_loss: 0.3372398614883423
    num_agent_steps_sampled: 196000
    num_agent_steps_trained: 196000
    num_steps_sampled: 196000
    num_steps_trained: 196000
  iterations_since_restore: 49
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 34.06238532110091
    ram_util_percent: 60.37247706422019
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06534077467554213
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 30.42948949236181
    mean_inference_ms: 1.121387571306383
    mean_raw_obs_processing_ms: 0.2521569253805079
  time_since_restore: 3415.3304789066315
  time_this_iter_s: 78.09835052490234
  time_total_s: 3415.3304789066315
  timers:
    learn_throughput: 747.037
    learn_time_ms: 5354.488
    load_throughput: 884594.327
    load_time_ms: 4.522
    sample_throughput: 55.703
    sample_time_ms: 71808.794
    update_time_ms: 3.917
  timestamp: 1651031915
  timesteps_since_restore: 0
  timesteps_total: 196000
  training_iteration: 49
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     49 |          3415.33 | 196000 |  2.74423 |              5.14572 |             -1.14244 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_50e5a_00000:
  agent_timesteps_total: 200000
  custom_metrics:
    eps_sum_utility_max: 921.6113390147046
    eps_sum_utility_mean: 473.7286957365811
    eps_sum_utility_min: -206.41528425294257
    sum_utility_max: 28.880265661216548
    sum_utility_mean: 19.78712922984106
    sum_utility_min: -16.371637423852288
  date: 2022-04-27_09-29-52
  done: true
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 5.68461773986399
  episode_reward_mean: 2.9079750349457667
  episode_reward_min: -1.142439812907322
  episodes_this_iter: 40
  episodes_total: 2000
  experiment_id: c64f1898cbc641838b31b032aaaabd69
  hostname: abhishek-pc
  info:
    learner:
      default_policy:
        learner_stats:
          cur_kl_coeff: 1.5187499523162842
          cur_lr: 4.999999873689376e-05
          entropy: 14.680994987487793
          entropy_coeff: 0.0
          kl: 0.014259634539484978
          model: {}
          policy_loss: -0.10996134579181671
          total_loss: 0.1376059353351593
          vf_explained_var: 0.7583587169647217
          vf_loss: 0.22591045498847961
    num_agent_steps_sampled: 200000
    num_agent_steps_trained: 200000
    num_steps_sampled: 200000
    num_steps_trained: 200000
  iterations_since_restore: 50
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 33.848598130841125
    ram_util_percent: 60.353271028037376
  pid: 123255
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.06535026052498343
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 30.512161023659015
    mean_inference_ms: 1.121503334432687
    mean_raw_obs_processing_ms: 0.25220071051587334
  time_since_restore: 3492.691193342209
  time_this_iter_s: 77.36071443557739
  time_total_s: 3492.691193342209
  timers:
    learn_throughput: 741.458
    learn_time_ms: 5394.773
    load_throughput: 907877.66
    load_time_ms: 4.406
    sample_throughput: 55.557
    sample_time_ms: 71998.643
    update_time_ms: 3.964
  timestamp: 1651031992
  timesteps_since_restore: 0
  timesteps_total: 200000
  training_iteration: 50
  trial_id: 50e5a_00000
  
== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc               |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | RUNNING  | 10.0.3.106:123255 |     50 |          3492.69 | 200000 |  2.90798 |              5.68462 |             -1.14244 |                100 |
+-----------------------------------+----------+-------------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


== Status ==
Memory usage on this node: 4.6/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/2.85 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21
Number of trials: 1/1 (1 TERMINATED)
+-----------------------------------+------------+-------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status     | loc   |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+------------+-------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_50e5a_00000 | TERMINATED |       |     50 |          3492.69 | 200000 |  2.90798 |              5.68462 |             -1.14244 |                100 |
+-----------------------------------+------------+-------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


2022-04-27 09:29:53,621	INFO tune.py:549 -- Total run time: 3512.38 seconds (3511.51 seconds for the tuning loop).
INFO:deepcomp.util.simulation:Training done                  episode_reward_mean=2.908 episodes_total=2000 log_dir=/home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21/PPO_CentralRelNormEnv_50e5a_00000_0_2022-04-27_08-31-21 num_steps_sampled=200000 num_steps_trained=200000 timesteps_total=200000
2022-04-27 09:29:53,797	INFO trainer.py:671 -- Tip: set framework=tfe or the --eager flag to enable TensorFlow eager execution
2022-04-27 09:29:53,797	WARNING deprecation.py:33 -- DeprecationWarning: `monitor` has been deprecated. Use `record_env` instead. This will raise an error in the future!
2022-04-27 09:29:53,798	INFO trainer.py:696 -- Current log_level is ERROR. For more information, set 'log_level': 'INFO' / 'DEBUG' or use the -v and -vv flags.
2022-04-27 09:30:06,468	INFO trainable.py:101 -- Trainable.setup took 12.694 seconds. If your trainable is slow to initialize, consider setting reuse_actors=True to reduce actor creation overheads.
INFO:deepcomp.util.simulation:Loading PPO agent              checkpoint=/home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21/PPO_CentralRelNormEnv_50e5a_00000_0_2022-04-27_08-31-21/checkpoint_000050/checkpoint-50
2022-04-27 09:30:06,647	INFO trainable.py:377 -- Restored on 10.0.3.106 from checkpoint: /home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21/PPO_CentralRelNormEnv_50e5a_00000_0_2022-04-27_08-31-21/checkpoint_000050/checkpoint-50
2022-04-27 09:30:06,647	INFO trainable.py:385 -- Current state after restoring: {'_iteration': 50, '_timesteps_total': None, '_time_total': 3492.691193342209, '_episodes_total': 2000}
INFO:deepcomp.util.simulation:Agent loaded                   agent=PPO checkpoint=None rllib_dir=/home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21/PPO_CentralRelNormEnv_50e5a_00000_0_2022-04-27_08-31-21/checkpoint_000050/checkpoint-50
INFO:deepcomp.util.simulation:Loaded training progress       progress_file=/home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21/PPO_CentralRelNormEnv_50e5a_00000_0_2022-04-27_08-31-21/progress.csv train_iteration=50 train_steps=200000
WARNING:deepcomp.util.simulation:Evaluating with a single worker for reproducibility and compatibility.
INFO:deepcomp.util.simulation:Starting evaluation            fast_ues=2 num_episodes=1 num_workers=1 slow_ues=5 static_ues=1
DEBUG:deepcomp.util.simulation:Step                           action=[6, 3, 2, 6, 3, 5, 1, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 0.048, 1.0, 0.01, 0.002, 0.002, 0.004, 0.021, 1.0, 0.008, 0.002, 0.002, 0.004, 0.04, 0.006, 0.001, 0.001, 0.001, 0.003, 1.0, 0.011, 0.036, 0.016, 1.0, 0.025, 0.004, 0.002, 0.003, 1.0, 0.03, 0.071, 0.584, 0.654, 0.076, 0.031, 1.0, 0.007, 0.004, 0.004, 0.008, 0.016, 0.016, 0.028, 0.009, 0.077, 1.0, 0.025, 0.006, 0.005], 'utility': [0.09, 0.125, 0.372, 0.173, 0.162, -0.178, 0.499, -0.04]} obs={'connected': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.014, 0.044, 1.0, 0.01, 0.002, 0.002, 0.004, 0.018, 1.0, 0.008, 0.002, 0.002, 0.003, 0.035, 0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.014, 0.039, 0.016, 1.0, 0.029, 0.004, 0.002, 0.003, 1.0, 0.034, 0.083, 0.787, 0.714, 0.079, 0.033, 1.0, 0.013, 0.007, 0.009, 0.02, 0.055, 0.04, 0.031, 0.011, 0.081, 1.0, 0.029, 0.007, 0.005], 'utility': [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]} reward=0.111 t=1
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 4, 7, 1, 4, 5, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.016, 0.053, 1.0, 0.01, 0.003, 0.002, 0.004, 0.024, 1.0, 0.009, 0.002, 0.002, 0.004, 0.046, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.009, 0.034, 0.016, 1.0, 0.021, 0.003, 0.002, 0.003, 1.0, 0.027, 0.06, 0.438, 0.595, 0.073, 0.029, 1.0, 0.003, 0.002, 0.002, 0.002, 0.004, 0.005, 0.026, 0.008, 0.075, 1.0, 0.021, 0.005, 0.004], 'utility': [-0.247, 0.003, 0.349, 0.576, 0.294, -0.102, 0.717, -0.148]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 0.048, 1.0, 0.01, 0.002, 0.002, 0.004, 0.021, 1.0, 0.008, 0.002, 0.002, 0.004, 0.04, 0.006, 0.001, 0.001, 0.001, 0.003, 1.0, 0.011, 0.036, 0.016, 1.0, 0.025, 0.004, 0.002, 0.003, 1.0, 0.03, 0.071, 0.584, 0.654, 0.076, 0.031, 1.0, 0.007, 0.004, 0.004, 0.008, 0.016, 0.016, 0.028, 0.009, 0.077, 1.0, 0.025, 0.006, 0.005], 'utility': [0.09, 0.125, 0.372, 0.173, 0.162, -0.178, 0.499, -0.04]} reward=0.141 t=2
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 4, 7, 1, 4, 4, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.017, 0.059, 1.0, 0.011, 0.003, 0.002, 0.005, 0.027, 1.0, 0.01, 0.003, 0.002, 0.004, 0.053, 0.004, 0.001, 0.0, 0.001, 0.003, 1.0, 0.008, 0.033, 0.016, 1.0, 0.019, 0.003, 0.002, 0.003, 1.0, 0.025, 0.052, 0.331, 0.538, 0.07, 0.027, 1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002, 0.024, 0.008, 0.074, 1.0, 0.018, 0.005, 0.004], 'utility': [0.057, 0.096, 0.328, 0.372, 0.212, -0.165, 0.897, 0.04]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.016, 0.053, 1.0, 0.01, 0.003, 0.002, 0.004, 0.024, 1.0, 0.009, 0.002, 0.002, 0.004, 0.046, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.009, 0.034, 0.016, 1.0, 0.021, 0.003, 0.002, 0.003, 1.0, 0.027, 0.06, 0.438, 0.595, 0.073, 0.029, 1.0, 0.003, 0.002, 0.002, 0.002, 0.004, 0.005, 0.026, 0.008, 0.075, 1.0, 0.021, 0.005, 0.004], 'utility': [-0.247, 0.003, 0.349, 0.576, 0.294, -0.102, 0.717, -0.148]} reward=0.19 t=3
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 4, 7, 1, 4, 4, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.019, 0.067, 1.0, 0.011, 0.003, 0.002, 0.005, 0.031, 1.0, 0.011, 0.003, 0.002, 0.005, 0.061, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007, 0.032, 0.017, 1.0, 0.017, 0.003, 0.002, 0.003, 1.0, 0.022, 0.044, 0.253, 0.485, 0.068, 0.026, 1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002, 0.023, 0.007, 0.076, 1.0, 0.016, 0.004, 0.003], 'utility': [-0.149, 0.012, 0.306, 0.614, 0.294, -0.161, 0.878, 0.072]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.017, 0.059, 1.0, 0.011, 0.003, 0.002, 0.005, 0.027, 1.0, 0.01, 0.003, 0.002, 0.004, 0.053, 0.004, 0.001, 0.0, 0.001, 0.003, 1.0, 0.008, 0.033, 0.016, 1.0, 0.019, 0.003, 0.002, 0.003, 1.0, 0.025, 0.052, 0.331, 0.538, 0.07, 0.027, 1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002, 0.024, 0.008, 0.074, 1.0, 0.018, 0.005, 0.004], 'utility': [0.057, 0.096, 0.328, 0.372, 0.212, -0.165, 0.897, 0.04]} reward=0.218 t=4
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 4, 7, 1, 4, 4, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.02, 0.077, 1.0, 0.012, 0.003, 0.002, 0.006, 0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.07, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.006, 0.031, 0.018, 1.0, 0.016, 0.003, 0.002, 0.003, 1.0, 0.02, 0.038, 0.196, 0.435, 0.067, 0.024, 1.0, 0.007, 0.004, 0.003, 0.002, 0.002, 0.004, 0.023, 0.007, 0.082, 1.0, 0.015, 0.004, 0.003], 'utility': [0.033, 0.064, 0.285, 0.481, 0.236, -0.159, 0.681, 0.096]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.019, 0.067, 1.0, 0.011, 0.003, 0.002, 0.005, 0.031, 1.0, 0.011, 0.003, 0.002, 0.005, 0.061, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007, 0.032, 0.017, 1.0, 0.017, 0.003, 0.002, 0.003, 1.0, 0.022, 0.044, 0.253, 0.485, 0.068, 0.026, 1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002, 0.023, 0.007, 0.076, 1.0, 0.016, 0.004, 0.003], 'utility': [-0.149, 0.012, 0.306, 0.614, 0.294, -0.161, 0.878, 0.072]} reward=0.233 t=5
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 4, 7, 1, 4, 4, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.023, 0.089, 1.0, 0.012, 0.003, 0.003, 0.006, 0.04, 1.0, 0.013, 0.004, 0.003, 0.006, 0.08, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.031, 0.02, 1.0, 0.015, 0.003, 0.002, 0.003, 1.0, 0.019, 0.033, 0.153, 0.389, 0.066, 0.023, 1.0, 0.022, 0.016, 0.007, 0.004, 0.005, 0.01, 0.024, 0.008, 0.093, 1.0, 0.014, 0.004, 0.003], 'utility': [-0.096, 0.003, 0.265, 0.629, 0.282, -0.16, 0.466, 0.109]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.02, 0.077, 1.0, 0.012, 0.003, 0.002, 0.006, 0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.07, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.006, 0.031, 0.018, 1.0, 0.016, 0.003, 0.002, 0.003, 1.0, 0.02, 0.038, 0.196, 0.435, 0.067, 0.024, 1.0, 0.007, 0.004, 0.003, 0.002, 0.002, 0.004, 0.023, 0.007, 0.082, 1.0, 0.015, 0.004, 0.003], 'utility': [0.033, 0.064, 0.285, 0.481, 0.236, -0.159, 0.681, 0.096]} reward=0.215 t=6
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 4, 7, 1, 4, 4, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.025, 0.104, 1.0, 0.013, 0.004, 0.003, 0.007, 0.045, 1.0, 0.014, 0.004, 0.003, 0.007, 0.092, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.032, 0.022, 1.0, 0.014, 0.003, 0.002, 0.003, 1.0, 0.017, 0.028, 0.122, 0.349, 0.066, 0.023, 1.0, 0.062, 0.052, 0.017, 0.009, 0.009, 0.019, 0.027, 0.008, 0.113, 1.0, 0.015, 0.004, 0.004], 'utility': [0.017, 0.028, 0.245, 0.53, 0.237, -0.162, 0.281, 0.111]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.023, 0.089, 1.0, 0.012, 0.003, 0.003, 0.006, 0.04, 1.0, 0.013, 0.004, 0.003, 0.006, 0.08, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.031, 0.02, 1.0, 0.015, 0.003, 0.002, 0.003, 1.0, 0.019, 0.033, 0.153, 0.389, 0.066, 0.023, 1.0, 0.022, 0.016, 0.007, 0.004, 0.005, 0.01, 0.024, 0.008, 0.093, 1.0, 0.014, 0.004, 0.003], 'utility': [-0.096, 0.003, 0.265, 0.629, 0.282, -0.16, 0.466, 0.109]} reward=0.187 t=7
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 7, 7, 1, 4, 2, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.028, 0.123, 1.0, 0.014, 0.004, 0.003, 0.008, 0.051, 1.0, 0.016, 0.004, 0.004, 0.008, 0.105, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.033, 0.025, 1.0, 0.014, 0.003, 0.002, 0.003, 1.0, 0.016, 0.025, 0.098, 0.314, 0.067, 0.022, 1.0, 0.149, 0.15, 0.036, 0.016, 0.015, 0.033, 0.032, 0.01, 0.146, 1.0, 0.016, 0.004, 0.004], 'utility': [-0.063, -0.018, 0.247, 0.61, 0.256, -0.166, 0.126, 0.102]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.025, 0.104, 1.0, 0.013, 0.004, 0.003, 0.007, 0.045, 1.0, 0.014, 0.004, 0.003, 0.007, 0.092, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.032, 0.022, 1.0, 0.014, 0.003, 0.002, 0.003, 1.0, 0.017, 0.028, 0.122, 0.349, 0.066, 0.023, 1.0, 0.062, 0.052, 0.017, 0.009, 0.009, 0.019, 0.027, 0.008, 0.113, 1.0, 0.015, 0.004, 0.004], 'utility': [0.017, 0.028, 0.245, 0.53, 0.237, -0.162, 0.281, 0.111]} reward=0.163 t=8
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 4, 7, 1, 1, 3, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.032, 0.147, 1.0, 0.015, 0.004, 0.004, 0.009, 0.057, 1.0, 0.017, 0.005, 0.004, 0.009, 0.119, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005, 0.034, 0.029, 1.0, 0.014, 0.003, 0.002, 0.004, 1.0, 0.015, 0.022, 0.081, 0.283, 0.069, 0.022, 1.0, 0.31, 0.401, 0.064, 0.025, 0.022, 0.05, 0.039, 0.012, 0.201, 1.0, 0.017, 0.005, 0.005], 'utility': [0.007, -0.028, 0.23, 0.526, 0.201, 0.049, -0.142, 0.082]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.028, 0.123, 1.0, 0.014, 0.004, 0.003, 0.008, 0.051, 1.0, 0.016, 0.004, 0.004, 0.008, 0.105, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.033, 0.025, 1.0, 0.014, 0.003, 0.002, 0.003, 1.0, 0.016, 0.025, 0.098, 0.314, 0.067, 0.022, 1.0, 0.149, 0.15, 0.036, 0.016, 0.015, 0.033, 0.032, 0.01, 0.146, 1.0, 0.016, 0.004, 0.004], 'utility': [-0.063, -0.018, 0.247, 0.61, 0.256, -0.166, 0.126, 0.102]} reward=0.143 t=9
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 4, 7, 0, 4, 7, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.036, 0.176, 1.0, 0.017, 0.005, 0.004, 0.01, 0.064, 1.0, 0.019, 0.005, 0.005, 0.01, 0.136, 0.006, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005, 0.036, 0.034, 1.0, 0.014, 0.003, 0.002, 0.004, 1.0, 0.015, 0.02, 0.068, 0.258, 0.073, 0.022, 0.986, 0.559, 1.0, 0.103, 0.035, 0.031, 0.07, 0.05, 0.015, 0.291, 1.0, 0.02, 0.006, 0.006], 'utility': [-0.042, -0.096, 0.214, 0.558, 0.17, 0.054, -0.193, 0.053]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.032, 0.147, 1.0, 0.015, 0.004, 0.004, 0.009, 0.057, 1.0, 0.017, 0.005, 0.004, 0.009, 0.119, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005, 0.034, 0.029, 1.0, 0.014, 0.003, 0.002, 0.004, 1.0, 0.015, 0.022, 0.081, 0.283, 0.069, 0.022, 1.0, 0.31, 0.401, 0.064, 0.025, 0.022, 0.05, 0.039, 0.012, 0.201, 1.0, 0.017, 0.005, 0.005], 'utility': [0.007, -0.028, 0.23, 0.526, 0.201, 0.049, -0.142, 0.082]} reward=0.116 t=10
DEBUG:deepcomp.util.simulation:Step                           action=[1, 0, 4, 7, 0, 4, 2, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 0.213, 1.0, 0.018, 0.005, 0.005, 0.011, 0.072, 1.0, 0.02, 0.006, 0.005, 0.011, 0.154, 0.007, 0.001, 0.0, 0.001, 0.004, 1.0, 0.006, 0.039, 0.04, 1.0, 0.014, 0.003, 0.002, 0.005, 1.0, 0.014, 0.019, 0.058, 0.237, 0.078, 0.023, 0.402, 0.371, 1.0, 0.063, 0.019, 0.017, 0.038, 0.067, 0.02, 0.442, 1.0, 0.023, 0.008, 0.007], 'utility': [0.001, -0.109, -0.101, 0.483, 0.128, 0.057, -0.08, 0.017]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.036, 0.176, 1.0, 0.017, 0.005, 0.004, 0.01, 0.064, 1.0, 0.019, 0.005, 0.005, 0.01, 0.136, 0.006, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005, 0.036, 0.034, 1.0, 0.014, 0.003, 0.002, 0.004, 1.0, 0.015, 0.02, 0.068, 0.258, 0.073, 0.022, 0.986, 0.559, 1.0, 0.103, 0.035, 0.031, 0.07, 0.05, 0.015, 0.291, 1.0, 0.02, 0.006, 0.006], 'utility': [-0.042, -0.096, 0.214, 0.558, 0.17, 0.054, -0.193, 0.053]} reward=0.064 t=11
DEBUG:deepcomp.util.simulation:Step                           action=[1, 2, 0, 7, 6, 4, 7, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.047, 0.259, 1.0, 0.02, 0.006, 0.005, 0.013, 0.08, 1.0, 0.022, 0.006, 0.006, 0.013, 0.174, 0.008, 0.001, 0.001, 0.001, 0.005, 1.0, 0.007, 0.042, 0.048, 1.0, 0.015, 0.003, 0.003, 0.005, 1.0, 0.014, 0.018, 0.051, 0.221, 0.086, 0.024, 0.167, 0.227, 1.0, 0.037, 0.011, 0.009, 0.02, 0.091, 0.027, 0.695, 1.0, 0.028, 0.009, 0.009], 'utility': [-0.029, -0.156, -0.147, 0.481, 0.057, 0.171, -0.035, -0.024]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 0.213, 1.0, 0.018, 0.005, 0.005, 0.011, 0.072, 1.0, 0.02, 0.006, 0.005, 0.011, 0.154, 0.007, 0.001, 0.0, 0.001, 0.004, 1.0, 0.006, 0.039, 0.04, 1.0, 0.014, 0.003, 0.002, 0.005, 1.0, 0.014, 0.019, 0.058, 0.237, 0.078, 0.023, 0.402, 0.371, 1.0, 0.063, 0.019, 0.017, 0.038, 0.067, 0.02, 0.442, 1.0, 0.023, 0.008, 0.007], 'utility': [0.001, -0.109, -0.101, 0.483, 0.128, 0.057, -0.08, 0.017]} reward=0.043 t=12
DEBUG:deepcomp.util.simulation:Step                           action=[1, 5, 0, 7, 6, 4, 1, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.054, 0.317, 1.0, 0.021, 0.006, 0.006, 0.015, 0.089, 1.0, 0.023, 0.007, 0.006, 0.014, 0.198, 0.011, 0.001, 0.001, 0.001, 0.006, 1.0, 0.008, 0.046, 0.059, 1.0, 0.016, 0.004, 0.003, 0.006, 1.0, 0.014, 0.017, 0.046, 0.209, 0.097, 0.026, 0.072, 0.131, 1.0, 0.021, 0.006, 0.005, 0.01, 0.112, 0.033, 1.0, 0.89, 0.031, 0.011, 0.011], 'utility': [-0.003, -0.151, -0.14, 0.414, 0.047, 0.169, -0.014, -0.047]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.047, 0.259, 1.0, 0.02, 0.006, 0.005, 0.013, 0.08, 1.0, 0.022, 0.006, 0.006, 0.013, 0.174, 0.008, 0.001, 0.001, 0.001, 0.005, 1.0, 0.007, 0.042, 0.048, 1.0, 0.015, 0.003, 0.003, 0.005, 1.0, 0.014, 0.018, 0.051, 0.221, 0.086, 0.024, 0.167, 0.227, 1.0, 0.037, 0.011, 0.009, 0.02, 0.091, 0.027, 0.695, 1.0, 0.028, 0.009, 0.009], 'utility': [-0.029, -0.156, -0.147, 0.481, 0.057, 0.171, -0.035, -0.024]} reward=0.036 t=13
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 7, 7, 4, 1, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.061, 0.39, 1.0, 0.023, 0.007, 0.007, 0.017, 0.1, 1.0, 0.025, 0.008, 0.007, 0.016, 0.223, 0.014, 0.001, 0.001, 0.001, 0.008, 1.0, 0.009, 0.05, 0.072, 1.0, 0.017, 0.004, 0.003, 0.007, 1.0, 0.015, 0.016, 0.043, 0.2, 0.112, 0.028, 0.034, 0.075, 1.0, 0.012, 0.003, 0.003, 0.006, 0.094, 0.028, 1.0, 0.539, 0.023, 0.008, 0.009], 'utility': [-0.022, -0.194, -0.136, 0.394, -0.017, 0.163, 0.1, -0.067]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.054, 0.317, 1.0, 0.021, 0.006, 0.006, 0.015, 0.089, 1.0, 0.023, 0.007, 0.006, 0.014, 0.198, 0.011, 0.001, 0.001, 0.001, 0.006, 1.0, 0.008, 0.046, 0.059, 1.0, 0.016, 0.004, 0.003, 0.006, 1.0, 0.014, 0.017, 0.046, 0.209, 0.097, 0.026, 0.072, 0.131, 1.0, 0.021, 0.006, 0.005, 0.01, 0.112, 0.033, 1.0, 0.89, 0.031, 0.011, 0.011], 'utility': [-0.003, -0.151, -0.14, 0.414, 0.047, 0.169, -0.014, -0.047]} reward=0.034 t=14
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 7, 7, 4, 6, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.481, 1.0, 0.025, 0.008, 0.007, 0.02, 0.111, 1.0, 0.027, 0.008, 0.007, 0.017, 0.252, 0.018, 0.002, 0.001, 0.002, 0.011, 1.0, 0.011, 0.055, 0.089, 1.0, 0.018, 0.004, 0.004, 0.008, 1.0, 0.015, 0.016, 0.04, 0.194, 0.132, 0.032, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.078, 0.024, 1.0, 0.323, 0.016, 0.006, 0.007], 'utility': [-0.007, -0.198, -0.129, 0.335, -0.014, 0.153, 0.059, -0.059]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.061, 0.39, 1.0, 0.023, 0.007, 0.007, 0.017, 0.1, 1.0, 0.025, 0.008, 0.007, 0.016, 0.223, 0.014, 0.001, 0.001, 0.001, 0.008, 1.0, 0.009, 0.05, 0.072, 1.0, 0.017, 0.004, 0.003, 0.007, 1.0, 0.015, 0.016, 0.043, 0.2, 0.112, 0.028, 0.034, 0.075, 1.0, 0.012, 0.003, 0.003, 0.006, 0.094, 0.028, 1.0, 0.539, 0.023, 0.008, 0.009], 'utility': [-0.022, -0.194, -0.136, 0.394, -0.017, 0.163, 0.1, -0.067]} reward=0.028 t=15
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 7, 6, 4, 6, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.081, 0.596, 1.0, 0.028, 0.009, 0.008, 0.023, 0.123, 1.0, 0.029, 0.009, 0.008, 0.019, 0.284, 0.023, 0.002, 0.001, 0.002, 0.014, 1.0, 0.012, 0.061, 0.11, 1.0, 0.019, 0.005, 0.004, 0.009, 1.0, 0.017, 0.016, 0.038, 0.191, 0.16, 0.036, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.065, 0.02, 1.0, 0.192, 0.012, 0.005, 0.006], 'utility': [-0.018, -0.223, -0.121, 0.305, -0.076, 0.14, 0.074, -0.03]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.481, 1.0, 0.025, 0.008, 0.007, 0.02, 0.111, 1.0, 0.027, 0.008, 0.007, 0.017, 0.252, 0.018, 0.002, 0.001, 0.002, 0.011, 1.0, 0.011, 0.055, 0.089, 1.0, 0.018, 0.004, 0.004, 0.008, 1.0, 0.015, 0.016, 0.04, 0.194, 0.132, 0.032, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.078, 0.024, 1.0, 0.323, 0.016, 0.006, 0.007], 'utility': [-0.007, -0.198, -0.129, 0.335, -0.014, 0.153, 0.059, -0.059]} reward=0.017 t=16
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 7, 6, 4, 6, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.093, 0.742, 1.0, 0.03, 0.01, 0.01, 0.027, 0.136, 1.0, 0.031, 0.01, 0.009, 0.021, 0.32, 0.029, 0.003, 0.002, 0.003, 0.018, 1.0, 0.015, 0.067, 0.137, 1.0, 0.02, 0.005, 0.004, 0.01, 1.0, 0.018, 0.017, 0.038, 0.19, 0.197, 0.042, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.053, 0.017, 1.0, 0.116, 0.009, 0.004, 0.005], 'utility': [-0.009, -0.239, -0.113, 0.252, -0.091, 0.124, 0.053, 0.009]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.081, 0.596, 1.0, 0.028, 0.009, 0.008, 0.023, 0.123, 1.0, 0.029, 0.009, 0.008, 0.019, 0.284, 0.023, 0.002, 0.001, 0.002, 0.014, 1.0, 0.012, 0.061, 0.11, 1.0, 0.019, 0.005, 0.004, 0.009, 1.0, 0.017, 0.016, 0.038, 0.191, 0.16, 0.036, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.065, 0.02, 1.0, 0.192, 0.012, 0.005, 0.006], 'utility': [-0.018, -0.223, -0.121, 0.305, -0.076, 0.14, 0.074, -0.03]} reward=0.006 t=17
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 7, 6, 4, 6, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.106, 0.928, 1.0, 0.033, 0.011, 0.011, 0.031, 0.151, 1.0, 0.033, 0.011, 0.01, 0.023, 0.36, 0.038, 0.003, 0.002, 0.004, 0.024, 1.0, 0.017, 0.073, 0.172, 1.0, 0.021, 0.006, 0.005, 0.012, 1.0, 0.02, 0.018, 0.038, 0.192, 0.247, 0.049, 0.07, 0.177, 1.0, 0.021, 0.006, 0.005, 0.012, 0.045, 0.015, 1.0, 0.071, 0.006, 0.003, 0.004], 'utility': [-0.016, -0.226, -0.092, 0.218, -0.128, 0.105, -0.157, 0.084]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.093, 0.742, 1.0, 0.03, 0.01, 0.01, 0.027, 0.136, 1.0, 0.031, 0.01, 0.009, 0.021, 0.32, 0.029, 0.003, 0.002, 0.003, 0.018, 1.0, 0.015, 0.067, 0.137, 1.0, 0.02, 0.005, 0.004, 0.01, 1.0, 0.018, 0.017, 0.038, 0.19, 0.197, 0.042, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.053, 0.017, 1.0, 0.116, 0.009, 0.004, 0.005], 'utility': [-0.009, -0.239, -0.113, 0.252, -0.091, 0.124, 0.053, 0.009]} reward=-0.002 t=18
DEBUG:deepcomp.util.simulation:Step                           action=[1, 5, 4, 7, 2, 0, 6, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.105, 1.0, 0.86, 0.031, 0.011, 0.011, 0.031, 0.167, 1.0, 0.035, 0.012, 0.011, 0.026, 0.404, 0.049, 0.004, 0.003, 0.005, 0.031, 1.0, 0.02, 0.08, 0.215, 1.0, 0.023, 0.007, 0.006, 0.014, 1.0, 0.022, 0.019, 0.038, 0.195, 0.314, 0.059, 0.18, 0.471, 1.0, 0.039, 0.012, 0.011, 0.028, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.011, -0.247, -0.103, 0.171, -0.096, 0.046, -0.207, 0.028]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.106, 0.928, 1.0, 0.033, 0.011, 0.011, 0.031, 0.151, 1.0, 0.033, 0.011, 0.01, 0.023, 0.36, 0.038, 0.003, 0.002, 0.004, 0.024, 1.0, 0.017, 0.073, 0.172, 1.0, 0.021, 0.006, 0.005, 0.012, 1.0, 0.02, 0.018, 0.038, 0.192, 0.247, 0.049, 0.07, 0.177, 1.0, 0.021, 0.006, 0.005, 0.012, 0.045, 0.015, 1.0, 0.071, 0.006, 0.003, 0.004], 'utility': [-0.016, -0.226, -0.092, 0.218, -0.128, 0.105, -0.157, 0.084]} reward=-0.035 t=19
DEBUG:deepcomp.util.simulation:Step                           action=[1, 5, 4, 7, 7, 0, 1, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.095, 1.0, 0.683, 0.027, 0.009, 0.009, 0.028, 0.184, 1.0, 0.037, 0.013, 0.012, 0.029, 0.453, 0.062, 0.005, 0.003, 0.006, 0.04, 1.0, 0.023, 0.088, 0.269, 1.0, 0.025, 0.007, 0.006, 0.016, 1.0, 0.024, 0.02, 0.039, 0.2, 0.406, 0.071, 0.377, 1.0, 0.887, 0.057, 0.021, 0.02, 0.056, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.016, -0.256, -0.089, 0.136, -0.109, 0.022, -0.279, 0.082]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.105, 1.0, 0.86, 0.031, 0.011, 0.011, 0.031, 0.167, 1.0, 0.035, 0.012, 0.011, 0.026, 0.404, 0.049, 0.004, 0.003, 0.005, 0.031, 1.0, 0.02, 0.08, 0.215, 1.0, 0.023, 0.007, 0.006, 0.014, 1.0, 0.022, 0.019, 0.038, 0.195, 0.314, 0.059, 0.18, 0.471, 1.0, 0.039, 0.012, 0.011, 0.028, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.011, -0.247, -0.103, 0.171, -0.096, 0.046, -0.207, 0.028]} reward=-0.053 t=20
DEBUG:deepcomp.util.simulation:Step                           action=[1, 5, 4, 7, 7, 0, 1, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.086, 1.0, 0.54, 0.023, 0.008, 0.008, 0.026, 0.203, 1.0, 0.04, 0.014, 0.013, 0.031, 0.507, 0.078, 0.006, 0.004, 0.007, 0.052, 1.0, 0.026, 0.096, 0.338, 1.0, 0.027, 0.008, 0.007, 0.018, 1.0, 0.027, 0.021, 0.04, 0.206, 0.531, 0.086, 0.393, 1.0, 0.421, 0.042, 0.017, 0.019, 0.057, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.013, -0.24, -0.075, 0.093, -0.104, -0.154, -0.191, 0.077]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.095, 1.0, 0.683, 0.027, 0.009, 0.009, 0.028, 0.184, 1.0, 0.037, 0.013, 0.012, 0.029, 0.453, 0.062, 0.005, 0.003, 0.006, 0.04, 1.0, 0.023, 0.088, 0.269, 1.0, 0.025, 0.007, 0.006, 0.016, 1.0, 0.024, 0.02, 0.039, 0.2, 0.406, 0.071, 0.377, 1.0, 0.887, 0.057, 0.021, 0.02, 0.056, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.016, -0.256, -0.089, 0.136, -0.109, 0.022, -0.279, 0.082]} reward=-0.072 t=21
DEBUG:deepcomp.util.simulation:Step                           action=[7, 5, 4, 7, 7, 0, 7, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.077, 1.0, 0.426, 0.02, 0.007, 0.008, 0.024, 0.224, 1.0, 0.042, 0.015, 0.014, 0.035, 0.567, 0.098, 0.007, 0.005, 0.009, 0.067, 1.0, 0.03, 0.105, 0.424, 1.0, 0.028, 0.009, 0.008, 0.021, 1.0, 0.031, 0.023, 0.042, 0.214, 0.702, 0.104, 0.438, 1.0, 0.232, 0.033, 0.016, 0.019, 0.065, 0.046, 0.017, 1.0, 0.038, 0.005, 0.003, 0.004], 'utility': [-0.016, -0.238, -0.063, 0.059, -0.114, -0.18, -0.177, 0.166]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.086, 1.0, 0.54, 0.023, 0.008, 0.008, 0.026, 0.203, 1.0, 0.04, 0.014, 0.013, 0.031, 0.507, 0.078, 0.006, 0.004, 0.007, 0.052, 1.0, 0.026, 0.096, 0.338, 1.0, 0.027, 0.008, 0.007, 0.018, 1.0, 0.027, 0.021, 0.04, 0.206, 0.531, 0.086, 0.393, 1.0, 0.421, 0.042, 0.017, 0.019, 0.057, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.013, -0.24, -0.075, 0.093, -0.104, -0.154, -0.191, 0.077]} reward=-0.076 t=22
DEBUG:deepcomp.util.simulation:Step                           action=[3, 5, 5, 7, 4, 0, 6, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.069, 1.0, 0.334, 0.017, 0.006, 0.007, 0.021, 0.246, 1.0, 0.044, 0.016, 0.015, 0.038, 0.633, 0.123, 0.008, 0.006, 0.011, 0.085, 1.0, 0.034, 0.114, 0.531, 1.0, 0.031, 0.01, 0.009, 0.024, 1.0, 0.034, 0.025, 0.044, 0.222, 0.935, 0.128, 0.529, 1.0, 0.152, 0.029, 0.016, 0.022, 0.085, 0.067, 0.028, 1.0, 0.034, 0.005, 0.003, 0.005], 'utility': [-0.014, -0.224, -0.053, 0.021, -0.099, -0.208, -0.146, 0.07]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.077, 1.0, 0.426, 0.02, 0.007, 0.008, 0.024, 0.224, 1.0, 0.042, 0.015, 0.014, 0.035, 0.567, 0.098, 0.007, 0.005, 0.009, 0.067, 1.0, 0.03, 0.105, 0.424, 1.0, 0.028, 0.009, 0.008, 0.021, 1.0, 0.031, 0.023, 0.042, 0.214, 0.702, 0.104, 0.438, 1.0, 0.232, 0.033, 0.016, 0.019, 0.065, 0.046, 0.017, 1.0, 0.038, 0.005, 0.003, 0.004], 'utility': [-0.016, -0.238, -0.063, 0.059, -0.114, -0.18, -0.177, 0.166]} reward=-0.07 t=23
DEBUG:deepcomp.util.simulation:Step                           action=[3, 5, 4, 7, 4, 0, 6, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.061, 1.0, 0.261, 0.014, 0.006, 0.006, 0.019, 0.27, 1.0, 0.047, 0.017, 0.016, 0.042, 0.707, 0.152, 0.009, 0.007, 0.014, 0.108, 1.0, 0.038, 0.123, 0.667, 1.0, 0.033, 0.011, 0.01, 0.028, 0.798, 0.031, 0.021, 0.036, 0.185, 1.0, 0.125, 0.68, 1.0, 0.117, 0.029, 0.019, 0.029, 0.131, 0.117, 0.059, 1.0, 0.038, 0.008, 0.005, 0.009], 'utility': [-0.016, -0.231, -0.045, -0.012, -0.122, -0.236, -0.125, 0.001]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.069, 1.0, 0.334, 0.017, 0.006, 0.007, 0.021, 0.246, 1.0, 0.044, 0.016, 0.015, 0.038, 0.633, 0.123, 0.008, 0.006, 0.011, 0.085, 1.0, 0.034, 0.114, 0.531, 1.0, 0.031, 0.01, 0.009, 0.024, 1.0, 0.034, 0.025, 0.044, 0.222, 0.935, 0.128, 0.529, 1.0, 0.152, 0.029, 0.016, 0.022, 0.085, 0.067, 0.028, 1.0, 0.034, 0.005, 0.003, 0.005], 'utility': [-0.014, -0.224, -0.053, 0.021, -0.099, -0.208, -0.146, 0.07]} reward=-0.082 t=24
DEBUG:deepcomp.util.simulation:Step                           action=[7, 5, 4, 7, 4, 0, 6, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.054, 1.0, 0.203, 0.012, 0.005, 0.005, 0.017, 0.296, 1.0, 0.05, 0.018, 0.018, 0.046, 0.788, 0.188, 0.011, 0.008, 0.017, 0.137, 1.0, 0.043, 0.133, 0.836, 1.0, 0.035, 0.012, 0.011, 0.031, 0.592, 0.026, 0.017, 0.029, 0.143, 1.0, 0.114, 0.888, 1.0, 0.105, 0.032, 0.024, 0.042, 0.235, 0.215, 0.144, 1.0, 0.047, 0.012, 0.009, 0.018], 'utility': [-0.015, -0.238, -0.04, -0.047, -0.13, -0.264, -0.119, -0.124]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.061, 1.0, 0.261, 0.014, 0.006, 0.006, 0.019, 0.27, 1.0, 0.047, 0.017, 0.016, 0.042, 0.707, 0.152, 0.009, 0.007, 0.014, 0.108, 1.0, 0.038, 0.123, 0.667, 1.0, 0.033, 0.011, 0.01, 0.028, 0.798, 0.031, 0.021, 0.036, 0.185, 1.0, 0.125, 0.68, 1.0, 0.117, 0.029, 0.019, 0.029, 0.131, 0.117, 0.059, 1.0, 0.038, 0.008, 0.005, 0.009], 'utility': [-0.016, -0.231, -0.045, -0.012, -0.122, -0.236, -0.125, 0.001]} reward=-0.098 t=25
DEBUG:deepcomp.util.simulation:Step                           action=[7, 5, 4, 7, 7, 6, 6, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.047, 1.0, 0.158, 0.01, 0.004, 0.005, 0.016, 0.324, 1.0, 0.052, 0.019, 0.019, 0.05, 0.877, 0.229, 0.013, 0.01, 0.02, 0.173, 1.0, 0.048, 0.137, 1.0, 0.955, 0.036, 0.012, 0.012, 0.034, 0.438, 0.022, 0.014, 0.022, 0.11, 1.0, 0.103, 1.0, 0.887, 0.092, 0.033, 0.029, 0.06, 0.42, 0.377, 0.372, 1.0, 0.061, 0.019, 0.016, 0.037], 'utility': [-0.068, -0.255, -0.036, -0.134, -0.155, -0.142, -0.13, -0.223]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.054, 1.0, 0.203, 0.012, 0.005, 0.005, 0.017, 0.296, 1.0, 0.05, 0.018, 0.018, 0.046, 0.788, 0.188, 0.011, 0.008, 0.017, 0.137, 1.0, 0.043, 0.133, 0.836, 1.0, 0.035, 0.012, 0.011, 0.031, 0.592, 0.026, 0.017, 0.029, 0.143, 1.0, 0.114, 0.888, 1.0, 0.105, 0.032, 0.024, 0.042, 0.235, 0.215, 0.144, 1.0, 0.047, 0.012, 0.009, 0.018], 'utility': [-0.015, -0.238, -0.04, -0.047, -0.13, -0.264, -0.119, -0.124]} reward=-0.129 t=26
DEBUG:deepcomp.util.simulation:Step                           action=[0, 5, 5, 7, 4, 0, 6, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 1.0, 0.122, 0.008, 0.003, 0.004, 0.014, 0.354, 1.0, 0.055, 0.021, 0.021, 0.055, 0.975, 0.278, 0.015, 0.012, 0.025, 0.218, 1.0, 0.053, 0.117, 1.0, 0.762, 0.03, 0.011, 0.011, 0.031, 0.324, 0.018, 0.011, 0.017, 0.085, 1.0, 0.094, 1.0, 0.739, 0.08, 0.033, 0.034, 0.083, 0.776, 0.601, 0.998, 1.0, 0.078, 0.028, 0.027, 0.072], 'utility': [-0.111, -0.299, -0.047, -0.204, -0.188, -0.07, -0.18, -0.26]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.047, 1.0, 0.158, 0.01, 0.004, 0.005, 0.016, 0.324, 1.0, 0.052, 0.019, 0.019, 0.05, 0.877, 0.229, 0.013, 0.01, 0.02, 0.173, 1.0, 0.048, 0.137, 1.0, 0.955, 0.036, 0.012, 0.012, 0.034, 0.438, 0.022, 0.014, 0.022, 0.11, 1.0, 0.103, 1.0, 0.887, 0.092, 0.033, 0.029, 0.06, 0.42, 0.377, 0.372, 1.0, 0.061, 0.019, 0.016, 0.037], 'utility': [-0.068, -0.255, -0.036, -0.134, -0.155, -0.142, -0.13, -0.223]} reward=-0.154 t=27
DEBUG:deepcomp.util.simulation:Step                           action=[0, 5, 5, 7, 4, 4, 6, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.035, 1.0, 0.093, 0.007, 0.003, 0.003, 0.012, 0.357, 0.924, 0.054, 0.021, 0.021, 0.055, 1.0, 0.335, 0.017, 0.014, 0.03, 0.273, 1.0, 0.058, 0.1, 1.0, 0.61, 0.026, 0.009, 0.009, 0.028, 0.24, 0.015, 0.009, 0.014, 0.066, 1.0, 0.085, 0.604, 0.395, 0.047, 0.022, 0.025, 0.074, 1.0, 0.311, 1.0, 0.359, 0.035, 0.015, 0.016, 0.05], 'utility': [-0.092, -0.313, -0.04, -0.219, -0.207, -0.077, -0.21, -0.3]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 1.0, 0.122, 0.008, 0.003, 0.004, 0.014, 0.354, 1.0, 0.055, 0.021, 0.021, 0.055, 0.975, 0.278, 0.015, 0.012, 0.025, 0.218, 1.0, 0.053, 0.117, 1.0, 0.762, 0.03, 0.011, 0.011, 0.031, 0.324, 0.018, 0.011, 0.017, 0.085, 1.0, 0.094, 1.0, 0.739, 0.08, 0.033, 0.034, 0.083, 0.776, 0.601, 0.998, 1.0, 0.078, 0.028, 0.027, 0.072], 'utility': [-0.111, -0.299, -0.047, -0.204, -0.188, -0.07, -0.18, -0.26]} reward=-0.17 t=28
DEBUG:deepcomp.util.simulation:Step                           action=[0, 3, 3, 7, 4, 3, 7, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.03, 1.0, 0.071, 0.006, 0.002, 0.003, 0.011, 0.351, 0.833, 0.051, 0.02, 0.02, 0.055, 1.0, 0.401, 0.019, 0.016, 0.036, 0.34, 1.0, 0.064, 0.086, 1.0, 0.488, 0.022, 0.008, 0.008, 0.025, 0.178, 0.013, 0.007, 0.011, 0.051, 1.0, 0.077, 0.245, 0.149, 0.019, 0.01, 0.013, 0.047, 1.0, 0.137, 1.0, 0.121, 0.014, 0.007, 0.008, 0.031], 'utility': [-0.111, -0.259, -0.089, -0.262, -0.032, -0.03, -0.016, -0.259]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.035, 1.0, 0.093, 0.007, 0.003, 0.003, 0.012, 0.357, 0.924, 0.054, 0.021, 0.021, 0.055, 1.0, 0.335, 0.017, 0.014, 0.03, 0.273, 1.0, 0.058, 0.1, 1.0, 0.61, 0.026, 0.009, 0.009, 0.028, 0.24, 0.015, 0.009, 0.014, 0.066, 1.0, 0.085, 0.604, 0.395, 0.047, 0.022, 0.025, 0.074, 1.0, 0.311, 1.0, 0.359, 0.035, 0.015, 0.016, 0.05], 'utility': [-0.092, -0.313, -0.04, -0.219, -0.207, -0.077, -0.21, -0.3]} reward=-0.18 t=29
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 2, 5, 1, 3, 3, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.026, 1.0, 0.054, 0.005, 0.002, 0.002, 0.009, 0.345, 0.752, 0.048, 0.019, 0.02, 0.054, 1.0, 0.477, 0.022, 0.019, 0.043, 0.423, 1.0, 0.07, 0.073, 1.0, 0.391, 0.019, 0.007, 0.007, 0.023, 0.133, 0.01, 0.006, 0.008, 0.039, 1.0, 0.069, 0.086, 0.05, 0.007, 0.004, 0.006, 0.026, 1.0, 0.051, 1.0, 0.038, 0.005, 0.003, 0.004, 0.017], 'utility': [-0.065, -0.042, -0.212, -0.144, 0.062, 0.014, 0.12, -0.042]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.03, 1.0, 0.071, 0.006, 0.002, 0.003, 0.011, 0.351, 0.833, 0.051, 0.02, 0.02, 0.055, 1.0, 0.401, 0.019, 0.016, 0.036, 0.34, 1.0, 0.064, 0.086, 1.0, 0.488, 0.022, 0.008, 0.008, 0.025, 0.178, 0.013, 0.007, 0.011, 0.051, 1.0, 0.077, 0.245, 0.149, 0.019, 0.01, 0.013, 0.047, 1.0, 0.137, 1.0, 0.121, 0.014, 0.007, 0.008, 0.031], 'utility': [-0.111, -0.259, -0.089, -0.262, -0.032, -0.03, -0.016, -0.259]} reward=-0.082 t=30
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 4, 5, 4, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.022, 1.0, 0.041, 0.004, 0.002, 0.002, 0.008, 0.339, 0.679, 0.046, 0.018, 0.019, 0.053, 1.0, 0.563, 0.025, 0.022, 0.052, 0.524, 1.0, 0.076, 0.062, 1.0, 0.314, 0.016, 0.006, 0.006, 0.02, 0.1, 0.009, 0.005, 0.007, 0.031, 1.0, 0.063, 0.025, 0.015, 0.002, 0.001, 0.002, 0.012, 1.0, 0.017, 1.0, 0.011, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.081, 0.009, -0.203, -0.071, 0.088, 0.062, 0.303, 0.009]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.026, 1.0, 0.054, 0.005, 0.002, 0.002, 0.009, 0.345, 0.752, 0.048, 0.019, 0.02, 0.054, 1.0, 0.477, 0.022, 0.019, 0.043, 0.423, 1.0, 0.07, 0.073, 1.0, 0.391, 0.019, 0.007, 0.007, 0.023, 0.133, 0.01, 0.006, 0.008, 0.039, 1.0, 0.069, 0.086, 0.05, 0.007, 0.004, 0.006, 0.026, 1.0, 0.051, 1.0, 0.038, 0.005, 0.003, 0.004, 0.017], 'utility': [-0.065, -0.042, -0.212, -0.144, 0.062, 0.014, 0.12, -0.042]} reward=-0.035 t=31
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 4, 1, 0, 5, 6, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.018, 1.0, 0.031, 0.003, 0.001, 0.002, 0.007, 0.333, 0.615, 0.043, 0.018, 0.019, 0.052, 1.0, 0.66, 0.028, 0.025, 0.062, 0.647, 1.0, 0.082, 0.053, 1.0, 0.253, 0.013, 0.005, 0.006, 0.018, 0.077, 0.007, 0.004, 0.005, 0.025, 1.0, 0.058, 0.006, 0.004, 0.001, 0.0, 0.001, 0.005, 1.0, 0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [-0.076, 0.049, -0.194, -0.134, 0.11, 0.062, 0.536, 0.049]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.022, 1.0, 0.041, 0.004, 0.002, 0.002, 0.008, 0.339, 0.679, 0.046, 0.018, 0.019, 0.053, 1.0, 0.563, 0.025, 0.022, 0.052, 0.524, 1.0, 0.076, 0.062, 1.0, 0.314, 0.016, 0.006, 0.006, 0.02, 0.1, 0.009, 0.005, 0.007, 0.031, 1.0, 0.063, 0.025, 0.015, 0.002, 0.001, 0.002, 0.012, 1.0, 0.017, 1.0, 0.011, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.081, 0.009, -0.203, -0.071, 0.088, 0.062, 0.303, 0.009]} reward=0.008 t=32
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 0, 1, 6, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 1.0, 0.023, 0.002, 0.001, 0.001, 0.006, 0.327, 0.557, 0.041, 0.017, 0.018, 0.052, 1.0, 0.768, 0.032, 0.029, 0.074, 0.797, 1.0, 0.088, 0.045, 1.0, 0.205, 0.011, 0.005, 0.005, 0.017, 0.06, 0.006, 0.003, 0.005, 0.02, 1.0, 0.055, 0.002, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0, 0.004], 'utility': [-0.058, 0.078, -0.185, -0.009, 0.128, 0.114, 0.719, 0.078]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.018, 1.0, 0.031, 0.003, 0.001, 0.002, 0.007, 0.333, 0.615, 0.043, 0.018, 0.019, 0.052, 1.0, 0.66, 0.028, 0.025, 0.062, 0.647, 1.0, 0.082, 0.053, 1.0, 0.253, 0.013, 0.005, 0.006, 0.018, 0.077, 0.007, 0.004, 0.005, 0.025, 1.0, 0.058, 0.006, 0.004, 0.001, 0.0, 0.001, 0.005, 1.0, 0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [-0.076, 0.049, -0.194, -0.134, 0.11, 0.062, 0.536, 0.049]} reward=0.066 t=33
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 4, 1, 0, 1, 6, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.012, 1.0, 0.017, 0.002, 0.001, 0.001, 0.005, 0.321, 0.506, 0.039, 0.016, 0.018, 0.051, 1.0, 0.887, 0.035, 0.034, 0.088, 0.978, 1.0, 0.095, 0.039, 1.0, 0.166, 0.01, 0.004, 0.004, 0.015, 0.048, 0.006, 0.003, 0.004, 0.016, 1.0, 0.052, 0.002, 0.001, 0.0, 0.0, 0.0, 0.003, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.067, 0.103, -0.176, -0.118, 0.144, 0.118, 0.663, 0.103]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 1.0, 0.023, 0.002, 0.001, 0.001, 0.006, 0.327, 0.557, 0.041, 0.017, 0.018, 0.052, 1.0, 0.768, 0.032, 0.029, 0.074, 0.797, 1.0, 0.088, 0.045, 1.0, 0.205, 0.011, 0.005, 0.005, 0.017, 0.06, 0.006, 0.003, 0.005, 0.02, 1.0, 0.055, 0.002, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0, 0.004], 'utility': [-0.058, 0.078, -0.185, -0.009, 0.128, 0.114, 0.719, 0.078]} reward=0.091 t=34
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 0, 1, 6, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.01, 1.0, 0.013, 0.001, 0.001, 0.001, 0.005, 0.316, 0.459, 0.037, 0.016, 0.017, 0.051, 1.0, 0.85, 0.033, 0.032, 0.087, 1.0, 0.835, 0.085, 0.033, 1.0, 0.135, 0.008, 0.003, 0.004, 0.013, 0.039, 0.005, 0.002, 0.003, 0.014, 1.0, 0.051, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.05, 0.129, -0.168, 0.011, 0.163, 0.156, 0.574, 0.129]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.012, 1.0, 0.017, 0.002, 0.001, 0.001, 0.005, 0.321, 0.506, 0.039, 0.016, 0.018, 0.051, 1.0, 0.887, 0.035, 0.034, 0.088, 0.978, 1.0, 0.095, 0.039, 1.0, 0.166, 0.01, 0.004, 0.004, 0.015, 0.048, 0.006, 0.003, 0.004, 0.016, 1.0, 0.052, 0.002, 0.001, 0.0, 0.0, 0.0, 0.003, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.067, 0.103, -0.176, -0.118, 0.144, 0.118, 0.663, 0.103]} reward=0.112 t=35
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 1, 1, 0, 1, 6, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.008, 1.0, 0.01, 0.001, 0.001, 0.001, 0.004, 0.31, 0.418, 0.035, 0.015, 0.017, 0.05, 1.0, 0.794, 0.03, 0.03, 0.084, 1.0, 0.684, 0.074, 0.028, 1.0, 0.111, 0.007, 0.003, 0.003, 0.012, 0.034, 0.005, 0.002, 0.003, 0.012, 1.0, 0.051, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.055, 0.153, -0.054, -0.094, 0.181, 0.152, 0.574, 0.153]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.01, 1.0, 0.013, 0.001, 0.001, 0.001, 0.005, 0.316, 0.459, 0.037, 0.016, 0.017, 0.051, 1.0, 0.85, 0.033, 0.032, 0.087, 1.0, 0.835, 0.085, 0.033, 1.0, 0.135, 0.008, 0.003, 0.004, 0.013, 0.039, 0.005, 0.002, 0.003, 0.014, 1.0, 0.051, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.05, 0.129, -0.168, 0.011, 0.163, 0.156, 0.574, 0.129]} reward=0.115 t=36
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 5, 1, 6, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.007, 1.0, 0.008, 0.001, 0.001, 0.001, 0.003, 0.305, 0.381, 0.034, 0.015, 0.016, 0.05, 1.0, 0.738, 0.027, 0.028, 0.081, 1.0, 0.562, 0.065, 0.025, 1.0, 0.091, 0.006, 0.003, 0.003, 0.011, 0.03, 0.005, 0.002, 0.003, 0.011, 1.0, 0.052, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.015], 'utility': [-0.045, 0.148, -0.093, -0.016, 0.148, 0.165, 0.574, 0.148]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.008, 1.0, 0.01, 0.001, 0.001, 0.001, 0.004, 0.31, 0.418, 0.035, 0.015, 0.017, 0.05, 1.0, 0.794, 0.03, 0.03, 0.084, 1.0, 0.684, 0.074, 0.028, 1.0, 0.111, 0.007, 0.003, 0.003, 0.012, 0.034, 0.005, 0.002, 0.003, 0.012, 1.0, 0.051, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.055, 0.153, -0.054, -0.094, 0.181, 0.152, 0.574, 0.153]} reward=0.129 t=37
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 2, 1, 0, 4, 4, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.006, 1.0, 0.006, 0.001, 0.0, 0.001, 0.003, 0.3, 0.348, 0.032, 0.014, 0.016, 0.049, 1.0, 0.684, 0.025, 0.026, 0.078, 1.0, 0.463, 0.057, 0.021, 1.0, 0.076, 0.005, 0.002, 0.003, 0.01, 0.027, 0.005, 0.002, 0.003, 0.011, 1.0, 0.056, 0.004, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.065, 1.0, 0.02, 0.005, 0.003, 0.006, 0.045], 'utility': [-0.044, -0.266, 0.026, -0.063, -0.266, 0.153, 0.589, -0.266]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.007, 1.0, 0.008, 0.001, 0.001, 0.001, 0.003, 0.305, 0.381, 0.034, 0.015, 0.016, 0.05, 1.0, 0.738, 0.027, 0.028, 0.081, 1.0, 0.562, 0.065, 0.025, 1.0, 0.091, 0.006, 0.003, 0.003, 0.011, 0.03, 0.005, 0.002, 0.003, 0.011, 1.0, 0.052, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.015], 'utility': [-0.045, 0.148, -0.093, -0.016, 0.148, 0.165, 0.574, 0.148]} reward=-0.013 t=38
DEBUG:deepcomp.util.simulation:Step                           action=[3, 3, 2, 1, 3, 1, 4, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.005, 0.001, 0.0, 0.001, 0.003, 0.295, 0.318, 0.03, 0.014, 0.016, 0.049, 1.0, 0.631, 0.022, 0.025, 0.076, 1.0, 0.383, 0.05, 0.019, 1.0, 0.063, 0.005, 0.002, 0.002, 0.009, 0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.061, 0.01, 0.005, 0.001, 0.001, 0.001, 0.01, 1.0, 0.256, 1.0, 0.053, 0.014, 0.01, 0.017, 0.109], 'utility': [-0.036, 0.009, -0.078, 0.011, 0.009, 0.148, 0.433, 0.009]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.006, 1.0, 0.006, 0.001, 0.0, 0.001, 0.003, 0.3, 0.348, 0.032, 0.014, 0.016, 0.049, 1.0, 0.684, 0.025, 0.026, 0.078, 1.0, 0.463, 0.057, 0.021, 1.0, 0.076, 0.005, 0.002, 0.003, 0.01, 0.027, 0.005, 0.002, 0.003, 0.011, 1.0, 0.056, 0.004, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.065, 1.0, 0.02, 0.005, 0.003, 0.006, 0.045], 'utility': [-0.044, -0.266, 0.026, -0.063, -0.266, 0.153, 0.589, -0.266]} reward=0.114 t=39
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 2, 1, 0, 1, 4, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.004, 0.001, 0.0, 0.0, 0.003, 0.29, 0.291, 0.029, 0.013, 0.015, 0.048, 1.0, 0.58, 0.02, 0.023, 0.074, 1.0, 0.318, 0.044, 0.016, 1.0, 0.054, 0.004, 0.002, 0.002, 0.009, 0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068, 0.037, 0.014, 0.003, 0.002, 0.004, 0.024, 1.0, 0.959, 1.0, 0.115, 0.034, 0.025, 0.042, 0.215], 'utility': [-0.035, -0.334, -0.014, -0.028, -0.334, 0.125, 0.235, -0.114]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.005, 0.001, 0.0, 0.001, 0.003, 0.295, 0.318, 0.03, 0.014, 0.016, 0.049, 1.0, 0.631, 0.022, 0.025, 0.076, 1.0, 0.383, 0.05, 0.019, 1.0, 0.063, 0.005, 0.002, 0.002, 0.009, 0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.061, 0.01, 0.005, 0.001, 0.001, 0.001, 0.01, 1.0, 0.256, 1.0, 0.053, 0.014, 0.01, 0.017, 0.109], 'utility': [-0.036, 0.009, -0.078, 0.011, 0.009, 0.148, 0.433, 0.009]} reward=-0.033 t=40
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 0, 4, 1, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.001, 0.0, 0.0, 0.003, 0.286, 0.267, 0.027, 0.013, 0.015, 0.048, 1.0, 0.532, 0.018, 0.022, 0.072, 1.0, 0.265, 0.038, 0.015, 1.0, 0.046, 0.004, 0.002, 0.002, 0.008, 0.026, 0.005, 0.002, 0.003, 0.011, 1.0, 0.078, 0.13, 0.04, 0.008, 0.006, 0.009, 0.052, 1.0, 1.0, 0.271, 0.059, 0.02, 0.015, 0.025, 0.097], 'utility': [-0.018, -0.382, -0.032, 0.021, -0.382, 0.117, 0.055, -0.076]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.004, 0.001, 0.0, 0.0, 0.003, 0.29, 0.291, 0.029, 0.013, 0.015, 0.048, 1.0, 0.58, 0.02, 0.023, 0.074, 1.0, 0.318, 0.044, 0.016, 1.0, 0.054, 0.004, 0.002, 0.002, 0.009, 0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068, 0.037, 0.014, 0.003, 0.002, 0.004, 0.024, 1.0, 0.959, 1.0, 0.115, 0.034, 0.025, 0.042, 0.215], 'utility': [-0.035, -0.334, -0.014, -0.028, -0.334, 0.125, 0.235, -0.114]} reward=-0.066 t=41
DEBUG:deepcomp.util.simulation:Step                           action=[2, 7, 5, 6, 7, 4, 1, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003, 0.281, 0.245, 0.026, 0.013, 0.015, 0.048, 1.0, 0.487, 0.017, 0.02, 0.07, 1.0, 0.221, 0.034, 0.013, 1.0, 0.04, 0.003, 0.002, 0.002, 0.007, 0.027, 0.006, 0.003, 0.003, 0.012, 1.0, 0.091, 0.426, 0.095, 0.02, 0.014, 0.021, 0.096, 1.0, 1.0, 0.062, 0.022, 0.01, 0.008, 0.011, 0.033], 'utility': [-0.016, -0.438, -0.043, 0.029, -0.438, 0.086, -0.057, 0.036]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.001, 0.0, 0.0, 0.003, 0.286, 0.267, 0.027, 0.013, 0.015, 0.048, 1.0, 0.532, 0.018, 0.022, 0.072, 1.0, 0.265, 0.038, 0.015, 1.0, 0.046, 0.004, 0.002, 0.002, 0.008, 0.026, 0.005, 0.002, 0.003, 0.011, 1.0, 0.078, 0.13, 0.04, 0.008, 0.006, 0.009, 0.052, 1.0, 1.0, 0.271, 0.059, 0.02, 0.015, 0.025, 0.097], 'utility': [-0.018, -0.382, -0.032, 0.021, -0.382, 0.117, 0.055, -0.076]} reward=-0.093 t=42
DEBUG:deepcomp.util.simulation:Step                           action=[0, 7, 5, 6, 1, 4, 3, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003, 0.277, 0.225, 0.025, 0.012, 0.015, 0.048, 1.0, 0.444, 0.015, 0.019, 0.069, 1.0, 0.186, 0.03, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.028, 0.007, 0.003, 0.003, 0.012, 1.0, 0.107, 1.0, 0.152, 0.035, 0.022, 0.032, 0.115, 0.749, 1.0, 0.01, 0.005, 0.003, 0.003, 0.003, 0.007], 'utility': [-0.016, -0.292, -0.007, 0.046, -0.292, 0.054, -0.119, 0.304]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003, 0.281, 0.245, 0.026, 0.013, 0.015, 0.048, 1.0, 0.487, 0.017, 0.02, 0.07, 1.0, 0.221, 0.034, 0.013, 1.0, 0.04, 0.003, 0.002, 0.002, 0.007, 0.027, 0.006, 0.003, 0.003, 0.012, 1.0, 0.091, 0.426, 0.095, 0.02, 0.014, 0.021, 0.096, 1.0, 1.0, 0.062, 0.022, 0.01, 0.008, 0.011, 0.033], 'utility': [-0.016, -0.438, -0.043, 0.029, -0.438, 0.086, -0.057, 0.036]} reward=-0.105 t=43
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 5, 6, 7, 4, 3, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.001, 0.003, 0.273, 0.208, 0.024, 0.012, 0.014, 0.048, 1.0, 0.405, 0.014, 0.018, 0.067, 1.0, 0.157, 0.026, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.03, 0.008, 0.003, 0.004, 0.014, 1.0, 0.126, 1.0, 0.093, 0.024, 0.015, 0.019, 0.054, 0.241, 1.0, 0.001, 0.001, 0.0, 0.0, 0.0, 0.001], 'utility': [-0.015, -0.301, -0.004, 0.061, -0.301, 0.018, -0.1, 0.804]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003, 0.277, 0.225, 0.025, 0.012, 0.015, 0.048, 1.0, 0.444, 0.015, 0.019, 0.069, 1.0, 0.186, 0.03, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.028, 0.007, 0.003, 0.003, 0.012, 1.0, 0.107, 1.0, 0.152, 0.035, 0.022, 0.032, 0.115, 0.749, 1.0, 0.01, 0.005, 0.003, 0.003, 0.003, 0.007], 'utility': [-0.016, -0.292, -0.007, 0.046, -0.292, 0.054, -0.119, 0.304]} reward=-0.04 t=44
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 5, 6, 0, 4, 3, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004, 0.269, 0.192, 0.023, 0.011, 0.014, 0.048, 1.0, 0.369, 0.013, 0.017, 0.067, 1.0, 0.133, 0.023, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.033, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148, 1.0, 0.051, 0.015, 0.009, 0.01, 0.023, 0.077, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.015, 0.285, -0.061, 0.077, 0.285, -0.019, -0.006, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.001, 0.003, 0.273, 0.208, 0.024, 0.012, 0.014, 0.048, 1.0, 0.405, 0.014, 0.018, 0.067, 1.0, 0.157, 0.026, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.03, 0.008, 0.003, 0.004, 0.014, 1.0, 0.126, 1.0, 0.093, 0.024, 0.015, 0.019, 0.054, 0.241, 1.0, 0.001, 0.001, 0.0, 0.0, 0.0, 0.001], 'utility': [-0.015, -0.301, -0.004, 0.061, -0.301, 0.018, -0.1, 0.804]} reward=0.02 t=45
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 5, 1, 0, 4, 2, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.005, 0.265, 0.177, 0.022, 0.011, 0.014, 0.048, 1.0, 0.336, 0.012, 0.016, 0.066, 1.0, 0.114, 0.021, 0.014, 1.0, 0.042, 0.004, 0.002, 0.002, 0.008, 0.035, 0.01, 0.004, 0.005, 0.017, 1.0, 0.174, 1.0, 0.026, 0.01, 0.006, 0.005, 0.009, 0.025, 1.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0], 'utility': [-0.014, 0.27, 0.087, 0.074, 0.27, -0.056, 0.179, 0.903]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004, 0.269, 0.192, 0.023, 0.011, 0.014, 0.048, 1.0, 0.369, 0.013, 0.017, 0.067, 1.0, 0.133, 0.023, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.033, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148, 1.0, 0.051, 0.015, 0.009, 0.01, 0.023, 0.077, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.015, 0.285, -0.061, 0.077, 0.285, -0.019, -0.006, 1.0]} reward=0.199 t=46
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 5, 1, 0, 7, 7, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.007, 1.0, 0.004, 0.001, 0.0, 0.001, 0.006, 0.262, 0.164, 0.021, 0.011, 0.014, 0.048, 1.0, 0.306, 0.011, 0.015, 0.066, 1.0, 0.098, 0.019, 0.015, 1.0, 0.049, 0.004, 0.002, 0.002, 0.008, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.015, 0.007, 0.004, 0.003, 0.004, 0.01, 1.0, 0.002, 0.003, 0.006, 0.009, 0.005, 0.003], 'utility': [-0.009, 0.252, -0.049, 0.105, 0.252, -0.04, 0.239, 0.323]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.005, 0.265, 0.177, 0.022, 0.011, 0.014, 0.048, 1.0, 0.336, 0.012, 0.016, 0.066, 1.0, 0.114, 0.021, 0.014, 1.0, 0.042, 0.004, 0.002, 0.002, 0.008, 0.035, 0.01, 0.004, 0.005, 0.017, 1.0, 0.174, 1.0, 0.026, 0.01, 0.006, 0.005, 0.009, 0.025, 1.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0], 'utility': [-0.014, 0.27, 0.087, 0.074, 0.27, -0.056, 0.179, 0.903]} reward=0.187 t=47
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 5, 1, 6, 4, 0, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.008, 1.0, 0.004, 0.001, 0.001, 0.001, 0.008, 0.259, 0.153, 0.02, 0.011, 0.014, 0.048, 1.0, 0.279, 0.01, 0.014, 0.066, 1.0, 0.085, 0.017, 0.017, 1.0, 0.058, 0.004, 0.002, 0.002, 0.009, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.013, 0.009, 0.004, 0.003, 0.003, 0.006, 1.0, 0.007, 0.011, 0.03, 0.057, 0.021, 0.009], 'utility': [-0.02, 0.231, -0.035, 0.103, 0.231, -0.029, 0.326, 0.085]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.007, 1.0, 0.004, 0.001, 0.0, 0.001, 0.006, 0.262, 0.164, 0.021, 0.011, 0.014, 0.048, 1.0, 0.306, 0.011, 0.015, 0.066, 1.0, 0.098, 0.019, 0.015, 1.0, 0.049, 0.004, 0.002, 0.002, 0.008, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.015, 0.007, 0.004, 0.003, 0.004, 0.01, 1.0, 0.002, 0.003, 0.006, 0.009, 0.005, 0.003], 'utility': [-0.009, 0.252, -0.049, 0.105, 0.252, -0.04, 0.239, 0.323]} reward=0.149 t=48
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 5, 3, 3, 4, 4, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.01, 1.0, 0.005, 0.001, 0.001, 0.001, 0.011, 0.256, 0.142, 0.019, 0.01, 0.013, 0.049, 1.0, 0.256, 0.009, 0.014, 0.067, 1.0, 0.074, 0.015, 0.02, 1.0, 0.069, 0.005, 0.002, 0.003, 0.01, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.018, 0.019, 0.009, 0.005, 0.004, 0.007, 1.0, 0.015, 0.024, 0.092, 0.254, 0.057, 0.02], 'utility': [-0.012, 0.208, -0.03, 0.116, 0.208, -0.037, 0.234, -0.128]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.008, 1.0, 0.004, 0.001, 0.001, 0.001, 0.008, 0.259, 0.153, 0.02, 0.011, 0.014, 0.048, 1.0, 0.279, 0.01, 0.014, 0.066, 1.0, 0.085, 0.017, 0.017, 1.0, 0.058, 0.004, 0.002, 0.002, 0.009, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.013, 0.009, 0.004, 0.003, 0.003, 0.006, 1.0, 0.007, 0.011, 0.03, 0.057, 0.021, 0.009], 'utility': [-0.02, 0.231, -0.035, 0.103, 0.231, -0.029, 0.326, 0.085]} reward=0.111 t=49
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 5, 3, 3, 5, 4, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.012, 1.0, 0.005, 0.001, 0.001, 0.002, 0.015, 0.253, 0.133, 0.019, 0.01, 0.013, 0.049, 1.0, 0.235, 0.009, 0.013, 0.068, 1.0, 0.065, 0.014, 0.023, 1.0, 0.083, 0.006, 0.002, 0.003, 0.011, 0.032, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148, 1.0, 0.031, 0.053, 0.022, 0.009, 0.007, 0.011, 1.0, 0.025, 0.042, 0.213, 0.981, 0.117, 0.034], 'utility': [-0.036, 0.182, -0.025, 0.127, 0.182, 0.013, 0.087, -0.292]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.01, 1.0, 0.005, 0.001, 0.001, 0.001, 0.011, 0.256, 0.142, 0.019, 0.01, 0.013, 0.049, 1.0, 0.256, 0.009, 0.014, 0.067, 1.0, 0.074, 0.015, 0.02, 1.0, 0.069, 0.005, 0.002, 0.003, 0.01, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.018, 0.019, 0.009, 0.005, 0.004, 0.007, 1.0, 0.015, 0.024, 0.092, 0.254, 0.057, 0.02], 'utility': [-0.012, 0.208, -0.03, 0.116, 0.208, -0.037, 0.234, -0.128]} reward=0.07 t=50
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 5, 3, 6, 5, 0, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.019, 0.251, 0.124, 0.018, 0.01, 0.013, 0.05, 1.0, 0.217, 0.008, 0.013, 0.07, 1.0, 0.058, 0.013, 0.026, 1.0, 0.101, 0.007, 0.003, 0.003, 0.012, 0.027, 0.007, 0.003, 0.004, 0.014, 1.0, 0.115, 1.0, 0.053, 0.155, 0.058, 0.018, 0.012, 0.017, 0.272, 0.01, 0.018, 0.111, 1.0, 0.055, 0.014], 'utility': [-0.035, 0.155, 0.114, -0.036, 0.155, 0.022, -0.066, -0.003]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.012, 1.0, 0.005, 0.001, 0.001, 0.002, 0.015, 0.253, 0.133, 0.019, 0.01, 0.013, 0.049, 1.0, 0.235, 0.009, 0.013, 0.068, 1.0, 0.065, 0.014, 0.023, 1.0, 0.083, 0.006, 0.002, 0.003, 0.011, 0.032, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148, 1.0, 0.031, 0.053, 0.022, 0.009, 0.007, 0.011, 1.0, 0.025, 0.042, 0.213, 0.981, 0.117, 0.034], 'utility': [-0.036, 0.182, -0.025, 0.127, 0.182, 0.013, 0.087, -0.292]} reward=0.027 t=51
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 5, 1, 0, 7, 3, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.018, 1.0, 0.007, 0.002, 0.001, 0.003, 0.026, 0.248, 0.116, 0.017, 0.01, 0.013, 0.05, 1.0, 0.201, 0.008, 0.013, 0.073, 1.0, 0.052, 0.012, 0.031, 1.0, 0.123, 0.008, 0.003, 0.004, 0.013, 0.023, 0.006, 0.003, 0.003, 0.012, 1.0, 0.089, 1.0, 0.085, 0.431, 0.141, 0.032, 0.019, 0.025, 0.069, 0.004, 0.006, 0.046, 1.0, 0.021, 0.005], 'utility': [-0.037, 0.127, 0.118, 0.072, 0.127, 0.064, -0.025, 0.051]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.019, 0.251, 0.124, 0.018, 0.01, 0.013, 0.05, 1.0, 0.217, 0.008, 0.013, 0.07, 1.0, 0.058, 0.013, 0.026, 1.0, 0.101, 0.007, 0.003, 0.003, 0.012, 0.027, 0.007, 0.003, 0.004, 0.014, 1.0, 0.115, 1.0, 0.053, 0.155, 0.058, 0.018, 0.012, 0.017, 0.272, 0.01, 0.018, 0.111, 1.0, 0.055, 0.014], 'utility': [-0.035, 0.155, 0.114, -0.036, 0.155, 0.022, -0.066, -0.003]} reward=0.045 t=52
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 2, 1, 0, 7, 4, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.021, 1.0, 0.008, 0.002, 0.002, 0.003, 0.034, 0.247, 0.109, 0.017, 0.01, 0.013, 0.051, 1.0, 0.188, 0.008, 0.013, 0.076, 1.0, 0.047, 0.011, 0.036, 1.0, 0.151, 0.009, 0.004, 0.004, 0.014, 0.019, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068, 0.894, 0.111, 1.0, 0.286, 0.047, 0.025, 0.032, 0.016, 0.001, 0.002, 0.015, 1.0, 0.007, 0.001], 'utility': [-0.037, 0.099, 0.13, 0.111, 0.099, 0.107, 0.015, 0.111]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.018, 1.0, 0.007, 0.002, 0.001, 0.003, 0.026, 0.248, 0.116, 0.017, 0.01, 0.013, 0.05, 1.0, 0.201, 0.008, 0.013, 0.073, 1.0, 0.052, 0.012, 0.031, 1.0, 0.123, 0.008, 0.003, 0.004, 0.013, 0.023, 0.006, 0.003, 0.003, 0.012, 1.0, 0.089, 1.0, 0.085, 0.431, 0.141, 0.032, 0.019, 0.025, 0.069, 0.004, 0.006, 0.046, 1.0, 0.021, 0.005], 'utility': [-0.037, 0.127, 0.118, 0.072, 0.127, 0.064, -0.025, 0.051]} reward=0.066 t=53
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 2, 1, 0, 7, 4, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.025, 1.0, 0.01, 0.002, 0.002, 0.004, 0.045, 0.245, 0.103, 0.016, 0.009, 0.013, 0.052, 1.0, 0.177, 0.007, 0.013, 0.081, 1.0, 0.043, 0.01, 0.042, 1.0, 0.186, 0.011, 0.004, 0.005, 0.016, 0.016, 0.004, 0.002, 0.002, 0.009, 1.0, 0.052, 0.376, 0.064, 1.0, 0.252, 0.03, 0.014, 0.018, 0.004, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [-0.038, 0.069, 0.126, 0.152, 0.069, 0.154, 0.04, 0.139]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.021, 1.0, 0.008, 0.002, 0.002, 0.003, 0.034, 0.247, 0.109, 0.017, 0.01, 0.013, 0.051, 1.0, 0.188, 0.008, 0.013, 0.076, 1.0, 0.047, 0.011, 0.036, 1.0, 0.151, 0.009, 0.004, 0.004, 0.014, 0.019, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068, 0.894, 0.111, 1.0, 0.286, 0.047, 0.025, 0.032, 0.016, 0.001, 0.002, 0.015, 1.0, 0.007, 0.001], 'utility': [-0.037, 0.099, 0.13, 0.111, 0.099, 0.107, 0.015, 0.111]} reward=0.077 t=54
DEBUG:deepcomp.util.simulation:Step                           action=[5, 7, 2, 1, 0, 7, 4, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.03, 1.0, 0.011, 0.003, 0.002, 0.005, 0.06, 0.244, 0.097, 0.016, 0.009, 0.013, 0.053, 1.0, 0.167, 0.007, 0.013, 0.086, 1.0, 0.04, 0.01, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.013, 0.003, 0.001, 0.002, 0.007, 1.0, 0.039, 0.179, 0.039, 1.0, 0.23, 0.021, 0.009, 0.011, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.039, 0.04, 0.16, 0.145, 0.04, 0.203, 0.124, 0.145]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.025, 1.0, 0.01, 0.002, 0.002, 0.004, 0.045, 0.245, 0.103, 0.016, 0.009, 0.013, 0.052, 1.0, 0.177, 0.007, 0.013, 0.081, 1.0, 0.043, 0.01, 0.042, 1.0, 0.186, 0.011, 0.004, 0.005, 0.016, 0.016, 0.004, 0.002, 0.002, 0.009, 1.0, 0.052, 0.376, 0.064, 1.0, 0.252, 0.03, 0.014, 0.018, 0.004, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [-0.038, 0.069, 0.126, 0.152, 0.069, 0.154, 0.04, 0.139]} reward=0.095 t=55
DEBUG:deepcomp.util.simulation:Step                           action=[5, 0, 5, 3, 0, 7, 6, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.079, 0.243, 0.092, 0.015, 0.009, 0.013, 0.054, 1.0, 0.159, 0.007, 0.013, 0.093, 1.0, 0.037, 0.01, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.01, 0.002, 0.001, 0.001, 0.006, 1.0, 0.028, 0.101, 0.027, 1.0, 0.226, 0.016, 0.007, 0.008, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.04, 0.027, 0.162, 0.143, 0.027, 0.256, 0.162, 0.143]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.03, 1.0, 0.011, 0.003, 0.002, 0.005, 0.06, 0.244, 0.097, 0.016, 0.009, 0.013, 0.053, 1.0, 0.167, 0.007, 0.013, 0.086, 1.0, 0.04, 0.01, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.013, 0.003, 0.001, 0.002, 0.007, 1.0, 0.039, 0.179, 0.039, 1.0, 0.23, 0.021, 0.009, 0.011, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.039, 0.04, 0.16, 0.145, 0.04, 0.203, 0.124, 0.145]} reward=0.102 t=56
DEBUG:deepcomp.util.simulation:Step                           action=[5, 0, 4, 3, 0, 7, 6, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 1.0, 0.014, 0.004, 0.003, 0.007, 0.103, 0.242, 0.087, 0.015, 0.009, 0.013, 0.056, 1.0, 0.153, 0.007, 0.013, 0.102, 1.0, 0.035, 0.009, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.008, 0.002, 0.001, 0.001, 0.005, 1.0, 0.021, 0.07, 0.022, 1.0, 0.247, 0.014, 0.006, 0.006, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.041, 0.014, 0.165, 0.14, 0.014, 0.312, 0.168, 0.14]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.079, 0.243, 0.092, 0.015, 0.009, 0.013, 0.054, 1.0, 0.159, 0.007, 0.013, 0.093, 1.0, 0.037, 0.01, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.01, 0.002, 0.001, 0.001, 0.006, 1.0, 0.028, 0.101, 0.027, 1.0, 0.226, 0.016, 0.007, 0.008, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.04, 0.027, 0.162, 0.143, 0.027, 0.256, 0.162, 0.143]} reward=0.11 t=57
DEBUG:deepcomp.util.simulation:Step                           action=[5, 0, 4, 3, 0, 7, 6, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.048, 1.0, 0.016, 0.005, 0.004, 0.009, 0.134, 0.241, 0.083, 0.015, 0.009, 0.013, 0.057, 1.0, 0.149, 0.007, 0.014, 0.113, 1.0, 0.034, 0.009, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.015, 0.059, 0.021, 1.0, 0.297, 0.014, 0.006, 0.006, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.043, -0.001, 0.166, 0.136, -0.001, 0.374, 0.142, 0.136]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 1.0, 0.014, 0.004, 0.003, 0.007, 0.103, 0.242, 0.087, 0.015, 0.009, 0.013, 0.056, 1.0, 0.153, 0.007, 0.013, 0.102, 1.0, 0.035, 0.009, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.008, 0.002, 0.001, 0.001, 0.005, 1.0, 0.021, 0.07, 0.022, 1.0, 0.247, 0.014, 0.006, 0.006, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.041, 0.014, 0.165, 0.14, 0.014, 0.312, 0.168, 0.14]} reward=0.114 t=58
DEBUG:deepcomp.util.simulation:Step                           action=[5, 0, 4, 3, 0, 7, 6, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.055, 1.0, 0.018, 0.005, 0.005, 0.011, 0.173, 0.241, 0.079, 0.014, 0.009, 0.013, 0.059, 1.0, 0.145, 0.007, 0.014, 0.126, 1.0, 0.032, 0.009, 0.056, 1.0, 0.265, 0.014, 0.005, 0.006, 0.019, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.01, 0.058, 0.023, 1.0, 0.376, 0.017, 0.007, 0.007, 0.003, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [-0.044, -0.024, 0.168, 0.125, -0.024, 0.441, 0.093, 0.125]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.048, 1.0, 0.016, 0.005, 0.004, 0.009, 0.134, 0.241, 0.083, 0.015, 0.009, 0.013, 0.057, 1.0, 0.149, 0.007, 0.014, 0.113, 1.0, 0.034, 0.009, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.015, 0.059, 0.021, 1.0, 0.297, 0.014, 0.006, 0.006, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.043, -0.001, 0.166, 0.136, -0.001, 0.374, 0.142, 0.136]} reward=0.114 t=59
DEBUG:deepcomp.util.simulation:Step                           action=[5, 0, 5, 3, 0, 7, 4, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.063, 1.0, 0.02, 0.006, 0.005, 0.013, 0.223, 0.241, 0.076, 0.014, 0.009, 0.014, 0.061, 1.0, 0.143, 0.007, 0.015, 0.142, 1.0, 0.032, 0.009, 0.063, 1.0, 0.306, 0.016, 0.006, 0.006, 0.02, 0.003, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007, 0.063, 0.028, 1.0, 0.476, 0.022, 0.008, 0.009, 0.006, 0.001, 0.001, 0.011, 1.0, 0.003, 0.001], 'utility': [-0.046, -0.047, 0.169, 0.108, -0.047, 0.514, -0.055, 0.108]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.055, 1.0, 0.018, 0.005, 0.005, 0.011, 0.173, 0.241, 0.079, 0.014, 0.009, 0.013, 0.059, 1.0, 0.145, 0.007, 0.014, 0.126, 1.0, 0.032, 0.009, 0.056, 1.0, 0.265, 0.014, 0.005, 0.006, 0.019, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.01, 0.058, 0.023, 1.0, 0.376, 0.017, 0.007, 0.007, 0.003, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [-0.044, -0.024, 0.168, 0.125, -0.024, 0.441, 0.093, 0.125]} reward=0.099 t=60
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 4, 1, 0, 7, 4, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 1.0, 0.022, 0.007, 0.006, 0.015, 0.286, 0.242, 0.073, 0.014, 0.009, 0.014, 0.063, 1.0, 0.141, 0.008, 0.016, 0.162, 1.0, 0.031, 0.009, 0.073, 1.0, 0.355, 0.018, 0.007, 0.007, 0.022, 0.002, 0.0, 0.0, 0.0, 0.002, 1.0, 0.004, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.012, 0.001, 0.002, 0.022, 1.0, 0.005, 0.001], 'utility': [-0.048, -0.015, 0.058, 0.083, -0.071, 0.595, -0.036, 0.083]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.063, 1.0, 0.02, 0.006, 0.005, 0.013, 0.223, 0.241, 0.076, 0.014, 0.009, 0.014, 0.061, 1.0, 0.143, 0.007, 0.015, 0.142, 1.0, 0.032, 0.009, 0.063, 1.0, 0.306, 0.016, 0.006, 0.006, 0.02, 0.003, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007, 0.063, 0.028, 1.0, 0.476, 0.022, 0.008, 0.009, 0.006, 0.001, 0.001, 0.011, 1.0, 0.003, 0.001], 'utility': [-0.046, -0.047, 0.169, 0.108, -0.047, 0.514, -0.055, 0.108]} reward=0.088 t=61
DEBUG:deepcomp.util.simulation:Step                           action=[0, 0, 3, 2, 0, 7, 4, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.08, 1.0, 0.024, 0.008, 0.007, 0.018, 0.365, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.141, 0.008, 0.017, 0.186, 1.0, 0.031, 0.009, 0.083, 1.0, 0.413, 0.02, 0.007, 0.008, 0.024, 0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.003, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.023, 0.002, 0.004, 0.044, 1.0, 0.009, 0.002], 'utility': [-0.052, -0.028, 0.058, 0.051, -0.096, 0.686, -0.135, 0.051]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 1.0, 0.022, 0.007, 0.006, 0.015, 0.286, 0.242, 0.073, 0.014, 0.009, 0.014, 0.063, 1.0, 0.141, 0.008, 0.016, 0.162, 1.0, 0.031, 0.009, 0.073, 1.0, 0.355, 0.018, 0.007, 0.007, 0.022, 0.002, 0.0, 0.0, 0.0, 0.002, 1.0, 0.004, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.012, 0.001, 0.002, 0.022, 1.0, 0.005, 0.001], 'utility': [-0.048, -0.015, 0.058, 0.083, -0.071, 0.595, -0.036, 0.083]} reward=0.069 t=62
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 2, 4, 0, 7, 4, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.09, 1.0, 0.026, 0.009, 0.008, 0.021, 0.465, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.141, 0.008, 0.018, 0.216, 1.0, 0.031, 0.009, 0.097, 1.0, 0.482, 0.023, 0.008, 0.009, 0.026, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.002, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.042, 0.003, 0.007, 0.086, 1.0, 0.014, 0.004], 'utility': [-0.055, -0.039, 0.058, 0.045, -0.12, 0.788, -0.08, 0.012]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.08, 1.0, 0.024, 0.008, 0.007, 0.018, 0.365, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.141, 0.008, 0.017, 0.186, 1.0, 0.031, 0.009, 0.083, 1.0, 0.413, 0.02, 0.007, 0.008, 0.024, 0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.003, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.023, 0.002, 0.004, 0.044, 1.0, 0.009, 0.002], 'utility': [-0.052, -0.028, 0.058, 0.051, -0.096, 0.686, -0.135, 0.051]} reward=0.077 t=63
DEBUG:deepcomp.util.simulation:Step                           action=[0, 0, 4, 2, 0, 7, 6, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.1, 1.0, 0.029, 0.01, 0.009, 0.025, 0.59, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.142, 0.009, 0.019, 0.251, 1.0, 0.031, 0.01, 0.112, 1.0, 0.563, 0.026, 0.009, 0.01, 0.029, 0.001, 0.0, 0.0, 0.0, 0.0, 1.0, 0.001, 0.053, 0.025, 1.0, 0.346, 0.018, 0.007, 0.008, 0.075, 0.005, 0.012, 0.162, 1.0, 0.021, 0.006], 'utility': [-0.06, -0.048, 0.058, -0.002, -0.144, 0.906, -0.005, -0.005]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.09, 1.0, 0.026, 0.009, 0.008, 0.021, 0.465, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.141, 0.008, 0.018, 0.216, 1.0, 0.031, 0.009, 0.097, 1.0, 0.482, 0.023, 0.008, 0.009, 0.026, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.002, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.042, 0.003, 0.007, 0.086, 1.0, 0.014, 0.004], 'utility': [-0.055, -0.039, 0.058, 0.045, -0.12, 0.788, -0.08, 0.012]} reward=0.075 t=64
DEBUG:deepcomp.util.simulation:Step                           action=[5, 0, 0, 2, 7, 0, 7, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.111, 1.0, 0.031, 0.011, 0.011, 0.029, 0.745, 0.252, 0.076, 0.014, 0.009, 0.014, 0.064, 1.0, 0.144, 0.009, 0.021, 0.295, 1.0, 0.032, 0.01, 0.13, 1.0, 0.658, 0.03, 0.011, 0.011, 0.032, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.036, 0.017, 1.0, 0.183, 0.01, 0.004, 0.005, 0.129, 0.008, 0.02, 0.295, 1.0, 0.03, 0.009], 'utility': [-0.066, -0.054, 0.055, -0.04, -0.168, 1.0, 0.106, -0.039]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.1, 1.0, 0.029, 0.01, 0.009, 0.025, 0.59, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.142, 0.009, 0.019, 0.251, 1.0, 0.031, 0.01, 0.112, 1.0, 0.563, 0.026, 0.009, 0.01, 0.029, 0.001, 0.0, 0.0, 0.0, 0.0, 1.0, 0.001, 0.053, 0.025, 1.0, 0.346, 0.018, 0.007, 0.008, 0.075, 0.005, 0.012, 0.162, 1.0, 0.021, 0.006], 'utility': [-0.06, -0.048, 0.058, -0.002, -0.144, 0.906, -0.005, -0.005]} reward=0.087 t=65
DEBUG:deepcomp.util.simulation:Step                           action=[5, 0, 0, 2, 7, 0, 0, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.122, 1.0, 0.034, 0.012, 0.012, 0.034, 0.939, 0.262, 0.081, 0.015, 0.01, 0.014, 0.064, 1.0, 0.147, 0.01, 0.023, 0.348, 1.0, 0.032, 0.01, 0.152, 1.0, 0.769, 0.034, 0.012, 0.012, 0.035, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.023, 0.011, 1.0, 0.086, 0.006, 0.002, 0.003, 0.213, 0.013, 0.032, 0.518, 1.0, 0.041, 0.014], 'utility': [-0.075, -0.058, 0.052, -0.054, -0.192, 1.0, 0.231, -0.045]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.111, 1.0, 0.031, 0.011, 0.011, 0.029, 0.745, 0.252, 0.076, 0.014, 0.009, 0.014, 0.064, 1.0, 0.144, 0.009, 0.021, 0.295, 1.0, 0.032, 0.01, 0.13, 1.0, 0.658, 0.03, 0.011, 0.011, 0.032, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.036, 0.017, 1.0, 0.183, 0.01, 0.004, 0.005, 0.129, 0.008, 0.02, 0.295, 1.0, 0.03, 0.009], 'utility': [-0.066, -0.054, 0.055, -0.04, -0.168, 1.0, 0.106, -0.039]} reward=0.099 t=66
DEBUG:deepcomp.util.simulation:Step                           action=[5, 3, 2, 2, 0, 0, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.113, 0.848, 0.031, 0.011, 0.012, 0.033, 1.0, 0.273, 0.087, 0.016, 0.01, 0.015, 0.063, 1.0, 0.15, 0.01, 0.025, 0.412, 1.0, 0.033, 0.011, 0.178, 1.0, 0.898, 0.039, 0.014, 0.013, 0.038, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.014, 0.007, 1.0, 0.036, 0.003, 0.001, 0.002, 0.34, 0.02, 0.051, 0.881, 1.0, 0.054, 0.02], 'utility': [-0.084, -0.059, 0.049, -0.082, -0.216, 1.0, 0.387, -0.06]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.122, 1.0, 0.034, 0.012, 0.012, 0.034, 0.939, 0.262, 0.081, 0.015, 0.01, 0.014, 0.064, 1.0, 0.147, 0.01, 0.023, 0.348, 1.0, 0.032, 0.01, 0.152, 1.0, 0.769, 0.034, 0.012, 0.012, 0.035, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.023, 0.011, 1.0, 0.086, 0.006, 0.002, 0.003, 0.213, 0.013, 0.032, 0.518, 1.0, 0.041, 0.014], 'utility': [-0.075, -0.058, 0.052, -0.054, -0.192, 1.0, 0.231, -0.045]} reward=0.107 t=67
DEBUG:deepcomp.util.simulation:Step                           action=[5, 3, 2, 2, 0, 0, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.098, 0.677, 0.027, 0.01, 0.01, 0.03, 1.0, 0.285, 0.093, 0.017, 0.01, 0.015, 0.063, 1.0, 0.153, 0.011, 0.027, 0.491, 1.0, 0.034, 0.011, 0.199, 0.955, 1.0, 0.043, 0.015, 0.014, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.008, 0.004, 1.0, 0.014, 0.001, 0.001, 0.001, 0.363, 0.02, 0.055, 1.0, 0.689, 0.048, 0.019], 'utility': [-0.089, -0.058, 0.045, -0.103, -0.239, 1.0, 0.55, -0.066]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.113, 0.848, 0.031, 0.011, 0.012, 0.033, 1.0, 0.273, 0.087, 0.016, 0.01, 0.015, 0.063, 1.0, 0.15, 0.01, 0.025, 0.412, 1.0, 0.033, 0.011, 0.178, 1.0, 0.898, 0.039, 0.014, 0.013, 0.038, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.014, 0.007, 1.0, 0.036, 0.003, 0.001, 0.002, 0.34, 0.02, 0.051, 0.881, 1.0, 0.054, 0.02], 'utility': [-0.084, -0.059, 0.049, -0.082, -0.216, 1.0, 0.387, -0.06]} reward=0.117 t=68
DEBUG:deepcomp.util.simulation:Step                           action=[5, 3, 2, 2, 0, 0, 5, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.085, 0.542, 0.023, 0.009, 0.009, 0.027, 1.0, 0.297, 0.101, 0.018, 0.011, 0.015, 0.063, 1.0, 0.157, 0.012, 0.03, 0.586, 1.0, 0.035, 0.012, 0.201, 0.822, 1.0, 0.043, 0.014, 0.014, 0.038, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.005, 0.003, 1.0, 0.007, 0.001, 0.0, 0.001, 0.343, 0.018, 0.053, 1.0, 0.433, 0.038, 0.016], 'utility': [-0.06, -0.054, 0.041, -0.12, -0.262, 1.0, 0.676, -0.064]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.098, 0.677, 0.027, 0.01, 0.01, 0.03, 1.0, 0.285, 0.093, 0.017, 0.01, 0.015, 0.063, 1.0, 0.153, 0.011, 0.027, 0.491, 1.0, 0.034, 0.011, 0.199, 0.955, 1.0, 0.043, 0.015, 0.014, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.008, 0.004, 1.0, 0.014, 0.001, 0.001, 0.001, 0.363, 0.02, 0.055, 1.0, 0.689, 0.048, 0.019], 'utility': [-0.089, -0.058, 0.045, -0.103, -0.239, 1.0, 0.55, -0.066]} reward=0.13 t=69
DEBUG:deepcomp.util.simulation:Step                           action=[5, 3, 2, 2, 0, 0, 5, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.074, 0.436, 0.02, 0.008, 0.008, 0.025, 1.0, 0.31, 0.109, 0.019, 0.011, 0.016, 0.063, 1.0, 0.162, 0.012, 0.032, 0.701, 1.0, 0.036, 0.013, 0.204, 0.71, 1.0, 0.043, 0.014, 0.013, 0.036, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.006, 0.004, 1.0, 0.005, 0.001, 0.0, 0.001, 0.327, 0.017, 0.052, 1.0, 0.283, 0.03, 0.014], 'utility': [0.008, -0.047, 0.037, -0.13, -0.285, 1.0, 0.687, -0.056]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.085, 0.542, 0.023, 0.009, 0.009, 0.027, 1.0, 0.297, 0.101, 0.018, 0.011, 0.015, 0.063, 1.0, 0.157, 0.012, 0.03, 0.586, 1.0, 0.035, 0.012, 0.201, 0.822, 1.0, 0.043, 0.014, 0.014, 0.038, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.005, 0.003, 1.0, 0.007, 0.001, 0.0, 0.001, 0.343, 0.018, 0.053, 1.0, 0.433, 0.038, 0.016], 'utility': [-0.06, -0.054, 0.041, -0.12, -0.262, 1.0, 0.676, -0.064]} reward=0.145 t=70
DEBUG:deepcomp.util.simulation:Step                           action=[5, 3, 2, 2, 0, 0, 4, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.323, 0.117, 0.02, 0.011, 0.016, 0.063, 1.0, 0.166, 0.013, 0.036, 0.839, 1.0, 0.037, 0.013, 0.208, 0.615, 1.0, 0.043, 0.014, 0.013, 0.034, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.012, 0.008, 1.0, 0.007, 0.001, 0.001, 0.001, 0.315, 0.016, 0.053, 1.0, 0.194, 0.025, 0.013], 'utility': [0.027, -0.047, 0.033, 0.037, -0.297, 1.0, 0.575, -0.102]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.074, 0.436, 0.02, 0.008, 0.008, 0.025, 1.0, 0.31, 0.109, 0.019, 0.011, 0.016, 0.063, 1.0, 0.162, 0.012, 0.032, 0.701, 1.0, 0.036, 0.013, 0.204, 0.71, 1.0, 0.043, 0.014, 0.013, 0.036, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.006, 0.004, 1.0, 0.005, 0.001, 0.0, 0.001, 0.327, 0.017, 0.052, 1.0, 0.283, 0.03, 0.014], 'utility': [0.008, -0.047, 0.037, -0.13, -0.285, 1.0, 0.687, -0.056]} reward=0.152 t=71
DEBUG:deepcomp.util.simulation:Step                           action=[5, 3, 3, 2, 3, 0, 0, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.338, 0.127, 0.021, 0.012, 0.017, 0.063, 1.0, 0.17, 0.014, 0.039, 1.0, 0.993, 0.039, 0.014, 0.213, 0.536, 1.0, 0.043, 0.014, 0.013, 0.033, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.028, 0.023, 1.0, 0.012, 0.002, 0.002, 0.003, 0.31, 0.015, 0.057, 1.0, 0.139, 0.021, 0.012], 'utility': [0.027, -0.05, 0.029, 0.03, -0.1, 1.0, 0.307, -0.08]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.323, 0.117, 0.02, 0.011, 0.016, 0.063, 1.0, 0.166, 0.013, 0.036, 0.839, 1.0, 0.037, 0.013, 0.208, 0.615, 1.0, 0.043, 0.014, 0.013, 0.034, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.012, 0.008, 1.0, 0.007, 0.001, 0.001, 0.001, 0.315, 0.016, 0.053, 1.0, 0.194, 0.025, 0.013], 'utility': [0.027, -0.047, 0.033, 0.037, -0.297, 1.0, 0.575, -0.102]} reward=0.14 t=72
DEBUG:deepcomp.util.simulation:Step                           action=[2, 3, 3, 2, 1, 4, 0, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.353, 0.138, 0.022, 0.012, 0.017, 0.063, 1.0, 0.146, 0.013, 0.035, 1.0, 0.828, 0.034, 0.012, 0.219, 0.47, 1.0, 0.043, 0.014, 0.012, 0.031, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.064, 0.069, 1.0, 0.02, 0.005, 0.004, 0.007, 0.312, 0.016, 0.064, 1.0, 0.106, 0.018, 0.011], 'utility': [0.019, -0.052, -0.026, 0.025, -0.018, 1.0, 0.018, -0.008]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.338, 0.127, 0.021, 0.012, 0.017, 0.063, 1.0, 0.17, 0.014, 0.039, 1.0, 0.993, 0.039, 0.014, 0.213, 0.536, 1.0, 0.043, 0.014, 0.013, 0.033, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.028, 0.023, 1.0, 0.012, 0.002, 0.002, 0.003, 0.31, 0.015, 0.057, 1.0, 0.139, 0.021, 0.012], 'utility': [0.027, -0.05, 0.029, 0.03, -0.1, 1.0, 0.307, -0.08]} reward=0.147 t=73
DEBUG:deepcomp.util.simulation:Step                           action=[2, 1, 3, 1, 7, 4, 0, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.075, 0.404, 0.019, 0.007, 0.008, 0.024, 1.0, 0.368, 0.15, 0.023, 0.013, 0.017, 0.064, 1.0, 0.126, 0.011, 0.032, 1.0, 0.69, 0.029, 0.011, 0.227, 0.414, 1.0, 0.044, 0.014, 0.012, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.132, 0.196, 1.0, 0.032, 0.009, 0.007, 0.017, 0.322, 0.017, 0.076, 1.0, 0.086, 0.017, 0.011], 'utility': [0.013, -0.046, -0.031, 0.021, -0.059, 0.942, -0.035, -0.004]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.353, 0.138, 0.022, 0.012, 0.017, 0.063, 1.0, 0.146, 0.013, 0.035, 1.0, 0.828, 0.034, 0.012, 0.219, 0.47, 1.0, 0.043, 0.014, 0.012, 0.031, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.064, 0.069, 1.0, 0.02, 0.005, 0.004, 0.007, 0.312, 0.016, 0.064, 1.0, 0.106, 0.018, 0.011], 'utility': [0.019, -0.052, -0.026, 0.025, -0.018, 1.0, 0.018, -0.008]} reward=0.12 t=74
DEBUG:deepcomp.util.simulation:Step                           action=[2, 1, 3, 1, 7, 4, 2, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.08, 0.4, 0.019, 0.008, 0.008, 0.025, 1.0, 0.384, 0.163, 0.025, 0.014, 0.018, 0.064, 1.0, 0.109, 0.01, 0.03, 1.0, 0.576, 0.025, 0.01, 0.236, 0.367, 1.0, 0.045, 0.014, 0.012, 0.029, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.242, 0.537, 1.0, 0.046, 0.015, 0.014, 0.035, 0.34, 0.019, 0.097, 1.0, 0.074, 0.017, 0.012], 'utility': [0.007, -0.06, -0.037, 0.019, -0.034, 0.821, -0.148, -0.009]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.075, 0.404, 0.019, 0.007, 0.008, 0.024, 1.0, 0.368, 0.15, 0.023, 0.013, 0.017, 0.064, 1.0, 0.126, 0.011, 0.032, 1.0, 0.69, 0.029, 0.011, 0.227, 0.414, 1.0, 0.044, 0.014, 0.012, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.132, 0.196, 1.0, 0.032, 0.009, 0.007, 0.017, 0.322, 0.017, 0.076, 1.0, 0.086, 0.017, 0.011], 'utility': [0.013, -0.046, -0.031, 0.021, -0.059, 0.942, -0.035, -0.004]} reward=0.097 t=75
DEBUG:deepcomp.util.simulation:Step                           action=[2, 3, 5, 2, 7, 4, 7, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.087, 0.398, 0.02, 0.008, 0.008, 0.025, 1.0, 0.401, 0.177, 0.026, 0.014, 0.019, 0.065, 1.0, 0.094, 0.009, 0.027, 1.0, 0.482, 0.022, 0.009, 0.248, 0.328, 1.0, 0.047, 0.014, 0.012, 0.028, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001, 0.269, 1.0, 0.682, 0.043, 0.016, 0.016, 0.046, 0.368, 0.023, 0.13, 1.0, 0.067, 0.017, 0.013], 'utility': [0.004, -0.051, -0.044, 0.018, -0.045, 0.714, -0.188, -0.024]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.08, 0.4, 0.019, 0.008, 0.008, 0.025, 1.0, 0.384, 0.163, 0.025, 0.014, 0.018, 0.064, 1.0, 0.109, 0.01, 0.03, 1.0, 0.576, 0.025, 0.01, 0.236, 0.367, 1.0, 0.045, 0.014, 0.012, 0.029, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.242, 0.537, 1.0, 0.046, 0.015, 0.014, 0.035, 0.34, 0.019, 0.097, 1.0, 0.074, 0.017, 0.012], 'utility': [0.007, -0.06, -0.037, 0.019, -0.034, 0.821, -0.148, -0.009]} reward=0.07 t=76
DEBUG:deepcomp.util.simulation:Step                           action=[2, 3, 5, 2, 7, 4, 7, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.097, 0.399, 0.02, 0.008, 0.009, 0.026, 1.0, 0.419, 0.193, 0.028, 0.015, 0.019, 0.065, 1.0, 0.081, 0.008, 0.025, 1.0, 0.404, 0.019, 0.008, 0.262, 0.296, 1.0, 0.049, 0.014, 0.012, 0.028, 0.002, 0.0, 0.0, 0.0, 0.003, 1.0, 0.001, 0.142, 1.0, 0.244, 0.02, 0.008, 0.009, 0.031, 0.403, 0.028, 0.184, 1.0, 0.064, 0.018, 0.014], 'utility': [0.0, -0.047, -0.05, 0.019, -0.023, 0.621, -0.248, -0.045]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.087, 0.398, 0.02, 0.008, 0.008, 0.025, 1.0, 0.401, 0.177, 0.026, 0.014, 0.019, 0.065, 1.0, 0.094, 0.009, 0.027, 1.0, 0.482, 0.022, 0.009, 0.248, 0.328, 1.0, 0.047, 0.014, 0.012, 0.028, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001, 0.269, 1.0, 0.682, 0.043, 0.016, 0.016, 0.046, 0.368, 0.023, 0.13, 1.0, 0.067, 0.017, 0.013], 'utility': [0.004, -0.051, -0.044, 0.018, -0.045, 0.714, -0.188, -0.024]} reward=0.048 t=77
DEBUG:deepcomp.util.simulation:Step                           action=[7, 3, 5, 2, 7, 4, 7, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.11, 0.403, 0.021, 0.009, 0.009, 0.028, 1.0, 0.437, 0.211, 0.03, 0.016, 0.02, 0.066, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.278, 0.268, 1.0, 0.051, 0.015, 0.012, 0.027, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.065, 1.0, 0.082, 0.008, 0.004, 0.005, 0.018, 0.444, 0.036, 0.273, 1.0, 0.064, 0.019, 0.017], 'utility': [-0.002, -0.048, -0.056, 0.019, 0.065, 0.537, -0.371, -0.072]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.097, 0.399, 0.02, 0.008, 0.009, 0.026, 1.0, 0.419, 0.193, 0.028, 0.015, 0.019, 0.065, 1.0, 0.081, 0.008, 0.025, 1.0, 0.404, 0.019, 0.008, 0.262, 0.296, 1.0, 0.049, 0.014, 0.012, 0.028, 0.002, 0.0, 0.0, 0.0, 0.003, 1.0, 0.001, 0.142, 1.0, 0.244, 0.02, 0.008, 0.009, 0.031, 0.403, 0.028, 0.184, 1.0, 0.064, 0.018, 0.014], 'utility': [0.0, -0.047, -0.05, 0.019, -0.023, 0.621, -0.248, -0.045]} reward=0.028 t=78
DEBUG:deepcomp.util.simulation:Step                           action=[3, 3, 5, 2, 7, 3, 7, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.128, 0.409, 0.023, 0.009, 0.01, 0.03, 1.0, 0.456, 0.231, 0.032, 0.016, 0.02, 0.067, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.298, 0.245, 1.0, 0.054, 0.015, 0.013, 0.027, 0.003, 0.0, 0.0, 0.001, 0.007, 1.0, 0.002, 0.025, 1.0, 0.025, 0.003, 0.002, 0.002, 0.009, 0.491, 0.047, 0.421, 1.0, 0.065, 0.021, 0.02], 'utility': [-0.005, -0.052, -0.062, 0.019, 0.001, 0.462, -0.375, -0.071]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.11, 0.403, 0.021, 0.009, 0.009, 0.028, 1.0, 0.437, 0.211, 0.03, 0.016, 0.02, 0.066, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.278, 0.268, 1.0, 0.051, 0.015, 0.012, 0.027, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.065, 1.0, 0.082, 0.008, 0.004, 0.005, 0.018, 0.444, 0.036, 0.273, 1.0, 0.064, 0.019, 0.017], 'utility': [-0.002, -0.048, -0.056, 0.019, 0.065, 0.537, -0.371, -0.072]} reward=0.006 t=79
DEBUG:deepcomp.util.simulation:Step                           action=[7, 3, 5, 2, 7, 3, 7, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.151, 0.418, 0.025, 0.01, 0.011, 0.033, 1.0, 0.475, 0.252, 0.034, 0.017, 0.021, 0.067, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.321, 0.226, 1.0, 0.058, 0.016, 0.013, 0.027, 0.004, 0.001, 0.0, 0.001, 0.01, 1.0, 0.003, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.54, 0.061, 0.676, 1.0, 0.068, 0.024, 0.024], 'utility': [-0.006, -0.061, -0.069, 0.019, -0.017, 0.393, -0.386, -0.08]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.128, 0.409, 0.023, 0.009, 0.01, 0.03, 1.0, 0.456, 0.231, 0.032, 0.016, 0.02, 0.067, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.298, 0.245, 1.0, 0.054, 0.015, 0.013, 0.027, 0.003, 0.0, 0.0, 0.001, 0.007, 1.0, 0.002, 0.025, 1.0, 0.025, 0.003, 0.002, 0.002, 0.009, 0.491, 0.047, 0.421, 1.0, 0.065, 0.021, 0.02], 'utility': [-0.005, -0.052, -0.062, 0.019, 0.001, 0.462, -0.375, -0.071]} reward=-0.01 t=80
DEBUG:deepcomp.util.simulation:Step                           action=[7, 3, 5, 2, 7, 3, 7, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.182, 0.43, 0.028, 0.011, 0.012, 0.037, 1.0, 0.495, 0.277, 0.036, 0.018, 0.022, 0.068, 1.0, 0.1, 0.01, 0.028, 1.0, 0.539, 0.024, 0.009, 0.348, 0.21, 1.0, 0.062, 0.017, 0.013, 0.027, 0.006, 0.001, 0.001, 0.001, 0.014, 1.0, 0.004, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.527, 0.072, 1.0, 0.893, 0.064, 0.024, 0.026], 'utility': [-0.008, 0.002, -0.075, 0.017, -0.071, 0.33, -0.172, -0.083]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.151, 0.418, 0.025, 0.01, 0.011, 0.033, 1.0, 0.475, 0.252, 0.034, 0.017, 0.021, 0.067, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.321, 0.226, 1.0, 0.058, 0.016, 0.013, 0.027, 0.004, 0.001, 0.0, 0.001, 0.01, 1.0, 0.003, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.54, 0.061, 0.676, 1.0, 0.068, 0.024, 0.024], 'utility': [-0.006, -0.061, -0.069, 0.019, -0.017, 0.393, -0.386, -0.08]} reward=-0.026 t=81
DEBUG:deepcomp.util.simulation:Step                           action=[0, 3, 5, 2, 1, 3, 6, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.223, 0.443, 0.031, 0.013, 0.014, 0.041, 1.0, 0.515, 0.303, 0.038, 0.019, 0.022, 0.069, 1.0, 0.126, 0.011, 0.033, 1.0, 0.742, 0.03, 0.011, 0.379, 0.197, 1.0, 0.067, 0.018, 0.014, 0.027, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.333, 0.056, 1.0, 0.521, 0.04, 0.016, 0.018], 'utility': [-0.021, -0.009, -0.108, 0.021, -0.075, 0.311, -0.179, -0.057]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.182, 0.43, 0.028, 0.011, 0.012, 0.037, 1.0, 0.495, 0.277, 0.036, 0.018, 0.022, 0.068, 1.0, 0.1, 0.01, 0.028, 1.0, 0.539, 0.024, 0.009, 0.348, 0.21, 1.0, 0.062, 0.017, 0.013, 0.027, 0.006, 0.001, 0.001, 0.001, 0.014, 1.0, 0.004, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.527, 0.072, 1.0, 0.893, 0.064, 0.024, 0.026], 'utility': [-0.008, 0.002, -0.075, 0.017, -0.071, 0.33, -0.172, -0.083]} reward=-0.008 t=82
DEBUG:deepcomp.util.simulation:Step                           action=[0, 3, 5, 1, 7, 3, 0, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.279, 0.459, 0.035, 0.015, 0.016, 0.047, 1.0, 0.536, 0.333, 0.041, 0.02, 0.023, 0.07, 1.0, 0.155, 0.013, 0.037, 0.978, 1.0, 0.037, 0.013, 0.416, 0.186, 1.0, 0.073, 0.019, 0.014, 0.028, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.053, 1.0, 0.061, 0.007, 0.003, 0.004, 0.016, 0.201, 0.041, 1.0, 0.293, 0.024, 0.01, 0.012], 'utility': [-0.027, -0.029, -0.089, 0.031, -0.067, 0.318, -0.202, -0.027]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.223, 0.443, 0.031, 0.013, 0.014, 0.041, 1.0, 0.515, 0.303, 0.038, 0.019, 0.022, 0.069, 1.0, 0.126, 0.011, 0.033, 1.0, 0.742, 0.03, 0.011, 0.379, 0.197, 1.0, 0.067, 0.018, 0.014, 0.027, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.333, 0.056, 1.0, 0.521, 0.04, 0.016, 0.018], 'utility': [-0.021, -0.009, -0.108, 0.021, -0.075, 0.311, -0.179, -0.057]} reward=-0.015 t=83
DEBUG:deepcomp.util.simulation:Step                           action=[0, 3, 5, 1, 7, 1, 6, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.354, 0.477, 0.04, 0.017, 0.019, 0.054, 1.0, 0.558, 0.366, 0.043, 0.021, 0.024, 0.071, 1.0, 0.141, 0.012, 0.031, 0.708, 1.0, 0.034, 0.012, 0.459, 0.177, 1.0, 0.081, 0.021, 0.015, 0.028, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.125, 1.0, 0.185, 0.017, 0.007, 0.008, 0.028, 0.115, 0.029, 1.0, 0.158, 0.014, 0.006, 0.008], 'utility': [-0.023, -0.054, -0.095, 0.047, -0.083, 0.313, -0.235, 0.058]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.279, 0.459, 0.035, 0.015, 0.016, 0.047, 1.0, 0.536, 0.333, 0.041, 0.02, 0.023, 0.07, 1.0, 0.155, 0.013, 0.037, 0.978, 1.0, 0.037, 0.013, 0.416, 0.186, 1.0, 0.073, 0.019, 0.014, 0.028, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.053, 1.0, 0.061, 0.007, 0.003, 0.004, 0.016, 0.201, 0.041, 1.0, 0.293, 0.024, 0.01, 0.012], 'utility': [-0.027, -0.029, -0.089, 0.031, -0.067, 0.318, -0.202, -0.027]} reward=-0.012 t=84
DEBUG:deepcomp.util.simulation:Step                           action=[0, 3, 5, 1, 7, 1, 3, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.456, 0.495, 0.046, 0.02, 0.022, 0.062, 1.0, 0.579, 0.403, 0.046, 0.022, 0.025, 0.072, 1.0, 0.127, 0.01, 0.025, 0.512, 1.0, 0.031, 0.01, 0.509, 0.17, 1.0, 0.089, 0.022, 0.016, 0.029, 0.005, 0.001, 0.001, 0.001, 0.011, 1.0, 0.003, 0.251, 1.0, 0.518, 0.037, 0.014, 0.015, 0.044, 0.062, 0.019, 1.0, 0.081, 0.008, 0.004, 0.005], 'utility': [-0.067, -0.083, -0.102, 0.108, -0.129, 0.425, -0.21, 0.106]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.354, 0.477, 0.04, 0.017, 0.019, 0.054, 1.0, 0.558, 0.366, 0.043, 0.021, 0.024, 0.071, 1.0, 0.141, 0.012, 0.031, 0.708, 1.0, 0.034, 0.012, 0.459, 0.177, 1.0, 0.081, 0.021, 0.015, 0.028, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.125, 1.0, 0.185, 0.017, 0.007, 0.008, 0.028, 0.115, 0.029, 1.0, 0.158, 0.014, 0.006, 0.008], 'utility': [-0.023, -0.054, -0.095, 0.047, -0.083, 0.313, -0.235, 0.058]} reward=-0.013 t=85
DEBUG:deepcomp.util.simulation:Step                           action=[0, 3, 6, 2, 7, 1, 6, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.596, 0.515, 0.053, 0.023, 0.026, 0.072, 1.0, 0.602, 0.444, 0.049, 0.023, 0.025, 0.073, 1.0, 0.114, 0.009, 0.021, 0.371, 1.0, 0.028, 0.009, 0.566, 0.164, 1.0, 0.1, 0.024, 0.017, 0.03, 0.003, 0.001, 0.0, 0.001, 0.007, 1.0, 0.002, 0.319, 0.722, 1.0, 0.055, 0.018, 0.017, 0.045, 0.031, 0.012, 1.0, 0.038, 0.004, 0.002, 0.003], 'utility': [-0.031, -0.116, -0.109, 0.124, -0.137, 0.472, -0.174, 0.201]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.456, 0.495, 0.046, 0.02, 0.022, 0.062, 1.0, 0.579, 0.403, 0.046, 0.022, 0.025, 0.072, 1.0, 0.127, 0.01, 0.025, 0.512, 1.0, 0.031, 0.01, 0.509, 0.17, 1.0, 0.089, 0.022, 0.016, 0.029, 0.005, 0.001, 0.001, 0.001, 0.011, 1.0, 0.003, 0.251, 1.0, 0.518, 0.037, 0.014, 0.015, 0.044, 0.062, 0.019, 1.0, 0.081, 0.008, 0.004, 0.005], 'utility': [-0.067, -0.083, -0.102, 0.108, -0.129, 0.425, -0.21, 0.106]} reward=0.006 t=86
DEBUG:deepcomp.util.simulation:Step                           action=[0, 3, 5, 2, 7, 1, 6, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.79, 0.536, 0.061, 0.028, 0.031, 0.084, 1.0, 0.624, 0.489, 0.053, 0.024, 0.026, 0.074, 1.0, 0.102, 0.007, 0.017, 0.269, 1.0, 0.026, 0.008, 0.632, 0.159, 1.0, 0.112, 0.027, 0.018, 0.031, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.191, 0.274, 1.0, 0.04, 0.012, 0.01, 0.023, 0.014, 0.006, 1.0, 0.016, 0.002, 0.001, 0.001], 'utility': [-0.06, -0.15, -0.115, 0.146, -0.153, 0.572, -0.106, 0.346]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.596, 0.515, 0.053, 0.023, 0.026, 0.072, 1.0, 0.602, 0.444, 0.049, 0.023, 0.025, 0.073, 1.0, 0.114, 0.009, 0.021, 0.371, 1.0, 0.028, 0.009, 0.566, 0.164, 1.0, 0.1, 0.024, 0.017, 0.03, 0.003, 0.001, 0.0, 0.001, 0.007, 1.0, 0.002, 0.319, 0.722, 1.0, 0.055, 0.018, 0.017, 0.045, 0.031, 0.012, 1.0, 0.038, 0.004, 0.002, 0.003], 'utility': [-0.031, -0.116, -0.109, 0.124, -0.137, 0.472, -0.174, 0.201]} reward=0.029 t=87
DEBUG:deepcomp.util.simulation:Step                           action=[0, 3, 5, 2, 7, 1, 6, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.525, 0.067, 0.031, 0.034, 0.093, 0.942, 0.647, 0.54, 0.056, 0.025, 0.027, 0.076, 1.0, 0.091, 0.006, 0.014, 0.196, 1.0, 0.024, 0.007, 0.707, 0.156, 1.0, 0.126, 0.029, 0.019, 0.032, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.104, 0.104, 1.0, 0.028, 0.007, 0.005, 0.011, 0.005, 0.003, 1.0, 0.006, 0.001, 0.0, 0.001], 'utility': [-0.009, -0.106, -0.122, 0.171, -0.169, 0.545, 0.004, 0.496]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.79, 0.536, 0.061, 0.028, 0.031, 0.084, 1.0, 0.624, 0.489, 0.053, 0.024, 0.026, 0.074, 1.0, 0.102, 0.007, 0.017, 0.269, 1.0, 0.026, 0.008, 0.632, 0.159, 1.0, 0.112, 0.027, 0.018, 0.031, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.191, 0.274, 1.0, 0.04, 0.012, 0.01, 0.023, 0.014, 0.006, 1.0, 0.016, 0.002, 0.001, 0.001], 'utility': [-0.06, -0.15, -0.115, 0.146, -0.153, 0.572, -0.106, 0.346]} reward=0.06 t=88
DEBUG:deepcomp.util.simulation:Step                           action=[0, 1, 3, 1, 7, 1, 2, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.4, 0.058, 0.027, 0.03, 0.08, 0.692, 0.67, 0.596, 0.06, 0.026, 0.028, 0.077, 1.0, 0.082, 0.005, 0.012, 0.144, 1.0, 0.022, 0.006, 0.792, 0.153, 1.0, 0.143, 0.033, 0.021, 0.033, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.052, 0.04, 1.0, 0.019, 0.004, 0.003, 0.005, 0.002, 0.001, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [-0.039, -0.046, -0.16, 0.199, -0.216, 0.575, 0.061, 0.785]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.525, 0.067, 0.031, 0.034, 0.093, 0.942, 0.647, 0.54, 0.056, 0.025, 0.027, 0.076, 1.0, 0.091, 0.006, 0.014, 0.196, 1.0, 0.024, 0.007, 0.707, 0.156, 1.0, 0.126, 0.029, 0.019, 0.032, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.104, 0.104, 1.0, 0.028, 0.007, 0.005, 0.011, 0.005, 0.003, 1.0, 0.006, 0.001, 0.0, 0.001], 'utility': [-0.009, -0.106, -0.122, 0.171, -0.169, 0.545, 0.004, 0.496]} reward=0.098 t=89
DEBUG:deepcomp.util.simulation:Step                           action=[0, 3, 5, 2, 0, 1, 2, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.3, 0.049, 0.024, 0.026, 0.068, 0.501, 0.693, 0.659, 0.064, 0.027, 0.029, 0.078, 1.0, 0.073, 0.005, 0.01, 0.106, 1.0, 0.02, 0.006, 0.888, 0.151, 1.0, 0.163, 0.036, 0.023, 0.035, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.026, 0.016, 1.0, 0.013, 0.002, 0.001, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.014, -0.045, -0.167, 0.228, -0.235, 0.551, 0.193, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.4, 0.058, 0.027, 0.03, 0.08, 0.692, 0.67, 0.596, 0.06, 0.026, 0.028, 0.077, 1.0, 0.082, 0.005, 0.012, 0.144, 1.0, 0.022, 0.006, 0.792, 0.153, 1.0, 0.143, 0.033, 0.021, 0.033, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.052, 0.04, 1.0, 0.019, 0.004, 0.003, 0.005, 0.002, 0.001, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [-0.039, -0.046, -0.16, 0.199, -0.216, 0.575, 0.061, 0.785]} reward=0.145 t=90
DEBUG:deepcomp.util.simulation:Step                           action=[0, 3, 4, 2, 0, 1, 2, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.222, 0.041, 0.02, 0.023, 0.057, 0.358, 0.717, 0.729, 0.068, 0.029, 0.03, 0.079, 1.0, 0.066, 0.004, 0.008, 0.08, 1.0, 0.019, 0.005, 0.996, 0.15, 1.0, 0.187, 0.04, 0.025, 0.037, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001, 0.015, 0.008, 1.0, 0.011, 0.002, 0.001, 0.001, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.105, -0.116, -0.175, 0.24, -0.273, 0.742, -0.005, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.3, 0.049, 0.024, 0.026, 0.068, 0.501, 0.693, 0.659, 0.064, 0.027, 0.029, 0.078, 1.0, 0.073, 0.005, 0.01, 0.106, 1.0, 0.02, 0.006, 0.888, 0.151, 1.0, 0.163, 0.036, 0.023, 0.035, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.026, 0.016, 1.0, 0.013, 0.002, 0.001, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.014, -0.045, -0.167, 0.228, -0.235, 0.551, 0.193, 1.0]} reward=0.189 t=91
DEBUG:deepcomp.util.simulation:Step                           action=[0, 2, 4, 4, 0, 3, 4, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.161, 0.033, 0.017, 0.019, 0.047, 0.252, 0.74, 0.807, 0.073, 0.03, 0.031, 0.081, 1.0, 0.06, 0.003, 0.007, 0.061, 1.0, 0.018, 0.005, 1.0, 0.134, 0.896, 0.193, 0.04, 0.024, 0.035, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.012, 0.006, 1.0, 0.014, 0.002, 0.001, 0.001, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.036, -0.088, -0.182, 0.271, -0.245, 0.831, 0.292, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.222, 0.041, 0.02, 0.023, 0.057, 0.358, 0.717, 0.729, 0.068, 0.029, 0.03, 0.079, 1.0, 0.066, 0.004, 0.008, 0.08, 1.0, 0.019, 0.005, 0.996, 0.15, 1.0, 0.187, 0.04, 0.025, 0.037, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001, 0.015, 0.008, 1.0, 0.011, 0.002, 0.001, 0.001, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.105, -0.116, -0.175, 0.24, -0.273, 0.742, -0.005, 1.0]} reward=0.164 t=92
DEBUG:deepcomp.util.simulation:Step                           action=[0, 2, 4, 4, 0, 3, 4, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.115, 0.027, 0.014, 0.016, 0.038, 0.174, 0.764, 0.895, 0.078, 0.032, 0.032, 0.082, 1.0, 0.055, 0.003, 0.006, 0.047, 1.0, 0.017, 0.004, 1.0, 0.12, 0.801, 0.199, 0.041, 0.023, 0.033, 0.0, 0.0, 0.0, 0.0, 0.001, 1.0, 0.0, 0.015, 0.007, 1.0, 0.026, 0.002, 0.001, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.099, -0.053, -0.19, 0.298, -0.149, 1.0, 0.229, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.161, 0.033, 0.017, 0.019, 0.047, 0.252, 0.74, 0.807, 0.073, 0.03, 0.031, 0.081, 1.0, 0.06, 0.003, 0.007, 0.061, 1.0, 0.018, 0.005, 1.0, 0.134, 0.896, 0.193, 0.04, 0.024, 0.035, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.012, 0.006, 1.0, 0.014, 0.002, 0.001, 0.001, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.036, -0.088, -0.182, 0.271, -0.245, 0.831, 0.292, 1.0]} reward=0.23 t=93
DEBUG:deepcomp.util.simulation:Step                           action=[0, 2, 4, 4, 0, 3, 4, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.08, 0.021, 0.012, 0.013, 0.03, 0.118, 0.788, 0.992, 0.083, 0.033, 0.033, 0.083, 1.0, 0.052, 0.003, 0.005, 0.038, 1.0, 0.017, 0.004, 1.0, 0.108, 0.718, 0.207, 0.041, 0.023, 0.031, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.022, 0.009, 1.0, 0.057, 0.004, 0.002, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.041, -0.009, -0.198, 0.32, -0.185, 1.0, 0.035, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.115, 0.027, 0.014, 0.016, 0.038, 0.174, 0.764, 0.895, 0.078, 0.032, 0.032, 0.082, 1.0, 0.055, 0.003, 0.006, 0.047, 1.0, 0.017, 0.004, 1.0, 0.12, 0.801, 0.199, 0.041, 0.023, 0.033, 0.0, 0.0, 0.0, 0.0, 0.001, 1.0, 0.0, 0.015, 0.007, 1.0, 0.026, 0.002, 0.001, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.099, -0.053, -0.19, 0.298, -0.149, 1.0, 0.229, 1.0]} reward=0.255 t=94
DEBUG:deepcomp.util.simulation:Step                           action=[0, 2, 4, 4, 0, 3, 4, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.055, 0.016, 0.009, 0.011, 0.023, 0.079, 0.737, 1.0, 0.081, 0.031, 0.031, 0.077, 0.908, 0.05, 0.003, 0.005, 0.032, 1.0, 0.018, 0.004, 1.0, 0.097, 0.646, 0.216, 0.042, 0.022, 0.029, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.033, 0.014, 1.0, 0.127, 0.008, 0.003, 0.004, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.056, 0.02, -0.096, 0.336, -0.132, 1.0, 0.074, 0.414]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.08, 0.021, 0.012, 0.013, 0.03, 0.118, 0.788, 0.992, 0.083, 0.033, 0.033, 0.083, 1.0, 0.052, 0.003, 0.005, 0.038, 1.0, 0.017, 0.004, 1.0, 0.108, 0.718, 0.207, 0.041, 0.023, 0.031, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.022, 0.009, 1.0, 0.057, 0.004, 0.002, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.041, -0.009, -0.198, 0.32, -0.185, 1.0, 0.035, 1.0]} reward=0.24 t=95
DEBUG:deepcomp.util.simulation:Step                           action=[0, 7, 4, 4, 0, 4, 4, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.036, 0.012, 0.007, 0.008, 0.017, 0.051, 0.682, 1.0, 0.077, 0.03, 0.029, 0.071, 0.817, 0.05, 0.003, 0.004, 0.027, 1.0, 0.019, 0.004, 1.0, 0.089, 0.583, 0.228, 0.042, 0.022, 0.028, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.048, 0.02, 1.0, 0.269, 0.013, 0.005, 0.006, 0.001, 0.001, 1.0, 0.001, 0.0, 0.0, 0.0], 'utility': [0.009, 0.09, -0.105, 0.344, -0.11, 1.0, -0.002, 0.116]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.055, 0.016, 0.009, 0.011, 0.023, 0.079, 0.737, 1.0, 0.081, 0.031, 0.031, 0.077, 0.908, 0.05, 0.003, 0.005, 0.032, 1.0, 0.018, 0.004, 1.0, 0.097, 0.646, 0.216, 0.042, 0.022, 0.029, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.033, 0.014, 1.0, 0.127, 0.008, 0.003, 0.004, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.056, 0.02, -0.096, 0.336, -0.132, 1.0, 0.074, 0.414]} reward=0.2 t=96
DEBUG:deepcomp.util.simulation:Step                           action=[0, 2, 5, 3, 6, 4, 6, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.023, 0.009, 0.006, 0.006, 0.012, 0.032, 0.631, 1.0, 0.074, 0.028, 0.027, 0.065, 0.735, 0.051, 0.003, 0.004, 0.024, 1.0, 0.021, 0.004, 1.0, 0.081, 0.529, 0.242, 0.044, 0.022, 0.027, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.067, 0.027, 1.0, 0.516, 0.022, 0.008, 0.009, 0.003, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.003, 0.167, -0.113, 0.344, -0.123, 1.0, -0.046, 0.074]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.036, 0.012, 0.007, 0.008, 0.017, 0.051, 0.682, 1.0, 0.077, 0.03, 0.029, 0.071, 0.817, 0.05, 0.003, 0.004, 0.027, 1.0, 0.019, 0.004, 1.0, 0.089, 0.583, 0.228, 0.042, 0.022, 0.028, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.048, 0.02, 1.0, 0.269, 0.013, 0.005, 0.006, 0.001, 0.001, 1.0, 0.001, 0.0, 0.0, 0.0], 'utility': [0.009, 0.09, -0.105, 0.344, -0.11, 1.0, -0.002, 0.116]} reward=0.168 t=97
DEBUG:deepcomp.util.simulation:Step                           action=[0, 0, 5, 3, 6, 4, 6, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.014, 0.006, 0.004, 0.005, 0.008, 0.019, 0.582, 1.0, 0.071, 0.026, 0.025, 0.059, 0.66, 0.054, 0.003, 0.004, 0.023, 1.0, 0.025, 0.004, 1.0, 0.075, 0.482, 0.258, 0.045, 0.022, 0.026, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012, 0.01, 0.009, 1.0, 0.005, 0.001, 0.001, 0.001], 'utility': [0.021, 0.253, -0.121, 0.337, -0.133, 0.848, -0.086, 0.159]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.023, 0.009, 0.006, 0.006, 0.012, 0.032, 0.631, 1.0, 0.074, 0.028, 0.027, 0.065, 0.735, 0.051, 0.003, 0.004, 0.024, 1.0, 0.021, 0.004, 1.0, 0.081, 0.529, 0.242, 0.044, 0.022, 0.027, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.067, 0.027, 1.0, 0.516, 0.022, 0.008, 0.009, 0.003, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.003, 0.167, -0.113, 0.344, -0.123, 1.0, -0.046, 0.074]} reward=0.163 t=98
DEBUG:deepcomp.util.simulation:Step                           action=[0, 0, 5, 3, 6, 4, 4, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.008, 0.004, 0.003, 0.003, 0.006, 0.011, 0.536, 1.0, 0.068, 0.025, 0.023, 0.054, 0.592, 0.058, 0.003, 0.004, 0.022, 1.0, 0.03, 0.005, 1.0, 0.07, 0.442, 0.278, 0.047, 0.022, 0.025, 0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012, 0.025, 0.021, 1.0, 0.011, 0.002, 0.001, 0.003], 'utility': [0.008, 0.349, -0.13, 0.322, -0.189, 0.724, -0.258, 0.122]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.014, 0.006, 0.004, 0.005, 0.008, 0.019, 0.582, 1.0, 0.071, 0.026, 0.025, 0.059, 0.66, 0.054, 0.003, 0.004, 0.023, 1.0, 0.025, 0.004, 1.0, 0.075, 0.482, 0.258, 0.045, 0.022, 0.026, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012, 0.01, 0.009, 1.0, 0.005, 0.001, 0.001, 0.001], 'utility': [0.021, 0.253, -0.121, 0.337, -0.133, 0.848, -0.086, 0.159]} reward=0.129 t=99
DEBUG:deepcomp.util.simulation:Step                           action=[0, 0, 5, 3, 4, 4, 4, 7] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.005, 0.002, 0.002, 0.002, 0.003, 0.006, 0.493, 1.0, 0.065, 0.023, 0.021, 0.049, 0.531, 0.065, 0.003, 0.005, 0.022, 1.0, 0.037, 0.006, 1.0, 0.065, 0.407, 0.301, 0.049, 0.022, 0.025, 0.004, 0.0, 0.0, 0.0, 0.003, 1.0, 0.003, 0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012, 0.055, 0.043, 1.0, 0.02, 0.004, 0.003, 0.006], 'utility': [0.012, 0.459, -0.138, 0.3, -0.127, 0.588, -0.197, 0.143]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.008, 0.004, 0.003, 0.003, 0.006, 0.011, 0.536, 1.0, 0.068, 0.025, 0.023, 0.054, 0.592, 0.058, 0.003, 0.004, 0.022, 1.0, 0.03, 0.005, 1.0, 0.07, 0.442, 0.278, 0.047, 0.022, 0.025, 0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012, 0.025, 0.021, 1.0, 0.011, 0.002, 0.001, 0.003], 'utility': [0.008, 0.349, -0.13, 0.322, -0.189, 0.724, -0.258, 0.122]} reward=0.141 t=100
INFO:deepcomp.util.simulation:Video saved                    path=/home/abhishek/cmc/result/DeepCoMP/good/videos/PPO_CentralRelNormEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-27_09-30-06.html
INFO:deepcomp.util.simulation:Gif saved                      path=/home/abhishek/cmc/result/DeepCoMP/good/videos/PPO_CentralRelNormEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-27_09-30-06.gif
DEBUG:deepcomp.util.simulation:Episode complete               avg_step_reward=0.065 eps_duration=528.921 scalar_metrics=['sum_utility'] vector_metrics=['dr', 'utility']
INFO:deepcomp.util.simulation:Scalar results                 results={'episode': [0], 'eps_duration_mean': [528.921], 'eps_duration_std': [528.921], 'step_reward_mean': [0.065], 'step_reward_std': [0.097], 'sum_utility_mean': [10.711], 'sum_utility_std': [15.56]}
INFO:deepcomp.util.simulation:Mean results                   results={'episode': 0.0, 'eps_duration_mean': 528.921, 'eps_duration_std': 528.921, 'step_reward_mean': 0.065, 'step_reward_std': 0.097, 'sum_utility_mean': 10.711, 'sum_utility_std': 15.56}
INFO:deepcomp.util.simulation:Simulation complete            avg_eps_reward=6.5 eps_length=100 num_episodes=1 step_reward_mean=0.065 step_reward_std=0.0
INFO:deepcomp.util.simulation:Starting evaluation            fast_ues=2 num_episodes=100 num_workers=1 slow_ues=5 static_ues=1
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [05:16<00:00,  3.16s/it]
INFO:deepcomp.util.simulation:Scalar results                 results={'episode': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 'eps_duration_mean': [2.647, 3.525, 3.242, 2.908, 2.806, 2.825, 2.773, 2.907, 2.962, 2.852, 2.772, 2.675, 2.878, 2.728, 3.037, 3.071, 2.794, 2.828, 2.912, 2.941, 2.995, 2.98, 6.282, 2.835, 2.851, 2.731, 2.928, 2.954, 2.8, 3.031, 5.01, 2.725, 2.868, 2.747, 2.779, 4.918, 2.578, 4.364, 2.917, 2.737, 4.916, 2.83, 2.832, 2.814, 5.25, 3.222, 2.545, 2.782, 2.894, 2.971, 5.0, 2.888, 3.725, 3.46, 3.054, 2.883, 2.877, 2.886, 2.735, 2.967, 2.948, 2.824, 2.698, 3.073, 3.093, 2.903, 4.851, 3.303, 3.084, 3.049, 3.345, 3.138, 3.286, 3.02, 3.088, 3.299, 3.161, 3.539, 3.288, 3.289, 3.117, 3.26, 3.166, 3.159, 4.847, 3.574, 2.803, 2.877, 3.032, 3.106, 2.889, 3.113, 2.542, 2.727, 2.845, 3.122, 3.107, 2.749, 2.769, 3.224], 'eps_duration_std': [2.647, 3.525, 3.242, 2.908, 2.806, 2.825, 2.773, 2.907, 2.962, 2.852, 2.772, 2.675, 2.878, 2.728, 3.037, 3.071, 2.794, 2.828, 2.912, 2.941, 2.995, 2.98, 6.282, 2.835, 2.851, 2.731, 2.928, 2.954, 2.8, 3.031, 5.01, 2.725, 2.868, 2.747, 2.779, 4.918, 2.578, 4.364, 2.917, 2.737, 4.916, 2.83, 2.832, 2.814, 5.25, 3.222, 2.545, 2.782, 2.894, 2.971, 5.0, 2.888, 3.725, 3.46, 3.054, 2.883, 2.877, 2.886, 2.735, 2.967, 2.948, 2.824, 2.698, 3.073, 3.093, 2.903, 4.851, 3.303, 3.084, 3.049, 3.345, 3.138, 3.286, 3.02, 3.088, 3.299, 3.161, 3.539, 3.288, 3.289, 3.117, 3.26, 3.166, 3.159, 4.847, 3.574, 2.803, 2.877, 3.032, 3.106, 2.889, 3.113, 2.542, 2.727, 2.845, 3.122, 3.107, 2.749, 2.769, 3.224], 'step_reward_mean': [0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065], 'step_reward_std': [0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097, 0.097], 'sum_utility_mean': [10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711, 10.711], 'sum_utility_std': [15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56, 15.56]}
INFO:deepcomp.util.simulation:Mean results                   results={'episode': 49.5, 'eps_duration_mean': 3.16, 'eps_duration_std': 3.16, 'step_reward_mean': 0.065, 'step_reward_std': 0.097, 'sum_utility_mean': 10.711, 'sum_utility_std': 15.56}
INFO:deepcomp.util.simulation:Simulation complete            avg_eps_reward=6.5 eps_length=100 num_episodes=100 step_reward_mean=0.065 step_reward_std=0.0
INFO:deepcomp.util.simulation:Writing scalar results         file=/home/abhishek/cmc/result/DeepCoMP/good/test/PPO_CentralRelNormEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-27_09-30-06.csv
INFO:deepcomp.util.simulation:Writing vector results         file=/home/abhishek/cmc/result/DeepCoMP/good/test/PPO_CentralRelNormEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-27_09-30-06_dr.pkl metric=dr
INFO:deepcomp.util.simulation:Writing vector results         file=/home/abhishek/cmc/result/DeepCoMP/good/test/PPO_CentralRelNormEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-27_09-30-06_utility.pkl metric=utility
INFO:deepcomp.main:Finished                       agent=/home/abhishek/cmc/result/DeepCoMP/good/train/PPO_2022-04-27_08-31-21/PPO_CentralRelNormEnv_50e5a_00000_0_2022-04-27_08-31-21/checkpoint_000050/checkpoint-50
abhishek@abhishek-pc:~$ 
```

