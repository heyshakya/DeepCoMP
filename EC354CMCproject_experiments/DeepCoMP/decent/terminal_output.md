```
abhishek@abhishek-pc:~$ deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent central --workers 2 --dashboard --ue-details --eval 100 --train-steps 50000 --seed 42 --video both --result-dir /home/abhishek/cmc/result/DeepCoMP/decent
2022-04-25 09:26:28,486	WARNING deprecation.py:33 -- DeprecationWarning: `monitor` has been deprecated. Use `record_env` instead. This will raise an error in the future!
== Status ==
Memory usage on this node: 3.0/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 PENDING)
+-----------------------------------+----------+-------+
| Trial name                        | status   | loc   |
|-----------------------------------+----------+-------|
| PPO_CentralRelNormEnv_af4f5_00000 | PENDING  |       |
+-----------------------------------+----------+-------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 4000
  custom_metrics:
    eps_sum_utility_max: -4604.335940579162
    eps_sum_utility_mean: -6109.31196109895
    eps_sum_utility_min: -7762.497251023287
    sum_utility_max: -9.181907918525676
    sum_utility_mean: -49.869562545094254
    sum_utility_min: -121.4704941854077
  date: 2022-04-25_09-27-25
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -29.09412394135115
  episode_reward_mean: -38.5913700235938
  episode_reward_min: -47.97170696172456
  episodes_this_iter: 40
  episodes_total: 40
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 33.45245901639345
    ram_util_percent: 50.51147540983607
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05174975940908331
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 18.119368596055516
    mean_inference_ms: 0.9286276761559711
    mean_raw_obs_processing_ms: 0.19326185000532572
  time_since_restore: 43.37806177139282
  time_this_iter_s: 43.37806177139282
  time_total_s: 43.37806177139282
  timers:
    learn_throughput: 964.473
    learn_time_ms: 4147.344
    load_throughput: 52922.801
    load_time_ms: 75.582
    sample_throughput: 102.351
    sample_time_ms: 39081.019
    update_time_ms: 3.092
  timestamp: 1650859045
  timesteps_since_restore: 0
  timesteps_total: 4000
  training_iteration: 1
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |   ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |      1 |          43.3781 | 4000 | -38.5914 |             -29.0941 |             -47.9717 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 8000
  custom_metrics:
    eps_sum_utility_max: -4490.21349807869
    eps_sum_utility_mean: -6046.177389125779
    eps_sum_utility_min: -7762.497251023287
    sum_utility_max: 18.048373540605937
    sum_utility_mean: -50.8281850702052
    sum_utility_min: -121.77710421382605
  date: 2022-04-25_09-28-11
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -28.221536917239217
  episode_reward_mean: -38.20477135250439
  episode_reward_min: -47.97170696172456
  episodes_this_iter: 40
  episodes_total: 80
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 34.68412698412698
    ram_util_percent: 50.94285714285714
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05216659130728061
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 18.345153512308165
    mean_inference_ms: 0.9306593274159477
    mean_raw_obs_processing_ms: 0.19418997816577893
  time_since_restore: 88.5896532535553
  time_this_iter_s: 45.211591482162476
  time_total_s: 88.5896532535553
  timers:
    learn_throughput: 941.824
    learn_time_ms: 4247.078
    load_throughput: 101902.43
    load_time_ms: 39.253
    sample_throughput: 100.085
    sample_time_ms: 39965.953
    update_time_ms: 3.254
  timestamp: 1650859091
  timesteps_since_restore: 0
  timesteps_total: 8000
  training_iteration: 2
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |   ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |      2 |          88.5897 | 8000 | -38.2048 |             -28.2215 |             -47.9717 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 12000
  custom_metrics:
    eps_sum_utility_max: -4290.134339859825
    eps_sum_utility_mean: -6022.762089362548
    eps_sum_utility_min: -7762.497251023287
    sum_utility_max: 18.048373540605937
    sum_utility_mean: -50.08735718761998
    sum_utility_min: -139.33231650288545
  date: 2022-04-25_09-28-57
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -27.746623392821036
  episode_reward_mean: -38.00493759322123
  episode_reward_min: -47.730309941700966
  episodes_this_iter: 40
  episodes_total: 120
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 34.24090909090909
    ram_util_percent: 50.919696969696965
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05248273958563306
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 18.632822244656815
    mean_inference_ms: 0.9325674391311007
    mean_raw_obs_processing_ms: 0.19524339533089197
  time_since_restore: 135.19537782669067
  time_this_iter_s: 46.605724573135376
  time_total_s: 135.19537782669067
  timers:
    learn_throughput: 949.904
    learn_time_ms: 4210.953
    load_throughput: 145266.085
    load_time_ms: 27.536
    sample_throughput: 98.059
    sample_time_ms: 40791.942
    update_time_ms: 3.206
  timestamp: 1650859137
  timesteps_since_restore: 0
  timesteps_total: 12000
  training_iteration: 3
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |      3 |          135.195 | 12000 | -38.0049 |             -27.7466 |             -47.7303 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 16000
  custom_metrics:
    eps_sum_utility_max: -4290.134339859825
    eps_sum_utility_mean: -5947.924445013126
    eps_sum_utility_min: -7527.481093640159
    sum_utility_max: 27.044947135067307
    sum_utility_mean: -45.601533552617255
    sum_utility_min: -139.33231650288545
  date: 2022-04-25_09-29-48
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -27.746623392821036
  episode_reward_mean: -37.59524751602417
  episode_reward_min: -46.85767841583622
  episodes_this_iter: 40
  episodes_total: 160
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 34.380281690140855
    ram_util_percent: 50.8605633802817
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05329756993552012
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 19.13203619896952
    mean_inference_ms: 0.9423083221135343
    mean_raw_obs_processing_ms: 0.19895082618765458
  time_since_restore: 186.3035180568695
  time_this_iter_s: 51.10814023017883
  time_total_s: 186.3035180568695
  timers:
    learn_throughput: 944.673
    learn_time_ms: 4234.268
    load_throughput: 184910.599
    load_time_ms: 21.632
    sample_throughput: 94.582
    sample_time_ms: 42291.166
    update_time_ms: 3.206
  timestamp: 1650859188
  timesteps_since_restore: 0
  timesteps_total: 16000
  training_iteration: 4
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |      4 |          186.304 | 16000 | -37.5952 |             -27.7466 |             -46.8577 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 20000
  custom_metrics:
    eps_sum_utility_max: -3525.8803680993356
    eps_sum_utility_mean: -5678.439248099426
    eps_sum_utility_min: -7527.481093640159
    sum_utility_max: 27.044947135067307
    sum_utility_mean: -45.685020554966016
    sum_utility_min: -127.85742259278885
  date: 2022-04-25_09-30-39
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -22.807167422100846
  episode_reward_mean: -35.955693338912745
  episode_reward_min: -46.85767841583622
  episodes_this_iter: 40
  episodes_total: 200
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 35.330000000000005
    ram_util_percent: 51.012857142857136
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05408358021835714
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 19.62552189548618
    mean_inference_ms: 0.9537546315150709
    mean_raw_obs_processing_ms: 0.20259774508426645
  time_since_restore: 236.58793425559998
  time_this_iter_s: 50.28441619873047
  time_total_s: 236.58793425559998
  timers:
    learn_throughput: 945.644
    learn_time_ms: 4229.921
    load_throughput: 222827.483
    load_time_ms: 17.951
    sample_throughput: 92.927
    sample_time_ms: 43044.362
    update_time_ms: 3.214
  timestamp: 1650859239
  timesteps_since_restore: 0
  timesteps_total: 20000
  training_iteration: 5
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |      5 |          236.588 | 20000 | -35.9557 |             -22.8072 |             -46.8577 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 24000
  custom_metrics:
    eps_sum_utility_max: -3525.8803680993356
    eps_sum_utility_mean: -5374.986407163066
    eps_sum_utility_min: -7182.285293717688
    sum_utility_max: 27.044947135067307
    sum_utility_mean: -42.427919339992684
    sum_utility_min: -122.5310128244098
  date: 2022-04-25_09-31-31
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -22.807167422100846
  episode_reward_mean: -34.03758972287803
  episode_reward_min: -45.13783105625884
  episodes_this_iter: 40
  episodes_total: 240
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 33.553424657534244
    ram_util_percent: 51.01917808219178
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05469522284972765
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 20.045083879273378
    mean_inference_ms: 0.9628995363137838
    mean_raw_obs_processing_ms: 0.20533377966345262
  time_since_restore: 289.1371388435364
  time_this_iter_s: 52.5492045879364
  time_total_s: 289.1371388435364
  timers:
    learn_throughput: 940.277
    learn_time_ms: 4254.066
    load_throughput: 258220.262
    load_time_ms: 15.491
    sample_throughput: 91.122
    sample_time_ms: 43896.961
    update_time_ms: 3.184
  timestamp: 1650859291
  timesteps_since_restore: 0
  timesteps_total: 24000
  training_iteration: 6
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |      6 |          289.137 | 24000 | -34.0376 |             -22.8072 |             -45.1378 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 28000
  custom_metrics:
    eps_sum_utility_max: -3553.4499788208873
    eps_sum_utility_mean: -5058.310392665019
    eps_sum_utility_min: -6296.691906440198
    sum_utility_max: 20.724260772592242
    sum_utility_mean: -38.52593985180344
    sum_utility_min: -121.12441426618442
  date: 2022-04-25_09-32-24
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -22.739649466716894
  episode_reward_mean: -32.05034395716557
  episode_reward_min: -40.05932677286126
  episodes_this_iter: 40
  episodes_total: 280
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 34.41486486486487
    ram_util_percent: 51.04324324324324
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05509945579861822
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 20.390556199031256
    mean_inference_ms: 0.9689690333632563
    mean_raw_obs_processing_ms: 0.20696754332368908
  time_since_restore: 341.9469609260559
  time_this_iter_s: 52.80982208251953
  time_total_s: 341.9469609260559
  timers:
    learn_throughput: 925.687
    learn_time_ms: 4321.115
    load_throughput: 286013.346
    load_time_ms: 13.985
    sample_throughput: 89.902
    sample_time_ms: 44493.039
    update_time_ms: 3.193
  timestamp: 1650859344
  timesteps_since_restore: 0
  timesteps_total: 28000
  training_iteration: 7
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |      7 |          341.947 | 28000 | -32.0503 |             -22.7396 |             -40.0593 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 32000
  custom_metrics:
    eps_sum_utility_max: -3036.901290114757
    eps_sum_utility_mean: -4823.33805622884
    eps_sum_utility_min: -6247.5722136338245
    sum_utility_max: 20.724260772592242
    sum_utility_mean: -39.30827758502975
    sum_utility_min: -121.12441426618442
  date: 2022-04-25_09-33-20
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -19.590843641164227
  episode_reward_mean: -30.65474825519207
  episode_reward_min: -39.087509598061054
  episodes_this_iter: 40
  episodes_total: 320
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 35.79740259740259
    ram_util_percent: 51.0961038961039
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05552746516605886
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 20.730550994527377
    mean_inference_ms: 0.97540696029406
    mean_raw_obs_processing_ms: 0.2083904811063173
  time_since_restore: 397.40514373779297
  time_this_iter_s: 55.45818281173706
  time_total_s: 397.40514373779297
  timers:
    learn_throughput: 909.04
    learn_time_ms: 4400.249
    load_throughput: 314519.479
    load_time_ms: 12.718
    sample_throughput: 88.413
    sample_time_ms: 45242.415
    update_time_ms: 3.216
  timestamp: 1650859400
  timesteps_since_restore: 0
  timesteps_total: 32000
  training_iteration: 8
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |      8 |          397.405 | 32000 | -30.6547 |             -19.5908 |             -39.0875 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 36000
  custom_metrics:
    eps_sum_utility_max: -2976.308701976648
    eps_sum_utility_mean: -4481.553036259203
    eps_sum_utility_min: -6127.286473506822
    sum_utility_max: 26.512455382135805
    sum_utility_mean: -33.675136954818576
    sum_utility_min: -101.73664390536783
  date: 2022-04-25_09-34-17
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -18.488671259703253
  episode_reward_mean: -28.5291993940564
  episode_reward_min: -38.49904696523823
  episodes_this_iter: 40
  episodes_total: 360
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 35.4375
    ram_util_percent: 51.02375000000001
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.056006929817914275
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 21.105782967189967
    mean_inference_ms: 0.98300525577122
    mean_raw_obs_processing_ms: 0.20994166865737462
  time_since_restore: 454.7500829696655
  time_this_iter_s: 57.34493923187256
  time_total_s: 454.7500829696655
  timers:
    learn_throughput: 904.123
    learn_time_ms: 4424.177
    load_throughput: 339627.396
    load_time_ms: 11.778
    sample_throughput: 86.82
    sample_time_ms: 46072.548
    update_time_ms: 3.208
  timestamp: 1650859457
  timesteps_since_restore: 0
  timesteps_total: 36000
  training_iteration: 9
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |      9 |           454.75 | 36000 | -28.5292 |             -18.4887 |              -38.499 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 40000
  custom_metrics:
    eps_sum_utility_max: -2907.995749155958
    eps_sum_utility_mean: -4287.434288569881
    eps_sum_utility_min: -6087.808995167782
    sum_utility_max: 26.512455382135805
    sum_utility_mean: -28.673396182754665
    sum_utility_min: -98.21591571461653
  date: 2022-04-25_09-35-13
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -18.488671259703253
  episode_reward_mean: -27.304824511375635
  episode_reward_min: -38.64328310550956
  episodes_this_iter: 40
  episodes_total: 400
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 34.39871794871796
    ram_util_percent: 51.162820512820524
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.056402035752717836
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 21.446421240665178
    mean_inference_ms: 0.9893291347496553
    mean_raw_obs_processing_ms: 0.2113384491809969
  time_since_restore: 510.77867889404297
  time_this_iter_s: 56.02859592437744
  time_total_s: 510.77867889404297
  timers:
    learn_throughput: 898.549
    learn_time_ms: 4451.621
    load_throughput: 366563.671
    load_time_ms: 10.912
    sample_throughput: 85.843
    sample_time_ms: 46596.803
    update_time_ms: 3.217
  timestamp: 1650859513
  timesteps_since_restore: 0
  timesteps_total: 40000
  training_iteration: 10
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |     10 |          510.779 | 40000 | -27.3048 |             -18.4887 |             -38.6433 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 44000
  custom_metrics:
    eps_sum_utility_max: -2723.8386096921636
    eps_sum_utility_mean: -4080.7599527664906
    eps_sum_utility_min: -6087.808995167782
    sum_utility_max: 26.512455382135805
    sum_utility_mean: -24.701286972986917
    sum_utility_min: -99.59107647667797
  date: 2022-04-25_09-36-18
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -18.05124686666383
  episode_reward_mean: -26.035504203193142
  episode_reward_min: -38.64328310550956
  episodes_this_iter: 40
  episodes_total: 440
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 38.16
    ram_util_percent: 51.15666666666666
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05695525757937716
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 21.857870690541958
    mean_inference_ms: 0.9982379297637999
    mean_raw_obs_processing_ms: 0.21374117561452877
  time_since_restore: 575.4136393070221
  time_this_iter_s: 64.63496041297913
  time_total_s: 575.4136393070221
  timers:
    learn_throughput: 883.198
    learn_time_ms: 4528.998
    load_throughput: 1056020.948
    load_time_ms: 3.788
    sample_throughput: 82.206
    sample_time_ms: 48658.291
    update_time_ms: 3.258
  timestamp: 1650859578
  timesteps_since_restore: 0
  timesteps_total: 44000
  training_iteration: 11
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |     11 |          575.414 | 44000 | -26.0355 |             -18.0512 |             -38.6433 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 48000
  custom_metrics:
    eps_sum_utility_max: -2643.13014285753
    eps_sum_utility_mean: -4013.79054165927
    eps_sum_utility_min: -6087.808995167782
    sum_utility_max: 21.672168605007016
    sum_utility_mean: -25.9684256655042
    sum_utility_min: -99.59107647667797
  date: 2022-04-25_09-37-24
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -17.37398097051279
  episode_reward_mean: -25.622710915296455
  episode_reward_min: -38.64328310550956
  episodes_this_iter: 40
  episodes_total: 480
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 40.60434782608696
    ram_util_percent: 51.160869565217396
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05770950911639189
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 22.34358354762614
    mean_inference_ms: 1.0102230580829945
    mean_raw_obs_processing_ms: 0.21690868303126598
  time_since_restore: 641.6305541992188
  time_this_iter_s: 66.21691489219666
  time_total_s: 641.6305541992188
  timers:
    learn_throughput: 870.212
    learn_time_ms: 4596.58
    load_throughput: 995840.046
    load_time_ms: 4.017
    sample_throughput: 78.91
    sample_time_ms: 50690.844
    update_time_ms: 3.234
  timestamp: 1650859644
  timesteps_since_restore: 0
  timesteps_total: 48000
  training_iteration: 12
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |     12 |          641.631 | 48000 | -25.6227 |              -17.374 |             -38.6433 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_CentralRelNormEnv_af4f5_00000:
  agent_timesteps_total: 52000
  custom_metrics:
    eps_sum_utility_max: -2352.7273072619173
    eps_sum_utility_mean: -3677.022759327488
    eps_sum_utility_min: -5230.752837276721
    sum_utility_max: 29.06025910750276
    sum_utility_mean: -25.549301519067022
    sum_utility_min: -99.59107647667797
  date: 2022-04-25_09-38-30
  done: true
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -14.669778544223696
  episode_reward_mean: -23.54080166133867
  episode_reward_min: -32.88922217337305
  episodes_this_iter: 40
  episodes_total: 520
  experiment_id: 7d7be16a615d46108812a29e7c4d838c
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
    cpu_util_percent: 38.386813186813185
    ram_util_percent: 51.31538461538462
  pid: 10454
  policy_reward_max: {}
  policy_reward_mean: {}
  policy_reward_min: {}
  sampler_perf:
    mean_action_processing_ms: 0.05848939530208485
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 22.84630506010396
    mean_inference_ms: 1.0228105689195088
    mean_raw_obs_processing_ms: 0.21995478309633576
  time_since_restore: 707.2296853065491
  time_this_iter_s: 65.59913110733032
  time_total_s: 707.2296853065491
  timers:
    learn_throughput: 851.44
    learn_time_ms: 4697.924
    load_throughput: 1003026.078
    load_time_ms: 3.988
    sample_throughput: 76.206
    sample_time_ms: 52489.608
    update_time_ms: 3.241
  timestamp: 1650859710
  timesteps_since_restore: 0
  timesteps_total: 52000
  training_iteration: 13
  trial_id: af4f5_00000
  
== Status ==
Memory usage on this node: 3.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 RUNNING)
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status   | loc              |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | RUNNING  | 10.0.3.106:10454 |     13 |           707.23 | 52000 | -23.5408 |             -14.6698 |             -32.8892 |                100 |
+-----------------------------------+----------+------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/3.37 GiB heap, 0.0/1.69 GiB objects
Result logdir: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28
Number of trials: 1/1 (1 TERMINATED)
+-----------------------------------+------------+-------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                        | status     | loc   |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-----------------------------------+------------+-------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_CentralRelNormEnv_af4f5_00000 | TERMINATED |       |     13 |           707.23 | 52000 | -23.5408 |             -14.6698 |             -32.8892 |                100 |
+-----------------------------------+------------+-------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


2022-04-25 09:38:30,910	INFO tune.py:549 -- Total run time: 722.47 seconds (722.22 seconds for the tuning loop).
INFO:deepcomp.util.simulation:Training done                  episode_reward_mean=-23.541 episodes_total=520 log_dir=/home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28/PPO_CentralRelNormEnv_af4f5_00000_0_2022-04-25_09-26-28 num_steps_sampled=52000 num_steps_trained=52000 timesteps_total=52000
2022-04-25 09:38:30,981	INFO trainer.py:671 -- Tip: set framework=tfe or the --eager flag to enable TensorFlow eager execution
2022-04-25 09:38:30,981	WARNING deprecation.py:33 -- DeprecationWarning: `monitor` has been deprecated. Use `record_env` instead. This will raise an error in the future!
2022-04-25 09:38:30,981	INFO trainer.py:696 -- Current log_level is ERROR. For more information, set 'log_level': 'INFO' / 'DEBUG' or use the -v and -vv flags.
2022-04-25 09:38:43,912	INFO trainable.py:101 -- Trainable.setup took 12.942 seconds. If your trainable is slow to initialize, consider setting reuse_actors=True to reduce actor creation overheads.
INFO:deepcomp.util.simulation:Loading PPO agent              checkpoint=/home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28/PPO_CentralRelNormEnv_af4f5_00000_0_2022-04-25_09-26-28/checkpoint_000013/checkpoint-13
2022-04-25 09:38:44,093	INFO trainable.py:377 -- Restored on 10.0.3.106 from checkpoint: /home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28/PPO_CentralRelNormEnv_af4f5_00000_0_2022-04-25_09-26-28/checkpoint_000013/checkpoint-13
2022-04-25 09:38:44,094	INFO trainable.py:385 -- Current state after restoring: {'_iteration': 13, '_timesteps_total': None, '_time_total': 707.2296853065491, '_episodes_total': 520}
INFO:deepcomp.util.simulation:Agent loaded                   agent=PPO checkpoint=None rllib_dir=/home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28/PPO_CentralRelNormEnv_af4f5_00000_0_2022-04-25_09-26-28/checkpoint_000013/checkpoint-13
INFO:deepcomp.util.simulation:Loaded training progress       progress_file=/home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28/PPO_CentralRelNormEnv_af4f5_00000_0_2022-04-25_09-26-28/progress.csv train_iteration=13 train_steps=52000
WARNING:deepcomp.util.simulation:Evaluating with a single worker for reproducibility and compatibility.
INFO:deepcomp.util.simulation:Starting evaluation            fast_ues=2 num_episodes=1 num_workers=1 slow_ues=5 static_ues=1
DEBUG:deepcomp.util.simulation:Step                           action=[6, 6, 2, 2, 3, 1, 1, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 0.048, 1.0, 0.01, 0.002, 0.002, 0.004, 0.021, 1.0, 0.008, 0.002, 0.002, 0.004, 0.04, 0.006, 0.001, 0.001, 0.001, 0.003, 1.0, 0.011, 0.036, 0.016, 1.0, 0.025, 0.004, 0.002, 0.003, 1.0, 0.03, 0.071, 0.584, 0.654, 0.076, 0.031, 1.0, 0.007, 0.004, 0.004, 0.008, 0.016, 0.016, 0.028, 0.009, 0.077, 1.0, 0.025, 0.006, 0.005], 'utility': [0.126, -1.0, 0.372, -1.0, 0.38, -0.236, 0.348, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.014, 0.044, 1.0, 0.01, 0.002, 0.002, 0.004, 0.018, 1.0, 0.008, 0.002, 0.002, 0.003, 0.035, 0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.014, 0.039, 0.016, 1.0, 0.029, 0.004, 0.002, 0.003, 1.0, 0.034, 0.083, 0.787, 0.714, 0.079, 0.033, 1.0, 0.013, 0.007, 0.009, 0.02, 0.055, 0.04, 0.031, 0.011, 0.081, 1.0, 0.029, 0.007, 0.005], 'utility': [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]} reward=-0.278 t=1
DEBUG:deepcomp.util.simulation:Step                           action=[3, 0, 2, 6, 1, 5, 3, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.016, 0.053, 1.0, 0.01, 0.003, 0.002, 0.004, 0.024, 1.0, 0.009, 0.002, 0.002, 0.004, 0.046, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.009, 0.034, 0.016, 1.0, 0.021, 0.003, 0.002, 0.003, 1.0, 0.027, 0.06, 0.438, 0.595, 0.073, 0.029, 1.0, 0.003, 0.002, 0.002, 0.002, 0.004, 0.005, 0.026, 0.008, 0.075, 1.0, 0.021, 0.005, 0.004], 'utility': [0.101, -1.0, -1.0, 0.134, 0.394, -0.038, 0.566, 0.002]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 0.048, 1.0, 0.01, 0.002, 0.002, 0.004, 0.021, 1.0, 0.008, 0.002, 0.002, 0.004, 0.04, 0.006, 0.001, 0.001, 0.001, 0.003, 1.0, 0.011, 0.036, 0.016, 1.0, 0.025, 0.004, 0.002, 0.003, 1.0, 0.03, 0.071, 0.584, 0.654, 0.076, 0.031, 1.0, 0.007, 0.004, 0.004, 0.008, 0.016, 0.016, 0.028, 0.009, 0.077, 1.0, 0.025, 0.006, 0.005], 'utility': [0.126, -1.0, 0.372, -1.0, 0.38, -0.236, 0.348, -1.0]} reward=-0.223 t=2
DEBUG:deepcomp.util.simulation:Step                           action=[3, 2, 2, 7, 6, 0, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.017, 0.059, 1.0, 0.011, 0.003, 0.002, 0.005, 0.027, 1.0, 0.01, 0.003, 0.002, 0.004, 0.053, 0.004, 0.001, 0.0, 0.001, 0.003, 1.0, 0.008, 0.033, 0.016, 1.0, 0.019, 0.003, 0.002, 0.003, 1.0, 0.025, 0.052, 0.331, 0.538, 0.07, 0.027, 1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002, 0.024, 0.008, 0.074, 1.0, 0.018, 0.005, 0.004], 'utility': [-0.284, -1.0, 0.328, 0.619, 0.404, -0.022, 0.747, 0.04]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.016, 0.053, 1.0, 0.01, 0.003, 0.002, 0.004, 0.024, 1.0, 0.009, 0.002, 0.002, 0.004, 0.046, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.009, 0.034, 0.016, 1.0, 0.021, 0.003, 0.002, 0.003, 1.0, 0.027, 0.06, 0.438, 0.595, 0.073, 0.029, 1.0, 0.003, 0.002, 0.002, 0.002, 0.004, 0.005, 0.026, 0.008, 0.075, 1.0, 0.021, 0.005, 0.004], 'utility': [0.101, -1.0, -1.0, 0.134, 0.394, -0.038, 0.566, 0.002]} reward=0.064 t=3
DEBUG:deepcomp.util.simulation:Step                           action=[3, 2, 4, 7, 6, 4, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.019, 0.067, 1.0, 0.011, 0.003, 0.002, 0.005, 0.031, 1.0, 0.011, 0.003, 0.002, 0.005, 0.061, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007, 0.032, 0.017, 1.0, 0.017, 0.003, 0.002, 0.003, 1.0, 0.022, 0.044, 0.253, 0.485, 0.068, 0.026, 1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002, 0.023, 0.007, 0.076, 1.0, 0.016, 0.004, 0.003], 'utility': [0.065, -1.0, 0.306, 0.38, 0.41, -0.007, 0.727, 0.072]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.017, 0.059, 1.0, 0.011, 0.003, 0.002, 0.005, 0.027, 1.0, 0.01, 0.003, 0.002, 0.004, 0.053, 0.004, 0.001, 0.0, 0.001, 0.003, 1.0, 0.008, 0.033, 0.016, 1.0, 0.019, 0.003, 0.002, 0.003, 1.0, 0.025, 0.052, 0.331, 0.538, 0.07, 0.027, 1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002, 0.024, 0.008, 0.074, 1.0, 0.018, 0.005, 0.004], 'utility': [-0.284, -1.0, 0.328, 0.619, 0.404, -0.022, 0.747, 0.04]} reward=0.089 t=4
DEBUG:deepcomp.util.simulation:Step                           action=[3, 2, 4, 7, 6, 4, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.02, 0.077, 1.0, 0.012, 0.003, 0.002, 0.006, 0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.07, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.006, 0.031, 0.018, 1.0, 0.016, 0.003, 0.002, 0.003, 1.0, 0.02, 0.038, 0.196, 0.435, 0.067, 0.024, 1.0, 0.007, 0.004, 0.003, 0.002, 0.002, 0.004, 0.023, 0.007, 0.082, 1.0, 0.015, 0.004, 0.003], 'utility': [-0.16, -1.0, 0.285, 0.642, 0.412, 0.007, 0.531, 0.096]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.019, 0.067, 1.0, 0.011, 0.003, 0.002, 0.005, 0.031, 1.0, 0.011, 0.003, 0.002, 0.005, 0.061, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007, 0.032, 0.017, 1.0, 0.017, 0.003, 0.002, 0.003, 1.0, 0.022, 0.044, 0.253, 0.485, 0.068, 0.026, 1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002, 0.023, 0.007, 0.076, 1.0, 0.016, 0.004, 0.003], 'utility': [0.065, -1.0, 0.306, 0.38, 0.41, -0.007, 0.727, 0.072]} reward=0.119 t=5
DEBUG:deepcomp.util.simulation:Step                           action=[3, 2, 4, 7, 6, 4, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.023, 0.089, 1.0, 0.012, 0.003, 0.003, 0.006, 0.04, 1.0, 0.013, 0.004, 0.003, 0.006, 0.08, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.031, 0.02, 1.0, 0.015, 0.003, 0.002, 0.003, 1.0, 0.019, 0.033, 0.153, 0.389, 0.066, 0.023, 1.0, 0.022, 0.016, 0.007, 0.004, 0.005, 0.01, 0.024, 0.008, 0.093, 1.0, 0.014, 0.004, 0.003], 'utility': [0.039, -1.0, 0.265, 0.484, 0.409, 0.02, 0.315, 0.109]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.02, 0.077, 1.0, 0.012, 0.003, 0.002, 0.006, 0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.07, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.006, 0.031, 0.018, 1.0, 0.016, 0.003, 0.002, 0.003, 1.0, 0.02, 0.038, 0.196, 0.435, 0.067, 0.024, 1.0, 0.007, 0.004, 0.003, 0.002, 0.002, 0.004, 0.023, 0.007, 0.082, 1.0, 0.015, 0.004, 0.003], 'utility': [-0.16, -1.0, 0.285, 0.642, 0.412, 0.007, 0.531, 0.096]} reward=0.102 t=6
DEBUG:deepcomp.util.simulation:Step                           action=[3, 2, 4, 7, 6, 4, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.025, 0.104, 1.0, 0.013, 0.004, 0.003, 0.007, 0.045, 1.0, 0.014, 0.004, 0.003, 0.007, 0.092, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.032, 0.022, 1.0, 0.014, 0.003, 0.002, 0.003, 1.0, 0.017, 0.028, 0.122, 0.349, 0.066, 0.023, 1.0, 0.062, 0.052, 0.017, 0.009, 0.009, 0.019, 0.027, 0.008, 0.113, 1.0, 0.015, 0.004, 0.004], 'utility': [-0.099, -1.0, 0.245, 0.637, 0.403, 0.031, 0.13, 0.111]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.023, 0.089, 1.0, 0.012, 0.003, 0.003, 0.006, 0.04, 1.0, 0.013, 0.004, 0.003, 0.006, 0.08, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.031, 0.02, 1.0, 0.015, 0.003, 0.002, 0.003, 1.0, 0.019, 0.033, 0.153, 0.389, 0.066, 0.023, 1.0, 0.022, 0.016, 0.007, 0.004, 0.005, 0.01, 0.024, 0.008, 0.093, 1.0, 0.014, 0.004, 0.003], 'utility': [0.039, -1.0, 0.265, 0.484, 0.409, 0.02, 0.315, 0.109]} reward=0.08 t=7
DEBUG:deepcomp.util.simulation:Step                           action=[3, 2, 4, 7, 6, 4, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.028, 0.123, 1.0, 0.014, 0.004, 0.003, 0.008, 0.051, 1.0, 0.016, 0.004, 0.004, 0.008, 0.105, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.033, 0.025, 1.0, 0.014, 0.003, 0.002, 0.003, 1.0, 0.016, 0.025, 0.098, 0.314, 0.067, 0.022, 1.0, 0.149, 0.15, 0.036, 0.016, 0.015, 0.033, 0.032, 0.01, 0.146, 1.0, 0.016, 0.004, 0.004], 'utility': [0.022, -1.0, 0.225, 0.517, 0.393, 0.041, -0.025, 0.102]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.025, 0.104, 1.0, 0.013, 0.004, 0.003, 0.007, 0.045, 1.0, 0.014, 0.004, 0.003, 0.007, 0.092, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.032, 0.022, 1.0, 0.014, 0.003, 0.002, 0.003, 1.0, 0.017, 0.028, 0.122, 0.349, 0.066, 0.023, 1.0, 0.062, 0.052, 0.017, 0.009, 0.009, 0.019, 0.027, 0.008, 0.113, 1.0, 0.015, 0.004, 0.004], 'utility': [-0.099, -1.0, 0.245, 0.637, 0.403, 0.031, 0.13, 0.111]} reward=0.057 t=8
DEBUG:deepcomp.util.simulation:Step                           action=[3, 2, 0, 7, 6, 0, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.032, 0.147, 1.0, 0.015, 0.004, 0.004, 0.009, 0.057, 1.0, 0.017, 0.005, 0.004, 0.009, 0.119, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005, 0.034, 0.029, 1.0, 0.014, 0.003, 0.002, 0.004, 1.0, 0.015, 0.022, 0.081, 0.283, 0.069, 0.022, 1.0, 0.31, 0.401, 0.064, 0.025, 0.022, 0.05, 0.039, 0.012, 0.201, 1.0, 0.017, 0.005, 0.005], 'utility': [-0.063, -1.0, 0.206, 0.597, 0.379, 0.049, -0.155, 0.082]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.028, 0.123, 1.0, 0.014, 0.004, 0.003, 0.008, 0.051, 1.0, 0.016, 0.004, 0.004, 0.008, 0.105, 0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005, 0.033, 0.025, 1.0, 0.014, 0.003, 0.002, 0.003, 1.0, 0.016, 0.025, 0.098, 0.314, 0.067, 0.022, 1.0, 0.149, 0.15, 0.036, 0.016, 0.015, 0.033, 0.032, 0.01, 0.146, 1.0, 0.016, 0.004, 0.004], 'utility': [0.022, -1.0, 0.225, 0.517, 0.393, 0.041, -0.025, 0.102]} reward=0.034 t=9
DEBUG:deepcomp.util.simulation:Step                           action=[3, 2, 0, 7, 6, 4, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.036, 0.176, 1.0, 0.017, 0.005, 0.004, 0.01, 0.064, 1.0, 0.019, 0.005, 0.005, 0.01, 0.136, 0.006, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005, 0.036, 0.034, 1.0, 0.014, 0.003, 0.002, 0.004, 1.0, 0.015, 0.02, 0.068, 0.258, 0.073, 0.022, 0.986, 0.559, 1.0, 0.103, 0.035, 0.031, 0.07, 0.05, 0.015, 0.291, 1.0, 0.02, 0.006, 0.006], 'utility': [0.011, -0.291, -0.291, 0.499, 0.361, 0.054, -0.268, 0.053]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.032, 0.147, 1.0, 0.015, 0.004, 0.004, 0.009, 0.057, 1.0, 0.017, 0.005, 0.004, 0.009, 0.119, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005, 0.034, 0.029, 1.0, 0.014, 0.003, 0.002, 0.004, 1.0, 0.015, 0.022, 0.081, 0.283, 0.069, 0.022, 1.0, 0.31, 0.401, 0.064, 0.025, 0.022, 0.05, 0.039, 0.012, 0.201, 1.0, 0.017, 0.005, 0.005], 'utility': [-0.063, -1.0, 0.206, 0.597, 0.379, 0.049, -0.155, 0.082]} reward=0.034 t=10
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 7, 7, 6, 0, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 0.213, 1.0, 0.018, 0.005, 0.005, 0.011, 0.072, 1.0, 0.02, 0.006, 0.005, 0.011, 0.154, 0.007, 0.001, 0.0, 0.001, 0.004, 1.0, 0.006, 0.039, 0.04, 1.0, 0.014, 0.003, 0.002, 0.005, 1.0, 0.014, 0.019, 0.058, 0.237, 0.078, 0.023, 0.402, 0.371, 1.0, 0.063, 0.019, 0.017, 0.038, 0.067, 0.02, 0.442, 1.0, 0.023, 0.008, 0.007], 'utility': [-0.042, -0.274, -0.105, 0.528, 0.342, 0.057, -0.366, 0.017]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.036, 0.176, 1.0, 0.017, 0.005, 0.004, 0.01, 0.064, 1.0, 0.019, 0.005, 0.005, 0.01, 0.136, 0.006, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005, 0.036, 0.034, 1.0, 0.014, 0.003, 0.002, 0.004, 1.0, 0.015, 0.02, 0.068, 0.258, 0.073, 0.022, 0.986, 0.559, 1.0, 0.103, 0.035, 0.031, 0.07, 0.05, 0.015, 0.291, 1.0, 0.02, 0.006, 0.006], 'utility': [0.011, -0.291, -0.291, 0.499, 0.361, 0.054, -0.268, 0.053]} reward=0.038 t=11
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 4, 6, 0, 7, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.047, 0.259, 1.0, 0.02, 0.006, 0.005, 0.013, 0.08, 1.0, 0.022, 0.006, 0.006, 0.013, 0.174, 0.008, 0.001, 0.001, 0.001, 0.005, 1.0, 0.007, 0.042, 0.048, 1.0, 0.015, 0.003, 0.003, 0.005, 1.0, 0.014, 0.018, 0.051, 0.221, 0.086, 0.024, 0.167, 0.227, 1.0, 0.037, 0.011, 0.009, 0.02, 0.091, 0.027, 0.695, 1.0, 0.028, 0.009, 0.009], 'utility': [0.003, -0.257, -0.092, 0.445, 0.319, 0.171, -1.0, -0.024]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 0.213, 1.0, 0.018, 0.005, 0.005, 0.011, 0.072, 1.0, 0.02, 0.006, 0.005, 0.011, 0.154, 0.007, 0.001, 0.0, 0.001, 0.004, 1.0, 0.006, 0.039, 0.04, 1.0, 0.014, 0.003, 0.002, 0.005, 1.0, 0.014, 0.019, 0.058, 0.237, 0.078, 0.023, 0.402, 0.371, 1.0, 0.063, 0.019, 0.017, 0.038, 0.067, 0.02, 0.442, 1.0, 0.023, 0.008, 0.007], 'utility': [-0.042, -0.274, -0.105, 0.528, 0.342, 0.057, -0.366, 0.017]} reward=0.02 t=12
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 0, 4, 6, 0, 7, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.054, 0.317, 1.0, 0.021, 0.006, 0.006, 0.015, 0.089, 1.0, 0.023, 0.007, 0.006, 0.014, 0.198, 0.011, 0.001, 0.001, 0.001, 0.006, 1.0, 0.008, 0.046, 0.059, 1.0, 0.016, 0.004, 0.003, 0.006, 1.0, 0.014, 0.017, 0.046, 0.209, 0.097, 0.026, 0.072, 0.131, 1.0, 0.021, 0.006, 0.005, 0.01, 0.112, 0.033, 1.0, 0.89, 0.031, 0.011, 0.011], 'utility': [-0.029, -0.241, -0.08, 0.443, 0.295, 0.169, -1.0, -0.068]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.047, 0.259, 1.0, 0.02, 0.006, 0.005, 0.013, 0.08, 1.0, 0.022, 0.006, 0.006, 0.013, 0.174, 0.008, 0.001, 0.001, 0.001, 0.005, 1.0, 0.007, 0.042, 0.048, 1.0, 0.015, 0.003, 0.003, 0.005, 1.0, 0.014, 0.018, 0.051, 0.221, 0.086, 0.024, 0.167, 0.227, 1.0, 0.037, 0.011, 0.009, 0.02, 0.091, 0.027, 0.695, 1.0, 0.028, 0.009, 0.009], 'utility': [0.003, -0.257, -0.092, 0.445, 0.319, 0.171, -1.0, -0.024]} reward=-0.054 t=13
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 0, 4, 6, 0, 7, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.061, 0.39, 1.0, 0.023, 0.007, 0.007, 0.017, 0.1, 1.0, 0.025, 0.008, 0.007, 0.016, 0.223, 0.014, 0.001, 0.001, 0.001, 0.008, 1.0, 0.009, 0.05, 0.072, 1.0, 0.017, 0.004, 0.003, 0.007, 1.0, 0.015, 0.016, 0.043, 0.2, 0.112, 0.028, 0.034, 0.075, 1.0, 0.012, 0.003, 0.003, 0.006, 0.094, 0.028, 1.0, 0.539, 0.023, 0.008, 0.009], 'utility': [-0.002, -0.225, -0.067, 0.372, 0.27, 0.163, -1.0, -0.114]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.054, 0.317, 1.0, 0.021, 0.006, 0.006, 0.015, 0.089, 1.0, 0.023, 0.007, 0.006, 0.014, 0.198, 0.011, 0.001, 0.001, 0.001, 0.006, 1.0, 0.008, 0.046, 0.059, 1.0, 0.016, 0.004, 0.003, 0.006, 1.0, 0.014, 0.017, 0.046, 0.209, 0.097, 0.026, 0.072, 0.131, 1.0, 0.021, 0.006, 0.005, 0.01, 0.112, 0.033, 1.0, 0.89, 0.031, 0.011, 0.011], 'utility': [-0.029, -0.241, -0.08, 0.443, 0.295, 0.169, -1.0, -0.068]} reward=-0.064 t=14
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 4, 6, 0, 7, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.481, 1.0, 0.025, 0.008, 0.007, 0.02, 0.111, 1.0, 0.027, 0.008, 0.007, 0.017, 0.252, 0.018, 0.002, 0.001, 0.002, 0.011, 1.0, 0.011, 0.055, 0.089, 1.0, 0.018, 0.004, 0.004, 0.008, 1.0, 0.015, 0.016, 0.04, 0.194, 0.132, 0.032, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.078, 0.024, 1.0, 0.323, 0.016, 0.006, 0.007], 'utility': [-0.022, -0.21, -0.055, 0.352, 0.244, 0.153, -1.0, -0.16]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.061, 0.39, 1.0, 0.023, 0.007, 0.007, 0.017, 0.1, 1.0, 0.025, 0.008, 0.007, 0.016, 0.223, 0.014, 0.001, 0.001, 0.001, 0.008, 1.0, 0.009, 0.05, 0.072, 1.0, 0.017, 0.004, 0.003, 0.007, 1.0, 0.015, 0.016, 0.043, 0.2, 0.112, 0.028, 0.034, 0.075, 1.0, 0.012, 0.003, 0.003, 0.006, 0.094, 0.028, 1.0, 0.539, 0.023, 0.008, 0.009], 'utility': [-0.002, -0.225, -0.067, 0.372, 0.27, 0.163, -1.0, -0.114]} reward=-0.075 t=15
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 4, 6, 0, 7, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.081, 0.596, 1.0, 0.028, 0.009, 0.008, 0.023, 0.123, 1.0, 0.029, 0.009, 0.008, 0.019, 0.284, 0.023, 0.002, 0.001, 0.002, 0.014, 1.0, 0.012, 0.061, 0.11, 1.0, 0.019, 0.005, 0.004, 0.009, 1.0, 0.017, 0.016, 0.038, 0.191, 0.16, 0.036, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.065, 0.02, 1.0, 0.192, 0.012, 0.005, 0.006], 'utility': [-0.006, -0.196, -0.044, 0.291, 0.216, 0.14, -1.0, -0.206]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.481, 1.0, 0.025, 0.008, 0.007, 0.02, 0.111, 1.0, 0.027, 0.008, 0.007, 0.017, 0.252, 0.018, 0.002, 0.001, 0.002, 0.011, 1.0, 0.011, 0.055, 0.089, 1.0, 0.018, 0.004, 0.004, 0.008, 1.0, 0.015, 0.016, 0.04, 0.194, 0.132, 0.032, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.078, 0.024, 1.0, 0.323, 0.016, 0.006, 0.007], 'utility': [-0.022, -0.21, -0.055, 0.352, 0.244, 0.153, -1.0, -0.16]} reward=-0.087 t=16
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 4, 6, 0, 7, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.093, 0.742, 1.0, 0.03, 0.01, 0.01, 0.027, 0.136, 1.0, 0.031, 0.01, 0.009, 0.021, 0.32, 0.029, 0.003, 0.002, 0.003, 0.018, 1.0, 0.015, 0.067, 0.137, 1.0, 0.02, 0.005, 0.004, 0.01, 1.0, 0.018, 0.017, 0.038, 0.19, 0.197, 0.042, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.053, 0.017, 1.0, 0.116, 0.009, 0.004, 0.005], 'utility': [-0.018, -0.183, -0.032, 0.262, 0.189, 0.124, -1.0, -0.251]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.081, 0.596, 1.0, 0.028, 0.009, 0.008, 0.023, 0.123, 1.0, 0.029, 0.009, 0.008, 0.019, 0.284, 0.023, 0.002, 0.001, 0.002, 0.014, 1.0, 0.012, 0.061, 0.11, 1.0, 0.019, 0.005, 0.004, 0.009, 1.0, 0.017, 0.016, 0.038, 0.191, 0.16, 0.036, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.065, 0.02, 1.0, 0.192, 0.012, 0.005, 0.006], 'utility': [-0.006, -0.196, -0.044, 0.291, 0.216, 0.14, -1.0, -0.206]} reward=-0.1 t=17
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 4, 7, 0, 7, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.106, 0.928, 1.0, 0.033, 0.011, 0.011, 0.031, 0.151, 1.0, 0.033, 0.011, 0.01, 0.023, 0.36, 0.038, 0.003, 0.002, 0.004, 0.024, 1.0, 0.017, 0.073, 0.172, 1.0, 0.021, 0.006, 0.005, 0.012, 1.0, 0.02, 0.018, 0.038, 0.192, 0.247, 0.049, 0.07, 0.177, 1.0, 0.021, 0.006, 0.005, 0.012, 0.045, 0.015, 1.0, 0.071, 0.006, 0.003, 0.004], 'utility': [-0.009, -0.171, -0.022, 0.21, 0.161, 0.105, -1.0, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.093, 0.742, 1.0, 0.03, 0.01, 0.01, 0.027, 0.136, 1.0, 0.031, 0.01, 0.009, 0.021, 0.32, 0.029, 0.003, 0.002, 0.003, 0.018, 1.0, 0.015, 0.067, 0.137, 1.0, 0.02, 0.005, 0.004, 0.01, 1.0, 0.018, 0.017, 0.038, 0.19, 0.197, 0.042, 0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005, 0.053, 0.017, 1.0, 0.116, 0.009, 0.004, 0.005], 'utility': [-0.018, -0.183, -0.032, 0.262, 0.189, 0.124, -1.0, -0.251]} reward=-0.114 t=18
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 4, 7, 4, 4, 1, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.105, 1.0, 0.86, 0.031, 0.011, 0.011, 0.031, 0.167, 1.0, 0.035, 0.012, 0.011, 0.026, 0.404, 0.049, 0.004, 0.003, 0.005, 0.031, 1.0, 0.02, 0.08, 0.215, 1.0, 0.023, 0.007, 0.006, 0.014, 1.0, 0.022, 0.019, 0.038, 0.195, 0.314, 0.059, 0.18, 0.471, 1.0, 0.039, 0.012, 0.011, 0.028, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.017, -0.16, -0.012, 0.177, 0.133, 0.046, -1.0, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.106, 0.928, 1.0, 0.033, 0.011, 0.011, 0.031, 0.151, 1.0, 0.033, 0.011, 0.01, 0.023, 0.36, 0.038, 0.003, 0.002, 0.004, 0.024, 1.0, 0.017, 0.073, 0.172, 1.0, 0.021, 0.006, 0.005, 0.012, 1.0, 0.02, 0.018, 0.038, 0.192, 0.247, 0.049, 0.07, 0.177, 1.0, 0.021, 0.006, 0.005, 0.012, 0.045, 0.015, 1.0, 0.071, 0.006, 0.003, 0.004], 'utility': [-0.009, -0.171, -0.022, 0.21, 0.161, 0.105, -1.0, -1.0]} reward=-0.216 t=19
DEBUG:deepcomp.util.simulation:Step                           action=[1, 7, 3, 3, 4, 4, 1, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.095, 1.0, 0.683, 0.027, 0.009, 0.009, 0.028, 0.184, 1.0, 0.037, 0.013, 0.012, 0.029, 0.453, 0.062, 0.005, 0.003, 0.006, 0.04, 1.0, 0.023, 0.088, 0.269, 1.0, 0.025, 0.007, 0.006, 0.016, 1.0, 0.024, 0.02, 0.039, 0.2, 0.406, 0.071, 0.377, 1.0, 0.887, 0.057, 0.021, 0.02, 0.056, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.011, -0.15, -0.002, 0.131, 0.106, 0.022, -1.0, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.105, 1.0, 0.86, 0.031, 0.011, 0.011, 0.031, 0.167, 1.0, 0.035, 0.012, 0.011, 0.026, 0.404, 0.049, 0.004, 0.003, 0.005, 0.031, 1.0, 0.02, 0.08, 0.215, 1.0, 0.023, 0.007, 0.006, 0.014, 1.0, 0.022, 0.019, 0.038, 0.195, 0.314, 0.059, 0.18, 0.471, 1.0, 0.039, 0.012, 0.011, 0.028, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.017, -0.16, -0.012, 0.177, 0.133, 0.046, -1.0, -1.0]} reward=-0.229 t=20
DEBUG:deepcomp.util.simulation:Step                           action=[2, 7, 1, 3, 4, 4, 1, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.086, 1.0, 0.54, 0.023, 0.008, 0.008, 0.026, 0.203, 1.0, 0.04, 0.014, 0.013, 0.031, 0.507, 0.078, 0.006, 0.004, 0.007, 0.052, 1.0, 0.026, 0.096, 0.338, 1.0, 0.027, 0.008, 0.007, 0.018, 1.0, 0.027, 0.021, 0.04, 0.206, 0.531, 0.086, 0.393, 1.0, 0.421, 0.042, 0.017, 0.019, 0.057, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.016, -0.143, 0.006, 0.097, 0.078, -0.154, -0.377, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.095, 1.0, 0.683, 0.027, 0.009, 0.009, 0.028, 0.184, 1.0, 0.037, 0.013, 0.012, 0.029, 0.453, 0.062, 0.005, 0.003, 0.006, 0.04, 1.0, 0.023, 0.088, 0.269, 1.0, 0.025, 0.007, 0.006, 0.016, 1.0, 0.024, 0.02, 0.039, 0.2, 0.406, 0.071, 0.377, 1.0, 0.887, 0.057, 0.021, 0.02, 0.056, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.011, -0.15, -0.002, 0.131, 0.106, 0.022, -1.0, -1.0]} reward=-0.187 t=21
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 1, 3, 4, 4, 6, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.077, 1.0, 0.426, 0.02, 0.007, 0.008, 0.024, 0.224, 1.0, 0.042, 0.015, 0.014, 0.035, 0.567, 0.098, 0.007, 0.005, 0.009, 0.067, 1.0, 0.03, 0.105, 0.424, 1.0, 0.028, 0.009, 0.008, 0.021, 1.0, 0.031, 0.023, 0.042, 0.214, 0.702, 0.104, 0.438, 1.0, 0.232, 0.033, 0.016, 0.019, 0.065, 0.046, 0.017, 1.0, 0.038, 0.005, 0.003, 0.004], 'utility': [-0.013, -0.137, 0.014, 0.056, 0.051, -0.18, -0.32, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.086, 1.0, 0.54, 0.023, 0.008, 0.008, 0.026, 0.203, 1.0, 0.04, 0.014, 0.013, 0.031, 0.507, 0.078, 0.006, 0.004, 0.007, 0.052, 1.0, 0.026, 0.096, 0.338, 1.0, 0.027, 0.008, 0.007, 0.018, 1.0, 0.027, 0.021, 0.04, 0.206, 0.531, 0.086, 0.393, 1.0, 0.421, 0.042, 0.017, 0.019, 0.057, 0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [-0.016, -0.143, 0.006, 0.097, 0.078, -0.154, -0.377, -1.0]} reward=-0.189 t=22
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 1, 3, 4, 4, 3, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.069, 1.0, 0.334, 0.017, 0.006, 0.007, 0.021, 0.246, 1.0, 0.044, 0.016, 0.015, 0.038, 0.633, 0.123, 0.008, 0.006, 0.011, 0.085, 1.0, 0.034, 0.114, 0.531, 1.0, 0.031, 0.01, 0.009, 0.024, 1.0, 0.034, 0.025, 0.044, 0.222, 0.935, 0.128, 0.529, 1.0, 0.152, 0.029, 0.016, 0.022, 0.085, 0.067, 0.028, 1.0, 0.034, 0.005, 0.003, 0.005], 'utility': [-0.016, -0.132, 0.021, 0.023, 0.024, -0.208, -0.272, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.077, 1.0, 0.426, 0.02, 0.007, 0.008, 0.024, 0.224, 1.0, 0.042, 0.015, 0.014, 0.035, 0.567, 0.098, 0.007, 0.005, 0.009, 0.067, 1.0, 0.03, 0.105, 0.424, 1.0, 0.028, 0.009, 0.008, 0.021, 1.0, 0.031, 0.023, 0.042, 0.214, 0.702, 0.104, 0.438, 1.0, 0.232, 0.033, 0.016, 0.019, 0.065, 0.046, 0.017, 1.0, 0.038, 0.005, 0.003, 0.004], 'utility': [-0.013, -0.137, 0.014, 0.056, 0.051, -0.18, -0.32, -1.0]} reward=-0.191 t=23
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 1, 3, 4, 4, 3, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.061, 1.0, 0.261, 0.014, 0.006, 0.006, 0.019, 0.27, 1.0, 0.047, 0.017, 0.016, 0.042, 0.707, 0.152, 0.009, 0.007, 0.014, 0.108, 1.0, 0.038, 0.123, 0.667, 1.0, 0.033, 0.011, 0.01, 0.028, 0.798, 0.031, 0.021, 0.036, 0.185, 1.0, 0.125, 0.68, 1.0, 0.117, 0.029, 0.019, 0.029, 0.131, 0.117, 0.059, 1.0, 0.038, 0.008, 0.005, 0.009], 'utility': [-0.014, -0.13, 0.027, -0.014, -0.002, -0.236, -0.239, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.069, 1.0, 0.334, 0.017, 0.006, 0.007, 0.021, 0.246, 1.0, 0.044, 0.016, 0.015, 0.038, 0.633, 0.123, 0.008, 0.006, 0.011, 0.085, 1.0, 0.034, 0.114, 0.531, 1.0, 0.031, 0.01, 0.009, 0.024, 1.0, 0.034, 0.025, 0.044, 0.222, 0.935, 0.128, 0.529, 1.0, 0.152, 0.029, 0.016, 0.022, 0.085, 0.067, 0.028, 1.0, 0.034, 0.005, 0.003, 0.005], 'utility': [-0.016, -0.132, 0.021, 0.023, 0.024, -0.208, -0.272, -1.0]} reward=-0.195 t=24
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 1, 3, 4, 4, 3, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.054, 1.0, 0.203, 0.012, 0.005, 0.005, 0.017, 0.296, 1.0, 0.05, 0.018, 0.018, 0.046, 0.788, 0.188, 0.011, 0.008, 0.017, 0.137, 1.0, 0.043, 0.133, 0.836, 1.0, 0.035, 0.012, 0.011, 0.031, 0.592, 0.026, 0.017, 0.029, 0.143, 1.0, 0.114, 0.888, 1.0, 0.105, 0.032, 0.024, 0.042, 0.235, 0.215, 0.144, 1.0, 0.047, 0.012, 0.009, 0.018], 'utility': [-0.016, -0.129, 0.032, -0.046, -0.028, -0.264, -0.226, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.061, 1.0, 0.261, 0.014, 0.006, 0.006, 0.019, 0.27, 1.0, 0.047, 0.017, 0.016, 0.042, 0.707, 0.152, 0.009, 0.007, 0.014, 0.108, 1.0, 0.038, 0.123, 0.667, 1.0, 0.033, 0.011, 0.01, 0.028, 0.798, 0.031, 0.021, 0.036, 0.185, 1.0, 0.125, 0.68, 1.0, 0.117, 0.029, 0.019, 0.029, 0.131, 0.117, 0.059, 1.0, 0.038, 0.008, 0.005, 0.009], 'utility': [-0.014, -0.13, 0.027, -0.014, -0.002, -0.236, -0.239, -1.0]} reward=-0.201 t=25
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 1, 3, 4, 4, 3, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.047, 1.0, 0.158, 0.01, 0.004, 0.005, 0.016, 0.324, 1.0, 0.052, 0.019, 0.019, 0.05, 0.877, 0.229, 0.013, 0.01, 0.02, 0.173, 1.0, 0.048, 0.137, 1.0, 0.955, 0.036, 0.012, 0.012, 0.034, 0.438, 0.022, 0.014, 0.022, 0.11, 1.0, 0.103, 1.0, 0.887, 0.092, 0.033, 0.029, 0.06, 0.42, 0.377, 0.372, 1.0, 0.061, 0.019, 0.016, 0.037], 'utility': [-0.015, -0.13, 0.037, -0.08, -0.053, -0.292, -0.236, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.054, 1.0, 0.203, 0.012, 0.005, 0.005, 0.017, 0.296, 1.0, 0.05, 0.018, 0.018, 0.046, 0.788, 0.188, 0.011, 0.008, 0.017, 0.137, 1.0, 0.043, 0.133, 0.836, 1.0, 0.035, 0.012, 0.011, 0.031, 0.592, 0.026, 0.017, 0.029, 0.143, 1.0, 0.114, 0.888, 1.0, 0.105, 0.032, 0.024, 0.042, 0.235, 0.215, 0.144, 1.0, 0.047, 0.012, 0.009, 0.018], 'utility': [-0.016, -0.129, 0.032, -0.046, -0.028, -0.264, -0.226, -1.0]} reward=-0.21 t=26
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 1, 3, 4, 6, 3, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 1.0, 0.122, 0.008, 0.003, 0.004, 0.014, 0.354, 1.0, 0.055, 0.021, 0.021, 0.055, 0.975, 0.278, 0.015, 0.012, 0.025, 0.218, 1.0, 0.053, 0.117, 1.0, 0.762, 0.03, 0.011, 0.011, 0.031, 0.324, 0.018, 0.011, 0.017, 0.085, 1.0, 0.094, 1.0, 0.739, 0.08, 0.033, 0.034, 0.083, 0.776, 0.601, 0.998, 1.0, 0.078, 0.028, 0.027, 0.072], 'utility': [-0.064, -0.133, 0.04, -0.161, -0.078, -0.145, -0.266, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.047, 1.0, 0.158, 0.01, 0.004, 0.005, 0.016, 0.324, 1.0, 0.052, 0.019, 0.019, 0.05, 0.877, 0.229, 0.013, 0.01, 0.02, 0.173, 1.0, 0.048, 0.137, 1.0, 0.955, 0.036, 0.012, 0.012, 0.034, 0.438, 0.022, 0.014, 0.022, 0.11, 1.0, 0.103, 1.0, 0.887, 0.092, 0.033, 0.029, 0.06, 0.42, 0.377, 0.372, 1.0, 0.061, 0.019, 0.016, 0.037], 'utility': [-0.015, -0.13, 0.037, -0.08, -0.053, -0.292, -0.236, -1.0]} reward=-0.228 t=27
DEBUG:deepcomp.util.simulation:Step                           action=[2, 7, 1, 7, 2, 3, 3, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.035, 1.0, 0.093, 0.007, 0.003, 0.003, 0.012, 0.357, 0.924, 0.054, 0.021, 0.021, 0.055, 1.0, 0.335, 0.017, 0.014, 0.03, 0.273, 1.0, 0.058, 0.1, 1.0, 0.61, 0.026, 0.009, 0.009, 0.028, 0.24, 0.015, 0.009, 0.014, 0.066, 1.0, 0.085, 0.604, 0.395, 0.047, 0.022, 0.025, 0.074, 1.0, 0.311, 1.0, 0.359, 0.035, 0.015, 0.016, 0.05], 'utility': [-0.126, -0.228, 0.009, -0.247, -0.005, -0.033, -0.312, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 1.0, 0.122, 0.008, 0.003, 0.004, 0.014, 0.354, 1.0, 0.055, 0.021, 0.021, 0.055, 0.975, 0.278, 0.015, 0.012, 0.025, 0.218, 1.0, 0.053, 0.117, 1.0, 0.762, 0.03, 0.011, 0.011, 0.031, 0.324, 0.018, 0.011, 0.017, 0.085, 1.0, 0.094, 1.0, 0.739, 0.08, 0.033, 0.034, 0.083, 0.776, 0.601, 0.998, 1.0, 0.078, 0.028, 0.027, 0.072], 'utility': [-0.064, -0.133, 0.04, -0.161, -0.078, -0.145, -0.266, -1.0]} reward=-0.232 t=28
DEBUG:deepcomp.util.simulation:Step                           action=[3, 7, 1, 5, 4, 0, 7, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.03, 1.0, 0.071, 0.006, 0.002, 0.003, 0.011, 0.351, 0.833, 0.051, 0.02, 0.02, 0.055, 1.0, 0.401, 0.019, 0.016, 0.036, 0.34, 1.0, 0.064, 0.086, 1.0, 0.488, 0.022, 0.008, 0.008, 0.025, 0.178, 0.013, 0.007, 0.011, 0.051, 1.0, 0.077, 0.245, 0.149, 0.019, 0.01, 0.013, 0.047, 1.0, 0.137, 1.0, 0.121, 0.014, 0.007, 0.008, 0.031], 'utility': [-0.054, -0.223, -0.072, -0.136, -0.018, -0.034, -0.016, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.035, 1.0, 0.093, 0.007, 0.003, 0.003, 0.012, 0.357, 0.924, 0.054, 0.021, 0.021, 0.055, 1.0, 0.335, 0.017, 0.014, 0.03, 0.273, 1.0, 0.058, 0.1, 1.0, 0.61, 0.026, 0.009, 0.009, 0.028, 0.24, 0.015, 0.009, 0.014, 0.066, 1.0, 0.085, 0.604, 0.395, 0.047, 0.022, 0.025, 0.074, 1.0, 0.311, 1.0, 0.359, 0.035, 0.015, 0.016, 0.05], 'utility': [-0.126, -0.228, 0.009, -0.247, -0.005, -0.033, -0.312, -1.0]} reward=-0.209 t=29
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 4, 1, 4, 0, 3, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.026, 1.0, 0.054, 0.005, 0.002, 0.002, 0.009, 0.345, 0.752, 0.048, 0.019, 0.02, 0.054, 1.0, 0.477, 0.022, 0.019, 0.043, 0.423, 1.0, 0.07, 0.073, 1.0, 0.391, 0.019, 0.007, 0.007, 0.023, 0.133, 0.01, 0.006, 0.008, 0.039, 1.0, 0.069, 0.086, 0.05, 0.007, 0.004, 0.006, 0.026, 1.0, 0.051, 1.0, 0.038, 0.005, 0.003, 0.004, 0.017], 'utility': [-0.097, -0.22, -0.066, -0.095, -0.031, 0.032, 0.114, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.03, 1.0, 0.071, 0.006, 0.002, 0.003, 0.011, 0.351, 0.833, 0.051, 0.02, 0.02, 0.055, 1.0, 0.401, 0.019, 0.016, 0.036, 0.34, 1.0, 0.064, 0.086, 1.0, 0.488, 0.022, 0.008, 0.008, 0.025, 0.178, 0.013, 0.007, 0.011, 0.051, 1.0, 0.077, 0.245, 0.149, 0.019, 0.01, 0.013, 0.047, 1.0, 0.137, 1.0, 0.121, 0.014, 0.007, 0.008, 0.031], 'utility': [-0.054, -0.223, -0.072, -0.136, -0.018, -0.034, -0.016, -1.0]} reward=-0.192 t=30
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 4, 1, 0, 3, 3, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.022, 1.0, 0.041, 0.004, 0.002, 0.002, 0.008, 0.339, 0.679, 0.046, 0.018, 0.019, 0.053, 1.0, 0.563, 0.025, 0.022, 0.052, 0.524, 1.0, 0.076, 0.062, 1.0, 0.314, 0.016, 0.006, 0.006, 0.02, 0.1, 0.009, 0.005, 0.007, 0.031, 1.0, 0.063, 0.025, 0.015, 0.002, 0.001, 0.002, 0.012, 1.0, 0.017, 1.0, 0.011, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.061, -0.219, -0.061, -0.134, -0.043, 0.053, 0.303, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.026, 1.0, 0.054, 0.005, 0.002, 0.002, 0.009, 0.345, 0.752, 0.048, 0.019, 0.02, 0.054, 1.0, 0.477, 0.022, 0.019, 0.043, 0.423, 1.0, 0.07, 0.073, 1.0, 0.391, 0.019, 0.007, 0.007, 0.023, 0.133, 0.01, 0.006, 0.008, 0.039, 1.0, 0.069, 0.086, 0.05, 0.007, 0.004, 0.006, 0.026, 1.0, 0.051, 1.0, 0.038, 0.005, 0.003, 0.004, 0.017], 'utility': [-0.097, -0.22, -0.066, -0.095, -0.031, 0.032, 0.114, -1.0]} reward=-0.175 t=31
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 4, 1, 0, 0, 1, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.018, 1.0, 0.031, 0.003, 0.001, 0.002, 0.007, 0.333, 0.615, 0.043, 0.018, 0.019, 0.052, 1.0, 0.66, 0.028, 0.025, 0.062, 0.647, 1.0, 0.082, 0.053, 1.0, 0.253, 0.013, 0.005, 0.006, 0.018, 0.077, 0.007, 0.004, 0.005, 0.025, 1.0, 0.058, 0.006, 0.004, 0.001, 0.0, 0.001, 0.005, 1.0, 0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [-0.088, -0.22, -0.056, -0.015, -0.056, 0.096, 0.536, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.022, 1.0, 0.041, 0.004, 0.002, 0.002, 0.008, 0.339, 0.679, 0.046, 0.018, 0.019, 0.053, 1.0, 0.563, 0.025, 0.022, 0.052, 0.524, 1.0, 0.076, 0.062, 1.0, 0.314, 0.016, 0.006, 0.006, 0.02, 0.1, 0.009, 0.005, 0.007, 0.031, 1.0, 0.063, 0.025, 0.015, 0.002, 0.001, 0.002, 0.012, 1.0, 0.017, 1.0, 0.011, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.061, -0.219, -0.061, -0.134, -0.043, 0.053, 0.303, -1.0]} reward=-0.14 t=32
DEBUG:deepcomp.util.simulation:Step                           action=[2, 1, 3, 1, 4, 1, 1, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 1.0, 0.023, 0.002, 0.001, 0.001, 0.006, 0.327, 0.557, 0.041, 0.017, 0.018, 0.052, 1.0, 0.768, 0.032, 0.029, 0.074, 0.797, 1.0, 0.088, 0.045, 1.0, 0.205, 0.011, 0.005, 0.005, 0.017, 0.06, 0.006, 0.003, 0.005, 0.02, 1.0, 0.055, 0.002, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0, 0.004], 'utility': [-0.057, -0.222, -0.052, -0.127, -0.068, 0.077, 0.719, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.018, 1.0, 0.031, 0.003, 0.001, 0.002, 0.007, 0.333, 0.615, 0.043, 0.018, 0.019, 0.052, 1.0, 0.66, 0.028, 0.025, 0.062, 0.647, 1.0, 0.082, 0.053, 1.0, 0.253, 0.013, 0.005, 0.006, 0.018, 0.077, 0.007, 0.004, 0.005, 0.025, 1.0, 0.058, 0.006, 0.004, 0.001, 0.0, 0.001, 0.005, 1.0, 0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [-0.088, -0.22, -0.056, -0.015, -0.056, 0.096, 0.536, -1.0]} reward=-0.117 t=33
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 4, 1, 1, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.012, 1.0, 0.017, 0.002, 0.001, 0.001, 0.005, 0.321, 0.506, 0.039, 0.016, 0.018, 0.051, 1.0, 0.887, 0.035, 0.034, 0.088, 0.978, 1.0, 0.095, 0.039, 1.0, 0.166, 0.01, 0.004, 0.004, 0.015, 0.048, 0.006, 0.003, 0.004, 0.016, 1.0, 0.052, 0.002, 0.001, 0.0, 0.0, 0.0, 0.003, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.067, -0.225, -0.049, 0.0, -0.08, 0.15, 0.663, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 1.0, 0.023, 0.002, 0.001, 0.001, 0.006, 0.327, 0.557, 0.041, 0.017, 0.018, 0.052, 1.0, 0.768, 0.032, 0.029, 0.074, 0.797, 1.0, 0.088, 0.045, 1.0, 0.205, 0.011, 0.005, 0.005, 0.017, 0.06, 0.006, 0.003, 0.005, 0.02, 1.0, 0.055, 0.002, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0, 0.004], 'utility': [-0.057, -0.222, -0.052, -0.127, -0.068, 0.077, 0.719, -1.0]} reward=-0.075 t=34
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 4, 1, 1, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.01, 1.0, 0.013, 0.001, 0.001, 0.001, 0.005, 0.316, 0.459, 0.037, 0.016, 0.017, 0.051, 1.0, 0.85, 0.033, 0.032, 0.087, 1.0, 0.835, 0.085, 0.033, 1.0, 0.135, 0.008, 0.003, 0.004, 0.013, 0.039, 0.005, 0.002, 0.003, 0.014, 1.0, 0.051, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.051, -0.229, -0.046, -0.107, -0.092, 0.129, 0.574, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.012, 1.0, 0.017, 0.002, 0.001, 0.001, 0.005, 0.321, 0.506, 0.039, 0.016, 0.018, 0.051, 1.0, 0.887, 0.035, 0.034, 0.088, 0.978, 1.0, 0.095, 0.039, 1.0, 0.166, 0.01, 0.004, 0.004, 0.015, 0.048, 0.006, 0.003, 0.004, 0.016, 1.0, 0.052, 0.002, 0.001, 0.0, 0.0, 0.0, 0.003, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.067, -0.225, -0.049, 0.0, -0.08, 0.15, 0.663, -1.0]} reward=-0.092 t=35
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 4, 1, 1, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.008, 1.0, 0.01, 0.001, 0.001, 0.001, 0.004, 0.31, 0.418, 0.035, 0.015, 0.017, 0.05, 1.0, 0.794, 0.03, 0.03, 0.084, 1.0, 0.684, 0.074, 0.028, 1.0, 0.111, 0.007, 0.003, 0.003, 0.012, 0.034, 0.005, 0.002, 0.003, 0.012, 1.0, 0.051, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.054, -0.235, -0.043, 0.022, -0.104, 0.174, 0.574, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.01, 1.0, 0.013, 0.001, 0.001, 0.001, 0.005, 0.316, 0.459, 0.037, 0.016, 0.017, 0.051, 1.0, 0.85, 0.033, 0.032, 0.087, 1.0, 0.835, 0.085, 0.033, 1.0, 0.135, 0.008, 0.003, 0.004, 0.013, 0.039, 0.005, 0.002, 0.003, 0.014, 1.0, 0.051, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.051, -0.229, -0.046, -0.107, -0.092, 0.129, 0.574, -1.0]} reward=-0.087 t=36
DEBUG:deepcomp.util.simulation:Step                           action=[2, 1, 3, 1, 4, 1, 1, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.007, 1.0, 0.008, 0.001, 0.001, 0.001, 0.003, 0.305, 0.381, 0.034, 0.015, 0.016, 0.05, 1.0, 0.738, 0.027, 0.028, 0.081, 1.0, 0.562, 0.065, 0.025, 1.0, 0.091, 0.006, 0.003, 0.003, 0.011, 0.03, 0.005, 0.002, 0.003, 0.011, 1.0, 0.052, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.015], 'utility': [-0.043, -0.241, -0.04, -0.079, -0.241, 0.15, 0.574, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.008, 1.0, 0.01, 0.001, 0.001, 0.001, 0.004, 0.31, 0.418, 0.035, 0.015, 0.017, 0.05, 1.0, 0.794, 0.03, 0.03, 0.084, 1.0, 0.684, 0.074, 0.028, 1.0, 0.111, 0.007, 0.003, 0.003, 0.012, 0.034, 0.005, 0.002, 0.003, 0.012, 1.0, 0.051, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.054, -0.235, -0.043, 0.022, -0.104, 0.174, 0.574, -1.0]} reward=-0.098 t=37
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 0, 1, 1, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.006, 1.0, 0.006, 0.001, 0.0, 0.001, 0.003, 0.3, 0.348, 0.032, 0.014, 0.016, 0.049, 1.0, 0.684, 0.025, 0.026, 0.078, 1.0, 0.463, 0.057, 0.021, 1.0, 0.076, 0.005, 0.002, 0.003, 0.01, 0.027, 0.005, 0.002, 0.003, 0.011, 1.0, 0.056, 0.004, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.065, 1.0, 0.02, 0.005, 0.003, 0.006, 0.045], 'utility': [-0.043, -0.248, -0.038, 0.044, -0.248, 0.169, 0.589, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.007, 1.0, 0.008, 0.001, 0.001, 0.001, 0.003, 0.305, 0.381, 0.034, 0.015, 0.016, 0.05, 1.0, 0.738, 0.027, 0.028, 0.081, 1.0, 0.562, 0.065, 0.025, 1.0, 0.091, 0.006, 0.003, 0.003, 0.011, 0.03, 0.005, 0.002, 0.003, 0.011, 1.0, 0.052, 0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.015], 'utility': [-0.043, -0.241, -0.04, -0.079, -0.241, 0.15, 0.574, -1.0]} reward=-0.101 t=38
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 0, 1, 1, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.005, 0.001, 0.0, 0.001, 0.003, 0.295, 0.318, 0.03, 0.014, 0.016, 0.049, 1.0, 0.631, 0.022, 0.025, 0.076, 1.0, 0.383, 0.05, 0.019, 1.0, 0.063, 0.005, 0.002, 0.002, 0.009, 0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.061, 0.01, 0.005, 0.001, 0.001, 0.001, 0.01, 1.0, 0.256, 1.0, 0.053, 0.014, 0.01, 0.017, 0.109], 'utility': [-0.035, -0.256, -0.036, -0.046, -0.256, 0.138, 0.433, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.006, 1.0, 0.006, 0.001, 0.0, 0.001, 0.003, 0.3, 0.348, 0.032, 0.014, 0.016, 0.049, 1.0, 0.684, 0.025, 0.026, 0.078, 1.0, 0.463, 0.057, 0.021, 1.0, 0.076, 0.005, 0.002, 0.003, 0.01, 0.027, 0.005, 0.002, 0.003, 0.011, 1.0, 0.056, 0.004, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0, 0.065, 1.0, 0.02, 0.005, 0.003, 0.006, 0.045], 'utility': [-0.043, -0.248, -0.038, 0.044, -0.248, 0.169, 0.589, -1.0]} reward=-0.111 t=39
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 0, 1, 1, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.004, 0.001, 0.0, 0.0, 0.003, 0.29, 0.291, 0.029, 0.013, 0.015, 0.048, 1.0, 0.58, 0.02, 0.023, 0.074, 1.0, 0.318, 0.044, 0.016, 1.0, 0.054, 0.004, 0.002, 0.002, 0.009, 0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068, 0.037, 0.014, 0.003, 0.002, 0.004, 0.024, 1.0, 0.959, 1.0, 0.115, 0.034, 0.025, 0.042, 0.215], 'utility': [-0.034, -0.264, -0.034, 0.068, -0.264, 0.135, 0.235, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.005, 0.001, 0.0, 0.001, 0.003, 0.295, 0.318, 0.03, 0.014, 0.016, 0.049, 1.0, 0.631, 0.022, 0.025, 0.076, 1.0, 0.383, 0.05, 0.019, 1.0, 0.063, 0.005, 0.002, 0.002, 0.009, 0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.061, 0.01, 0.005, 0.001, 0.001, 0.001, 0.01, 1.0, 0.256, 1.0, 0.053, 0.014, 0.01, 0.017, 0.109], 'utility': [-0.035, -0.256, -0.036, -0.046, -0.256, 0.138, 0.433, -1.0]} reward=-0.119 t=40
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 3, 1, 0, 0, 1, 1] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.001, 0.0, 0.0, 0.003, 0.286, 0.267, 0.027, 0.013, 0.015, 0.048, 1.0, 0.532, 0.018, 0.022, 0.072, 1.0, 0.265, 0.038, 0.015, 1.0, 0.046, 0.004, 0.002, 0.002, 0.008, 0.026, 0.005, 0.002, 0.003, 0.011, 1.0, 0.078, 0.13, 0.04, 0.008, 0.006, 0.009, 0.052, 1.0, 1.0, 0.271, 0.059, 0.02, 0.015, 0.025, 0.097], 'utility': [-0.015, -0.273, -0.031, -0.014, -0.273, 0.113, 0.055, 0.102]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.004, 0.001, 0.0, 0.0, 0.003, 0.29, 0.291, 0.029, 0.013, 0.015, 0.048, 1.0, 0.58, 0.02, 0.023, 0.074, 1.0, 0.318, 0.044, 0.016, 1.0, 0.054, 0.004, 0.002, 0.002, 0.009, 0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068, 0.037, 0.014, 0.003, 0.002, 0.004, 0.024, 1.0, 0.959, 1.0, 0.115, 0.034, 0.025, 0.042, 0.215], 'utility': [-0.034, -0.264, -0.034, 0.068, -0.264, 0.135, 0.235, -1.0]} reward=-0.04 t=41
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 4, 1, 0, 4, 1, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003, 0.281, 0.245, 0.026, 0.013, 0.015, 0.048, 1.0, 0.487, 0.017, 0.02, 0.07, 1.0, 0.221, 0.034, 0.013, 1.0, 0.04, 0.003, 0.002, 0.002, 0.007, 0.027, 0.006, 0.003, 0.003, 0.012, 1.0, 0.091, 0.426, 0.095, 0.02, 0.014, 0.021, 0.096, 1.0, 1.0, 0.062, 0.022, 0.01, 0.008, 0.011, 0.033], 'utility': [-0.019, -0.282, -0.029, 0.037, -0.282, 0.089, -0.045, 0.073]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.001, 0.0, 0.0, 0.003, 0.286, 0.267, 0.027, 0.013, 0.015, 0.048, 1.0, 0.532, 0.018, 0.022, 0.072, 1.0, 0.265, 0.038, 0.015, 1.0, 0.046, 0.004, 0.002, 0.002, 0.008, 0.026, 0.005, 0.002, 0.003, 0.011, 1.0, 0.078, 0.13, 0.04, 0.008, 0.006, 0.009, 0.052, 1.0, 1.0, 0.271, 0.059, 0.02, 0.015, 0.025, 0.097], 'utility': [-0.015, -0.273, -0.031, -0.014, -0.273, 0.113, 0.055, 0.102]} reward=-0.065 t=42
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 4, 1, 0, 4, 1, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003, 0.277, 0.225, 0.025, 0.012, 0.015, 0.048, 1.0, 0.444, 0.015, 0.019, 0.069, 1.0, 0.186, 0.03, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.028, 0.007, 0.003, 0.003, 0.012, 1.0, 0.107, 1.0, 0.152, 0.035, 0.022, 0.032, 0.115, 0.749, 1.0, 0.01, 0.005, 0.003, 0.003, 0.003, 0.007], 'utility': [-0.014, -0.292, -0.027, 0.023, -0.292, 0.051, -0.23, 0.605]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003, 0.281, 0.245, 0.026, 0.013, 0.015, 0.048, 1.0, 0.487, 0.017, 0.02, 0.07, 1.0, 0.221, 0.034, 0.013, 1.0, 0.04, 0.003, 0.002, 0.002, 0.007, 0.027, 0.006, 0.003, 0.003, 0.012, 1.0, 0.091, 0.426, 0.095, 0.02, 0.014, 0.021, 0.096, 1.0, 1.0, 0.062, 0.022, 0.01, 0.008, 0.011, 0.033], 'utility': [-0.019, -0.282, -0.029, 0.037, -0.282, 0.089, -0.045, 0.073]} reward=-0.038 t=43
DEBUG:deepcomp.util.simulation:Step                           action=[3, 1, 4, 1, 0, 4, 1, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.001, 0.003, 0.273, 0.208, 0.024, 0.012, 0.014, 0.048, 1.0, 0.405, 0.014, 0.018, 0.067, 1.0, 0.157, 0.026, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.03, 0.008, 0.003, 0.004, 0.014, 1.0, 0.126, 1.0, 0.093, 0.024, 0.015, 0.019, 0.054, 0.241, 1.0, 0.001, 0.001, 0.0, 0.0, 0.0, 0.001], 'utility': [-0.016, -0.301, -0.025, 0.068, -0.301, 0.02, -0.056, 0.866]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003, 0.277, 0.225, 0.025, 0.012, 0.015, 0.048, 1.0, 0.444, 0.015, 0.019, 0.069, 1.0, 0.186, 0.03, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.028, 0.007, 0.003, 0.003, 0.012, 1.0, 0.107, 1.0, 0.152, 0.035, 0.022, 0.032, 0.115, 0.749, 1.0, 0.01, 0.005, 0.003, 0.003, 0.003, 0.007], 'utility': [-0.014, -0.292, -0.027, 0.023, -0.292, 0.051, -0.23, 0.605]} reward=-0.031 t=44
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 6, 0, 4, 3, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004, 0.269, 0.192, 0.023, 0.011, 0.014, 0.048, 1.0, 0.369, 0.013, 0.017, 0.067, 1.0, 0.133, 0.023, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.033, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148, 1.0, 0.051, 0.015, 0.009, 0.01, 0.023, 0.077, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.013, 0.285, -0.089, 0.083, 0.285, -0.02, 0.049, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.004, 1.0, 0.003, 0.0, 0.0, 0.001, 0.003, 0.273, 0.208, 0.024, 0.012, 0.014, 0.048, 1.0, 0.405, 0.014, 0.018, 0.067, 1.0, 0.157, 0.026, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.03, 0.008, 0.003, 0.004, 0.014, 1.0, 0.126, 1.0, 0.093, 0.024, 0.015, 0.019, 0.054, 0.241, 1.0, 0.001, 0.001, 0.0, 0.0, 0.0, 0.001], 'utility': [-0.016, -0.301, -0.025, 0.068, -0.301, 0.02, -0.056, 0.866]} reward=0.032 t=45
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 0, 0, 4, 3, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.005, 0.265, 0.177, 0.022, 0.011, 0.014, 0.048, 1.0, 0.336, 0.012, 0.016, 0.066, 1.0, 0.114, 0.021, 0.014, 1.0, 0.042, 0.004, 0.002, 0.002, 0.008, 0.035, 0.01, 0.004, 0.005, 0.017, 1.0, 0.174, 1.0, 0.026, 0.01, 0.006, 0.005, 0.009, 0.025, 1.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0], 'utility': [-0.015, 0.27, 0.068, 0.097, 0.27, -0.055, 0.179, 0.903]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.005, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004, 0.269, 0.192, 0.023, 0.011, 0.014, 0.048, 1.0, 0.369, 0.013, 0.017, 0.067, 1.0, 0.133, 0.023, 0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007, 0.033, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148, 1.0, 0.051, 0.015, 0.009, 0.01, 0.023, 0.077, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.013, 0.285, -0.089, 0.083, 0.285, -0.02, 0.049, 1.0]} reward=0.197 t=46
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 0, 0, 0, 3, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.007, 1.0, 0.004, 0.001, 0.0, 0.001, 0.006, 0.262, 0.164, 0.021, 0.011, 0.014, 0.048, 1.0, 0.306, 0.011, 0.015, 0.066, 1.0, 0.098, 0.019, 0.015, 1.0, 0.049, 0.004, 0.002, 0.002, 0.008, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.015, 0.007, 0.004, 0.003, 0.004, 0.01, 1.0, 0.002, 0.003, 0.006, 0.009, 0.005, 0.003], 'utility': [-0.024, 0.252, 0.075, 0.11, 0.252, -0.064, 0.301, 0.385]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.005, 0.265, 0.177, 0.022, 0.011, 0.014, 0.048, 1.0, 0.336, 0.012, 0.016, 0.066, 1.0, 0.114, 0.021, 0.014, 1.0, 0.042, 0.004, 0.002, 0.002, 0.008, 0.035, 0.01, 0.004, 0.005, 0.017, 1.0, 0.174, 1.0, 0.026, 0.01, 0.006, 0.005, 0.009, 0.025, 1.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0], 'utility': [-0.015, 0.27, 0.068, 0.097, 0.27, -0.055, 0.179, 0.903]} reward=0.215 t=47
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 0, 0, 0, 3, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.008, 1.0, 0.004, 0.001, 0.001, 0.001, 0.008, 0.259, 0.153, 0.02, 0.011, 0.014, 0.048, 1.0, 0.279, 0.01, 0.014, 0.066, 1.0, 0.085, 0.017, 0.017, 1.0, 0.058, 0.004, 0.002, 0.002, 0.009, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.013, 0.009, 0.004, 0.003, 0.003, 0.006, 1.0, 0.007, 0.011, 0.03, 0.057, 0.021, 0.009], 'utility': [-0.026, 0.231, 0.081, 0.122, 0.231, -0.062, 0.326, 0.085]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.007, 1.0, 0.004, 0.001, 0.0, 0.001, 0.006, 0.262, 0.164, 0.021, 0.011, 0.014, 0.048, 1.0, 0.306, 0.011, 0.015, 0.066, 1.0, 0.098, 0.019, 0.015, 1.0, 0.049, 0.004, 0.002, 0.002, 0.008, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.015, 0.007, 0.004, 0.003, 0.004, 0.01, 1.0, 0.002, 0.003, 0.006, 0.009, 0.005, 0.003], 'utility': [-0.024, 0.252, 0.075, 0.11, 0.252, -0.064, 0.301, 0.385]} reward=0.161 t=48
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 0, 0, 4, 3, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.01, 1.0, 0.005, 0.001, 0.001, 0.001, 0.011, 0.256, 0.142, 0.019, 0.01, 0.013, 0.049, 1.0, 0.256, 0.009, 0.014, 0.067, 1.0, 0.074, 0.015, 0.02, 1.0, 0.069, 0.005, 0.002, 0.003, 0.01, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.018, 0.019, 0.009, 0.005, 0.004, 0.007, 1.0, 0.015, 0.024, 0.092, 0.254, 0.057, 0.02], 'utility': [-0.024, 0.208, 0.086, 0.133, 0.208, -0.063, 0.234, -0.128]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.008, 1.0, 0.004, 0.001, 0.001, 0.001, 0.008, 0.259, 0.153, 0.02, 0.011, 0.014, 0.048, 1.0, 0.279, 0.01, 0.014, 0.066, 1.0, 0.085, 0.017, 0.017, 1.0, 0.058, 0.004, 0.002, 0.002, 0.009, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.013, 0.009, 0.004, 0.003, 0.003, 0.006, 1.0, 0.007, 0.011, 0.03, 0.057, 0.021, 0.009], 'utility': [-0.026, 0.231, 0.081, 0.122, 0.231, -0.062, 0.326, 0.085]} reward=0.124 t=49
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 6, 0, 7, 3, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.012, 1.0, 0.005, 0.001, 0.001, 0.002, 0.015, 0.253, 0.133, 0.019, 0.01, 0.013, 0.049, 1.0, 0.235, 0.009, 0.013, 0.068, 1.0, 0.065, 0.014, 0.023, 1.0, 0.083, 0.006, 0.002, 0.003, 0.011, 0.032, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148, 1.0, 0.031, 0.053, 0.022, 0.009, 0.007, 0.011, 1.0, 0.025, 0.042, 0.213, 0.981, 0.117, 0.034], 'utility': [-0.027, 0.182, -0.059, -0.085, 0.182, 0.005, 0.087, -0.049]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.01, 1.0, 0.005, 0.001, 0.001, 0.001, 0.011, 0.256, 0.142, 0.019, 0.01, 0.013, 0.049, 1.0, 0.256, 0.009, 0.014, 0.067, 1.0, 0.074, 0.015, 0.02, 1.0, 0.069, 0.005, 0.002, 0.003, 0.01, 0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187, 1.0, 0.018, 0.019, 0.009, 0.005, 0.004, 0.007, 1.0, 0.015, 0.024, 0.092, 0.254, 0.057, 0.02], 'utility': [-0.024, 0.208, 0.086, 0.133, 0.208, -0.063, 0.234, -0.128]} reward=0.044 t=50
DEBUG:deepcomp.util.simulation:Step                           action=[2, 1, 2, 3, 0, 0, 3, 2] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.019, 0.251, 0.124, 0.018, 0.01, 0.013, 0.05, 1.0, 0.217, 0.008, 0.013, 0.07, 1.0, 0.058, 0.013, 0.026, 1.0, 0.101, 0.007, 0.003, 0.003, 0.012, 0.027, 0.007, 0.003, 0.004, 0.014, 1.0, 0.115, 1.0, 0.053, 0.155, 0.058, 0.018, 0.012, 0.017, 0.272, 0.01, 0.018, 0.111, 1.0, 0.055, 0.014], 'utility': [-0.043, 0.155, 0.097, -0.004, 0.155, 0.029, -0.066, -0.003]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.012, 1.0, 0.005, 0.001, 0.001, 0.002, 0.015, 0.253, 0.133, 0.019, 0.01, 0.013, 0.049, 1.0, 0.235, 0.009, 0.013, 0.068, 1.0, 0.065, 0.014, 0.023, 1.0, 0.083, 0.006, 0.002, 0.003, 0.011, 0.032, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148, 1.0, 0.031, 0.053, 0.022, 0.009, 0.007, 0.011, 1.0, 0.025, 0.042, 0.213, 0.981, 0.117, 0.034], 'utility': [-0.027, 0.182, -0.059, -0.085, 0.182, 0.005, 0.087, -0.049]} reward=0.03 t=51
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 0, 0, 7, 3, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.018, 1.0, 0.007, 0.002, 0.001, 0.003, 0.026, 0.248, 0.116, 0.017, 0.01, 0.013, 0.05, 1.0, 0.201, 0.008, 0.013, 0.073, 1.0, 0.052, 0.012, 0.031, 1.0, 0.123, 0.008, 0.003, 0.004, 0.013, 0.023, 0.006, 0.003, 0.003, 0.012, 1.0, 0.089, 1.0, 0.085, 0.431, 0.141, 0.032, 0.019, 0.025, 0.069, 0.004, 0.006, 0.046, 1.0, 0.021, 0.005], 'utility': [-0.031, 0.127, 0.101, 0.082, 0.127, 0.059, 0.018, 0.051]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.019, 0.251, 0.124, 0.018, 0.01, 0.013, 0.05, 1.0, 0.217, 0.008, 0.013, 0.07, 1.0, 0.058, 0.013, 0.026, 1.0, 0.101, 0.007, 0.003, 0.003, 0.012, 0.027, 0.007, 0.003, 0.004, 0.014, 1.0, 0.115, 1.0, 0.053, 0.155, 0.058, 0.018, 0.012, 0.017, 0.272, 0.01, 0.018, 0.111, 1.0, 0.055, 0.014], 'utility': [-0.043, 0.155, 0.097, -0.004, 0.155, 0.029, -0.066, -0.003]} reward=0.051 t=52
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 3, 0, 7, 3, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.021, 1.0, 0.008, 0.002, 0.002, 0.003, 0.034, 0.247, 0.109, 0.017, 0.01, 0.013, 0.051, 1.0, 0.188, 0.008, 0.013, 0.076, 1.0, 0.047, 0.011, 0.036, 1.0, 0.151, 0.009, 0.004, 0.004, 0.014, 0.019, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068, 0.894, 0.111, 1.0, 0.286, 0.047, 0.025, 0.032, 0.016, 0.001, 0.002, 0.015, 1.0, 0.007, 0.001], 'utility': [-0.042, 0.099, 0.105, 0.134, 0.099, 0.112, -0.24, 0.111]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.018, 1.0, 0.007, 0.002, 0.001, 0.003, 0.026, 0.248, 0.116, 0.017, 0.01, 0.013, 0.05, 1.0, 0.201, 0.008, 0.013, 0.073, 1.0, 0.052, 0.012, 0.031, 1.0, 0.123, 0.008, 0.003, 0.004, 0.013, 0.023, 0.006, 0.003, 0.003, 0.012, 1.0, 0.089, 1.0, 0.085, 0.431, 0.141, 0.032, 0.019, 0.025, 0.069, 0.004, 0.006, 0.046, 1.0, 0.021, 0.005], 'utility': [-0.031, 0.127, 0.101, 0.082, 0.127, 0.059, 0.018, 0.051]} reward=0.05 t=53
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 3, 0, 7, 3, 0] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.025, 1.0, 0.01, 0.002, 0.002, 0.004, 0.045, 0.245, 0.103, 0.016, 0.009, 0.013, 0.052, 1.0, 0.177, 0.007, 0.013, 0.081, 1.0, 0.043, 0.01, 0.042, 1.0, 0.186, 0.011, 0.004, 0.005, 0.016, 0.016, 0.004, 0.002, 0.002, 0.009, 1.0, 0.052, 0.376, 0.064, 1.0, 0.252, 0.03, 0.014, 0.018, 0.004, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [-0.034, 0.069, 0.109, 0.159, 0.069, 0.15, 0.052, 0.139]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.021, 1.0, 0.008, 0.002, 0.002, 0.003, 0.034, 0.247, 0.109, 0.017, 0.01, 0.013, 0.051, 1.0, 0.188, 0.008, 0.013, 0.076, 1.0, 0.047, 0.011, 0.036, 1.0, 0.151, 0.009, 0.004, 0.004, 0.014, 0.019, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068, 0.894, 0.111, 1.0, 0.286, 0.047, 0.025, 0.032, 0.016, 0.001, 0.002, 0.015, 1.0, 0.007, 0.001], 'utility': [-0.042, 0.099, 0.105, 0.134, 0.099, 0.112, -0.24, 0.111]} reward=0.079 t=54
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 3, 0, 7, 6, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.03, 1.0, 0.011, 0.003, 0.002, 0.005, 0.06, 0.244, 0.097, 0.016, 0.009, 0.013, 0.053, 1.0, 0.167, 0.007, 0.013, 0.086, 1.0, 0.04, 0.01, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.013, 0.003, 0.001, 0.002, 0.007, 1.0, 0.039, 0.179, 0.039, 1.0, 0.23, 0.021, 0.009, 0.011, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.042, 0.04, 0.112, 0.189, 0.04, 0.206, 0.079, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.025, 1.0, 0.01, 0.002, 0.002, 0.004, 0.045, 0.245, 0.103, 0.016, 0.009, 0.013, 0.052, 1.0, 0.177, 0.007, 0.013, 0.081, 1.0, 0.043, 0.01, 0.042, 1.0, 0.186, 0.011, 0.004, 0.005, 0.016, 0.016, 0.004, 0.002, 0.002, 0.009, 1.0, 0.052, 0.376, 0.064, 1.0, 0.252, 0.03, 0.014, 0.018, 0.004, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [-0.034, 0.069, 0.109, 0.159, 0.069, 0.15, 0.052, 0.139]} reward=-0.052 t=55
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 5, 3, 0, 4, 6, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.079, 0.243, 0.092, 0.015, 0.009, 0.013, 0.054, 1.0, 0.159, 0.007, 0.013, 0.093, 1.0, 0.037, 0.01, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.01, 0.002, 0.001, 0.001, 0.006, 1.0, 0.028, 0.101, 0.027, 1.0, 0.226, 0.016, 0.007, 0.008, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.037, 0.027, 0.115, 0.177, 0.027, 0.253, 0.118, 0.143]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.03, 1.0, 0.011, 0.003, 0.002, 0.005, 0.06, 0.244, 0.097, 0.016, 0.009, 0.013, 0.053, 1.0, 0.167, 0.007, 0.013, 0.086, 1.0, 0.04, 0.01, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.013, 0.003, 0.001, 0.002, 0.007, 1.0, 0.039, 0.179, 0.039, 1.0, 0.23, 0.021, 0.009, 0.011, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.042, 0.04, 0.112, 0.189, 0.04, 0.206, 0.079, -1.0]} reward=0.095 t=56
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 3, 0, 0, 6, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 1.0, 0.014, 0.004, 0.003, 0.007, 0.103, 0.242, 0.087, 0.015, 0.009, 0.013, 0.056, 1.0, 0.153, 0.007, 0.013, 0.102, 1.0, 0.035, 0.009, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.008, 0.002, 0.001, 0.001, 0.005, 1.0, 0.021, 0.07, 0.022, 1.0, 0.247, 0.014, 0.006, 0.006, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.043, 0.014, 0.118, 0.173, 0.014, 0.314, 0.12, 0.14]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.079, 0.243, 0.092, 0.015, 0.009, 0.013, 0.054, 1.0, 0.159, 0.007, 0.013, 0.093, 1.0, 0.037, 0.01, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.01, 0.002, 0.001, 0.001, 0.006, 1.0, 0.028, 0.101, 0.027, 1.0, 0.226, 0.016, 0.007, 0.008, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.037, 0.027, 0.115, 0.177, 0.027, 0.253, 0.118, 0.143]} reward=0.103 t=57
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 3, 0, 0, 6, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.048, 1.0, 0.016, 0.005, 0.004, 0.009, 0.134, 0.241, 0.083, 0.015, 0.009, 0.013, 0.057, 1.0, 0.149, 0.007, 0.014, 0.113, 1.0, 0.034, 0.009, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.015, 0.059, 0.021, 1.0, 0.297, 0.014, 0.006, 0.006, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.041, -0.001, 0.12, 0.168, -0.001, 0.372, 0.086, 0.136]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.041, 1.0, 0.014, 0.004, 0.003, 0.007, 0.103, 0.242, 0.087, 0.015, 0.009, 0.013, 0.056, 1.0, 0.153, 0.007, 0.013, 0.102, 1.0, 0.035, 0.009, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.008, 0.002, 0.001, 0.001, 0.005, 1.0, 0.021, 0.07, 0.022, 1.0, 0.247, 0.014, 0.006, 0.006, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.043, 0.014, 0.118, 0.173, 0.014, 0.314, 0.12, 0.14]} reward=0.106 t=58
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 3, 0, 0, 6, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.055, 1.0, 0.018, 0.005, 0.005, 0.011, 0.173, 0.241, 0.079, 0.014, 0.009, 0.013, 0.059, 1.0, 0.145, 0.007, 0.014, 0.126, 1.0, 0.032, 0.009, 0.056, 1.0, 0.265, 0.014, 0.005, 0.006, 0.019, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.01, 0.058, 0.023, 1.0, 0.376, 0.017, 0.007, 0.007, 0.003, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [-0.046, -0.024, 0.121, 0.157, -0.024, 0.442, 0.023, 0.125]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.048, 1.0, 0.016, 0.005, 0.004, 0.009, 0.134, 0.241, 0.083, 0.015, 0.009, 0.013, 0.057, 1.0, 0.149, 0.007, 0.014, 0.113, 1.0, 0.034, 0.009, 0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018, 0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.015, 0.059, 0.021, 1.0, 0.297, 0.014, 0.006, 0.006, 0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [-0.041, -0.001, 0.12, 0.168, -0.001, 0.372, 0.086, 0.136]} reward=0.105 t=59
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 3, 0, 0, 6, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.063, 1.0, 0.02, 0.006, 0.005, 0.013, 0.223, 0.241, 0.076, 0.014, 0.009, 0.014, 0.061, 1.0, 0.143, 0.007, 0.015, 0.142, 1.0, 0.032, 0.009, 0.063, 1.0, 0.306, 0.016, 0.006, 0.006, 0.02, 0.003, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007, 0.063, 0.028, 1.0, 0.476, 0.022, 0.008, 0.009, 0.006, 0.001, 0.001, 0.011, 1.0, 0.003, 0.001], 'utility': [-0.045, -0.047, 0.122, 0.14, -0.047, 0.513, -0.055, 0.108]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.055, 1.0, 0.018, 0.005, 0.005, 0.011, 0.173, 0.241, 0.079, 0.014, 0.009, 0.013, 0.059, 1.0, 0.145, 0.007, 0.014, 0.126, 1.0, 0.032, 0.009, 0.056, 1.0, 0.265, 0.014, 0.005, 0.006, 0.019, 0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.01, 0.058, 0.023, 1.0, 0.376, 0.017, 0.007, 0.007, 0.003, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [-0.046, -0.024, 0.121, 0.157, -0.024, 0.442, 0.023, 0.125]} reward=0.097 t=60
DEBUG:deepcomp.util.simulation:Step                           action=[5, 1, 4, 3, 0, 0, 6, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 1.0, 0.022, 0.007, 0.006, 0.015, 0.286, 0.242, 0.073, 0.014, 0.009, 0.014, 0.063, 1.0, 0.141, 0.008, 0.016, 0.162, 1.0, 0.031, 0.009, 0.073, 1.0, 0.355, 0.018, 0.007, 0.007, 0.022, 0.002, 0.0, 0.0, 0.0, 0.002, 1.0, 0.004, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.012, 0.001, 0.002, 0.022, 1.0, 0.005, 0.001], 'utility': [-0.05, -0.071, 0.123, 0.083, -0.071, 0.596, -0.135, 0.083]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.063, 1.0, 0.02, 0.006, 0.005, 0.013, 0.223, 0.241, 0.076, 0.014, 0.009, 0.014, 0.061, 1.0, 0.143, 0.007, 0.015, 0.142, 1.0, 0.032, 0.009, 0.063, 1.0, 0.306, 0.016, 0.006, 0.006, 0.02, 0.003, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007, 0.063, 0.028, 1.0, 0.476, 0.022, 0.008, 0.009, 0.006, 0.001, 0.001, 0.011, 1.0, 0.003, 0.001], 'utility': [-0.045, -0.047, 0.122, 0.14, -0.047, 0.513, -0.055, 0.108]} reward=0.086 t=61
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 4, 4, 0, 0, 6, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.08, 1.0, 0.024, 0.008, 0.007, 0.018, 0.365, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.141, 0.008, 0.017, 0.186, 1.0, 0.031, 0.009, 0.083, 1.0, 0.413, 0.02, 0.007, 0.008, 0.024, 0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.003, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.023, 0.002, 0.004, 0.044, 1.0, 0.009, 0.002], 'utility': [-0.051, -0.096, 0.123, 0.099, -0.096, 0.685, -0.135, 0.051]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 1.0, 0.022, 0.007, 0.006, 0.015, 0.286, 0.242, 0.073, 0.014, 0.009, 0.014, 0.063, 1.0, 0.141, 0.008, 0.016, 0.162, 1.0, 0.031, 0.009, 0.073, 1.0, 0.355, 0.018, 0.007, 0.007, 0.022, 0.002, 0.0, 0.0, 0.0, 0.002, 1.0, 0.004, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.012, 0.001, 0.002, 0.022, 1.0, 0.005, 0.001], 'utility': [-0.05, -0.071, 0.123, 0.083, -0.071, 0.596, -0.135, 0.083]} reward=0.075 t=62
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 4, 2, 0, 0, 1, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.09, 1.0, 0.026, 0.009, 0.008, 0.021, 0.465, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.141, 0.008, 0.018, 0.216, 1.0, 0.031, 0.009, 0.097, 1.0, 0.482, 0.023, 0.008, 0.009, 0.026, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.002, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.042, 0.003, 0.007, 0.086, 1.0, 0.014, 0.004], 'utility': [-0.056, -0.12, 0.123, 0.073, -0.12, 0.789, -0.135, 0.012]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.08, 1.0, 0.024, 0.008, 0.007, 0.018, 0.365, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.141, 0.008, 0.017, 0.186, 1.0, 0.031, 0.009, 0.083, 1.0, 0.413, 0.02, 0.007, 0.008, 0.024, 0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.003, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.023, 0.002, 0.004, 0.044, 1.0, 0.009, 0.002], 'utility': [-0.051, -0.096, 0.123, 0.099, -0.096, 0.685, -0.135, 0.051]} reward=0.073 t=63
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 4, 2, 0, 0, 1, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.1, 1.0, 0.029, 0.01, 0.009, 0.025, 0.59, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.142, 0.009, 0.019, 0.251, 1.0, 0.031, 0.01, 0.112, 1.0, 0.563, 0.026, 0.009, 0.01, 0.029, 0.001, 0.0, 0.0, 0.0, 0.0, 1.0, 0.001, 0.053, 0.025, 1.0, 0.346, 0.018, 0.007, 0.008, 0.075, 0.005, 0.012, 0.162, 1.0, 0.021, 0.006], 'utility': [-0.059, -0.144, 0.123, 0.046, -0.144, 0.905, -0.028, -0.031]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.09, 1.0, 0.026, 0.009, 0.008, 0.021, 0.465, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.141, 0.008, 0.018, 0.216, 1.0, 0.031, 0.009, 0.097, 1.0, 0.482, 0.023, 0.008, 0.009, 0.026, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.002, 0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011, 0.042, 0.003, 0.007, 0.086, 1.0, 0.014, 0.004], 'utility': [-0.056, -0.12, 0.123, 0.073, -0.12, 0.789, -0.135, 0.012]} reward=0.071 t=64
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 4, 2, 0, 0, 1, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.111, 1.0, 0.031, 0.011, 0.011, 0.029, 0.745, 0.252, 0.076, 0.014, 0.009, 0.014, 0.064, 1.0, 0.144, 0.009, 0.021, 0.295, 1.0, 0.032, 0.01, 0.13, 1.0, 0.658, 0.03, 0.011, 0.011, 0.032, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.036, 0.017, 1.0, 0.183, 0.01, 0.004, 0.005, 0.129, 0.008, 0.02, 0.295, 1.0, 0.03, 0.009], 'utility': [-0.067, -0.168, 0.117, 0.021, -0.168, 1.0, 0.093, -0.078]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.1, 1.0, 0.029, 0.01, 0.009, 0.025, 0.59, 0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0, 0.142, 0.009, 0.019, 0.251, 1.0, 0.031, 0.01, 0.112, 1.0, 0.563, 0.026, 0.009, 0.01, 0.029, 0.001, 0.0, 0.0, 0.0, 0.0, 1.0, 0.001, 0.053, 0.025, 1.0, 0.346, 0.018, 0.007, 0.008, 0.075, 0.005, 0.012, 0.162, 1.0, 0.021, 0.006], 'utility': [-0.059, -0.144, 0.123, 0.046, -0.144, 0.905, -0.028, -0.031]} reward=0.083 t=65
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 4, 2, 0, 0, 1, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.122, 1.0, 0.034, 0.012, 0.012, 0.034, 0.939, 0.262, 0.081, 0.015, 0.01, 0.014, 0.064, 1.0, 0.147, 0.01, 0.023, 0.348, 1.0, 0.032, 0.01, 0.152, 1.0, 0.769, 0.034, 0.012, 0.012, 0.035, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.023, 0.011, 1.0, 0.086, 0.006, 0.002, 0.003, 0.213, 0.013, 0.032, 0.518, 1.0, 0.041, 0.014], 'utility': [-0.074, -0.192, 0.111, 0.0, -0.192, 1.0, 0.231, -0.127]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.111, 1.0, 0.031, 0.011, 0.011, 0.029, 0.745, 0.252, 0.076, 0.014, 0.009, 0.014, 0.064, 1.0, 0.144, 0.009, 0.021, 0.295, 1.0, 0.032, 0.01, 0.13, 1.0, 0.658, 0.03, 0.011, 0.011, 0.032, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.036, 0.017, 1.0, 0.183, 0.01, 0.004, 0.005, 0.129, 0.008, 0.02, 0.295, 1.0, 0.03, 0.009], 'utility': [-0.067, -0.168, 0.117, 0.021, -0.168, 1.0, 0.093, -0.078]} reward=0.094 t=66
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 4, 2, 0, 0, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.113, 0.848, 0.031, 0.011, 0.012, 0.033, 1.0, 0.273, 0.087, 0.016, 0.01, 0.015, 0.063, 1.0, 0.15, 0.01, 0.025, 0.412, 1.0, 0.033, 0.011, 0.178, 1.0, 0.898, 0.039, 0.014, 0.013, 0.038, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.014, 0.007, 1.0, 0.036, 0.003, 0.001, 0.002, 0.34, 0.02, 0.051, 0.881, 1.0, 0.054, 0.02], 'utility': [-0.085, -0.216, 0.104, -0.016, -0.216, 1.0, 0.387, -0.176]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.122, 1.0, 0.034, 0.012, 0.012, 0.034, 0.939, 0.262, 0.081, 0.015, 0.01, 0.014, 0.064, 1.0, 0.147, 0.01, 0.023, 0.348, 1.0, 0.032, 0.01, 0.152, 1.0, 0.769, 0.034, 0.012, 0.012, 0.035, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.023, 0.011, 1.0, 0.086, 0.006, 0.002, 0.003, 0.213, 0.013, 0.032, 0.518, 1.0, 0.041, 0.014], 'utility': [-0.074, -0.192, 0.111, 0.0, -0.192, 1.0, 0.231, -0.127]} reward=0.095 t=67
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 4, 2, 0, 0, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.098, 0.677, 0.027, 0.01, 0.01, 0.03, 1.0, 0.285, 0.093, 0.017, 0.01, 0.015, 0.063, 1.0, 0.153, 0.011, 0.027, 0.491, 1.0, 0.034, 0.011, 0.199, 0.955, 1.0, 0.043, 0.015, 0.014, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.008, 0.004, 1.0, 0.014, 0.001, 0.001, 0.001, 0.363, 0.02, 0.055, 1.0, 0.689, 0.048, 0.019], 'utility': [-0.089, -0.239, 0.098, -0.026, -0.239, 1.0, 0.55, -0.225]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.113, 0.848, 0.031, 0.011, 0.012, 0.033, 1.0, 0.273, 0.087, 0.016, 0.01, 0.015, 0.063, 1.0, 0.15, 0.01, 0.025, 0.412, 1.0, 0.033, 0.011, 0.178, 1.0, 0.898, 0.039, 0.014, 0.013, 0.038, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.014, 0.007, 1.0, 0.036, 0.003, 0.001, 0.002, 0.34, 0.02, 0.051, 0.881, 1.0, 0.054, 0.02], 'utility': [-0.085, -0.216, 0.104, -0.016, -0.216, 1.0, 0.387, -0.176]} reward=0.098 t=68
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 4, 2, 0, 0, 0, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.085, 0.542, 0.023, 0.009, 0.009, 0.027, 1.0, 0.297, 0.101, 0.018, 0.011, 0.015, 0.063, 1.0, 0.157, 0.012, 0.03, 0.586, 1.0, 0.035, 0.012, 0.201, 0.822, 1.0, 0.043, 0.014, 0.014, 0.038, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.005, 0.003, 1.0, 0.007, 0.001, 0.0, 0.001, 0.343, 0.018, 0.053, 1.0, 0.433, 0.038, 0.016], 'utility': [-0.061, -0.262, 0.091, -0.12, -0.262, 1.0, 0.676, -0.064]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.098, 0.677, 0.027, 0.01, 0.01, 0.03, 1.0, 0.285, 0.093, 0.017, 0.01, 0.015, 0.063, 1.0, 0.153, 0.011, 0.027, 0.491, 1.0, 0.034, 0.011, 0.199, 0.955, 1.0, 0.043, 0.015, 0.014, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.008, 0.004, 1.0, 0.014, 0.001, 0.001, 0.001, 0.363, 0.02, 0.055, 1.0, 0.689, 0.048, 0.019], 'utility': [-0.089, -0.239, 0.098, -0.026, -0.239, 1.0, 0.55, -0.225]} reward=0.114 t=69
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 2, 2, 0, 0, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.074, 0.436, 0.02, 0.008, 0.008, 0.025, 1.0, 0.31, 0.109, 0.019, 0.011, 0.016, 0.063, 1.0, 0.162, 0.012, 0.032, 0.701, 1.0, 0.036, 0.013, 0.204, 0.71, 1.0, 0.043, 0.014, 0.013, 0.036, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.006, 0.004, 1.0, 0.005, 0.001, 0.0, 0.001, 0.327, 0.017, 0.052, 1.0, 0.283, 0.03, 0.014], 'utility': [0.009, -0.285, 0.083, -0.13, -0.285, 1.0, 0.687, -0.056]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.085, 0.542, 0.023, 0.009, 0.009, 0.027, 1.0, 0.297, 0.101, 0.018, 0.011, 0.015, 0.063, 1.0, 0.157, 0.012, 0.03, 0.586, 1.0, 0.035, 0.012, 0.201, 0.822, 1.0, 0.043, 0.014, 0.014, 0.038, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.005, 0.003, 1.0, 0.007, 0.001, 0.0, 0.001, 0.343, 0.018, 0.053, 1.0, 0.433, 0.038, 0.016], 'utility': [-0.061, -0.262, 0.091, -0.12, -0.262, 1.0, 0.676, -0.064]} reward=0.125 t=70
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 2, 2, 0, 0, 0, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.323, 0.117, 0.02, 0.011, 0.016, 0.063, 1.0, 0.166, 0.013, 0.036, 0.839, 1.0, 0.037, 0.013, 0.208, 0.615, 1.0, 0.043, 0.014, 0.013, 0.034, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.012, 0.008, 1.0, 0.007, 0.001, 0.001, 0.001, 0.315, 0.016, 0.053, 1.0, 0.194, 0.025, 0.013], 'utility': [0.027, -0.297, 0.075, 0.037, -0.297, 1.0, 0.575, -0.102]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.074, 0.436, 0.02, 0.008, 0.008, 0.025, 1.0, 0.31, 0.109, 0.019, 0.011, 0.016, 0.063, 1.0, 0.162, 0.012, 0.032, 0.701, 1.0, 0.036, 0.013, 0.204, 0.71, 1.0, 0.043, 0.014, 0.013, 0.036, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.006, 0.004, 1.0, 0.005, 0.001, 0.0, 0.001, 0.327, 0.017, 0.052, 1.0, 0.283, 0.03, 0.014], 'utility': [0.009, -0.285, 0.083, -0.13, -0.285, 1.0, 0.687, -0.056]} reward=0.128 t=71
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 2, 1, 0, 4, 0, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.338, 0.127, 0.021, 0.012, 0.017, 0.063, 1.0, 0.17, 0.014, 0.039, 1.0, 0.993, 0.039, 0.014, 0.213, 0.536, 1.0, 0.043, 0.014, 0.013, 0.033, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.028, 0.023, 1.0, 0.012, 0.002, 0.002, 0.003, 0.31, 0.015, 0.057, 1.0, 0.139, 0.021, 0.012], 'utility': [0.027, -0.306, 0.068, 0.03, -0.306, 1.0, 0.414, -0.08]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.323, 0.117, 0.02, 0.011, 0.016, 0.063, 1.0, 0.166, 0.013, 0.036, 0.839, 1.0, 0.037, 0.013, 0.208, 0.615, 1.0, 0.043, 0.014, 0.013, 0.034, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.012, 0.008, 1.0, 0.007, 0.001, 0.001, 0.001, 0.315, 0.016, 0.053, 1.0, 0.194, 0.025, 0.013], 'utility': [0.027, -0.297, 0.075, 0.037, -0.297, 1.0, 0.575, -0.102]} reward=0.127 t=72
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 2, 1, 0, 4, 0, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.353, 0.138, 0.022, 0.012, 0.017, 0.063, 1.0, 0.146, 0.013, 0.035, 1.0, 0.828, 0.034, 0.012, 0.219, 0.47, 1.0, 0.043, 0.014, 0.012, 0.031, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.064, 0.069, 1.0, 0.02, 0.005, 0.004, 0.007, 0.312, 0.016, 0.064, 1.0, 0.106, 0.018, 0.011], 'utility': [0.019, -0.315, 0.059, 0.025, -0.315, 1.0, 0.256, -0.067]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.338, 0.127, 0.021, 0.012, 0.017, 0.063, 1.0, 0.17, 0.014, 0.039, 1.0, 0.993, 0.039, 0.014, 0.213, 0.536, 1.0, 0.043, 0.014, 0.013, 0.033, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.028, 0.023, 1.0, 0.012, 0.002, 0.002, 0.003, 0.31, 0.015, 0.057, 1.0, 0.139, 0.021, 0.012], 'utility': [0.027, -0.306, 0.068, 0.03, -0.306, 1.0, 0.414, -0.08]} reward=0.106 t=73
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 2, 1, 0, 4, 0, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.075, 0.404, 0.019, 0.007, 0.008, 0.024, 1.0, 0.368, 0.15, 0.023, 0.013, 0.017, 0.064, 1.0, 0.126, 0.011, 0.032, 1.0, 0.69, 0.029, 0.011, 0.227, 0.414, 1.0, 0.044, 0.014, 0.012, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.132, 0.196, 1.0, 0.032, 0.009, 0.007, 0.017, 0.322, 0.017, 0.076, 1.0, 0.086, 0.017, 0.011], 'utility': [0.013, -0.321, 0.051, 0.021, -0.321, 0.942, 0.114, -0.065]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0, 0.353, 0.138, 0.022, 0.012, 0.017, 0.063, 1.0, 0.146, 0.013, 0.035, 1.0, 0.828, 0.034, 0.012, 0.219, 0.47, 1.0, 0.043, 0.014, 0.012, 0.031, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.064, 0.069, 1.0, 0.02, 0.005, 0.004, 0.007, 0.312, 0.016, 0.064, 1.0, 0.106, 0.018, 0.011], 'utility': [0.019, -0.315, 0.059, 0.025, -0.315, 1.0, 0.256, -0.067]} reward=0.083 t=74
DEBUG:deepcomp.util.simulation:Step                           action=[1, 1, 2, 1, 0, 4, 0, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.08, 0.4, 0.019, 0.008, 0.008, 0.025, 1.0, 0.384, 0.163, 0.025, 0.014, 0.018, 0.064, 1.0, 0.109, 0.01, 0.03, 1.0, 0.576, 0.025, 0.01, 0.236, 0.367, 1.0, 0.045, 0.014, 0.012, 0.029, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.242, 0.537, 1.0, 0.046, 0.015, 0.014, 0.035, 0.34, 0.019, 0.097, 1.0, 0.074, 0.017, 0.012], 'utility': [0.007, -0.328, 0.042, 0.019, -0.328, 0.821, -0.01, -0.073]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.075, 0.404, 0.019, 0.007, 0.008, 0.024, 1.0, 0.368, 0.15, 0.023, 0.013, 0.017, 0.064, 1.0, 0.126, 0.011, 0.032, 1.0, 0.69, 0.029, 0.011, 0.227, 0.414, 1.0, 0.044, 0.014, 0.012, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.132, 0.196, 1.0, 0.032, 0.009, 0.007, 0.017, 0.322, 0.017, 0.076, 1.0, 0.086, 0.017, 0.011], 'utility': [0.013, -0.321, 0.051, 0.021, -0.321, 0.942, 0.114, -0.065]} reward=0.054 t=75
DEBUG:deepcomp.util.simulation:Step                           action=[7, 1, 2, 1, 0, 4, 0, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.087, 0.398, 0.02, 0.008, 0.008, 0.025, 1.0, 0.401, 0.177, 0.026, 0.014, 0.019, 0.065, 1.0, 0.094, 0.009, 0.027, 1.0, 0.482, 0.022, 0.009, 0.248, 0.328, 1.0, 0.047, 0.014, 0.012, 0.028, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001, 0.269, 1.0, 0.682, 0.043, 0.016, 0.016, 0.046, 0.368, 0.023, 0.13, 1.0, 0.067, 0.017, 0.013], 'utility': [0.004, -0.336, 0.034, 0.018, -0.336, 0.714, -0.119, -0.092]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.08, 0.4, 0.019, 0.008, 0.008, 0.025, 1.0, 0.384, 0.163, 0.025, 0.014, 0.018, 0.064, 1.0, 0.109, 0.01, 0.03, 1.0, 0.576, 0.025, 0.01, 0.236, 0.367, 1.0, 0.045, 0.014, 0.012, 0.029, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.242, 0.537, 1.0, 0.046, 0.015, 0.014, 0.035, 0.34, 0.019, 0.097, 1.0, 0.074, 0.017, 0.012], 'utility': [0.007, -0.328, 0.042, 0.019, -0.328, 0.821, -0.01, -0.073]} reward=0.019 t=76
DEBUG:deepcomp.util.simulation:Step                           action=[7, 3, 2, 1, 0, 4, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.097, 0.399, 0.02, 0.008, 0.009, 0.026, 1.0, 0.419, 0.193, 0.028, 0.015, 0.019, 0.065, 1.0, 0.081, 0.008, 0.025, 1.0, 0.404, 0.019, 0.008, 0.262, 0.296, 1.0, 0.049, 0.014, 0.012, 0.028, 0.002, 0.0, 0.0, 0.0, 0.003, 1.0, 0.001, 0.142, 1.0, 0.244, 0.02, 0.008, 0.009, 0.031, 0.403, 0.028, 0.184, 1.0, 0.064, 0.018, 0.014], 'utility': [0.0, -0.346, 0.025, 0.019, -0.346, 0.621, -0.215, -0.119]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.087, 0.398, 0.02, 0.008, 0.008, 0.025, 1.0, 0.401, 0.177, 0.026, 0.014, 0.019, 0.065, 1.0, 0.094, 0.009, 0.027, 1.0, 0.482, 0.022, 0.009, 0.248, 0.328, 1.0, 0.047, 0.014, 0.012, 0.028, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001, 0.269, 1.0, 0.682, 0.043, 0.016, 0.016, 0.046, 0.368, 0.023, 0.13, 1.0, 0.067, 0.017, 0.013], 'utility': [0.004, -0.336, 0.034, 0.018, -0.336, 0.714, -0.119, -0.092]} reward=-0.014 t=77
DEBUG:deepcomp.util.simulation:Step                           action=[7, 3, 4, 1, 0, 4, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.11, 0.403, 0.021, 0.009, 0.009, 0.028, 1.0, 0.437, 0.211, 0.03, 0.016, 0.02, 0.066, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.278, 0.268, 1.0, 0.051, 0.015, 0.012, 0.027, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.065, 1.0, 0.082, 0.008, 0.004, 0.005, 0.018, 0.444, 0.036, 0.273, 1.0, 0.064, 0.019, 0.017], 'utility': [-0.002, -0.357, 0.016, 0.019, -0.357, 0.537, -1.0, -0.152]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.097, 0.399, 0.02, 0.008, 0.009, 0.026, 1.0, 0.419, 0.193, 0.028, 0.015, 0.019, 0.065, 1.0, 0.081, 0.008, 0.025, 1.0, 0.404, 0.019, 0.008, 0.262, 0.296, 1.0, 0.049, 0.014, 0.012, 0.028, 0.002, 0.0, 0.0, 0.0, 0.003, 1.0, 0.001, 0.142, 1.0, 0.244, 0.02, 0.008, 0.009, 0.031, 0.403, 0.028, 0.184, 1.0, 0.064, 0.018, 0.014], 'utility': [0.0, -0.346, 0.025, 0.019, -0.346, 0.621, -0.215, -0.119]} reward=-0.045 t=78
DEBUG:deepcomp.util.simulation:Step                           action=[7, 3, 3, 1, 7, 0, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.128, 0.409, 0.023, 0.009, 0.01, 0.03, 1.0, 0.456, 0.231, 0.032, 0.016, 0.02, 0.067, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.298, 0.245, 1.0, 0.054, 0.015, 0.013, 0.027, 0.003, 0.0, 0.0, 0.001, 0.007, 1.0, 0.002, 0.025, 1.0, 0.025, 0.003, 0.002, 0.002, 0.009, 0.491, 0.047, 0.421, 1.0, 0.065, 0.021, 0.02], 'utility': [-0.005, -0.369, 0.007, 0.019, -0.369, 0.462, -1.0, -0.191]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.11, 0.403, 0.021, 0.009, 0.009, 0.028, 1.0, 0.437, 0.211, 0.03, 0.016, 0.02, 0.066, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.278, 0.268, 1.0, 0.051, 0.015, 0.012, 0.027, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.065, 1.0, 0.082, 0.008, 0.004, 0.005, 0.018, 0.444, 0.036, 0.273, 1.0, 0.064, 0.019, 0.017], 'utility': [-0.002, -0.357, 0.016, 0.019, -0.357, 0.537, -1.0, -0.152]} reward=-0.162 t=79
DEBUG:deepcomp.util.simulation:Step                           action=[7, 3, 3, 1, 7, 1, 0, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.151, 0.418, 0.025, 0.01, 0.011, 0.033, 1.0, 0.475, 0.252, 0.034, 0.017, 0.021, 0.067, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.321, 0.226, 1.0, 0.058, 0.016, 0.013, 0.027, 0.004, 0.001, 0.0, 0.001, 0.01, 1.0, 0.003, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.54, 0.061, 0.676, 1.0, 0.068, 0.024, 0.024], 'utility': [-0.006, -0.382, -0.003, 0.019, -0.382, 0.393, -1.0, -0.233]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.128, 0.409, 0.023, 0.009, 0.01, 0.03, 1.0, 0.456, 0.231, 0.032, 0.016, 0.02, 0.067, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.298, 0.245, 1.0, 0.054, 0.015, 0.013, 0.027, 0.003, 0.0, 0.0, 0.001, 0.007, 1.0, 0.002, 0.025, 1.0, 0.025, 0.003, 0.002, 0.002, 0.009, 0.491, 0.047, 0.421, 1.0, 0.065, 0.021, 0.02], 'utility': [-0.005, -0.369, 0.007, 0.019, -0.369, 0.462, -1.0, -0.191]} reward=-0.181 t=80
DEBUG:deepcomp.util.simulation:Step                           action=[7, 3, 3, 1, 7, 1, 1, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.182, 0.43, 0.028, 0.011, 0.012, 0.037, 1.0, 0.495, 0.277, 0.036, 0.018, 0.022, 0.068, 1.0, 0.1, 0.01, 0.028, 1.0, 0.539, 0.024, 0.009, 0.348, 0.21, 1.0, 0.062, 0.017, 0.013, 0.027, 0.006, 0.001, 0.001, 0.001, 0.014, 1.0, 0.004, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.527, 0.072, 1.0, 0.893, 0.064, 0.024, 0.026], 'utility': [-0.008, -0.161, -0.012, 0.017, -1.0, 0.33, -1.0, -0.277]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.151, 0.418, 0.025, 0.01, 0.011, 0.033, 1.0, 0.475, 0.252, 0.034, 0.017, 0.021, 0.067, 1.0, 0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007, 0.321, 0.226, 1.0, 0.058, 0.016, 0.013, 0.027, 0.004, 0.001, 0.0, 0.001, 0.01, 1.0, 0.003, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.54, 0.061, 0.676, 1.0, 0.068, 0.024, 0.024], 'utility': [-0.006, -0.382, -0.003, 0.019, -0.382, 0.393, -1.0, -0.233]} reward=-0.199 t=81
DEBUG:deepcomp.util.simulation:Step                           action=[7, 3, 2, 1, 3, 1, 3, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.223, 0.443, 0.031, 0.013, 0.014, 0.041, 1.0, 0.515, 0.303, 0.038, 0.019, 0.022, 0.069, 1.0, 0.126, 0.011, 0.033, 1.0, 0.742, 0.03, 0.011, 0.379, 0.197, 1.0, 0.067, 0.018, 0.014, 0.027, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.333, 0.056, 1.0, 0.521, 0.04, 0.016, 0.018], 'utility': [-0.021, -0.382, 0.016, 0.021, 0.029, 0.311, -1.0, -0.321]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.182, 0.43, 0.028, 0.011, 0.012, 0.037, 1.0, 0.495, 0.277, 0.036, 0.018, 0.022, 0.068, 1.0, 0.1, 0.01, 0.028, 1.0, 0.539, 0.024, 0.009, 0.348, 0.21, 1.0, 0.062, 0.017, 0.013, 0.027, 0.006, 0.001, 0.001, 0.001, 0.014, 1.0, 0.004, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.527, 0.072, 1.0, 0.893, 0.064, 0.024, 0.026], 'utility': [-0.008, -0.161, -0.012, 0.017, -1.0, 0.33, -1.0, -0.277]} reward=-0.158 t=82
DEBUG:deepcomp.util.simulation:Step                           action=[2, 7, 5, 7, 4, 1, 3, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.279, 0.459, 0.035, 0.015, 0.016, 0.047, 1.0, 0.536, 0.333, 0.041, 0.02, 0.023, 0.07, 1.0, 0.155, 0.013, 0.037, 0.978, 1.0, 0.037, 0.013, 0.416, 0.186, 1.0, 0.073, 0.019, 0.014, 0.028, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.053, 1.0, 0.061, 0.007, 0.003, 0.004, 0.016, 0.201, 0.041, 1.0, 0.293, 0.024, 0.01, 0.012], 'utility': [-0.027, -0.092, -0.108, 0.031, 0.024, 0.318, -1.0, -0.366]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.223, 0.443, 0.031, 0.013, 0.014, 0.041, 1.0, 0.515, 0.303, 0.038, 0.019, 0.022, 0.069, 1.0, 0.126, 0.011, 0.033, 1.0, 0.742, 0.03, 0.011, 0.379, 0.197, 1.0, 0.067, 0.018, 0.014, 0.027, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008, 0.333, 0.056, 1.0, 0.521, 0.04, 0.016, 0.018], 'utility': [-0.021, -0.382, 0.016, 0.021, 0.029, 0.311, -1.0, -0.321]} reward=-0.145 t=83
DEBUG:deepcomp.util.simulation:Step                           action=[2, 3, 3, 4, 7, 1, 3, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.354, 0.477, 0.04, 0.017, 0.019, 0.054, 1.0, 0.558, 0.366, 0.043, 0.021, 0.024, 0.071, 1.0, 0.141, 0.012, 0.031, 0.708, 1.0, 0.034, 0.012, 0.459, 0.177, 1.0, 0.081, 0.021, 0.015, 0.028, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.125, 1.0, 0.185, 0.017, 0.007, 0.008, 0.028, 0.115, 0.029, 1.0, 0.158, 0.014, 0.006, 0.008], 'utility': [-0.023, -0.105, -0.114, -0.019, 0.018, 0.313, -1.0, -0.259]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.279, 0.459, 0.035, 0.015, 0.016, 0.047, 1.0, 0.536, 0.333, 0.041, 0.02, 0.023, 0.07, 1.0, 0.155, 0.013, 0.037, 0.978, 1.0, 0.037, 0.013, 0.416, 0.186, 1.0, 0.073, 0.019, 0.014, 0.028, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.053, 1.0, 0.061, 0.007, 0.003, 0.004, 0.016, 0.201, 0.041, 1.0, 0.293, 0.024, 0.01, 0.012], 'utility': [-0.027, -0.092, -0.108, 0.031, 0.024, 0.318, -1.0, -0.366]} reward=-0.145 t=84
DEBUG:deepcomp.util.simulation:Step                           action=[2, 3, 3, 4, 7, 1, 3, 6] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.456, 0.495, 0.046, 0.02, 0.022, 0.062, 1.0, 0.579, 0.403, 0.046, 0.022, 0.025, 0.072, 1.0, 0.127, 0.01, 0.025, 0.512, 1.0, 0.031, 0.01, 0.509, 0.17, 1.0, 0.089, 0.022, 0.016, 0.029, 0.005, 0.001, 0.001, 0.001, 0.011, 1.0, 0.003, 0.251, 1.0, 0.518, 0.037, 0.014, 0.015, 0.044, 0.062, 0.019, 1.0, 0.081, 0.008, 0.004, 0.005], 'utility': [-0.067, -0.119, -0.121, 0.108, -0.026, 0.425, -0.56, -1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.354, 0.477, 0.04, 0.017, 0.019, 0.054, 1.0, 0.558, 0.366, 0.043, 0.021, 0.024, 0.071, 1.0, 0.141, 0.012, 0.031, 0.708, 1.0, 0.034, 0.012, 0.459, 0.177, 1.0, 0.081, 0.021, 0.015, 0.028, 0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004, 0.125, 1.0, 0.185, 0.017, 0.007, 0.008, 0.028, 0.115, 0.029, 1.0, 0.158, 0.014, 0.006, 0.008], 'utility': [-0.023, -0.105, -0.114, -0.019, 0.018, 0.313, -1.0, -0.259]} reward=-0.192 t=85
DEBUG:deepcomp.util.simulation:Step                           action=[2, 3, 3, 7, 4, 1, 1, 3] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.596, 0.515, 0.053, 0.023, 0.026, 0.072, 1.0, 0.602, 0.444, 0.049, 0.023, 0.025, 0.073, 1.0, 0.114, 0.009, 0.021, 0.371, 1.0, 0.028, 0.009, 0.566, 0.164, 1.0, 0.1, 0.024, 0.017, 0.03, 0.003, 0.001, 0.0, 0.001, 0.007, 1.0, 0.002, 0.319, 0.722, 1.0, 0.055, 0.018, 0.017, 0.045, 0.031, 0.012, 1.0, 0.038, 0.004, 0.002, 0.003], 'utility': [-0.031, -0.135, -0.128, 0.124, -0.262, 0.472, -0.149, -0.227]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.456, 0.495, 0.046, 0.02, 0.022, 0.062, 1.0, 0.579, 0.403, 0.046, 0.022, 0.025, 0.072, 1.0, 0.127, 0.01, 0.025, 0.512, 1.0, 0.031, 0.01, 0.509, 0.17, 1.0, 0.089, 0.022, 0.016, 0.029, 0.005, 0.001, 0.001, 0.001, 0.011, 1.0, 0.003, 0.251, 1.0, 0.518, 0.037, 0.014, 0.015, 0.044, 0.062, 0.019, 1.0, 0.081, 0.008, 0.004, 0.005], 'utility': [-0.067, -0.119, -0.121, 0.108, -0.026, 0.425, -0.56, -1.0]} reward=-0.132 t=86
DEBUG:deepcomp.util.simulation:Step                           action=[1, 3, 4, 2, 4, 2, 6, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.79, 0.536, 0.061, 0.028, 0.031, 0.084, 1.0, 0.624, 0.489, 0.053, 0.024, 0.026, 0.074, 1.0, 0.102, 0.007, 0.017, 0.269, 1.0, 0.026, 0.008, 0.632, 0.159, 1.0, 0.112, 0.027, 0.018, 0.031, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.191, 0.274, 1.0, 0.04, 0.012, 0.01, 0.023, 0.014, 0.006, 1.0, 0.016, 0.002, 0.001, 0.001], 'utility': [-0.06, -0.15, -0.135, 0.146, -0.438, 0.572, -0.406, 0.445]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.596, 0.515, 0.053, 0.023, 0.026, 0.072, 1.0, 0.602, 0.444, 0.049, 0.023, 0.025, 0.073, 1.0, 0.114, 0.009, 0.021, 0.371, 1.0, 0.028, 0.009, 0.566, 0.164, 1.0, 0.1, 0.024, 0.017, 0.03, 0.003, 0.001, 0.0, 0.001, 0.007, 1.0, 0.002, 0.319, 0.722, 1.0, 0.055, 0.018, 0.017, 0.045, 0.031, 0.012, 1.0, 0.038, 0.004, 0.002, 0.003], 'utility': [-0.031, -0.135, -0.128, 0.124, -0.262, 0.472, -0.149, -0.227]} reward=-0.042 t=87
DEBUG:deepcomp.util.simulation:Step                           action=[1, 3, 4, 2, 4, 2, 1, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.525, 0.067, 0.031, 0.034, 0.093, 0.942, 0.647, 0.54, 0.056, 0.025, 0.027, 0.076, 1.0, 0.091, 0.006, 0.014, 0.196, 1.0, 0.024, 0.007, 0.707, 0.156, 1.0, 0.126, 0.029, 0.019, 0.032, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.104, 0.104, 1.0, 0.028, 0.007, 0.005, 0.011, 0.005, 0.003, 1.0, 0.006, 0.001, 0.0, 0.001], 'utility': [-0.009, -0.167, -0.142, 0.171, -0.298, 0.545, 0.062, 0.278]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 0.79, 0.536, 0.061, 0.028, 0.031, 0.084, 1.0, 0.624, 0.489, 0.053, 0.024, 0.026, 0.074, 1.0, 0.102, 0.007, 0.017, 0.269, 1.0, 0.026, 0.008, 0.632, 0.159, 1.0, 0.112, 0.027, 0.018, 0.031, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.191, 0.274, 1.0, 0.04, 0.012, 0.01, 0.023, 0.014, 0.006, 1.0, 0.016, 0.002, 0.001, 0.001], 'utility': [-0.06, -0.15, -0.135, 0.146, -0.438, 0.572, -0.406, 0.445]} reward=-0.003 t=88
DEBUG:deepcomp.util.simulation:Step                           action=[1, 3, 4, 2, 4, 2, 1, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.4, 0.058, 0.027, 0.03, 0.08, 0.692, 0.67, 0.596, 0.06, 0.026, 0.028, 0.077, 1.0, 0.082, 0.005, 0.012, 0.144, 1.0, 0.022, 0.006, 0.792, 0.153, 1.0, 0.143, 0.033, 0.021, 0.033, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.052, 0.04, 1.0, 0.019, 0.004, 0.003, 0.005, 0.002, 0.001, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [-0.039, -0.184, -0.15, 0.199, -0.455, 0.575, -0.11, 0.852]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.525, 0.067, 0.031, 0.034, 0.093, 0.942, 0.647, 0.54, 0.056, 0.025, 0.027, 0.076, 1.0, 0.091, 0.006, 0.014, 0.196, 1.0, 0.024, 0.007, 0.707, 0.156, 1.0, 0.126, 0.029, 0.019, 0.032, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.104, 0.104, 1.0, 0.028, 0.007, 0.005, 0.011, 0.005, 0.003, 1.0, 0.006, 0.001, 0.0, 0.001], 'utility': [-0.009, -0.167, -0.142, 0.171, -0.298, 0.545, 0.062, 0.278]} reward=0.055 t=89
DEBUG:deepcomp.util.simulation:Step                           action=[1, 3, 4, 2, 4, 2, 1, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.3, 0.049, 0.024, 0.026, 0.068, 0.501, 0.693, 0.659, 0.064, 0.027, 0.029, 0.078, 1.0, 0.073, 0.005, 0.01, 0.106, 1.0, 0.02, 0.006, 0.888, 0.151, 1.0, 0.163, 0.036, 0.023, 0.035, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.026, 0.016, 1.0, 0.013, 0.002, 0.001, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.014, -0.201, -0.158, 0.228, -0.356, 0.551, 0.269, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.4, 0.058, 0.027, 0.03, 0.08, 0.692, 0.67, 0.596, 0.06, 0.026, 0.028, 0.077, 1.0, 0.082, 0.005, 0.012, 0.144, 1.0, 0.022, 0.006, 0.792, 0.153, 1.0, 0.143, 0.033, 0.021, 0.033, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.052, 0.04, 1.0, 0.019, 0.004, 0.003, 0.005, 0.002, 0.001, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [-0.039, -0.184, -0.15, 0.199, -0.455, 0.575, -0.11, 0.852]} reward=0.086 t=90
DEBUG:deepcomp.util.simulation:Step                           action=[1, 3, 4, 2, 4, 2, 1, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.222, 0.041, 0.02, 0.023, 0.057, 0.358, 0.717, 0.729, 0.068, 0.029, 0.03, 0.079, 1.0, 0.066, 0.004, 0.008, 0.08, 1.0, 0.019, 0.005, 0.996, 0.15, 1.0, 0.187, 0.04, 0.025, 0.037, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001, 0.015, 0.008, 1.0, 0.011, 0.002, 0.001, 0.001, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.105, -0.344, -0.065, 0.24, -0.742, 0.742, -0.187, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.3, 0.049, 0.024, 0.026, 0.068, 0.501, 0.693, 0.659, 0.064, 0.027, 0.029, 0.078, 1.0, 0.073, 0.005, 0.01, 0.106, 1.0, 0.02, 0.006, 0.888, 0.151, 1.0, 0.163, 0.036, 0.023, 0.035, 0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002, 0.026, 0.016, 1.0, 0.013, 0.002, 0.001, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.014, -0.201, -0.158, 0.228, -0.356, 0.551, 0.269, 1.0]} reward=0.165 t=91
DEBUG:deepcomp.util.simulation:Step                           action=[1, 3, 4, 2, 4, 3, 6, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.161, 0.033, 0.017, 0.019, 0.047, 0.252, 0.74, 0.807, 0.073, 0.03, 0.031, 0.081, 1.0, 0.06, 0.003, 0.007, 0.061, 1.0, 0.018, 0.005, 1.0, 0.134, 0.896, 0.193, 0.04, 0.024, 0.035, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.012, 0.006, 1.0, 0.014, 0.002, 0.001, 0.001, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.036, -0.369, -0.061, 0.271, -0.33, 0.831, 0.295, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.222, 0.041, 0.02, 0.023, 0.057, 0.358, 0.717, 0.729, 0.068, 0.029, 0.03, 0.079, 1.0, 0.066, 0.004, 0.008, 0.08, 1.0, 0.019, 0.005, 0.996, 0.15, 1.0, 0.187, 0.04, 0.025, 0.037, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001, 0.015, 0.008, 1.0, 0.011, 0.002, 0.001, 0.001, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.105, -0.344, -0.065, 0.24, -0.742, 0.742, -0.187, 1.0]} reward=0.067 t=92
DEBUG:deepcomp.util.simulation:Step                           action=[1, 3, 4, 2, 4, 4, 6, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.115, 0.027, 0.014, 0.016, 0.038, 0.174, 0.764, 0.895, 0.078, 0.032, 0.032, 0.082, 1.0, 0.055, 0.003, 0.006, 0.047, 1.0, 0.017, 0.004, 1.0, 0.12, 0.801, 0.199, 0.041, 0.023, 0.033, 0.0, 0.0, 0.0, 0.0, 0.001, 1.0, 0.0, 0.015, 0.007, 1.0, 0.026, 0.002, 0.001, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.099, -0.395, -0.057, 0.298, -0.294, 1.0, 0.157, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.161, 0.033, 0.017, 0.019, 0.047, 0.252, 0.74, 0.807, 0.073, 0.03, 0.031, 0.081, 1.0, 0.06, 0.003, 0.007, 0.061, 1.0, 0.018, 0.005, 1.0, 0.134, 0.896, 0.193, 0.04, 0.024, 0.035, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.012, 0.006, 1.0, 0.014, 0.002, 0.001, 0.001, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.036, -0.369, -0.061, 0.271, -0.33, 0.831, 0.295, 1.0]} reward=0.2 t=93
DEBUG:deepcomp.util.simulation:Step                           action=[1, 3, 4, 2, 4, 4, 6, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.08, 0.021, 0.012, 0.013, 0.03, 0.118, 0.788, 0.992, 0.083, 0.033, 0.033, 0.083, 1.0, 0.052, 0.003, 0.005, 0.038, 1.0, 0.017, 0.004, 1.0, 0.108, 0.718, 0.207, 0.041, 0.023, 0.031, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.022, 0.009, 1.0, 0.057, 0.004, 0.002, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.041, -0.42, -0.052, 0.32, -0.339, 1.0, 0.049, 1.0]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.115, 0.027, 0.014, 0.016, 0.038, 0.174, 0.764, 0.895, 0.078, 0.032, 0.032, 0.082, 1.0, 0.055, 0.003, 0.006, 0.047, 1.0, 0.017, 0.004, 1.0, 0.12, 0.801, 0.199, 0.041, 0.023, 0.033, 0.0, 0.0, 0.0, 0.0, 0.001, 1.0, 0.0, 0.015, 0.007, 1.0, 0.026, 0.002, 0.001, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.099, -0.395, -0.057, 0.298, -0.294, 1.0, 0.157, 1.0]} reward=0.201 t=94
DEBUG:deepcomp.util.simulation:Step                           action=[1, 3, 4, 4, 4, 4, 6, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.055, 0.016, 0.009, 0.011, 0.023, 0.079, 0.737, 1.0, 0.081, 0.031, 0.031, 0.077, 0.908, 0.05, 0.003, 0.005, 0.032, 1.0, 0.018, 0.004, 1.0, 0.097, 0.646, 0.216, 0.042, 0.022, 0.029, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.033, 0.014, 1.0, 0.127, 0.008, 0.003, 0.004, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.056, -1.0, 0.013, 0.336, -0.231, 1.0, -0.003, 0.395]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.08, 0.021, 0.012, 0.013, 0.03, 0.118, 0.788, 0.992, 0.083, 0.033, 0.033, 0.083, 1.0, 0.052, 0.003, 0.005, 0.038, 1.0, 0.017, 0.004, 1.0, 0.108, 0.718, 0.207, 0.041, 0.023, 0.031, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.022, 0.009, 1.0, 0.057, 0.004, 0.002, 0.002, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.041, -0.42, -0.052, 0.32, -0.339, 1.0, 0.049, 1.0]} reward=0.19 t=95
DEBUG:deepcomp.util.simulation:Step                           action=[1, 2, 4, 2, 4, 4, 6, 4] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.036, 0.012, 0.007, 0.008, 0.017, 0.051, 0.682, 1.0, 0.077, 0.03, 0.029, 0.071, 0.817, 0.05, 0.003, 0.004, 0.027, 1.0, 0.019, 0.004, 1.0, 0.089, 0.583, 0.228, 0.042, 0.022, 0.028, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.048, 0.02, 1.0, 0.269, 0.013, 0.005, 0.006, 0.001, 0.001, 1.0, 0.001, 0.0, 0.0, 0.0], 'utility': [0.009, -1.0, 0.015, 0.344, -0.268, 1.0, -0.101, 0.07]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.055, 0.016, 0.009, 0.011, 0.023, 0.079, 0.737, 1.0, 0.081, 0.031, 0.031, 0.077, 0.908, 0.05, 0.003, 0.005, 0.032, 1.0, 0.018, 0.004, 1.0, 0.097, 0.646, 0.216, 0.042, 0.022, 0.029, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.033, 0.014, 1.0, 0.127, 0.008, 0.003, 0.004, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [-0.056, -1.0, 0.013, 0.336, -0.231, 1.0, -0.003, 0.395]} reward=0.057 t=96
DEBUG:deepcomp.util.simulation:Step                           action=[1, 2, 4, 7, 4, 4, 6, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.023, 0.009, 0.006, 0.006, 0.012, 0.032, 0.631, 1.0, 0.074, 0.028, 0.027, 0.065, 0.735, 0.051, 0.003, 0.004, 0.024, 1.0, 0.021, 0.004, 1.0, 0.081, 0.529, 0.242, 0.044, 0.022, 0.027, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.067, 0.027, 1.0, 0.516, 0.022, 0.008, 0.009, 0.003, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.003, -1.0, 0.019, 0.344, -0.275, 1.0, -0.235, 0.006]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.036, 0.012, 0.007, 0.008, 0.017, 0.051, 0.682, 1.0, 0.077, 0.03, 0.029, 0.071, 0.817, 0.05, 0.003, 0.004, 0.027, 1.0, 0.019, 0.004, 1.0, 0.089, 0.583, 0.228, 0.042, 0.022, 0.028, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.048, 0.02, 1.0, 0.269, 0.013, 0.005, 0.006, 0.001, 0.001, 1.0, 0.001, 0.0, 0.0, 0.0], 'utility': [0.009, -1.0, 0.015, 0.344, -0.268, 1.0, -0.101, 0.07]} reward=0.009 t=97
DEBUG:deepcomp.util.simulation:Step                           action=[1, 2, 4, 7, 4, 4, 6, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.014, 0.006, 0.004, 0.005, 0.008, 0.019, 0.582, 1.0, 0.071, 0.026, 0.025, 0.059, 0.66, 0.054, 0.003, 0.004, 0.023, 1.0, 0.025, 0.004, 1.0, 0.075, 0.482, 0.258, 0.045, 0.022, 0.026, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012, 0.01, 0.009, 1.0, 0.005, 0.001, 0.001, 0.001], 'utility': [0.021, -1.0, 0.023, 0.337, -0.327, 0.848, -0.308, 0.067]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.023, 0.009, 0.006, 0.006, 0.012, 0.032, 0.631, 1.0, 0.074, 0.028, 0.027, 0.065, 0.735, 0.051, 0.003, 0.004, 0.024, 1.0, 0.021, 0.004, 1.0, 0.081, 0.529, 0.242, 0.044, 0.022, 0.027, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.067, 0.027, 1.0, 0.516, 0.022, 0.008, 0.009, 0.003, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.003, -1.0, 0.019, 0.344, -0.275, 1.0, -0.235, 0.006]} reward=-0.017 t=98
DEBUG:deepcomp.util.simulation:Step                           action=[1, 2, 4, 7, 4, 4, 6, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.008, 0.004, 0.003, 0.003, 0.006, 0.011, 0.536, 1.0, 0.068, 0.025, 0.023, 0.054, 0.592, 0.058, 0.003, 0.004, 0.022, 1.0, 0.03, 0.005, 1.0, 0.07, 0.442, 0.278, 0.047, 0.022, 0.025, 0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012, 0.025, 0.021, 1.0, 0.011, 0.002, 0.001, 0.003], 'utility': [0.008, -1.0, 0.028, 0.322, -0.404, 0.724, -0.318, 0.109]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.014, 0.006, 0.004, 0.005, 0.008, 0.019, 0.582, 1.0, 0.071, 0.026, 0.025, 0.059, 0.66, 0.054, 0.003, 0.004, 0.023, 1.0, 0.025, 0.004, 1.0, 0.075, 0.482, 0.258, 0.045, 0.022, 0.026, 0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012, 0.01, 0.009, 1.0, 0.005, 0.001, 0.001, 0.001], 'utility': [0.021, -1.0, 0.023, 0.337, -0.327, 0.848, -0.308, 0.067]} reward=-0.043 t=99
DEBUG:deepcomp.util.simulation:Step                           action=[1, 2, 4, 2, 4, 4, 6, 5] done=None next_obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.005, 0.002, 0.002, 0.002, 0.003, 0.006, 0.493, 1.0, 0.065, 0.023, 0.021, 0.049, 0.531, 0.065, 0.003, 0.005, 0.022, 1.0, 0.037, 0.006, 1.0, 0.065, 0.407, 0.301, 0.049, 0.022, 0.025, 0.004, 0.0, 0.0, 0.0, 0.003, 1.0, 0.003, 0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012, 0.055, 0.043, 1.0, 0.02, 0.004, 0.003, 0.006], 'utility': [0.012, -1.0, 0.033, 0.3, -0.216, 0.588, -0.3, 0.083]} obs={'connected': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014, 1.0, 0.008, 0.004, 0.003, 0.003, 0.006, 0.011, 0.536, 1.0, 0.068, 0.025, 0.023, 0.054, 0.592, 0.058, 0.003, 0.004, 0.022, 1.0, 0.03, 0.005, 1.0, 0.07, 0.442, 0.278, 0.047, 0.022, 0.025, 0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001, 0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012, 0.025, 0.021, 1.0, 0.011, 0.002, 0.001, 0.003], 'utility': [0.008, -1.0, 0.028, 0.322, -0.404, 0.724, -0.318, 0.109]} reward=-0.039 t=100
INFO:deepcomp.util.simulation:Video saved                    path=/home/abhishek/cmc/result/DeepCoMP/decent/videos/PPO_CentralRelNormEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-25_09-38-44.html
INFO:deepcomp.util.simulation:Gif saved                      path=/home/abhishek/cmc/result/DeepCoMP/decent/videos/PPO_CentralRelNormEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-25_09-38-44.gif
DEBUG:deepcomp.util.simulation:Episode complete               avg_step_reward=-0.017 eps_duration=490.428 scalar_metrics=['sum_utility'] vector_metrics=['dr', 'utility']
INFO:deepcomp.util.simulation:Scalar results                 results={'episode': [0], 'eps_duration_mean': [490.428], 'eps_duration_std': [490.428], 'step_reward_mean': [-0.017], 'step_reward_std': [0.125], 'sum_utility_mean': [-3.337], 'sum_utility_std': [20.275]}
INFO:deepcomp.util.simulation:Mean results                   results={'episode': 0.0, 'eps_duration_mean': 490.428, 'eps_duration_std': 490.428, 'step_reward_mean': -0.017, 'step_reward_std': 0.125, 'sum_utility_mean': -3.337, 'sum_utility_std': 20.275}
INFO:deepcomp.util.simulation:Simulation complete            avg_eps_reward=-1.7 eps_length=100 num_episodes=1 step_reward_mean=-0.017 step_reward_std=0.0
INFO:deepcomp.util.simulation:Starting evaluation            fast_ues=2 num_episodes=100 num_workers=1 slow_ues=5 static_ues=1
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [04:23<00:00,  2.63s/it]
INFO:deepcomp.util.simulation:Scalar results                 results={'episode': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 'eps_duration_mean': [2.59, 2.694, 2.597, 2.443, 2.574, 3.91, 2.42, 2.412, 2.353, 2.54, 3.928, 2.378, 4.444, 2.469, 2.503, 2.647, 2.385, 2.304, 2.541, 4.177, 2.435, 2.499, 2.345, 2.476, 2.515, 2.433, 2.369, 2.415, 2.24, 2.478, 2.169, 2.578, 2.233, 2.491, 2.507, 2.572, 2.664, 2.595, 2.544, 2.634, 3.908, 2.355, 2.243, 2.615, 4.241, 2.386, 2.464, 2.306, 6.793, 2.407, 2.306, 2.422, 2.519, 2.378, 2.288, 2.456, 2.172, 2.377, 2.346, 2.35, 2.14, 2.347, 2.907, 2.709, 2.752, 6.514, 2.559, 2.448, 2.382, 2.393, 2.514, 2.389, 2.247, 2.48, 2.276, 2.537, 2.307, 2.502, 2.254, 2.691, 2.685, 2.272, 2.559, 2.319, 2.485, 2.491, 2.377, 2.444, 2.535, 2.456, 2.325, 2.461, 2.227, 2.407, 2.38, 2.431, 2.436, 2.308, 2.463, 2.635], 'eps_duration_std': [2.59, 2.694, 2.597, 2.443, 2.574, 3.91, 2.42, 2.412, 2.353, 2.54, 3.928, 2.378, 4.444, 2.469, 2.503, 2.647, 2.385, 2.304, 2.541, 4.177, 2.435, 2.499, 2.345, 2.476, 2.515, 2.433, 2.369, 2.415, 2.24, 2.478, 2.169, 2.578, 2.233, 2.491, 2.507, 2.572, 2.664, 2.595, 2.544, 2.634, 3.908, 2.355, 2.243, 2.615, 4.241, 2.386, 2.464, 2.306, 6.793, 2.407, 2.306, 2.422, 2.519, 2.378, 2.288, 2.456, 2.172, 2.377, 2.346, 2.35, 2.14, 2.347, 2.907, 2.709, 2.752, 6.514, 2.559, 2.448, 2.382, 2.393, 2.514, 2.389, 2.247, 2.48, 2.276, 2.537, 2.307, 2.502, 2.254, 2.691, 2.685, 2.272, 2.559, 2.319, 2.485, 2.491, 2.377, 2.444, 2.535, 2.456, 2.325, 2.461, 2.227, 2.407, 2.38, 2.431, 2.436, 2.308, 2.463, 2.635], 'step_reward_mean': [-0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017, -0.017], 'step_reward_std': [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], 'sum_utility_mean': [-3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337, -3.337], 'sum_utility_std': [20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275, 20.275]}
INFO:deepcomp.util.simulation:Mean results                   results={'episode': 49.5, 'eps_duration_mean': 2.629, 'eps_duration_std': 2.629, 'step_reward_mean': -0.017, 'step_reward_std': 0.125, 'sum_utility_mean': -3.337, 'sum_utility_std': 20.275}
INFO:deepcomp.util.simulation:Simulation complete            avg_eps_reward=-1.7 eps_length=100 num_episodes=100 step_reward_mean=-0.017 step_reward_std=0.0
INFO:deepcomp.util.simulation:Writing scalar results         file=/home/abhishek/cmc/result/DeepCoMP/decent/test/PPO_CentralRelNormEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-25_09-38-44.csv
INFO:deepcomp.util.simulation:Writing vector results         file=/home/abhishek/cmc/result/DeepCoMP/decent/test/PPO_CentralRelNormEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-25_09-38-44_dr.pkl metric=dr
INFO:deepcomp.util.simulation:Writing vector results         file=/home/abhishek/cmc/result/DeepCoMP/decent/test/PPO_CentralRelNormEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-25_09-38-44_utility.pkl metric=utility
INFO:deepcomp.main:Finished                       agent=/home/abhishek/cmc/result/DeepCoMP/decent/train/PPO_2022-04-25_09-26-28/PPO_CentralRelNormEnv_af4f5_00000_0_2022-04-25_09-26-28/checkpoint_000013/checkpoint-13
abhishek@abhishek-pc:~$ 
```






