```
abhishek@abhishek-pc:~$ deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent multi --workers 2 --dashboard --ue-details --eval 100 --train-steps 200000 --seed 42 --video both --result-dir /home/abhishek/cmc/result/DD-CoMP/good
2022-04-28 03:24:17,873	WARNING deprecation.py:33 -- DeprecationWarning: `monitor` has been deprecated. Use `record_env` instead. This will raise an error in the future!
== Status ==
Memory usage on this node: 1.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 PENDING)
+-------------------------------------+----------+-------+
| Trial name                          | status   | loc   |
|-------------------------------------+----------+-------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | PENDING  |       |
+-------------------------------------+----------+-------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 32000
  custom_metrics:
    eps_sum_utility_max: -4685.4584070251485
    eps_sum_utility_mean: -6156.229485382219
    eps_sum_utility_min: -7755.421692779556
    sum_utility_max: 24.45245154075271
    sum_utility_mean: -46.43957230674722
    sum_utility_min: -96.62046992860205
  date: 2022-04-28_03-25-40
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -1859.6099685231234
  episode_reward_mean: -3494.5956326153478
  episode_reward_min: -4966.083225632978
  episodes_this_iter: 40
  episodes_total: 40
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.061990261077881
          entropy_coeff: 0.0
          kl: 0.01781199872493744
          model: {}
          policy_loss: -0.019940052181482315
          total_loss: 35162.7265625
          vf_explained_var: 1.7676591596682556e-05
          vf_loss: 35162.7421875
    num_agent_steps_sampled: 32000
    num_agent_steps_trained: 32000
    num_steps_sampled: 4000
    num_steps_trained: 4000
  iterations_since_restore: 1
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.79393939393939
    ram_util_percent: 36.26767676767677
  pid: 3889
  policy_reward_max:
    ue: 304.1542621190504
  policy_reward_mean:
    ue: -436.82445407691887
  policy_reward_min:
    ue: -1038.6047304659887
  sampler_perf:
    mean_action_processing_ms: 0.1017454562933072
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 22.441688386992418
    mean_inference_ms: 0.755117095630804
    mean_raw_obs_processing_ms: 0.4899332607942245
  time_since_restore: 70.01181125640869
  time_this_iter_s: 70.01181125640869
  time_total_s: 70.01181125640869
  timers:
    learn_throughput: 183.005
    learn_time_ms: 21857.27
    load_throughput: 111179.547
    load_time_ms: 35.978
    sample_throughput: 83.144
    sample_time_ms: 48109.28
    update_time_ms: 2.335
  timestamp: 1651096540
  timesteps_since_restore: 0
  timesteps_total: 4000
  training_iteration: 1
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |   ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |      1 |          70.0118 | 4000 |  -3494.6 |             -1859.61 |             -4966.08 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 64000
  custom_metrics:
    eps_sum_utility_max: -3017.479459673959
    eps_sum_utility_mean: -5152.2184894404845
    eps_sum_utility_min: -7755.421692779556
    sum_utility_max: 24.45245154075271
    sum_utility_mean: -41.031201996692374
    sum_utility_min: -113.93509351180417
  date: 2022-04-28_03-27-00
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -640.4355849069906
  episode_reward_mean: -2717.084201786265
  episode_reward_min: -4966.083225632978
  episodes_this_iter: 40
  episodes_total: 80
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.030324697494507
          entropy_coeff: 0.0
          kl: 0.018845928832888603
          model: {}
          policy_loss: -0.02144678868353367
          total_loss: 12172.4306640625
          vf_explained_var: 0.03561444953083992
          vf_loss: 12172.4501953125
    num_agent_steps_sampled: 64000
    num_agent_steps_trained: 64000
    num_steps_sampled: 8000
    num_steps_trained: 8000
  iterations_since_restore: 2
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.99374999999999
    ram_util_percent: 36.627678571428575
  pid: 3889
  policy_reward_max:
    ue: 311.54433763876756
  policy_reward_mean:
    ue: -339.63552522328337
  policy_reward_min:
    ue: -1038.6047304659887
  sampler_perf:
    mean_action_processing_ms: 0.10390967402168845
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 23.567346960347333
    mean_inference_ms: 0.7648107442801407
    mean_raw_obs_processing_ms: 0.501512172280074
  time_since_restore: 150.12264704704285
  time_this_iter_s: 80.11083579063416
  time_total_s: 150.12264704704285
  timers:
    learn_throughput: 179.457
    learn_time_ms: 22289.48
    load_throughput: 185893.011
    load_time_ms: 21.518
    sample_throughput: 75.844
    sample_time_ms: 52740.077
    update_time_ms: 2.542
  timestamp: 1651096620
  timesteps_since_restore: 0
  timesteps_total: 8000
  training_iteration: 2
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |   ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |      2 |          150.123 | 8000 | -2717.08 |             -640.436 |             -4966.08 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 96000
  custom_metrics:
    eps_sum_utility_max: -903.5993633784835
    eps_sum_utility_mean: -3847.6568520392843
    eps_sum_utility_min: -7755.421692779556
    sum_utility_max: 25.858863361978745
    sum_utility_mean: -27.906408019564214
    sum_utility_min: -113.93509351180417
  date: 2022-04-28_03-28-32
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 82.9225426390563
  episode_reward_mean: -1762.212497349554
  episode_reward_min: -4966.083225632978
  episodes_this_iter: 40
  episodes_total: 120
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 1.9781564474105835
          entropy_coeff: 0.0
          kl: 0.02075112983584404
          model: {}
          policy_loss: -0.02023133635520935
          total_loss: 6895.08544921875
          vf_explained_var: 0.16714663803577423
          vf_loss: 6895.10107421875
    num_agent_steps_sampled: 96000
    num_agent_steps_trained: 96000
    num_steps_sampled: 12000
    num_steps_trained: 12000
  iterations_since_restore: 3
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.18828125
    ram_util_percent: 36.692968750000006
  pid: 3889
  policy_reward_max:
    ue: 383.2209246762679
  policy_reward_mean:
    ue: -220.27656216869434
  policy_reward_min:
    ue: -1038.6047304659887
  sampler_perf:
    mean_action_processing_ms: 0.10706040837809784
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 25.15808357677211
    mean_inference_ms: 0.78140361588421
    mean_raw_obs_processing_ms: 0.5171230869961646
  time_since_restore: 241.51077008247375
  time_this_iter_s: 91.38812303543091
  time_total_s: 241.51077008247375
  timers:
    learn_throughput: 174.584
    learn_time_ms: 22911.672
    load_throughput: 240178.89
    load_time_ms: 16.654
    sample_throughput: 69.501
    sample_time_ms: 57553.312
    update_time_ms: 2.855
  timestamp: 1651096712
  timesteps_since_restore: 0
  timesteps_total: 12000
  training_iteration: 3
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |      3 |          241.511 | 12000 | -1762.21 |              82.9225 |             -4966.08 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 128000
  custom_metrics:
    eps_sum_utility_max: -253.90823094692948
    eps_sum_utility_mean: -2223.465797272898
    eps_sum_utility_min: -5970.064228109271
    sum_utility_max: 28.284823279843565
    sum_utility_mean: -9.256347701091801
    sum_utility_min: -96.70896686148481
  date: 2022-04-28_03-30-09
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 550.9017387098014
  episode_reward_mean: -708.516068434452
  episode_reward_min: -3259.5156010310984
  episodes_this_iter: 40
  episodes_total: 160
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9311113357543945
          entropy_coeff: 0.0
          kl: 0.012792796827852726
          model: {}
          policy_loss: -0.014926317147910595
          total_loss: 5677.091796875
          vf_explained_var: 0.2966287136077881
          vf_loss: 5677.103515625
    num_agent_steps_sampled: 128000
    num_agent_steps_trained: 128000
    num_steps_sampled: 16000
    num_steps_trained: 16000
  iterations_since_restore: 4
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.893382352941174
    ram_util_percent: 36.71397058823529
  pid: 3889
  policy_reward_max:
    ue: 420.349216237817
  policy_reward_mean:
    ue: -88.56450855430654
  policy_reward_min:
    ue: -664.3054112298676
  sampler_perf:
    mean_action_processing_ms: 0.11095306921659377
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 27.258400837159034
    mean_inference_ms: 0.8034632090314137
    mean_raw_obs_processing_ms: 0.5375139643032302
  time_since_restore: 338.74710416793823
  time_this_iter_s: 97.23633408546448
  time_total_s: 338.74710416793823
  timers:
    learn_throughput: 170.302
    learn_time_ms: 23487.648
    load_throughput: 277405.645
    load_time_ms: 14.419
    sample_throughput: 65.397
    sample_time_ms: 61165.193
    update_time_ms: 2.852
  timestamp: 1651096809
  timesteps_since_restore: 0
  timesteps_total: 16000
  training_iteration: 4
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |      4 |          338.747 | 16000 | -708.516 |              550.902 |             -3259.52 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 160000
  custom_metrics:
    eps_sum_utility_max: 187.21909019877586
    eps_sum_utility_mean: -968.7726382806801
    eps_sum_utility_min: -2960.3391545762183
    sum_utility_max: 28.284823279843565
    sum_utility_mean: 5.303225668597184
    sum_utility_min: -86.71782647184298
  date: 2022-04-28_03-31-53
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 809.4795574253408
  episode_reward_mean: 28.860744590034578
  episode_reward_min: -1051.968049328432
  episodes_this_iter: 40
  episodes_total: 200
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.897154450416565
          entropy_coeff: 0.0
          kl: 0.010311219841241837
          model: {}
          policy_loss: -0.010826995596289635
          total_loss: 5938.02783203125
          vf_explained_var: 0.3468320369720459
          vf_loss: 5938.0361328125
    num_agent_steps_sampled: 160000
    num_agent_steps_trained: 160000
    num_steps_sampled: 20000
    num_steps_trained: 20000
  iterations_since_restore: 5
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.431724137931035
    ram_util_percent: 36.63103448275862
  pid: 3889
  policy_reward_max:
    ue: 420.349216237817
  policy_reward_mean:
    ue: 3.6075930737543285
  policy_reward_min:
    ue: -476.73074529985854
  sampler_perf:
    mean_action_processing_ms: 0.11402677625374888
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.06794701354453
    mean_inference_ms: 0.8221045190597333
    mean_raw_obs_processing_ms: 0.5534239705979765
  time_since_restore: 442.2804310321808
  time_this_iter_s: 103.53332686424255
  time_total_s: 442.2804310321808
  timers:
    learn_throughput: 165.828
    learn_time_ms: 24121.443
    load_throughput: 312810.504
    load_time_ms: 12.787
    sample_throughput: 62.205
    sample_time_ms: 64303.791
    update_time_ms: 2.862
  timestamp: 1651096913
  timesteps_since_restore: 0
  timesteps_total: 20000
  training_iteration: 5
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |      5 |           442.28 | 20000 |  28.8607 |               809.48 |             -1051.97 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 192000
  custom_metrics:
    eps_sum_utility_max: 638.8037864990213
    eps_sum_utility_mean: -271.7694364536798
    eps_sum_utility_min: -1621.2073747786094
    sum_utility_max: 28.402149706219717
    sum_utility_mean: 13.361480165665915
    sum_utility_min: -37.94772713773642
  date: 2022-04-28_03-33-42
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 862.1459187335009
  episode_reward_mean: 385.77195440868445
  episode_reward_min: -502.5022181722392
  episodes_this_iter: 40
  episodes_total: 240
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.875530481338501
          entropy_coeff: 0.0
          kl: 0.00875017885118723
          model: {}
          policy_loss: -0.008836985565721989
          total_loss: 5359.40478515625
          vf_explained_var: 0.41149526834487915
          vf_loss: 5359.4111328125
    num_agent_steps_sampled: 192000
    num_agent_steps_trained: 192000
    num_steps_sampled: 24000
    num_steps_trained: 24000
  iterations_since_restore: 6
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.15065789473684
    ram_util_percent: 36.623026315789474
  pid: 3889
  policy_reward_max:
    ue: 400.78878384402304
  policy_reward_mean:
    ue: 48.22149430108555
  policy_reward_min:
    ue: -347.5855972506295
  sampler_perf:
    mean_action_processing_ms: 0.1166840355361932
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 30.619480966449064
    mean_inference_ms: 0.8381724381553988
    mean_raw_obs_processing_ms: 0.566887465501554
  time_since_restore: 551.2626955509186
  time_this_iter_s: 108.9822645187378
  time_total_s: 551.2626955509186
  timers:
    learn_throughput: 162.586
    learn_time_ms: 24602.385
    load_throughput: 329286.774
    load_time_ms: 12.147
    sample_throughput: 59.484
    sample_time_ms: 67245.459
    update_time_ms: 2.842
  timestamp: 1651097022
  timesteps_since_restore: 0
  timesteps_total: 24000
  training_iteration: 6
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |      6 |          551.263 | 24000 |  385.772 |              862.146 |             -502.502 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 224000
  custom_metrics:
    eps_sum_utility_max: 654.77705507386
    eps_sum_utility_mean: 129.48847282396179
    eps_sum_utility_min: -745.9840620447504
    sum_utility_max: 28.447238265903458
    sum_utility_mean: 18.12766871203447
    sum_utility_min: -18.631779097107447
  date: 2022-04-28_03-35-36
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 863.5059372789642
  episode_reward_mean: 575.5746720785042
  episode_reward_min: 103.7004119952179
  episodes_this_iter: 40
  episodes_total: 280
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8524287939071655
          entropy_coeff: 0.0
          kl: 0.00827199686318636
          model: {}
          policy_loss: -0.008327501825988293
          total_loss: 4577.708984375
          vf_explained_var: 0.48651543259620667
          vf_loss: 4577.71484375
    num_agent_steps_sampled: 224000
    num_agent_steps_trained: 224000
    num_steps_sampled: 28000
    num_steps_trained: 28000
  iterations_since_restore: 7
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.285000000000004
    ram_util_percent: 36.635625
  pid: 3889
  policy_reward_max:
    ue: 395.51546650909563
  policy_reward_mean:
    ue: 71.94683400981302
  policy_reward_min:
    ue: -230.32887276632633
  sampler_perf:
    mean_action_processing_ms: 0.11930028319906655
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 32.06196057760258
    mean_inference_ms: 0.8542757993852844
    mean_raw_obs_processing_ms: 0.5799584775438269
  time_since_restore: 665.9307856559753
  time_this_iter_s: 114.66809010505676
  time_total_s: 665.9307856559753
  timers:
    learn_throughput: 159.535
    learn_time_ms: 25072.86
    load_throughput: 354247.58
    load_time_ms: 11.292
    sample_throughput: 57.117
    sample_time_ms: 70032.066
    update_time_ms: 2.86
  timestamp: 1651097136
  timesteps_since_restore: 0
  timesteps_total: 28000
  training_iteration: 7
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |      7 |          665.931 | 28000 |  575.575 |              863.506 |                103.7 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 256000
  custom_metrics:
    eps_sum_utility_max: 733.8726264159679
    eps_sum_utility_mean: 350.6785103185988
    eps_sum_utility_min: -312.3802896556478
    sum_utility_max: 28.74678100245414
    sum_utility_mean: 20.27587962787223
    sum_utility_min: -26.041878962424093
  date: 2022-04-28_03-37-39
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 930.9897059516616
  episode_reward_mean: 663.8869245029209
  episode_reward_min: 103.7004119952179
  episodes_this_iter: 40
  episodes_total: 320
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8362332582473755
          entropy_coeff: 0.0
          kl: 0.00834003183990717
          model: {}
          policy_loss: -0.00775230024009943
          total_loss: 3928.384033203125
          vf_explained_var: 0.5530317425727844
          vf_loss: 3928.38916015625
    num_agent_steps_sampled: 256000
    num_agent_steps_trained: 256000
    num_steps_sampled: 32000
    num_steps_trained: 32000
  iterations_since_restore: 8
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 38.333333333333336
    ram_util_percent: 37.00760233918129
  pid: 3889
  policy_reward_max:
    ue: 373.5500156642461
  policy_reward_mean:
    ue: 82.98586556286509
  policy_reward_min:
    ue: -206.5022997138336
  sampler_perf:
    mean_action_processing_ms: 0.12213803121065248
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 33.465952500498
    mean_inference_ms: 0.8719810299075802
    mean_raw_obs_processing_ms: 0.5943278116904241
  time_since_restore: 788.3811042308807
  time_this_iter_s: 122.4503185749054
  time_total_s: 788.3811042308807
  timers:
    learn_throughput: 156.32
    learn_time_ms: 25588.54
    load_throughput: 367290.124
    load_time_ms: 10.891
    sample_throughput: 54.846
    sample_time_ms: 72931.83
    update_time_ms: 2.909
  timestamp: 1651097259
  timesteps_since_restore: 0
  timesteps_total: 32000
  training_iteration: 8
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |      8 |          788.381 | 32000 |  663.887 |               930.99 |                103.7 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 288000
  custom_metrics:
    eps_sum_utility_max: 912.3748657279792
    eps_sum_utility_mean: 502.5101908484958
    eps_sum_utility_min: -286.1892520406062
    sum_utility_max: 28.74678100245414
    sum_utility_mean: 21.607035675339645
    sum_utility_min: -26.041878962424093
  date: 2022-04-28_03-39-39
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 996.1358754153218
  episode_reward_mean: 735.4191244271308
  episode_reward_min: 103.7004119952179
  episodes_this_iter: 40
  episodes_total: 360
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8232413530349731
          entropy_coeff: 0.0
          kl: 0.008653209544718266
          model: {}
          policy_loss: -0.008363033644855022
          total_loss: 3156.485107421875
          vf_explained_var: 0.6291764974594116
          vf_loss: 3156.49072265625
    num_agent_steps_sampled: 288000
    num_agent_steps_trained: 288000
    num_steps_sampled: 36000
    num_steps_trained: 36000
  iterations_since_restore: 9
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.67664670658683
    ram_util_percent: 37.39341317365269
  pid: 3889
  policy_reward_max:
    ue: 378.324135056215
  policy_reward_mean:
    ue: 91.92739055339135
  policy_reward_min:
    ue: -179.21757503816647
  sampler_perf:
    mean_action_processing_ms: 0.12463474039457732
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 34.67892604379673
    mean_inference_ms: 0.8875915646301522
    mean_raw_obs_processing_ms: 0.6072298958797089
  time_since_restore: 908.1399073600769
  time_this_iter_s: 119.75880312919617
  time_total_s: 908.1399073600769
  timers:
    learn_throughput: 153.688
    learn_time_ms: 26026.759
    load_throughput: 366042.137
    load_time_ms: 10.928
    sample_throughput: 53.44
    sample_time_ms: 74850.575
    update_time_ms: 2.958
  timestamp: 1651097379
  timesteps_since_restore: 0
  timesteps_total: 36000
  training_iteration: 9
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |      9 |           908.14 | 36000 |  735.419 |              996.136 |                103.7 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 320000
  custom_metrics:
    eps_sum_utility_max: 912.3748657279792
    eps_sum_utility_mean: 603.2113201612159
    eps_sum_utility_min: 164.74828380121653
    sum_utility_max: 27.915161193583785
    sum_utility_mean: 20.583452146540612
    sum_utility_min: -26.041878962424093
  date: 2022-04-28_03-41-43
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 996.1358754153218
  episode_reward_mean: 778.4128609519207
  episode_reward_min: 544.1911554466934
  episodes_this_iter: 40
  episodes_total: 400
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.816927433013916
          entropy_coeff: 0.0
          kl: 0.008071422576904297
          model: {}
          policy_loss: -0.00797024555504322
          total_loss: 2516.478515625
          vf_explained_var: 0.6879082322120667
          vf_loss: 2516.48388671875
    num_agent_steps_sampled: 320000
    num_agent_steps_trained: 320000
    num_steps_sampled: 40000
    num_steps_trained: 40000
  iterations_since_restore: 10
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.802312138728325
    ram_util_percent: 37.31156069364162
  pid: 3889
  policy_reward_max:
    ue: 378.324135056215
  policy_reward_mean:
    ue: 97.30160761899009
  policy_reward_min:
    ue: -147.49922647389718
  sampler_perf:
    mean_action_processing_ms: 0.12677688460687692
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 35.72624842578082
    mean_inference_ms: 0.9011427807564061
    mean_raw_obs_processing_ms: 0.6184910145618038
  time_since_restore: 1032.423086643219
  time_this_iter_s: 124.28317928314209
  time_total_s: 1032.423086643219
  timers:
    learn_throughput: 151.523
    learn_time_ms: 26398.639
    load_throughput: 364734.773
    load_time_ms: 10.967
    sample_throughput: 52.072
    sample_time_ms: 76816.682
    update_time_ms: 2.992
  timestamp: 1651097503
  timesteps_since_restore: 0
  timesteps_total: 40000
  training_iteration: 10
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     10 |          1032.42 | 40000 |  778.413 |              996.136 |              544.191 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 352000
  custom_metrics:
    eps_sum_utility_max: 989.7173133147769
    eps_sum_utility_mean: 672.2227639920939
    eps_sum_utility_min: 164.74828380121653
    sum_utility_max: 27.92706244768804
    sum_utility_mean: 22.054129424804195
    sum_utility_min: -8.565383323503156
  date: 2022-04-28_03-43-45
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1118.2892625557997
  episode_reward_mean: 801.4707827992092
  episode_reward_min: 551.2805001823073
  episodes_this_iter: 40
  episodes_total: 440
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7988383769989014
          entropy_coeff: 0.0
          kl: 0.009088896214962006
          model: {}
          policy_loss: -0.008392785675823689
          total_loss: 2113.5498046875
          vf_explained_var: 0.7330496907234192
          vf_loss: 2113.555419921875
    num_agent_steps_sampled: 352000
    num_agent_steps_trained: 352000
    num_steps_sampled: 44000
    num_steps_trained: 44000
  iterations_since_restore: 11
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.19294117647058
    ram_util_percent: 37.31176470588236
  pid: 3889
  policy_reward_max:
    ue: 375.75969388047673
  policy_reward_mean:
    ue: 100.18384784990114
  policy_reward_min:
    ue: -147.49922647389718
  sampler_perf:
    mean_action_processing_ms: 0.1284501016078759
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 36.58244355055071
    mean_inference_ms: 0.9117294874611462
    mean_raw_obs_processing_ms: 0.6273632697893707
  time_since_restore: 1153.955181837082
  time_this_iter_s: 121.53209519386292
  time_total_s: 1153.955181837082
  timers:
    learn_throughput: 147.498
    learn_time_ms: 27118.944
    load_throughput: 475790.118
    load_time_ms: 8.407
    sample_throughput: 49.231
    sample_time_ms: 81250.236
    update_time_ms: 3.088
  timestamp: 1651097625
  timesteps_since_restore: 0
  timesteps_total: 44000
  training_iteration: 11
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     11 |          1153.96 | 44000 |  801.471 |              1118.29 |              551.281 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 384000
  custom_metrics:
    eps_sum_utility_max: 989.7173133147769
    eps_sum_utility_mean: 728.4022527982697
    eps_sum_utility_min: 475.9087729424967
    sum_utility_max: 28.247904192338435
    sum_utility_mean: 22.42778369515973
    sum_utility_min: -7.300897125575836
  date: 2022-04-28_03-45-51
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1118.2892625557997
  episode_reward_mean: 824.9120883227267
  episode_reward_min: 563.0134038413256
  episodes_this_iter: 40
  episodes_total: 480
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.789840579032898
          entropy_coeff: 0.0
          kl: 0.00825226865708828
          model: {}
          policy_loss: -0.008053830824792385
          total_loss: 1682.3748779296875
          vf_explained_var: 0.779088020324707
          vf_loss: 1682.3804931640625
    num_agent_steps_sampled: 384000
    num_agent_steps_trained: 384000
    num_steps_sampled: 48000
    num_steps_trained: 48000
  iterations_since_restore: 12
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.00685714285715
    ram_util_percent: 37.22685714285715
  pid: 3889
  policy_reward_max:
    ue: 375.75969388047673
  policy_reward_mean:
    ue: 103.11401104034083
  policy_reward_min:
    ue: -144.7365732711991
  sampler_perf:
    mean_action_processing_ms: 0.129996934024749
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 37.34988481227147
    mean_inference_ms: 0.9213365562316532
    mean_raw_obs_processing_ms: 0.6353418496659016
  time_since_restore: 1279.9186370372772
  time_this_iter_s: 125.96345520019531
  time_total_s: 1279.9186370372772
  timers:
    learn_throughput: 143.801
    learn_time_ms: 27816.266
    load_throughput: 456596.188
    load_time_ms: 8.76
    sample_throughput: 46.983
    sample_time_ms: 85137.501
    update_time_ms: 3.117
  timestamp: 1651097751
  timesteps_since_restore: 0
  timesteps_total: 48000
  training_iteration: 12
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     12 |          1279.92 | 48000 |  824.912 |              1118.29 |              563.013 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 416000
  custom_metrics:
    eps_sum_utility_max: 989.7173133147769
    eps_sum_utility_mean: 767.4350954502162
    eps_sum_utility_min: 553.1369712947844
    sum_utility_max: 28.247904192338435
    sum_utility_mean: 21.95143895928697
    sum_utility_min: -8.370234660525545
  date: 2022-04-28_03-47-55
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1118.2892625557997
  episode_reward_mean: 846.7159152665422
  episode_reward_min: 701.5807788096181
  episodes_this_iter: 40
  episodes_total: 520
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7777940034866333
          entropy_coeff: 0.0
          kl: 0.008239634335041046
          model: {}
          policy_loss: -0.008400381542742252
          total_loss: 1345.2900390625
          vf_explained_var: 0.820795476436615
          vf_loss: 1345.2958984375
    num_agent_steps_sampled: 416000
    num_agent_steps_trained: 416000
    num_steps_sampled: 52000
    num_steps_trained: 52000
  iterations_since_restore: 13
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.98390804597701
    ram_util_percent: 37.27413793103449
  pid: 3889
  policy_reward_max:
    ue: 374.7822059512604
  policy_reward_mean:
    ue: 105.83948940831775
  policy_reward_min:
    ue: -109.18352223412484
  sampler_perf:
    mean_action_processing_ms: 0.1313336187800614
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 38.00622147256207
    mean_inference_ms: 0.9295181948180808
    mean_raw_obs_processing_ms: 0.6422970941114942
  time_since_restore: 1404.1054978370667
  time_this_iter_s: 124.18686079978943
  time_total_s: 1404.1054978370667
  timers:
    learn_throughput: 141.078
    learn_time_ms: 28353.206
    load_throughput: 442578.354
    load_time_ms: 9.038
    sample_throughput: 45.515
    sample_time_ms: 87883.293
    update_time_ms: 3.094
  timestamp: 1651097875
  timesteps_since_restore: 0
  timesteps_total: 52000
  training_iteration: 13
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     13 |          1404.11 | 52000 |  846.716 |              1118.29 |              701.581 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 448000
  custom_metrics:
    eps_sum_utility_max: 1001.2091019718932
    eps_sum_utility_mean: 781.522886897822
    eps_sum_utility_min: 580.6093787747454
    sum_utility_max: 27.94134630341574
    sum_utility_mean: 21.28596931802292
    sum_utility_min: -8.370234660525545
  date: 2022-04-28_03-50-02
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1016.5082807153017
  episode_reward_mean: 844.4189341283713
  episode_reward_min: 710.6819683392224
  episodes_this_iter: 40
  episodes_total: 560
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.758292317390442
          entropy_coeff: 0.0
          kl: 0.009396699257194996
          model: {}
          policy_loss: -0.008775301277637482
          total_loss: 995.3296508789062
          vf_explained_var: 0.8686257004737854
          vf_loss: 995.3355102539062
    num_agent_steps_sampled: 448000
    num_agent_steps_trained: 448000
    num_steps_sampled: 56000
    num_steps_trained: 56000
  iterations_since_restore: 14
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.14147727272727
    ram_util_percent: 37.275
  pid: 3889
  policy_reward_max:
    ue: 374.7822059512604
  policy_reward_mean:
    ue: 105.55236676604638
  policy_reward_min:
    ue: -106.64622911820159
  sampler_perf:
    mean_action_processing_ms: 0.13256295537536497
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 38.59025727321219
    mean_inference_ms: 0.9369858661897689
    mean_raw_obs_processing_ms: 0.6486130806925527
  time_since_restore: 1530.7037606239319
  time_this_iter_s: 126.59826278686523
  time_total_s: 1530.7037606239319
  timers:
    learn_throughput: 138.63
    learn_time_ms: 28853.825
    load_throughput: 437489.987
    load_time_ms: 9.143
    sample_throughput: 44.288
    sample_time_ms: 90318.325
    update_time_ms: 3.13
  timestamp: 1651098002
  timesteps_since_restore: 0
  timesteps_total: 56000
  training_iteration: 14
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     14 |           1530.7 | 56000 |  844.419 |              1016.51 |              710.682 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 480000
  custom_metrics:
    eps_sum_utility_max: 1001.2091019718932
    eps_sum_utility_mean: 811.3653736301874
    eps_sum_utility_min: 580.6093787747454
    sum_utility_max: 27.91237584899335
    sum_utility_mean: 22.657320845846037
    sum_utility_min: -23.593085271061764
  date: 2022-04-28_03-52-12
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1016.5082807153017
  episode_reward_mean: 846.6509478009685
  episode_reward_min: 709.8384607514348
  episodes_this_iter: 40
  episodes_total: 600
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7402033805847168
          entropy_coeff: 0.0
          kl: 0.008246541023254395
          model: {}
          policy_loss: -0.007320700213313103
          total_loss: 704.5733642578125
          vf_explained_var: 0.9066774249076843
          vf_loss: 704.5781860351562
    num_agent_steps_sampled: 480000
    num_agent_steps_trained: 480000
    num_steps_sampled: 60000
    num_steps_trained: 60000
  iterations_since_restore: 15
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.029281767955794
    ram_util_percent: 37.29281767955801
  pid: 3889
  policy_reward_max:
    ue: 374.583848114991
  policy_reward_mean:
    ue: 105.83136847512105
  policy_reward_min:
    ue: -122.69590891943014
  sampler_perf:
    mean_action_processing_ms: 0.13374209978281992
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 39.14352978285842
    mean_inference_ms: 0.9442138136687598
    mean_raw_obs_processing_ms: 0.6546596344685831
  time_since_restore: 1660.3885409832
  time_this_iter_s: 129.6847803592682
  time_total_s: 1660.3885409832
  timers:
    learn_throughput: 136.84
    learn_time_ms: 29231.167
    load_throughput: 425778.761
    load_time_ms: 9.395
    sample_throughput: 43.217
    sample_time_ms: 92555.545
    update_time_ms: 3.214
  timestamp: 1651098132
  timesteps_since_restore: 0
  timesteps_total: 60000
  training_iteration: 15
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     15 |          1660.39 | 60000 |  846.651 |              1016.51 |              709.838 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 512000
  custom_metrics:
    eps_sum_utility_max: 1001.2091019718932
    eps_sum_utility_mean: 829.095197540001
    eps_sum_utility_min: 635.2451909444496
    sum_utility_max: 27.92914889743163
    sum_utility_mean: 22.700595201520272
    sum_utility_min: -23.593085271061764
  date: 2022-04-28_03-54-21
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1013.7984291457324
  episode_reward_mean: 852.2648936984535
  episode_reward_min: 709.8384607514348
  episodes_this_iter: 40
  episodes_total: 640
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7301020622253418
          entropy_coeff: 0.0
          kl: 0.00791793130338192
          model: {}
          policy_loss: -0.007836057804524899
          total_loss: 511.05181884765625
          vf_explained_var: 0.9315606951713562
          vf_loss: 511.05731201171875
    num_agent_steps_sampled: 512000
    num_agent_steps_trained: 512000
    num_steps_sampled: 64000
    num_steps_trained: 64000
  iterations_since_restore: 16
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.93
    ram_util_percent: 37.29222222222222
  pid: 3889
  policy_reward_max:
    ue: 374.583848114991
  policy_reward_mean:
    ue: 106.5331117123067
  policy_reward_min:
    ue: -122.69590891943014
  sampler_perf:
    mean_action_processing_ms: 0.1348790650750313
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 39.67170800183584
    mean_inference_ms: 0.9513105409642602
    mean_raw_obs_processing_ms: 0.6605263934535759
  time_since_restore: 1789.7557582855225
  time_this_iter_s: 129.3672173023224
  time_total_s: 1789.7557582855225
  timers:
    learn_throughput: 135.39
    learn_time_ms: 29544.18
    load_throughput: 425829.554
    load_time_ms: 9.393
    sample_throughput: 42.426
    sample_time_ms: 94280.781
    update_time_ms: 3.266
  timestamp: 1651098261
  timesteps_since_restore: 0
  timesteps_total: 64000
  training_iteration: 16
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     16 |          1789.76 | 64000 |  852.265 |               1013.8 |              709.838 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 544000
  custom_metrics:
    eps_sum_utility_max: 1111.622519990647
    eps_sum_utility_mean: 859.9315497777662
    eps_sum_utility_min: 635.2451909444496
    sum_utility_max: 27.92914889743163
    sum_utility_mean: 23.795094592815826
    sum_utility_min: -5.639587178231683
  date: 2022-04-28_03-56-32
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1111.7421736978329
  episode_reward_mean: 867.4094401781379
  episode_reward_min: 709.8384607514348
  episodes_this_iter: 40
  episodes_total: 680
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7255854606628418
          entropy_coeff: 0.0
          kl: 0.008234507404267788
          model: {}
          policy_loss: -0.007213044911623001
          total_loss: 335.4619445800781
          vf_explained_var: 0.9519652724266052
          vf_loss: 335.4666748046875
    num_agent_steps_sampled: 544000
    num_agent_steps_trained: 544000
    num_steps_sampled: 68000
    num_steps_trained: 68000
  iterations_since_restore: 17
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.13186813186813
    ram_util_percent: 37.30714285714286
  pid: 3889
  policy_reward_max:
    ue: 375.1577271520142
  policy_reward_mean:
    ue: 108.4261800222672
  policy_reward_min:
    ue: -104.56498271683543
  sampler_perf:
    mean_action_processing_ms: 0.13589375177747473
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 40.15076593667964
    mean_inference_ms: 0.9576226545732012
    mean_raw_obs_processing_ms: 0.6657399510998954
  time_since_restore: 1920.6680190563202
  time_this_iter_s: 130.91226077079773
  time_total_s: 1920.6680190563202
  timers:
    learn_throughput: 133.511
    learn_time_ms: 29959.974
    load_throughput: 408787.614
    load_time_ms: 9.785
    sample_throughput: 41.89
    sample_time_ms: 95489.016
    update_time_ms: 3.306
  timestamp: 1651098392
  timesteps_since_restore: 0
  timesteps_total: 68000
  training_iteration: 17
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     17 |          1920.67 | 68000 |  867.409 |              1111.74 |              709.838 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 576000
  custom_metrics:
    eps_sum_utility_max: 1111.622519990647
    eps_sum_utility_mean: 885.7883265485391
    eps_sum_utility_min: 635.2451909444496
    sum_utility_max: 27.92914889743163
    sum_utility_mean: 24.0983788242015
    sum_utility_min: -5.639587178231683
  date: 2022-04-28_03-58-42
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1111.7421736978329
  episode_reward_mean: 878.2924112821914
  episode_reward_min: 730.2418834297955
  episodes_this_iter: 40
  episodes_total: 720
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.721545696258545
          entropy_coeff: 0.0
          kl: 0.008899019099771976
          model: {}
          policy_loss: -0.008703590370714664
          total_loss: 221.93711853027344
          vf_explained_var: 0.9668849110603333
          vf_loss: 221.9431610107422
    num_agent_steps_sampled: 576000
    num_agent_steps_trained: 576000
    num_steps_sampled: 72000
    num_steps_trained: 72000
  iterations_since_restore: 18
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.14175824175824
    ram_util_percent: 37.29065934065934
  pid: 3889
  policy_reward_max:
    ue: 375.1577271520142
  policy_reward_mean:
    ue: 109.78655141027392
  policy_reward_min:
    ue: -104.56498271683543
  sampler_perf:
    mean_action_processing_ms: 0.13680121240350235
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 40.57798282050197
    mean_inference_ms: 0.9631333805849509
    mean_raw_obs_processing_ms: 0.670284550614337
  time_since_restore: 2050.703676223755
  time_this_iter_s: 130.0356571674347
  time_total_s: 2050.703676223755
  timers:
    learn_throughput: 132.951
    learn_time_ms: 30086.316
    load_throughput: 393818.419
    load_time_ms: 10.157
    sample_throughput: 41.615
    sample_time_ms: 96120.241
    update_time_ms: 3.366
  timestamp: 1651098522
  timesteps_since_restore: 0
  timesteps_total: 72000
  training_iteration: 18
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     18 |           2050.7 | 72000 |  878.292 |              1111.74 |              730.242 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 608000
  custom_metrics:
    eps_sum_utility_max: 1111.622519990647
    eps_sum_utility_mean: 895.0341509264538
    eps_sum_utility_min: 767.4132128514531
    sum_utility_max: 27.896212174759178
    sum_utility_mean: 24.41342632449282
    sum_utility_min: 17.995220758295616
  date: 2022-04-28_04-00-53
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1111.7421736978329
  episode_reward_mean: 876.6059147279852
  episode_reward_min: 781.6194021941701
  episodes_this_iter: 40
  episodes_total: 760
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7106053829193115
          entropy_coeff: 0.0
          kl: 0.008509594947099686
          model: {}
          policy_loss: -0.008883306756615639
          total_loss: 174.95152282714844
          vf_explained_var: 0.9730851054191589
          vf_loss: 174.9578399658203
    num_agent_steps_sampled: 608000
    num_agent_steps_trained: 608000
    num_steps_sampled: 76000
    num_steps_trained: 76000
  iterations_since_restore: 19
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.85911602209945
    ram_util_percent: 37.229281767955804
  pid: 3889
  policy_reward_max:
    ue: 375.1577271520142
  policy_reward_mean:
    ue: 109.57573934099815
  policy_reward_min:
    ue: -102.97714360630906
  sampler_perf:
    mean_action_processing_ms: 0.13763813518939969
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 40.965450715661284
    mean_inference_ms: 0.9680858939865629
    mean_raw_obs_processing_ms: 0.6745476913837899
  time_since_restore: 2181.0033762454987
  time_this_iter_s: 130.29970002174377
  time_total_s: 2181.0033762454987
  timers:
    learn_throughput: 132.571
    learn_time_ms: 30172.581
    load_throughput: 399167.652
    load_time_ms: 10.021
    sample_throughput: 41.2
    sample_time_ms: 97087.986
    update_time_ms: 3.348
  timestamp: 1651098653
  timesteps_since_restore: 0
  timesteps_total: 76000
  training_iteration: 19
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     19 |             2181 | 76000 |  876.606 |              1111.74 |              781.619 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 640000
  custom_metrics:
    eps_sum_utility_max: 1038.5736845400818
    eps_sum_utility_mean: 899.9505025342316
    eps_sum_utility_min: 777.2126844686311
    sum_utility_max: 27.896212174759178
    sum_utility_mean: 24.342543524612044
    sum_utility_min: 17.995220758295616
  date: 2022-04-28_04-03-05
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1028.524715708701
  episode_reward_mean: 876.7701421830056
  episode_reward_min: 781.6194021941701
  episodes_this_iter: 40
  episodes_total: 800
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.694992184638977
          entropy_coeff: 0.0
          kl: 0.009046578779816628
          model: {}
          policy_loss: -0.00900360569357872
          total_loss: 155.84495544433594
          vf_explained_var: 0.9761608839035034
          vf_loss: 155.85125732421875
    num_agent_steps_sampled: 640000
    num_agent_steps_trained: 640000
    num_steps_sampled: 80000
    num_steps_trained: 80000
  iterations_since_restore: 20
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.18864864864865
    ram_util_percent: 37.274594594594596
  pid: 3889
  policy_reward_max:
    ue: 375.12487169450225
  policy_reward_mean:
    ue: 109.59626777287569
  policy_reward_min:
    ue: -92.42163148263595
  sampler_perf:
    mean_action_processing_ms: 0.13840088153316446
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 41.32399681640715
    mean_inference_ms: 0.9726495238561274
    mean_raw_obs_processing_ms: 0.6784325534388383
  time_since_restore: 2313.4582920074463
  time_this_iter_s: 132.45491576194763
  time_total_s: 2313.4582920074463
  timers:
    learn_throughput: 131.577
    learn_time_ms: 30400.509
    load_throughput: 403912.097
    load_time_ms: 9.903
    sample_throughput: 40.951
    sample_time_ms: 97677.536
    update_time_ms: 3.318
  timestamp: 1651098785
  timesteps_since_restore: 0
  timesteps_total: 80000
  training_iteration: 20
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     20 |          2313.46 | 80000 |   876.77 |              1028.52 |              781.619 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 672000
  custom_metrics:
    eps_sum_utility_max: 1072.7292637062915
    eps_sum_utility_mean: 907.7337440320276
    eps_sum_utility_min: 811.6885500540379
    sum_utility_max: 27.864297001577967
    sum_utility_mean: 24.44086600700392
    sum_utility_min: 20.451209217307138
  date: 2022-04-28_04-05-16
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1064.8321138890815
  episode_reward_mean: 883.2099381485975
  episode_reward_min: 781.3444433465542
  episodes_this_iter: 40
  episodes_total: 840
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6863396167755127
          entropy_coeff: 0.0
          kl: 0.008768831379711628
          model: {}
          policy_loss: -0.01068823505192995
          total_loss: 125.67251586914062
          vf_explained_var: 0.9801916480064392
          vf_loss: 125.68058013916016
    num_agent_steps_sampled: 672000
    num_agent_steps_trained: 672000
    num_steps_sampled: 84000
    num_steps_trained: 84000
  iterations_since_restore: 21
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.95303867403315
    ram_util_percent: 37.3049723756906
  pid: 3889
  policy_reward_max:
    ue: 375.12487169450225
  policy_reward_mean:
    ue: 110.40124226857466
  policy_reward_min:
    ue: -92.42163148263595
  sampler_perf:
    mean_action_processing_ms: 0.1390602404582881
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 41.645056859629264
    mean_inference_ms: 0.9766415894527952
    mean_raw_obs_processing_ms: 0.6817635430290966
  time_since_restore: 2443.4437425136566
  time_this_iter_s: 129.98545050621033
  time_total_s: 2443.4437425136566
  timers:
    learn_throughput: 130.978
    learn_time_ms: 30539.468
    load_throughput: 409189.412
    load_time_ms: 9.775
    sample_throughput: 40.657
    sample_time_ms: 98384.298
    update_time_ms: 3.296
  timestamp: 1651098916
  timesteps_since_restore: 0
  timesteps_total: 84000
  training_iteration: 21
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     21 |          2443.44 | 84000 |   883.21 |              1064.83 |              781.344 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 704000
  custom_metrics:
    eps_sum_utility_max: 1072.7292637062915
    eps_sum_utility_mean: 900.5572779147041
    eps_sum_utility_min: 655.2574650634386
    sum_utility_max: 27.864297001577967
    sum_utility_mean: 24.502646842802484
    sum_utility_min: 21.13295282210432
  date: 2022-04-28_04-07-28
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1064.8321138890815
  episode_reward_mean: 877.6819208579343
  episode_reward_min: 663.7787339368391
  episodes_this_iter: 40
  episodes_total: 880
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6805219650268555
          entropy_coeff: 0.0
          kl: 0.010057765990495682
          model: {}
          policy_loss: -0.012244009412825108
          total_loss: 119.66829681396484
          vf_explained_var: 0.9814854860305786
          vf_loss: 119.67752838134766
    num_agent_steps_sampled: 704000
    num_agent_steps_trained: 704000
    num_steps_sampled: 88000
    num_steps_trained: 88000
  iterations_since_restore: 22
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.273369565217386
    ram_util_percent: 37.339130434782604
  pid: 3889
  policy_reward_max:
    ue: 374.76409784712035
  policy_reward_mean:
    ue: 109.71024010724177
  policy_reward_min:
    ue: -88.55280420246156
  sampler_perf:
    mean_action_processing_ms: 0.13966662386980996
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 41.93977641166611
    mean_inference_ms: 0.980288640660762
    mean_raw_obs_processing_ms: 0.6846735324132305
  time_since_restore: 2575.736405849457
  time_this_iter_s: 132.29266333580017
  time_total_s: 2575.736405849457
  timers:
    learn_throughput: 130.165
    learn_time_ms: 30730.248
    load_throughput: 416584.089
    load_time_ms: 9.602
    sample_throughput: 40.475
    sample_time_ms: 98826.634
    update_time_ms: 3.313
  timestamp: 1651099048
  timesteps_since_restore: 0
  timesteps_total: 88000
  training_iteration: 22
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     22 |          2575.74 | 88000 |  877.682 |              1064.83 |              663.779 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 736000
  custom_metrics:
    eps_sum_utility_max: 1072.7292637062915
    eps_sum_utility_mean: 890.7161843189766
    eps_sum_utility_min: 655.2574650634386
    sum_utility_max: 27.864297001577967
    sum_utility_mean: 24.693848509633664
    sum_utility_min: 21.137605556265537
  date: 2022-04-28_04-09-39
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1064.8321138890815
  episode_reward_mean: 869.9502704481985
  episode_reward_min: 663.7787339368391
  episodes_this_iter: 40
  episodes_total: 920
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6759591102600098
          entropy_coeff: 0.0
          kl: 0.007520436309278011
          model: {}
          policy_loss: -0.010282188653945923
          total_loss: 110.19554138183594
          vf_explained_var: 0.9826751947402954
          vf_loss: 110.20355987548828
    num_agent_steps_sampled: 736000
    num_agent_steps_trained: 736000
    num_steps_sampled: 92000
    num_steps_trained: 92000
  iterations_since_restore: 23
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.96557377049181
    ram_util_percent: 37.26010928961749
  pid: 3889
  policy_reward_max:
    ue: 373.69461000940214
  policy_reward_mean:
    ue: 108.74378380602478
  policy_reward_min:
    ue: -85.76090928325058
  sampler_perf:
    mean_action_processing_ms: 0.14021045371066068
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 42.207059039092115
    mean_inference_ms: 0.983668443399753
    mean_raw_obs_processing_ms: 0.6873449274065689
  time_since_restore: 2706.7255384922028
  time_this_iter_s: 130.98913264274597
  time_total_s: 2706.7255384922028
  timers:
    learn_throughput: 129.516
    learn_time_ms: 30884.283
    load_throughput: 413043.712
    load_time_ms: 9.684
    sample_throughput: 40.261
    sample_time_ms: 99352.579
    update_time_ms: 3.348
  timestamp: 1651099179
  timesteps_since_restore: 0
  timesteps_total: 92000
  training_iteration: 23
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     23 |          2706.73 | 92000 |   869.95 |              1064.83 |              663.779 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 768000
  custom_metrics:
    eps_sum_utility_max: 1139.5618436102231
    eps_sum_utility_mean: 903.7405540872916
    eps_sum_utility_min: 655.2574650634386
    sum_utility_max: 27.892665167264155
    sum_utility_mean: 24.723011704427204
    sum_utility_min: 21.137605556265537
  date: 2022-04-28_04-11-51
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1093.9097314650892
  episode_reward_mean: 877.412523720205
  episode_reward_min: 663.7787339368391
  episodes_this_iter: 40
  episodes_total: 960
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6712719202041626
          entropy_coeff: 0.0
          kl: 0.008371736854314804
          model: {}
          policy_loss: -0.009099079295992851
          total_loss: 95.99718475341797
          vf_explained_var: 0.984826922416687
          vf_loss: 96.00377655029297
    num_agent_steps_sampled: 768000
    num_agent_steps_trained: 768000
    num_steps_sampled: 96000
    num_steps_trained: 96000
  iterations_since_restore: 24
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.03478260869565
    ram_util_percent: 37.30380434782609
  pid: 3889
  policy_reward_max:
    ue: 375.77806498853283
  policy_reward_mean:
    ue: 109.67656546502562
  policy_reward_min:
    ue: -86.68180165693883
  sampler_perf:
    mean_action_processing_ms: 0.14073888413888758
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 42.46137674727616
    mean_inference_ms: 0.9869876161155301
    mean_raw_obs_processing_ms: 0.6900465433457381
  time_since_restore: 2838.8909475803375
  time_this_iter_s: 132.16540908813477
  time_total_s: 2838.8909475803375
  timers:
    learn_throughput: 129.279
    learn_time_ms: 30940.716
    load_throughput: 413871.077
    load_time_ms: 9.665
    sample_throughput: 40.059
    sample_time_ms: 99853.133
    update_time_ms: 3.347
  timestamp: 1651099311
  timesteps_since_restore: 0
  timesteps_total: 96000
  training_iteration: 24
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     24 |          2838.89 | 96000 |  877.413 |              1093.91 |              663.779 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 800000
  custom_metrics:
    eps_sum_utility_max: 1159.190725535431
    eps_sum_utility_mean: 933.394545122253
    eps_sum_utility_min: 713.3353110276024
    sum_utility_max: 27.892665167264155
    sum_utility_mean: 24.671031116203963
    sum_utility_min: 19.59768228353794
  date: 2022-04-28_04-14-10
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1161.24883581362
  episode_reward_mean: 901.3185648366839
  episode_reward_min: 717.6529585607528
  episodes_this_iter: 40
  episodes_total: 1000
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6598422527313232
          entropy_coeff: 0.0
          kl: 0.00817926786839962
          model: {}
          policy_loss: -0.008645990863442421
          total_loss: 106.77301788330078
          vf_explained_var: 0.9828705787658691
          vf_loss: 106.77920532226562
    num_agent_steps_sampled: 800000
    num_agent_steps_trained: 800000
    num_steps_sampled: 100000
    num_steps_trained: 100000
  iterations_since_restore: 25
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 37.09222797927461
    ram_util_percent: 37.30621761658031
  pid: 3889
  policy_reward_max:
    ue: 375.77806498853283
  policy_reward_mean:
    ue: 112.66482060458547
  policy_reward_min:
    ue: -89.14655253912073
  sampler_perf:
    mean_action_processing_ms: 0.14124222167602704
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 42.69640862635298
    mean_inference_ms: 0.9901055910764768
    mean_raw_obs_processing_ms: 0.6926721572822728
  time_since_restore: 2977.4725472927094
  time_this_iter_s: 138.58159971237183
  time_total_s: 2977.4725472927094
  timers:
    learn_throughput: 126.194
    learn_time_ms: 31697.292
    load_throughput: 412898.348
    load_time_ms: 9.688
    sample_throughput: 40.006
    sample_time_ms: 99985.998
    update_time_ms: 3.384
  timestamp: 1651099450
  timesteps_since_restore: 0
  timesteps_total: 100000
  training_iteration: 25
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     25 |          2977.47 | 100000 |  901.319 |              1161.25 |              717.653 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 832000
  custom_metrics:
    eps_sum_utility_max: 1187.5140607841397
    eps_sum_utility_mean: 960.6198567326626
    eps_sum_utility_min: 782.238472250561
    sum_utility_max: 27.878398717319683
    sum_utility_mean: 24.628173711931844
    sum_utility_min: 19.59768228353794
  date: 2022-04-28_04-16-19
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1161.24883581362
  episode_reward_mean: 927.6532908759854
  episode_reward_min: 739.6449224179688
  episodes_this_iter: 40
  episodes_total: 1040
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6559077501296997
          entropy_coeff: 0.0
          kl: 0.009049512445926666
          model: {}
          policy_loss: -0.010341554880142212
          total_loss: 91.71443939208984
          vf_explained_var: 0.9851850867271423
          vf_loss: 91.72205352783203
    num_agent_steps_sampled: 832000
    num_agent_steps_trained: 832000
    num_steps_sampled: 104000
    num_steps_trained: 104000
  iterations_since_restore: 26
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.053333333333335
    ram_util_percent: 37.31111111111111
  pid: 3889
  policy_reward_max:
    ue: 375.77806498853283
  policy_reward_mean:
    ue: 115.95666135949814
  policy_reward_min:
    ue: -89.14655253912073
  sampler_perf:
    mean_action_processing_ms: 0.1416622695147743
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 42.89833879281393
    mean_inference_ms: 0.9926902518663588
    mean_raw_obs_processing_ms: 0.6948139500876888
  time_since_restore: 3106.6664249897003
  time_this_iter_s: 129.19387769699097
  time_total_s: 3106.6664249897003
  timers:
    learn_throughput: 126.025
    learn_time_ms: 31739.799
    load_throughput: 415556.376
    load_time_ms: 9.626
    sample_throughput: 40.029
    sample_time_ms: 99926.356
    update_time_ms: 3.365
  timestamp: 1651099579
  timesteps_since_restore: 0
  timesteps_total: 104000
  training_iteration: 26
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     26 |          3106.67 | 104000 |  927.653 |              1161.25 |              739.645 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 864000
  custom_metrics:
    eps_sum_utility_max: 1187.5140607841397
    eps_sum_utility_mean: 974.852306422249
    eps_sum_utility_min: 782.238472250561
    sum_utility_max: 27.878398717319683
    sum_utility_mean: 24.608173910071663
    sum_utility_min: 19.59768228353794
  date: 2022-04-28_04-18-30
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1129.3974137038954
  episode_reward_mean: 946.862862019573
  episode_reward_min: 739.6449224179688
  episodes_this_iter: 40
  episodes_total: 1080
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.642992377281189
          entropy_coeff: 0.0
          kl: 0.008452258072793484
          model: {}
          policy_loss: -0.00889618881046772
          total_loss: 106.56172180175781
          vf_explained_var: 0.9826175570487976
          vf_loss: 106.5680923461914
    num_agent_steps_sampled: 864000
    num_agent_steps_trained: 864000
    num_steps_sampled: 108000
    num_steps_trained: 108000
  iterations_since_restore: 27
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.09672131147541
    ram_util_percent: 37.31530054644808
  pid: 3889
  policy_reward_max:
    ue: 372.4046342135342
  policy_reward_mean:
    ue: 118.35785775244658
  policy_reward_min:
    ue: -81.86360102692029
  sampler_perf:
    mean_action_processing_ms: 0.1420388855750885
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.0778890658419
    mean_inference_ms: 0.9949567877754194
    mean_raw_obs_processing_ms: 0.6966294711411762
  time_since_restore: 3237.693855047226
  time_this_iter_s: 131.02743005752563
  time_total_s: 3237.693855047226
  timers:
    learn_throughput: 126.471
    learn_time_ms: 31627.742
    load_throughput: 418990.46
    load_time_ms: 9.547
    sample_throughput: 39.98
    sample_time_ms: 100050.023
    update_time_ms: 3.368
  timestamp: 1651099710
  timesteps_since_restore: 0
  timesteps_total: 108000
  training_iteration: 27
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     27 |          3237.69 | 108000 |  946.863 |               1129.4 |              739.645 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 896000
  custom_metrics:
    eps_sum_utility_max: 1229.2574293237085
    eps_sum_utility_mean: 987.8744679107441
    eps_sum_utility_min: 818.1458317115989
    sum_utility_max: 27.861277635705644
    sum_utility_mean: 24.576365778964618
    sum_utility_min: 20.442622344154547
  date: 2022-04-28_04-20-42
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1256.8586364084952
  episode_reward_mean: 969.6306095831573
  episode_reward_min: 813.3538968949867
  episodes_this_iter: 40
  episodes_total: 1120
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.628890037536621
          entropy_coeff: 0.0
          kl: 0.008106091991066933
          model: {}
          policy_loss: -0.009119701571762562
          total_loss: 112.43595123291016
          vf_explained_var: 0.9814628958702087
          vf_loss: 112.44264221191406
    num_agent_steps_sampled: 896000
    num_agent_steps_trained: 896000
    num_steps_sampled: 112000
    num_steps_trained: 112000
  iterations_since_restore: 28
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.86065573770492
    ram_util_percent: 37.3120218579235
  pid: 3889
  policy_reward_max:
    ue: 373.30389890775064
  policy_reward_mean:
    ue: 121.20382619789463
  policy_reward_min:
    ue: -81.86360102692029
  sampler_perf:
    mean_action_processing_ms: 0.14241534310853401
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.25370047549999
    mean_inference_ms: 0.997313021258327
    mean_raw_obs_processing_ms: 0.6984901394209987
  time_since_restore: 3369.5724880695343
  time_this_iter_s: 131.87863302230835
  time_total_s: 3369.5724880695343
  timers:
    learn_throughput: 126.329
    learn_time_ms: 31663.336
    load_throughput: 429043.111
    load_time_ms: 9.323
    sample_throughput: 39.92
    sample_time_ms: 100199.456
    update_time_ms: 3.299
  timestamp: 1651099842
  timesteps_since_restore: 0
  timesteps_total: 112000
  training_iteration: 28
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     28 |          3369.57 | 112000 |  969.631 |              1256.86 |              813.354 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 928000
  custom_metrics:
    eps_sum_utility_max: 1229.2574293237085
    eps_sum_utility_mean: 996.5005832546569
    eps_sum_utility_min: 818.1458317115989
    sum_utility_max: 25.383381049715556
    sum_utility_mean: 24.59579728462064
    sum_utility_min: 20.442622344154547
  date: 2022-04-28_04-22-54
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1256.8586364084952
  episode_reward_mean: 985.9254665819764
  episode_reward_min: 850.3629278744326
  episodes_this_iter: 40
  episodes_total: 1160
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.603114366531372
          entropy_coeff: 0.0
          kl: 0.008502256125211716
          model: {}
          policy_loss: -0.009392119012773037
          total_loss: 107.6156005859375
          vf_explained_var: 0.9824552536010742
          vf_loss: 107.62244415283203
    num_agent_steps_sampled: 928000
    num_agent_steps_trained: 928000
    num_steps_sampled: 116000
    num_steps_trained: 116000
  iterations_since_restore: 29
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.06775956284153
    ram_util_percent: 37.31366120218579
  pid: 3889
  policy_reward_max:
    ue: 373.306219871679
  policy_reward_mean:
    ue: 123.24068332274705
  policy_reward_min:
    ue: -82.11909797608786
  sampler_perf:
    mean_action_processing_ms: 0.1427957066669517
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.42443936217592
    mean_inference_ms: 0.9997128199440287
    mean_raw_obs_processing_ms: 0.7004760105030919
  time_since_restore: 3500.712077140808
  time_this_iter_s: 131.1395890712738
  time_total_s: 3500.712077140808
  timers:
    learn_throughput: 126.173
    learn_time_ms: 31702.493
    load_throughput: 433779.837
    load_time_ms: 9.221
    sample_throughput: 39.902
    sample_time_ms: 100244.6
    update_time_ms: 3.308
  timestamp: 1651099974
  timesteps_since_restore: 0
  timesteps_total: 116000
  training_iteration: 29
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     29 |          3500.71 | 116000 |  985.925 |              1256.86 |              850.363 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 960000
  custom_metrics:
    eps_sum_utility_max: 1221.6478569290932
    eps_sum_utility_mean: 1008.8770178690947
    eps_sum_utility_min: 847.3907740038892
    sum_utility_max: 25.38028737608236
    sum_utility_mean: 24.52347233998452
    sum_utility_min: 20.434499190456098
  date: 2022-04-28_04-25-05
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1220.3293566968007
  episode_reward_mean: 995.1789046365994
  episode_reward_min: 850.3629278744326
  episodes_this_iter: 40
  episodes_total: 1200
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5816714763641357
          entropy_coeff: 0.0
          kl: 0.00915345549583435
          model: {}
          policy_loss: -0.010880877263844013
          total_loss: 112.84884643554688
          vf_explained_var: 0.9811534285545349
          vf_loss: 112.85698699951172
    num_agent_steps_sampled: 960000
    num_agent_steps_trained: 960000
    num_steps_sampled: 120000
    num_steps_trained: 120000
  iterations_since_restore: 30
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.879781420765035
    ram_util_percent: 37.30928961748634
  pid: 3889
  policy_reward_max:
    ue: 374.0724026799963
  policy_reward_mean:
    ue: 124.3973630795749
  policy_reward_min:
    ue: -87.57871708221217
  sampler_perf:
    mean_action_processing_ms: 0.14315215679989662
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.58294155162242
    mean_inference_ms: 1.0018857272949528
    mean_raw_obs_processing_ms: 0.7024321768116127
  time_since_restore: 3631.861059188843
  time_this_iter_s: 131.14898204803467
  time_total_s: 3631.861059188843
  timers:
    learn_throughput: 126.766
    learn_time_ms: 31554.142
    load_throughput: 434525.827
    load_time_ms: 9.205
    sample_throughput: 39.895
    sample_time_ms: 100262.309
    update_time_ms: 3.308
  timestamp: 1651100105
  timesteps_since_restore: 0
  timesteps_total: 120000
  training_iteration: 30
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     30 |          3631.86 | 120000 |  995.179 |              1220.33 |              850.363 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 992000
  custom_metrics:
    eps_sum_utility_max: 1221.6478569290932
    eps_sum_utility_mean: 1032.5504465670213
    eps_sum_utility_min: 881.3712196129981
    sum_utility_max: 25.38028737608236
    sum_utility_mean: 24.626625158545576
    sum_utility_min: 20.434499190456098
  date: 2022-04-28_04-27-18
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1220.3293566968007
  episode_reward_mean: 1016.5591912603112
  episode_reward_min: 870.9923328844337
  episodes_this_iter: 40
  episodes_total: 1240
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5737046003341675
          entropy_coeff: 0.0
          kl: 0.00855229515582323
          model: {}
          policy_loss: -0.009127294644713402
          total_loss: 103.45269012451172
          vf_explained_var: 0.9823600053787231
          vf_loss: 103.4592514038086
    num_agent_steps_sampled: 992000
    num_agent_steps_trained: 992000
    num_steps_sampled: 124000
    num_steps_trained: 124000
  iterations_since_restore: 31
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.29459459459459
    ram_util_percent: 37.33513513513513
  pid: 3889
  policy_reward_max:
    ue: 376.0051902101027
  policy_reward_mean:
    ue: 127.06989890753884
  policy_reward_min:
    ue: -87.57871708221217
  sampler_perf:
    mean_action_processing_ms: 0.14349753220546746
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.73081818709431
    mean_inference_ms: 1.0040178289320476
    mean_raw_obs_processing_ms: 0.704312766428144
  time_since_restore: 3765.0579216480255
  time_this_iter_s: 133.19686245918274
  time_total_s: 3765.0579216480255
  timers:
    learn_throughput: 125.97
    learn_time_ms: 31753.486
    load_throughput: 423443.587
    load_time_ms: 9.446
    sample_throughput: 39.847
    sample_time_ms: 100383.809
    update_time_ms: 3.319
  timestamp: 1651100238
  timesteps_since_restore: 0
  timesteps_total: 124000
  training_iteration: 31
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     31 |          3765.06 | 124000 |  1016.56 |              1220.33 |              870.992 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1024000
  custom_metrics:
    eps_sum_utility_max: 1262.329853397147
    eps_sum_utility_mean: 1047.6607144264717
    eps_sum_utility_min: 906.447268035913
    sum_utility_max: 27.868118117002332
    sum_utility_mean: 24.6620785797642
    sum_utility_min: 21.13023448099787
  date: 2022-04-28_04-29-29
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1296.0334066239177
  episode_reward_mean: 1031.22156685175
  episode_reward_min: 868.9726598534702
  episodes_this_iter: 40
  episodes_total: 1280
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5619049072265625
          entropy_coeff: 0.0
          kl: 0.007821056060492992
          model: {}
          policy_loss: -0.008663696236908436
          total_loss: 108.0134048461914
          vf_explained_var: 0.9815113544464111
          vf_loss: 108.01972961425781
    num_agent_steps_sampled: 1024000
    num_agent_steps_trained: 1024000
    num_steps_sampled: 128000
    num_steps_trained: 128000
  iterations_since_restore: 32
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.94725274725275
    ram_util_percent: 37.39010989010989
  pid: 3889
  policy_reward_max:
    ue: 376.0051902101027
  policy_reward_mean:
    ue: 128.90269585646868
  policy_reward_min:
    ue: -87.57871708221217
  sampler_perf:
    mean_action_processing_ms: 0.14381178166371011
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.86773320743506
    mean_inference_ms: 1.006016583381108
    mean_raw_obs_processing_ms: 0.7060561558537745
  time_since_restore: 3895.547107934952
  time_this_iter_s: 130.48918628692627
  time_total_s: 3895.547107934952
  timers:
    learn_throughput: 126.471
    learn_time_ms: 31627.842
    load_throughput: 425645.894
    load_time_ms: 9.397
    sample_throughput: 39.869
    sample_time_ms: 100329.136
    update_time_ms: 3.333
  timestamp: 1651100369
  timesteps_since_restore: 0
  timesteps_total: 128000
  training_iteration: 32
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     32 |          3895.55 | 128000 |  1031.22 |              1296.03 |              868.973 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1056000
  custom_metrics:
    eps_sum_utility_max: 1263.8909783982358
    eps_sum_utility_mean: 1080.8197614547666
    eps_sum_utility_min: 906.447268035913
    sum_utility_max: 27.868118117002332
    sum_utility_mean: 24.693670605546203
    sum_utility_min: 21.13023448099787
  date: 2022-04-28_04-31-40
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1296.0334066239177
  episode_reward_mean: 1065.5205448805082
  episode_reward_min: 868.9726598534702
  episodes_this_iter: 40
  episodes_total: 1320
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5353502035140991
          entropy_coeff: 0.0
          kl: 0.008145052939653397
          model: {}
          policy_loss: -0.01033852994441986
          total_loss: 119.46022033691406
          vf_explained_var: 0.9788570404052734
          vf_loss: 119.46812438964844
    num_agent_steps_sampled: 1056000
    num_agent_steps_trained: 1056000
    num_steps_sampled: 132000
    num_steps_trained: 132000
  iterations_since_restore: 33
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.13406593406593
    ram_util_percent: 37.392857142857146
  pid: 3889
  policy_reward_max:
    ue: 376.0051902101027
  policy_reward_mean:
    ue: 133.1900681100635
  policy_reward_min:
    ue: -74.53551604409242
  sampler_perf:
    mean_action_processing_ms: 0.144108551398674
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.99217143544255
    mean_inference_ms: 1.007862908512816
    mean_raw_obs_processing_ms: 0.70767036139856
  time_since_restore: 4026.390319108963
  time_this_iter_s: 130.84321117401123
  time_total_s: 4026.390319108963
  timers:
    learn_throughput: 126.582
    learn_time_ms: 31600.156
    load_throughput: 434867.095
    load_time_ms: 9.198
    sample_throughput: 39.864
    sample_time_ms: 100342.382
    update_time_ms: 3.286
  timestamp: 1651100500
  timesteps_since_restore: 0
  timesteps_total: 132000
  training_iteration: 33
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     33 |          4026.39 | 132000 |  1065.52 |              1296.03 |              868.973 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1088000
  custom_metrics:
    eps_sum_utility_max: 1265.7173498458455
    eps_sum_utility_mean: 1110.9401235006305
    eps_sum_utility_min: 906.447268035913
    sum_utility_max: 27.868118117002332
    sum_utility_mean: 24.673034059707238
    sum_utility_min: 20.43269643853403
  date: 2022-04-28_04-33-50
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1297.3749421823986
  episode_reward_mean: 1098.7307062863028
  episode_reward_min: 868.9726598534702
  episodes_this_iter: 40
  episodes_total: 1360
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.508001446723938
          entropy_coeff: 0.0
          kl: 0.00800048466771841
          model: {}
          policy_loss: -0.009037046693265438
          total_loss: 88.02725219726562
          vf_explained_var: 0.9839498400688171
          vf_loss: 88.03388977050781
    num_agent_steps_sampled: 1088000
    num_agent_steps_trained: 1088000
    num_steps_sampled: 136000
    num_steps_trained: 136000
  iterations_since_restore: 34
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.1489010989011
    ram_util_percent: 37.31428571428572
  pid: 3889
  policy_reward_max:
    ue: 374.35895252735787
  policy_reward_mean:
    ue: 137.3413382857878
  policy_reward_min:
    ue: -74.53551604409242
  sampler_perf:
    mean_action_processing_ms: 0.14438131308627825
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.10241382823656
    mean_inference_ms: 1.0095728493070701
    mean_raw_obs_processing_ms: 0.7091120342594027
  time_since_restore: 4156.518511772156
  time_this_iter_s: 130.12819266319275
  time_total_s: 4156.518511772156
  timers:
    learn_throughput: 126.613
    learn_time_ms: 31592.291
    load_throughput: 429645.215
    load_time_ms: 9.31
    sample_throughput: 39.942
    sample_time_ms: 100146.289
    update_time_ms: 3.308
  timestamp: 1651100630
  timesteps_since_restore: 0
  timesteps_total: 136000
  training_iteration: 34
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     34 |          4156.52 | 136000 |  1098.73 |              1297.37 |              868.973 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1120000
  custom_metrics:
    eps_sum_utility_max: 1274.5892152596937
    eps_sum_utility_mean: 1147.1085112084697
    eps_sum_utility_min: 931.3589521403367
    sum_utility_max: 25.035998154442346
    sum_utility_mean: 24.572436941897855
    sum_utility_min: 20.43269643853403
  date: 2022-04-28_04-36-01
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1297.3749421823986
  episode_reward_mean: 1143.9002387047115
  episode_reward_min: 873.5229839867297
  episodes_this_iter: 40
  episodes_total: 1400
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4998232126235962
          entropy_coeff: 0.0
          kl: 0.008114363066852093
          model: {}
          policy_loss: -0.00952138565480709
          total_loss: 73.74996185302734
          vf_explained_var: 0.98638516664505
          vf_loss: 73.75704956054688
    num_agent_steps_sampled: 1120000
    num_agent_steps_trained: 1120000
    num_steps_sampled: 140000
    num_steps_trained: 140000
  iterations_since_restore: 35
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.14010989010989
    ram_util_percent: 37.324725274725274
  pid: 3889
  policy_reward_max:
    ue: 374.35895252735787
  policy_reward_mean:
    ue: 142.9875298380889
  policy_reward_min:
    ue: -69.24719526799818
  sampler_perf:
    mean_action_processing_ms: 0.14463530916098655
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.20275817143021
    mean_inference_ms: 1.011202066799108
    mean_raw_obs_processing_ms: 0.7109585682831167
  time_since_restore: 4287.176971912384
  time_this_iter_s: 130.65846014022827
  time_total_s: 4287.176971912384
  timers:
    learn_throughput: 129.446
    learn_time_ms: 30900.865
    load_throughput: 430559.281
    load_time_ms: 9.29
    sample_throughput: 39.982
    sample_time_ms: 100045.653
    update_time_ms: 3.265
  timestamp: 1651100761
  timesteps_since_restore: 0
  timesteps_total: 140000
  training_iteration: 35
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     35 |          4287.18 | 140000 |   1143.9 |              1297.37 |              873.523 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1152000
  custom_metrics:
    eps_sum_utility_max: 1274.5892152596937
    eps_sum_utility_mean: 1166.4878260069534
    eps_sum_utility_min: 978.4738667678703
    sum_utility_max: 25.036378667471116
    sum_utility_mean: 24.572814460507885
    sum_utility_min: 19.60439930964957
  date: 2022-04-28_04-38-09
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1335.0162500467943
  episode_reward_mean: 1173.4282341334438
  episode_reward_min: 964.07442258197
  episodes_this_iter: 40
  episodes_total: 1440
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4943004846572876
          entropy_coeff: 0.0
          kl: 0.007703191600739956
          model: {}
          policy_loss: -0.00938433688133955
          total_loss: 76.62013244628906
          vf_explained_var: 0.9854769110679626
          vf_loss: 76.62720489501953
    num_agent_steps_sampled: 1152000
    num_agent_steps_trained: 1152000
    num_steps_sampled: 144000
    num_steps_trained: 144000
  iterations_since_restore: 36
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.20786516853933
    ram_util_percent: 37.348314606741575
  pid: 3889
  policy_reward_max:
    ue: 374.33544090678606
  policy_reward_mean:
    ue: 146.67852926668044
  policy_reward_min:
    ue: -66.62715417394601
  sampler_perf:
    mean_action_processing_ms: 0.14483615221297477
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.28133401526274
    mean_inference_ms: 1.0125052391517668
    mean_raw_obs_processing_ms: 0.712499841115432
  time_since_restore: 4415.044336080551
  time_this_iter_s: 127.86736416816711
  time_total_s: 4415.044336080551
  timers:
    learn_throughput: 129.157
    learn_time_ms: 30970.127
    load_throughput: 412663.746
    load_time_ms: 9.693
    sample_throughput: 40.063
    sample_time_ms: 99843.246
    update_time_ms: 3.288
  timestamp: 1651100889
  timesteps_since_restore: 0
  timesteps_total: 144000
  training_iteration: 36
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     36 |          4415.04 | 144000 |  1173.43 |              1335.02 |              964.074 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1184000
  custom_metrics:
    eps_sum_utility_max: 1277.4570967875632
    eps_sum_utility_mean: 1186.6222150891922
    eps_sum_utility_min: 978.4738667678703
    sum_utility_max: 25.059334884688155
    sum_utility_mean: 24.68777592855492
    sum_utility_min: 19.60439930964957
  date: 2022-04-28_04-40-20
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1335.0162500467943
  episode_reward_mean: 1197.9679556979029
  episode_reward_min: 964.07442258197
  episodes_this_iter: 40
  episodes_total: 1480
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.482661485671997
          entropy_coeff: 0.0
          kl: 0.008686223067343235
          model: {}
          policy_loss: -0.01023756805807352
          total_loss: 65.05439758300781
          vf_explained_var: 0.9875680208206177
          vf_loss: 65.06204223632812
    num_agent_steps_sampled: 1184000
    num_agent_steps_trained: 1184000
    num_steps_sampled: 148000
    num_steps_trained: 148000
  iterations_since_restore: 37
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.05628415300546
    ram_util_percent: 37.428415300546455
  pid: 3889
  policy_reward_max:
    ue: 373.47625312197
  policy_reward_mean:
    ue: 149.74599446223783
  policy_reward_min:
    ue: -66.62715417394601
  sampler_perf:
    mean_action_processing_ms: 0.145035987451967
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.35638429794319
    mean_inference_ms: 1.013769211257746
    mean_raw_obs_processing_ms: 0.7140788848998085
  time_since_restore: 4546.343849182129
  time_this_iter_s: 131.29951310157776
  time_total_s: 4546.343849182129
  timers:
    learn_throughput: 128.915
    learn_time_ms: 31028.123
    load_throughput: 386602.975
    load_time_ms: 10.347
    sample_throughput: 40.076
    sample_time_ms: 99810.559
    update_time_ms: 4.243
  timestamp: 1651101020
  timesteps_since_restore: 0
  timesteps_total: 148000
  training_iteration: 37
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     37 |          4546.34 | 148000 |  1197.97 |              1335.02 |              964.074 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1216000
  custom_metrics:
    eps_sum_utility_max: 1277.4570967875632
    eps_sum_utility_mean: 1195.5547875142913
    eps_sum_utility_min: 978.4738667678703
    sum_utility_max: 25.38567779301407
    sum_utility_mean: 24.71608346039084
    sum_utility_min: 19.60439930964957
  date: 2022-04-28_04-42-33
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1336.2557869077425
  episode_reward_mean: 1209.8431095485985
  episode_reward_min: 964.07442258197
  episodes_this_iter: 40
  episodes_total: 1520
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4709372520446777
          entropy_coeff: 0.0
          kl: 0.008340740576386452
          model: {}
          policy_loss: -0.009312981739640236
          total_loss: 48.515926361083984
          vf_explained_var: 0.9906834959983826
          vf_loss: 48.522743225097656
    num_agent_steps_sampled: 1216000
    num_agent_steps_trained: 1216000
    num_steps_sampled: 152000
    num_steps_trained: 152000
  iterations_since_restore: 38
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.408152173913045
    ram_util_percent: 37.30326086956522
  pid: 3889
  policy_reward_max:
    ue: 373.03711884916635
  policy_reward_mean:
    ue: 151.2303886935748
  policy_reward_min:
    ue: -66.62715417394601
  sampler_perf:
    mean_action_processing_ms: 0.1452507104494597
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.43265229914267
    mean_inference_ms: 1.0151106530785647
    mean_raw_obs_processing_ms: 0.7151567003246896
  time_since_restore: 4678.569216012955
  time_this_iter_s: 132.2253668308258
  time_total_s: 4678.569216012955
  timers:
    learn_throughput: 127.957
    learn_time_ms: 31260.492
    load_throughput: 385533.345
    load_time_ms: 10.375
    sample_throughput: 40.156
    sample_time_ms: 99612.506
    update_time_ms: 4.352
  timestamp: 1651101153
  timesteps_since_restore: 0
  timesteps_total: 152000
  training_iteration: 38
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     38 |          4678.57 | 152000 |  1209.84 |              1336.26 |              964.074 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1248000
  custom_metrics:
    eps_sum_utility_max: 1296.5672506586002
    eps_sum_utility_mean: 1213.1741313644602
    eps_sum_utility_min: 983.9871769377843
    sum_utility_max: 25.38567779301407
    sum_utility_mean: 24.783491133252966
    sum_utility_min: 24.305923544242248
  date: 2022-04-28_04-44-49
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1336.2557869077425
  episode_reward_mean: 1227.0818647032384
  episode_reward_min: 985.5662244102681
  episodes_this_iter: 40
  episodes_total: 1560
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.450191617012024
          entropy_coeff: 0.0
          kl: 0.008894004859030247
          model: {}
          policy_loss: -0.010236100293695927
          total_loss: 50.8376350402832
          vf_explained_var: 0.9902557730674744
          vf_loss: 50.84520721435547
    num_agent_steps_sampled: 1248000
    num_agent_steps_trained: 1248000
    num_steps_sampled: 156000
    num_steps_trained: 156000
  iterations_since_restore: 39
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.230687830687835
    ram_util_percent: 37.33174603174603
  pid: 3889
  policy_reward_max:
    ue: 374.59337627959934
  policy_reward_mean:
    ue: 153.3852330879048
  policy_reward_min:
    ue: -59.27633871235547
  sampler_perf:
    mean_action_processing_ms: 0.14555834562735945
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.53746987489208
    mean_inference_ms: 1.0170570473673697
    mean_raw_obs_processing_ms: 0.716766269641929
  time_since_restore: 4814.402527809143
  time_this_iter_s: 135.83331179618835
  time_total_s: 4814.402527809143
  timers:
    learn_throughput: 127.931
    learn_time_ms: 31266.895
    load_throughput: 383397.723
    load_time_ms: 10.433
    sample_throughput: 39.97
    sample_time_ms: 100075.312
    update_time_ms: 4.368
  timestamp: 1651101289
  timesteps_since_restore: 0
  timesteps_total: 156000
  training_iteration: 39
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     39 |           4814.4 | 156000 |  1227.08 |              1336.26 |              985.566 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1280000
  custom_metrics:
    eps_sum_utility_max: 1296.5672506586002
    eps_sum_utility_mean: 1218.0869281870762
    eps_sum_utility_min: 1059.5748714680794
    sum_utility_max: 27.85175281772527
    sum_utility_mean: 24.84059155529513
    sum_utility_min: 24.305923544242248
  date: 2022-04-28_04-46-58
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1331.833707418535
  episode_reward_mean: 1235.7381273080446
  episode_reward_min: 1097.9304669079465
  episodes_this_iter: 40
  episodes_total: 1600
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.433775782585144
          entropy_coeff: 0.0
          kl: 0.00798999797552824
          model: {}
          policy_loss: -0.009024789556860924
          total_loss: 43.997276306152344
          vf_explained_var: 0.9914316534996033
          vf_loss: 44.00390625
    num_agent_steps_sampled: 1280000
    num_agent_steps_trained: 1280000
    num_steps_sampled: 160000
    num_steps_trained: 160000
  iterations_since_restore: 40
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.17666666666666
    ram_util_percent: 37.33555555555555
  pid: 3889
  policy_reward_max:
    ue: 374.59337627959934
  policy_reward_mean:
    ue: 154.46726591350557
  policy_reward_min:
    ue: -25.719904252225383
  sampler_perf:
    mean_action_processing_ms: 0.1458482403758651
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.634508326429476
    mean_inference_ms: 1.0188795546308682
    mean_raw_obs_processing_ms: 0.7183474573371964
  time_since_restore: 4944.092809915543
  time_this_iter_s: 129.69028210639954
  time_total_s: 4944.092809915543
  timers:
    learn_throughput: 127.718
    learn_time_ms: 31318.976
    load_throughput: 385404.926
    load_time_ms: 10.379
    sample_throughput: 40.049
    sample_time_ms: 99877.262
    update_time_ms: 4.387
  timestamp: 1651101418
  timesteps_since_restore: 0
  timesteps_total: 160000
  training_iteration: 40
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     40 |          4944.09 | 160000 |  1235.74 |              1331.83 |              1097.93 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1312000
  custom_metrics:
    eps_sum_utility_max: 1296.5672506586002
    eps_sum_utility_mean: 1224.5807974073211
    eps_sum_utility_min: 1028.4073217753566
    sum_utility_max: 27.85175281772527
    sum_utility_mean: 24.855941487672865
    sum_utility_min: 21.137201030289763
  date: 2022-04-28_04-49-08
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1331.833707418535
  episode_reward_mean: 1245.7210414444723
  episode_reward_min: 1127.383520624029
  episodes_this_iter: 40
  episodes_total: 1640
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4206608533859253
          entropy_coeff: 0.0
          kl: 0.008844166062772274
          model: {}
          policy_loss: -0.01041848212480545
          total_loss: 41.026546478271484
          vf_explained_var: 0.9919974207878113
          vf_loss: 41.03430938720703
    num_agent_steps_sampled: 1312000
    num_agent_steps_trained: 1312000
    num_steps_sampled: 164000
    num_steps_trained: 164000
  iterations_since_restore: 41
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.18674033149172
    ram_util_percent: 37.33646408839779
  pid: 3889
  policy_reward_max:
    ue: 373.4930197676929
  policy_reward_mean:
    ue: 155.71513018055902
  policy_reward_min:
    ue: -17.19021542263631
  sampler_perf:
    mean_action_processing_ms: 0.14608016271285648
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.711256438566686
    mean_inference_ms: 1.0203356872826688
    mean_raw_obs_processing_ms: 0.7196372196406194
  time_since_restore: 5073.613185167313
  time_this_iter_s: 129.52037525177002
  time_total_s: 5073.613185167313
  timers:
    learn_throughput: 128.292
    learn_time_ms: 31178.907
    load_throughput: 378234.089
    load_time_ms: 10.575
    sample_throughput: 40.141
    sample_time_ms: 99649.17
    update_time_ms: 4.486
  timestamp: 1651101548
  timesteps_since_restore: 0
  timesteps_total: 164000
  training_iteration: 41
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     41 |          5073.61 | 164000 |  1245.72 |              1331.83 |              1127.38 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1344000
  custom_metrics:
    eps_sum_utility_max: 1294.4338648946994
    eps_sum_utility_mean: 1232.5698298712784
    eps_sum_utility_min: 1028.4073217753566
    sum_utility_max: 27.87381319373192
    sum_utility_mean: 24.86093781592622
    sum_utility_min: 21.137201030289763
  date: 2022-04-28_04-51-18
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1344.8769529279823
  episode_reward_mean: 1254.9972552915915
  episode_reward_min: 1127.383520624029
  episodes_this_iter: 40
  episodes_total: 1680
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4195042848587036
          entropy_coeff: 0.0
          kl: 0.008243863470852375
          model: {}
          policy_loss: -0.009605100378394127
          total_loss: 36.91568374633789
          vf_explained_var: 0.9927398562431335
          vf_loss: 36.922821044921875
    num_agent_steps_sampled: 1344000
    num_agent_steps_trained: 1344000
    num_steps_sampled: 168000
    num_steps_trained: 168000
  iterations_since_restore: 42
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.22486187845304
    ram_util_percent: 37.387845303867394
  pid: 3889
  policy_reward_max:
    ue: 374.4657857022532
  policy_reward_mean:
    ue: 156.87465691144894
  policy_reward_min:
    ue: -17.19021542263631
  sampler_perf:
    mean_action_processing_ms: 0.14626135770337567
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.77012313017062
    mean_inference_ms: 1.0214548007233972
    mean_raw_obs_processing_ms: 0.7205913247596321
  time_since_restore: 5203.749338626862
  time_this_iter_s: 130.13615345954895
  time_total_s: 5203.749338626862
  timers:
    learn_throughput: 127.869
    learn_time_ms: 31282.111
    load_throughput: 373054.171
    load_time_ms: 10.722
    sample_throughput: 40.197
    sample_time_ms: 99510.354
    update_time_ms: 4.517
  timestamp: 1651101678
  timesteps_since_restore: 0
  timesteps_total: 168000
  training_iteration: 42
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     42 |          5203.75 | 168000 |     1255 |              1344.88 |              1127.38 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1376000
  custom_metrics:
    eps_sum_utility_max: 1294.4338648946994
    eps_sum_utility_mean: 1241.264694471374
    eps_sum_utility_min: 1145.6963300376442
    sum_utility_max: 27.87381319373192
    sum_utility_mean: 24.865279109022325
    sum_utility_min: 21.137201030289763
  date: 2022-04-28_04-53-29
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1344.8769529279823
  episode_reward_mean: 1267.2551247169074
  episode_reward_min: 1127.383520624029
  episodes_this_iter: 40
  episodes_total: 1720
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4025347232818604
          entropy_coeff: 0.0
          kl: 0.007235164288431406
          model: {}
          policy_loss: -0.008094355463981628
          total_loss: 36.961795806884766
          vf_explained_var: 0.9927279949188232
          vf_loss: 36.96772384643555
    num_agent_steps_sampled: 1376000
    num_agent_steps_trained: 1376000
    num_steps_sampled: 172000
    num_steps_trained: 172000
  iterations_since_restore: 43
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.535164835164835
    ram_util_percent: 37.373626373626365
  pid: 3889
  policy_reward_max:
    ue: 374.4657857022532
  policy_reward_mean:
    ue: 158.40689058961337
  policy_reward_min:
    ue: -11.870550938733917
  sampler_perf:
    mean_action_processing_ms: 0.14645252063414543
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.83063020928839
    mean_inference_ms: 1.0226194175018173
    mean_raw_obs_processing_ms: 0.721556702286507
  time_since_restore: 5334.688295125961
  time_this_iter_s: 130.93895649909973
  time_total_s: 5334.688295125961
  timers:
    learn_throughput: 127.652
    learn_time_ms: 31335.25
    load_throughput: 365550.934
    load_time_ms: 10.942
    sample_throughput: 40.214
    sample_time_ms: 99466.737
    update_time_ms: 4.51
  timestamp: 1651101809
  timesteps_since_restore: 0
  timesteps_total: 172000
  training_iteration: 43
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     43 |          5334.69 | 172000 |  1267.26 |              1344.88 |              1127.38 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1408000
  custom_metrics:
    eps_sum_utility_max: 1320.3961230168636
    eps_sum_utility_mean: 1248.4905421441647
    eps_sum_utility_min: 1162.5913649607
    sum_utility_max: 27.87243628738625
    sum_utility_mean: 24.951153007417314
    sum_utility_min: 24.30750378202235
  date: 2022-04-28_04-55-44
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1407.0449971172516
  episode_reward_mean: 1280.4098756620647
  episode_reward_min: 1172.107847009634
  episodes_this_iter: 40
  episodes_total: 1760
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3965978622436523
          entropy_coeff: 0.0
          kl: 0.008620748296380043
          model: {}
          policy_loss: -0.009602298960089684
          total_loss: 34.323455810546875
          vf_explained_var: 0.9931799173355103
          vf_loss: 34.33047103881836
    num_agent_steps_sampled: 1408000
    num_agent_steps_trained: 1408000
    num_steps_sampled: 176000
    num_steps_trained: 176000
  iterations_since_restore: 44
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.33582887700534
    ram_util_percent: 37.37647058823529
  pid: 3889
  policy_reward_max:
    ue: 374.4657857022532
  policy_reward_mean:
    ue: 160.05123445775803
  policy_reward_min:
    ue: -2.0071039862971918
  sampler_perf:
    mean_action_processing_ms: 0.14668276128625615
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.90598660669268
    mean_inference_ms: 1.0240766850050038
    mean_raw_obs_processing_ms: 0.7227606989388236
  time_since_restore: 5468.890519142151
  time_this_iter_s: 134.20222401618958
  time_total_s: 5468.890519142151
  timers:
    learn_throughput: 127.319
    learn_time_ms: 31417.213
    load_throughput: 370510.099
    load_time_ms: 10.796
    sample_throughput: 40.083
    sample_time_ms: 99792.431
    update_time_ms: 4.49
  timestamp: 1651101944
  timesteps_since_restore: 0
  timesteps_total: 176000
  training_iteration: 44
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     44 |          5468.89 | 176000 |  1280.41 |              1407.04 |              1172.11 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1440000
  custom_metrics:
    eps_sum_utility_max: 1320.3961230168636
    eps_sum_utility_mean: 1249.3724119504045
    eps_sum_utility_min: 1077.6916839454962
    sum_utility_max: 27.87243628738625
    sum_utility_mean: 24.964005273018564
    sum_utility_min: 24.305914967930576
  date: 2022-04-28_04-57-54
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1407.0449971172516
  episode_reward_mean: 1282.527881020153
  episode_reward_min: 1063.0468238429057
  episodes_this_iter: 40
  episodes_total: 1800
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3970155715942383
          entropy_coeff: 0.0
          kl: 0.007887963205575943
          model: {}
          policy_loss: -0.009213150478899479
          total_loss: 36.94607162475586
          vf_explained_var: 0.9926965236663818
          vf_loss: 36.95292282104492
    num_agent_steps_sampled: 1440000
    num_agent_steps_trained: 1440000
    num_steps_sampled: 180000
    num_steps_trained: 180000
  iterations_since_restore: 45
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.11813186813187
    ram_util_percent: 37.387912087912085
  pid: 3889
  policy_reward_max:
    ue: 373.9900613729767
  policy_reward_mean:
    ue: 160.31598512751916
  policy_reward_min:
    ue: -31.841337742322995
  sampler_perf:
    mean_action_processing_ms: 0.1469047107884141
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.97888344842837
    mean_inference_ms: 1.025463130704776
    mean_raw_obs_processing_ms: 0.7239273179283481
  time_since_restore: 5599.443658590317
  time_this_iter_s: 130.5531394481659
  time_total_s: 5599.443658590317
  timers:
    learn_throughput: 127.333
    learn_time_ms: 31413.73
    load_throughput: 366043.823
    load_time_ms: 10.928
    sample_throughput: 40.086
    sample_time_ms: 99785.434
    update_time_ms: 4.431
  timestamp: 1651102074
  timesteps_since_restore: 0
  timesteps_total: 180000
  training_iteration: 45
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     45 |          5599.44 | 180000 |  1282.53 |              1407.04 |              1063.05 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1472000
  custom_metrics:
    eps_sum_utility_max: 1306.324749787008
    eps_sum_utility_mean: 1250.1586531131416
    eps_sum_utility_min: 1077.6916839454962
    sum_utility_max: 27.86516644925228
    sum_utility_mean: 24.907855833803506
    sum_utility_min: 24.305914967930576
  date: 2022-04-28_05-00-10
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1354.9124931827532
  episode_reward_mean: 1278.1854517354213
  episode_reward_min: 1063.0468238429057
  episodes_this_iter: 40
  episodes_total: 1840
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3834738731384277
          entropy_coeff: 0.0
          kl: 0.007472516968846321
          model: {}
          policy_loss: -0.008927283808588982
          total_loss: 33.618324279785156
          vf_explained_var: 0.993411660194397
          vf_loss: 33.62500762939453
    num_agent_steps_sampled: 1472000
    num_agent_steps_trained: 1472000
    num_steps_sampled: 184000
    num_steps_trained: 184000
  iterations_since_restore: 46
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.86223404255319
    ram_util_percent: 37.3968085106383
  pid: 3889
  policy_reward_max:
    ue: 374.192595162605
  policy_reward_mean:
    ue: 159.77318146692767
  policy_reward_min:
    ue: -31.841337742322995
  sampler_perf:
    mean_action_processing_ms: 0.1470909984982801
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 45.04078795590882
    mean_inference_ms: 1.0266310141989734
    mean_raw_obs_processing_ms: 0.7248660661350873
  time_since_restore: 5734.8152096271515
  time_this_iter_s: 135.37155103683472
  time_total_s: 5734.8152096271515
  timers:
    learn_throughput: 125.422
    learn_time_ms: 31892.433
    load_throughput: 371335.902
    load_time_ms: 10.772
    sample_throughput: 39.977
    sample_time_ms: 100056.664
    update_time_ms: 4.505
  timestamp: 1651102210
  timesteps_since_restore: 0
  timesteps_total: 184000
  training_iteration: 46
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     46 |          5734.82 | 184000 |  1278.19 |              1354.91 |              1063.05 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1504000
  custom_metrics:
    eps_sum_utility_max: 1306.220284453038
    eps_sum_utility_mean: 1258.8273984763398
    eps_sum_utility_min: 1117.5600545564828
    sum_utility_max: 25.033636146292817
    sum_utility_mean: 24.860190323317383
    sum_utility_min: 24.313409948982443
  date: 2022-04-28_05-02-24
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1362.4996722103606
  episode_reward_mean: 1292.5987732415315
  episode_reward_min: 1133.038190175196
  episodes_this_iter: 40
  episodes_total: 1880
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3855540752410889
          entropy_coeff: 0.0
          kl: 0.0072737885639071465
          model: {}
          policy_loss: -0.009203087538480759
          total_loss: 24.80427360534668
          vf_explained_var: 0.9950740337371826
          vf_loss: 24.81129264831543
    num_agent_steps_sampled: 1504000
    num_agent_steps_trained: 1504000
    num_steps_sampled: 188000
    num_steps_trained: 188000
  iterations_since_restore: 47
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.37486631016043
    ram_util_percent: 37.46256684491979
  pid: 3889
  policy_reward_max:
    ue: 374.192595162605
  policy_reward_mean:
    ue: 161.57484665519144
  policy_reward_min:
    ue: -19.87260822611608
  sampler_perf:
    mean_action_processing_ms: 0.1472983197499344
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 45.10849902805102
    mean_inference_ms: 1.027915308110389
    mean_raw_obs_processing_ms: 0.725888101140731
  time_since_restore: 5869.276677131653
  time_this_iter_s: 134.46146750450134
  time_total_s: 5869.276677131653
  timers:
    learn_throughput: 125.493
    learn_time_ms: 31874.181
    load_throughput: 389446.884
    load_time_ms: 10.271
    sample_throughput: 39.843
    sample_time_ms: 100392.965
    update_time_ms: 3.504
  timestamp: 1651102344
  timesteps_since_restore: 0
  timesteps_total: 188000
  training_iteration: 47
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     47 |          5869.28 | 188000 |   1292.6 |               1362.5 |              1133.04 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1536000
  custom_metrics:
    eps_sum_utility_max: 1310.7286444027252
    eps_sum_utility_mean: 1264.3118656813924
    eps_sum_utility_min: 1189.3297820651474
    sum_utility_max: 25.033636146292817
    sum_utility_mean: 24.85209900483303
    sum_utility_min: 24.309717867810523
  date: 2022-04-28_05-04-37
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1369.5437869490027
  episode_reward_mean: 1300.844072255606
  episode_reward_min: 1212.3668133439655
  episodes_this_iter: 40
  episodes_total: 1920
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3805525302886963
          entropy_coeff: 0.0
          kl: 0.007289935369044542
          model: {}
          policy_loss: -0.007846562191843987
          total_loss: 27.550668716430664
          vf_explained_var: 0.9945606589317322
          vf_loss: 27.55632781982422
    num_agent_steps_sampled: 1536000
    num_agent_steps_trained: 1536000
    num_steps_sampled: 192000
    num_steps_trained: 192000
  iterations_since_restore: 48
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.35567567567568
    ram_util_percent: 37.358378378378376
  pid: 3889
  policy_reward_max:
    ue: 373.53459063067737
  policy_reward_mean:
    ue: 162.60550903195076
  policy_reward_min:
    ue: -8.518846974490835
  sampler_perf:
    mean_action_processing_ms: 0.14750193489663954
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 45.175709122351726
    mean_inference_ms: 1.0292092299855227
    mean_raw_obs_processing_ms: 0.7269373722501481
  time_since_restore: 6001.880192041397
  time_this_iter_s: 132.60351490974426
  time_total_s: 6001.880192041397
  timers:
    learn_throughput: 125.674
    learn_time_ms: 31828.398
    load_throughput: 392321.935
    load_time_ms: 10.196
    sample_throughput: 39.81
    sample_time_ms: 100476.728
    update_time_ms: 3.4
  timestamp: 1651102477
  timesteps_since_restore: 0
  timesteps_total: 192000
  training_iteration: 48
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     48 |          6001.88 | 192000 |  1300.84 |              1369.54 |              1212.37 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1568000
  custom_metrics:
    eps_sum_utility_max: 1310.7286444027252
    eps_sum_utility_mean: 1266.1734520370417
    eps_sum_utility_min: 1205.831608703889
    sum_utility_max: 25.02792520800438
    sum_utility_mean: 24.749353244880965
    sum_utility_min: 21.104323543548706
  date: 2022-04-28_05-06-47
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1369.5437869490027
  episode_reward_mean: 1304.8151839472425
  episode_reward_min: 1212.3668133439655
  episodes_this_iter: 40
  episodes_total: 1960
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.369201898574829
          entropy_coeff: 0.0
          kl: 0.006963518448174
          model: {}
          policy_loss: -0.008460483513772488
          total_loss: 24.082599639892578
          vf_explained_var: 0.9952846765518188
          vf_loss: 24.088970184326172
    num_agent_steps_sampled: 1568000
    num_agent_steps_trained: 1568000
    num_steps_sampled: 196000
    num_steps_trained: 196000
  iterations_since_restore: 49
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.2756906077348
    ram_util_percent: 37.40718232044198
  pid: 3889
  policy_reward_max:
    ue: 375.70674887602325
  policy_reward_mean:
    ue: 163.1018979934053
  policy_reward_min:
    ue: -2.975194372791272
  sampler_perf:
    mean_action_processing_ms: 0.1476812349278983
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 45.23293921389369
    mean_inference_ms: 1.0303200002504058
    mean_raw_obs_processing_ms: 0.7278464900443024
  time_since_restore: 6131.8740882873535
  time_this_iter_s: 129.99389624595642
  time_total_s: 6131.8740882873535
  timers:
    learn_throughput: 125.762
    learn_time_ms: 31806.001
    load_throughput: 366672.626
    load_time_ms: 10.909
    sample_throughput: 40.034
    sample_time_ms: 99914.56
    update_time_ms: 3.387
  timestamp: 1651102607
  timesteps_since_restore: 0
  timesteps_total: 196000
  training_iteration: 49
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     49 |          6131.87 | 196000 |  1304.82 |              1369.54 |              1212.37 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_95ec4_00000:
  agent_timesteps_total: 1600000
  custom_metrics:
    eps_sum_utility_max: 1310.8556617238116
    eps_sum_utility_mean: 1268.7431401976519
    eps_sum_utility_min: 1205.831608703889
    sum_utility_max: 25.02792520800438
    sum_utility_mean: 24.782896228294575
    sum_utility_min: 21.104323543548706
  date: 2022-04-28_05-09-03
  done: true
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1374.0672794477912
  episode_reward_mean: 1307.5728964952693
  episode_reward_min: 1212.3668133439655
  episodes_this_iter: 40
  episodes_total: 2000
  experiment_id: 4d54074bcc084e92ac2969b754f3ba26
  hostname: abhishek-pc
  info:
    learner:
      ue:
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3487980365753174
          entropy_coeff: 0.0
          kl: 0.007095624227076769
          model: {}
          policy_loss: -0.008033748716115952
          total_loss: 25.620567321777344
          vf_explained_var: 0.9949430823326111
          vf_loss: 25.6264705657959
    num_agent_steps_sampled: 1600000
    num_agent_steps_trained: 1600000
    num_steps_sampled: 200000
    num_steps_trained: 200000
  iterations_since_restore: 50
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.96170212765957
    ram_util_percent: 37.405851063829786
  pid: 3889
  policy_reward_max:
    ue: 375.70674887602325
  policy_reward_mean:
    ue: 163.4466120619086
  policy_reward_min:
    ue: -2.975194372791272
  sampler_perf:
    mean_action_processing_ms: 0.1478200018914908
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 45.27625967291364
    mean_inference_ms: 1.0311806423861476
    mean_raw_obs_processing_ms: 0.7285277261658004
  time_since_restore: 6267.2378005981445
  time_this_iter_s: 135.36371231079102
  time_total_s: 6267.2378005981445
  timers:
    learn_throughput: 123.589
    learn_time_ms: 32365.434
    load_throughput: 364063.607
    load_time_ms: 10.987
    sample_throughput: 40.031
    sample_time_ms: 99921.825
    update_time_ms: 3.469
  timestamp: 1651102743
  timesteps_since_restore: 0
  timesteps_total: 200000
  training_iteration: 50
  trial_id: 95ec4_00000
  
== Status ==
Memory usage on this node: 2.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | RUNNING  | 10.0.3.106:3889 |     50 |          6267.24 | 200000 |  1307.57 |              1374.07 |              1212.37 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


== Status ==
Memory usage on this node: 2.8/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/3.91 GiB heap, 0.0/1.96 GiB objects
Result logdir: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17
Number of trials: 1/1 (1 TERMINATED)
+-------------------------------------+------------+-------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status     | loc   |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+------------+-------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_95ec4_00000 | TERMINATED |       |     50 |          6267.24 | 200000 |  1307.57 |              1374.07 |              1212.37 |                100 |
+-------------------------------------+------------+-------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


2022-04-28 05:09:04,108	INFO tune.py:549 -- Total run time: 6286.66 seconds (6285.45 seconds for the tuning loop).
INFO:deepcomp.util.simulation:Training done                  episode_reward_mean=1307.573 episodes_total=2000 log_dir=/home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17/PPO_MultiAgentMobileEnv_95ec4_00000_0_2022-04-28_03-24-19 num_steps_sampled=200000 num_steps_trained=200000 timesteps_total=200000
2022-04-28 05:09:04,262	INFO trainer.py:671 -- Tip: set framework=tfe or the --eager flag to enable TensorFlow eager execution
2022-04-28 05:09:04,262	WARNING deprecation.py:33 -- DeprecationWarning: `monitor` has been deprecated. Use `record_env` instead. This will raise an error in the future!
2022-04-28 05:09:04,262	INFO trainer.py:696 -- Current log_level is ERROR. For more information, set 'log_level': 'INFO' / 'DEBUG' or use the -v and -vv flags.
INFO:deepcomp.util.simulation:Loading PPO agent              checkpoint=/home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17/PPO_MultiAgentMobileEnv_95ec4_00000_0_2022-04-28_03-24-19/checkpoint_000050/checkpoint-50
2022-04-28 05:09:12,484	INFO trainable.py:377 -- Restored on 10.0.3.106 from checkpoint: /home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17/PPO_MultiAgentMobileEnv_95ec4_00000_0_2022-04-28_03-24-19/checkpoint_000050/checkpoint-50
2022-04-28 05:09:12,484	INFO trainable.py:385 -- Current state after restoring: {'_iteration': 50, '_timesteps_total': None, '_time_total': 6267.2378005981445, '_episodes_total': 2000}
INFO:deepcomp.util.simulation:Agent loaded                   agent=PPO checkpoint=None rllib_dir=/home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17/PPO_MultiAgentMobileEnv_95ec4_00000_0_2022-04-28_03-24-19/checkpoint_000050/checkpoint-50
INFO:deepcomp.util.simulation:Loaded training progress       progress_file=/home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17/PPO_MultiAgentMobileEnv_95ec4_00000_0_2022-04-28_03-24-19/progress.csv train_iteration=50 train_steps=200000
WARNING:deepcomp.util.simulation:Evaluating with a single worker for reproducibility and compatibility.
INFO:deepcomp.util.simulation:Starting evaluation            fast_ues=2 num_episodes=1 num_workers=1 slow_ues=5 static_ues=1
DEBUG:deepcomp.util.simulation:Step                           action={'1': 6, '2': 3, '3': 2, '4': 6, '5': 3, '6': 5, '7': 1, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.09], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.048, 1.0, 0.01, 0.002, 0.002, 0.004], 'utility': [0.125], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.004, 0.04], 'utility': [0.372], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.003, 1.0, 0.011], 'utility': [0.173], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.016, 1.0, 0.025, 0.004, 0.002, 0.003], 'utility': [0.162], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.03, 0.071, 0.584, 0.654, 0.076, 0.031], 'utility': [-0.178], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.004, 0.008, 0.016, 0.016], 'utility': [0.499], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.028, 0.009, 0.077, 1.0, 0.025, 0.006, 0.005], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.014, 0.044, 1.0, 0.01, 0.002, 0.002, 0.004], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.008, 0.002, 0.002, 0.003, 0.035], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.014], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '5': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.039, 0.016, 1.0, 0.029, 0.004, 0.002, 0.003], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '6': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.034, 0.083, 0.787, 0.714, 0.079, 0.033], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.013, 0.007, 0.009, 0.02, 0.055, 0.04], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '8': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.031, 0.011, 0.081, 1.0, 0.029, 0.007, 0.005], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}} reward={'1': 2.624, '2': 2.867, '3': 7.436, '4': 2.624, '5': 2.867, '6': 1.874, '7': 9.979, '8': -0.796} t=1
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 5, '3': 5, '4': 5, '5': 5, '6': 6, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.247], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.016, 0.053, 1.0, 0.01, 0.003, 0.002, 0.004], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.024, 1.0, 0.009, 0.002, 0.002, 0.004, 0.046], 'utility': [0.349], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.009], 'utility': [0.576], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.016, 1.0, 0.021, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.027, 0.06, 0.438, 0.595, 0.073, 0.029], 'utility': [-0.171], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.003, 0.002, 0.002, 0.002, 0.004, 0.005], 'utility': [0.717], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.026, 0.008, 0.075, 1.0, 0.021, 0.005, 0.004], 'utility': [0.002], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.09], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.048, 1.0, 0.01, 0.002, 0.002, 0.004], 'utility': [0.125], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.004, 0.04], 'utility': [0.372], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.003, 1.0, 0.011], 'utility': [0.173], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.016, 1.0, 0.025, 0.004, 0.002, 0.003], 'utility': [0.162], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.03, 0.071, 0.584, 0.654, 0.076, 0.031], 'utility': [-0.178], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.004, 0.008, 0.016, 0.016], 'utility': [0.499], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.028, 0.009, 0.077, 1.0, 0.025, 0.006, 0.005], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}} reward={'1': 3.289, '2': 2.968, '3': 6.99, '4': 3.289, '5': 2.968, '6': 3.658, '7': 14.337, '8': 0.048} t=2
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 5, '3': 5, '4': 5, '5': 5, '6': 6, '7': 5, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.057], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.017, 0.059, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.027, 1.0, 0.01, 0.003, 0.002, 0.004, 0.053], 'utility': [0.328], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.003, 1.0, 0.008], 'utility': [0.372], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.016, 1.0, 0.019, 0.003, 0.002, 0.003], 'utility': [0.212], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.052, 0.331, 0.538, 0.07, 0.027], 'utility': [-0.165], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.897], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.074, 1.0, 0.018, 0.005, 0.004], 'utility': [0.04], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.247], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.016, 0.053, 1.0, 0.01, 0.003, 0.002, 0.004], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.024, 1.0, 0.009, 0.002, 0.002, 0.004, 0.046], 'utility': [0.349], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.009], 'utility': [0.576], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.016, 1.0, 0.021, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.027, 0.06, 0.438, 0.595, 0.073, 0.029], 'utility': [-0.171], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.003, 0.002, 0.002, 0.002, 0.004, 0.005], 'utility': [0.717], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.026, 0.008, 0.075, 1.0, 0.021, 0.005, 0.004], 'utility': [0.002], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}} reward={'1': 4.291, '2': 3.087, '3': 6.553, '4': 4.291, '5': 3.087, '6': 5.153, '7': 17.949, '8': 0.808} t=3
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 5, '3': 5, '4': 5, '5': 5, '6': 6, '7': 5, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.149], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.019, 0.067, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.012], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.011, 0.003, 0.002, 0.005, 0.061], 'utility': [0.306], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.614], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.017, 1.0, 0.017, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.022, 0.044, 0.253, 0.485, 0.068, 0.026], 'utility': [-0.161], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.878], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.076, 1.0, 0.016, 0.004, 0.003], 'utility': [0.072], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.057], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.017, 0.059, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.027, 1.0, 0.01, 0.003, 0.002, 0.004, 0.053], 'utility': [0.328], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.003, 1.0, 0.008], 'utility': [0.372], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.016, 1.0, 0.019, 0.003, 0.002, 0.003], 'utility': [0.212], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.052, 0.331, 0.538, 0.07, 0.027], 'utility': [-0.165], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.897], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.074, 1.0, 0.018, 0.005, 0.004], 'utility': [0.04], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}} reward={'1': 4.652, '2': 3.056, '3': 6.125, '4': 4.652, '5': 3.056, '6': 7.164, '7': 17.551, '8': 1.444} t=4
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 5, '3': 5, '4': 5, '5': 5, '6': 6, '7': 5, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.033], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.077, 1.0, 0.012, 0.003, 0.002, 0.006], 'utility': [0.064], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.07], 'utility': [0.285], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.006], 'utility': [0.481], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.018, 1.0, 0.016, 0.003, 0.002, 0.003], 'utility': [0.236], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.02, 0.038, 0.196, 0.435, 0.067, 0.024], 'utility': [-0.159], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.003, 0.002, 0.002, 0.004], 'utility': [0.681], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.082, 1.0, 0.015, 0.004, 0.003], 'utility': [0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.149], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.019, 0.067, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.012], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.011, 0.003, 0.002, 0.005, 0.061], 'utility': [0.306], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.614], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.017, 1.0, 0.017, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.022, 0.044, 0.253, 0.485, 0.068, 0.026], 'utility': [-0.161], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.878], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.076, 1.0, 0.016, 0.004, 0.003], 'utility': [0.072], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}} reward={'1': 5.139, '2': 3.003, '3': 5.705, '4': 5.139, '5': 3.003, '6': 5.219, '7': 13.623, '8': 1.915} t=5
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 5, '3': 5, '4': 5, '5': 5, '6': 6, '7': 5, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.089, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.04, 1.0, 0.013, 0.004, 0.003, 0.006, 0.08], 'utility': [0.265], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.629], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.02, 1.0, 0.015, 0.003, 0.002, 0.003], 'utility': [0.282], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.019, 0.033, 0.153, 0.389, 0.066, 0.023], 'utility': [-0.16], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.022, 0.016, 0.007, 0.004, 0.005, 0.01], 'utility': [0.466], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.093, 1.0, 0.014, 0.004, 0.003], 'utility': [0.109], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.033], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.077, 1.0, 0.012, 0.003, 0.002, 0.006], 'utility': [0.064], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.07], 'utility': [0.285], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.006], 'utility': [0.481], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.018, 1.0, 0.016, 0.003, 0.002, 0.003], 'utility': [0.236], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.02, 0.038, 0.196, 0.435, 0.067, 0.024], 'utility': [-0.159], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.003, 0.002, 0.002, 0.004], 'utility': [0.681], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.082, 1.0, 0.015, 0.004, 0.003], 'utility': [0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}} reward={'1': 5.327, '2': 2.847, '3': 5.295, '4': 5.327, '5': 2.847, '6': 3.065, '7': 9.32, '8': 2.183} t=6
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 5, '3': 5, '4': 5, '5': 5, '6': 1, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.017], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.104, 1.0, 0.013, 0.004, 0.003, 0.007], 'utility': [0.028], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.045, 1.0, 0.014, 0.004, 0.003, 0.007, 0.092], 'utility': [0.245], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.53], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.022, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.237], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.028, 0.122, 0.349, 0.066, 0.023], 'utility': [0.031], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.052, 0.017, 0.009, 0.009, 0.019], 'utility': [0.13], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.027, 0.008, 0.113, 1.0, 0.015, 0.004, 0.004], 'utility': [0.111], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.089, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.04, 1.0, 0.013, 0.004, 0.003, 0.006, 0.08], 'utility': [0.265], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.629], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.02, 1.0, 0.015, 0.003, 0.002, 0.003], 'utility': [0.282], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.019, 0.033, 0.153, 0.389, 0.066, 0.023], 'utility': [-0.16], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.022, 0.016, 0.007, 0.004, 0.005, 0.01], 'utility': [0.466], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.093, 1.0, 0.014, 0.004, 0.003], 'utility': [0.109], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.466, 0.265, 0.142, 0.109, -0.16, 0.266, 0.0]}} reward={'1': 5.466, '2': 2.651, '3': 4.892, '4': 5.466, '5': 2.651, '6': 1.286, '7': 1.615, '8': 2.225} t=7
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 4, '3': 7, '4': 4, '5': 4, '6': 2, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.123, 1.0, 0.014, 0.004, 0.003, 0.008], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.051, 1.0, 0.016, 0.004, 0.004, 0.008, 0.105], 'utility': [0.247], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.61], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.025, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.256], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.016, 0.025, 0.098, 0.314, 0.067, 0.022], 'utility': [0.041], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.149, 0.15, 0.036, 0.016, 0.015, 0.033], 'utility': [-0.025], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.032, 0.01, 0.146, 1.0, 0.016, 0.004, 0.004], 'utility': [0.102], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.017], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.104, 1.0, 0.013, 0.004, 0.003, 0.007], 'utility': [0.028], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.045, 1.0, 0.014, 0.004, 0.003, 0.007, 0.092], 'utility': [0.245], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.53], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.022, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.237], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.028, 0.122, 0.349, 0.066, 0.023], 'utility': [0.031], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.052, 0.017, 0.009, 0.009, 0.019], 'utility': [0.13], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.027, 0.008, 0.113, 1.0, 0.015, 0.004, 0.004], 'utility': [0.111], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.081, 0.245, 0.133, 0.111, 0.031, 0.273, 0.0]}} reward={'1': 5.47, '2': 2.384, '3': 4.93, '4': 5.47, '5': 2.384, '6': 0.384, '7': 2.006, '8': 2.037} t=8
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 2, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.147, 1.0, 0.015, 0.004, 0.004, 0.009], 'utility': [-0.011], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.057, 1.0, 0.017, 0.005, 0.004, 0.009, 0.119], 'utility': [0.23], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.526], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.029, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.218], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.022, 0.081, 0.283, 0.069, 0.022], 'utility': [0.049], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.31, 0.401, 0.064, 0.025, 0.022, 0.05], 'utility': [-0.155], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.039, 0.012, 0.201, 1.0, 0.017, 0.005, 0.005], 'utility': [0.082], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.123, 1.0, 0.014, 0.004, 0.003, 0.008], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.051, 1.0, 0.016, 0.004, 0.004, 0.008, 0.105], 'utility': [0.247], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.61], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.025, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.256], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.016, 0.025, 0.098, 0.314, 0.067, 0.022], 'utility': [0.041], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.149, 0.15, 0.036, 0.016, 0.015, 0.033], 'utility': [-0.025], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.032, 0.01, 0.146, 1.0, 0.016, 0.004, 0.004], 'utility': [0.102], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}} reward={'1': 5.335, '2': 2.917, '3': 4.601, '4': 5.335, '5': 2.075, '6': -0.384, '7': 1.324, '8': 1.928} t=9
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 2, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.176, 1.0, 0.017, 0.005, 0.004, 0.01], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.064, 1.0, 0.019, 0.005, 0.005, 0.01, 0.136], 'utility': [0.214], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.558], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.034, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.219], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.02, 0.068, 0.258, 0.073, 0.022], 'utility': [0.054], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [0.986, 0.559, 1.0, 0.103, 0.035, 0.031, 0.07], 'utility': [-0.268], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.05, 0.015, 0.291, 1.0, 0.02, 0.006, 0.006], 'utility': [0.053], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.147, 1.0, 0.015, 0.004, 0.004, 0.009], 'utility': [-0.011], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.057, 1.0, 0.017, 0.005, 0.004, 0.009, 0.119], 'utility': [0.23], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.526], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.029, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.218], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.022, 0.081, 0.283, 0.069, 0.022], 'utility': [0.049], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.31, 0.401, 0.064, 0.025, 0.022, 0.05], 'utility': [-0.155], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.039, 0.012, 0.201, 1.0, 0.017, 0.005, 0.005], 'utility': [0.082], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}} reward={'1': 5.156, '2': 2.574, '3': 4.286, '4': 5.156, '5': 1.718, '6': -1.063, '7': 0.689, '8': 1.497} t=10
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 2, '7': 3, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.001], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.041, 0.213, 1.0, 0.018, 0.005, 0.005, 0.011], 'utility': [-0.144], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.072, 1.0, 0.02, 0.006, 0.005, 0.011, 0.154], 'utility': [0.199], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.0, 0.001, 0.004, 1.0, 0.006], 'utility': [0.483], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.039, 0.04, 1.0, 0.014, 0.003, 0.002, 0.005], 'utility': [0.093], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.019, 0.058, 0.237, 0.078, 0.023], 'utility': [0.057], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.402, 0.371, 1.0, 0.063, 0.019, 0.017, 0.038], 'utility': [-0.171], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.067, 0.02, 0.442, 1.0, 0.023, 0.008, 0.007], 'utility': [0.022], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.176, 1.0, 0.017, 0.005, 0.004, 0.01], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.064, 1.0, 0.019, 0.005, 0.005, 0.01, 0.136], 'utility': [0.214], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.558], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.034, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.219], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.02, 0.068, 0.258, 0.073, 0.022], 'utility': [0.054], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [0.986, 0.559, 1.0, 0.103, 0.035, 0.031, 0.07], 'utility': [-0.268], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.05, 0.015, 0.291, 1.0, 0.02, 0.006, 0.006], 'utility': [0.053], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.107, 0.214, 0.086, 0.053, 0.054, 0.258, 0.214]}} reward={'1': 4.839, '2': -0.002, '3': 3.985, '4': 4.839, '5': -0.998, '6': -0.379, '7': -0.326, '8': -0.712} t=11
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 2, '7': 4, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.029], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.047, 0.259, 1.0, 0.02, 0.006, 0.005, 0.013], 'utility': [-0.239], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 1.0, 0.022, 0.006, 0.006, 0.013, 0.174], 'utility': [0.185], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.001, 0.001, 0.001, 0.005, 1.0, 0.007], 'utility': [0.481], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.048, 1.0, 0.015, 0.003, 0.003, 0.005], 'utility': [0.016], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.018, 0.051, 0.221, 0.086, 0.024], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.167, 0.227, 1.0, 0.037, 0.011, 0.009, 0.02], 'utility': [-0.081], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.091, 0.027, 0.695, 1.0, 0.028, 0.009, 0.009], 'utility': [-0.017], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.001], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.041, 0.213, 1.0, 0.018, 0.005, 0.005, 0.011], 'utility': [-0.144], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.072, 1.0, 0.02, 0.006, 0.005, 0.011, 0.154], 'utility': [0.199], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.0, 0.001, 0.004, 1.0, 0.006], 'utility': [0.483], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.039, 0.04, 1.0, 0.014, 0.003, 0.002, 0.005], 'utility': [0.093], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.019, 0.058, 0.237, 0.078, 0.023], 'utility': [0.057], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.402, 0.371, 1.0, 0.063, 0.019, 0.017, 0.038], 'utility': [-0.171], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.067, 0.02, 0.442, 1.0, 0.023, 0.008, 0.007], 'utility': [0.022], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.057, 0.199, -0.05, 0.022, 0.057, 0.242, 0.199]}} reward={'1': 4.524, '2': -0.547, '3': 3.698, '4': 4.524, '5': -1.608, '6': 3.415, '7': -0.547, '8': -1.354} t=12
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 2, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.003], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.054, 0.317, 1.0, 0.021, 0.006, 0.006, 0.015], 'utility': [-0.203], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.089, 1.0, 0.023, 0.007, 0.006, 0.014, 0.198], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.011, 0.001, 0.001, 0.001, 0.006, 1.0, 0.008], 'utility': [0.414], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.059, 1.0, 0.016, 0.004, 0.003, 0.006], 'utility': [0.032], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.017, 0.046, 0.209, 0.097, 0.026], 'utility': [0.169], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.072, 0.131, 1.0, 0.021, 0.006, 0.005, 0.01], 'utility': [-0.059], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.112, 0.033, 1.0, 0.89, 0.031, 0.011, 0.011], 'utility': [-0.051], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.029], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.047, 0.259, 1.0, 0.02, 0.006, 0.005, 0.013], 'utility': [-0.239], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 1.0, 0.022, 0.006, 0.006, 0.013, 0.174], 'utility': [0.185], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.001, 0.001, 0.001, 0.005, 1.0, 0.007], 'utility': [0.481], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.048, 1.0, 0.015, 0.003, 0.003, 0.005], 'utility': [0.016], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.018, 0.051, 0.221, 0.086, 0.024], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.167, 0.227, 1.0, 0.037, 0.011, 0.009, 0.02], 'utility': [-0.081], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.091, 0.027, 0.695, 1.0, 0.028, 0.009, 0.009], 'utility': [-0.017], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}} reward={'1': 4.113, '2': -0.439, '3': 3.427, '4': 4.113, '5': -1.405, '6': 3.372, '7': -0.439, '8': -1.326} t=13
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 2, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.061, 0.39, 1.0, 0.023, 0.007, 0.007, 0.017], 'utility': [-0.279], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.1, 1.0, 0.025, 0.008, 0.007, 0.016, 0.223], 'utility': [0.159], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.014, 0.001, 0.001, 0.001, 0.008, 1.0, 0.009], 'utility': [0.394], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.05, 0.072, 1.0, 0.017, 0.004, 0.003, 0.007], 'utility': [-0.036], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.043, 0.2, 0.112, 0.028], 'utility': [0.163], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.075, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.088], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.094, 0.028, 1.0, 0.539, 0.023, 0.008, 0.009], 'utility': [-0.073], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.003], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.054, 0.317, 1.0, 0.021, 0.006, 0.006, 0.015], 'utility': [-0.203], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.089, 1.0, 0.023, 0.007, 0.006, 0.014, 0.198], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.011, 0.001, 0.001, 0.001, 0.006, 1.0, 0.008], 'utility': [0.414], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.059, 1.0, 0.016, 0.004, 0.003, 0.006], 'utility': [0.032], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.017, 0.046, 0.209, 0.097, 0.026], 'utility': [0.169], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.072, 0.131, 1.0, 0.021, 0.006, 0.005, 0.01], 'utility': [-0.059], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.112, 0.033, 1.0, 0.89, 0.031, 0.011, 0.011], 'utility': [-0.051], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}} reward={'1': 3.724, '2': -0.566, '3': 3.171, '4': 3.724, '5': -1.5, '6': 3.254, '7': -0.566, '8': -1.492} t=14
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 4, '4': 4, '5': 4, '6': 2, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.007], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.071, 0.481, 1.0, 0.025, 0.008, 0.007, 0.02], 'utility': [-0.255], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.111, 1.0, 0.027, 0.008, 0.007, 0.017, 0.252], 'utility': [0.146], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.018, 0.002, 0.001, 0.002, 0.011, 1.0, 0.011], 'utility': [0.335], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.055, 0.089, 1.0, 0.018, 0.004, 0.004, 0.008], 'utility': [-0.027], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.04, 0.194, 0.132, 0.032], 'utility': [0.153], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.014], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.078, 0.024, 1.0, 0.323, 0.016, 0.006, 0.007], 'utility': [-0.069], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.061, 0.39, 1.0, 0.023, 0.007, 0.007, 0.017], 'utility': [-0.279], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.1, 1.0, 0.025, 0.008, 0.007, 0.016, 0.223], 'utility': [0.159], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.014, 0.001, 0.001, 0.001, 0.008, 1.0, 0.009], 'utility': [0.394], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.05, 0.072, 1.0, 0.017, 0.004, 0.003, 0.007], 'utility': [-0.036], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.043, 0.2, 0.112, 0.028], 'utility': [0.163], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.075, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.088], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.094, 0.028, 1.0, 0.539, 0.023, 0.008, 0.009], 'utility': [-0.073], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}} reward={'1': 3.282, '2': -0.762, '3': 2.93, '4': 3.282, '5': -0.762, '6': 3.063, '7': -0.762, '8': -1.623} t=15
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 4, '4': 4, '5': 4, '6': 2, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.018], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.081, 0.596, 1.0, 0.028, 0.009, 0.008, 0.023], 'utility': [-0.323], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.123, 1.0, 0.029, 0.009, 0.008, 0.019, 0.284], 'utility': [0.135], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.002, 0.001, 0.002, 0.014, 1.0, 0.012], 'utility': [0.305], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.061, 0.11, 1.0, 0.019, 0.005, 0.004, 0.009], 'utility': [-0.093], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.016, 0.038, 0.191, 0.16, 0.036], 'utility': [0.14], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.058], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.065, 0.02, 1.0, 0.192, 0.012, 0.005, 0.006], 'utility': [-0.042], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.007], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.071, 0.481, 1.0, 0.025, 0.008, 0.007, 0.02], 'utility': [-0.255], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.111, 1.0, 0.027, 0.008, 0.007, 0.017, 0.252], 'utility': [0.146], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.018, 0.002, 0.001, 0.002, 0.011, 1.0, 0.011], 'utility': [0.335], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.055, 0.089, 1.0, 0.018, 0.004, 0.004, 0.008], 'utility': [-0.027], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.04, 0.194, 0.132, 0.032], 'utility': [0.153], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.014], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.078, 0.024, 1.0, 0.323, 0.016, 0.006, 0.007], 'utility': [-0.069], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.069, 0.153, 0.164, 0.146]}} reward={'1': 2.867, '2': -1.059, '3': 2.704, '4': 2.867, '5': -1.059, '6': 2.804, '7': -1.059, '8': -1.769} t=16
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 4, '4': 4, '5': 4, '6': 2, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.093, 0.742, 1.0, 0.03, 0.01, 0.01, 0.027], 'utility': [-0.325], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.136, 1.0, 0.031, 0.01, 0.009, 0.021, 0.32], 'utility': [0.125], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.029, 0.003, 0.002, 0.003, 0.018, 1.0, 0.015], 'utility': [0.252], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.137, 1.0, 0.02, 0.005, 0.004, 0.01], 'utility': [-0.107], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.018, 0.017, 0.038, 0.19, 0.197, 0.042], 'utility': [0.124], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.007], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.017, 1.0, 0.116, 0.009, 0.004, 0.005], 'utility': [-0.006], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.018], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.081, 0.596, 1.0, 0.028, 0.009, 0.008, 0.023], 'utility': [-0.323], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.123, 1.0, 0.029, 0.009, 0.008, 0.019, 0.284], 'utility': [0.135], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.002, 0.001, 0.002, 0.014, 1.0, 0.012], 'utility': [0.305], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.061, 0.11, 1.0, 0.019, 0.005, 0.004, 0.009], 'utility': [-0.093], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.016, 0.038, 0.191, 0.16, 0.036], 'utility': [0.14], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.058], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.065, 0.02, 1.0, 0.192, 0.012, 0.005, 0.006], 'utility': [-0.042], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}} reward={'1': 2.429, '2': -1.223, '3': 2.495, '4': 2.429, '5': -1.223, '6': 2.456, '7': -1.223, '8': -1.746} t=17
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 2, '3': 4, '4': 4, '5': 4, '6': 2, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.106, 0.928, 1.0, 0.033, 0.011, 0.011, 0.031], 'utility': [-0.135], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.151, 1.0, 0.033, 0.011, 0.01, 0.023, 0.36], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.038, 0.003, 0.002, 0.004, 0.024, 1.0, 0.017], 'utility': [0.218], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.073, 0.172, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.112], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.02, 0.018, 0.038, 0.192, 0.247, 0.049], 'utility': [0.105], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.07, 0.177, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.234], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.045, 0.015, 1.0, 0.071, 0.006, 0.003, 0.004], 'utility': [0.103], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.093, 0.742, 1.0, 0.03, 0.01, 0.01, 0.027], 'utility': [-0.325], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.136, 1.0, 0.031, 0.01, 0.009, 0.021, 0.32], 'utility': [0.125], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.029, 0.003, 0.002, 0.003, 0.018, 1.0, 0.015], 'utility': [0.252], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.137, 1.0, 0.02, 0.005, 0.004, 0.01], 'utility': [-0.107], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.018, 0.017, 0.038, 0.19, 0.197, 0.042], 'utility': [0.124], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.007], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.017, 1.0, 0.116, 0.009, 0.004, 0.005], 'utility': [-0.006], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.125, -0.108, -0.006, 0.124, 0.121, 0.125]}} reward={'1': 2.016, '2': -1.779, '3': -1.189, '4': 2.016, '5': -1.779, '6': 2.062, '7': -1.779, '8': -1.885} t=18
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 1, '3': 4, '4': 2, '5': 0, '6': 2, '7': 0, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.011], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.105, 1.0, 0.86, 0.031, 0.011, 0.011, 0.031], 'utility': [-0.121], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.167, 1.0, 0.035, 0.012, 0.011, 0.026, 0.404], 'utility': [-0.012], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.049, 0.004, 0.003, 0.005, 0.031, 1.0, 0.02], 'utility': [0.171], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.08, 0.215, 1.0, 0.023, 0.007, 0.006, 0.014], 'utility': [-0.115], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.022, 0.019, 0.038, 0.195, 0.314, 0.059], 'utility': [0.046], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.18, 0.471, 1.0, 0.039, 0.012, 0.011, 0.028], 'utility': [-0.263], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.106, 0.928, 1.0, 0.033, 0.011, 0.011, 0.031], 'utility': [-0.135], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.151, 1.0, 0.033, 0.011, 0.01, 0.023, 0.36], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.038, 0.003, 0.002, 0.004, 0.024, 1.0, 0.017], 'utility': [0.218], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.073, 0.172, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.112], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.02, 0.018, 0.038, 0.192, 0.247, 0.049], 'utility': [0.105], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.07, 0.177, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.234], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.045, 0.015, 1.0, 0.071, 0.006, 0.003, 0.004], 'utility': [0.103], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.078, -0.094, 0.0, 0.105, 0.101, -0.022]}} reward={'1': 1.597, '2': -2.032, '3': -0.963, '4': 1.597, '5': -2.032, '6': 1.37, '7': -2.032, '8': -2.384} t=19
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 1, '3': 4, '4': 1, '5': 0, '6': 5, '7': 0, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.095, 1.0, 0.683, 0.027, 0.009, 0.009, 0.028], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.184, 1.0, 0.037, 0.013, 0.012, 0.029, 0.453], 'utility': [-0.002], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.062, 0.005, 0.003, 0.006, 0.04, 1.0, 0.023], 'utility': [0.136], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.088, 0.269, 1.0, 0.025, 0.007, 0.006, 0.016], 'utility': [-0.16], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.024, 0.02, 0.039, 0.2, 0.406, 0.071], 'utility': [0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.377, 1.0, 0.887, 0.057, 0.021, 0.02, 0.056], 'utility': [-0.439], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.089], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.011], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.105, 1.0, 0.86, 0.031, 0.011, 0.011, 0.031], 'utility': [-0.121], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.167, 1.0, 0.035, 0.012, 0.011, 0.026, 0.404], 'utility': [-0.012], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.049, 0.004, 0.003, 0.005, 0.031, 1.0, 0.02], 'utility': [0.171], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.08, 0.215, 1.0, 0.023, 0.007, 0.006, 0.014], 'utility': [-0.115], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.022, 0.019, 0.038, 0.195, 0.314, 0.059], 'utility': [0.046], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.18, 0.471, 1.0, 0.039, 0.012, 0.011, 0.028], 'utility': [-0.263], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.066, -0.119, 0.0, 0.0, 0.08, -0.012]}} reward={'1': 1.2, '2': -2.51, '3': -0.83, '4': 1.2, '5': -2.51, '6': 0.948, '7': -2.088, '8': -3.153} t=20
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 1, '3': 4, '4': 1, '5': 0, '6': 6, '7': 2, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.54, 0.023, 0.008, 0.008, 0.026], 'utility': [-0.181], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.203, 1.0, 0.04, 0.014, 0.013, 0.031, 0.507], 'utility': [-0.038], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.078, 0.006, 0.004, 0.007, 0.052, 1.0, 0.026], 'utility': [0.07], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.096, 0.338, 1.0, 0.027, 0.008, 0.007, 0.018], 'utility': [-0.142], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.027, 0.021, 0.04, 0.206, 0.531, 0.086], 'utility': [0.008], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.393, 1.0, 0.421, 0.042, 0.017, 0.019, 0.057], 'utility': [-0.215], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.068], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.095, 1.0, 0.683, 0.027, 0.009, 0.009, 0.028], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.184, 1.0, 0.037, 0.013, 0.012, 0.029, 0.453], 'utility': [-0.002], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.062, 0.005, 0.003, 0.006, 0.04, 1.0, 0.023], 'utility': [0.136], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.088, 0.269, 1.0, 0.025, 0.007, 0.006, 0.016], 'utility': [-0.16], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.024, 0.02, 0.039, 0.2, 0.406, 0.071], 'utility': [0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.377, 1.0, 0.887, 0.057, 0.021, 0.02, 0.056], 'utility': [-0.439], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.089], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.158, 0.0, 0.0, 0.06, -0.002]}} reward={'1': 0.28, '2': -2.584, '3': -2.361, '4': 0.28, '5': -2.584, '6': 0.252, '7': -2.24, '8': -2.351} t=21
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 1, '3': 1, '4': 1, '5': 0, '6': 5, '7': 1, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.064], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.077, 1.0, 0.426, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.176], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.224, 1.0, 0.042, 0.015, 0.014, 0.035, 0.567], 'utility': [-0.026], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.098, 0.007, 0.005, 0.009, 0.067, 1.0, 0.03], 'utility': [0.011], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.105, 0.424, 1.0, 0.028, 0.009, 0.008, 0.021], 'utility': [-0.177], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.031, 0.023, 0.042, 0.214, 0.702, 0.104], 'utility': [-0.127], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.438, 1.0, 0.232, 0.033, 0.016, 0.019, 0.065], 'utility': [-0.117], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.017, 1.0, 0.038, 0.005, 0.003, 0.004], 'utility': [0.169], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.54, 0.023, 0.008, 0.008, 0.026], 'utility': [-0.181], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.203, 1.0, 0.04, 0.014, 0.013, 0.031, 0.507], 'utility': [-0.038], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.078, 0.006, 0.004, 0.007, 0.052, 1.0, 0.026], 'utility': [0.07], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.096, 0.338, 1.0, 0.027, 0.008, 0.007, 0.018], 'utility': [-0.142], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.027, 0.021, 0.04, 0.206, 0.531, 0.086], 'utility': [0.008], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.393, 1.0, 0.421, 0.042, 0.017, 0.019, 0.057], 'utility': [-0.215], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.068], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.008, -0.145, -0.118, 0.0, 0.0, 0.014, -0.038]}} reward={'1': -1.2, '2': -1.678, '3': -1.727, '4': -1.695, '5': -1.678, '6': -1.695, '7': -2.253, '8': -1.227} t=22
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 1, '3': 1, '4': 1, '5': 0, '6': 5, '7': 3, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.077], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.069, 1.0, 0.334, 0.017, 0.006, 0.007, 0.021], 'utility': [-0.17], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.246, 1.0, 0.044, 0.016, 0.015, 0.038, 0.633], 'utility': [-0.018], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.123, 0.008, 0.006, 0.011, 0.085, 1.0, 0.034], 'utility': [-0.033], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.114, 0.531, 1.0, 0.031, 0.01, 0.009, 0.024], 'utility': [-0.144], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.034, 0.025, 0.044, 0.222, 0.935, 0.128], 'utility': [-0.171], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.529, 1.0, 0.152, 0.029, 0.016, 0.022, 0.085], 'utility': [-0.129], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.028, 1.0, 0.034, 0.005, 0.003, 0.005], 'utility': [0.058], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.064], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.077, 1.0, 0.426, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.176], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.224, 1.0, 0.042, 0.015, 0.014, 0.035, 0.567], 'utility': [-0.026], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.098, 0.007, 0.005, 0.009, 0.067, 1.0, 0.03], 'utility': [0.011], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.105, 0.424, 1.0, 0.028, 0.009, 0.008, 0.021], 'utility': [-0.177], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.031, 0.023, 0.042, 0.214, 0.702, 0.104], 'utility': [-0.127], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.438, 1.0, 0.232, 0.033, 0.016, 0.019, 0.065], 'utility': [-0.117], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.017, 1.0, 0.038, 0.005, 0.003, 0.004], 'utility': [0.169], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.122, -0.106, -0.061, 0.0, 0.0, -0.06, -0.026]}} reward={'1': -1.871, '2': -1.91, '3': -1.679, '4': -2.044, '5': -1.91, '6': -2.044, '7': -2.166, '8': -1.705} t=23
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 1, '3': 1, '4': 4, '5': 0, '6': 5, '7': 3, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.083], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.061, 1.0, 0.261, 0.014, 0.006, 0.006, 0.019], 'utility': [-0.179], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.27, 1.0, 0.047, 0.017, 0.016, 0.042, 0.707], 'utility': [-0.015], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.152, 0.009, 0.007, 0.014, 0.108, 1.0, 0.038], 'utility': [-0.06], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.123, 0.667, 1.0, 0.033, 0.011, 0.01, 0.028], 'utility': [-0.196], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.798, 0.031, 0.021, 0.036, 0.185, 1.0, 0.125], 'utility': [-0.166], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.68, 1.0, 0.117, 0.029, 0.019, 0.029, 0.131], 'utility': [-0.12], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.117, 0.059, 1.0, 0.038, 0.008, 0.005, 0.009], 'utility': [0.002], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.077], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.069, 1.0, 0.334, 0.017, 0.006, 0.007, 0.021], 'utility': [-0.17], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.246, 1.0, 0.044, 0.016, 0.015, 0.038, 0.633], 'utility': [-0.018], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.123, 0.008, 0.006, 0.011, 0.085, 1.0, 0.034], 'utility': [-0.033], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.114, 0.531, 1.0, 0.031, 0.01, 0.009, 0.024], 'utility': [-0.144], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.034, 0.025, 0.044, 0.222, 0.935, 0.128], 'utility': [-0.171], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.529, 1.0, 0.152, 0.029, 0.016, 0.022, 0.085], 'utility': [-0.129], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.028, 1.0, 0.034, 0.005, 0.003, 0.005], 'utility': [0.058], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.111, -0.106, -0.085, 0.0, 0.0, -0.094, -0.018]}} reward={'1': -2.06, '2': -2.289, '3': -1.645, '4': -2.184, '5': -2.289, '6': -2.184, '7': -2.201, '8': -2.396} t=24
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 4, '3': 2, '4': 4, '5': 0, '6': 4, '7': 3, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.087], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.054, 1.0, 0.203, 0.012, 0.005, 0.005, 0.017], 'utility': [-0.104], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.296, 1.0, 0.05, 0.018, 0.018, 0.046, 0.788], 'utility': [-0.108], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.188, 0.011, 0.008, 0.017, 0.137, 1.0, 0.043], 'utility': [-0.099], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.133, 0.836, 1.0, 0.035, 0.012, 0.011, 0.031], 'utility': [-0.176], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.592, 0.026, 0.017, 0.029, 0.143, 1.0, 0.114], 'utility': [-0.146], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.888, 1.0, 0.105, 0.032, 0.024, 0.042, 0.235], 'utility': [-0.049], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.215, 0.144, 1.0, 0.047, 0.012, 0.009, 0.018], 'utility': [-0.126], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.083], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.061, 1.0, 0.261, 0.014, 0.006, 0.006, 0.019], 'utility': [-0.179], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.27, 1.0, 0.047, 0.017, 0.016, 0.042, 0.707], 'utility': [-0.015], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.152, 0.009, 0.007, 0.014, 0.108, 1.0, 0.038], 'utility': [-0.06], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.123, 0.667, 1.0, 0.033, 0.011, 0.01, 0.028], 'utility': [-0.196], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.798, 0.031, 0.021, 0.036, 0.185, 1.0, 0.125], 'utility': [-0.166], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.68, 1.0, 0.117, 0.029, 0.019, 0.029, 0.131], 'utility': [-0.12], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.117, 0.059, 1.0, 0.038, 0.008, 0.005, 0.009], 'utility': [0.002], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.115, -0.105, -0.124, 0.0, 0.0, -0.103, -0.015]}} reward={'1': -2.216, '2': -2.235, '3': -1.74, '4': -2.089, '5': -2.235, '6': -2.089, '7': -1.788, '8': -2.334} t=25
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 4, '3': 2, '4': 4, '5': 2, '6': 4, '7': 7, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.101], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.047, 1.0, 0.158, 0.01, 0.004, 0.005, 0.016], 'utility': [-0.246], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.324, 1.0, 0.052, 0.019, 0.019, 0.05, 0.877], 'utility': [-0.036], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.229, 0.013, 0.01, 0.02, 0.173, 1.0, 0.048], 'utility': [-0.139], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.955, 0.036, 0.012, 0.012, 0.034], 'utility': [-0.164], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.438, 0.022, 0.014, 0.022, 0.11, 1.0, 0.103], 'utility': [-0.135], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.887, 0.092, 0.033, 0.029, 0.06, 0.42], 'utility': [-0.209], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '8': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.377, 0.372, 1.0, 0.061, 0.019, 0.016, 0.037], 'utility': [-0.18], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.087], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.054, 1.0, 0.203, 0.012, 0.005, 0.005, 0.017], 'utility': [-0.104], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.296, 1.0, 0.05, 0.018, 0.018, 0.046, 0.788], 'utility': [-0.108], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.188, 0.011, 0.008, 0.017, 0.137, 1.0, 0.043], 'utility': [-0.099], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.133, 0.836, 1.0, 0.035, 0.012, 0.011, 0.031], 'utility': [-0.176], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.592, 0.026, 0.017, 0.029, 0.143, 1.0, 0.114], 'utility': [-0.146], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.888, 1.0, 0.105, 0.032, 0.024, 0.042, 0.235], 'utility': [-0.049], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.215, 0.144, 1.0, 0.047, 0.012, 0.009, 0.018], 'utility': [-0.126], 'ues_at_bs': [0.375, 0.25, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.098, -0.076, -0.135, 0.0, 0.0, -0.111, -0.108]}} reward={'1': -2.503, '2': -3.562, '3': -2.769, '4': -2.969, '5': -3.562, '6': -2.969, '7': -3.013, '8': -3.473} t=26
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 1, '3': 2, '4': 4, '5': 1, '6': 4, '7': 7, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.095], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.122, 0.008, 0.003, 0.004, 0.014], 'utility': [-0.229], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.354, 1.0, 0.055, 0.021, 0.021, 0.055, 0.975], 'utility': [-0.24], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.278, 0.015, 0.012, 0.025, 0.218, 1.0, 0.053], 'utility': [-0.169], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.117, 1.0, 0.762, 0.03, 0.011, 0.011, 0.031], 'utility': [-0.139], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.324, 0.018, 0.011, 0.017, 0.085, 1.0, 0.094], 'utility': [-0.112], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.739, 0.08, 0.033, 0.034, 0.083, 0.776], 'utility': [-0.097], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '8': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.601, 0.998, 1.0, 0.078, 0.028, 0.027, 0.072], 'utility': [-0.257], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.101], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.047, 1.0, 0.158, 0.01, 0.004, 0.005, 0.016], 'utility': [-0.246], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.324, 1.0, 0.052, 0.019, 0.019, 0.05, 0.877], 'utility': [-0.036], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.229, 0.013, 0.01, 0.02, 0.173, 1.0, 0.048], 'utility': [-0.139], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.955, 0.036, 0.012, 0.012, 0.034], 'utility': [-0.164], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.438, 0.022, 0.014, 0.022, 0.11, 1.0, 0.103], 'utility': [-0.135], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.887, 0.092, 0.033, 0.029, 0.06, 0.42], 'utility': [-0.209], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}, '8': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.377, 0.372, 1.0, 0.061, 0.019, 0.016, 0.037], 'utility': [-0.18], 'ues_at_bs': [0.5, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.166, -0.164, -0.197, 0.0, 0.0, -0.125, -0.036]}} reward={'1': -2.51, '2': -3.638, '3': -3.208, '4': -2.89, '5': -3.638, '6': -2.89, '7': -3.194, '8': -3.453} t=27
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 1, '3': 1, '4': 4, '5': 1, '6': 4, '7': 2, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.103], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.093, 0.007, 0.003, 0.003, 0.012], 'utility': [-0.135], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.357, 0.924, 0.054, 0.021, 0.021, 0.055, 1.0], 'utility': [-0.231], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.335, 0.017, 0.014, 0.03, 0.273, 1.0, 0.058], 'utility': [-0.194], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.1, 1.0, 0.61, 0.026, 0.009, 0.009, 0.028], 'utility': [-0.071], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.24, 0.015, 0.009, 0.014, 0.066, 1.0, 0.085], 'utility': [-0.077], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.604, 0.395, 0.047, 0.022, 0.025, 0.074, 1.0], 'utility': [-0.145], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '8': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.311, 1.0, 0.359, 0.035, 0.015, 0.016, 0.05], 'utility': [-0.106], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.095], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.122, 0.008, 0.003, 0.004, 0.014], 'utility': [-0.229], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.354, 1.0, 0.055, 0.021, 0.021, 0.055, 0.975], 'utility': [-0.24], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.278, 0.015, 0.012, 0.025, 0.218, 1.0, 0.053], 'utility': [-0.169], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.117, 1.0, 0.762, 0.03, 0.011, 0.011, 0.031], 'utility': [-0.139], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.324, 0.018, 0.011, 0.017, 0.085, 1.0, 0.094], 'utility': [-0.112], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.739, 0.08, 0.033, 0.034, 0.083, 0.776], 'utility': [-0.097], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}, '8': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.601, 0.998, 1.0, 0.078, 0.028, 0.027, 0.072], 'utility': [-0.257], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.159, -0.155, -0.209, 0.0, 0.0, -0.126, -0.168]}} reward={'1': -2.491, '2': -2.086, '3': -2.757, '4': -2.561, '5': -2.086, '6': -2.561, '7': -2.693, '8': -2.297} t=28
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 4, '3': 1, '4': 4, '5': 1, '6': 4, '7': 0, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.099], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.071, 0.006, 0.002, 0.003, 0.011], 'utility': [-0.07], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.351, 0.833, 0.051, 0.02, 0.02, 0.055, 1.0], 'utility': [-0.222], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.401, 0.019, 0.016, 0.036, 0.34, 1.0, 0.064], 'utility': [-0.219], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.488, 0.022, 0.008, 0.008, 0.025], 'utility': [-0.011], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.178, 0.013, 0.007, 0.011, 0.051, 1.0, 0.077], 'utility': [-0.047], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.149, 0.019, 0.01, 0.013, 0.047, 1.0], 'utility': [-0.039], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.121, 0.014, 0.007, 0.008, 0.031], 'utility': [-0.082], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.103], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.093, 0.007, 0.003, 0.003, 0.012], 'utility': [-0.135], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.357, 0.924, 0.054, 0.021, 0.021, 0.055, 1.0], 'utility': [-0.231], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.335, 0.017, 0.014, 0.03, 0.273, 1.0, 0.058], 'utility': [-0.194], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.1, 1.0, 0.61, 0.026, 0.009, 0.009, 0.028], 'utility': [-0.071], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.24, 0.015, 0.009, 0.014, 0.066, 1.0, 0.085], 'utility': [-0.077], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.604, 0.395, 0.047, 0.022, 0.025, 0.074, 1.0], 'utility': [-0.145], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}, '8': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.311, 1.0, 0.359, 0.035, 0.015, 0.016, 0.05], 'utility': [-0.106], 'ues_at_bs': [0.5, 0.375, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.131, -0.104, -0.104, 0.0, 0.0, -0.125, -0.188]}} reward={'1': -2.431, '2': -0.971, '3': -1.692, '4': -2.148, '5': -0.971, '6': -2.148, '7': -2.159, '8': -1.571} t=29
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 4, '3': 5, '4': 4, '5': 1, '6': 4, '7': 0, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.102], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.054, 0.005, 0.002, 0.002, 0.009], 'utility': [-0.042], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.345, 0.752, 0.048, 0.019, 0.02, 0.054, 1.0], 'utility': [-0.212], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.477, 0.022, 0.019, 0.043, 0.423, 1.0, 0.07], 'utility': [-0.219], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.391, 0.019, 0.007, 0.007, 0.023], 'utility': [0.062], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.133, 0.01, 0.006, 0.008, 0.039, 1.0, 0.069], 'utility': [-0.006], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.086, 0.05, 0.007, 0.004, 0.006, 0.026, 1.0], 'utility': [0.114], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.051, 1.0, 0.038, 0.005, 0.003, 0.004, 0.017], 'utility': [-0.042], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.099], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.071, 0.006, 0.002, 0.003, 0.011], 'utility': [-0.07], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.351, 0.833, 0.051, 0.02, 0.02, 0.055, 1.0], 'utility': [-0.222], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.401, 0.019, 0.016, 0.036, 0.34, 1.0, 0.064], 'utility': [-0.219], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.488, 0.022, 0.008, 0.008, 0.025], 'utility': [-0.011], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.178, 0.013, 0.007, 0.011, 0.051, 1.0, 0.077], 'utility': [-0.047], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.149, 0.019, 0.01, 0.013, 0.047, 1.0], 'utility': [-0.039], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.121, 0.014, 0.007, 0.008, 0.031], 'utility': [-0.082], 'ues_at_bs': [0.5, 0.375, 0.25, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.097, -0.054, -0.04, 0.0, 0.0, -0.122, -0.13]}} reward={'1': -2.179, '2': -0.151, '3': -0.483, '4': -1.459, '5': 0.194, '6': -1.459, '7': -0.836, '8': -0.151} t=30
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 0, '3': 5, '4': 5, '5': 0, '6': 4, '7': 0, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.022, 1.0, 0.041, 0.004, 0.002, 0.002, 0.008], 'utility': [0.009], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.339, 0.679, 0.046, 0.018, 0.019, 0.053, 1.0], 'utility': [-0.203], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.563, 0.025, 0.022, 0.052, 0.524, 1.0, 0.076], 'utility': [-0.076], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.062, 1.0, 0.314, 0.016, 0.006, 0.006, 0.02], 'utility': [0.088], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.1, 0.009, 0.005, 0.007, 0.031, 1.0, 0.063], 'utility': [0.058], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.025, 0.015, 0.002, 0.001, 0.002, 0.012, 1.0], 'utility': [0.303], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.011, 0.002, 0.001, 0.002, 0.008], 'utility': [0.009], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.102], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.054, 0.005, 0.002, 0.002, 0.009], 'utility': [-0.042], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.345, 0.752, 0.048, 0.019, 0.02, 0.054, 1.0], 'utility': [-0.212], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '4': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.477, 0.022, 0.019, 0.043, 0.423, 1.0, 0.07], 'utility': [-0.219], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.391, 0.019, 0.007, 0.007, 0.023], 'utility': [0.062], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.133, 0.01, 0.006, 0.008, 0.039, 1.0, 0.069], 'utility': [-0.006], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.086, 0.05, 0.007, 0.004, 0.006, 0.026, 1.0], 'utility': [0.114], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.051, 1.0, 0.038, 0.005, 0.003, 0.004, 0.017], 'utility': [-0.042], 'ues_at_bs': [0.375, 0.375, 0.125, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.037, -0.008, 0.062, 0.0, 0.0, -0.109, -0.049]}} reward={'1': -0.544, '2': 0.71, '3': 0.538, '4': -0.586, '5': 0.971, '6': -0.399, '7': 1.002, '8': 0.71} t=31
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 0, '3': 5, '4': 4, '5': 0, '6': 4, '7': 5, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.075], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.031, 0.003, 0.001, 0.002, 0.007], 'utility': [0.049], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.333, 0.615, 0.043, 0.018, 0.019, 0.052, 1.0], 'utility': [-0.194], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.66, 0.028, 0.025, 0.062, 0.647, 1.0, 0.082], 'utility': [-0.013], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.253, 0.013, 0.005, 0.006, 0.018], 'utility': [0.11], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.077, 0.007, 0.004, 0.005, 0.025, 1.0, 0.058], 'utility': [0.08], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.006, 0.004, 0.001, 0.0, 0.001, 0.005, 1.0], 'utility': [0.536], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [0.049], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.022, 1.0, 0.041, 0.004, 0.002, 0.002, 0.008], 'utility': [0.009], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.339, 0.679, 0.046, 0.018, 0.019, 0.053, 1.0], 'utility': [-0.203], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.563, 0.025, 0.022, 0.052, 0.524, 1.0, 0.076], 'utility': [-0.076], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.062, 1.0, 0.314, 0.016, 0.006, 0.006, 0.02], 'utility': [0.088], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.1, 0.009, 0.005, 0.007, 0.031, 1.0, 0.063], 'utility': [0.058], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.025, 0.015, 0.002, 0.001, 0.002, 0.012, 1.0], 'utility': [0.303], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.011, 0.002, 0.001, 0.002, 0.008], 'utility': [0.009], 'ues_at_bs': [0.25, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.035, 0.088, 0.0, -0.076, -0.027, 0.05]}} reward={'1': -0.054, '2': 1.386, '3': 1.789, '4': -0.136, '5': 1.591, '6': -0.054, '7': 3.418, '8': 1.386} t=32
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 0, '3': 5, '4': 4, '5': 0, '6': 0, '7': 5, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.052], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.023, 0.002, 0.001, 0.001, 0.006], 'utility': [0.078], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.327, 0.557, 0.041, 0.017, 0.018, 0.052, 1.0], 'utility': [-0.185], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.768, 0.032, 0.029, 0.074, 0.797, 1.0, 0.088], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.045, 1.0, 0.205, 0.011, 0.005, 0.005, 0.017], 'utility': [0.128], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.06, 0.006, 0.003, 0.005, 0.02, 1.0, 0.055], 'utility': [0.106], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0], 'utility': [0.719], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.003, 1.0, 0.002, 0.0, 0.0, 0.0, 0.004], 'utility': [0.078], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.075], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.031, 0.003, 0.001, 0.002, 0.007], 'utility': [0.049], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.333, 0.615, 0.043, 0.018, 0.019, 0.052, 1.0], 'utility': [-0.194], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.66, 0.028, 0.025, 0.062, 0.647, 1.0, 0.082], 'utility': [-0.013], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.253, 0.013, 0.005, 0.006, 0.018], 'utility': [0.11], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.077, 0.007, 0.004, 0.005, 0.025, 1.0, 0.058], 'utility': [0.08], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.006, 0.004, 0.001, 0.0, 0.001, 0.005, 1.0], 'utility': [0.536], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [0.049], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.069, 0.11, 0.0, -0.013, -0.003, 0.171]}} reward={'1': 0.302, '2': 1.9, '3': 2.7, '4': 0.111, '5': 2.067, '6': 0.302, '7': 5.337, '8': 1.9} t=33
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 4, '5': 0, '6': 4, '7': 5, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.058], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.017, 0.002, 0.001, 0.001, 0.005], 'utility': [0.103], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.321, 0.506, 0.039, 0.016, 0.018, 0.051, 1.0], 'utility': [-0.176], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.887, 0.035, 0.034, 0.088, 0.978, 1.0, 0.095], 'utility': [0.001], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.039, 1.0, 0.166, 0.01, 0.004, 0.004, 0.015], 'utility': [0.144], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.048, 0.006, 0.003, 0.004, 0.016, 1.0, 0.052], 'utility': [0.139], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.003, 1.0], 'utility': [0.663], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.103], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.052], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.023, 0.002, 0.001, 0.001, 0.006], 'utility': [0.078], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.327, 0.557, 0.041, 0.017, 0.018, 0.052, 1.0], 'utility': [-0.185], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.768, 0.032, 0.029, 0.074, 0.797, 1.0, 0.088], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.045, 1.0, 0.205, 0.011, 0.005, 0.005, 0.017], 'utility': [0.128], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.06, 0.006, 0.003, 0.005, 0.02, 1.0, 0.055], 'utility': [0.106], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0], 'utility': [0.719], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.003, 1.0, 0.002, 0.0, 0.0, 0.0, 0.004], 'utility': [0.078], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.095, 0.128, 0.0, -0.009, 0.015, 0.267]}} reward={'1': 0.549, '2': 2.338, '3': 2.795, '4': 0.337, '5': 2.476, '6': 0.549, '7': 4.867, '8': 2.338} t=34
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 4, '5': 0, '6': 0, '7': 5, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.046], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.013, 0.001, 0.001, 0.001, 0.005], 'utility': [0.129], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.316, 0.459, 0.037, 0.016, 0.017, 0.051, 1.0], 'utility': [-0.168], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.85, 0.033, 0.032, 0.087, 1.0, 0.835, 0.085], 'utility': [0.011], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.033, 1.0, 0.135, 0.008, 0.003, 0.004, 0.013], 'utility': [0.163], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.039, 0.005, 0.002, 0.003, 0.014, 1.0, 0.051], 'utility': [0.15], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.129], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.058], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.017, 0.002, 0.001, 0.001, 0.005], 'utility': [0.103], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.321, 0.506, 0.039, 0.016, 0.018, 0.051, 1.0], 'utility': [-0.176], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.887, 0.035, 0.034, 0.088, 0.978, 1.0, 0.095], 'utility': [0.001], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.039, 1.0, 0.166, 0.01, 0.004, 0.004, 0.015], 'utility': [0.144], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.048, 0.006, 0.003, 0.004, 0.016, 1.0, 0.052], 'utility': [0.139], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.003, 1.0], 'utility': [0.663], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.103], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.117, 0.144, 0.0, 0.001, 0.027, 0.243]}} reward={'1': 0.771, '2': 2.801, '3': 2.794, '4': 0.551, '5': 2.914, '6': 0.771, '7': 4.069, '8': 2.801} t=35
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 0, '3': 5, '4': 4, '5': 0, '6': 0, '7': 5, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.01, 0.001, 0.001, 0.001, 0.004], 'utility': [0.153], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.31, 0.418, 0.035, 0.015, 0.017, 0.05, 1.0], 'utility': [-0.159], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.794, 0.03, 0.03, 0.084, 1.0, 0.684, 0.074], 'utility': [0.022], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.028, 1.0, 0.111, 0.007, 0.003, 0.003, 0.012], 'utility': [0.181], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.034, 0.005, 0.002, 0.003, 0.012, 1.0, 0.051], 'utility': [0.167], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.153], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.046], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.013, 0.001, 0.001, 0.001, 0.005], 'utility': [0.129], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.316, 0.459, 0.037, 0.016, 0.017, 0.051, 1.0], 'utility': [-0.168], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.85, 0.033, 0.032, 0.087, 1.0, 0.835, 0.085], 'utility': [0.011], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.033, 1.0, 0.135, 0.008, 0.003, 0.004, 0.013], 'utility': [0.163], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.039, 0.005, 0.002, 0.003, 0.014, 1.0, 0.051], 'utility': [0.15], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.129], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.14, 0.163, 0.0, 0.011, 0.039, 0.203]}} reward={'1': 0.943, '2': 3.251, '3': 3.083, '4': 0.741, '5': 3.344, '6': 0.943, '7': 4.156, '8': 3.251} t=36
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 0, '3': 5, '4': 4, '5': 0, '6': 0, '7': 5, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.038], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.008, 0.001, 0.001, 0.001, 0.003], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.305, 0.381, 0.034, 0.015, 0.016, 0.05, 1.0], 'utility': [-0.15], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.738, 0.027, 0.028, 0.081, 1.0, 0.562, 0.065], 'utility': [0.033], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.091, 0.006, 0.003, 0.003, 0.011], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.005, 0.002, 0.003, 0.011, 1.0, 0.052], 'utility': [0.165], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.015], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.01, 0.001, 0.001, 0.001, 0.004], 'utility': [0.153], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.31, 0.418, 0.035, 0.015, 0.017, 0.05, 1.0], 'utility': [-0.159], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.794, 0.03, 0.03, 0.084, 1.0, 0.684, 0.074], 'utility': [0.022], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.028, 1.0, 0.111, 0.007, 0.003, 0.003, 0.012], 'utility': [0.181], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.034, 0.005, 0.002, 0.003, 0.012, 1.0, 0.051], 'utility': [0.167], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.153], 'ues_at_bs': [0.125, 0.375, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.163, 0.181, 0.0, 0.022, 0.047, 0.208]}} reward={'1': 1.066, '2': 2.96, '3': 3.004, '4': 0.904, '5': 2.96, '6': 1.066, '7': 4.241, '8': 2.96} t=37
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 4, '5': 0, '6': 4, '7': 5, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.038], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.006, 0.001, 0.0, 0.001, 0.003], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.3, 0.348, 0.032, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.142], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.684, 0.025, 0.026, 0.078, 1.0, 0.463, 0.057], 'utility': [0.045], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.076, 0.005, 0.002, 0.003, 0.01], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.005, 0.002, 0.003, 0.011, 1.0, 0.056], 'utility': [0.164], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.004, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.589], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.02, 0.005, 0.003, 0.006, 0.045], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.038], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.008, 0.001, 0.001, 0.001, 0.003], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.305, 0.381, 0.034, 0.015, 0.016, 0.05, 1.0], 'utility': [-0.15], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.738, 0.027, 0.028, 0.081, 1.0, 0.562, 0.065], 'utility': [0.033], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.091, 0.006, 0.003, 0.003, 0.011], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.005, 0.002, 0.003, 0.011, 1.0, 0.052], 'utility': [0.165], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.015], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}} reward={'1': 1.137, '2': 1.973, '3': 2.625, '4': 1.038, '5': 1.973, '6': 1.137, '7': 4.47, '8': 1.973} t=38
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 4, '5': 0, '6': 4, '7': 5, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.005, 0.001, 0.0, 0.001, 0.003], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.295, 0.318, 0.03, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.134], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.631, 0.022, 0.025, 0.076, 1.0, 0.383, 0.05], 'utility': [0.056], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.063, 0.005, 0.002, 0.002, 0.009], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.061], 'utility': [0.149], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.01, 0.005, 0.001, 0.001, 0.001, 0.01, 1.0], 'utility': [0.433], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.256, 1.0, 0.053, 0.014, 0.01, 0.017, 0.109], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.038], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.006, 0.001, 0.0, 0.001, 0.003], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.3, 0.348, 0.032, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.142], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.684, 0.025, 0.026, 0.078, 1.0, 0.463, 0.057], 'utility': [0.045], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.076, 0.005, 0.002, 0.003, 0.01], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.005, 0.002, 0.003, 0.011, 1.0, 0.056], 'utility': [0.164], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.004, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.589], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.02, 0.005, 0.003, 0.006, 0.045], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}} reward={'1': 1.156, '2': 0.175, '3': 1.274, '4': 1.144, '5': 0.175, '6': 1.892, '7': 2.996, '8': 0.413} t=39
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 4, '5': 0, '6': 4, '7': 5, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.004, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.29, 0.291, 0.029, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.126], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.58, 0.02, 0.023, 0.074, 1.0, 0.318, 0.044], 'utility': [0.068], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.016, 1.0, 0.054, 0.004, 0.002, 0.002, 0.009], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.133], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.037, 0.014, 0.003, 0.002, 0.004, 0.024, 1.0], 'utility': [0.235], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.959, 1.0, 0.115, 0.034, 0.025, 0.042, 0.215], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.005, 0.001, 0.0, 0.001, 0.003], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.295, 0.318, 0.03, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.134], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.631, 0.022, 0.025, 0.076, 1.0, 0.383, 0.05], 'utility': [0.056], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.063, 0.005, 0.002, 0.002, 0.009], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.061], 'utility': [0.149], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.01, 0.005, 0.001, 0.001, 0.001, 0.01, 1.0], 'utility': [0.433], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.256, 1.0, 0.053, 0.014, 0.01, 0.017, 0.109], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}} reward={'1': 1.131, '2': -1.98, '3': -0.399, '4': 1.223, '5': -1.98, '6': 1.115, '7': 1.091, '8': -1.144} t=40
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 4, '5': 0, '6': 0, '7': 5, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.017], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.207], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.286, 0.267, 0.027, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.118], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.532, 0.018, 0.022, 0.072, 1.0, 0.265, 0.038], 'utility': [0.037], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.046, 0.004, 0.002, 0.002, 0.008], 'utility': [-0.207], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.011, 1.0, 0.078], 'utility': [0.116], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.13, 0.04, 0.008, 0.006, 0.009, 0.052, 1.0], 'utility': [0.055], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.271, 0.059, 0.02, 0.015, 0.025, 0.097], 'utility': [0.037], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.004, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.29, 0.291, 0.029, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.126], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.58, 0.02, 0.023, 0.074, 1.0, 0.318, 0.044], 'utility': [0.068], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.016, 1.0, 0.054, 0.004, 0.002, 0.002, 0.009], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.133], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.037, 0.014, 0.003, 0.002, 0.004, 0.024, 1.0], 'utility': [0.235], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.959, 1.0, 0.115, 0.034, 0.025, 0.042, 0.215], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.068, -0.099, 0.0, 0.0, 0.068, 0.057, 0.055]}} reward={'1': 0.991, '2': -2.513, '3': -1.047, '4': 0.737, '5': -2.513, '6': 0.179, '7': 0.052, '8': -1.213} t=41
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 2, '5': 0, '6': 0, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.017], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [-0.307], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.281, 0.245, 0.026, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.11], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.487, 0.017, 0.02, 0.07, 1.0, 0.221, 0.034], 'utility': [0.052], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.013, 1.0, 0.04, 0.003, 0.002, 0.002, 0.007], 'utility': [-0.307], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.006, 0.003, 0.003, 0.012, 1.0, 0.091], 'utility': [0.087], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.426, 0.095, 0.02, 0.014, 0.021, 0.096, 1.0], 'utility': [-0.099], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.022, 0.01, 0.008, 0.011, 0.033], 'utility': [0.184], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.017], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.207], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.286, 0.267, 0.027, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.118], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.532, 0.018, 0.022, 0.072, 1.0, 0.265, 0.038], 'utility': [0.037], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.046, 0.004, 0.002, 0.002, 0.008], 'utility': [-0.207], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.011, 1.0, 0.078], 'utility': [0.116], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.13, 0.04, 0.008, 0.006, 0.009, 0.052, 1.0], 'utility': [0.055], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.271, 0.059, 0.02, 0.015, 0.025, 0.097], 'utility': [0.037], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}} reward={'1': 0.703, '2': -2.87, '3': -1.154, '4': 1.919, '5': -2.87, '6': -0.695, '7': 0.134, '8': -0.777} t=42
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 7, '3': 5, '4': 2, '5': 7, '6': 0, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [0.289], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.277, 0.225, 0.025, 0.012, 0.015, 0.048, 1.0], 'utility': [-0.103], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.444, 0.015, 0.019, 0.069, 1.0, 0.186, 0.03], 'utility': [0.066], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.289], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.028, 0.007, 0.003, 0.003, 0.012, 1.0, 0.107], 'utility': [0.053], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.152, 0.035, 0.022, 0.032, 0.115, 0.749], 'utility': [-0.23], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.01, 0.005, 0.003, 0.003, 0.003, 0.007], 'utility': [0.455], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.017], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [-0.307], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.281, 0.245, 0.026, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.11], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.487, 0.017, 0.02, 0.07, 1.0, 0.221, 0.034], 'utility': [0.052], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.013, 1.0, 0.04, 0.003, 0.002, 0.002, 0.007], 'utility': [-0.307], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.006, 0.003, 0.003, 0.012, 1.0, 0.091], 'utility': [0.087], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.426, 0.095, 0.02, 0.014, 0.021, 0.096, 1.0], 'utility': [-0.099], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.022, 0.01, 0.008, 0.011, 0.033], 'utility': [0.184], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.118, -0.143, 0.0, 0.0, 0.052, 0.035, -0.105]}} reward={'1': 0.378, '2': 5.789, '3': 2.557, '4': 3.917, '5': 5.789, '6': -1.476, '7': 0.941, '8': 5.212} t=43
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 7, '3': 5, '4': 6, '5': 7, '6': 5, '7': 1, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.001, 0.003], 'utility': [0.288], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.273, 0.208, 0.024, 0.012, 0.014, 0.048, 1.0], 'utility': [-0.096], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.405, 0.014, 0.018, 0.067, 1.0, 0.157, 0.026], 'utility': [0.068], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.288], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.008, 0.003, 0.004, 0.014, 1.0, 0.126], 'utility': [0.019], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.093, 0.024, 0.015, 0.019, 0.054, 0.241], 'utility': [-0.056], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.001, 0.001, 0.0, 0.0, 0.0, 0.001], 'utility': [0.866], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [0.289], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.277, 0.225, 0.025, 0.012, 0.015, 0.048, 1.0], 'utility': [-0.103], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.444, 0.015, 0.019, 0.069, 1.0, 0.186, 0.03], 'utility': [0.066], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.289], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.028, 0.007, 0.003, 0.003, 0.012, 1.0, 0.107], 'utility': [0.053], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.152, 0.035, 0.022, 0.032, 0.115, 0.749], 'utility': [-0.23], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.01, 0.005, 0.003, 0.003, 0.003, 0.007], 'utility': [0.455], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.261, 0.289, 0.0, 0.0, 0.066, 0.019, -0.167]}} reward={'1': 0.031, '2': 5.757, '3': 3.722, '4': 4.732, '5': 5.757, '6': -0.741, '7': 2.909, '8': 5.857} t=44
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 7, '3': 5, '4': 6, '5': 7, '6': 3, '7': 0, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.014], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [0.285], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.269, 0.192, 0.023, 0.011, 0.014, 0.048, 1.0], 'utility': [-0.089], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.369, 0.013, 0.017, 0.067, 1.0, 0.133, 0.023], 'utility': [0.083], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.285], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.033, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.019], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.051, 0.015, 0.009, 0.01, 0.023, 0.077], 'utility': [0.049], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.001, 0.003], 'utility': [0.288], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.273, 0.208, 0.024, 0.012, 0.014, 0.048, 1.0], 'utility': [-0.096], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.405, 0.014, 0.018, 0.067, 1.0, 0.157, 0.026], 'utility': [0.068], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.288], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.008, 0.003, 0.004, 0.014, 1.0, 0.126], 'utility': [0.019], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.093, 0.024, 0.015, 0.019, 0.054, 0.241], 'utility': [-0.056], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.001, 0.001, 0.0, 0.0, 0.0, 0.001], 'utility': [0.866], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.293, 0.288, 0.0, 0.0, 0.068, 0.002, -0.076]}} reward={'1': -0.333, '2': 5.697, '3': 4.369, '4': 6.073, '5': 5.697, '6': -0.364, '7': 4.369, '8': 7.546} t=45
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 5, '4': 6, '5': 0, '6': 3, '7': 0, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.005], 'utility': [0.27], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.265, 0.177, 0.022, 0.011, 0.014, 0.048, 1.0], 'utility': [0.068], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.336, 0.012, 0.016, 0.066, 1.0, 0.114, 0.021], 'utility': [0.097], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.014, 1.0, 0.042, 0.004, 0.002, 0.002, 0.008], 'utility': [0.27], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.035, 0.01, 0.004, 0.005, 0.017, 1.0, 0.174], 'utility': [-0.056], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.026, 0.01, 0.006, 0.005, 0.009, 0.025], 'utility': [0.179], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0], 'utility': [0.903], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.014], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [0.285], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.269, 0.192, 0.023, 0.011, 0.014, 0.048, 1.0], 'utility': [-0.089], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.369, 0.013, 0.017, 0.067, 1.0, 0.133, 0.023], 'utility': [0.083], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.285], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.033, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.019], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.051, 0.015, 0.009, 0.01, 0.023, 0.077], 'utility': [0.049], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.377, 0.285, 0.0, 0.0, 0.083, -0.017, -0.02]}} reward={'1': -0.704, '2': 5.404, '3': 6.234, '4': 6.376, '5': 5.404, '6': -0.014, '7': 7.856, '8': 7.856} t=46
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 5, '4': 6, '5': 0, '6': 3, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.024], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.004, 0.001, 0.0, 0.001, 0.006], 'utility': [0.252], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.164, 0.021, 0.011, 0.014, 0.048, 1.0], 'utility': [0.075], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.306, 0.011, 0.015, 0.066, 1.0, 0.098, 0.019], 'utility': [0.11], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.049, 0.004, 0.002, 0.002, 0.008], 'utility': [0.252], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.063], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.007, 0.004, 0.003, 0.004, 0.01], 'utility': [0.301], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.003, 0.006, 0.009, 0.005, 0.003], 'utility': [0.385], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.005], 'utility': [0.27], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.265, 0.177, 0.022, 0.011, 0.014, 0.048, 1.0], 'utility': [0.068], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.336, 0.012, 0.016, 0.066, 1.0, 0.114, 0.021], 'utility': [0.097], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.014, 1.0, 0.042, 0.004, 0.002, 0.002, 0.008], 'utility': [0.27], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.035, 0.01, 0.004, 0.005, 0.017, 1.0, 0.174], 'utility': [-0.056], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.026, 0.01, 0.006, 0.005, 0.009, 0.025], 'utility': [0.179], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0], 'utility': [0.903], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.393, 0.27, 0.0, 0.0, 0.097, -0.035, 0.068]}} reward={'1': -0.873, '2': 5.043, '3': 4.354, '4': 4.531, '5': 5.043, '6': -0.085, '7': 5.308, '8': 5.308} t=47
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 6, '5': 0, '6': 4, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.025], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.004, 0.001, 0.001, 0.001, 0.008], 'utility': [0.231], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.259, 0.153, 0.02, 0.011, 0.014, 0.048, 1.0], 'utility': [0.081], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.279, 0.01, 0.014, 0.066, 1.0, 0.085, 0.017], 'utility': [0.122], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.058, 0.004, 0.002, 0.002, 0.009], 'utility': [0.231], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.062], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.013, 0.009, 0.004, 0.003, 0.003, 0.006], 'utility': [0.326], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.011, 0.03, 0.057, 0.021, 0.009], 'utility': [0.085], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.024], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.004, 0.001, 0.0, 0.001, 0.006], 'utility': [0.252], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.164, 0.021, 0.011, 0.014, 0.048, 1.0], 'utility': [0.075], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.306, 0.011, 0.015, 0.066, 1.0, 0.098, 0.019], 'utility': [0.11], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.049, 0.004, 0.002, 0.002, 0.008], 'utility': [0.252], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.063], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.007, 0.004, 0.003, 0.004, 0.01], 'utility': [0.301], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.003, 0.006, 0.009, 0.005, 0.003], 'utility': [0.385], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.265, 0.252, 0.0, 0.0, 0.11, -0.044, 0.075]}} reward={'1': -0.873, '2': 4.624, '3': 3.067, '4': 3.275, '5': 4.624, '6': -0.045, '7': 3.552, '8': 3.552} t=48
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 6, '5': 3, '6': 4, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.024], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.005, 0.001, 0.001, 0.001, 0.011], 'utility': [0.208], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.256, 0.142, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.086], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.256, 0.009, 0.014, 0.067, 1.0, 0.074, 0.015], 'utility': [0.133], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 1.0, 0.069, 0.005, 0.002, 0.003, 0.01], 'utility': [0.208], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.063], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.018, 0.019, 0.009, 0.005, 0.004, 0.007], 'utility': [0.234], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.024, 0.092, 0.254, 0.057, 0.02], 'utility': [-0.128], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.025], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.004, 0.001, 0.001, 0.001, 0.008], 'utility': [0.231], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.259, 0.153, 0.02, 0.011, 0.014, 0.048, 1.0], 'utility': [0.081], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.279, 0.01, 0.014, 0.066, 1.0, 0.085, 0.017], 'utility': [0.122], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.058, 0.004, 0.002, 0.002, 0.009], 'utility': [0.231], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.062], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.013, 0.009, 0.004, 0.003, 0.003, 0.006], 'utility': [0.326], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.011, 0.03, 0.057, 0.021, 0.009], 'utility': [0.085], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.178, 0.231, 0.0, 0.0, 0.122, -0.044, 0.081]}} reward={'1': -0.873, '2': 4.156, '3': 1.631, '4': 1.866, '5': 4.156, '6': -0.007, '7': 1.6, '8': 1.866} t=49
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 6, '5': 6, '6': 4, '7': 6, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.044], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.005, 0.001, 0.001, 0.002, 0.015], 'utility': [0.182], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.253, 0.133, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.092], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.235, 0.009, 0.013, 0.068, 1.0, 0.065, 0.014], 'utility': [-0.085], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.023, 1.0, 0.083, 0.006, 0.002, 0.003, 0.011], 'utility': [0.182], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.032, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.008], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.031, 0.053, 0.022, 0.009, 0.007, 0.011], 'utility': [0.087], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.042, 0.213, 0.981, 0.117, 0.034], 'utility': [-0.049], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.024], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.005, 0.001, 0.001, 0.001, 0.011], 'utility': [0.208], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.256, 0.142, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.086], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.256, 0.009, 0.014, 0.067, 1.0, 0.074, 0.015], 'utility': [0.133], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 1.0, 0.069, 0.005, 0.002, 0.003, 0.01], 'utility': [0.208], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.063], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.018, 0.019, 0.009, 0.005, 0.004, 0.007], 'utility': [0.234], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.024, 0.092, 0.254, 0.057, 0.02], 'utility': [-0.128], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.08, 0.208, 0.0, 0.0, 0.133, -0.044, 0.086]}} reward={'1': -0.524, '2': 3.648, '3': 0.222, '4': -0.725, '5': 3.648, '6': 0.261, '7': -0.315, '8': -0.725} t=50
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 6, '5': 6, '6': 4, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.029], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.019], 'utility': [0.155], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.251, 0.124, 0.018, 0.01, 0.013, 0.05, 1.0], 'utility': [0.097], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.217, 0.008, 0.013, 0.07, 1.0, 0.058, 0.013], 'utility': [-0.004], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.101, 0.007, 0.003, 0.003, 0.012], 'utility': [0.155], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.007, 0.003, 0.004, 0.014, 1.0, 0.115], 'utility': [0.016], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.053, 0.155, 0.058, 0.018, 0.012, 0.017], 'utility': [-0.066], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.272, 0.01, 0.018, 0.111, 1.0, 0.055, 0.014], 'utility': [-0.003], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.044], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.005, 0.001, 0.001, 0.002, 0.015], 'utility': [0.182], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.253, 0.133, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.092], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.235, 0.009, 0.013, 0.068, 1.0, 0.065, 0.014], 'utility': [-0.085], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.023, 1.0, 0.083, 0.006, 0.002, 0.003, 0.011], 'utility': [0.182], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.032, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.008], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.031, 0.053, 0.022, 0.009, 0.007, 0.011], 'utility': [0.087], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.042, 0.213, 0.981, 0.117, 0.034], 'utility': [-0.049], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.016, 0.182, 0.0, 0.0, -0.067, -0.026, 0.092]}} reward={'1': -0.124, '2': 3.11, '3': 0.122, '4': -0.313, '5': 3.11, '6': -0.124, '7': -0.48, '8': -0.313} t=51
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 6, '3': 5, '4': 6, '5': 6, '6': 4, '7': 3, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.007, 0.002, 0.001, 0.003, 0.026], 'utility': [0.127], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.248, 0.116, 0.017, 0.01, 0.013, 0.05, 1.0], 'utility': [0.101], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.201, 0.008, 0.013, 0.073, 1.0, 0.052, 0.012], 'utility': [0.082], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.123, 0.008, 0.003, 0.004, 0.013], 'utility': [0.127], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.006, 0.003, 0.003, 0.012, 1.0, 0.089], 'utility': [0.069], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.085, 0.431, 0.141, 0.032, 0.019, 0.025], 'utility': [0.018], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.069, 0.004, 0.006, 0.046, 1.0, 0.021, 0.005], 'utility': [0.051], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.029], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.019], 'utility': [0.155], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.251, 0.124, 0.018, 0.01, 0.013, 0.05, 1.0], 'utility': [0.097], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.217, 0.008, 0.013, 0.07, 1.0, 0.058, 0.013], 'utility': [-0.004], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.101, 0.007, 0.003, 0.003, 0.012], 'utility': [0.155], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.007, 0.003, 0.004, 0.014, 1.0, 0.115], 'utility': [0.016], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.053, 0.155, 0.058, 0.018, 0.012, 0.017], 'utility': [-0.066], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.272, 0.01, 0.018, 0.111, 1.0, 0.055, 0.014], 'utility': [-0.003], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.024, 0.155, 0.0, 0.0, -0.003, -0.006, 0.097]}} reward={'1': 0.268, '2': 2.549, '3': 1.342, '4': 1.167, '5': 1.82, '6': 0.268, '7': 0.789, '8': 1.332} t=52
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 5, '4': 6, '5': 0, '6': 4, '7': 5, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.032], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.003, 0.034], 'utility': [0.099], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.247, 0.109, 0.017, 0.01, 0.013, 0.051, 1.0], 'utility': [0.105], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.188, 0.008, 0.013, 0.076, 1.0, 0.047, 0.011], 'utility': [0.134], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.036, 1.0, 0.151, 0.009, 0.004, 0.004, 0.014], 'utility': [0.099], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.019, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.103], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.894, 0.111, 1.0, 0.286, 0.047, 0.025, 0.032], 'utility': [0.015], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.016, 0.001, 0.002, 0.015, 1.0, 0.007, 0.001], 'utility': [0.111], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.007, 0.002, 0.001, 0.003, 0.026], 'utility': [0.127], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.248, 0.116, 0.017, 0.01, 0.013, 0.05, 1.0], 'utility': [0.101], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.201, 0.008, 0.013, 0.073, 1.0, 0.052, 0.012], 'utility': [0.082], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.123, 0.008, 0.003, 0.004, 0.013], 'utility': [0.127], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.006, 0.003, 0.003, 0.012, 1.0, 0.089], 'utility': [0.069], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.085, 0.431, 0.141, 0.032, 0.019, 0.025], 'utility': [0.018], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.069, 0.004, 0.006, 0.046, 1.0, 0.021, 0.005], 'utility': [0.051], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.05, 0.127, 0.018, 0.0, 0.067, 0.013, 0.101]}} reward={'1': 0.708, '2': 1.973, '3': 1.696, '4': 1.969, '5': 1.416, '6': 0.708, '7': 1.095, '8': 2.448} t=53
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 5, '4': 6, '5': 3, '6': 4, '7': 4, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.01, 0.002, 0.002, 0.004, 0.045], 'utility': [0.069], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.103, 0.016, 0.009, 0.013, 0.052, 1.0], 'utility': [0.109], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.177, 0.007, 0.013, 0.081, 1.0, 0.043, 0.01], 'utility': [0.159], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.042, 1.0, 0.186, 0.011, 0.004, 0.005, 0.016], 'utility': [0.078], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.016, 0.004, 0.002, 0.002, 0.009, 1.0, 0.052], 'utility': [0.157], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.376, 0.064, 1.0, 0.252, 0.03, 0.014, 0.018], 'utility': [0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.004, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.139], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.032], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.003, 0.034], 'utility': [0.099], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.247, 0.109, 0.017, 0.01, 0.013, 0.051, 1.0], 'utility': [0.105], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.188, 0.008, 0.013, 0.076, 1.0, 0.047, 0.011], 'utility': [0.134], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.036, 1.0, 0.151, 0.009, 0.004, 0.004, 0.014], 'utility': [0.099], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.019, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.103], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.894, 0.111, 1.0, 0.286, 0.047, 0.025, 0.032], 'utility': [0.015], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.016, 0.001, 0.002, 0.015, 1.0, 0.007, 0.001], 'utility': [0.111], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.075, 0.099, 0.015, 0.0, 0.122, 0.035, 0.105]}} reward={'1': 1.153, '2': 1.473, '3': 1.923, '4': 2.387, '5': 1.23, '6': 1.153, '7': 1.391, '8': 2.979} t=54
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 5, '4': 6, '5': 4, '6': 4, '7': 4, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.011, 0.003, 0.002, 0.005, 0.06], 'utility': [0.04], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.244, 0.097, 0.016, 0.009, 0.013, 0.053, 1.0], 'utility': [0.112], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.167, 0.007, 0.013, 0.086, 1.0, 0.04, 0.01], 'utility': [0.18], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.052], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.013, 0.003, 0.001, 0.002, 0.007, 1.0, 0.039], 'utility': [0.2], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.179, 0.039, 1.0, 0.23, 0.021, 0.009, 0.011], 'utility': [0.091], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.145], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.01, 0.002, 0.002, 0.004, 0.045], 'utility': [0.069], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.103, 0.016, 0.009, 0.013, 0.052, 1.0], 'utility': [0.109], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.177, 0.007, 0.013, 0.081, 1.0, 0.043, 0.01], 'utility': [0.159], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.042, 1.0, 0.186, 0.011, 0.004, 0.005, 0.016], 'utility': [0.078], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.016, 0.004, 0.002, 0.002, 0.009, 1.0, 0.052], 'utility': [0.157], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.376, 0.064, 1.0, 0.252, 0.03, 0.014, 0.018], 'utility': [0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.004, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.139], 'ues_at_bs': [0.25, 0.25, 0.25, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.09, 0.074, 0.049, 0.0, 0.149, 0.058, 0.109]}} reward={'1': 1.644, '2': 0.919, '3': 2.924, '4': 3.369, '5': 1.172, '6': 1.644, '7': 1.554, '8': 3.252} t=55
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 5, '3': 5, '4': 6, '5': 5, '6': 5, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.079], 'utility': [0.027], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.243, 0.092, 0.015, 0.009, 0.013, 0.054, 1.0], 'utility': [0.115], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.159, 0.007, 0.013, 0.093, 1.0, 0.037, 0.01], 'utility': [0.177], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.042], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.01, 0.002, 0.001, 0.001, 0.006, 1.0, 0.028], 'utility': [0.258], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.101, 0.027, 1.0, 0.226, 0.016, 0.007, 0.008], 'utility': [0.122], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.143], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.011, 0.003, 0.002, 0.005, 0.06], 'utility': [0.04], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.244, 0.097, 0.016, 0.009, 0.013, 0.053, 1.0], 'utility': [0.112], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.167, 0.007, 0.013, 0.086, 1.0, 0.04, 0.01], 'utility': [0.18], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.052], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.013, 0.003, 0.001, 0.002, 0.007, 1.0, 0.039], 'utility': [0.2], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.179, 0.039, 1.0, 0.23, 0.021, 0.009, 0.011], 'utility': [0.091], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.145], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.18, 0.046, 0.071, 0.091, 0.163, 0.082, 0.112]}} reward={'1': 2.155, '2': 1.231, '3': 2.916, '4': 3.304, '5': 1.168, '6': 2.155, '7': 1.907, '8': 3.191} t=56
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 5, '3': 5, '4': 6, '5': 5, '6': 5, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.014, 0.004, 0.003, 0.007, 0.103], 'utility': [0.014], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.087, 0.015, 0.009, 0.013, 0.056, 1.0], 'utility': [0.118], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.153, 0.007, 0.013, 0.102, 1.0, 0.035, 0.009], 'utility': [0.173], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.032], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.002, 0.001, 0.001, 0.005, 1.0, 0.021], 'utility': [0.311], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.07, 0.022, 1.0, 0.247, 0.014, 0.006, 0.006], 'utility': [0.122], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.079], 'utility': [0.027], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.243, 0.092, 0.015, 0.009, 0.013, 0.054, 1.0], 'utility': [0.115], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.159, 0.007, 0.013, 0.093, 1.0, 0.037, 0.01], 'utility': [0.177], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.042], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.01, 0.002, 0.001, 0.001, 0.006, 1.0, 0.028], 'utility': [0.258], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.101, 0.027, 1.0, 0.226, 0.016, 0.007, 0.008], 'utility': [0.122], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.143], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.177, 0.035, 0.082, 0.122, 0.16, 0.108, 0.115]}} reward={'1': 2.717, '2': 1.09, '3': 2.906, '4': 3.243, '5': 0.998, '6': 2.717, '7': 1.835, '8': 3.134} t=57
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 5, '3': 5, '4': 6, '5': 5, '6': 5, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.044], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.048, 1.0, 0.016, 0.005, 0.004, 0.009, 0.134], 'utility': [-0.001], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.083, 0.015, 0.009, 0.013, 0.057, 1.0], 'utility': [0.12], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.149, 0.007, 0.014, 0.113, 1.0, 0.034, 0.009], 'utility': [0.168], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.022], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.015], 'utility': [0.375], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.059, 0.021, 1.0, 0.297, 0.014, 0.006, 0.006], 'utility': [0.089], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.136], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.014, 0.004, 0.003, 0.007, 0.103], 'utility': [0.014], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.087, 0.015, 0.009, 0.013, 0.056, 1.0], 'utility': [0.118], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.153, 0.007, 0.013, 0.102, 1.0, 0.035, 0.009], 'utility': [0.173], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.032], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.002, 0.001, 0.001, 0.005, 1.0, 0.021], 'utility': [0.311], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.07, 0.022, 1.0, 0.247, 0.014, 0.006, 0.006], 'utility': [0.122], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.173, 0.023, 0.077, 0.122, 0.157, 0.136, 0.118]}} reward={'1': 3.311, '2': 0.939, '3': 2.874, '4': 3.146, '5': 0.66, '6': 3.311, '7': 1.33, '8': 3.04} t=58
DEBUG:deepcomp.util.simulation:Step                           action={'1': 5, '2': 5, '3': 5, '4': 6, '5': 5, '6': 5, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.055, 1.0, 0.018, 0.005, 0.005, 0.011, 0.173], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.079, 0.014, 0.009, 0.013, 0.059, 1.0], 'utility': [0.121], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.145, 0.007, 0.014, 0.126, 1.0, 0.032, 0.009], 'utility': [0.157], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.056, 1.0, 0.265, 0.014, 0.005, 0.006, 0.019], 'utility': [0.009], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.01], 'utility': [0.439], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.058, 0.023, 1.0, 0.376, 0.017, 0.007, 0.007], 'utility': [0.03], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.003, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.125], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.044], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.048, 1.0, 0.016, 0.005, 0.004, 0.009, 0.134], 'utility': [-0.001], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.083, 0.015, 0.009, 0.013, 0.057, 1.0], 'utility': [0.12], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.149, 0.007, 0.014, 0.113, 1.0, 0.034, 0.009], 'utility': [0.168], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.022], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.015], 'utility': [0.375], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.059, 0.021, 1.0, 0.297, 0.014, 0.006, 0.006], 'utility': [0.089], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.136], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, 0.011, 0.055, 0.089, 0.152, 0.166, 0.12]}} reward={'1': 3.968, '2': 0.707, '3': 2.779, '4': 2.928, '5': 0.12, '6': 3.968, '7': 0.464, '8': 2.822} t=59
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 5, '4': 6, '5': 5, '6': 5, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.02, 0.006, 0.005, 0.013, 0.223], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.076, 0.014, 0.009, 0.014, 0.061, 1.0], 'utility': [0.122], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.143, 0.007, 0.015, 0.142, 1.0, 0.032, 0.009], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.306, 0.016, 0.006, 0.006, 0.02], 'utility': [-0.003], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.515], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.063, 0.028, 1.0, 0.476, 0.022, 0.008, 0.009], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.006, 0.001, 0.001, 0.011, 1.0, 0.003, 0.001], 'utility': [0.108], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.055, 1.0, 0.018, 0.005, 0.005, 0.011, 0.173], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.079, 0.014, 0.009, 0.013, 0.059, 1.0], 'utility': [0.121], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.145, 0.007, 0.014, 0.126, 1.0, 0.032, 0.009], 'utility': [0.157], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.056, 1.0, 0.265, 0.014, 0.005, 0.006, 0.019], 'utility': [0.009], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.01], 'utility': [0.439], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.058, 0.023, 1.0, 0.376, 0.017, 0.007, 0.007], 'utility': [0.03], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.003, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.125], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.008, 0.02, 0.03, 0.141, 0.198, 0.121]}} reward={'1': 4.677, '2': 0.477, '3': 2.623, '4': 1.749, '5': -0.461, '6': 4.677, '7': -0.537, '8': 2.481} t=60
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 5, '4': 2, '5': 4, '6': 4, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.071, 1.0, 0.022, 0.007, 0.006, 0.015, 0.286], 'utility': [-0.071], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.073, 0.014, 0.009, 0.014, 0.063, 1.0], 'utility': [0.123], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.141, 0.008, 0.016, 0.162, 1.0, 0.031, 0.009], 'utility': [0.083], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.355, 0.018, 0.007, 0.007, 0.022], 'utility': [-0.014], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.002, 1.0, 0.004], 'utility': [0.594], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.107], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.012, 0.001, 0.002, 0.022, 1.0, 0.005, 0.001], 'utility': [0.083], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.02, 0.006, 0.005, 0.013, 0.223], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.076, 0.014, 0.009, 0.014, 0.061, 1.0], 'utility': [0.122], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.143, 0.007, 0.015, 0.142, 1.0, 0.032, 0.009], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.306, 0.016, 0.006, 0.006, 0.02], 'utility': [-0.003], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.515], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.063, 0.028, 1.0, 0.476, 0.022, 0.008, 0.009], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.006, 0.001, 0.001, 0.011, 1.0, 0.003, 0.001], 'utility': [0.108], 'ues_at_bs': [0.125, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.14, -0.025, -0.021, -0.039, 0.124, 0.234, 0.122]}} reward={'1': 5.468, '2': 0.249, '3': 2.451, '4': 0.393, '5': -1.032, '6': 5.468, '7': -1.525, '8': 1.664} t=61
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 7, '3': 5, '4': 4, '5': 4, '6': 4, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.052], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 1.0, 0.024, 0.008, 0.007, 0.018, 0.365], 'utility': [-0.028], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [-0.028], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.017, 0.186, 1.0, 0.031, 0.009], 'utility': [0.076], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.083, 1.0, 0.413, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.042], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.003], 'utility': [0.686], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.146], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.023, 0.002, 0.004, 0.044, 1.0, 0.009, 0.002], 'utility': [0.051], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.071, 1.0, 0.022, 0.007, 0.006, 0.015, 0.286], 'utility': [-0.071], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.073, 0.014, 0.009, 0.014, 0.063, 1.0], 'utility': [0.123], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.141, 0.008, 0.016, 0.162, 1.0, 0.031, 0.009], 'utility': [0.083], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.355, 0.018, 0.007, 0.007, 0.022], 'utility': [-0.014], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.002, 1.0, 0.004], 'utility': [0.594], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.107], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.012, 0.001, 0.002, 0.022, 1.0, 0.005, 0.001], 'utility': [0.083], 'ues_at_bs': [0.0, 0.25, 0.25, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, -0.043, -0.061, -0.107, 0.083, 0.273, 0.123]}} reward={'1': 6.34, '2': -0.626, '3': -0.554, '4': 0.288, '5': -1.29, '6': 6.34, '7': -1.291, '8': 1.275} t=62
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 4, '3': 1, '4': 2, '5': 5, '6': 2, '7': 0, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.09, 1.0, 0.026, 0.009, 0.008, 0.021, 0.465], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.058], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.018, 0.216, 1.0, 0.031, 0.009], 'utility': [0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.097, 1.0, 0.482, 0.023, 0.008, 0.009, 0.026], 'utility': [-0.049], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.002], 'utility': [0.788], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.158], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.042, 0.003, 0.007, 0.086, 1.0, 0.014, 0.004], 'utility': [0.012], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.052], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 1.0, 0.024, 0.008, 0.007, 0.018, 0.365], 'utility': [-0.028], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [-0.028], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.017, 0.186, 1.0, 0.031, 0.009], 'utility': [0.076], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.083, 1.0, 0.413, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.042], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.003], 'utility': [0.686], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.146], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.023, 0.002, 0.004, 0.044, 1.0, 0.009, 0.002], 'utility': [0.051], 'ues_at_bs': [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.0, -0.035, -0.094, -0.035, 0.064, 0.317, -0.028]}} reward={'1': 7.331, '2': -0.342, '3': 0.513, '4': -0.28, '5': -1.474, '6': 7.331, '7': -1.603, '8': -0.28} t=63
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 4, '3': 0, '4': 2, '5': 4, '6': 2, '7': 0, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.061], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.1, 1.0, 0.029, 0.01, 0.009, 0.025, 0.59], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.058], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.142, 0.009, 0.019, 0.251, 1.0, 0.031, 0.01], 'utility': [0.011], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.112, 1.0, 0.563, 0.026, 0.009, 0.01, 0.029], 'utility': [-0.079], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.0, 1.0, 0.001], 'utility': [0.906], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.025, 1.0, 0.346, 0.018, 0.007, 0.008], 'utility': [-0.057], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.075, 0.005, 0.012, 0.162, 1.0, 0.021, 0.006], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.09, 1.0, 0.026, 0.009, 0.008, 0.021, 0.465], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.058], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.018, 0.216, 1.0, 0.031, 0.009], 'utility': [0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.097, 1.0, 0.482, 0.023, 0.008, 0.009, 0.026], 'utility': [-0.049], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.002], 'utility': [0.788], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.158], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.042, 0.003, 0.007, 0.086, 1.0, 0.014, 0.004], 'utility': [0.012], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.044, -0.104, -0.057, 0.029, 0.367, 0.01]}} reward={'1': 8.454, '2': -0.581, '3': 0.454, '4': -0.332, '5': -1.311, '6': 8.454, '7': -0.911, '8': -0.332} t=64
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 4, '3': 0, '4': 2, '5': 4, '6': 0, '7': 0, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.111, 1.0, 0.031, 0.011, 0.011, 0.029, 0.745], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.252, 0.076, 0.014, 0.009, 0.014, 0.064, 1.0], 'utility': [0.055], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.144, 0.009, 0.021, 0.295, 1.0, 0.032, 0.01], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.13, 1.0, 0.658, 0.03, 0.011, 0.011, 0.032], 'utility': [-0.092], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.036, 0.017, 1.0, 0.183, 0.01, 0.004, 0.005], 'utility': [0.035], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.129, 0.008, 0.02, 0.295, 1.0, 0.03, 0.009], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.061], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.1, 1.0, 0.029, 0.01, 0.009, 0.025, 0.59], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.058], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.142, 0.009, 0.019, 0.251, 1.0, 0.031, 0.01], 'utility': [0.011], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.112, 1.0, 0.563, 0.026, 0.009, 0.01, 0.029], 'utility': [-0.079], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.0, 1.0, 0.001], 'utility': [0.906], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.025, 1.0, 0.346, 0.018, 0.007, 0.008], 'utility': [-0.057], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.075, 0.005, 0.012, 0.162, 1.0, 0.021, 0.006], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.058, -0.063, -0.068, -0.023, -0.01, 0.423, 0.005]}} reward={'1': 9.341, '2': -0.726, '3': 0.372, '4': -0.491, '5': -1.018, '6': 9.341, '7': -0.406, '8': -0.491} t=65
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 5, '3': 5, '4': 2, '5': 5, '6': 7, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.075], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.122, 1.0, 0.034, 0.012, 0.012, 0.034, 0.939], 'utility': [-0.058], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.081, 0.015, 0.01, 0.014, 0.064, 1.0], 'utility': [0.052], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.147, 0.01, 0.023, 0.348, 1.0, 0.032, 0.01], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.152, 1.0, 0.769, 0.034, 0.012, 0.012, 0.035], 'utility': [-0.109], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.011, 1.0, 0.086, 0.006, 0.002, 0.003], 'utility': [0.161], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.213, 0.013, 0.032, 0.518, 1.0, 0.041, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.111, 1.0, 0.031, 0.011, 0.011, 0.029, 0.745], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.252, 0.076, 0.014, 0.009, 0.014, 0.064, 1.0], 'utility': [0.055], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.144, 0.009, 0.021, 0.295, 1.0, 0.032, 0.01], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.13, 1.0, 0.658, 0.03, 0.011, 0.011, 0.032], 'utility': [-0.092], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.036, 0.017, 1.0, 0.183, 0.01, 0.004, 0.005], 'utility': [0.035], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.129, 0.008, 0.02, 0.295, 1.0, 0.03, 0.009], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.25], 'util_at_bs': [0.055, -0.073, -0.029, -0.015, -0.039, 0.467, 0.0]}} reward={'1': 9.248, '2': -0.864, '3': 0.305, '4': -0.992, '5': -0.571, '6': 9.248, '7': 0.525, '8': -0.992} t=66
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 0, '4': 2, '5': 1, '6': 0, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.084], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.113, 0.848, 0.031, 0.011, 0.012, 0.033, 1.0], 'utility': [-0.059], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.273, 0.087, 0.016, 0.01, 0.015, 0.063, 1.0], 'utility': [0.049], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.15, 0.01, 0.025, 0.412, 1.0, 0.033, 0.011], 'utility': [-0.082], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.178, 1.0, 0.898, 0.039, 0.014, 0.013, 0.038], 'utility': [-0.115], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.007, 1.0, 0.036, 0.003, 0.001, 0.002], 'utility': [0.313], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.34, 0.02, 0.051, 0.881, 1.0, 0.054, 0.02], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.075], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.122, 1.0, 0.034, 0.012, 0.012, 0.034, 0.939], 'utility': [-0.058], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.081, 0.015, 0.01, 0.014, 0.064, 1.0], 'utility': [0.052], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.147, 0.01, 0.023, 0.348, 1.0, 0.032, 0.01], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.152, 1.0, 0.769, 0.034, 0.012, 0.012, 0.035], 'utility': [-0.109], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.011, 1.0, 0.086, 0.006, 0.002, 0.003], 'utility': [0.161], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.213, 0.013, 0.032, 0.518, 1.0, 0.041, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.052, -0.083, 0.026, -0.05, -0.05, 0.462, -0.003]}} reward={'1': 9.16, '2': -0.925, '3': 0.252, '4': -1.418, '5': 0.115, '6': 9.16, '7': 1.974, '8': -1.418} t=67
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 0, '4': 2, '5': 1, '6': 0, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.089], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.098, 0.677, 0.027, 0.01, 0.01, 0.03, 1.0], 'utility': [-0.058], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.285, 0.093, 0.017, 0.01, 0.015, 0.063, 1.0], 'utility': [0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.153, 0.011, 0.027, 0.491, 1.0, 0.034, 0.011], 'utility': [-0.103], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.199, 0.955, 1.0, 0.043, 0.015, 0.014, 0.04], 'utility': [-0.121], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.008, 0.004, 1.0, 0.014, 0.001, 0.001, 0.001], 'utility': [0.472], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.363, 0.02, 0.055, 1.0, 0.689, 0.048, 0.019], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.084], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.113, 0.848, 0.031, 0.011, 0.012, 0.033, 1.0], 'utility': [-0.059], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.273, 0.087, 0.016, 0.01, 0.015, 0.063, 1.0], 'utility': [0.049], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.15, 0.01, 0.025, 0.412, 1.0, 0.033, 0.011], 'utility': [-0.082], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.178, 1.0, 0.898, 0.039, 0.014, 0.013, 0.038], 'utility': [-0.115], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.007, 1.0, 0.036, 0.003, 0.001, 0.002], 'utility': [0.313], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.34, 0.02, 0.051, 0.881, 1.0, 0.054, 0.02], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.087, 0.099, -0.071, -0.071, 0.458, -0.005]}} reward={'1': 9.107, '2': -0.958, '3': 0.215, '4': -1.698, '5': 0.862, '6': 9.107, '7': 3.513, '8': -1.178} t=68
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 0, '4': 2, '5': 1, '6': 0, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.085, 0.542, 0.023, 0.009, 0.009, 0.027, 1.0], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.297, 0.101, 0.018, 0.011, 0.015, 0.063, 1.0], 'utility': [0.041], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.157, 0.012, 0.03, 0.586, 1.0, 0.035, 0.012], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.201, 0.822, 1.0, 0.043, 0.014, 0.014, 0.038], 'utility': [-0.111], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.007, 0.001, 0.0, 0.001], 'utility': [0.581], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.343, 0.018, 0.053, 1.0, 0.433, 0.038, 0.016], 'utility': [-0.064], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.089], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.098, 0.677, 0.027, 0.01, 0.01, 0.03, 1.0], 'utility': [-0.058], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.285, 0.093, 0.017, 0.01, 0.015, 0.063, 1.0], 'utility': [0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.153, 0.011, 0.027, 0.491, 1.0, 0.034, 0.011], 'utility': [-0.103], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.199, 0.955, 1.0, 0.043, 0.015, 0.014, 0.04], 'utility': [-0.121], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.008, 0.004, 1.0, 0.014, 0.001, 0.001, 0.001], 'utility': [0.472], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.363, 0.02, 0.055, 1.0, 0.689, 0.048, 0.019], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.089, 0.176, -0.085, -0.085, 0.455, -0.006]}} reward={'1': 9.4, '2': -0.886, '3': 0.193, '4': -1.835, '5': 1.525, '6': 9.4, '7': 4.697, '8': -1.303} t=69
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 0, '4': 2, '5': 1, '6': 0, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.074, 0.436, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.31, 0.109, 0.019, 0.011, 0.016, 0.063, 1.0], 'utility': [0.037], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.162, 0.012, 0.032, 0.701, 1.0, 0.036, 0.013], 'utility': [-0.13], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.204, 0.71, 1.0, 0.043, 0.014, 0.013, 0.036], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.006, 0.004, 1.0, 0.005, 0.001, 0.0, 0.001], 'utility': [0.55], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.327, 0.017, 0.052, 1.0, 0.283, 0.03, 0.014], 'utility': [-0.056], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.085, 0.542, 0.023, 0.009, 0.009, 0.027, 1.0], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.297, 0.101, 0.018, 0.011, 0.015, 0.063, 1.0], 'utility': [0.041], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.157, 0.012, 0.03, 0.586, 1.0, 0.035, 0.012], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.201, 0.822, 1.0, 0.043, 0.014, 0.014, 0.038], 'utility': [-0.111], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.007, 0.001, 0.0, 0.001], 'utility': [0.581], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.343, 0.018, 0.053, 1.0, 0.433, 0.038, 0.016], 'utility': [-0.064], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.041, -0.082, 0.235, -0.092, -0.092, 0.47, -0.006]}} reward={'1': 10.083, '2': -0.686, '3': 0.184, '4': -1.855, '5': 1.709, '6': 10.083, '7': 4.693, '8': -1.334} t=70
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 5, '3': 0, '4': 2, '5': 1, '6': 0, '7': 0, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.323, 0.117, 0.02, 0.011, 0.016, 0.063, 1.0], 'utility': [0.033], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.166, 0.013, 0.036, 0.839, 1.0, 0.037, 0.013], 'utility': [0.037], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.208, 0.615, 1.0, 0.043, 0.014, 0.013, 0.034], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.008, 1.0, 0.007, 0.001, 0.001, 0.001], 'utility': [0.399], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.315, 0.016, 0.053, 1.0, 0.194, 0.025, 0.013], 'utility': [-0.102], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.074, 0.436, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.31, 0.109, 0.019, 0.011, 0.016, 0.063, 1.0], 'utility': [0.037], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.162, 0.012, 0.032, 0.701, 1.0, 0.036, 0.013], 'utility': [-0.13], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.204, 0.71, 1.0, 0.043, 0.014, 0.013, 0.036], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.006, 0.004, 1.0, 0.005, 0.001, 0.0, 0.001], 'utility': [0.55], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.327, 0.017, 0.052, 1.0, 0.283, 0.03, 0.014], 'utility': [-0.056], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.037, -0.064, 0.235, -0.093, -0.093, 0.504, -0.005]}} reward={'1': 10.274, '2': -0.572, '3': 0.131, '4': -0.184, '5': 1.221, '6': 10.274, '7': 3.449, '8': -0.211} t=71
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 5, '3': 0, '4': 2, '5': 1, '6': 0, '7': 7, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.338, 0.127, 0.021, 0.012, 0.017, 0.063, 1.0], 'utility': [0.029], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.17, 0.014, 0.039, 1.0, 0.993, 0.039, 0.014], 'utility': [0.03], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.213, 0.536, 1.0, 0.043, 0.014, 0.013, 0.033], 'utility': [-0.046], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.023, 1.0, 0.012, 0.002, 0.002, 0.003], 'utility': [0.231], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.31, 0.015, 0.057, 1.0, 0.139, 0.021, 0.012], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.323, 0.117, 0.02, 0.011, 0.016, 0.063, 1.0], 'utility': [0.033], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.166, 0.013, 0.036, 0.839, 1.0, 0.037, 0.013], 'utility': [0.037], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.208, 0.615, 1.0, 0.043, 0.014, 0.013, 0.034], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.008, 1.0, 0.007, 0.001, 0.001, 0.001], 'utility': [0.399], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.315, 0.016, 0.053, 1.0, 0.194, 0.025, 0.013], 'utility': [-0.102], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.033, -0.05, 0.172, -0.032, 0.037, 0.514, -0.007]}} reward={'1': 10.271, '2': -0.58, '3': 0.057, '4': -0.128, '5': 0.448, '6': 10.271, '7': 1.85, '8': -0.136} t=72
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 2, '3': 0, '4': 2, '5': 1, '6': 0, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.019], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.129], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.353, 0.138, 0.022, 0.012, 0.017, 0.063, 1.0], 'utility': [0.025], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.146, 0.013, 0.035, 1.0, 0.828, 0.034, 0.012], 'utility': [0.025], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.219, 0.47, 1.0, 0.043, 0.014, 0.012, 0.031], 'utility': [0.0], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.064, 0.069, 1.0, 0.02, 0.005, 0.004, 0.007], 'utility': [0.106], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.312, 0.016, 0.064, 1.0, 0.106, 0.018, 0.011], 'utility': [-0.067], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.338, 0.127, 0.021, 0.012, 0.017, 0.063, 1.0], 'utility': [0.029], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.17, 0.014, 0.039, 1.0, 0.993, 0.039, 0.014], 'utility': [0.03], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.213, 0.536, 1.0, 0.043, 0.014, 0.013, 0.033], 'utility': [-0.046], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.023, 1.0, 0.012, 0.002, 0.002, 0.003], 'utility': [0.231], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.31, 0.015, 0.057, 1.0, 0.139, 0.021, 0.012], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.029, -0.048, 0.092, -0.025, 0.03, 0.514, -0.01]}} reward={'1': 10.194, '2': -0.696, '3': -0.532, '4': -0.115, '5': 0.71, '6': 10.194, '7': 1.064, '8': -0.116} t=73
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 6, '3': 0, '4': 2, '5': 1, '6': 7, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.013], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.075, 0.404, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.118], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.368, 0.15, 0.023, 0.013, 0.017, 0.064, 1.0], 'utility': [0.02], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.032, 1.0, 0.69, 0.029, 0.011], 'utility': [0.021], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.227, 0.414, 1.0, 0.044, 0.014, 0.012, 0.03], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [0.942], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.132, 0.196, 1.0, 0.032, 0.009, 0.007, 0.017], 'utility': [-0.051], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.322, 0.017, 0.076, 1.0, 0.086, 0.017, 0.011], 'utility': [-0.065], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.019], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.129], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.353, 0.138, 0.022, 0.012, 0.017, 0.063, 1.0], 'utility': [0.025], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.146, 0.013, 0.035, 1.0, 0.828, 0.034, 0.012], 'utility': [0.025], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.219, 0.47, 1.0, 0.043, 0.014, 0.012, 0.031], 'utility': [0.0], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.064, 0.069, 1.0, 0.02, 0.005, 0.004, 0.007], 'utility': [0.106], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.312, 0.016, 0.064, 1.0, 0.106, 0.018, 0.011], 'utility': [-0.067], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.025, 0.0, 0.053, -0.021, 0.025, 0.51, -0.052]}} reward={'1': 9.55, '2': -0.626, '3': -0.512, '4': -0.151, '5': -0.294, '6': 9.55, '7': -0.294, '8': -0.156} t=74
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 6, '3': 0, '4': 2, '5': 1, '6': 7, '7': 7, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.08, 0.4, 0.019, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.109], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.384, 0.163, 0.025, 0.014, 0.018, 0.064, 1.0], 'utility': [-0.037], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.109, 0.01, 0.03, 1.0, 0.576, 0.025, 0.01], 'utility': [0.019], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.236, 0.367, 1.0, 0.045, 0.014, 0.012, 0.029], 'utility': [-0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.821], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.242, 0.537, 1.0, 0.046, 0.015, 0.014, 0.035], 'utility': [-0.163], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.34, 0.019, 0.097, 1.0, 0.074, 0.017, 0.012], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.013], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.075, 0.404, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.118], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.368, 0.15, 0.023, 0.013, 0.017, 0.064, 1.0], 'utility': [0.02], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.032, 1.0, 0.69, 0.029, 0.011], 'utility': [0.021], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.227, 0.414, 1.0, 0.044, 0.014, 0.012, 0.03], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [0.942], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.132, 0.196, 1.0, 0.032, 0.009, 0.007, 0.017], 'utility': [-0.051], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.322, 0.017, 0.076, 1.0, 0.086, 0.017, 0.011], 'utility': [-0.065], 'ues_at_bs': [0.125, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.02, 0.003, -0.024, -0.022, 0.021, 0.478, -0.049]}} reward={'1': 8.281, '2': -1.025, '3': -0.966, '4': 0.187, '5': -0.898, '6': 8.281, '7': -1.183, '8': -0.188} t=75
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 1, '3': 4, '4': 2, '5': 1, '6': 7, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.004], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.087, 0.398, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.103], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.401, 0.177, 0.026, 0.014, 0.019, 0.065, 1.0], 'utility': [-0.065], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.094, 0.009, 0.027, 1.0, 0.482, 0.022, 0.009], 'utility': [0.018], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '5': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.248, 0.328, 1.0, 0.047, 0.014, 0.012, 0.028], 'utility': [0.005], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.714], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.269, 1.0, 0.682, 0.043, 0.016, 0.016, 0.046], 'utility': [-0.265], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.368, 0.023, 0.13, 1.0, 0.067, 0.017, 0.013], 'utility': [-0.044], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.08, 0.4, 0.019, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.109], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.384, 0.163, 0.025, 0.014, 0.018, 0.064, 1.0], 'utility': [-0.037], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.109, 0.01, 0.03, 1.0, 0.576, 0.025, 0.01], 'utility': [0.019], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.236, 0.367, 1.0, 0.045, 0.014, 0.012, 0.029], 'utility': [-0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.821], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.242, 0.537, 1.0, 0.046, 0.015, 0.014, 0.035], 'utility': [-0.163], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.34, 0.019, 0.097, 1.0, 0.074, 0.017, 0.012], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.007, -0.085, 0.005, 0.019, 0.414, -0.073]}} reward={'1': 7.178, '2': -1.092, '3': -1.092, '4': -0.052, '5': -1.198, '6': 7.178, '7': -1.7, '8': -0.521} t=76
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 1, '3': 3, '4': 2, '5': 4, '6': 7, '7': 2, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.0], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.097, 0.399, 0.02, 0.008, 0.009, 0.026, 1.0], 'utility': [-0.102], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.419, 0.193, 0.028, 0.015, 0.019, 0.065, 1.0], 'utility': [-0.072], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.081, 0.008, 0.025, 1.0, 0.404, 0.019, 0.008], 'utility': [0.019], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '5': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.262, 0.296, 1.0, 0.049, 0.014, 0.012, 0.028], 'utility': [0.027], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.003, 1.0, 0.001], 'utility': [0.621], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.142, 1.0, 0.244, 0.02, 0.008, 0.009, 0.031], 'utility': [-0.194], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.403, 0.028, 0.184, 1.0, 0.064, 0.018, 0.014], 'utility': [-0.067], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.004], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.087, 0.398, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.103], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.401, 0.177, 0.026, 0.014, 0.019, 0.065, 1.0], 'utility': [-0.065], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.094, 0.009, 0.027, 1.0, 0.482, 0.022, 0.009], 'utility': [0.018], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '5': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.248, 0.328, 1.0, 0.047, 0.014, 0.012, 0.028], 'utility': [0.005], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.714], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.269, 1.0, 0.682, 0.043, 0.016, 0.016, 0.046], 'utility': [-0.265], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.368, 0.023, 0.13, 1.0, 0.067, 0.017, 0.013], 'utility': [-0.044], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.035, 0.005, -0.13, -0.013, 0.018, 0.359, -0.084]}} reward={'1': 6.211, '2': -1.705, '3': -1.145, '4': -0.194, '5': -1.276, '6': 6.211, '7': -1.671, '8': -0.642} t=77
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 1, '3': 3, '4': 2, '5': 4, '6': 7, '7': 4, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.002], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.11, 0.403, 0.021, 0.009, 0.009, 0.028, 1.0], 'utility': [-0.103], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.437, 0.211, 0.03, 0.016, 0.02, 0.066, 1.0], 'utility': [-0.079], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '5': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.278, 0.268, 1.0, 0.051, 0.015, 0.012, 0.027], 'utility': [0.097], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.537], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.082, 0.008, 0.004, 0.005, 0.018], 'utility': [-0.273], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.444, 0.036, 0.273, 1.0, 0.064, 0.019, 0.017], 'utility': [-0.096], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.0], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.097, 0.399, 0.02, 0.008, 0.009, 0.026, 1.0], 'utility': [-0.102], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.419, 0.193, 0.028, 0.015, 0.019, 0.065, 1.0], 'utility': [-0.072], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.081, 0.008, 0.025, 1.0, 0.404, 0.019, 0.008], 'utility': [0.019], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '5': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.262, 0.296, 1.0, 0.049, 0.014, 0.012, 0.028], 'utility': [0.027], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.003, 1.0, 0.001], 'utility': [0.621], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.142, 1.0, 0.244, 0.02, 0.008, 0.009, 0.031], 'utility': [-0.194], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.403, 0.028, 0.184, 1.0, 0.064, 0.018, 0.014], 'utility': [-0.067], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.037, -0.084, -0.084, -0.024, 0.019, 0.311, -0.087]}} reward={'1': 5.349, '2': -1.792, '3': -1.043, '4': -0.384, '5': -0.525, '6': 5.349, '7': -1.761, '8': -0.194} t=78
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 0, '4': 2, '5': 4, '6': 0, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.005], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.128, 0.409, 0.023, 0.009, 0.01, 0.03, 1.0], 'utility': [-0.108], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.456, 0.231, 0.032, 0.016, 0.02, 0.067, 1.0], 'utility': [-0.086], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '5': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.298, 0.245, 1.0, 0.054, 0.015, 0.013, 0.027], 'utility': [0.098], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.0, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.462], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.025, 0.003, 0.002, 0.002, 0.009], 'utility': [-0.279], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.491, 0.047, 0.421, 1.0, 0.065, 0.021, 0.02], 'utility': [-0.13], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.002], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.11, 0.403, 0.021, 0.009, 0.009, 0.028, 1.0], 'utility': [-0.103], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.437, 0.211, 0.03, 0.016, 0.02, 0.066, 1.0], 'utility': [-0.079], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '5': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.278, 0.268, 1.0, 0.051, 0.015, 0.012, 0.027], 'utility': [0.097], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.537], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.082, 0.008, 0.004, 0.005, 0.018], 'utility': [-0.273], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.444, 0.036, 0.273, 1.0, 0.064, 0.019, 0.017], 'utility': [-0.096], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.026, -0.088, 0.097, -0.038, 0.019, 0.267, -0.091]}} reward={'1': 4.574, '2': -1.878, '3': -1.251, '4': -0.608, '5': -0.672, '6': 4.574, '7': -1.811, '8': -0.436} t=79
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 0, '4': 2, '5': 4, '6': 0, '7': 7, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.006], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.151, 0.418, 0.025, 0.01, 0.011, 0.033, 1.0], 'utility': [-0.117], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.475, 0.252, 0.034, 0.017, 0.021, 0.067, 1.0], 'utility': [-0.094], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '5': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.321, 0.226, 1.0, 0.058, 0.016, 0.013, 0.027], 'utility': [0.02], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.01, 1.0, 0.003], 'utility': [0.393], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.294], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.54, 0.061, 0.676, 1.0, 0.068, 0.024, 0.024], 'utility': [-0.095], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.005], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.128, 0.409, 0.023, 0.009, 0.01, 0.03, 1.0], 'utility': [-0.108], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.456, 0.231, 0.032, 0.016, 0.02, 0.067, 1.0], 'utility': [-0.086], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '5': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.298, 0.245, 1.0, 0.054, 0.015, 0.013, 0.027], 'utility': [0.098], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.0, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.462], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.025, 0.003, 0.002, 0.002, 0.009], 'utility': [-0.279], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.491, 0.047, 0.421, 1.0, 0.065, 0.021, 0.02], 'utility': [-0.13], 'ues_at_bs': [0.375, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.039, -0.091, 0.098, -0.055, 0.019, 0.229, -0.097]}} reward={'1': 3.87, '2': -2.424, '3': -1.515, '4': -0.375, '5': -1.481, '6': 3.87, '7': -2.748, '8': -0.911} t=80
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 1, '3': 5, '4': 2, '5': 4, '6': 7, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.008], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.182, 0.43, 0.028, 0.011, 0.012, 0.037, 1.0], 'utility': [-0.128], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.495, 0.277, 0.036, 0.018, 0.022, 0.068, 1.0], 'utility': [-0.101], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.1, 0.01, 0.028, 1.0, 0.539, 0.024, 0.009], 'utility': [0.017], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.348, 0.21, 1.0, 0.062, 0.017, 0.013, 0.027], 'utility': [-0.046], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.014, 1.0, 0.004], 'utility': [0.33], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [0.48], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.527, 0.072, 1.0, 0.893, 0.064, 0.024, 0.026], 'utility': [-0.093], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.006], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.151, 0.418, 0.025, 0.01, 0.011, 0.033, 1.0], 'utility': [-0.117], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.475, 0.252, 0.034, 0.017, 0.021, 0.067, 1.0], 'utility': [-0.094], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '5': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.321, 0.226, 1.0, 0.058, 0.016, 0.013, 0.027], 'utility': [0.02], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.01, 1.0, 0.003], 'utility': [0.393], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.294], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.54, 0.061, 0.676, 1.0, 0.068, 0.024, 0.024], 'utility': [-0.095], 'ues_at_bs': [0.375, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.056, -0.137, -0.037, -0.038, 0.019, 0.194, -0.105]}} reward={'1': 3.226, '2': 1.676, '3': 0.04, '4': -0.392, '5': -1.513, '6': 3.226, '7': 9.605, '8': -1.297} t=81
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 3, '3': 3, '4': 3, '5': 4, '6': 4, '7': 7, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.021], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.223, 0.443, 0.031, 0.013, 0.014, 0.041, 1.0], 'utility': [-0.142], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.515, 0.303, 0.038, 0.019, 0.022, 0.069, 1.0], 'utility': [-0.108], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.033, 1.0, 0.742, 0.03, 0.011], 'utility': [0.021], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.379, 0.197, 1.0, 0.067, 0.018, 0.014, 0.027], 'utility': [-0.069], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.311], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [0.48], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.333, 0.056, 1.0, 0.521, 0.04, 0.016, 0.018], 'utility': [-0.062], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.008], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.182, 0.43, 0.028, 0.011, 0.012, 0.037, 1.0], 'utility': [-0.128], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.495, 0.277, 0.036, 0.018, 0.022, 0.068, 1.0], 'utility': [-0.101], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.1, 0.01, 0.028, 1.0, 0.539, 0.024, 0.009], 'utility': [0.017], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.348, 0.21, 1.0, 0.062, 0.017, 0.013, 0.027], 'utility': [-0.046], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.014, 1.0, 0.004], 'utility': [0.33], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [0.48], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.527, 0.072, 1.0, 0.893, 0.064, 0.024, 0.026], 'utility': [-0.093], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.069, -0.038, 0.017, 0.161, -0.114]}} reward={'1': 2.9, '2': 1.532, '3': -0.03, '4': -0.129, '5': -1.477, '6': 2.9, '7': 9.605, '8': -1.17} t=82
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 3, '3': 3, '4': 3, '5': 4, '6': 4, '7': 7, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.027], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.279, 0.459, 0.035, 0.015, 0.016, 0.047, 1.0], 'utility': [-0.159], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.536, 0.333, 0.041, 0.02, 0.023, 0.07, 1.0], 'utility': [-0.089], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.155, 0.013, 0.037, 0.978, 1.0, 0.037, 0.013], 'utility': [0.031], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.416, 0.186, 1.0, 0.073, 0.019, 0.014, 0.028], 'utility': [-0.07], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.318], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.061, 0.007, 0.003, 0.004, 0.016], 'utility': [0.284], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.201, 0.041, 1.0, 0.293, 0.024, 0.01, 0.012], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.021], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.223, 0.443, 0.031, 0.013, 0.014, 0.041, 1.0], 'utility': [-0.142], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.515, 0.303, 0.038, 0.019, 0.022, 0.069, 1.0], 'utility': [-0.108], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.033, 1.0, 0.742, 0.03, 0.011], 'utility': [0.021], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.379, 0.197, 1.0, 0.067, 0.018, 0.014, 0.027], 'utility': [-0.069], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.311], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [0.48], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.333, 0.056, 1.0, 0.521, 0.04, 0.016, 0.018], 'utility': [-0.062], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.08, 0.48, -0.065, -0.02, 0.021, 0.145, -0.125]}} reward={'1': 2.9, '2': -0.491, '3': -0.491, '4': 0.256, '5': -1.265, '6': 2.9, '7': 5.675, '8': -0.435} t=83
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 1, '3': 5, '4': 2, '5': 4, '6': 4, '7': 7, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.023], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.354, 0.477, 0.04, 0.017, 0.019, 0.054, 1.0], 'utility': [-0.132], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.558, 0.366, 0.043, 0.021, 0.024, 0.071, 1.0], 'utility': [-0.123], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.012, 0.031, 0.708, 1.0, 0.034, 0.012], 'utility': [0.047], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.459, 0.177, 1.0, 0.081, 0.021, 0.015, 0.028], 'utility': [-0.1], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.313], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.125, 1.0, 0.185, 0.017, 0.007, 0.008, 0.028], 'utility': [0.124], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.115, 0.029, 1.0, 0.158, 0.014, 0.006, 0.008], 'utility': [0.048], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.027], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.279, 0.459, 0.035, 0.015, 0.016, 0.047, 1.0], 'utility': [-0.159], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.536, 0.333, 0.041, 0.02, 0.023, 0.07, 1.0], 'utility': [-0.089], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.155, 0.013, 0.037, 0.978, 1.0, 0.037, 0.013], 'utility': [0.031], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.416, 0.186, 1.0, 0.073, 0.019, 0.014, 0.028], 'utility': [-0.07], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.318], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.061, 0.007, 0.003, 0.004, 0.016], 'utility': [0.284], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.201, 0.041, 1.0, 0.293, 0.024, 0.01, 0.012], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, 0.284, -0.047, 0.004, 0.031, 0.145, -0.124]}} reward={'1': 2.9, '2': -1.618, '3': -1.618, '4': 0.947, '5': -1.626, '6': 2.9, '7': 0.485, '8': 0.218} t=84
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 5, '3': 5, '4': 2, '5': 4, '6': 4, '7': 7, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.067], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.456, 0.495, 0.046, 0.02, 0.022, 0.062, 1.0], 'utility': [-0.141], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.579, 0.403, 0.046, 0.022, 0.025, 0.072, 1.0], 'utility': [-0.13], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.127, 0.01, 0.025, 0.512, 1.0, 0.031, 0.01], 'utility': [0.108], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.509, 0.17, 1.0, 0.089, 0.022, 0.016, 0.029], 'utility': [-0.126], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.001, 0.001, 0.011, 1.0, 0.003], 'utility': [0.425], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.251, 1.0, 0.518, 0.037, 0.014, 0.015, 0.044], 'utility': [-0.009], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.062, 0.019, 1.0, 0.081, 0.008, 0.004, 0.005], 'utility': [0.146], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.023], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.354, 0.477, 0.04, 0.017, 0.019, 0.054, 1.0], 'utility': [-0.132], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.558, 0.366, 0.043, 0.021, 0.024, 0.071, 1.0], 'utility': [-0.123], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.012, 0.031, 0.708, 1.0, 0.034, 0.012], 'utility': [0.047], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.459, 0.177, 1.0, 0.081, 0.021, 0.015, 0.028], 'utility': [-0.1], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.313], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.125, 1.0, 0.185, 0.017, 0.007, 0.008, 0.028], 'utility': [0.124], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.115, 0.029, 1.0, 0.158, 0.014, 0.006, 0.008], 'utility': [0.048], 'ues_at_bs': [0.375, 0.125, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.118, 0.124, -0.026, 0.048, 0.047, 0.145, -0.127]}} reward={'1': 3.575, '2': -2.258, '3': -2.258, '4': 2.161, '5': -1.508, '6': 3.575, '7': 0.079, '8': 0.204} t=85
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 2, '3': 2, '4': 2, '5': 4, '6': 4, '7': 1, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.596, 0.515, 0.053, 0.023, 0.026, 0.072, 1.0], 'utility': [-0.097], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.602, 0.444, 0.049, 0.023, 0.025, 0.073, 1.0], 'utility': [-0.088], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.114, 0.009, 0.021, 0.371, 1.0, 0.028, 0.009], 'utility': [0.124], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.566, 0.164, 1.0, 0.1, 0.024, 0.017, 0.03], 'utility': [-0.121], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.472], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.319, 0.722, 1.0, 0.055, 0.018, 0.017, 0.045], 'utility': [-0.435], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.012, 1.0, 0.038, 0.004, 0.002, 0.003], 'utility': [0.26], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.067], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.456, 0.495, 0.046, 0.02, 0.022, 0.062, 1.0], 'utility': [-0.141], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.579, 0.403, 0.046, 0.022, 0.025, 0.072, 1.0], 'utility': [-0.13], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.127, 0.01, 0.025, 0.512, 1.0, 0.031, 0.01], 'utility': [0.108], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.509, 0.17, 1.0, 0.089, 0.022, 0.016, 0.029], 'utility': [-0.126], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.001, 0.001, 0.011, 1.0, 0.003], 'utility': [0.425], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.251, 1.0, 0.518, 0.037, 0.014, 0.015, 0.044], 'utility': [-0.009], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.062, 0.019, 1.0, 0.081, 0.008, 0.004, 0.005], 'utility': [0.146], 'ues_at_bs': [0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.132, -0.009, 0.01, 0.108, 0.108, 0.179, -0.136]}} reward={'1': 4.408, '2': -2.78, '3': -2.78, '4': 2.489, '5': -0.664, '6': 4.408, '7': -1.922, '8': 1.399} t=86
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 5, '3': 5, '4': 2, '5': 0, '6': 1, '7': 3, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.79, 0.536, 0.061, 0.028, 0.031, 0.084, 1.0], 'utility': [-0.106], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.624, 0.489, 0.053, 0.024, 0.026, 0.074, 1.0], 'utility': [-0.1], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.102, 0.007, 0.017, 0.269, 1.0, 0.026, 0.008], 'utility': [0.146], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.632, 0.159, 1.0, 0.112, 0.027, 0.018, 0.031], 'utility': [-0.199], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.572], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.191, 0.274, 1.0, 0.04, 0.012, 0.01, 0.023], 'utility': [-0.13], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.006, 1.0, 0.016, 0.002, 0.001, 0.001], 'utility': [0.344], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.596, 0.515, 0.053, 0.023, 0.026, 0.072, 1.0], 'utility': [-0.097], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.602, 0.444, 0.049, 0.023, 0.025, 0.073, 1.0], 'utility': [-0.088], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.114, 0.009, 0.021, 0.371, 1.0, 0.028, 0.009], 'utility': [0.124], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.566, 0.164, 1.0, 0.1, 0.024, 0.017, 0.03], 'utility': [-0.121], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.472], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.319, 0.722, 1.0, 0.055, 0.018, 0.017, 0.045], 'utility': [-0.435], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.012, 1.0, 0.038, 0.004, 0.002, 0.003], 'utility': [0.26], 'ues_at_bs': [0.375, 0.375, 0.25, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.102, -0.207, 0.07, 0.124, 0.124, 0.22, -0.093]}} reward={'1': 5.119, '2': -2.368, '3': -2.368, '4': 2.915, '5': -1.303, '6': 5.119, '7': -1.07, '8': 0.098} t=87
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 5, '3': 5, '4': 1, '5': 0, '6': 1, '7': 1, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.525, 0.067, 0.031, 0.034, 0.093, 0.942], 'utility': [-0.087], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.647, 0.54, 0.056, 0.025, 0.027, 0.076, 1.0], 'utility': [-0.087], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.091, 0.006, 0.014, 0.196, 1.0, 0.024, 0.007], 'utility': [0.171], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.707, 0.156, 1.0, 0.126, 0.029, 0.019, 0.032], 'utility': [-0.213], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.545], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.104, 0.104, 1.0, 0.028, 0.007, 0.005, 0.011], 'utility': [-0.003], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.006, 0.001, 0.0, 0.001], 'utility': [0.489], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.79, 0.536, 0.061, 0.028, 0.031, 0.084, 1.0], 'utility': [-0.106], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.624, 0.489, 0.053, 0.024, 0.026, 0.074, 1.0], 'utility': [-0.1], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.102, 0.007, 0.017, 0.269, 1.0, 0.026, 0.008], 'utility': [0.146], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.632, 0.159, 1.0, 0.112, 0.027, 0.018, 0.031], 'utility': [-0.199], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.572], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.191, 0.274, 1.0, 0.04, 0.012, 0.01, 0.023], 'utility': [-0.13], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.006, 1.0, 0.016, 0.002, 0.001, 0.001], 'utility': [0.344], 'ues_at_bs': [0.375, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.135, -0.112, 0.005, 0.146, 0.146, 0.256, -0.103]}} reward={'1': 5.363, '2': -2.105, '3': -2.105, '4': 3.417, '5': -0.38, '6': 5.363, '7': 1.824, '8': 1.824} t=88
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 5, '3': 5, '4': 2, '5': 5, '6': 2, '7': 1, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.4, 0.058, 0.027, 0.03, 0.08, 0.692], 'utility': [-0.084], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.67, 0.596, 0.06, 0.026, 0.028, 0.077, 1.0], 'utility': [-0.094], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.082, 0.005, 0.012, 0.144, 1.0, 0.022, 0.006], 'utility': [0.199], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.792, 0.153, 1.0, 0.143, 0.033, 0.021, 0.033], 'utility': [-0.22], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.575], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.052, 0.04, 1.0, 0.019, 0.004, 0.003, 0.005], 'utility': [0.062], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.002, 0.001, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.788], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.525, 0.067, 0.031, 0.034, 0.093, 0.942], 'utility': [-0.087], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.647, 0.54, 0.056, 0.025, 0.027, 0.076, 1.0], 'utility': [-0.087], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.091, 0.006, 0.014, 0.196, 1.0, 0.024, 0.007], 'utility': [0.171], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.707, 0.156, 1.0, 0.126, 0.029, 0.019, 0.032], 'utility': [-0.213], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.545], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.104, 0.104, 1.0, 0.028, 0.007, 0.005, 0.011], 'utility': [-0.003], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.006, 0.001, 0.0, 0.001], 'utility': [0.489], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.129, -0.087, 0.091, 0.171, 0.171, 0.268, -0.087]}} reward={'1': 5.367, '2': -2.156, '3': -2.156, '4': 3.971, '5': 0.77, '6': 5.367, '7': 4.197, '8': 4.197} t=89
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 5, '3': 5, '4': 2, '5': 5, '6': 5, '7': 0, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.014], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.3, 0.049, 0.024, 0.026, 0.068, 0.501], 'utility': [-0.076], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.693, 0.659, 0.064, 0.027, 0.029, 0.078, 1.0], 'utility': [-0.101], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.073, 0.005, 0.01, 0.106, 1.0, 0.02, 0.006], 'utility': [0.228], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.888, 0.151, 1.0, 0.163, 0.036, 0.023, 0.035], 'utility': [-0.234], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.551], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.016, 1.0, 0.013, 0.002, 0.001, 0.002], 'utility': [0.193], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.4, 0.058, 0.027, 0.03, 0.08, 0.692], 'utility': [-0.084], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.67, 0.596, 0.06, 0.026, 0.028, 0.077, 1.0], 'utility': [-0.094], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.082, 0.005, 0.012, 0.144, 1.0, 0.022, 0.006], 'utility': [0.199], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.792, 0.153, 1.0, 0.143, 0.033, 0.021, 0.033], 'utility': [-0.22], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.575], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.052, 0.04, 1.0, 0.019, 0.004, 0.003, 0.005], 'utility': [0.062], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.002, 0.001, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.788], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.133, -0.089, 0.21, 0.199, 0.199, 0.268, -0.089]}} reward={'1': 5.37, '2': -2.187, '3': -2.187, '4': 4.552, '5': 1.825, '6': 5.37, '7': 6.392, '8': 6.392} t=90
DEBUG:deepcomp.util.simulation:Step                           action={'1': 1, '2': 3, '3': 5, '4': 2, '5': 5, '6': 5, '7': 0, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.105], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.222, 0.041, 0.02, 0.023, 0.057, 0.358], 'utility': [-0.116], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.717, 0.729, 0.068, 0.029, 0.03, 0.079, 1.0], 'utility': [-0.026], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.066, 0.004, 0.008, 0.08, 1.0, 0.019, 0.005], 'utility': [0.24], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.996, 0.15, 1.0, 0.187, 0.04, 0.025, 0.037], 'utility': [-0.273], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.742], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.008, 1.0, 0.011, 0.002, 0.001, 0.001], 'utility': [-0.006], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.014], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.3, 0.049, 0.024, 0.026, 0.068, 0.501], 'utility': [-0.076], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.693, 0.659, 0.064, 0.027, 0.029, 0.078, 1.0], 'utility': [-0.101], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.073, 0.005, 0.01, 0.106, 1.0, 0.02, 0.006], 'utility': [0.228], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.888, 0.151, 1.0, 0.163, 0.036, 0.023, 0.035], 'utility': [-0.234], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.551], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.016, 1.0, 0.013, 0.002, 0.001, 0.002], 'utility': [0.193], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.137, -0.089, 0.32, 0.228, 0.228, 0.269, -0.089]}} reward={'1': 6.372, '2': -2.224, '3': -1.94, '4': 4.798, '5': 1.022, '6': 6.372, '7': 4.808, '8': 4.808} t=91
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 3, '4': 4, '5': 4, '6': 4, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.161, 0.033, 0.017, 0.019, 0.047, 0.252], 'utility': [-0.088], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.74, 0.807, 0.073, 0.03, 0.031, 0.081, 1.0], 'utility': [-0.023], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.06, 0.003, 0.007, 0.061, 1.0, 0.018, 0.005], 'utility': [0.271], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.134, 0.896, 0.193, 0.04, 0.024, 0.035], 'utility': [-0.245], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.831], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.006, 1.0, 0.014, 0.002, 0.001, 0.001], 'utility': [0.292], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.105], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.222, 0.041, 0.02, 0.023, 0.057, 0.358], 'utility': [-0.116], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.717, 0.729, 0.068, 0.029, 0.03, 0.079, 1.0], 'utility': [-0.026], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.066, 0.004, 0.008, 0.08, 1.0, 0.019, 0.005], 'utility': [0.24], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.996, 0.15, 1.0, 0.187, 0.04, 0.025, 0.037], 'utility': [-0.273], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.742], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.008, 1.0, 0.011, 0.002, 0.001, 0.001], 'utility': [-0.006], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.138, -0.026, 0.24, 0.0, 0.24, 0.319, -0.071]}} reward={'1': 7.95, '2': -1.874, '3': -1.64, '4': 5.422, '5': 2.303, '6': 7.95, '7': 6.983, '8': 6.983} t=92
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 3, '4': 4, '5': 6, '6': 4, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.099], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.115, 0.027, 0.014, 0.016, 0.038, 0.174], 'utility': [-0.053], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.764, 0.895, 0.078, 0.032, 0.032, 0.082, 1.0], 'utility': [-0.02], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.055, 0.003, 0.006, 0.047, 1.0, 0.017, 0.004], 'utility': [0.298], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.12, 0.801, 0.199, 0.041, 0.023, 0.033], 'utility': [-0.149], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.001, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.007, 1.0, 0.026, 0.002, 0.001, 0.002], 'utility': [0.229], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.161, 0.033, 0.017, 0.019, 0.047, 0.252], 'utility': [-0.088], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.74, 0.807, 0.073, 0.03, 0.031, 0.081, 1.0], 'utility': [-0.023], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.06, 0.003, 0.007, 0.061, 1.0, 0.018, 0.005], 'utility': [0.271], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.134, 0.896, 0.193, 0.04, 0.024, 0.035], 'utility': [-0.245], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.831], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.006, 1.0, 0.014, 0.002, 0.001, 0.001], 'utility': [0.292], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.119, -0.023, 0.349, 0.0, 0.271, 0.397, -0.056]}} reward={'1': 9.009, '2': -1.18, '3': -1.05, '4': 5.965, '5': 2.862, '6': 9.009, '7': 7.203, '8': 7.203} t=93
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 3, '4': 4, '5': 6, '6': 0, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.041], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.08, 0.021, 0.012, 0.013, 0.03, 0.118], 'utility': [-0.009], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.788, 0.992, 0.083, 0.033, 0.033, 0.083, 1.0], 'utility': [-0.017], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.052, 0.003, 0.005, 0.038, 1.0, 0.017, 0.004], 'utility': [0.32], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.108, 0.718, 0.207, 0.041, 0.023, 0.031], 'utility': [-0.185], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.022, 0.009, 1.0, 0.057, 0.004, 0.002, 0.002], 'utility': [0.035], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.099], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.115, 0.027, 0.014, 0.016, 0.038, 0.174], 'utility': [-0.053], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.764, 0.895, 0.078, 0.032, 0.032, 0.082, 1.0], 'utility': [-0.02], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.055, 0.003, 0.006, 0.047, 1.0, 0.017, 0.004], 'utility': [0.298], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.12, 0.801, 0.199, 0.041, 0.023, 0.033], 'utility': [-0.149], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.001, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.007, 1.0, 0.026, 0.002, 0.001, 0.002], 'utility': [0.229], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.074, -0.02, 0.36, 0.0, 0.298, 0.45, -0.037]}} reward={'1': 9.591, '2': -0.945, '3': -0.843, '4': 6.402, '5': 2.131, '6': 9.591, '7': 5.668, '8': 5.668} t=94
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 0, '3': 3, '4': 4, '5': 2, '6': 4, '7': 4, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.056], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.055, 0.016, 0.009, 0.011, 0.023, 0.079], 'utility': [0.02], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.737, 1.0, 0.081, 0.031, 0.031, 0.077, 0.908], 'utility': [0.039], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.005, 0.032, 1.0, 0.018, 0.004], 'utility': [0.336], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.097, 0.646, 0.216, 0.042, 0.022, 0.029], 'utility': [-0.132], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.014, 1.0, 0.127, 0.008, 0.003, 0.004], 'utility': [0.074], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [0.414], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.041], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.08, 0.021, 0.012, 0.013, 0.03, 0.118], 'utility': [-0.009], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.788, 0.992, 0.083, 0.033, 0.033, 0.083, 1.0], 'utility': [-0.017], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.052, 0.003, 0.005, 0.038, 1.0, 0.017, 0.004], 'utility': [0.32], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.108, 0.718, 0.207, 0.041, 0.023, 0.031], 'utility': [-0.185], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.022, 0.009, 1.0, 0.057, 0.004, 0.002, 0.002], 'utility': [0.035], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.017, 0.283, 0.0, 0.32, 0.48, -0.013]}} reward={'1': 9.442, '2': -0.485, '3': 0.022, '4': 6.71, '5': 0.947, '6': 9.442, '7': 2.38, '8': 2.38} t=95
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 7, '3': 3, '4': 4, '5': 2, '6': 4, '7': 4, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.009], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.036, 0.012, 0.007, 0.008, 0.017, 0.051], 'utility': [0.09], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.682, 1.0, 0.077, 0.03, 0.029, 0.071, 0.817], 'utility': [0.041], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.004, 0.027, 1.0, 0.019, 0.004], 'utility': [0.344], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.089, 0.583, 0.228, 0.042, 0.022, 0.028], 'utility': [-0.11], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.048, 0.02, 1.0, 0.269, 0.013, 0.005, 0.006], 'utility': [-0.002], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.001, 0.001, 1.0, 0.001, 0.0, 0.0, 0.0], 'utility': [0.116], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.056], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.055, 0.016, 0.009, 0.011, 0.023, 0.079], 'utility': [0.02], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.737, 1.0, 0.081, 0.031, 0.031, 0.077, 0.908], 'utility': [0.039], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.005, 0.032, 1.0, 0.018, 0.004], 'utility': [0.336], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.097, 0.646, 0.216, 0.042, 0.022, 0.029], 'utility': [-0.132], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.014, 1.0, 0.127, 0.008, 0.003, 0.004], 'utility': [0.074], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [0.414], 'ues_at_bs': [0.375, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [-0.024, 0.039, 0.119, 0.0, 0.336, 0.472, 0.039]}} reward={'1': 10.087, '2': 0.138, '3': 0.412, '4': 6.873, '5': 0.083, '6': 10.087, '7': 0.009, '8': 0.027} t=96
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 7, '3': 3, '4': 2, '5': 2, '6': 4, '7': 0, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.003], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.023, 0.009, 0.006, 0.006, 0.012, 0.032], 'utility': [0.167], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.631, 1.0, 0.074, 0.028, 0.027, 0.065, 0.735], 'utility': [0.044], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.051, 0.003, 0.004, 0.024, 1.0, 0.021, 0.004], 'utility': [0.344], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.081, 0.529, 0.242, 0.044, 0.022, 0.027], 'utility': [-0.123], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.067, 0.027, 1.0, 0.516, 0.022, 0.008, 0.009], 'utility': [-0.046], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.003, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.074], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.009], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.036, 0.012, 0.007, 0.008, 0.017, 0.051], 'utility': [0.09], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.682, 1.0, 0.077, 0.03, 0.029, 0.071, 0.817], 'utility': [0.041], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.004, 0.027, 1.0, 0.019, 0.004], 'utility': [0.344], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.089, 0.583, 0.228, 0.042, 0.022, 0.028], 'utility': [-0.11], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.048, 0.02, 1.0, 0.269, 0.013, 0.005, 0.006], 'utility': [-0.002], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.001, 0.001, 1.0, 0.001, 0.0, 0.0, 0.0], 'utility': [0.116], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.007, 0.041, 0.001, -0.002, 0.344, 0.504, 0.041]}} reward={'1': 10.026, '2': 0.581, '3': 0.698, '4': 6.88, '5': -0.027, '6': 10.026, '7': -0.706, '8': -0.635} t=97
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 7, '3': 3, '4': 2, '5': 2, '6': 4, '7': 0, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.021], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.014, 0.006, 0.004, 0.005, 0.008, 0.019], 'utility': [0.253], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.582, 1.0, 0.071, 0.026, 0.025, 0.059, 0.66], 'utility': [0.047], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.054, 0.003, 0.004, 0.023, 1.0, 0.025, 0.004], 'utility': [0.337], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.075, 0.482, 0.258, 0.045, 0.022, 0.026], 'utility': [-0.133], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.848], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.086], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.01, 0.009, 1.0, 0.005, 0.001, 0.001, 0.001], 'utility': [0.159], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.003], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.023, 0.009, 0.006, 0.006, 0.012, 0.032], 'utility': [0.167], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.631, 1.0, 0.074, 0.028, 0.027, 0.065, 0.735], 'utility': [0.044], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.051, 0.003, 0.004, 0.024, 1.0, 0.021, 0.004], 'utility': [0.344], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.081, 0.529, 0.242, 0.044, 0.022, 0.027], 'utility': [-0.123], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.067, 0.027, 1.0, 0.516, 0.022, 0.008, 0.009], 'utility': [-0.046], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.003, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.074], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.029, 0.044, -0.032, -0.046, 0.344, 0.501, 0.044]}} reward={'1': 8.691, '2': 1.112, '3': 1.042, '4': 6.73, '5': 0.357, '6': 8.691, '7': -0.729, '8': -0.399} t=98
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 7, '3': 3, '4': 7, '5': 2, '6': 4, '7': 0, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.008, 0.004, 0.003, 0.003, 0.006, 0.011], 'utility': [0.349], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.536, 1.0, 0.068, 0.025, 0.023, 0.054, 0.592], 'utility': [0.051], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.058, 0.003, 0.004, 0.022, 1.0, 0.03, 0.005], 'utility': [0.322], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.07, 0.442, 0.278, 0.047, 0.022, 0.025], 'utility': [-0.167], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.724], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.097], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.021, 1.0, 0.011, 0.002, 0.001, 0.003], 'utility': [0.208], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.021], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.014, 0.006, 0.004, 0.005, 0.008, 0.019], 'utility': [0.253], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.582, 1.0, 0.071, 0.026, 0.025, 0.059, 0.66], 'utility': [0.047], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.054, 0.003, 0.004, 0.023, 1.0, 0.025, 0.004], 'utility': [0.337], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.075, 0.482, 0.258, 0.045, 0.022, 0.026], 'utility': [-0.133], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.848], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.086], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.01, 0.009, 1.0, 0.005, 0.001, 0.001, 0.001], 'utility': [0.159], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.056, 0.047, -0.02, -0.086, 0.337, 0.435, 0.047]}} reward={'1': 7.316, '2': 1.553, '3': 1.339, '4': 6.434, '5': 0.226, '6': 7.316, '7': -0.769, '8': -0.378} t=99
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 7, '3': 3, '4': 7, '5': 2, '6': 4, '7': 0, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.012], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.112, 0.056, -0.055, -0.104, 0.3, 0.3, 0.056]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.005, 0.002, 0.002, 0.002, 0.003, 0.006], 'utility': [0.459], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.112, 0.056, -0.055, -0.104, 0.3, 0.3, 0.056]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.493, 1.0, 0.065, 0.023, 0.021, 0.049, 0.531], 'utility': [0.056], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.112, 0.056, -0.055, -0.104, 0.3, 0.3, 0.056]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.065, 0.003, 0.005, 0.022, 1.0, 0.037, 0.006], 'utility': [0.3], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.112, 0.056, -0.055, -0.104, 0.3, 0.3, 0.056]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.065, 0.407, 0.301, 0.049, 0.022, 0.025], 'utility': [-0.178], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.112, 0.056, -0.055, -0.104, 0.3, 0.3, 0.056]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.0, 0.0, 0.0, 0.003, 1.0, 0.003], 'utility': [0.588], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.112, 0.056, -0.055, -0.104, 0.3, 0.3, 0.056]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.104], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.112, 0.056, -0.055, -0.104, 0.3, 0.3, 0.056]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.055, 0.043, 1.0, 0.02, 0.004, 0.003, 0.006], 'utility': [0.118], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.112, 0.056, -0.055, -0.104, 0.3, 0.3, 0.056]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.008, 0.004, 0.003, 0.003, 0.006, 0.011], 'utility': [0.349], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.536, 1.0, 0.068, 0.025, 0.023, 0.054, 0.592], 'utility': [0.051], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.058, 0.003, 0.004, 0.022, 1.0, 0.03, 0.005], 'utility': [0.322], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '5': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.07, 0.442, 0.278, 0.047, 0.022, 0.025], 'utility': [-0.167], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.724], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.097], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.021, 1.0, 0.011, 0.002, 0.001, 0.003], 'utility': [0.208], 'ues_at_bs': [0.375, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.078, 0.051, -0.019, -0.097, 0.322, 0.366, 0.051]}} reward={'1': 5.997, '2': 2.246, '3': 1.792, '4': 6.007, '5': 0.194, '6': 5.997, '7': -1.344, '8': -1.096} t=100
INFO:deepcomp.util.simulation:Video saved                    path=/home/abhishek/cmc/result/DD-CoMP/good/videos/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-28_05-09-12.html
INFO:deepcomp.util.simulation:Gif saved                      path=/home/abhishek/cmc/result/DD-CoMP/good/videos/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-28_05-09-12.gif
DEBUG:deepcomp.util.simulation:Episode complete               avg_step_reward=13.475 eps_duration=496.155 scalar_metrics=['sum_utility'] vector_metrics=['dr', 'utility']
INFO:deepcomp.util.simulation:Scalar results                 results={'episode': [0], 'eps_duration_mean': [496.155], 'eps_duration_std': [496.155], 'step_reward_mean': [13.475], 'step_reward_std': [15.027], 'sum_utility_mean': [12.975], 'sum_utility_std': [15.047]}
INFO:deepcomp.util.simulation:Mean results                   results={'episode': 0.0, 'eps_duration_mean': 496.155, 'eps_duration_std': 496.155, 'step_reward_mean': 13.475, 'step_reward_std': 15.027, 'sum_utility_mean': 12.975, 'sum_utility_std': 15.047}
INFO:deepcomp.util.simulation:Simulation complete            avg_eps_reward=1347.5 eps_length=100 num_episodes=1 step_reward_mean=13.475 step_reward_std=0.0
INFO:deepcomp.util.simulation:Starting evaluation            fast_ues=2 num_episodes=100 num_workers=1 slow_ues=5 static_ues=1
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [07:58<00:00,  4.79s/it]
INFO:deepcomp.util.simulation:Scalar results                 results={'episode': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 'eps_duration_mean': [4.495, 4.765, 5.008, 4.667, 4.991, 4.537, 6.175, 4.205, 4.464, 4.431, 4.182, 4.471, 4.752, 5.615, 4.664, 4.11, 4.324, 4.452, 4.3, 4.344, 4.294, 4.402, 6.352, 4.526, 4.441, 4.478, 6.161, 4.201, 4.388, 4.622, 4.368, 4.612, 6.755, 4.456, 4.302, 4.743, 4.542, 4.373, 4.509, 4.977, 5.718, 4.522, 4.309, 4.59, 4.252, 6.218, 4.877, 4.946, 4.645, 4.686, 5.11, 4.699, 4.947, 4.546, 4.985, 4.752, 4.68, 4.695, 4.895, 6.298, 4.398, 4.607, 4.547, 4.386, 5.76, 4.677, 4.19, 4.566, 6.282, 4.617, 4.238, 4.413, 4.396, 4.438, 5.878, 4.413, 4.438, 4.349, 4.185, 4.38, 4.307, 5.055, 4.943, 4.75, 4.582, 5.291, 4.862, 4.92, 6.643, 4.23, 5.698, 4.228, 4.199, 4.239, 5.49, 6.079, 6.188, 4.264, 4.186, 4.278], 'eps_duration_std': [4.495, 4.765, 5.008, 4.667, 4.991, 4.537, 6.175, 4.205, 4.464, 4.431, 4.182, 4.471, 4.752, 5.615, 4.664, 4.11, 4.324, 4.452, 4.3, 4.344, 4.294, 4.402, 6.352, 4.526, 4.441, 4.478, 6.161, 4.201, 4.388, 4.622, 4.368, 4.612, 6.755, 4.456, 4.302, 4.743, 4.542, 4.373, 4.509, 4.977, 5.718, 4.522, 4.309, 4.59, 4.252, 6.218, 4.877, 4.946, 4.645, 4.686, 5.11, 4.699, 4.947, 4.546, 4.985, 4.752, 4.68, 4.695, 4.895, 6.298, 4.398, 4.607, 4.547, 4.386, 5.76, 4.677, 4.19, 4.566, 6.282, 4.617, 4.238, 4.413, 4.396, 4.438, 5.878, 4.413, 4.438, 4.349, 4.185, 4.38, 4.307, 5.055, 4.943, 4.75, 4.582, 5.291, 4.862, 4.92, 6.643, 4.23, 5.698, 4.228, 4.199, 4.239, 5.49, 6.079, 6.188, 4.264, 4.186, 4.278], 'step_reward_mean': [13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475, 13.475], 'step_reward_std': [15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027, 15.027], 'sum_utility_mean': [12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975, 12.975], 'sum_utility_std': [15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047, 15.047]}
INFO:deepcomp.util.simulation:Mean results                   results={'episode': 49.5, 'eps_duration_mean': 4.784, 'eps_duration_std': 4.784, 'step_reward_mean': 13.475, 'step_reward_std': 15.027, 'sum_utility_mean': 12.975, 'sum_utility_std': 15.047}
INFO:deepcomp.util.simulation:Simulation complete            avg_eps_reward=1347.5 eps_length=100 num_episodes=100 step_reward_mean=13.475 step_reward_std=0.0
INFO:deepcomp.util.simulation:Writing scalar results         file=/home/abhishek/cmc/result/DD-CoMP/good/test/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-28_05-09-12.csv
INFO:deepcomp.util.simulation:Writing vector results         file=/home/abhishek/cmc/result/DD-CoMP/good/test/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-28_05-09-12_dr.pkl metric=dr
INFO:deepcomp.util.simulation:Writing vector results         file=/home/abhishek/cmc/result/DD-CoMP/good/test/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-28_05-09-12_utility.pkl metric=utility
INFO:deepcomp.main:Finished                       agent=/home/abhishek/cmc/result/DD-CoMP/good/train/PPO_2022-04-28_03-24-17/PPO_MultiAgentMobileEnv_95ec4_00000_0_2022-04-28_03-24-19/checkpoint_000050/checkpoint-50
abhishek@abhishek-pc:~$ 
```


