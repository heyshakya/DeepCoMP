```
          policy_loss: -0.01474168710410595
          total_loss: 182.94503784179688
          vf_explained_var: 0.4667660593986511
          vf_loss: 182.95640563964844
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8367607593536377
          entropy_coeff: 0.0
          kl: 0.007682356517761946
          model: {}
          policy_loss: -0.01028455886989832
          total_loss: 169.4307098388672
          vf_explained_var: 0.6222289800643921
          vf_loss: 169.43753051757812
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7624638080596924
          entropy_coeff: 0.0
          kl: 0.01554951723664999
          model: {}
          policy_loss: -0.016047950834035873
          total_loss: 5748.109375
          vf_explained_var: 2.095776153510087e-06
          vf_loss: 5748.12060546875
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6265838146209717
          entropy_coeff: 0.0
          kl: 0.010056018829345703
          model: {}
          policy_loss: -0.017099743708968163
          total_loss: 275.80389404296875
          vf_explained_var: 0.6138132214546204
          vf_loss: 275.8179931640625
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.684657335281372
          entropy_coeff: 0.0
          kl: 0.01340053416788578
          model: {}
          policy_loss: -0.021396372467279434
          total_loss: 182.47132873535156
          vf_explained_var: 0.6128275990486145
          vf_loss: 182.4866943359375
    num_agent_steps_sampled: 416000
    num_agent_steps_trained: 416000
    num_steps_sampled: 52000
    num_steps_trained: 52000
  iterations_since_restore: 13
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.01363636363636
    ram_util_percent: 56.82784090909092
  pid: 3846
  policy_reward_max:
    '1': 379.9996923585933
    '2': 53.228779032703926
    '3': 111.1049203386392
    '4': 203.10886955533712
    '5': 68.08377573114646
    '6': 363.6407414594212
    '7': 213.5775684911459
    '8': 55.87189796160214
  policy_reward_mean:
    '1': 360.342512532006
    '2': -40.112886997273385
    '3': 39.96777234109479
    '4': 172.29315536862373
    '5': -22.592610377329326
    '6': 317.7843477933365
    '7': 95.24192016890888
    '8': -5.851817064864099
  policy_reward_min:
    '1': 303.3015447575422
    '2': -110.50103067498914
    '3': -61.79930702545966
    '4': 130.98108833282564
    '5': -69.50654822980226
    '6': 252.00615257234102
    '7': 26.117504758005936
    '8': -59.27207324369715
  sampler_perf:
    mean_action_processing_ms: 0.19438566553741135
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 36.74870275170696
    mean_inference_ms: 5.8072974442492225
    mean_raw_obs_processing_ms: 0.6655030721830422
  time_since_restore: 1502.2476530075073
  time_this_iter_s: 130.01738047599792
  time_total_s: 1502.2476530075073
  timers:
    learn_throughput: 144.286
    learn_time_ms: 27722.762
    load_throughput: 301989.646
    load_time_ms: 13.245
    sample_throughput: 41.723
    sample_time_ms: 95870.797
    update_time_ms: 13.922
  timestamp: 1651206147
  timesteps_since_restore: 0
  timesteps_total: 52000
  training_iteration: 13
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.4/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     13 |          1502.25 | 52000 |  917.072 |              1178.28 |              754.781 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 448000
  custom_metrics:
    eps_sum_utility_max: 1066.525565886466
    eps_sum_utility_mean: 823.1349184845914
    eps_sum_utility_min: 484.3216318023563
    sum_utility_max: 27.824576552237044
    sum_utility_mean: 20.109037861679305
    sum_utility_min: -8.856092900234987
  date: 2022-04-29_09-54-47
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1155.2784397724517
  episode_reward_mean: 929.3459854657859
  episode_reward_min: 762.2316932253735
  episodes_this_iter: 40
  episodes_total: 560
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.816954493522644
          entropy_coeff: 0.0
          kl: 0.008457611314952374
          model: {}
          policy_loss: -0.014542454853653908
          total_loss: 6602.81201171875
          vf_explained_var: -1.5497207641601562e-06
          vf_loss: 6602.82421875
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6717976331710815
          entropy_coeff: 0.0
          kl: 0.01202569529414177
          model: {}
          policy_loss: -0.017901621758937836
          total_loss: 196.1526641845703
          vf_explained_var: 0.6711781620979309
          vf_loss: 196.1669464111328
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.757423996925354
          entropy_coeff: 0.0
          kl: 0.012747642584145069
          model: {}
          policy_loss: -0.017784979194402695
          total_loss: 153.8006591796875
          vf_explained_var: 0.5853449702262878
          vf_loss: 153.81459045410156
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6816127300262451
          entropy_coeff: 0.0
          kl: 0.008719840086996555
          model: {}
          policy_loss: -0.012038003653287888
          total_loss: 98.3280258178711
          vf_explained_var: 0.7169031500816345
          vf_loss: 98.33614349365234
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8287345170974731
          entropy_coeff: 0.0
          kl: 0.0079902159050107
          model: {}
          policy_loss: -0.01334370020776987
          total_loss: 127.81355285644531
          vf_explained_var: 0.7210641503334045
          vf_loss: 127.82330322265625
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7369885444641113
          entropy_coeff: 0.0
          kl: 0.011372600682079792
          model: {}
          policy_loss: -0.016771674156188965
          total_loss: 5003.29638671875
          vf_explained_var: 1.7496847704023821e-06
          vf_loss: 5003.3095703125
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5832493305206299
          entropy_coeff: 0.0
          kl: 0.012795187532901764
          model: {}
          policy_loss: -0.021590420976281166
          total_loss: 265.1010437011719
          vf_explained_var: 0.6218706965446472
          vf_loss: 265.11883544921875
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.668750286102295
          entropy_coeff: 0.0
          kl: 0.011390233412384987
          model: {}
          policy_loss: -0.023525172844529152
          total_loss: 144.79977416992188
          vf_explained_var: 0.6897504925727844
          vf_loss: 144.8181610107422
    num_agent_steps_sampled: 448000
    num_agent_steps_trained: 448000
    num_steps_sampled: 56000
    num_steps_trained: 56000
  iterations_since_restore: 14
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.11851851851851
    ram_util_percent: 56.831746031746036
  pid: 3846
  policy_reward_max:
    '1': 380.0228664395912
    '2': 34.464406644247234
    '3': 104.57103106239293
    '4': 195.2791404575477
    '5': 43.18142415835939
    '6': 348.4427954869661
    '7': 172.50204808442055
    '8': 55.87189796160214
  policy_reward_mean:
    '1': 362.5136980689877
    '2': -43.852406646227976
    '3': 41.82695745347692
    '4': 174.5604751228001
    '5': -24.254507925777283
    '6': 320.526371391634
    '7': 97.55508036517502
    '8': 0.470317635717468
  policy_reward_min:
    '1': 327.672150998807
    '2': -114.33112027250957
    '3': -33.628978714520805
    '4': 147.3341109069954
    '5': -68.0158957610325
    '6': 265.28399598863103
    '7': 21.7304739764342
    '8': -59.27207324369715
  sampler_perf:
    mean_action_processing_ms: 0.19640888075181792
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 37.39477502829209
    mean_inference_ms: 5.861582772062836
    mean_raw_obs_processing_ms: 0.67259997902858
  time_since_restore: 1642.4814054965973
  time_this_iter_s: 140.23375248908997
  time_total_s: 1642.4814054965973
  timers:
    learn_throughput: 141.745
    learn_time_ms: 28219.753
    load_throughput: 287633.743
    load_time_ms: 13.907
    sample_throughput: 40.274
    sample_time_ms: 99320.65
    update_time_ms: 14.137
  timestamp: 1651206287
  timesteps_since_restore: 0
  timesteps_total: 56000
  training_iteration: 14
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     14 |          1642.48 | 56000 |  929.346 |              1155.28 |              762.232 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 480000
  custom_metrics:
    eps_sum_utility_max: 1150.6455568498523
    eps_sum_utility_mean: 888.4654634219545
    eps_sum_utility_min: 630.1275531731005
    sum_utility_max: 26.86048372778746
    sum_utility_mean: 19.70427697267888
    sum_utility_min: -7.6732227231123185
  date: 2022-04-29_09-57-08
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1250.8547107954766
  episode_reward_mean: 966.753706910237
  episode_reward_min: 778.9798727791435
  episodes_this_iter: 40
  episodes_total: 600
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8295317888259888
          entropy_coeff: 0.0
          kl: 0.0108506940305233
          model: {}
          policy_loss: -0.014503655955195427
          total_loss: 5584.16943359375
          vf_explained_var: -1.0267381185258273e-06
          vf_loss: 5584.1806640625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6470906734466553
          entropy_coeff: 0.0
          kl: 0.011661089025437832
          model: {}
          policy_loss: -0.017565913498401642
          total_loss: 273.32598876953125
          vf_explained_var: 0.48472273349761963
          vf_loss: 273.34002685546875
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7268824577331543
          entropy_coeff: 0.0
          kl: 0.00870149489492178
          model: {}
          policy_loss: -0.018599461764097214
          total_loss: 131.1975555419922
          vf_explained_var: 0.6532800197601318
          vf_loss: 131.21353149414062
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6673067808151245
          entropy_coeff: 0.0
          kl: 0.007611253298819065
          model: {}
          policy_loss: -0.011306468397378922
          total_loss: 69.4421615600586
          vf_explained_var: 0.7922340035438538
          vf_loss: 69.45004272460938
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8138960599899292
          entropy_coeff: 0.0
          kl: 0.009266125969588757
          model: {}
          policy_loss: -0.013071609660983086
          total_loss: 201.84127807617188
          vf_explained_var: 0.4934515058994293
          vf_loss: 201.85015869140625
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7102429866790771
          entropy_coeff: 0.0
          kl: 0.008214497938752174
          model: {}
          policy_loss: -0.011063162237405777
          total_loss: 4365.1220703125
          vf_explained_var: 1.1305654652460362e-06
          vf_loss: 4365.130859375
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5502070188522339
          entropy_coeff: 0.0
          kl: 0.013060467317700386
          model: {}
          policy_loss: -0.01923404261469841
          total_loss: 185.42721557617188
          vf_explained_var: 0.7228267192840576
          vf_loss: 185.4425506591797
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.659335970878601
          entropy_coeff: 0.0
          kl: 0.008457565680146217
          model: {}
          policy_loss: -0.019302064552903175
          total_loss: 220.1724090576172
          vf_explained_var: 0.519468367099762
          vf_loss: 220.1879119873047
    num_agent_steps_sampled: 480000
    num_agent_steps_trained: 480000
    num_steps_sampled: 60000
    num_steps_trained: 60000
  iterations_since_restore: 15
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.08994708994709
    ram_util_percent: 56.82539682539682
  pid: 3846
  policy_reward_max:
    '1': 380.0228664395912
    '2': 58.735436721570906
    '3': 104.57103106239293
    '4': 202.5752001575831
    '5': 68.15507090358857
    '6': 345.5992690342254
    '7': 169.29229240929556
    '8': 85.11700141682157
  policy_reward_mean:
    '1': 363.86530295289754
    '2': -34.190045276929645
    '3': 46.34584668262137
    '4': 174.88028769301866
    '5': -17.070910711225846
    '6': 325.1614227824424
    '7': 97.43438258736491
    '8': 10.327420200047674
  policy_reward_min:
    '1': 329.33449229577235
    '2': -114.33112027250957
    '3': -33.628978714520805
    '4': 147.3341109069954
    '5': -62.406473909768195
    '6': 265.28399598863103
    '7': 21.7304739764342
    '8': -53.594293450465194
  sampler_perf:
    mean_action_processing_ms: 0.19846530380252092
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 38.0200850549507
    mean_inference_ms: 5.915886077100346
    mean_raw_obs_processing_ms: 0.6793834535866111
  time_since_restore: 1782.6538462638855
  time_this_iter_s: 140.1724407672882
  time_total_s: 1782.6538462638855
  timers:
    learn_throughput: 141.032
    learn_time_ms: 28362.445
    load_throughput: 286122.886
    load_time_ms: 13.98
    sample_throughput: 39.65
    sample_time_ms: 100881.857
    update_time_ms: 14.426
  timestamp: 1651206428
  timesteps_since_restore: 0
  timesteps_total: 60000
  training_iteration: 15
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     15 |          1782.65 | 60000 |  966.754 |              1250.85 |               778.98 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 512000
  custom_metrics:
    eps_sum_utility_max: 1160.0196540071977
    eps_sum_utility_mean: 937.6394695098337
    eps_sum_utility_min: 645.7037201065021
    sum_utility_max: 26.86048372778746
    sum_utility_mean: 19.46130885606807
    sum_utility_min: -7.6732227231123185
  date: 2022-04-29_09-59-29
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1250.8547107954766
  episode_reward_mean: 998.8132249973929
  episode_reward_min: 790.8183644842259
  episodes_this_iter: 40
  episodes_total: 640
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8358794450759888
          entropy_coeff: 0.0
          kl: 0.011243659071624279
          model: {}
          policy_loss: -0.012201002798974514
          total_loss: 4796.81689453125
          vf_explained_var: -6.114282768976409e-07
          vf_loss: 4796.8251953125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6333575248718262
          entropy_coeff: 0.0
          kl: 0.008789551444351673
          model: {}
          policy_loss: -0.015169255435466766
          total_loss: 220.29776000976562
          vf_explained_var: 0.5530927181243896
          vf_loss: 220.3102569580078
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7253732681274414
          entropy_coeff: 0.0
          kl: 0.008084745146334171
          model: {}
          policy_loss: -0.014818635769188404
          total_loss: 149.2059326171875
          vf_explained_var: 0.6316909193992615
          vf_loss: 149.2183074951172
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6095466613769531
          entropy_coeff: 0.0
          kl: 0.01176687702536583
          model: {}
          policy_loss: -0.015413426794111729
          total_loss: 58.28687286376953
          vf_explained_var: 0.8348073363304138
          vf_loss: 58.2969970703125
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7962639331817627
          entropy_coeff: 0.0
          kl: 0.007299164310097694
          model: {}
          policy_loss: -0.011977323330938816
          total_loss: 168.95896911621094
          vf_explained_var: 0.5722536444664001
          vf_loss: 168.96763610839844
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.66331148147583
          entropy_coeff: 0.0
          kl: 0.010063269175589085
          model: {}
          policy_loss: -0.012241298332810402
          total_loss: 3903.66455078125
          vf_explained_var: 1.1286427934464882e-06
          vf_loss: 3903.673828125
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5276588201522827
          entropy_coeff: 0.0
          kl: 0.014837373048067093
          model: {}
          policy_loss: -0.02064153365790844
          total_loss: 152.51803588867188
          vf_explained_var: 0.7770939469337463
          vf_loss: 152.5342254638672
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6549094915390015
          entropy_coeff: 0.0
          kl: 0.010870104655623436
          model: {}
          policy_loss: -0.01840384490787983
          total_loss: 190.6122589111328
          vf_explained_var: 0.5777278542518616
          vf_loss: 190.62579345703125
    num_agent_steps_sampled: 512000
    num_agent_steps_trained: 512000
    num_steps_sampled: 64000
    num_steps_trained: 64000
  iterations_since_restore: 16
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.02105263157895
    ram_util_percent: 56.84315789473685
  pid: 3846
  policy_reward_max:
    '1': 378.5233040680125
    '2': 58.735436721570906
    '3': 117.33426780764302
    '4': 202.5752001575831
    '5': 68.15507090358857
    '6': 345.5992690342254
    '7': 173.3967621915884
    '8': 91.54633922818802
  policy_reward_mean:
    '1': 364.24473148483355
    '2': -28.32674554364137
    '3': 50.36857338356757
    '4': 176.70526282524526
    '5': -12.889349849338942
    '6': 328.7692615724534
    '7': 103.89146771535587
    '8': 16.05002340891766
  policy_reward_min:
    '1': 317.03723671214885
    '2': -91.3108590260437
    '3': -4.290803493753662
    '4': 154.5459122890265
    '5': -57.1350449830154
    '6': 285.6673892610479
    '7': 21.7304739764342
    '8': -42.316539648164664
  sampler_perf:
    mean_action_processing_ms: 0.20053658232882887
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 38.631592673779345
    mean_inference_ms: 5.970127219202353
    mean_raw_obs_processing_ms: 0.6861114165305631
  time_since_restore: 1923.6557443141937
  time_this_iter_s: 141.00189805030823
  time_total_s: 1923.6557443141937
  timers:
    learn_throughput: 139.289
    learn_time_ms: 28717.268
    load_throughput: 277769.856
    load_time_ms: 14.4
    sample_throughput: 38.846
    sample_time_ms: 102971.87
    update_time_ms: 14.463
  timestamp: 1651206569
  timesteps_since_restore: 0
  timesteps_total: 64000
  training_iteration: 16
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     16 |          1923.66 | 64000 |  998.813 |              1250.85 |              790.818 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 544000
  custom_metrics:
    eps_sum_utility_max: 1173.5618460857916
    eps_sum_utility_mean: 969.9604356851828
    eps_sum_utility_min: 690.8300619288029
    sum_utility_max: 28.30426714008479
    sum_utility_mean: 20.245767857854393
    sum_utility_min: -7.6732227231123185
  date: 2022-04-29_10-01-50
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1218.6716530102767
  episode_reward_mean: 1017.4353466532124
  episode_reward_min: 840.2568613264219
  episodes_this_iter: 40
  episodes_total: 680
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.825783610343933
          entropy_coeff: 0.0
          kl: 0.00832377839833498
          model: {}
          policy_loss: -0.0069329384714365005
          total_loss: 4119.46728515625
          vf_explained_var: -4.7491442956015817e-07
          vf_loss: 4119.47216796875
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6246100664138794
          entropy_coeff: 0.0
          kl: 0.009344320744276047
          model: {}
          policy_loss: -0.018205979838967323
          total_loss: 220.46493530273438
          vf_explained_var: 0.5254431366920471
          vf_loss: 220.48031616210938
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7023571729660034
          entropy_coeff: 0.0
          kl: 0.009575864300131798
          model: {}
          policy_loss: -0.015484819188714027
          total_loss: 128.4766387939453
          vf_explained_var: 0.6784015893936157
          vf_loss: 128.4892578125
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6318894624710083
          entropy_coeff: 0.0
          kl: 0.0070877098478376865
          model: {}
          policy_loss: -0.010318033397197723
          total_loss: 41.30907440185547
          vf_explained_var: 0.8773866891860962
          vf_loss: 41.316200256347656
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7703734636306763
          entropy_coeff: 0.0
          kl: 0.007715869694948196
          model: {}
          policy_loss: -0.01312980055809021
          total_loss: 154.8343505859375
          vf_explained_var: 0.5440272092819214
          vf_loss: 154.84397888183594
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6474953889846802
          entropy_coeff: 0.0
          kl: 0.006245181430131197
          model: {}
          policy_loss: -0.011106564663350582
          total_loss: 3545.07470703125
          vf_explained_var: 1.4151296454656404e-06
          vf_loss: 3545.083740234375
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5446795225143433
          entropy_coeff: 0.0
          kl: 0.01116930041462183
          model: {}
          policy_loss: -0.016924753785133362
          total_loss: 111.347900390625
          vf_explained_var: 0.8057615160942078
          vf_loss: 111.3614730834961
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6321438550949097
          entropy_coeff: 0.0
          kl: 0.007518695667386055
          model: {}
          policy_loss: -0.017778875306248665
          total_loss: 191.67999267578125
          vf_explained_var: 0.5601242780685425
          vf_loss: 191.69435119628906
    num_agent_steps_sampled: 544000
    num_agent_steps_trained: 544000
    num_steps_sampled: 68000
    num_steps_trained: 68000
  iterations_since_restore: 17
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.150261780104714
    ram_util_percent: 56.84502617801047
  pid: 3846
  policy_reward_max:
    '1': 378.5233040680125
    '2': 37.38508538324102
    '3': 117.33426780764302
    '4': 198.6379685003428
    '5': 47.869402669845314
    '6': 345.5992690342254
    '7': 173.3967621915884
    '8': 91.54633922818802
  policy_reward_mean:
    '1': 364.9802271269793
    '2': -21.223053263213306
    '3': 54.35010362309926
    '4': 177.64170324512855
    '5': -8.592942289263156
    '6': 328.93985794999475
    '7': 102.4416717702754
    '8': 18.897778490211646
  policy_reward_min:
    '1': 317.03723671214885
    '2': -78.6984775240402
    '3': 8.523756500589597
    '4': 149.0068480313524
    '5': -53.67047569436478
    '6': 237.2496962106876
    '7': 38.04831383795492
    '8': -42.316539648164664
  sampler_perf:
    mean_action_processing_ms: 0.20236091471257242
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 39.17594778526434
    mean_inference_ms: 6.018702239144563
    mean_raw_obs_processing_ms: 0.6921681983556417
  time_since_restore: 2064.7903084754944
  time_this_iter_s: 141.13456416130066
  time_total_s: 2064.7903084754944
  timers:
    learn_throughput: 137.737
    learn_time_ms: 29040.896
    load_throughput: 270650.896
    load_time_ms: 14.779
    sample_throughput: 38.066
    sample_time_ms: 105080.425
    update_time_ms: 14.655
  timestamp: 1651206710
  timesteps_since_restore: 0
  timesteps_total: 68000
  training_iteration: 17
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     17 |          2064.79 | 68000 |  1017.44 |              1218.67 |              840.257 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 576000
  custom_metrics:
    eps_sum_utility_max: 1173.5618460857916
    eps_sum_utility_mean: 995.276030303251
    eps_sum_utility_min: 710.5905279328541
    sum_utility_max: 28.30426714008479
    sum_utility_mean: 21.42699362362514
    sum_utility_min: 5.43659911021559
  date: 2022-04-29_10-04-13
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1259.177663464084
  episode_reward_mean: 1035.8425202239862
  episode_reward_min: 861.7236984842286
  episodes_this_iter: 40
  episodes_total: 720
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.834733247756958
          entropy_coeff: 0.0
          kl: 0.01070348359644413
          model: {}
          policy_loss: -0.01228940486907959
          total_loss: 3736.37158203125
          vf_explained_var: -2.730277230966749e-07
          vf_loss: 3736.380859375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6249747276306152
          entropy_coeff: 0.0
          kl: 0.010776082053780556
          model: {}
          policy_loss: -0.017299063503742218
          total_loss: 256.5055236816406
          vf_explained_var: 0.48880207538604736
          vf_loss: 256.51959228515625
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.684744119644165
          entropy_coeff: 0.0
          kl: 0.009623855352401733
          model: {}
          policy_loss: -0.012881917878985405
          total_loss: 157.57781982421875
          vf_explained_var: 0.6371906995773315
          vf_loss: 157.58779907226562
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6333812475204468
          entropy_coeff: 0.0
          kl: 0.006704732310026884
          model: {}
          policy_loss: -0.01569335162639618
          total_loss: 38.573612213134766
          vf_explained_var: 0.890927255153656
          vf_loss: 38.5862922668457
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.767396092414856
          entropy_coeff: 0.0
          kl: 0.007825651206076145
          model: {}
          policy_loss: -0.013638937845826149
          total_loss: 172.76376342773438
          vf_explained_var: 0.5112974643707275
          vf_loss: 172.7738800048828
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6538499593734741
          entropy_coeff: 0.0
          kl: 0.00869826227426529
          model: {}
          policy_loss: -0.013545705005526543
          total_loss: 3450.008544921875
          vf_explained_var: 2.40918125200551e-05
          vf_loss: 3450.019775390625
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5194123983383179
          entropy_coeff: 0.0
          kl: 0.009885454550385475
          model: {}
          policy_loss: -0.01656736619770527
          total_loss: 115.27842712402344
          vf_explained_var: 0.8193761110305786
          vf_loss: 115.29205322265625
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6511541604995728
          entropy_coeff: 0.0
          kl: 0.009854947216808796
          model: {}
          policy_loss: -0.01659313030540943
          total_loss: 219.39295959472656
          vf_explained_var: 0.5394864082336426
          vf_loss: 219.40513610839844
    num_agent_steps_sampled: 576000
    num_agent_steps_trained: 576000
    num_steps_sampled: 72000
    num_steps_trained: 72000
  iterations_since_restore: 18
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.18541666666667
    ram_util_percent: 56.869791666666664
  pid: 3846
  policy_reward_max:
    '1': 380.6630728955488
    '2': 64.83121507216671
    '3': 117.33426780764302
    '4': 203.90112332279293
    '5': 40.051023700022995
    '6': 350.43521943698846
    '7': 173.3967621915884
    '8': 77.46024683794094
  policy_reward_mean:
    '1': 365.0647687496977
    '2': -14.903360834890934
    '3': 57.894075030159584
    '4': 178.93734962400174
    '5': -3.611302563710171
    '6': 329.15392526905066
    '7': 102.56110906295974
    '8': 20.7459558867179
  policy_reward_min:
    '1': 339.04888137060914
    '2': -77.63105131534529
    '3': 5.681182743644561
    '4': 149.0068480313524
    '5': -53.67047569436478
    '6': 237.2496962106876
    '7': 47.851051145269295
    '8': -71.59013457081812
  sampler_perf:
    mean_action_processing_ms: 0.20405056109750253
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 39.67200286631778
    mean_inference_ms: 6.0639990733660944
    mean_raw_obs_processing_ms: 0.6979475764786539
  time_since_restore: 2207.1854877471924
  time_this_iter_s: 142.395179271698
  time_total_s: 2207.1854877471924
  timers:
    learn_throughput: 136.268
    learn_time_ms: 29353.851
    load_throughput: 265764.207
    load_time_ms: 15.051
    sample_throughput: 37.449
    sample_time_ms: 106810.67
    update_time_ms: 14.734
  timestamp: 1651206853
  timesteps_since_restore: 0
  timesteps_total: 72000
  training_iteration: 18
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     18 |          2207.19 | 72000 |  1035.84 |              1259.18 |              861.724 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 608000
  custom_metrics:
    eps_sum_utility_max: 1192.9855099606896
    eps_sum_utility_mean: 1007.5297913371933
    eps_sum_utility_min: 785.217181214921
    sum_utility_max: 27.950763276368882
    sum_utility_mean: 21.63882802736615
    sum_utility_min: 5.43659911021559
  date: 2022-04-29_10-06-34
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1265.4964490027182
  episode_reward_mean: 1056.1134658137353
  episode_reward_min: 860.3535085420191
  episodes_this_iter: 40
  episodes_total: 760
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8185213804244995
          entropy_coeff: 0.0
          kl: 0.011404495686292648
          model: {}
          policy_loss: -0.018143750727176666
          total_loss: 3533.390869140625
          vf_explained_var: -2.0765489239238377e-07
          vf_loss: 3533.40576171875
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6127698421478271
          entropy_coeff: 0.0
          kl: 0.010785293765366077
          model: {}
          policy_loss: -0.017068376764655113
          total_loss: 181.02761840820312
          vf_explained_var: 0.534473180770874
          vf_loss: 181.04139709472656
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6522536277770996
          entropy_coeff: 0.0
          kl: 0.012724324129521847
          model: {}
          policy_loss: -0.018134184181690216
          total_loss: 145.9922637939453
          vf_explained_var: 0.656301736831665
          vf_loss: 146.00656127929688
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6288208961486816
          entropy_coeff: 0.0
          kl: 0.009751150384545326
          model: {}
          policy_loss: -0.01577201671898365
          total_loss: 53.55527877807617
          vf_explained_var: 0.8562477827072144
          vf_loss: 53.566654205322266
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7410980463027954
          entropy_coeff: 0.0
          kl: 0.009450642392039299
          model: {}
          policy_loss: -0.01445739809423685
          total_loss: 131.2478790283203
          vf_explained_var: 0.5373859405517578
          vf_loss: 131.25807189941406
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6108975410461426
          entropy_coeff: 0.0
          kl: 0.010166008956730366
          model: {}
          policy_loss: -0.013328474946320057
          total_loss: 2719.3701171875
          vf_explained_var: 0.37909233570098877
          vf_loss: 2719.380126953125
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4641920328140259
          entropy_coeff: 0.0
          kl: 0.014092467725276947
          model: {}
          policy_loss: -0.017553118988871574
          total_loss: 105.20542907714844
          vf_explained_var: 0.8098415732383728
          vf_loss: 105.2187728881836
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6119749546051025
          entropy_coeff: 0.0
          kl: 0.011057364754378796
          model: {}
          policy_loss: -0.018915768712759018
          total_loss: 172.4453125
          vf_explained_var: 0.5643659830093384
          vf_loss: 172.4593048095703
    num_agent_steps_sampled: 608000
    num_agent_steps_trained: 608000
    num_steps_sampled: 76000
    num_steps_trained: 76000
  iterations_since_restore: 19
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.26596858638743
    ram_util_percent: 56.851832460732986
  pid: 3846
  policy_reward_max:
    '1': 384.02291892985085
    '2': 64.83121507216671
    '3': 115.38538730902846
    '4': 203.90112332279293
    '5': 45.71258072745652
    '6': 351.4586200632637
    '7': 157.94674309814403
    '8': 90.51740513597466
  policy_reward_mean:
    '1': 365.50537712323546
    '2': -9.916688398390143
    '3': 60.69486727615248
    '4': 179.6466774562064
    '5': 2.843457366347137
    '6': 329.9795083225105
    '7': 102.76180755923173
    '8': 24.598459108441894
  policy_reward_min:
    '1': 334.3132535374889
    '2': -67.93072176606626
    '3': 5.681182743644561
    '4': 139.61914424560075
    '5': -53.67047569436478
    '6': 278.5460129504958
    '7': 47.851051145269295
    '8': -71.59013457081812
  sampler_perf:
    mean_action_processing_ms: 0.20557102876668343
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 40.11336134402636
    mean_inference_ms: 6.1046776622322065
    mean_raw_obs_processing_ms: 0.7032422880457432
  time_since_restore: 2348.700206041336
  time_this_iter_s: 141.51471829414368
  time_total_s: 2348.700206041336
  timers:
    learn_throughput: 134.951
    learn_time_ms: 29640.463
    load_throughput: 265167.322
    load_time_ms: 15.085
    sample_throughput: 36.965
    sample_time_ms: 108209.137
    update_time_ms: 14.602
  timestamp: 1651206994
  timesteps_since_restore: 0
  timesteps_total: 76000
  training_iteration: 19
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     19 |           2348.7 | 76000 |  1056.11 |               1265.5 |              860.354 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 640000
  custom_metrics:
    eps_sum_utility_max: 1230.7697776072819
    eps_sum_utility_mean: 1035.51823451439
    eps_sum_utility_min: 785.217181214921
    sum_utility_max: 27.950763276368882
    sum_utility_mean: 21.688949208499288
    sum_utility_min: 5.43659911021559
  date: 2022-04-29_10-08-57
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1349.7317215649077
  episode_reward_mean: 1094.134725313398
  episode_reward_min: 860.3535085420191
  episodes_this_iter: 40
  episodes_total: 800
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8153663873672485
          entropy_coeff: 0.0
          kl: 0.01117506343871355
          model: {}
          policy_loss: -0.016088075935840607
          total_loss: 3426.2900390625
          vf_explained_var: -1.5381843354589364e-07
          vf_loss: 3426.302978515625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6067606210708618
          entropy_coeff: 0.0
          kl: 0.0067483773455023766
          model: {}
          policy_loss: -0.008953611366450787
          total_loss: 275.6397705078125
          vf_explained_var: 0.45076534152030945
          vf_loss: 275.64666748046875
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6564533710479736
          entropy_coeff: 0.0
          kl: 0.009451023302972317
          model: {}
          policy_loss: -0.019366120919585228
          total_loss: 151.22264099121094
          vf_explained_var: 0.6795111894607544
          vf_loss: 151.2391815185547
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.603376865386963
          entropy_coeff: 0.0
          kl: 0.010439892299473286
          model: {}
          policy_loss: -0.01623987965285778
          total_loss: 43.70140075683594
          vf_explained_var: 0.8818459510803223
          vf_loss: 43.71294403076172
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7041205167770386
          entropy_coeff: 0.0
          kl: 0.010288495570421219
          model: {}
          policy_loss: -0.015617034398019314
          total_loss: 127.63909912109375
          vf_explained_var: 0.5589816570281982
          vf_loss: 127.65008544921875
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.593052625656128
          entropy_coeff: 0.0
          kl: 0.009836954064667225
          model: {}
          policy_loss: -0.013279815204441547
          total_loss: 1640.4090576171875
          vf_explained_var: 0.5573475956916809
          vf_loss: 1640.419677734375
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4477715492248535
          entropy_coeff: 0.0
          kl: 0.012738354504108429
          model: {}
          policy_loss: -0.015517032705247402
          total_loss: 98.36715698242188
          vf_explained_var: 0.837291955947876
          vf_loss: 98.37884521484375
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5843262672424316
          entropy_coeff: 0.0
          kl: 0.007719571236521006
          model: {}
          policy_loss: -0.010487227700650692
          total_loss: 207.98915100097656
          vf_explained_var: 0.5889180898666382
          vf_loss: 207.9961700439453
    num_agent_steps_sampled: 640000
    num_agent_steps_trained: 640000
    num_steps_sampled: 80000
    num_steps_trained: 80000
  iterations_since_restore: 20
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.229166666666664
    ram_util_percent: 56.85416666666668
  pid: 3846
  policy_reward_max:
    '1': 384.02291892985085
    '2': 75.51890851067778
    '3': 115.38538730902846
    '4': 206.9010673571157
    '5': 60.86243606445372
    '6': 351.4586200632637
    '7': 161.05626101594493
    '8': 96.98963784194927
  policy_reward_mean:
    '1': 367.1298716425369
    '2': 0.2849250362524738
    '3': 63.73482181926854
    '4': 180.93880735568192
    '5': 12.870345010291741
    '6': 329.27595533025806
    '7': 106.29853745407776
    '8': 33.60146166503039
  policy_reward_min:
    '1': 334.3132535374889
    '2': -67.93072176606626
    '3': 10.151080814960043
    '4': 139.61914424560075
    '5': -50.97821567028012
    '6': 270.40776317798293
    '7': 47.851051145269295
    '8': -71.59013457081812
  sampler_perf:
    mean_action_processing_ms: 0.20698202454649667
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 40.50985324804533
    mean_inference_ms: 6.141969730725204
    mean_raw_obs_processing_ms: 0.7081146350920656
  time_since_restore: 2491.1849048137665
  time_this_iter_s: 142.48469877243042
  time_total_s: 2491.1849048137665
  timers:
    learn_throughput: 133.798
    learn_time_ms: 29895.717
    load_throughput: 259635.274
    load_time_ms: 15.406
    sample_throughput: 36.629
    sample_time_ms: 109203.436
    update_time_ms: 14.603
  timestamp: 1651207137
  timesteps_since_restore: 0
  timesteps_total: 80000
  training_iteration: 20
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     20 |          2491.18 | 80000 |  1094.13 |              1349.73 |              860.354 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 672000
  custom_metrics:
    eps_sum_utility_max: 1230.7697776072819
    eps_sum_utility_mean: 1064.9979755284244
    eps_sum_utility_min: 800.0726080718857
    sum_utility_max: 27.872996295262205
    sum_utility_mean: 21.608641587489156
    sum_utility_min: -9.602074573648679
  date: 2022-04-29_10-11-19
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1357.1836314598404
  episode_reward_mean: 1122.71441370658
  episode_reward_min: 860.3535085420191
  episodes_this_iter: 40
  episodes_total: 840
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8103364706039429
          entropy_coeff: 0.0
          kl: 0.007219014689326286
          model: {}
          policy_loss: -0.010130678303539753
          total_loss: 3377.888916015625
          vf_explained_var: -9.229106012753618e-08
          vf_loss: 3377.896728515625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6073499917984009
          entropy_coeff: 0.0
          kl: 0.0162508487701416
          model: {}
          policy_loss: -0.018102843314409256
          total_loss: 251.6710662841797
          vf_explained_var: 0.47548049688339233
          vf_loss: 251.68429565429688
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6418941020965576
          entropy_coeff: 0.0
          kl: 0.01046080607920885
          model: {}
          policy_loss: -0.014135983772575855
          total_loss: 125.16505432128906
          vf_explained_var: 0.7385365962982178
          vf_loss: 125.17604064941406
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5826936960220337
          entropy_coeff: 0.0
          kl: 0.009504000656306744
          model: {}
          policy_loss: -0.020210158079862595
          total_loss: 34.56224822998047
          vf_explained_var: 0.9094083309173584
          vf_loss: 34.57817840576172
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6948884725570679
          entropy_coeff: 0.0
          kl: 0.008550669997930527
          model: {}
          policy_loss: -0.014723257161676884
          total_loss: 134.14120483398438
          vf_explained_var: 0.5613184571266174
          vf_loss: 134.15206909179688
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5858999490737915
          entropy_coeff: 0.0
          kl: 0.014400630258023739
          model: {}
          policy_loss: -0.01956934854388237
          total_loss: 1140.1053466796875
          vf_explained_var: 0.6721848249435425
          vf_loss: 1140.1204833984375
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4206465482711792
          entropy_coeff: 0.0
          kl: 0.012782180681824684
          model: {}
          policy_loss: -0.017138049006462097
          total_loss: 114.47576904296875
          vf_explained_var: 0.832815945148468
          vf_loss: 114.48905181884766
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5610582828521729
          entropy_coeff: 0.0
          kl: 0.009859380312263966
          model: {}
          policy_loss: -0.016105560585856438
          total_loss: 133.5866241455078
          vf_explained_var: 0.6973736882209778
          vf_loss: 133.59829711914062
    num_agent_steps_sampled: 672000
    num_agent_steps_trained: 672000
    num_steps_sampled: 84000
    num_steps_trained: 84000
  iterations_since_restore: 21
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.309424083769635
    ram_util_percent: 56.80157068062828
  pid: 3846
  policy_reward_max:
    '1': 384.02291892985085
    '2': 75.51890851067778
    '3': 115.41920646355427
    '4': 212.46665309296483
    '5': 62.311009606169925
    '6': 347.71839526479454
    '7': 161.05626101594493
    '8': 97.54842754551603
  policy_reward_mean:
    '1': 367.79153935008463
    '2': 8.212617837788645
    '3': 67.63156414499764
    '4': 182.28508869387122
    '5': 19.526147129694348
    '6': 329.6170486175943
    '7': 107.0931811247036
    '8': 40.55722680784544
  policy_reward_min:
    '1': 349.11192242675725
    '2': -54.81484056385158
    '3': 15.663548706893621
    '4': 139.61914424560075
    '5': -36.90997127611451
    '6': 270.40776317798293
    '7': 53.67088538335157
    '8': -26.28640707126332
  sampler_perf:
    mean_action_processing_ms: 0.2082524052310587
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 40.86735224738713
    mean_inference_ms: 6.175798494377363
    mean_raw_obs_processing_ms: 0.7124413932315534
  time_since_restore: 2632.6612923145294
  time_this_iter_s: 141.47638750076294
  time_total_s: 2632.6612923145294
  timers:
    learn_throughput: 133.179
    learn_time_ms: 30034.747
    load_throughput: 264619.015
    load_time_ms: 15.116
    sample_throughput: 36.43
    sample_time_ms: 109800.568
    update_time_ms: 14.679
  timestamp: 1651207279
  timesteps_since_restore: 0
  timesteps_total: 84000
  training_iteration: 21
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     21 |          2632.66 | 84000 |  1122.71 |              1357.18 |              860.354 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 704000
  custom_metrics:
    eps_sum_utility_max: 1234.2057102225542
    eps_sum_utility_mean: 1095.6818526633879
    eps_sum_utility_min: 905.9826279043774
    sum_utility_max: 28.30034232162957
    sum_utility_mean: 21.925102400254087
    sum_utility_min: -9.602074573648679
  date: 2022-04-29_10-13-42
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1433.390966354154
  episode_reward_mean: 1167.99059683054
  episode_reward_min: 929.7034081635917
  episodes_this_iter: 40
  episodes_total: 880
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8028537034988403
          entropy_coeff: 0.0
          kl: 0.011780111119151115
          model: {}
          policy_loss: -0.014923784881830215
          total_loss: 3390.371337890625
          vf_explained_var: -6.729556645268531e-08
          vf_loss: 3390.3818359375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.587158441543579
          entropy_coeff: 0.0
          kl: 0.011631747707724571
          model: {}
          policy_loss: -0.018834609538316727
          total_loss: 271.3521728515625
          vf_explained_var: 0.4876585006713867
          vf_loss: 271.3674621582031
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.592740774154663
          entropy_coeff: 0.0
          kl: 0.008802059106528759
          model: {}
          policy_loss: -0.017221415415406227
          total_loss: 149.28863525390625
          vf_explained_var: 0.7265695333480835
          vf_loss: 149.30320739746094
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5967332124710083
          entropy_coeff: 0.0
          kl: 0.006608680821955204
          model: {}
          policy_loss: -0.012572187930345535
          total_loss: 42.65428161621094
          vf_explained_var: 0.8941342234611511
          vf_loss: 42.66389083862305
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6640808582305908
          entropy_coeff: 0.0
          kl: 0.00840725377202034
          model: {}
          policy_loss: -0.013435298576951027
          total_loss: 85.57035064697266
          vf_explained_var: 0.7036398649215698
          vf_loss: 85.58000183105469
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5968546867370605
          entropy_coeff: 0.0
          kl: 0.012785783037543297
          model: {}
          policy_loss: -0.016819573938846588
          total_loss: 949.44482421875
          vf_explained_var: 0.7143173813819885
          vf_loss: 949.457763671875
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3957549333572388
          entropy_coeff: 0.0
          kl: 0.010465500876307487
          model: {}
          policy_loss: -0.0209816787391901
          total_loss: 149.31210327148438
          vf_explained_var: 0.8007793426513672
          vf_loss: 149.32994079589844
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5358710289001465
          entropy_coeff: 0.0
          kl: 0.009191789664328098
          model: {}
          policy_loss: -0.016916275024414062
          total_loss: 256.36822509765625
          vf_explained_var: 0.6128900647163391
          vf_loss: 256.3810119628906
    num_agent_steps_sampled: 704000
    num_agent_steps_trained: 704000
    num_steps_sampled: 88000
    num_steps_trained: 88000
  iterations_since_restore: 22
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.40621761658031
    ram_util_percent: 56.83937823834197
  pid: 3846
  policy_reward_max:
    '1': 379.94032768080643
    '2': 118.1062431709854
    '3': 123.10845636090602
    '4': 219.8801245247043
    '5': 66.45490201632063
    '6': 350.5570905101582
    '7': 229.38394949777768
    '8': 126.83991505574538
  policy_reward_mean:
    '1': 368.20593275058303
    '2': 19.217304702874106
    '3': 72.21743030253306
    '4': 186.21224896862034
    '5': 27.613199854796306
    '6': 332.01078170691216
    '7': 110.78368038354174
    '8': 51.73001816067953
  policy_reward_min:
    '1': 349.11192242675725
    '2': -54.81484056385158
    '3': 19.152953872897548
    '4': 167.13324186033498
    '5': -35.869447296483465
    '6': 277.05312559540045
    '7': 53.67088538335157
    '8': -20.811667483017175
  sampler_perf:
    mean_action_processing_ms: 0.2093933688604851
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 41.18128889814797
    mean_inference_ms: 6.206173971445359
    mean_raw_obs_processing_ms: 0.7162442221125369
  time_since_restore: 2775.485316991806
  time_this_iter_s: 142.8240246772766
  time_total_s: 2775.485316991806
  timers:
    learn_throughput: 132.228
    learn_time_ms: 30250.744
    load_throughput: 265823.159
    load_time_ms: 15.048
    sample_throughput: 36.357
    sample_time_ms: 110021.414
    update_time_ms: 12.89
  timestamp: 1651207422
  timesteps_since_restore: 0
  timesteps_total: 88000
  training_iteration: 22
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     22 |          2775.49 | 88000 |  1167.99 |              1433.39 |              929.703 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 736000
  custom_metrics:
    eps_sum_utility_max: 1234.2057102225542
    eps_sum_utility_mean: 1110.900928670674
    eps_sum_utility_min: 942.3792557446275
    sum_utility_max: 28.30034232162957
    sum_utility_mean: 22.46262491343149
    sum_utility_min: 12.923625139216815
  date: 2022-04-29_10-16-03
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1433.390966354154
  episode_reward_mean: 1210.8538572728346
  episode_reward_min: 945.8916094029496
  episodes_this_iter: 40
  episodes_total: 920
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8017760515213013
          entropy_coeff: 0.0
          kl: 0.008603276684880257
          model: {}
          policy_loss: -0.013319021090865135
          total_loss: 3374.374755859375
          vf_explained_var: -6.152737341835746e-08
          vf_loss: 3374.38525390625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5644409656524658
          entropy_coeff: 0.0
          kl: 0.009862683713436127
          model: {}
          policy_loss: -0.013126389123499393
          total_loss: 322.02203369140625
          vf_explained_var: 0.5103009939193726
          vf_loss: 322.0321960449219
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.587123990058899
          entropy_coeff: 0.0
          kl: 0.009598893113434315
          model: {}
          policy_loss: -0.014070081524550915
          total_loss: 163.41909790039062
          vf_explained_var: 0.7366966009140015
          vf_loss: 163.4302978515625
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5765348672866821
          entropy_coeff: 0.0
          kl: 0.006489736959338188
          model: {}
          policy_loss: -0.011829433962702751
          total_loss: 36.20058822631836
          vf_explained_var: 0.9131352305412292
          vf_loss: 36.20949172973633
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.656244158744812
          entropy_coeff: 0.0
          kl: 0.009193995967507362
          model: {}
          policy_loss: -0.023563427850604057
          total_loss: 143.49574279785156
          vf_explained_var: 0.5397381782531738
          vf_loss: 143.51519775390625
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6179603338241577
          entropy_coeff: 0.0
          kl: 0.02301277592778206
          model: {}
          policy_loss: -0.021109191700816154
          total_loss: 892.4760131835938
          vf_explained_var: 0.7417681813240051
          vf_loss: 892.4901733398438
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.383958339691162
          entropy_coeff: 0.0
          kl: 0.010714861564338207
          model: {}
          policy_loss: -0.018872549757361412
          total_loss: 74.77761840820312
          vf_explained_var: 0.8871925473213196
          vf_loss: 74.79327392578125
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5249009132385254
          entropy_coeff: 0.0
          kl: 0.0083546731621027
          model: {}
          policy_loss: -0.015151020139455795
          total_loss: 201.32534790039062
          vf_explained_var: 0.7191563248634338
          vf_loss: 201.33673095703125
    num_agent_steps_sampled: 736000
    num_agent_steps_trained: 736000
    num_steps_sampled: 92000
    num_steps_trained: 92000
  iterations_since_restore: 23
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.2
    ram_util_percent: 56.83052631578948
  pid: 3846
  policy_reward_max:
    '1': 383.07268150275905
    '2': 118.1062431709854
    '3': 143.70835827601007
    '4': 219.8801245247043
    '5': 69.05281422435382
    '6': 355.69837449333875
    '7': 229.38394949777768
    '8': 126.83991505574538
  policy_reward_mean:
    '1': 366.4685969159629
    '2': 34.15935270364291
    '3': 80.23469923928195
    '4': 187.4132854262308
    '5': 32.43977024124236
    '6': 334.7106850053207
    '7': 114.22466228492651
    '8': 61.202805456226216
  policy_reward_min:
    '1': 332.90881168087793
    '2': -42.01033903794679
    '3': 19.152953872897548
    '4': 156.65086112702593
    '5': -35.20382136339056
    '6': 271.1994291350995
    '7': 58.049982536751514
    '8': -20.811667483017175
  sampler_perf:
    mean_action_processing_ms: 0.21041610484722814
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 41.454689104970285
    mean_inference_ms: 6.233741188286404
    mean_raw_obs_processing_ms: 0.719670219940873
  time_since_restore: 2916.535213947296
  time_this_iter_s: 141.0498969554901
  time_total_s: 2916.535213947296
  timers:
    learn_throughput: 131.935
    learn_time_ms: 30318.029
    load_throughput: 262550.954
    load_time_ms: 15.235
    sample_throughput: 36.017
    sample_time_ms: 111057.507
    update_time_ms: 12.996
  timestamp: 1651207563
  timesteps_since_restore: 0
  timesteps_total: 92000
  training_iteration: 23
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     23 |          2916.54 | 92000 |  1210.85 |              1433.39 |              945.892 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 768000
  custom_metrics:
    eps_sum_utility_max: 1234.2057102225542
    eps_sum_utility_mean: 1124.1666402934297
    eps_sum_utility_min: 828.0929429588386
    sum_utility_max: 28.002493750763904
    sum_utility_mean: 22.1559985588407
    sum_utility_min: 14.978665151750644
  date: 2022-04-29_10-18-26
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1433.390966354154
  episode_reward_mean: 1239.582931863356
  episode_reward_min: 982.3186613791953
  episodes_this_iter: 40
  episodes_total: 960
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7999564409255981
          entropy_coeff: 0.0
          kl: 0.012842727825045586
          model: {}
          policy_loss: -0.015988154336810112
          total_loss: 3401.416015625
          vf_explained_var: -2.1150034612560376e-08
          vf_loss: 3401.42822265625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5306462049484253
          entropy_coeff: 0.0
          kl: 0.012592392042279243
          model: {}
          policy_loss: -0.01329596247524023
          total_loss: 209.3717803955078
          vf_explained_var: 0.5691311955451965
          vf_loss: 209.38133239746094
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5847804546356201
          entropy_coeff: 0.0
          kl: 0.00984440091997385
          model: {}
          policy_loss: -0.013682834804058075
          total_loss: 130.74844360351562
          vf_explained_var: 0.7501295804977417
          vf_loss: 130.75917053222656
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5655783414840698
          entropy_coeff: 0.0
          kl: 0.009529750794172287
          model: {}
          policy_loss: -0.01564549282193184
          total_loss: 40.769752502441406
          vf_explained_var: 0.8940060138702393
          vf_loss: 40.7811164855957
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6545960903167725
          entropy_coeff: 0.0
          kl: 0.006619494874030352
          model: {}
          policy_loss: -0.010336507111787796
          total_loss: 65.36414337158203
          vf_explained_var: 0.7769078016281128
          vf_loss: 65.37149810791016
      '6':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5955320596694946
          entropy_coeff: 0.0
          kl: 0.008893946185708046
          model: {}
          policy_loss: -0.01905037648975849
          total_loss: 667.0661010742188
          vf_explained_var: 0.8126387596130371
          vf_loss: 667.0809936523438
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3548388481140137
          entropy_coeff: 0.0
          kl: 0.009918984025716782
          model: {}
          policy_loss: -0.011971321888267994
          total_loss: 77.41939544677734
          vf_explained_var: 0.8799863457679749
          vf_loss: 77.42839050292969
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.503280758857727
          entropy_coeff: 0.0
          kl: 0.011064831167459488
          model: {}
          policy_loss: -0.021564504131674767
          total_loss: 124.02261352539062
          vf_explained_var: 0.7705672979354858
          vf_loss: 124.03919982910156
    num_agent_steps_sampled: 768000
    num_agent_steps_trained: 768000
    num_steps_sampled: 96000
    num_steps_trained: 96000
  iterations_since_restore: 24
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.62849740932642
    ram_util_percent: 56.827979274611394
  pid: 3846
  policy_reward_max:
    '1': 389.14210029759187
    '2': 118.1062431709854
    '3': 156.73915228647456
    '4': 219.8801245247043
    '5': 84.12446474783098
    '6': 355.69837449333875
    '7': 159.0142469636519
    '8': 122.27268934141523
  policy_reward_mean:
    '1': 365.7280189517018
    '2': 45.236940204315076
    '3': 86.67999122541877
    '4': 186.39307885212938
    '5': 39.03386144210501
    '6': 334.0501519032158
    '7': 117.3694644557631
    '8': 65.09142482870722
  policy_reward_min:
    '1': 324.8074761514395
    '2': -42.01033903794679
    '3': 40.550844198224496
    '4': 156.65086112702593
    '5': -35.20382136339056
    '6': 167.95119314840684
    '7': 62.2477444455709
    '8': 6.042688976986432
  sampler_perf:
    mean_action_processing_ms: 0.21135867626553534
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 41.70353344596196
    mean_inference_ms: 6.26003906956129
    mean_raw_obs_processing_ms: 0.7229048849155281
  time_since_restore: 3059.6887850761414
  time_this_iter_s: 143.15357112884521
  time_total_s: 3059.6887850761414
  timers:
    learn_throughput: 130.896
    learn_time_ms: 30558.682
    load_throughput: 267251.425
    load_time_ms: 14.967
    sample_throughput: 36.001
    sample_time_ms: 111109.508
    update_time_ms: 12.878
  timestamp: 1651207706
  timesteps_since_restore: 0
  timesteps_total: 96000
  training_iteration: 24
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     24 |          3059.69 | 96000 |  1239.58 |              1433.39 |              982.319 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 800000
  custom_metrics:
    eps_sum_utility_max: 1256.787661084886
    eps_sum_utility_mean: 1134.725707725722
    eps_sum_utility_min: 828.0929429588386
    sum_utility_max: 28.07662141167756
    sum_utility_mean: 22.12339387793513
    sum_utility_min: 8.896167585159013
  date: 2022-04-29_10-20-49
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1398.8229482506924
  episode_reward_mean: 1250.013920227066
  episode_reward_min: 1045.740913577321
  episodes_this_iter: 40
  episodes_total: 1000
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7927577495574951
          entropy_coeff: 0.0
          kl: 0.019984614104032516
          model: {}
          policy_loss: -0.026917820796370506
          total_loss: 3362.432861328125
          vf_explained_var: -2.8840956289855058e-08
          vf_loss: 3362.4541015625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5307608842849731
          entropy_coeff: 0.0
          kl: 0.0097952326759696
          model: {}
          policy_loss: -0.01642637513577938
          total_loss: 269.85052490234375
          vf_explained_var: 0.5536733269691467
          vf_loss: 269.8639831542969
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.565921664237976
          entropy_coeff: 0.0
          kl: 0.008897893130779266
          model: {}
          policy_loss: -0.014428304508328438
          total_loss: 101.47640991210938
          vf_explained_var: 0.7954193353652954
          vf_loss: 101.48817443847656
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5395557880401611
          entropy_coeff: 0.0
          kl: 0.010804090648889542
          model: {}
          policy_loss: -0.01968180388212204
          total_loss: 31.836788177490234
          vf_explained_var: 0.9254134297370911
          vf_loss: 31.851608276367188
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6416412591934204
          entropy_coeff: 0.0
          kl: 0.009068799205124378
          model: {}
          policy_loss: -0.016030872240662575
          total_loss: 69.07198333740234
          vf_explained_var: 0.7748387455940247
          vf_loss: 69.08393096923828
      '6':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6086854934692383
          entropy_coeff: 0.0
          kl: 0.004512472543865442
          model: {}
          policy_loss: -0.009822552092373371
          total_loss: 327.26171875
          vf_explained_var: 0.9079334139823914
          vf_loss: 327.26947021484375
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.315253734588623
          entropy_coeff: 0.0
          kl: 0.009585392661392689
          model: {}
          policy_loss: -0.01684679090976715
          total_loss: 105.080810546875
          vf_explained_var: 0.8464343547821045
          vf_loss: 105.09476470947266
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.478587031364441
          entropy_coeff: 0.0
          kl: 0.009553255513310432
          model: {}
          policy_loss: -0.02010226808488369
          total_loss: 152.6809844970703
          vf_explained_var: 0.7711991667747498
          vf_loss: 152.69676208496094
    num_agent_steps_sampled: 800000
    num_agent_steps_trained: 800000
    num_steps_sampled: 100000
    num_steps_trained: 100000
  iterations_since_restore: 25
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.215624999999996
    ram_util_percent: 56.81822916666667
  pid: 3846
  policy_reward_max:
    '1': 389.14210029759187
    '2': 116.60164458738986
    '3': 156.73915228647456
    '4': 207.2176733063296
    '5': 84.12446474783098
    '6': 365.1010379926646
    '7': 191.83276417177547
    '8': 122.27268934141523
  policy_reward_mean:
    '1': 365.2110724178089
    '2': 51.51871124713528
    '3': 85.92256307182858
    '4': 187.63504559729546
    '5': 42.94889645675186
    '6': 335.6663149942959
    '7': 115.71528743010532
    '8': 65.39602901184493
  policy_reward_min:
    '1': 324.8074761514395
    '2': -8.17722969068658
    '3': 40.864719343108774
    '4': 160.7359781844125
    '5': -35.20382136339056
    '6': 167.95119314840684
    '7': 62.2477444455709
    '8': 16.80763929864587
  sampler_perf:
    mean_action_processing_ms: 0.2122825623397408
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 41.94337518120653
    mean_inference_ms: 6.285506229777019
    mean_raw_obs_processing_ms: 0.7260193297899049
  time_since_restore: 3202.3074402809143
  time_this_iter_s: 142.61865520477295
  time_total_s: 3202.3074402809143
  timers:
    learn_throughput: 130.718
    learn_time_ms: 30600.167
    load_throughput: 265194.985
    load_time_ms: 15.083
    sample_throughput: 35.935
    sample_time_ms: 111312.853
    update_time_ms: 12.952
  timestamp: 1651207849
  timesteps_since_restore: 0
  timesteps_total: 100000
  training_iteration: 25
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     25 |          3202.31 | 100000 |  1250.01 |              1398.82 |              1045.74 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 832000
  custom_metrics:
    eps_sum_utility_max: 1256.787661084886
    eps_sum_utility_mean: 1120.8388501025265
    eps_sum_utility_min: 828.0929429588386
    sum_utility_max: 28.48544602181517
    sum_utility_mean: 22.076475433854142
    sum_utility_min: 5.437749960267352
  date: 2022-04-29_10-23-10
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1485.4839420289966
  episode_reward_mean: 1254.4943578605903
  episode_reward_min: 1059.894970822597
  episodes_this_iter: 40
  episodes_total: 1040
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7410987615585327
          entropy_coeff: 0.0
          kl: 0.010734336450695992
          model: {}
          policy_loss: -0.018406938761472702
          total_loss: 3394.529541015625
          vf_explained_var: -5.5759183936743284e-08
          vf_loss: 3394.544677734375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.499982237815857
          entropy_coeff: 0.0
          kl: 0.01494990661740303
          model: {}
          policy_loss: -0.021974768489599228
          total_loss: 391.77752685546875
          vf_explained_var: 0.4532870650291443
          vf_loss: 391.7950134277344
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5566420555114746
          entropy_coeff: 0.0
          kl: 0.010591701604425907
          model: {}
          policy_loss: -0.013337221927940845
          total_loss: 110.37610626220703
          vf_explained_var: 0.7940611243247986
          vf_loss: 110.38626861572266
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5124974250793457
          entropy_coeff: 0.0
          kl: 0.010443529114127159
          model: {}
          policy_loss: -0.013758976943790913
          total_loss: 32.47792053222656
          vf_explained_var: 0.9216103553771973
          vf_loss: 32.486976623535156
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6236498355865479
          entropy_coeff: 0.0
          kl: 0.008066543377935886
          model: {}
          policy_loss: -0.012944381684064865
          total_loss: 46.95326232910156
          vf_explained_var: 0.8430957198143005
          vf_loss: 46.96257781982422
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.626977801322937
          entropy_coeff: 0.0
          kl: 0.0175157580524683
          model: {}
          policy_loss: -0.015638334676623344
          total_loss: 309.63385009765625
          vf_explained_var: 0.9175550937652588
          vf_loss: 309.64556884765625
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3032052516937256
          entropy_coeff: 0.0
          kl: 0.009393728338181973
          model: {}
          policy_loss: -0.015314892865717411
          total_loss: 62.46116256713867
          vf_explained_var: 0.89362633228302
          vf_loss: 62.473655700683594
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.443473219871521
          entropy_coeff: 0.0
          kl: 0.007907113060355186
          model: {}
          policy_loss: -0.017572585493326187
          total_loss: 142.0790252685547
          vf_explained_var: 0.7619228959083557
          vf_loss: 142.09304809570312
    num_agent_steps_sampled: 832000
    num_agent_steps_trained: 832000
    num_steps_sampled: 104000
    num_steps_trained: 104000
  iterations_since_restore: 26
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.14736842105263
    ram_util_percent: 56.830000000000005
  pid: 3846
  policy_reward_max:
    '1': 389.14210029759187
    '2': 116.60164458738986
    '3': 140.97499003453413
    '4': 208.7870417598318
    '5': 70.73494089537678
    '6': 381.38485038122775
    '7': 191.83276417177547
    '8': 124.644509593111
  policy_reward_mean:
    '1': 355.4272975148105
    '2': 55.21855403997935
    '3': 88.06842296277115
    '4': 189.2678270972918
    '5': 47.262759701879695
    '6': 342.222002559967
    '7': 114.28974593723291
    '8': 62.7377480466581
  policy_reward_min:
    '1': 301.3742537986781
    '2': -80.25179245212622
    '3': 40.864719343108774
    '4': 160.7359781844125
    '5': 3.9611617643728794
    '6': 167.95119314840684
    '7': 67.23769096983042
    '8': -3.0550726808901016
  sampler_perf:
    mean_action_processing_ms: 0.2131511467290829
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 42.16140641870911
    mean_inference_ms: 6.307982864959225
    mean_raw_obs_processing_ms: 0.7289188792603829
  time_since_restore: 3343.43616938591
  time_this_iter_s: 141.12872910499573
  time_total_s: 3343.43616938591
  timers:
    learn_throughput: 130.603
    learn_time_ms: 30627.231
    load_throughput: 266649.12
    load_time_ms: 15.001
    sample_throughput: 35.939
    sample_time_ms: 111298.854
    update_time_ms: 12.981
  timestamp: 1651207990
  timesteps_since_restore: 0
  timesteps_total: 104000
  training_iteration: 26
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     26 |          3343.44 | 104000 |  1254.49 |              1485.48 |              1059.89 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 864000
  custom_metrics:
    eps_sum_utility_max: 1230.4097457939176
    eps_sum_utility_mean: 1108.5383325409196
    eps_sum_utility_min: 187.1464515856281
    sum_utility_max: 28.48544602181517
    sum_utility_mean: 22.009887260656193
    sum_utility_min: 5.437749960267352
  date: 2022-04-29_10-25-33
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1485.4839420289966
  episode_reward_mean: 1267.2743901283309
  episode_reward_min: 995.8429734133506
  episodes_this_iter: 40
  episodes_total: 1080
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.708698034286499
          entropy_coeff: 0.0
          kl: 0.009368483908474445
          model: {}
          policy_loss: -0.012765409424901009
          total_loss: 3365.487060546875
          vf_explained_var: -5.7681912579710115e-09
          vf_loss: 3365.497802734375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4295819997787476
          entropy_coeff: 0.0
          kl: 0.015110742300748825
          model: {}
          policy_loss: -0.018093816936016083
          total_loss: 220.1514129638672
          vf_explained_var: 0.6156680583953857
          vf_loss: 220.1649932861328
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.553838849067688
          entropy_coeff: 0.0
          kl: 0.00840433407574892
          model: {}
          policy_loss: -0.019803429022431374
          total_loss: 821.9505004882812
          vf_explained_var: 0.3595826029777527
          vf_loss: 821.9678955078125
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5102185010910034
          entropy_coeff: 0.0
          kl: 0.005022700410336256
          model: {}
          policy_loss: -0.008962327614426613
          total_loss: 27.967485427856445
          vf_explained_var: 0.9343612790107727
          vf_loss: 27.97418785095215
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.6087228059768677
          entropy_coeff: 0.0
          kl: 0.007021717261523008
          model: {}
          policy_loss: -0.011934136040508747
          total_loss: 56.65434646606445
          vf_explained_var: 0.8191454410552979
          vf_loss: 56.66313171386719
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.605231523513794
          entropy_coeff: 0.0
          kl: 0.011950709857046604
          model: {}
          policy_loss: -0.019567355513572693
          total_loss: 242.16282653808594
          vf_explained_var: 0.9313482642173767
          vf_loss: 242.1796875
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.2571532726287842
          entropy_coeff: 0.0
          kl: 0.00817960873246193
          model: {}
          policy_loss: -0.012451008893549442
          total_loss: 144.0164337158203
          vf_explained_var: 0.8193297982215881
          vf_loss: 144.02639770507812
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4490461349487305
          entropy_coeff: 0.0
          kl: 0.0068796114064753056
          model: {}
          policy_loss: -0.014549490064382553
          total_loss: 162.5541229248047
          vf_explained_var: 0.7724770903587341
          vf_loss: 162.56553649902344
    num_agent_steps_sampled: 864000
    num_agent_steps_trained: 864000
    num_steps_sampled: 108000
    num_steps_trained: 108000
  iterations_since_restore: 27
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.301562499999996
    ram_util_percent: 56.8203125
  pid: 3846
  policy_reward_max:
    '1': 381.64320661038744
    '2': 116.60164458738986
    '3': 145.24654567465367
    '4': 210.4354964347102
    '5': 71.59586715971383
    '6': 381.38485038122775
    '7': 233.6875037761275
    '8': 124.644509593111
  policy_reward_mean:
    '1': 349.83511102867726
    '2': 59.604406613386644
    '3': 88.53742382975807
    '4': 191.70223089803017
    '5': 48.533324211534
    '6': 346.989272725974
    '7': 115.84822769528823
    '8': 66.22439312568284
  policy_reward_min:
    '1': 301.3742537986781
    '2': -80.25179245212622
    '3': -193.81119472037997
    '4': 171.13435659602024
    '5': 11.950447755406277
    '6': 263.0432458915501
    '7': 63.65463280634832
    '8': -3.0550726808901016
  sampler_perf:
    mean_action_processing_ms: 0.2139474113113683
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 42.364845267399524
    mean_inference_ms: 6.328933281789777
    mean_raw_obs_processing_ms: 0.7315571385273424
  time_since_restore: 3485.7753295898438
  time_this_iter_s: 142.33916020393372
  time_total_s: 3485.7753295898438
  timers:
    learn_throughput: 130.249
    learn_time_ms: 30710.519
    load_throughput: 266090.032
    load_time_ms: 15.033
    sample_throughput: 35.927
    sample_time_ms: 111335.553
    update_time_ms: 12.986
  timestamp: 1651208133
  timesteps_since_restore: 0
  timesteps_total: 108000
  training_iteration: 27
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.4/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     27 |          3485.78 | 108000 |  1267.27 |              1485.48 |              995.843 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 896000
  custom_metrics:
    eps_sum_utility_max: 1254.0753166009117
    eps_sum_utility_mean: 1125.882415878834
    eps_sum_utility_min: 187.1464515856281
    sum_utility_max: 28.48544602181517
    sum_utility_mean: 21.947218657187634
    sum_utility_min: 5.437749960267352
  date: 2022-04-29_10-27-55
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1493.1515932673458
  episode_reward_mean: 1287.354247819564
  episode_reward_min: 995.8429734133506
  episodes_this_iter: 40
  episodes_total: 1120
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.725850224494934
          entropy_coeff: 0.0
          kl: 0.01451831590384245
          model: {}
          policy_loss: -0.01873447746038437
          total_loss: 3436.995849609375
          vf_explained_var: -1.7304573773913035e-08
          vf_loss: 3437.010009765625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.459663987159729
          entropy_coeff: 0.0
          kl: 0.010020765475928783
          model: {}
          policy_loss: -0.01325756125152111
          total_loss: 189.62364196777344
          vf_explained_var: 0.6919299960136414
          vf_loss: 189.63389587402344
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5804675817489624
          entropy_coeff: 0.0
          kl: 0.007197309285402298
          model: {}
          policy_loss: -0.008733377791941166
          total_loss: 98.3716812133789
          vf_explained_var: 0.8463910818099976
          vf_loss: 98.37825775146484
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4773317575454712
          entropy_coeff: 0.0
          kl: 0.008353800512850285
          model: {}
          policy_loss: -0.015736358240246773
          total_loss: 32.38227844238281
          vf_explained_var: 0.9246963858604431
          vf_loss: 32.39425277709961
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5841425657272339
          entropy_coeff: 0.0
          kl: 0.0071759773418307304
          model: {}
          policy_loss: -0.01294262520968914
          total_loss: 41.72738265991211
          vf_explained_var: 0.8739274740219116
          vf_loss: 41.73709487915039
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.5506147146224976
          entropy_coeff: 0.0
          kl: 0.01497857179492712
          model: {}
          policy_loss: -0.01628529466688633
          total_loss: 157.99497985839844
          vf_explained_var: 0.9530403017997742
          vf_loss: 158.0078887939453
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.250950813293457
          entropy_coeff: 0.0
          kl: 0.008400158025324345
          model: {}
          policy_loss: -0.01624949462711811
          total_loss: 99.26824188232422
          vf_explained_var: 0.8528213500976562
          vf_loss: 99.28197479248047
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4332754611968994
          entropy_coeff: 0.0
          kl: 0.009154831990599632
          model: {}
          policy_loss: -0.015255955047905445
          total_loss: 145.47959899902344
          vf_explained_var: 0.8231818079948425
          vf_loss: 145.49075317382812
    num_agent_steps_sampled: 896000
    num_agent_steps_trained: 896000
    num_steps_sampled: 112000
    num_steps_trained: 112000
  iterations_since_restore: 28
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.30677083333333
    ram_util_percent: 56.833333333333336
  pid: 3846
  policy_reward_max:
    '1': 379.53491655950734
    '2': 125.48916884478697
    '3': 145.24654567465367
    '4': 218.07345756927194
    '5': 73.00103575216099
    '6': 381.38485038122775
    '7': 233.6875037761275
    '8': 137.75610852060095
  policy_reward_mean:
    '1': 349.92845601374785
    '2': 66.04679399227534
    '3': 95.18625366938029
    '4': 192.06748929549423
    '5': 50.87771992699903
    '6': 346.5336330231188
    '7': 116.62785204643798
    '8': 70.08604985211106
  policy_reward_min:
    '1': 308.28589661345137
    '2': 3.7137389339463356
    '3': -193.81119472037997
    '4': 168.34802657878288
    '5': 11.950447755406277
    '6': 263.0432458915501
    '7': 42.86265287036753
    '8': 20.672836185538497
  sampler_perf:
    mean_action_processing_ms: 0.21464741634505968
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 42.552249800997416
    mean_inference_ms: 6.348278526779811
    mean_raw_obs_processing_ms: 0.7339717215472902
  time_since_restore: 3627.7860276699066
  time_this_iter_s: 142.01069808006287
  time_total_s: 3627.7860276699066
  timers:
    learn_throughput: 130.112
    learn_time_ms: 30742.77
    load_throughput: 269920.233
    load_time_ms: 14.819
    sample_throughput: 35.95
    sample_time_ms: 111264.792
    update_time_ms: 13.105
  timestamp: 1651208275
  timesteps_since_restore: 0
  timesteps_total: 112000
  training_iteration: 28
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     28 |          3627.79 | 112000 |  1287.35 |              1493.15 |              995.843 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 928000
  custom_metrics:
    eps_sum_utility_max: 1293.8602770260882
    eps_sum_utility_mean: 1156.4480458197684
    eps_sum_utility_min: 1008.265837880724
    sum_utility_max: 28.297117079165513
    sum_utility_mean: 22.469606034678858
    sum_utility_min: 15.350596548986244
  date: 2022-04-29_10-30-17
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1493.1515932673458
  episode_reward_mean: 1316.389786382913
  episode_reward_min: 1161.728181643613
  episodes_this_iter: 40
  episodes_total: 1160
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7299983501434326
          entropy_coeff: 0.0
          kl: 0.008740860037505627
          model: {}
          policy_loss: -0.011389244347810745
          total_loss: 3390.4775390625
          vf_explained_var: -1.7304573773913035e-08
          vf_loss: 3390.486083984375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4498823881149292
          entropy_coeff: 0.0
          kl: 0.012900225818157196
          model: {}
          policy_loss: -0.017059162259101868
          total_loss: 202.52618408203125
          vf_explained_var: 0.6926818490028381
          vf_loss: 202.53936767578125
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5799810886383057
          entropy_coeff: 0.0
          kl: 0.008656041696667671
          model: {}
          policy_loss: -0.012376059778034687
          total_loss: 99.91011047363281
          vf_explained_var: 0.8386250734329224
          vf_loss: 99.91989135742188
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4769175052642822
          entropy_coeff: 0.0
          kl: 0.0061005461029708385
          model: {}
          policy_loss: -0.013918746262788773
          total_loss: 34.53255081176758
          vf_explained_var: 0.9177488088607788
          vf_loss: 34.54372787475586
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5654064416885376
          entropy_coeff: 0.0
          kl: 0.010019627399742603
          model: {}
          policy_loss: -0.01705125905573368
          total_loss: 58.596126556396484
          vf_explained_var: 0.8146856427192688
          vf_loss: 58.608665466308594
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.5291516780853271
          entropy_coeff: 0.0
          kl: 0.014579525217413902
          model: {}
          policy_loss: -0.018449174240231514
          total_loss: 122.14643859863281
          vf_explained_var: 0.9635226726531982
          vf_loss: 122.16161346435547
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1942849159240723
          entropy_coeff: 0.0
          kl: 0.009639465250074863
          model: {}
          policy_loss: -0.015428655780851841
          total_loss: 120.60578918457031
          vf_explained_var: 0.8522708415985107
          vf_loss: 120.61832427978516
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4299718141555786
          entropy_coeff: 0.0
          kl: 0.007524434011429548
          model: {}
          policy_loss: -0.017768649384379387
          total_loss: 169.03421020507812
          vf_explained_var: 0.8146502375602722
          vf_loss: 169.04859924316406
    num_agent_steps_sampled: 928000
    num_agent_steps_trained: 928000
    num_steps_sampled: 116000
    num_steps_trained: 116000
  iterations_since_restore: 29
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.201047120418856
    ram_util_percent: 56.83664921465968
  pid: 3846
  policy_reward_max:
    '1': 381.6183886170378
    '2': 126.41713838767384
    '3': 146.8648654189347
    '4': 218.07345756927194
    '5': 75.2489455598817
    '6': 371.24415112158965
    '7': 179.66733129428223
    '8': 142.19258147159556
  policy_reward_mean:
    '1': 352.6438442069591
    '2': 70.74549650479197
    '3': 101.89317005419781
    '4': 191.85559683615054
    '5': 52.234943315463354
    '6': 345.8179141009843
    '7': 123.0015227612793
    '8': 78.19729860308662
  policy_reward_min:
    '1': 315.24308048452895
    '2': 15.451176971692156
    '3': 21.55457751329708
    '4': 168.34802657878288
    '5': 8.506109033386133
    '6': 319.43441533845197
    '7': 42.86265287036753
    '8': 30.394083522037725
  sampler_perf:
    mean_action_processing_ms: 0.21533303668726225
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 42.72836860665694
    mean_inference_ms: 6.3670115740324125
    mean_raw_obs_processing_ms: 0.7363176131847377
  time_since_restore: 3769.88076877594
  time_this_iter_s: 142.09474110603333
  time_total_s: 3769.88076877594
  timers:
    learn_throughput: 129.913
    learn_time_ms: 30789.787
    load_throughput: 273496.23
    load_time_ms: 14.625
    sample_throughput: 35.947
    sample_time_ms: 111276.084
    update_time_ms: 13.266
  timestamp: 1651208417
  timesteps_since_restore: 0
  timesteps_total: 116000
  training_iteration: 29
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     29 |          3769.88 | 116000 |  1316.39 |              1493.15 |              1161.73 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 960000
  custom_metrics:
    eps_sum_utility_max: 1293.8602770260882
    eps_sum_utility_mean: 1162.2179083510957
    eps_sum_utility_min: 1043.8472500583741
    sum_utility_max: 27.8151321870445
    sum_utility_mean: 22.562311222072235
    sum_utility_min: 15.350596548986244
  date: 2022-04-29_10-32-39
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1487.1994155187076
  episode_reward_mean: 1318.751615031922
  episode_reward_min: 1174.5009090479296
  episodes_this_iter: 40
  episodes_total: 1200
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7210829257965088
          entropy_coeff: 0.0
          kl: 0.011455662548542023
          model: {}
          policy_loss: -0.011616213247179985
          total_loss: 3346.04150390625
          vf_explained_var: -1.5381843354589364e-08
          vf_loss: 3346.050048828125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.44053053855896
          entropy_coeff: 0.0
          kl: 0.011480201967060566
          model: {}
          policy_loss: -0.015766778960824013
          total_loss: 139.42835998535156
          vf_explained_var: 0.7332249879837036
          vf_loss: 139.44065856933594
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5473854541778564
          entropy_coeff: 0.0
          kl: 0.011282223276793957
          model: {}
          policy_loss: -0.014401585794985294
          total_loss: 107.93494415283203
          vf_explained_var: 0.8365283608436584
          vf_loss: 107.94596099853516
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5019867420196533
          entropy_coeff: 0.0
          kl: 0.008874554187059402
          model: {}
          policy_loss: -0.019701069220900536
          total_loss: 25.661340713500977
          vf_explained_var: 0.9429702162742615
          vf_loss: 25.677045822143555
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5440984964370728
          entropy_coeff: 0.0
          kl: 0.008053494617342949
          model: {}
          policy_loss: -0.01397364679723978
          total_loss: 37.768211364746094
          vf_explained_var: 0.8879218697547913
          vf_loss: 37.778560638427734
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.5540577173233032
          entropy_coeff: 0.0
          kl: 0.012235022149980068
          model: {}
          policy_loss: -0.013957362622022629
          total_loss: 84.8409652709961
          vf_explained_var: 0.9749247431755066
          vf_loss: 84.85215759277344
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1994575262069702
          entropy_coeff: 0.0
          kl: 0.01357182301580906
          model: {}
          policy_loss: -0.019994262605905533
          total_loss: 86.83277893066406
          vf_explained_var: 0.8878775238990784
          vf_loss: 86.84870910644531
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.432013750076294
          entropy_coeff: 0.0
          kl: 0.00816528219729662
          model: {}
          policy_loss: -0.017153898254036903
          total_loss: 93.4378890991211
          vf_explained_var: 0.8763392567634583
          vf_loss: 93.45135498046875
    num_agent_steps_sampled: 960000
    num_agent_steps_trained: 960000
    num_steps_sampled: 120000
    num_steps_trained: 120000
  iterations_since_restore: 30
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.4565445026178
    ram_util_percent: 56.83298429319371
  pid: 3846
  policy_reward_max:
    '1': 381.6183886170378
    '2': 126.41713838767384
    '3': 156.77354836207442
    '4': 218.07345756927194
    '5': 75.2489455598817
    '6': 362.96714706634793
    '7': 179.66733129428223
    '8': 142.19258147159556
  policy_reward_mean:
    '1': 354.19025370963504
    '2': 69.20190774071472
    '3': 104.80339629431455
    '4': 192.70340375958511
    '5': 52.433436180575264
    '6': 343.47349023694716
    '7': 124.89995963987192
    '8': 77.04576747027829
  policy_reward_min:
    '1': 323.98661655589115
    '2': 23.426898720956395
    '3': 66.4808916260172
    '4': 169.22968498386166
    '5': 8.506109033386133
    '6': 315.0432292226154
    '7': 42.86265287036753
    '8': 30.394083522037725
  sampler_perf:
    mean_action_processing_ms: 0.2159346725208366
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 42.88607321741685
    mean_inference_ms: 6.383873997006501
    mean_raw_obs_processing_ms: 0.7385707064821907
  time_since_restore: 3911.3813393115997
  time_this_iter_s: 141.5005705356598
  time_total_s: 3911.3813393115997
  timers:
    learn_throughput: 129.768
    learn_time_ms: 30824.261
    load_throughput: 273067.111
    load_time_ms: 14.648
    sample_throughput: 35.99
    sample_time_ms: 111143.412
    update_time_ms: 13.445
  timestamp: 1651208559
  timesteps_since_restore: 0
  timesteps_total: 120000
  training_iteration: 30
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     30 |          3911.38 | 120000 |  1318.75 |               1487.2 |               1174.5 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 992000
  custom_metrics:
    eps_sum_utility_max: 1266.743284569671
    eps_sum_utility_mean: 1173.6713429024128
    eps_sum_utility_min: 1043.8472500583741
    sum_utility_max: 27.8151321870445
    sum_utility_mean: 22.694575093983623
    sum_utility_min: 18.189888809907284
  date: 2022-04-29_10-35-02
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1517.7086887318105
  episode_reward_mean: 1341.5994893618647
  episode_reward_min: 1133.0160151086766
  episodes_this_iter: 40
  episodes_total: 1240
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7011631727218628
          entropy_coeff: 0.0
          kl: 0.010520858690142632
          model: {}
          policy_loss: -0.01276591420173645
          total_loss: 3361.820068359375
          vf_explained_var: -1.5381843354589364e-08
          vf_loss: 3361.829833984375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4121055603027344
          entropy_coeff: 0.0
          kl: 0.013930853456258774
          model: {}
          policy_loss: -0.01923701912164688
          total_loss: 168.78602600097656
          vf_explained_var: 0.7308180332183838
          vf_loss: 168.80108642578125
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.536434531211853
          entropy_coeff: 0.0
          kl: 0.011857072822749615
          model: {}
          policy_loss: -0.013890339992940426
          total_loss: 92.02066802978516
          vf_explained_var: 0.8607955574989319
          vf_loss: 92.0309829711914
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.485077977180481
          entropy_coeff: 0.0
          kl: 0.0075804139487445354
          model: {}
          policy_loss: -0.013342846184968948
          total_loss: 26.70542335510254
          vf_explained_var: 0.9384506344795227
          vf_loss: 26.71535301208496
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4993290901184082
          entropy_coeff: 0.0
          kl: 0.013361247256398201
          model: {}
          policy_loss: -0.021653832867741585
          total_loss: 34.84042739868164
          vf_explained_var: 0.9008815288543701
          vf_loss: 34.8560676574707
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.5202869176864624
          entropy_coeff: 0.0
          kl: 0.009028234519064426
          model: {}
          policy_loss: -0.010983804240822792
          total_loss: 67.0961685180664
          vf_explained_var: 0.9802002310752869
          vf_loss: 67.10511779785156
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.184970736503601
          entropy_coeff: 0.0
          kl: 0.011883391067385674
          model: {}
          policy_loss: -0.01948762685060501
          total_loss: 158.22360229492188
          vf_explained_var: 0.8376232981681824
          vf_loss: 158.23953247070312
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4287077188491821
          entropy_coeff: 0.0
          kl: 0.007241209037601948
          model: {}
          policy_loss: -0.01493032369762659
          total_loss: 87.96043395996094
          vf_explained_var: 0.8975713849067688
          vf_loss: 87.97211456298828
    num_agent_steps_sampled: 992000
    num_agent_steps_trained: 992000
    num_steps_sampled: 124000
    num_steps_trained: 124000
  iterations_since_restore: 31
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.26891191709844
    ram_util_percent: 56.81347150259067
  pid: 3846
  policy_reward_max:
    '1': 381.7256085427858
    '2': 124.95973274392864
    '3': 156.77354836207442
    '4': 218.11986088838412
    '5': 79.87845131248716
    '6': 365.67152160901526
    '7': 204.23304174071143
    '8': 142.19258147159556
  policy_reward_mean:
    '1': 356.46038592676183
    '2': 72.04945895567508
    '3': 107.33749061168882
    '4': 194.4354624291683
    '5': 55.00809404973621
    '6': 342.2484534590138
    '7': 134.06602028708997
    '8': 79.99412364273108
  policy_reward_min:
    '1': 323.98661655589115
    '2': 22.682089333471257
    '3': 62.0541677376132
    '4': 173.8112646947181
    '5': 25.877265134645054
    '6': 315.0432292226154
    '7': 74.62191709474412
    '8': 31.23627373266501
  sampler_perf:
    mean_action_processing_ms: 0.21653737036009432
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.03626474174602
    mean_inference_ms: 6.400330888835572
    mean_raw_obs_processing_ms: 0.7408279496773167
  time_since_restore: 4054.46497631073
  time_this_iter_s: 143.08363699913025
  time_total_s: 4054.46497631073
  timers:
    learn_throughput: 129.506
    learn_time_ms: 30886.576
    load_throughput: 274420.905
    load_time_ms: 14.576
    sample_throughput: 35.958
    sample_time_ms: 111241.617
    update_time_ms: 13.37
  timestamp: 1651208702
  timesteps_since_restore: 0
  timesteps_total: 124000
  training_iteration: 31
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     31 |          4054.46 | 124000 |   1341.6 |              1517.71 |              1133.02 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1024000
  custom_metrics:
    eps_sum_utility_max: 1267.432039137206
    eps_sum_utility_mean: 1175.5278808618286
    eps_sum_utility_min: 990.405924305157
    sum_utility_max: 25.37735205035703
    sum_utility_mean: 22.437977424053674
    sum_utility_min: 19.20154019746592
  date: 2022-04-29_10-37-24
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1523.716656554541
  episode_reward_mean: 1350.432509952945
  episode_reward_min: 1133.0160151086766
  episodes_this_iter: 40
  episodes_total: 1280
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6726808547973633
          entropy_coeff: 0.0
          kl: 0.008301310241222382
          model: {}
          policy_loss: -0.012844482436776161
          total_loss: 3353.806640625
          vf_explained_var: -2.3072765031884046e-08
          vf_loss: 3353.817138671875
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4205329418182373
          entropy_coeff: 0.0
          kl: 0.0103760389611125
          model: {}
          policy_loss: -0.016253255307674408
          total_loss: 200.54342651367188
          vf_explained_var: 0.6819720268249512
          vf_loss: 200.5565948486328
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5383718013763428
          entropy_coeff: 0.0
          kl: 0.009855500422418118
          model: {}
          policy_loss: -0.014170100912451744
          total_loss: 105.4549789428711
          vf_explained_var: 0.8633416891098022
          vf_loss: 105.46619415283203
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4627262353897095
          entropy_coeff: 0.0
          kl: 0.006237765308469534
          model: {}
          policy_loss: -0.00907327700406313
          total_loss: 27.485322952270508
          vf_explained_var: 0.9391626119613647
          vf_loss: 27.491586685180664
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.5135865211486816
          entropy_coeff: 0.0
          kl: 0.005314364098012447
          model: {}
          policy_loss: -0.008182649500668049
          total_loss: 43.026527404785156
          vf_explained_var: 0.8759641051292419
          vf_loss: 43.03232192993164
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.520728588104248
          entropy_coeff: 0.0
          kl: 0.011277753859758377
          model: {}
          policy_loss: -0.01560496911406517
          total_loss: 57.62739181518555
          vf_explained_var: 0.9829290509223938
          vf_loss: 57.64045333862305
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1944231986999512
          entropy_coeff: 0.0
          kl: 0.011320190504193306
          model: {}
          policy_loss: -0.015049073845148087
          total_loss: 124.06655883789062
          vf_explained_var: 0.8669572472572327
          vf_loss: 124.07820892333984
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.424386739730835
          entropy_coeff: 0.0
          kl: 0.006593821570277214
          model: {}
          policy_loss: -0.014193638227880001
          total_loss: 141.48052978515625
          vf_explained_var: 0.8407860398292542
          vf_loss: 141.49176025390625
    num_agent_steps_sampled: 1024000
    num_agent_steps_trained: 1024000
    num_steps_sampled: 128000
    num_steps_trained: 128000
  iterations_since_restore: 32
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.355497382198955
    ram_util_percent: 56.8282722513089
  pid: 3846
  policy_reward_max:
    '1': 381.7256085427858
    '2': 128.68281441971303
    '3': 151.76739862724793
    '4': 218.11986088838412
    '5': 79.87845131248716
    '6': 365.67152160901526
    '7': 205.19760150370448
    '8': 123.0232410139003
  policy_reward_mean:
    '1': 356.8571538058322
    '2': 73.49676804987409
    '3': 110.56464831750472
    '4': 194.26016419842338
    '5': 56.08428503045662
    '6': 343.17141115757937
    '7': 137.90217302512016
    '8': 78.09590636815454
  policy_reward_min:
    '1': 318.1163460158315
    '2': 22.682089333471257
    '3': 62.0541677376132
    '4': 174.92647425827482
    '5': 26.659169699870944
    '6': 315.0432292226154
    '7': 79.34286306842236
    '8': 6.012015605406781
  sampler_perf:
    mean_action_processing_ms: 0.21711585017173032
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.177693382921454
    mean_inference_ms: 6.415959022189388
    mean_raw_obs_processing_ms: 0.7429231549166425
  time_since_restore: 4196.524230003357
  time_this_iter_s: 142.05925369262695
  time_total_s: 4196.524230003357
  timers:
    learn_throughput: 129.983
    learn_time_ms: 30773.351
    load_throughput: 273904.34
    load_time_ms: 14.604
    sample_throughput: 35.946
    sample_time_ms: 111278.13
    update_time_ms: 13.45
  timestamp: 1651208844
  timesteps_since_restore: 0
  timesteps_total: 128000
  training_iteration: 32
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     32 |          4196.52 | 128000 |  1350.43 |              1523.72 |              1133.02 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1056000
  custom_metrics:
    eps_sum_utility_max: 1272.1010629842312
    eps_sum_utility_mean: 1177.0040970134278
    eps_sum_utility_min: 963.9853223454603
    sum_utility_max: 27.983691994704884
    sum_utility_mean: 22.453761853406046
    sum_utility_min: 17.837147102375468
  date: 2022-04-29_10-39-46
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1542.381087652106
  episode_reward_mean: 1367.291996410874
  episode_reward_min: 1133.0160151086766
  episodes_this_iter: 40
  episodes_total: 1320
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5909583568572998
          entropy_coeff: 0.0
          kl: 0.015414088033139706
          model: {}
          policy_loss: -0.017032980918884277
          total_loss: 3348.77001953125
          vf_explained_var: -9.613652096618353e-09
          vf_loss: 3348.782470703125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3986434936523438
          entropy_coeff: 0.0
          kl: 0.010288236662745476
          model: {}
          policy_loss: -0.013579431921243668
          total_loss: 184.59779357910156
          vf_explained_var: 0.7334621548652649
          vf_loss: 184.60829162597656
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5291296243667603
          entropy_coeff: 0.0
          kl: 0.007424782495945692
          model: {}
          policy_loss: -0.011300257407128811
          total_loss: 78.33235931396484
          vf_explained_var: 0.8923011422157288
          vf_loss: 78.34142303466797
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4441137313842773
          entropy_coeff: 0.0
          kl: 0.0072293831035494804
          model: {}
          policy_loss: -0.013195669278502464
          total_loss: 44.300506591796875
          vf_explained_var: 0.9053826928138733
          vf_loss: 44.31045150756836
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.492508053779602
          entropy_coeff: 0.0
          kl: 0.010519137606024742
          model: {}
          policy_loss: -0.020090384408831596
          total_loss: 52.171085357666016
          vf_explained_var: 0.848342776298523
          vf_loss: 52.18643569946289
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.5176056623458862
          entropy_coeff: 0.0
          kl: 0.011101962998509407
          model: {}
          policy_loss: -0.01546219177544117
          total_loss: 154.44100952148438
          vf_explained_var: 0.9558116793632507
          vf_loss: 154.45399475097656
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1964174509048462
          entropy_coeff: 0.0
          kl: 0.008067954331636429
          model: {}
          policy_loss: -0.009590734727680683
          total_loss: 151.45445251464844
          vf_explained_var: 0.8466489911079407
          vf_loss: 151.46160888671875
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4041167497634888
          entropy_coeff: 0.0
          kl: 0.009091108106076717
          model: {}
          policy_loss: -0.01652456633746624
          total_loss: 139.00021362304688
          vf_explained_var: 0.8697143793106079
          vf_loss: 139.01266479492188
    num_agent_steps_sampled: 1056000
    num_agent_steps_trained: 1056000
    num_steps_sampled: 132000
    num_steps_trained: 132000
  iterations_since_restore: 33
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.297905759162305
    ram_util_percent: 56.83821989528797
  pid: 3846
  policy_reward_max:
    '1': 381.7256085427858
    '2': 138.816665424496
    '3': 158.44241345064654
    '4': 222.1096664468778
    '5': 79.09816087323507
    '6': 377.2390228763253
    '7': 205.3148585459082
    '8': 148.03752756864762
  policy_reward_mean:
    '1': 353.65899367402693
    '2': 78.64513852356687
    '3': 114.5871244874449
    '4': 194.42699612459234
    '5': 55.948463239751625
    '6': 348.0038238007166
    '7': 140.66727535729004
    '8': 81.3541812034845
  policy_reward_min:
    '1': 314.824367508819
    '2': 13.693515008520773
    '3': 62.0541677376132
    '4': 158.03163019912677
    '5': 9.190991966349872
    '6': 321.3940086558527
    '7': 79.34286306842236
    '8': 6.012015605406781
  sampler_perf:
    mean_action_processing_ms: 0.21762818751735977
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.30500553219277
    mean_inference_ms: 6.430162326716695
    mean_raw_obs_processing_ms: 0.7446570827836783
  time_since_restore: 4337.624468803406
  time_this_iter_s: 141.10023880004883
  time_total_s: 4337.624468803406
  timers:
    learn_throughput: 129.794
    learn_time_ms: 30818.014
    load_throughput: 276892.415
    load_time_ms: 14.446
    sample_throughput: 35.959
    sample_time_ms: 111237.656
    update_time_ms: 13.43
  timestamp: 1651208986
  timesteps_since_restore: 0
  timesteps_total: 132000
  training_iteration: 33
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     33 |          4337.62 | 132000 |  1367.29 |              1542.38 |              1133.02 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1088000
  custom_metrics:
    eps_sum_utility_max: 1272.1010629842312
    eps_sum_utility_mean: 1181.764635108004
    eps_sum_utility_min: 963.9853223454603
    sum_utility_max: 27.983691994704884
    sum_utility_mean: 22.54598690791946
    sum_utility_min: 16.215812447919497
  date: 2022-04-29_10-42-08
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1542.381087652106
  episode_reward_mean: 1379.7643694083513
  episode_reward_min: 1196.6732172207903
  episodes_this_iter: 40
  episodes_total: 1360
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6235711574554443
          entropy_coeff: 0.0
          kl: 0.011379762552678585
          model: {}
          policy_loss: -0.011222331784665585
          total_loss: 3347.7568359375
          vf_explained_var: 0.0
          vf_loss: 3347.7646484375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3478748798370361
          entropy_coeff: 0.0
          kl: 0.011624676175415516
          model: {}
          policy_loss: -0.01646994613111019
          total_loss: 131.35848999023438
          vf_explained_var: 0.7454768419265747
          vf_loss: 131.37147521972656
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.5307780504226685
          entropy_coeff: 0.0
          kl: 0.01113515067845583
          model: {}
          policy_loss: -0.015041070990264416
          total_loss: 74.16702270507812
          vf_explained_var: 0.8888785243034363
          vf_loss: 74.1787338256836
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4419301748275757
          entropy_coeff: 0.0
          kl: 0.004146818071603775
          model: {}
          policy_loss: -0.006588519550859928
          total_loss: 23.631193161010742
          vf_explained_var: 0.9480457305908203
          vf_loss: 23.635915756225586
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4740245342254639
          entropy_coeff: 0.0
          kl: 0.007934690453112125
          model: {}
          policy_loss: -0.013207177631556988
          total_loss: 19.982933044433594
          vf_explained_var: 0.941558301448822
          vf_loss: 19.992572784423828
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.514628291130066
          entropy_coeff: 0.0
          kl: 0.011674114502966404
          model: {}
          policy_loss: -0.012679368257522583
          total_loss: 42.83015441894531
          vf_explained_var: 0.9872757792472839
          vf_loss: 42.840206146240234
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.199785828590393
          entropy_coeff: 0.0
          kl: 0.008687974885106087
          model: {}
          policy_loss: -0.016753336414694786
          total_loss: 189.89222717285156
          vf_explained_var: 0.8280866742134094
          vf_loss: 189.9063720703125
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3978157043457031
          entropy_coeff: 0.0
          kl: 0.007772242184728384
          model: {}
          policy_loss: -0.01460843626409769
          total_loss: 64.41462707519531
          vf_explained_var: 0.921674907207489
          vf_loss: 64.42574310302734
    num_agent_steps_sampled: 1088000
    num_agent_steps_trained: 1088000
    num_steps_sampled: 136000
    num_steps_trained: 136000
  iterations_since_restore: 34
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.3734375
    ram_util_percent: 56.85989583333335
  pid: 3846
  policy_reward_max:
    '1': 378.7592272386535
    '2': 138.816665424496
    '3': 158.44241345064654
    '4': 222.1096664468778
    '5': 79.09816087323507
    '6': 377.2390228763253
    '7': 209.78244374043862
    '8': 148.03752756864762
  policy_reward_mean:
    '1': 349.8603066908712
    '2': 82.23525393046097
    '3': 117.39866921958082
    '4': 195.1294397200132
    '5': 57.58471625928767
    '6': 350.94089371100716
    '7': 143.77468838901416
    '8': 82.84040148811593
  policy_reward_min:
    '1': 314.824367508819
    '2': 13.693515008520773
    '3': 78.15100138642742
    '4': 158.03163019912677
    '5': 9.190991966349872
    '6': 331.17143699972377
    '7': 90.6732077854028
    '8': 29.244615635208298
  sampler_perf:
    mean_action_processing_ms: 0.21811489537948917
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.422867815328345
    mean_inference_ms: 6.443440127941535
    mean_raw_obs_processing_ms: 0.7463011292133075
  time_since_restore: 4480.071528911591
  time_this_iter_s: 142.44706010818481
  time_total_s: 4480.071528911591
  timers:
    learn_throughput: 130.208
    learn_time_ms: 30720.112
    load_throughput: 272243.379
    load_time_ms: 14.693
    sample_throughput: 35.951
    sample_time_ms: 111261.539
    update_time_ms: 14.319
  timestamp: 1651209128
  timesteps_since_restore: 0
  timesteps_total: 136000
  training_iteration: 34
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     34 |          4480.07 | 136000 |  1379.76 |              1542.38 |              1196.67 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1120000
  custom_metrics:
    eps_sum_utility_max: 1274.158059402842
    eps_sum_utility_mean: 1182.0324774138364
    eps_sum_utility_min: 1056.5089618030256
    sum_utility_max: 27.473803908742184
    sum_utility_mean: 22.341009203993963
    sum_utility_min: 14.81478790573968
  date: 2022-04-29_10-44-30
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1542.381087652106
  episode_reward_mean: 1386.4532793691985
  episode_reward_min: 1196.6732172207903
  episodes_this_iter: 40
  episodes_total: 1400
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6349071264266968
          entropy_coeff: 0.0
          kl: 0.00485465582460165
          model: {}
          policy_loss: -0.007970597594976425
          total_loss: 3409.29638671875
          vf_explained_var: -9.613652096618353e-09
          vf_loss: 3409.302978515625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3420377969741821
          entropy_coeff: 0.0
          kl: 0.008501352742314339
          model: {}
          policy_loss: -0.01602717861533165
          total_loss: 107.80026245117188
          vf_explained_var: 0.7771992683410645
          vf_loss: 107.8137435913086
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4938071966171265
          entropy_coeff: 0.0
          kl: 0.010488634929060936
          model: {}
          policy_loss: -0.0172334685921669
          total_loss: 73.77876281738281
          vf_explained_var: 0.8870362043380737
          vf_loss: 73.79285430908203
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4803210496902466
          entropy_coeff: 0.0
          kl: 0.010167510248720646
          model: {}
          policy_loss: -0.016013246029615402
          total_loss: 24.71664810180664
          vf_explained_var: 0.942600429058075
          vf_loss: 24.73037338256836
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4654935598373413
          entropy_coeff: 0.0
          kl: 0.005537285003811121
          model: {}
          policy_loss: -0.007678125984966755
          total_loss: 35.95618438720703
          vf_explained_var: 0.8913630247116089
          vf_loss: 35.96137237548828
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.5019471645355225
          entropy_coeff: 0.0
          kl: 0.01282800454646349
          model: {}
          policy_loss: -0.014617358334362507
          total_loss: 43.29817199707031
          vf_explained_var: 0.9870779514312744
          vf_loss: 43.30990219116211
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1510270833969116
          entropy_coeff: 0.0
          kl: 0.00966520793735981
          model: {}
          policy_loss: -0.014561112970113754
          total_loss: 219.6967010498047
          vf_explained_var: 0.8047922849655151
          vf_loss: 219.70835876464844
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4017255306243896
          entropy_coeff: 0.0
          kl: 0.007518017664551735
          model: {}
          policy_loss: -0.011989245191216469
          total_loss: 83.4687271118164
          vf_explained_var: 0.8911406993865967
          vf_loss: 83.47732543945312
    num_agent_steps_sampled: 1120000
    num_agent_steps_trained: 1120000
    num_steps_sampled: 140000
    num_steps_trained: 140000
  iterations_since_restore: 35
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.27539267015707
    ram_util_percent: 56.854973821989525
  pid: 3846
  policy_reward_max:
    '1': 378.7592272386535
    '2': 138.816665424496
    '3': 158.44241345064654
    '4': 232.69330093942918
    '5': 73.65903006200584
    '6': 377.2390228763253
    '7': 209.78244374043862
    '8': 113.98351683490506
  policy_reward_mean:
    '1': 352.8557234315909
    '2': 83.40757087104436
    '3': 117.73142921655614
    '4': 194.70226669122465
    '5': 58.21498381025901
    '6': 349.9921473267945
    '7': 149.4433445525621
    '8': 80.10581346916621
  policy_reward_min:
    '1': 314.824367508819
    '2': 27.705567047473973
    '3': 77.64774806324806
    '4': 170.13484343615426
    '5': 9.190991966349872
    '6': 333.8754925845868
    '7': 90.6732077854028
    '8': 29.244615635208298
  sampler_perf:
    mean_action_processing_ms: 0.21859147788388256
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.53560141341995
    mean_inference_ms: 6.456083168749407
    mean_raw_obs_processing_ms: 0.747903824063145
  time_since_restore: 4622.101419687271
  time_this_iter_s: 142.02989077568054
  time_total_s: 4622.101419687271
  timers:
    learn_throughput: 129.847
    learn_time_ms: 30805.432
    load_throughput: 274111.986
    load_time_ms: 14.593
    sample_throughput: 35.998
    sample_time_ms: 111117.205
    update_time_ms: 14.383
  timestamp: 1651209270
  timesteps_since_restore: 0
  timesteps_total: 140000
  training_iteration: 35
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.4/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     35 |           4622.1 | 140000 |  1386.45 |              1542.38 |              1196.67 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1152000
  custom_metrics:
    eps_sum_utility_max: 1282.4940556155493
    eps_sum_utility_mean: 1195.411688885087
    eps_sum_utility_min: 1066.9104373901127
    sum_utility_max: 28.277642446410972
    sum_utility_mean: 22.19450942796767
    sum_utility_min: 12.776090068917831
  date: 2022-04-29_10-46-54
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1529.7785866674258
  episode_reward_mean: 1409.1884076014749
  episode_reward_min: 1248.6016564684046
  episodes_this_iter: 40
  episodes_total: 1440
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.15000000596046448
          cur_lr: 4.999999873689376e-05
          entropy: 1.6083972454071045
          entropy_coeff: 0.0
          kl: 0.014081887900829315
          model: {}
          policy_loss: -0.015397842973470688
          total_loss: 3361.195556640625
          vf_explained_var: -7.690921677294682e-09
          vf_loss: 3361.208984375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3335108757019043
          entropy_coeff: 0.0
          kl: 0.009903650730848312
          model: {}
          policy_loss: -0.01203111745417118
          total_loss: 132.48117065429688
          vf_explained_var: 0.7732218503952026
          vf_loss: 132.490234375
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4862220287322998
          entropy_coeff: 0.0
          kl: 0.00781415868550539
          model: {}
          policy_loss: -0.011919505894184113
          total_loss: 87.01123046875
          vf_explained_var: 0.895614504814148
          vf_loss: 87.02082061767578
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.446183443069458
          entropy_coeff: 0.0
          kl: 0.010689419694244862
          model: {}
          policy_loss: -0.011953087523579597
          total_loss: 20.699542999267578
          vf_explained_var: 0.9584873914718628
          vf_loss: 20.709095001220703
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4453890323638916
          entropy_coeff: 0.0
          kl: 0.011041523888707161
          model: {}
          policy_loss: -0.017100753262639046
          total_loss: 21.484254837036133
          vf_explained_var: 0.9410999417304993
          vf_loss: 21.496389389038086
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4955761432647705
          entropy_coeff: 0.0
          kl: 0.010642263107001781
          model: {}
          policy_loss: -0.011815538629889488
          total_loss: 40.58140182495117
          vf_explained_var: 0.9878013730049133
          vf_loss: 40.59082794189453
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1589176654815674
          entropy_coeff: 0.0
          kl: 0.01010519452393055
          model: {}
          policy_loss: -0.015506373718380928
          total_loss: 202.96542358398438
          vf_explained_var: 0.8368946313858032
          vf_loss: 202.9779052734375
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.402089238166809
          entropy_coeff: 0.0
          kl: 0.00646858150139451
          model: {}
          policy_loss: -0.014597506262362003
          total_loss: 94.68943786621094
          vf_explained_var: 0.9118863940238953
          vf_loss: 94.70113372802734
    num_agent_steps_sampled: 1152000
    num_agent_steps_trained: 1152000
    num_steps_sampled: 144000
    num_steps_trained: 144000
  iterations_since_restore: 36
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.64455958549223
    ram_util_percent: 56.880829015544045
  pid: 3846
  policy_reward_max:
    '1': 377.355802903341
    '2': 126.79545297426328
    '3': 169.2422416457762
    '4': 232.69330093942918
    '5': 80.13909949050759
    '6': 369.29833651610113
    '7': 229.49039303959435
    '8': 126.78360317112724
  policy_reward_mean:
    '1': 356.50217480580227
    '2': 87.40107225955352
    '3': 119.78117882731354
    '4': 196.87151446869962
    '5': 61.96111528523491
    '6': 348.7811968518118
    '7': 154.94752828047186
    '8': 82.9426268225868
  policy_reward_min:
    '1': 317.64311980171976
    '2': 47.188297854709674
    '3': 77.64774806324806
    '4': 173.12878771687397
    '5': 20.933537418866464
    '6': 322.17573221584627
    '7': 100.58933346174878
    '8': 30.75113133390127
  sampler_perf:
    mean_action_processing_ms: 0.21907074740314098
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.643409984062124
    mean_inference_ms: 6.468752058898324
    mean_raw_obs_processing_ms: 0.7494232459415406
  time_since_restore: 4765.429179191589
  time_this_iter_s: 143.32775950431824
  time_total_s: 4765.429179191589
  timers:
    learn_throughput: 129.234
    learn_time_ms: 30951.681
    load_throughput: 273500.689
    load_time_ms: 14.625
    sample_throughput: 35.974
    sample_time_ms: 111190.768
    update_time_ms: 14.434
  timestamp: 1651209414
  timesteps_since_restore: 0
  timesteps_total: 144000
  training_iteration: 36
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     36 |          4765.43 | 144000 |  1409.19 |              1529.78 |               1248.6 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1184000
  custom_metrics:
    eps_sum_utility_max: 1300.610264010033
    eps_sum_utility_mean: 1205.6321601216923
    eps_sum_utility_min: 1114.0955776725807
    sum_utility_max: 28.29705895986013
    sum_utility_mean: 22.49164638377689
    sum_utility_min: 6.863124874752875
  date: 2022-04-29_10-49-16
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1554.3417462653406
  episode_reward_mean: 1433.290584127528
  episode_reward_min: 1248.6016564684046
  episodes_this_iter: 40
  episodes_total: 1480
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.15000000596046448
          cur_lr: 4.999999873689376e-05
          entropy: 1.604504942893982
          entropy_coeff: 0.0
          kl: 0.013881590217351913
          model: {}
          policy_loss: -0.016875874251127243
          total_loss: 3423.89501953125
          vf_explained_var: 1.9227304193236705e-09
          vf_loss: 3423.9091796875
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3254623413085938
          entropy_coeff: 0.0
          kl: 0.010439421981573105
          model: {}
          policy_loss: -0.013853967189788818
          total_loss: 131.10423278808594
          vf_explained_var: 0.7772992849349976
          vf_loss: 131.11495971679688
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4737399816513062
          entropy_coeff: 0.0
          kl: 0.009350932203233242
          model: {}
          policy_loss: -0.009056140668690205
          total_loss: 93.5712890625
          vf_explained_var: 0.8961965441703796
          vf_loss: 93.57754516601562
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4331269264221191
          entropy_coeff: 0.0
          kl: 0.008011765778064728
          model: {}
          policy_loss: -0.010677115060389042
          total_loss: 23.39931869506836
          vf_explained_var: 0.9529733061790466
          vf_loss: 23.408193588256836
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4437445402145386
          entropy_coeff: 0.0
          kl: 0.007925612851977348
          model: {}
          policy_loss: -0.015618531033396721
          total_loss: 22.80656623840332
          vf_explained_var: 0.933684766292572
          vf_loss: 22.818620681762695
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4645947217941284
          entropy_coeff: 0.0
          kl: 0.012031023390591145
          model: {}
          policy_loss: -0.01154159102588892
          total_loss: 49.167755126953125
          vf_explained_var: 0.9852057695388794
          vf_loss: 49.176597595214844
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1310343742370605
          entropy_coeff: 0.0
          kl: 0.009686179459095001
          model: {}
          policy_loss: -0.012819068506360054
          total_loss: 211.18211364746094
          vf_explained_var: 0.8354046940803528
          vf_loss: 211.19203186035156
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4000918865203857
          entropy_coeff: 0.0
          kl: 0.007056905888020992
          model: {}
          policy_loss: -0.014418582431972027
          total_loss: 68.99335479736328
          vf_explained_var: 0.9318522810935974
          vf_loss: 69.00460052490234
    num_agent_steps_sampled: 1184000
    num_agent_steps_trained: 1184000
    num_steps_sampled: 148000
    num_steps_trained: 148000
  iterations_since_restore: 37
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.34083769633508
    ram_util_percent: 56.879057591623024
  pid: 3846
  policy_reward_max:
    '1': 381.12798987428425
    '2': 126.79545297426328
    '3': 174.43035316038777
    '4': 221.36938646570545
    '5': 80.13909949050759
    '6': 377.6027302078164
    '7': 229.49039303959435
    '8': 126.78360317112724
  policy_reward_mean:
    '1': 358.34277141077933
    '2': 90.57071510274177
    '3': 127.13018245649153
    '4': 198.82255207020006
    '5': 63.04616320832753
    '6': 348.20322558918195
    '7': 159.94161454685465
    '8': 87.23335974295061
  policy_reward_min:
    '1': 305.04171489856606
    '2': 36.67531733827534
    '3': 78.34226159610216
    '4': 174.62903725216958
    '5': 20.933537418866464
    '6': 315.7632606141931
    '7': 109.65322047110344
    '8': 30.75113133390127
  sampler_perf:
    mean_action_processing_ms: 0.21953729295226465
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.745799895937125
    mean_inference_ms: 6.4811475019622415
    mean_raw_obs_processing_ms: 0.7508182038612644
  time_since_restore: 4907.639905452728
  time_this_iter_s: 142.21072626113892
  time_total_s: 4907.639905452728
  timers:
    learn_throughput: 129.043
    learn_time_ms: 30997.395
    load_throughput: 273538.592
    load_time_ms: 14.623
    sample_throughput: 35.993
    sample_time_ms: 111132.641
    update_time_ms: 14.434
  timestamp: 1651209556
  timesteps_since_restore: 0
  timesteps_total: 148000
  training_iteration: 37
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.4/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     37 |          4907.64 | 148000 |  1433.29 |              1554.34 |               1248.6 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1216000
  custom_metrics:
    eps_sum_utility_max: 1300.610264010033
    eps_sum_utility_mean: 1211.5484613191925
    eps_sum_utility_min: 1057.416131556519
    sum_utility_max: 28.474231176112877
    sum_utility_mean: 23.184739369992876
    sum_utility_min: 6.863124874752875
  date: 2022-04-29_10-51-39
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1554.3417462653406
  episode_reward_mean: 1451.4442248229182
  episode_reward_min: 1335.465608560586
  episodes_this_iter: 40
  episodes_total: 1520
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.15000000596046448
          cur_lr: 4.999999873689376e-05
          entropy: 1.5887173414230347
          entropy_coeff: 0.0
          kl: 0.014128456823527813
          model: {}
          policy_loss: -0.012214829213917255
          total_loss: 3361.8095703125
          vf_explained_var: -1.9227304193236705e-08
          vf_loss: 3361.820068359375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3172296285629272
          entropy_coeff: 0.0
          kl: 0.008342164568603039
          model: {}
          policy_loss: -0.013346485793590546
          total_loss: 121.2410659790039
          vf_explained_var: 0.7904400825500488
          vf_loss: 121.25191497802734
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.483738899230957
          entropy_coeff: 0.0
          kl: 0.010881423018872738
          model: {}
          policy_loss: -0.014940823428332806
          total_loss: 86.29415130615234
          vf_explained_var: 0.8838517665863037
          vf_loss: 86.30582427978516
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4228618144989014
          entropy_coeff: 0.0
          kl: 0.007843774743378162
          model: {}
          policy_loss: -0.014192450791597366
          total_loss: 20.617521286010742
          vf_explained_var: 0.9571282267570496
          vf_loss: 20.629947662353516
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.412841796875
          entropy_coeff: 0.0
          kl: 0.00877591036260128
          model: {}
          policy_loss: -0.014601226896047592
          total_loss: 19.508970260620117
          vf_explained_var: 0.946100652217865
          vf_loss: 19.51961898803711
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.511651635169983
          entropy_coeff: 0.0
          kl: 0.019365694373846054
          model: {}
          policy_loss: -0.02096746116876602
          total_loss: 134.0570831298828
          vf_explained_var: 0.962679922580719
          vf_loss: 134.07369995117188
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.075696349143982
          entropy_coeff: 0.0
          kl: 0.0089431032538414
          model: {}
          policy_loss: -0.013650808483362198
          total_loss: 249.45545959472656
          vf_explained_var: 0.8224227428436279
          vf_loss: 249.46644592285156
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3710445165634155
          entropy_coeff: 0.0
          kl: 0.008446869440376759
          model: {}
          policy_loss: -0.017328478395938873
          total_loss: 78.75981140136719
          vf_explained_var: 0.9230362772941589
          vf_loss: 78.77332305908203
    num_agent_steps_sampled: 1216000
    num_agent_steps_trained: 1216000
    num_steps_sampled: 152000
    num_steps_trained: 152000
  iterations_since_restore: 38
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.553886010362696
    ram_util_percent: 56.88238341968911
  pid: 3846
  policy_reward_max:
    '1': 381.12798987428425
    '2': 125.16594195345043
    '3': 174.43035316038777
    '4': 234.20089114048702
    '5': 80.13909949050759
    '6': 437.7883006703387
    '7': 236.64932780912153
    '8': 132.34502685600648
  policy_reward_mean:
    '1': 358.64484735150984
    '2': 93.98802468722575
    '3': 126.70357851216167
    '4': 199.7863627374445
    '5': 64.77253145214567
    '6': 349.3918046793671
    '7': 167.10002987048375
    '8': 91.05704553257887
  policy_reward_min:
    '1': 272.2793315909792
    '2': 36.67531733827534
    '3': 79.65370027655767
    '4': 180.91549545166032
    '5': 42.9079906799757
    '6': 315.7632606141931
    '7': 116.35674323641926
    '8': 53.40395957733182
  sampler_perf:
    mean_action_processing_ms: 0.2199712262825153
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.843559898081345
    mean_inference_ms: 6.493279326520901
    mean_raw_obs_processing_ms: 0.7522931473292664
  time_since_restore: 5050.683738231659
  time_this_iter_s: 143.04383277893066
  time_total_s: 5050.683738231659
  timers:
    learn_throughput: 128.712
    learn_time_ms: 31077.233
    load_throughput: 272506.042
    load_time_ms: 14.679
    sample_throughput: 35.986
    sample_time_ms: 111155.541
    update_time_ms: 14.471
  timestamp: 1651209699
  timesteps_since_restore: 0
  timesteps_total: 152000
  training_iteration: 38
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     38 |          5050.68 | 152000 |  1451.44 |              1554.34 |              1335.47 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1248000
  custom_metrics:
    eps_sum_utility_max: 1298.5534070384178
    eps_sum_utility_mean: 1208.380938726039
    eps_sum_utility_min: 1057.416131556519
    sum_utility_max: 28.474231176112877
    sum_utility_mean: 23.098749860075976
    sum_utility_min: 6.848998150535927
  date: 2022-04-29_10-54-02
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1573.323703382208
  episode_reward_mean: 1457.6443941270752
  episode_reward_min: 1305.4113769806281
  episodes_this_iter: 40
  episodes_total: 1560
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.15000000596046448
          cur_lr: 4.999999873689376e-05
          entropy: 1.563101053237915
          entropy_coeff: 0.0
          kl: 0.021230343729257584
          model: {}
          policy_loss: -0.01936328411102295
          total_loss: 3487.951171875
          vf_explained_var: -1.1536382515942023e-08
          vf_loss: 3487.967041015625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.2761218547821045
          entropy_coeff: 0.0
          kl: 0.010145070031285286
          model: {}
          policy_loss: -0.014381812885403633
          total_loss: 103.02493286132812
          vf_explained_var: 0.8300665020942688
          vf_loss: 103.03627014160156
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4703165292739868
          entropy_coeff: 0.0
          kl: 0.009732804261147976
          model: {}
          policy_loss: -0.011790198273956776
          total_loss: 83.37620544433594
          vf_explained_var: 0.9011491537094116
          vf_loss: 83.38507080078125
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4000803232192993
          entropy_coeff: 0.0
          kl: 0.011077668517827988
          model: {}
          policy_loss: -0.02114703506231308
          total_loss: 23.01548194885254
          vf_explained_var: 0.9536407589912415
          vf_loss: 23.03413200378418
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.377241611480713
          entropy_coeff: 0.0
          kl: 0.007953225634992123
          model: {}
          policy_loss: -0.01167511846870184
          total_loss: 19.52947425842285
          vf_explained_var: 0.9481101632118225
          vf_loss: 19.53757095336914
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4819016456604004
          entropy_coeff: 0.0
          kl: 0.009509292431175709
          model: {}
          policy_loss: -0.012271041050553322
          total_loss: 137.83457946777344
          vf_explained_var: 0.9604608416557312
          vf_loss: 137.84471130371094
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.0726227760314941
          entropy_coeff: 0.0
          kl: 0.009572945535182953
          model: {}
          policy_loss: -0.015749670565128326
          total_loss: 264.0721740722656
          vf_explained_var: 0.8066912293434143
          vf_loss: 264.0850830078125
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3779935836791992
          entropy_coeff: 0.0
          kl: 0.006959359627217054
          model: {}
          policy_loss: -0.013909908942878246
          total_loss: 94.38221740722656
          vf_explained_var: 0.9103964567184448
          vf_loss: 94.39299774169922
    num_agent_steps_sampled: 1248000
    num_agent_steps_trained: 1248000
    num_steps_sampled: 156000
    num_steps_trained: 156000
  iterations_since_restore: 39
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.29791666666666
    ram_util_percent: 56.88125
  pid: 3846
  policy_reward_max:
    '1': 380.8071493284023
    '2': 144.78885449148075
    '3': 174.27764686958028
    '4': 234.20089114048702
    '5': 77.44869576296156
    '6': 437.7883006703387
    '7': 236.72265018596696
    '8': 132.34502685600648
  policy_reward_mean:
    '1': 356.57342282356933
    '2': 97.86409666003073
    '3': 127.25326816523204
    '4': 200.23436114390591
    '5': 65.62465848699216
    '6': 352.08351768955833
    '7': 167.49785854404897
    '8': 90.5132106137371
  policy_reward_min:
    '1': 272.2793315909792
    '2': 55.55845899059797
    '3': 85.5337362083915
    '4': 178.95471073832326
    '5': 42.9079906799757
    '6': 315.7632606141931
    '7': 113.11385575572649
    '8': 54.2094836859313
  sampler_perf:
    mean_action_processing_ms: 0.22037996912072177
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 43.93665739875568
    mean_inference_ms: 6.504676698246812
    mean_raw_obs_processing_ms: 0.7537155957209246
  time_since_restore: 5192.840227365494
  time_this_iter_s: 142.15648913383484
  time_total_s: 5192.840227365494
  timers:
    learn_throughput: 128.676
    learn_time_ms: 31085.947
    load_throughput: 273993.356
    load_time_ms: 14.599
    sample_throughput: 35.986
    sample_time_ms: 111153.434
    update_time_ms: 14.365
  timestamp: 1651209842
  timesteps_since_restore: 0
  timesteps_total: 156000
  training_iteration: 39
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     39 |          5192.84 | 156000 |  1457.64 |              1573.32 |              1305.41 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1280000
  custom_metrics:
    eps_sum_utility_max: 1293.8045822506238
    eps_sum_utility_mean: 1204.1133133487608
    eps_sum_utility_min: 1017.029228850386
    sum_utility_max: 27.8218246340982
    sum_utility_mean: 22.88869256870645
    sum_utility_min: 6.848998150535927
  date: 2022-04-29_10-56-25
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1585.611572550485
  episode_reward_mean: 1465.6860912916254
  episode_reward_min: 1305.4113769806281
  episodes_this_iter: 40
  episodes_total: 1600
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.524367094039917
          entropy_coeff: 0.0
          kl: 0.005176354665309191
          model: {}
          policy_loss: -0.011391883715987206
          total_loss: 3545.057373046875
          vf_explained_var: -1.1536382515942023e-08
          vf_loss: 3545.068115234375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.2725348472595215
          entropy_coeff: 0.0
          kl: 0.007768138311803341
          model: {}
          policy_loss: -0.014926369301974773
          total_loss: 103.77061462402344
          vf_explained_var: 0.8284269571304321
          vf_loss: 103.78321075439453
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.477514386177063
          entropy_coeff: 0.0
          kl: 0.008278969675302505
          model: {}
          policy_loss: -0.014322475530207157
          total_loss: 82.22689819335938
          vf_explained_var: 0.9040243625640869
          vf_loss: 82.23873138427734
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.3817145824432373
          entropy_coeff: 0.0
          kl: 0.008040688000619411
          model: {}
          policy_loss: -0.010134530253708363
          total_loss: 19.95816993713379
          vf_explained_var: 0.9626468420028687
          vf_loss: 19.96649742126465
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3998428583145142
          entropy_coeff: 0.0
          kl: 0.0068736630491912365
          model: {}
          policy_loss: -0.012352894991636276
          total_loss: 22.741079330444336
          vf_explained_var: 0.9378535151481628
          vf_loss: 22.75033950805664
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.5066732168197632
          entropy_coeff: 0.0
          kl: 0.01607484556734562
          model: {}
          policy_loss: -0.017014279961586
          total_loss: 288.7376708984375
          vf_explained_var: 0.9220513701438904
          vf_loss: 288.7510681152344
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.0113303661346436
          entropy_coeff: 0.0
          kl: 0.008879601955413818
          model: {}
          policy_loss: -0.009573251008987427
          total_loss: 168.4398956298828
          vf_explained_var: 0.8705025911331177
          vf_loss: 168.4468231201172
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.371156096458435
          entropy_coeff: 0.0
          kl: 0.010259311646223068
          model: {}
          policy_loss: -0.020465601235628128
          total_loss: 113.47526550292969
          vf_explained_var: 0.9066359996795654
          vf_loss: 113.4911117553711
    num_agent_steps_sampled: 1280000
    num_agent_steps_trained: 1280000
    num_steps_sampled: 160000
    num_steps_trained: 160000
  iterations_since_restore: 40
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.33958333333333
    ram_util_percent: 56.885937500000004
  pid: 3846
  policy_reward_max:
    '1': 380.88706468559536
    '2': 144.78885449148075
    '3': 166.37758996493346
    '4': 234.20089114048702
    '5': 79.07230051078005
    '6': 437.7883006703387
    '7': 236.72265018596696
    '8': 125.29337722992243
  policy_reward_mean:
    '1': 353.80499345280606
    '2': 101.15973892131524
    '3': 128.03881320132862
    '4': 201.90727820851708
    '5': 65.64793091637773
    '6': 355.9830589473601
    '7': 167.0690761332049
    '8': 92.07520151071478
  policy_reward_min:
    '1': 257.3096263341721
    '2': 50.90592981146884
    '3': 84.76635165505704
    '4': 178.95471073832326
    '5': 27.378256287615297
    '6': 329.04133439456393
    '7': 113.11385575572649
    '8': 30.166898320618873
  sampler_perf:
    mean_action_processing_ms: 0.22076513563958208
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.02598516113344
    mean_inference_ms: 6.51542210122619
    mean_raw_obs_processing_ms: 0.7550883342386909
  time_since_restore: 5335.648032665253
  time_this_iter_s: 142.8078052997589
  time_total_s: 5335.648032665253
  timers:
    learn_throughput: 128.516
    learn_time_ms: 31124.47
    load_throughput: 277746.404
    load_time_ms: 14.402
    sample_throughput: 35.956
    sample_time_ms: 111245.929
    update_time_ms: 14.272
  timestamp: 1651209985
  timesteps_since_restore: 0
  timesteps_total: 160000
  training_iteration: 40
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     40 |          5335.65 | 160000 |  1465.69 |              1585.61 |              1305.41 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1312000
  custom_metrics:
    eps_sum_utility_max: 1320.7417326515683
    eps_sum_utility_mean: 1221.9509321154687
    eps_sum_utility_min: 1017.029228850386
    sum_utility_max: 28.33667702807594
    sum_utility_mean: 23.20024997077218
    sum_utility_min: 3.2020807040074875
  date: 2022-04-29_10-58-48
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1605.795105625347
  episode_reward_mean: 1481.2575532656629
  episode_reward_min: 1305.4113769806281
  episodes_this_iter: 40
  episodes_total: 1640
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.5288898944854736
          entropy_coeff: 0.0
          kl: 0.015501315705478191
          model: {}
          policy_loss: -0.01781615987420082
          total_loss: 3402.9814453125
          vf_explained_var: -1.3459112935265694e-08
          vf_loss: 3402.995361328125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.2784039974212646
          entropy_coeff: 0.0
          kl: 0.00710470462217927
          model: {}
          policy_loss: -0.007841924205422401
          total_loss: 99.90633392333984
          vf_explained_var: 0.8353025317192078
          vf_loss: 99.91203308105469
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4830735921859741
          entropy_coeff: 0.0
          kl: 0.008117971941828728
          model: {}
          policy_loss: -0.011456876993179321
          total_loss: 97.45832824707031
          vf_explained_var: 0.8989841341972351
          vf_loss: 97.46734619140625
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.3572099208831787
          entropy_coeff: 0.0
          kl: 0.008458562195301056
          model: {}
          policy_loss: -0.019931187853217125
          total_loss: 17.96269989013672
          vf_explained_var: 0.9654875993728638
          vf_loss: 17.98072624206543
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4166043996810913
          entropy_coeff: 0.0
          kl: 0.007042010314762592
          model: {}
          policy_loss: -0.010913156904280186
          total_loss: 20.88250160217285
          vf_explained_var: 0.9420498609542847
          vf_loss: 20.890243530273438
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4926691055297852
          entropy_coeff: 0.0
          kl: 0.01262256782501936
          model: {}
          policy_loss: -0.014461032114923
          total_loss: 27.479463577270508
          vf_explained_var: 0.991771399974823
          vf_loss: 27.4910831451416
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.0154894590377808
          entropy_coeff: 0.0
          kl: 0.011330647394061089
          model: {}
          policy_loss: -0.01927177794277668
          total_loss: 257.82415771484375
          vf_explained_var: 0.8283969759941101
          vf_loss: 257.8400573730469
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3767458200454712
          entropy_coeff: 0.0
          kl: 0.007616112474352121
          model: {}
          policy_loss: -0.014157918281853199
          total_loss: 46.24883270263672
          vf_explained_var: 0.9596017599105835
          vf_loss: 46.25956344604492
    num_agent_steps_sampled: 1312000
    num_agent_steps_trained: 1312000
    num_steps_sampled: 164000
    num_steps_trained: 164000
  iterations_since_restore: 41
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.25
    ram_util_percent: 56.82812500000001
  pid: 3846
  policy_reward_max:
    '1': 380.88706468559536
    '2': 144.78885449148075
    '3': 184.3904528081794
    '4': 222.54142187903383
    '5': 79.07230051078005
    '6': 430.27974763931445
    '7': 224.60598558027877
    '8': 130.92934998056992
  policy_reward_mean:
    '1': 358.79427278846697
    '2': 101.21836525044814
    '3': 132.95422779047857
    '4': 203.37666581961585
    '5': 65.19270520352232
    '6': 352.7777408943711
    '7': 172.08301999591546
    '8': 94.86055552284397
  policy_reward_min:
    '1': 257.3096263341721
    '2': 50.90592981146884
    '3': 84.76635165505704
    '4': 178.95471073832326
    '5': 27.378256287615297
    '6': 335.7033737335533
    '7': 127.83481611031259
    '8': 30.166898320618873
  sampler_perf:
    mean_action_processing_ms: 0.22114319299632526
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.1111743307524
    mean_inference_ms: 6.525706325315973
    mean_raw_obs_processing_ms: 0.7563684742308884
  time_since_restore: 5478.3869597911835
  time_this_iter_s: 142.7389271259308
  time_total_s: 5478.3869597911835
  timers:
    learn_throughput: 128.378
    learn_time_ms: 31158.07
    load_throughput: 271577.059
    load_time_ms: 14.729
    sample_throughput: 35.978
    sample_time_ms: 111177.726
    update_time_ms: 14.344
  timestamp: 1651210128
  timesteps_since_restore: 0
  timesteps_total: 164000
  training_iteration: 41
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.4/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     41 |          5478.39 | 164000 |  1481.26 |               1605.8 |              1305.41 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1344000
  custom_metrics:
    eps_sum_utility_max: 1320.7417326515683
    eps_sum_utility_mean: 1232.4991721103067
    eps_sum_utility_min: 1068.6929822909142
    sum_utility_max: 28.33667702807594
    sum_utility_mean: 23.385506085431487
    sum_utility_min: 3.2020807040074875
  date: 2022-04-29_11-01-11
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1634.871724889616
  episode_reward_mean: 1497.2142664657629
  episode_reward_min: 1296.4926648592873
  episodes_this_iter: 40
  episodes_total: 1680
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.5364197492599487
          entropy_coeff: 0.0
          kl: 0.014408763498067856
          model: {}
          policy_loss: -0.017823202535510063
          total_loss: 3482.356689453125
          vf_explained_var: -1.9227304193236705e-09
          vf_loss: 3482.371826171875
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.2638713121414185
          entropy_coeff: 0.0
          kl: 0.010299820452928543
          model: {}
          policy_loss: -0.017650770023465157
          total_loss: 72.44180297851562
          vf_explained_var: 0.8675890564918518
          vf_loss: 72.45635986328125
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.479624629020691
          entropy_coeff: 0.0
          kl: 0.009378073737025261
          model: {}
          policy_loss: -0.013714240863919258
          total_loss: 84.69803619384766
          vf_explained_var: 0.9164310693740845
          vf_loss: 84.70894622802734
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.321641445159912
          entropy_coeff: 0.0
          kl: 0.007872132584452629
          model: {}
          policy_loss: -0.014854834415018559
          total_loss: 24.284969329833984
          vf_explained_var: 0.9552277326583862
          vf_loss: 24.298053741455078
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4421418905258179
          entropy_coeff: 0.0
          kl: 0.009229190647602081
          model: {}
          policy_loss: -0.012262052856385708
          total_loss: 25.701950073242188
          vf_explained_var: 0.9289918541908264
          vf_loss: 25.710060119628906
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4632163047790527
          entropy_coeff: 0.0
          kl: 0.011061622761189938
          model: {}
          policy_loss: -0.014544636942446232
          total_loss: 163.74703979492188
          vf_explained_var: 0.9541154503822327
          vf_loss: 163.75912475585938
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.0019419193267822
          entropy_coeff: 0.0
          kl: 0.009690668433904648
          model: {}
          policy_loss: -0.01444416306912899
          total_loss: 213.0845489501953
          vf_explained_var: 0.8781007528305054
          vf_loss: 213.09609985351562
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3640152215957642
          entropy_coeff: 0.0
          kl: 0.008977347984910011
          model: {}
          policy_loss: -0.01830722950398922
          total_loss: 66.220458984375
          vf_explained_var: 0.9441203474998474
          vf_loss: 66.23472595214844
    num_agent_steps_sampled: 1344000
    num_agent_steps_trained: 1344000
    num_steps_sampled: 168000
    num_steps_trained: 168000
  iterations_since_restore: 42
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.56528497409327
    ram_util_percent: 56.91295336787565
  pid: 3846
  policy_reward_max:
    '1': 382.90838536526394
    '2': 127.22641550877515
    '3': 186.74679041340283
    '4': 235.60137820327495
    '5': 79.07230051078005
    '6': 430.27974763931445
    '7': 224.60598558027877
    '8': 130.92934998056992
  policy_reward_mean:
    '1': 358.5593558558445
    '2': 101.10643756469025
    '3': 137.39596751204192
    '4': 204.09134426736858
    '5': 65.270574288959
    '6': 354.3546320511518
    '7': 180.2432583585531
    '8': 96.19269656715349
  policy_reward_min:
    '1': 274.0306381242074
    '2': 59.82413904206486
    '3': 84.76635165505704
    '4': 180.10729726097642
    '5': 33.484894601564406
    '6': 336.24724304636175
    '7': 105.27541289981478
    '8': 55.296000495591535
  sampler_perf:
    mean_action_processing_ms: 0.2214968518875644
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.19249206493763
    mean_inference_ms: 6.535490356816399
    mean_raw_obs_processing_ms: 0.7576043942340027
  time_since_restore: 5621.596064329147
  time_this_iter_s: 143.20910453796387
  time_total_s: 5621.596064329147
  timers:
    learn_throughput: 128.107
    learn_time_ms: 31223.842
    load_throughput: 266387.046
    load_time_ms: 15.016
    sample_throughput: 35.963
    sample_time_ms: 111226.673
    update_time_ms: 14.353
  timestamp: 1651210271
  timesteps_since_restore: 0
  timesteps_total: 168000
  training_iteration: 42
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     42 |           5621.6 | 168000 |  1497.21 |              1634.87 |              1296.49 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1376000
  custom_metrics:
    eps_sum_utility_max: 1320.7417326515683
    eps_sum_utility_mean: 1236.3634340706524
    eps_sum_utility_min: 1084.0674127488332
    sum_utility_max: 28.33667702807594
    sum_utility_mean: 23.579731290915603
    sum_utility_min: 7.800015578889096
  date: 2022-04-29_11-03-35
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1646.011266113474
  episode_reward_mean: 1520.1975734954028
  episode_reward_min: 1296.4926648592873
  episodes_this_iter: 40
  episodes_total: 1720
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.582349419593811
          entropy_coeff: 0.0
          kl: 0.023282846435904503
          model: {}
          policy_loss: -0.023429041728377342
          total_loss: 3418.117919921875
          vf_explained_var: -3.845460838647341e-09
          vf_loss: 3418.135986328125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.2347121238708496
          entropy_coeff: 0.0
          kl: 0.00888931192457676
          model: {}
          policy_loss: -0.014997599646449089
          total_loss: 75.78239440917969
          vf_explained_var: 0.8806114792823792
          vf_loss: 75.7947006225586
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4579367637634277
          entropy_coeff: 0.0
          kl: 0.009157640859484673
          model: {}
          policy_loss: -0.013152009807527065
          total_loss: 72.7160415649414
          vf_explained_var: 0.9328051805496216
          vf_loss: 72.72645568847656
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.3027029037475586
          entropy_coeff: 0.0
          kl: 0.008409416303038597
          model: {}
          policy_loss: -0.012073395773768425
          total_loss: 16.906147003173828
          vf_explained_var: 0.9702953100204468
          vf_loss: 16.91632843017578
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4299689531326294
          entropy_coeff: 0.0
          kl: 0.00661524198949337
          model: {}
          policy_loss: -0.01197583507746458
          total_loss: 12.248324394226074
          vf_explained_var: 0.9656198620796204
          vf_loss: 12.257323265075684
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4421380758285522
          entropy_coeff: 0.0
          kl: 0.010993152856826782
          model: {}
          policy_loss: -0.014997578226029873
          total_loss: 150.5526580810547
          vf_explained_var: 0.9586778283119202
          vf_loss: 150.56517028808594
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.01785409450531
          entropy_coeff: 0.0
          kl: 0.00923614576458931
          model: {}
          policy_loss: -0.016498414799571037
          total_loss: 274.9700622558594
          vf_explained_var: 0.8356192111968994
          vf_loss: 274.9837646484375
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3306041955947876
          entropy_coeff: 0.0
          kl: 0.008780078031122684
          model: {}
          policy_loss: -0.017881935462355614
          total_loss: 74.7997055053711
          vf_explained_var: 0.9451079368591309
          vf_loss: 74.81362915039062
    num_agent_steps_sampled: 1376000
    num_agent_steps_trained: 1376000
    num_steps_sampled: 172000
    num_steps_trained: 172000
  iterations_since_restore: 43
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.72886597938144
    ram_util_percent: 56.897422680412376
  pid: 3846
  policy_reward_max:
    '1': 382.93472850950633
    '2': 132.5163855375541
    '3': 186.74679041340283
    '4': 235.60137820327495
    '5': 78.40620461679569
    '6': 418.71640048157775
    '7': 233.85636536919822
    '8': 132.40062119058578
  policy_reward_mean:
    '1': 357.40346280102744
    '2': 104.22533502922938
    '3': 146.91883859730476
    '4': 205.5957611971917
    '5': 65.38366663972893
    '6': 356.74520887700567
    '7': 184.91508481816928
    '8': 99.0102155357452
  policy_reward_min:
    '1': 284.77147911162575
    '2': 61.417676353791336
    '3': 99.18709497028688
    '4': 182.28117687520825
    '5': 33.484894601564406
    '6': 336.24724304636175
    '7': 95.87856848598108
    '8': 55.296000495591535
  sampler_perf:
    mean_action_processing_ms: 0.2218228551471068
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.26625665033726
    mean_inference_ms: 6.5446680636938455
    mean_raw_obs_processing_ms: 0.7587254817444085
  time_since_restore: 5765.719372987747
  time_this_iter_s: 144.12330865859985
  time_total_s: 5765.719372987747
  timers:
    learn_throughput: 126.977
    learn_time_ms: 31501.754
    load_throughput: 266017.885
    load_time_ms: 15.037
    sample_throughput: 35.955
    sample_time_ms: 111251.219
    update_time_ms: 14.702
  timestamp: 1651210415
  timesteps_since_restore: 0
  timesteps_total: 172000
  training_iteration: 43
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     43 |          5765.72 | 172000 |   1520.2 |              1646.01 |              1296.49 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1408000
  custom_metrics:
    eps_sum_utility_max: 1315.7584464227675
    eps_sum_utility_mean: 1236.98565861309
    eps_sum_utility_min: 1094.2396724700186
    sum_utility_max: 28.28505492997243
    sum_utility_mean: 23.30781253651896
    sum_utility_min: 7.800015578889096
  date: 2022-04-29_11-05-58
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1646.011266113474
  episode_reward_mean: 1527.2192508010796
  episode_reward_min: 1387.8777004846552
  episodes_this_iter: 40
  episodes_total: 1760
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.3375000059604645
          cur_lr: 4.999999873689376e-05
          entropy: 1.5407220125198364
          entropy_coeff: 0.0
          kl: 0.006171264220029116
          model: {}
          policy_loss: -0.008904797025024891
          total_loss: 3410.505615234375
          vf_explained_var: -5.7681912579710115e-09
          vf_loss: 3410.51220703125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.2217410802841187
          entropy_coeff: 0.0
          kl: 0.008717481046915054
          model: {}
          policy_loss: -0.015840981155633926
          total_loss: 81.08161163330078
          vf_explained_var: 0.872301459312439
          vf_loss: 81.09484100341797
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.4411506652832031
          entropy_coeff: 0.0
          kl: 0.010227156803011894
          model: {}
          policy_loss: -0.013570422306656837
          total_loss: 77.05712890625
          vf_explained_var: 0.9231314063072205
          vf_loss: 77.067626953125
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.2566167116165161
          entropy_coeff: 0.0
          kl: 0.007734477985650301
          model: {}
          policy_loss: -0.013646217994391918
          total_loss: 21.310815811157227
          vf_explained_var: 0.9621914029121399
          vf_loss: 21.322721481323242
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.4055768251419067
          entropy_coeff: 0.0
          kl: 0.005092133767902851
          model: {}
          policy_loss: -0.009591850452125072
          total_loss: 22.607728958129883
          vf_explained_var: 0.9371457099914551
          vf_loss: 22.615034103393555
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.4252139329910278
          entropy_coeff: 0.0
          kl: 0.010594851337373257
          model: {}
          policy_loss: -0.011495447717607021
          total_loss: 93.31478118896484
          vf_explained_var: 0.9733240604400635
          vf_loss: 93.32389831542969
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.0080503225326538
          entropy_coeff: 0.0
          kl: 0.006961807608604431
          model: {}
          policy_loss: -0.012953574769198895
          total_loss: 186.79605102539062
          vf_explained_var: 0.8843533992767334
          vf_loss: 186.80694580078125
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3284910917282104
          entropy_coeff: 0.0
          kl: 0.008343173190951347
          model: {}
          policy_loss: -0.012180468067526817
          total_loss: 58.39067077636719
          vf_explained_var: 0.9570383429527283
          vf_loss: 58.39909744262695
    num_agent_steps_sampled: 1408000
    num_agent_steps_trained: 1408000
    num_steps_sampled: 176000
    num_steps_trained: 176000
  iterations_since_restore: 44
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.620312500000004
    ram_util_percent: 56.906770833333326
  pid: 3846
  policy_reward_max:
    '1': 382.93472850950633
    '2': 132.5163855375541
    '3': 186.74679041340283
    '4': 235.60137820327495
    '5': 83.73845796733839
    '6': 418.01913355973267
    '7': 233.85636536919822
    '8': 133.20222020135841
  policy_reward_mean:
    '1': 358.5166526353758
    '2': 107.17183395764336
    '3': 146.384495827254
    '4': 207.48583558520605
    '5': 66.22878091350671
    '6': 356.245663749394
    '7': 182.70098975566285
    '8': 102.4849983770361
  policy_reward_min:
    '1': 300.7733970745986
    '2': 56.148241177604056
    '3': 99.18709497028688
    '4': 188.93669513133952
    '5': 43.74099519230088
    '6': 335.4542600591626
    '7': 95.87856848598108
    '8': 62.075964700945235
  sampler_perf:
    mean_action_processing_ms: 0.2221416896664568
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.33686915893201
    mean_inference_ms: 6.55353630147793
    mean_raw_obs_processing_ms: 0.7598830954804088
  time_since_restore: 5908.456037282944
  time_this_iter_s: 142.73666429519653
  time_total_s: 5908.456037282944
  timers:
    learn_throughput: 126.944
    learn_time_ms: 31509.948
    load_throughput: 276596.605
    load_time_ms: 14.461
    sample_throughput: 35.947
    sample_time_ms: 111275.402
    update_time_ms: 13.918
  timestamp: 1651210558
  timesteps_since_restore: 0
  timesteps_total: 176000
  training_iteration: 44
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     44 |          5908.46 | 176000 |  1527.22 |              1646.01 |              1387.88 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1440000
  custom_metrics:
    eps_sum_utility_max: 1320.3835611392617
    eps_sum_utility_mean: 1244.7594561683766
    eps_sum_utility_min: 1094.2396724700186
    sum_utility_max: 28.28505492997243
    sum_utility_mean: 23.70410023778176
    sum_utility_min: 5.438310764362527
  date: 2022-04-29_11-08-21
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1632.8010235199565
  episode_reward_mean: 1535.3533055383762
  episode_reward_min: 1387.8777004846552
  episodes_this_iter: 40
  episodes_total: 1800
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.3375000059604645
          cur_lr: 4.999999873689376e-05
          entropy: 1.54835045337677
          entropy_coeff: 0.0
          kl: 0.009913015179336071
          model: {}
          policy_loss: -0.013778217136859894
          total_loss: 3508.831787109375
          vf_explained_var: 7.690921677294682e-09
          vf_loss: 3508.842529296875
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.17554771900177
          entropy_coeff: 0.0
          kl: 0.009751301258802414
          model: {}
          policy_loss: -0.012499839998781681
          total_loss: 40.62467956542969
          vf_explained_var: 0.9237380623817444
          vf_loss: 40.63425827026367
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.412440299987793
          entropy_coeff: 0.0
          kl: 0.010554087348282337
          model: {}
          policy_loss: -0.016855379566550255
          total_loss: 78.82833099365234
          vf_explained_var: 0.928562581539154
          vf_loss: 78.8420181274414
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.2267948389053345
          entropy_coeff: 0.0
          kl: 0.009892060421407223
          model: {}
          policy_loss: -0.012976462952792645
          total_loss: 9.327836990356445
          vf_explained_var: 0.9846473932266235
          vf_loss: 9.338586807250977
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3853310346603394
          entropy_coeff: 0.0
          kl: 0.006811725441366434
          model: {}
          policy_loss: -0.00992976687848568
          total_loss: 11.212100982666016
          vf_explained_var: 0.9690967798233032
          vf_loss: 11.218966484069824
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.426017165184021
          entropy_coeff: 0.0
          kl: 0.011707833036780357
          model: {}
          policy_loss: -0.014965739101171494
          total_loss: 108.67414855957031
          vf_explained_var: 0.968462347984314
          vf_loss: 108.68648529052734
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 0.9807417988777161
          entropy_coeff: 0.0
          kl: 0.008547671139240265
          model: {}
          policy_loss: -0.012488486245274544
          total_loss: 169.8151092529297
          vf_explained_var: 0.9013217091560364
          vf_loss: 169.8250732421875
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.329268455505371
          entropy_coeff: 0.0
          kl: 0.006825814489275217
          model: {}
          policy_loss: -0.014255327172577381
          total_loss: 28.74257469177246
          vf_explained_var: 0.9787430167198181
          vf_loss: 28.75376319885254
    num_agent_steps_sampled: 1440000
    num_agent_steps_trained: 1440000
    num_steps_sampled: 180000
    num_steps_trained: 180000
  iterations_since_restore: 45
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.4703125
    ram_util_percent: 56.901041666666664
  pid: 3846
  policy_reward_max:
    '1': 383.4576052124074
    '2': 132.5163855375541
    '3': 183.43969626190005
    '4': 235.45429886637825
    '5': 83.73845796733839
    '6': 413.81528635953066
    '7': 225.67465238581642
    '8': 133.20222020135841
  policy_reward_mean:
    '1': 362.4430506975685
    '2': 108.19470431781643
    '3': 148.7050255101856
    '4': 208.73990037188392
    '5': 66.43093370895029
    '6': 355.2906804139066
    '7': 182.0202531536292
    '8': 103.52875736443501
  policy_reward_min:
    '1': 300.7733970745986
    '2': 56.148241177604056
    '3': 99.18709497028688
    '4': 188.93669513133952
    '5': 43.74099519230088
    '6': 335.4542600591626
    '7': 95.87856848598108
    '8': 62.075964700945235
  sampler_perf:
    mean_action_processing_ms: 0.22245577236206557
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.404828912322984
    mean_inference_ms: 6.56224353894388
    mean_raw_obs_processing_ms: 0.761091277811121
  time_since_restore: 6050.886467695236
  time_this_iter_s: 142.43043041229248
  time_total_s: 6050.886467695236
  timers:
    learn_throughput: 126.942
    learn_time_ms: 31510.333
    load_throughput: 271825.666
    load_time_ms: 14.715
    sample_throughput: 35.934
    sample_time_ms: 111314.364
    update_time_ms: 13.977
  timestamp: 1651210701
  timesteps_since_restore: 0
  timesteps_total: 180000
  training_iteration: 45
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.4/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     45 |          6050.89 | 180000 |  1535.35 |               1632.8 |              1387.88 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1472000
  custom_metrics:
    eps_sum_utility_max: 1324.868391941943
    eps_sum_utility_mean: 1247.6291356240881
    eps_sum_utility_min: 1094.2396724700186
    sum_utility_max: 28.280574445822094
    sum_utility_mean: 23.21707548693053
    sum_utility_min: 5.438310764362527
  date: 2022-04-29_11-10-44
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1634.2828804699916
  episode_reward_mean: 1546.5246081867112
  episode_reward_min: 1387.8777004846552
  episodes_this_iter: 40
  episodes_total: 1840
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.3375000059604645
          cur_lr: 4.999999873689376e-05
          entropy: 1.5357513427734375
          entropy_coeff: 0.0
          kl: 0.012274500913918018
          model: {}
          policy_loss: -0.01893683336675167
          total_loss: 3618.94970703125
          vf_explained_var: -3.845460838647341e-09
          vf_loss: 3618.964599609375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.2012722492218018
          entropy_coeff: 0.0
          kl: 0.009543199092149734
          model: {}
          policy_loss: -0.013943282887339592
          total_loss: 84.84178161621094
          vf_explained_var: 0.8597217798233032
          vf_loss: 84.85287475585938
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3854068517684937
          entropy_coeff: 0.0
          kl: 0.011111564934253693
          model: {}
          policy_loss: -0.013432805426418781
          total_loss: 49.534950256347656
          vf_explained_var: 0.9574544429779053
          vf_loss: 49.545047760009766
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.2171010971069336
          entropy_coeff: 0.0
          kl: 0.007901954464614391
          model: {}
          policy_loss: -0.013720417395234108
          total_loss: 11.29166030883789
          vf_explained_var: 0.9807475209236145
          vf_loss: 11.30360221862793
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3243151903152466
          entropy_coeff: 0.0
          kl: 0.009987352415919304
          model: {}
          policy_loss: -0.013630670495331287
          total_loss: 12.185914039611816
          vf_explained_var: 0.9659462571144104
          vf_loss: 12.195050239562988
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.3954298496246338
          entropy_coeff: 0.0
          kl: 0.008736156858503819
          model: {}
          policy_loss: -0.010624711401760578
          total_loss: 334.93902587890625
          vf_explained_var: 0.9097998738288879
          vf_loss: 334.9476318359375
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 0.927170991897583
          entropy_coeff: 0.0
          kl: 0.00683222059160471
          model: {}
          policy_loss: -0.015351410955190659
          total_loss: 162.8259735107422
          vf_explained_var: 0.9119276404380798
          vf_loss: 162.83929443359375
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3259085416793823
          entropy_coeff: 0.0
          kl: 0.006122326012700796
          model: {}
          policy_loss: -0.011039848439395428
          total_loss: 46.7954216003418
          vf_explained_var: 0.9645127654075623
          vf_loss: 46.803707122802734
    num_agent_steps_sampled: 1472000
    num_agent_steps_trained: 1472000
    num_steps_sampled: 184000
    num_steps_trained: 184000
  iterations_since_restore: 46
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.22020725388601
    ram_util_percent: 56.91502590673574
  pid: 3846
  policy_reward_max:
    '1': 383.4576052124074
    '2': 127.62763526756358
    '3': 183.43969626190005
    '4': 235.45429886637825
    '5': 78.85450344067841
    '6': 452.28512838279204
    '7': 230.18877137925128
    '8': 133.51245385181636
  policy_reward_mean:
    '1': 362.3685666638561
    '2': 106.09789540116037
    '3': 151.4261290188898
    '4': 209.31602422714343
    '5': 66.766904557854
    '6': 357.6139547308783
    '7': 190.19130705704802
    '8': 102.74382652988062
  policy_reward_min:
    '1': 283.40745575495407
    '2': 56.148241177604056
    '3': 100.67229140712622
    '4': 188.93669513133952
    '5': 43.74099519230088
    '6': 335.558626440358
    '7': 144.57339992044263
    '8': 62.294811744098716
  sampler_perf:
    mean_action_processing_ms: 0.22279296263782136
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.47139065727957
    mean_inference_ms: 6.571194017399304
    mean_raw_obs_processing_ms: 0.7622752424000353
  time_since_restore: 6193.951523303986
  time_this_iter_s: 143.0650556087494
  time_total_s: 6193.951523303986
  timers:
    learn_throughput: 127.14
    learn_time_ms: 31461.375
    load_throughput: 270193.66
    load_time_ms: 14.804
    sample_throughput: 35.927
    sample_time_ms: 111336.911
    update_time_ms: 13.988
  timestamp: 1651210844
  timesteps_since_restore: 0
  timesteps_total: 184000
  training_iteration: 46
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     46 |          6193.95 | 184000 |  1546.52 |              1634.28 |              1387.88 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1504000
  custom_metrics:
    eps_sum_utility_max: 1336.1225792125535
    eps_sum_utility_mean: 1258.362580395784
    eps_sum_utility_min: 1098.8695925802517
    sum_utility_max: 27.839971222164372
    sum_utility_mean: 23.18470859402454
    sum_utility_min: 5.438310764362527
  date: 2022-04-29_11-13-07
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1639.56706583638
  episode_reward_mean: 1558.8373883242136
  episode_reward_min: 1463.2077412878868
  episodes_this_iter: 40
  episodes_total: 1880
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.3375000059604645
          cur_lr: 4.999999873689376e-05
          entropy: 1.5202178955078125
          entropy_coeff: 0.0
          kl: 0.012784799560904503
          model: {}
          policy_loss: -0.018005024641752243
          total_loss: 3470.51416015625
          vf_explained_var: -1.7304573773913035e-08
          vf_loss: 3470.52783203125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1570807695388794
          entropy_coeff: 0.0
          kl: 0.010870436206459999
          model: {}
          policy_loss: -0.015042716637253761
          total_loss: 76.74079895019531
          vf_explained_var: 0.8703930974006653
          vf_loss: 76.7525863647461
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3727439641952515
          entropy_coeff: 0.0
          kl: 0.010078929364681244
          model: {}
          policy_loss: -0.014111809432506561
          total_loss: 51.3874626159668
          vf_explained_var: 0.9529078602790833
          vf_loss: 51.39854431152344
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.188705563545227
          entropy_coeff: 0.0
          kl: 0.007339373230934143
          model: {}
          policy_loss: -0.011394670233130455
          total_loss: 15.532748222351074
          vf_explained_var: 0.975527822971344
          vf_loss: 15.542492866516113
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.310185432434082
          entropy_coeff: 0.0
          kl: 0.006854856386780739
          model: {}
          policy_loss: -0.014999995939433575
          total_loss: 9.424018859863281
          vf_explained_var: 0.9751891493797302
          vf_loss: 9.435935020446777
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.394191026687622
          entropy_coeff: 0.0
          kl: 0.011583952233195305
          model: {}
          policy_loss: -0.016362031921744347
          total_loss: 105.42350006103516
          vf_explained_var: 0.9694148898124695
          vf_loss: 105.43724822998047
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 0.9090307950973511
          entropy_coeff: 0.0
          kl: 0.007186636794358492
          model: {}
          policy_loss: -0.012865609489381313
          total_loss: 110.04498291015625
          vf_explained_var: 0.9378473162651062
          vf_loss: 110.0556869506836
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.330547571182251
          entropy_coeff: 0.0
          kl: 0.008946657180786133
          model: {}
          policy_loss: -0.013483237475156784
          total_loss: 40.10183334350586
          vf_explained_var: 0.9701420664787292
          vf_loss: 40.11129379272461
    num_agent_steps_sampled: 1504000
    num_agent_steps_trained: 1504000
    num_steps_sampled: 188000
    num_steps_trained: 188000
  iterations_since_restore: 47
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.42135416666667
    ram_util_percent: 56.901562500000004
  pid: 3846
  policy_reward_max:
    '1': 386.68440392793696
    '2': 143.55306726089543
    '3': 182.47696869722728
    '4': 251.8926161804434
    '5': 78.85450344067841
    '6': 452.28512838279204
    '7': 230.18877137925128
    '8': 133.51245385181636
  policy_reward_mean:
    '1': 363.6783517815522
    '2': 106.26563522577484
    '3': 153.6572151075914
    '4': 211.57684798985056
    '5': 68.3794437598109
    '6': 356.3992972370709
    '7': 195.14267987895073
    '8': 103.73791734361117
  policy_reward_min:
    '1': 283.40745575495407
    '2': 61.864755269548986
    '3': 120.52432292406034
    '4': 191.40531864333056
    '5': 48.12872630565207
    '6': 337.73777161556336
    '7': 146.97510892107118
    '8': 62.294811744098716
  sampler_perf:
    mean_action_processing_ms: 0.22312158954677128
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.53297178740851
    mean_inference_ms: 6.579752023297995
    mean_raw_obs_processing_ms: 0.7634149716660406
  time_since_restore: 6336.569839477539
  time_this_iter_s: 142.61831617355347
  time_total_s: 6336.569839477539
  timers:
    learn_throughput: 126.893
    learn_time_ms: 31522.606
    load_throughput: 268826.006
    load_time_ms: 14.88
    sample_throughput: 35.934
    sample_time_ms: 111315.166
    update_time_ms: 14.262
  timestamp: 1651210987
  timesteps_since_restore: 0
  timesteps_total: 188000
  training_iteration: 47
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     47 |          6336.57 | 188000 |  1558.84 |              1639.57 |              1463.21 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1536000
  custom_metrics:
    eps_sum_utility_max: 1336.1225792125535
    eps_sum_utility_mean: 1263.6754629152958
    eps_sum_utility_min: 1072.307307235001
    sum_utility_max: 27.839971222164372
    sum_utility_mean: 23.45125760338101
    sum_utility_min: 7.796092479504731
  date: 2022-04-29_11-15-31
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1676.4242879186359
  episode_reward_mean: 1563.248270546761
  episode_reward_min: 1436.084469964529
  episodes_this_iter: 40
  episodes_total: 1920
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.3375000059604645
          cur_lr: 4.999999873689376e-05
          entropy: 1.5171735286712646
          entropy_coeff: 0.0
          kl: 0.005963982082903385
          model: {}
          policy_loss: -0.010396518744528294
          total_loss: 3580.327392578125
          vf_explained_var: -3.845460838647341e-09
          vf_loss: 3580.33642578125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1490062475204468
          entropy_coeff: 0.0
          kl: 0.01081238966435194
          model: {}
          policy_loss: -0.017969688400626183
          total_loss: 65.99198150634766
          vf_explained_var: 0.8959947228431702
          vf_loss: 66.00670623779297
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.365221619606018
          entropy_coeff: 0.0
          kl: 0.010308689437806606
          model: {}
          policy_loss: -0.012727578170597553
          total_loss: 74.35822296142578
          vf_explained_var: 0.9361609816551208
          vf_loss: 74.36786651611328
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.1834533214569092
          entropy_coeff: 0.0
          kl: 0.007496600970625877
          model: {}
          policy_loss: -0.01680128648877144
          total_loss: 19.546607971191406
          vf_explained_var: 0.9678590297698975
          vf_loss: 19.56171989440918
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.321638584136963
          entropy_coeff: 0.0
          kl: 0.0056269196793437
          model: {}
          policy_loss: -0.008853886276483536
          total_loss: 10.583901405334473
          vf_explained_var: 0.9707502722740173
          vf_loss: 10.59022331237793
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.3955267667770386
          entropy_coeff: 0.0
          kl: 0.009997555986046791
          model: {}
          policy_loss: -0.014202420599758625
          total_loss: 223.19415283203125
          vf_explained_var: 0.9378616809844971
          vf_loss: 223.2061004638672
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 0.8960696458816528
          entropy_coeff: 0.0
          kl: 0.007749516516923904
          model: {}
          policy_loss: -0.012156963348388672
          total_loss: 144.07334899902344
          vf_explained_var: 0.9124432802200317
          vf_loss: 144.0831756591797
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3222949504852295
          entropy_coeff: 0.0
          kl: 0.005207646172493696
          model: {}
          policy_loss: -0.011687188409268856
          total_loss: 91.0242691040039
          vf_explained_var: 0.9397088885307312
          vf_loss: 91.03363037109375
    num_agent_steps_sampled: 1536000
    num_agent_steps_trained: 1536000
    num_steps_sampled: 192000
    num_steps_trained: 192000
  iterations_since_restore: 48
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.70567010309278
    ram_util_percent: 56.925257731958766
  pid: 3846
  policy_reward_max:
    '1': 386.68440392793696
    '2': 143.55306726089543
    '3': 193.98198798474579
    '4': 251.8926161804434
    '5': 91.88475343745938
    '6': 460.21298136763187
    '7': 230.18877137925128
    '8': 155.23365778314536
  policy_reward_mean:
    '1': 366.0682671788198
    '2': 108.45499318730103
    '3': 155.08073315915487
    '4': 211.30483364366307
    '5': 68.51014580564883
    '6': 354.4026062386528
    '7': 193.76854625736422
    '8': 105.65814507615546
  policy_reward_min:
    '1': 265.29920819107014
    '2': 61.864755269548986
    '3': 116.7698042663714
    '4': 188.8873679211469
    '5': 58.409880820470846
    '6': 334.5706441057588
    '7': 153.95883050671486
    '8': 67.00663143086432
  sampler_perf:
    mean_action_processing_ms: 0.22346894240453302
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.59976500748857
    mean_inference_ms: 6.588791210424886
    mean_raw_obs_processing_ms: 0.7645158354655363
  time_since_restore: 6480.8607006073
  time_this_iter_s: 144.29086112976074
  time_total_s: 6480.8607006073
  timers:
    learn_throughput: 127.012
    learn_time_ms: 31493.013
    load_throughput: 277318.523
    load_time_ms: 14.424
    sample_throughput: 35.884
    sample_time_ms: 111470.688
    update_time_ms: 14.185
  timestamp: 1651211131
  timesteps_since_restore: 0
  timesteps_total: 192000
  training_iteration: 48
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     48 |          6480.86 | 192000 |  1563.25 |              1676.42 |              1436.08 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1568000
  custom_metrics:
    eps_sum_utility_max: 1322.9170423993212
    eps_sum_utility_mean: 1264.5723406071947
    eps_sum_utility_min: 1072.307307235001
    sum_utility_max: 28.138185844743898
    sum_utility_mean: 22.813379567489804
    sum_utility_min: 1.8669243902470316
  date: 2022-04-29_11-17-53
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1676.4242879186359
  episode_reward_mean: 1573.8893619482028
  episode_reward_min: 1436.084469964529
  episodes_this_iter: 40
  episodes_total: 1960
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.3375000059604645
          cur_lr: 4.999999873689376e-05
          entropy: 1.4975320100784302
          entropy_coeff: 0.0
          kl: 0.010955046862363815
          model: {}
          policy_loss: -0.018154647201299667
          total_loss: 3699.71240234375
          vf_explained_var: -1.1536382515942023e-08
          vf_loss: 3699.72705078125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1342767477035522
          entropy_coeff: 0.0
          kl: 0.009416264481842518
          model: {}
          policy_loss: -0.011976204812526703
          total_loss: 65.07121276855469
          vf_explained_var: 0.8938159942626953
          vf_loss: 65.08036804199219
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3279168605804443
          entropy_coeff: 0.0
          kl: 0.007648470811545849
          model: {}
          policy_loss: -0.016179487109184265
          total_loss: 44.62160873413086
          vf_explained_var: 0.9605759978294373
          vf_loss: 44.635494232177734
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.1081924438476562
          entropy_coeff: 0.0
          kl: 0.010507195256650448
          model: {}
          policy_loss: -0.014823367819190025
          total_loss: 5.471224308013916
          vf_explained_var: 0.991431713104248
          vf_loss: 5.483683109283447
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3200416564941406
          entropy_coeff: 0.0
          kl: 0.007030002307146788
          model: {}
          policy_loss: -0.01189412735402584
          total_loss: 7.7616472244262695
          vf_explained_var: 0.9791833162307739
          vf_loss: 7.770376682281494
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.411995768547058
          entropy_coeff: 0.0
          kl: 0.008240881375968456
          model: {}
          policy_loss: -0.010327075608074665
          total_loss: 288.5079345703125
          vf_explained_var: 0.9194400906562805
          vf_loss: 288.5163879394531
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 0.9132349491119385
          entropy_coeff: 0.0
          kl: 0.009254498407244682
          model: {}
          policy_loss: -0.014675434678792953
          total_loss: 83.11841583251953
          vf_explained_var: 0.9613345265388489
          vf_loss: 83.13031005859375
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.322476863861084
          entropy_coeff: 0.0
          kl: 0.006335917394608259
          model: {}
          policy_loss: -0.014409744180738926
          total_loss: 37.90279006958008
          vf_explained_var: 0.9745010137557983
          vf_loss: 37.914344787597656
    num_agent_steps_sampled: 1568000
    num_agent_steps_trained: 1568000
    num_steps_sampled: 196000
    num_steps_trained: 196000
  iterations_since_restore: 49
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.39736842105264
    ram_util_percent: 56.90052631578948
  pid: 3846
  policy_reward_max:
    '1': 386.68440392793696
    '2': 143.55306726089543
    '3': 193.98198798474579
    '4': 251.8926161804434
    '5': 91.88475343745938
    '6': 460.21298136763187
    '7': 237.85356886060802
    '8': 155.23365778314536
  policy_reward_mean:
    '1': 367.55210040631545
    '2': 110.09837683014497
    '3': 155.38949123398822
    '4': 212.06795433295738
    '5': 69.17974991961124
    '6': 355.86423221639643
    '7': 197.41294235041573
    '8': 106.32451465837252
  policy_reward_min:
    '1': 265.29920819107014
    '2': 60.06396212824387
    '3': 116.7698042663714
    '4': 188.8873679211469
    '5': 58.787854842989006
    '6': 334.5706441057588
    '7': 153.95883050671486
    '8': 67.00663143086432
  sampler_perf:
    mean_action_processing_ms: 0.2237715628641683
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.65823022508228
    mean_inference_ms: 6.596804033046897
    mean_raw_obs_processing_ms: 0.7654680302014163
  time_since_restore: 6622.029549360275
  time_this_iter_s: 141.16884875297546
  time_total_s: 6622.029549360275
  timers:
    learn_throughput: 126.863
    learn_time_ms: 31530.08
    load_throughput: 276084.544
    load_time_ms: 14.488
    sample_throughput: 35.928
    sample_time_ms: 111334.934
    update_time_ms: 14.158
  timestamp: 1651211273
  timesteps_since_restore: 0
  timesteps_total: 196000
  training_iteration: 49
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.4/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     49 |          6622.03 | 196000 |  1573.89 |              1676.42 |              1436.08 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_572f4_00000:
  agent_timesteps_total: 1600000
  custom_metrics:
    eps_sum_utility_max: 1323.852645445427
    eps_sum_utility_mean: 1274.6861093194148
    eps_sum_utility_min: 1072.307307235001
    sum_utility_max: 28.138185844743898
    sum_utility_mean: 23.090828538277894
    sum_utility_min: 1.8669243902470316
  date: 2022-04-29_11-20-22
  done: true
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1689.1098601658514
  episode_reward_mean: 1585.2477271184378
  episode_reward_min: 1399.481887117299
  episodes_this_iter: 40
  episodes_total: 2000
  experiment_id: 4e83bae06b244c1a89c798d7bfc8a630
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.3375000059604645
          cur_lr: 4.999999873689376e-05
          entropy: 1.5389344692230225
          entropy_coeff: 0.0
          kl: 0.030157912522554398
          model: {}
          policy_loss: -0.041824501007795334
          total_loss: 3410.517578125
          vf_explained_var: -1.1536382515942023e-08
          vf_loss: 3410.548828125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.1168326139450073
          entropy_coeff: 0.0
          kl: 0.010305293835699558
          model: {}
          policy_loss: -0.013624992221593857
          total_loss: 50.2540283203125
          vf_explained_var: 0.9205642938613892
          vf_loss: 50.264564514160156
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.3022147417068481
          entropy_coeff: 0.0
          kl: 0.009057186543941498
          model: {}
          policy_loss: -0.014089059084653854
          total_loss: 47.05484390258789
          vf_explained_var: 0.9588812589645386
          vf_loss: 47.06621551513672
      '4':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.0759708881378174
          entropy_coeff: 0.0
          kl: 0.0069760470651090145
          model: {}
          policy_loss: -0.01296949852257967
          total_loss: 8.999812126159668
          vf_explained_var: 0.9854521155357361
          vf_loss: 9.011212348937988
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.3216804265975952
          entropy_coeff: 0.0
          kl: 0.006909511052072048
          model: {}
          policy_loss: -0.013044035993516445
          total_loss: 14.912623405456543
          vf_explained_var: 0.9600124359130859
          vf_loss: 14.922557830810547
      '6':
        learner_stats:
          cur_kl_coeff: 0.22499999403953552
          cur_lr: 4.999999873689376e-05
          entropy: 1.3707704544067383
          entropy_coeff: 0.0
          kl: 0.01388288103044033
          model: {}
          policy_loss: -0.017561983317136765
          total_loss: 10.608091354370117
          vf_explained_var: 0.9967889189720154
          vf_loss: 10.622528076171875
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 0.9018644690513611
          entropy_coeff: 0.0
          kl: 0.006492088548839092
          model: {}
          policy_loss: -0.014746779575943947
          total_loss: 78.7818832397461
          vf_explained_var: 0.9577999711036682
          vf_loss: 78.794677734375
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.312682867050171
          entropy_coeff: 0.0
          kl: 0.0061612860299646854
          model: {}
          policy_loss: -0.009685767814517021
          total_loss: 57.19818878173828
          vf_explained_var: 0.962090790271759
          vf_loss: 57.20510482788086
    num_agent_steps_sampled: 1600000
    num_agent_steps_trained: 1600000
    num_steps_sampled: 200000
    num_steps_trained: 200000
  iterations_since_restore: 50
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 37.1595
    ram_util_percent: 56.90700000000001
  pid: 3846
  policy_reward_max:
    '1': 384.29995977605176
    '2': 138.3300942009352
    '3': 193.98198798474579
    '4': 222.88374729178682
    '5': 79.13504619865553
    '6': 460.21298136763187
    '7': 237.85356886060802
    '8': 143.8668755055307
  policy_reward_mean:
    '1': 371.0131085444997
    '2': 112.24490912064046
    '3': 157.09754720453452
    '4': 211.98356808892188
    '5': 69.10909830294776
    '6': 353.4562886928338
    '7': 201.88997634694257
    '8': 108.45323081711688
  policy_reward_min:
    '1': 265.29920819107014
    '2': 60.06396212824387
    '3': 117.6765401549316
    '4': 194.58005646828153
    '5': 34.556974000318235
    '6': 335.8279349789861
    '7': 155.97887953654853
    '8': 50.65363256625423
  sampler_perf:
    mean_action_processing_ms: 0.22405974802502499
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 44.71309557525803
    mean_inference_ms: 6.604274758747541
    mean_raw_obs_processing_ms: 0.766357913888832
  time_since_restore: 6770.897191286087
  time_this_iter_s: 148.86764192581177
  time_total_s: 6770.897191286087
  timers:
    learn_throughput: 124.584
    learn_time_ms: 32106.755
    load_throughput: 275913.371
    load_time_ms: 14.497
    sample_throughput: 35.919
    sample_time_ms: 111361.379
    update_time_ms: 14.557
  timestamp: 1651211422
  timesteps_since_restore: 0
  timesteps_total: 200000
  training_iteration: 50
  trial_id: 572f4_00000
  
== Status ==
Memory usage on this node: 4.3/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc             |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | RUNNING  | 10.0.3.106:3846 |     50 |           6770.9 | 200000 |  1585.25 |              1689.11 |              1399.48 |                100 |
+-------------------------------------+----------+-----------------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


== Status ==
Memory usage on this node: 3.2/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/3.86 GiB heap, 0.0/1.93 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25
Number of trials: 1/1 (1 TERMINATED)
+-------------------------------------+------------+-------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status     | loc   |   iter |   total time (s) |     ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+------------+-------+--------+------------------+--------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_572f4_00000 | TERMINATED |       |     50 |           6770.9 | 200000 |  1585.25 |              1689.11 |              1399.48 |                100 |
+-------------------------------------+------------+-------+--------+------------------+--------+----------+----------------------+----------------------+--------------------+


2022-04-29 11:20:23,008	INFO tune.py:549 -- Total run time: 6837.69 seconds (6836.87 seconds for the tuning loop).
INFO:deepcomp.util.simulation:Training done                  episode_reward_mean=1585.248 episodes_total=2000 log_dir=/home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25/PPO_MultiAgentMobileEnv_572f4_00000_0_2022-04-29_09-26-26 num_steps_sampled=200000 num_steps_trained=200000 timesteps_total=200000
2022-04-29 11:20:23,288	INFO trainer.py:671 -- Tip: set framework=tfe or the --eager flag to enable TensorFlow eager execution
2022-04-29 11:20:23,288	WARNING deprecation.py:33 -- DeprecationWarning: `monitor` has been deprecated. Use `record_env` instead. This will raise an error in the future!
2022-04-29 11:20:23,288	INFO trainer.py:696 -- Current log_level is ERROR. For more information, set 'log_level': 'INFO' / 'DEBUG' or use the -v and -vv flags.
2022-04-29 11:21:38,508	INFO trainable.py:101 -- Trainable.setup took 75.243 seconds. If your trainable is slow to initialize, consider setting reuse_actors=True to reduce actor creation overheads.
INFO:deepcomp.util.simulation:Loading PPO agent              checkpoint=/home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25/PPO_MultiAgentMobileEnv_572f4_00000_0_2022-04-29_09-26-26/checkpoint_000050/checkpoint-50
2022-04-29 11:21:42,714	INFO trainable.py:377 -- Restored on 10.0.3.106 from checkpoint: /home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25/PPO_MultiAgentMobileEnv_572f4_00000_0_2022-04-29_09-26-26/checkpoint_000050/checkpoint-50
2022-04-29 11:21:42,715	INFO trainable.py:385 -- Current state after restoring: {'_iteration': 50, '_timesteps_total': None, '_time_total': 6770.897191286087, '_episodes_total': 2000}
INFO:deepcomp.util.simulation:Agent loaded                   agent=PPO checkpoint=None rllib_dir=/home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25/PPO_MultiAgentMobileEnv_572f4_00000_0_2022-04-29_09-26-26/checkpoint_000050/checkpoint-50
INFO:deepcomp.util.simulation:Loaded training progress       progress_file=/home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25/PPO_MultiAgentMobileEnv_572f4_00000_0_2022-04-29_09-26-26/progress.csv train_iteration=50 train_steps=200000
WARNING:deepcomp.util.simulation:Evaluating with a single worker for reproducibility and compatibility.
INFO:deepcomp.util.simulation:Starting evaluation            fast_ues=2 num_episodes=1 num_workers=1 slow_ues=5 static_ues=1
DEBUG:deepcomp.util.simulation:Step                           action={'1': 6, '2': 3, '3': 2, '4': 6, '5': 3, '6': 5, '7': 1, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.09], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.048, 1.0, 0.01, 0.002, 0.002, 0.004], 'utility': [0.125], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.004, 0.04], 'utility': [0.372], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.003, 1.0, 0.011], 'utility': [0.173], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.016, 1.0, 0.025, 0.004, 0.002, 0.003], 'utility': [0.162], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.03, 0.071, 0.584, 0.654, 0.076, 0.031], 'utility': [-0.178], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.004, 0.008, 0.016, 0.016], 'utility': [0.499], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.028, 0.009, 0.077, 1.0, 0.025, 0.006, 0.005], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.014, 0.044, 1.0, 0.01, 0.002, 0.002, 0.004], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.008, 0.002, 0.002, 0.003, 0.035], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.014], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '5': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.039, 0.016, 1.0, 0.029, 0.004, 0.002, 0.003], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '6': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.034, 0.083, 0.787, 0.714, 0.079, 0.033], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.013, 0.007, 0.009, 0.02, 0.055, 0.04], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '8': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.031, 0.011, 0.081, 1.0, 0.029, 0.007, 0.005], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}} reward={'1': 2.624, '2': 2.867, '3': 7.436, '4': 2.624, '5': 2.867, '6': 1.874, '7': 9.979, '8': -0.796} t=1
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 5, '3': 7, '4': 7, '5': 6, '6': 6, '7': 4, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.247], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.016, 0.053, 1.0, 0.01, 0.003, 0.002, 0.004], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.024, 1.0, 0.009, 0.002, 0.002, 0.004, 0.046], 'utility': [0.349], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.009], 'utility': [0.576], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.016, 1.0, 0.021, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.027, 0.06, 0.438, 0.595, 0.073, 0.029], 'utility': [-0.171], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.003, 0.002, 0.002, 0.002, 0.004, 0.005], 'utility': [0.717], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.026, 0.008, 0.075, 1.0, 0.021, 0.005, 0.004], 'utility': [0.002], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.09], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.048, 1.0, 0.01, 0.002, 0.002, 0.004], 'utility': [0.125], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.004, 0.04], 'utility': [0.372], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.003, 1.0, 0.011], 'utility': [0.173], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.016, 1.0, 0.025, 0.004, 0.002, 0.003], 'utility': [0.162], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.03, 0.071, 0.584, 0.654, 0.076, 0.031], 'utility': [-0.178], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.004, 0.008, 0.016, 0.016], 'utility': [0.499], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.028, 0.009, 0.077, 1.0, 0.025, 0.006, 0.005], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}} reward={'1': 3.289, '2': 2.968, '3': 6.99, '4': 3.289, '5': 2.968, '6': 3.658, '7': 14.337, '8': 0.048} t=2
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 7, '3': 7, '4': 7, '5': 6, '6': 6, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.057], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.017, 0.059, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.027, 1.0, 0.01, 0.003, 0.002, 0.004, 0.053], 'utility': [0.328], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.003, 1.0, 0.008], 'utility': [0.372], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.016, 1.0, 0.019, 0.003, 0.002, 0.003], 'utility': [0.212], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.052, 0.331, 0.538, 0.07, 0.027], 'utility': [-0.165], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.897], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.074, 1.0, 0.018, 0.005, 0.004], 'utility': [0.04], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.247], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.016, 0.053, 1.0, 0.01, 0.003, 0.002, 0.004], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.024, 1.0, 0.009, 0.002, 0.002, 0.004, 0.046], 'utility': [0.349], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.009], 'utility': [0.576], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.016, 1.0, 0.021, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.027, 0.06, 0.438, 0.595, 0.073, 0.029], 'utility': [-0.171], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.003, 0.002, 0.002, 0.002, 0.004, 0.005], 'utility': [0.717], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.026, 0.008, 0.075, 1.0, 0.021, 0.005, 0.004], 'utility': [0.002], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.717, 0.349, 0.148, 0.002, -0.171, 0.164, 0.0]}} reward={'1': 4.291, '2': 3.087, '3': 6.553, '4': 4.291, '5': 3.087, '6': 5.153, '7': 17.949, '8': 0.808} t=3
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 7, '3': 7, '4': 7, '5': 6, '6': 6, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.149], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.019, 0.067, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.012], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.011, 0.003, 0.002, 0.005, 0.061], 'utility': [0.306], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.614], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.017, 1.0, 0.017, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.022, 0.044, 0.253, 0.485, 0.068, 0.026], 'utility': [-0.161], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.878], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.076, 1.0, 0.016, 0.004, 0.003], 'utility': [0.072], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.057], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.017, 0.059, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.027, 1.0, 0.01, 0.003, 0.002, 0.004, 0.053], 'utility': [0.328], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.003, 1.0, 0.008], 'utility': [0.372], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.016, 1.0, 0.019, 0.003, 0.002, 0.003], 'utility': [0.212], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.052, 0.331, 0.538, 0.07, 0.027], 'utility': [-0.165], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.897], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.074, 1.0, 0.018, 0.005, 0.004], 'utility': [0.04], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.897, 0.328, 0.154, 0.04, -0.165, 0.215, 0.0]}} reward={'1': 4.652, '2': 3.056, '3': 6.125, '4': 4.652, '5': 3.056, '6': 7.164, '7': 17.551, '8': 1.444} t=4
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 7, '3': 7, '4': 7, '5': 6, '6': 6, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.033], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.077, 1.0, 0.012, 0.003, 0.002, 0.006], 'utility': [0.064], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.07], 'utility': [0.285], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.006], 'utility': [0.481], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.018, 1.0, 0.016, 0.003, 0.002, 0.003], 'utility': [0.236], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.02, 0.038, 0.196, 0.435, 0.067, 0.024], 'utility': [-0.159], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.003, 0.002, 0.002, 0.004], 'utility': [0.681], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.082, 1.0, 0.015, 0.004, 0.003], 'utility': [0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.149], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.019, 0.067, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.012], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.011, 0.003, 0.002, 0.005, 0.061], 'utility': [0.306], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.614], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.017, 1.0, 0.017, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.022, 0.044, 0.253, 0.485, 0.068, 0.026], 'utility': [-0.161], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.878], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.076, 1.0, 0.016, 0.004, 0.003], 'utility': [0.072], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.878, 0.306, 0.153, 0.072, -0.161, 0.233, 0.0]}} reward={'1': 5.139, '2': 3.003, '3': 5.705, '4': 5.139, '5': 3.003, '6': 5.219, '7': 13.623, '8': 1.915} t=5
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 5, '3': 7, '4': 7, '5': 6, '6': 6, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.089, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.04, 1.0, 0.013, 0.004, 0.003, 0.006, 0.08], 'utility': [0.281], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.629], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.02, 1.0, 0.015, 0.003, 0.002, 0.003], 'utility': [0.282], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.019, 0.033, 0.153, 0.389, 0.066, 0.023], 'utility': [-0.16], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.022, 0.016, 0.007, 0.004, 0.005, 0.01], 'utility': [0.466], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.093, 1.0, 0.014, 0.004, 0.003], 'utility': [0.109], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.033], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.077, 1.0, 0.012, 0.003, 0.002, 0.006], 'utility': [0.064], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.07], 'utility': [0.285], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.006], 'utility': [0.481], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.018, 1.0, 0.016, 0.003, 0.002, 0.003], 'utility': [0.236], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.02, 0.038, 0.196, 0.435, 0.067, 0.024], 'utility': [-0.159], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.003, 0.002, 0.002, 0.004], 'utility': [0.681], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.082, 1.0, 0.015, 0.004, 0.003], 'utility': [0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.681, 0.285, 0.15, 0.096, -0.159, 0.257, 0.0]}} reward={'1': 5.327, '2': 2.847, '3': 5.63, '4': 5.327, '5': 2.847, '6': 3.065, '7': 9.32, '8': 2.183} t=6
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 5, '3': 4, '4': 7, '5': 6, '6': 1, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.017], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.104, 1.0, 0.013, 0.004, 0.003, 0.007], 'utility': [0.028], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.045, 1.0, 0.014, 0.004, 0.003, 0.007, 0.092], 'utility': [0.264], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.53], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.022, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.237], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.028, 0.122, 0.349, 0.066, 0.023], 'utility': [0.031], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.052, 0.017, 0.009, 0.009, 0.019], 'utility': [0.13], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.027, 0.008, 0.113, 1.0, 0.015, 0.004, 0.004], 'utility': [0.111], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.096], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.089, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.04, 1.0, 0.013, 0.004, 0.003, 0.006, 0.08], 'utility': [0.281], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.629], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.02, 1.0, 0.015, 0.003, 0.002, 0.003], 'utility': [0.282], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.019, 0.033, 0.153, 0.389, 0.066, 0.023], 'utility': [-0.16], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.022, 0.016, 0.007, 0.004, 0.005, 0.01], 'utility': [0.466], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.093, 1.0, 0.014, 0.004, 0.003], 'utility': [0.109], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.466, 0.281, 0.142, 0.109, -0.16, 0.266, 0.281]}} reward={'1': 5.466, '2': 2.651, '3': 5.273, '4': 5.466, '5': 2.651, '6': 1.286, '7': 1.615, '8': 2.225} t=7
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 5, '3': 1, '4': 7, '5': 6, '6': 2, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.123, 1.0, 0.014, 0.004, 0.003, 0.008], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.051, 1.0, 0.016, 0.004, 0.004, 0.008, 0.105], 'utility': [0.247], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.61], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.025, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.256], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.016, 0.025, 0.098, 0.314, 0.067, 0.022], 'utility': [0.041], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.149, 0.15, 0.036, 0.016, 0.015, 0.033], 'utility': [-0.025], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.032, 0.01, 0.146, 1.0, 0.016, 0.004, 0.004], 'utility': [0.102], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.017], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.104, 1.0, 0.013, 0.004, 0.003, 0.007], 'utility': [0.028], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.045, 1.0, 0.014, 0.004, 0.003, 0.007, 0.092], 'utility': [0.264], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.53], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.022, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.237], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.028, 0.122, 0.349, 0.066, 0.023], 'utility': [0.031], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.052, 0.017, 0.009, 0.009, 0.019], 'utility': [0.13], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.027, 0.008, 0.113, 1.0, 0.015, 0.004, 0.004], 'utility': [0.111], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}} reward={'1': 5.47, '2': 2.384, '3': 4.93, '4': 5.47, '5': 2.384, '6': 0.384, '7': 2.006, '8': 2.037} t=8
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 5, '3': 1, '4': 7, '5': 6, '6': 2, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.147, 1.0, 0.015, 0.004, 0.004, 0.009], 'utility': [-0.011], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.057, 1.0, 0.017, 0.005, 0.004, 0.009, 0.119], 'utility': [0.23], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.526], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.029, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.218], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.022, 0.081, 0.283, 0.069, 0.022], 'utility': [0.049], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.31, 0.401, 0.064, 0.025, 0.022, 0.05], 'utility': [-0.155], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.039, 0.012, 0.201, 1.0, 0.017, 0.005, 0.005], 'utility': [0.082], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.123, 1.0, 0.014, 0.004, 0.003, 0.008], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.051, 1.0, 0.016, 0.004, 0.004, 0.008, 0.105], 'utility': [0.247], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.61], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.025, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.256], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.016, 0.025, 0.098, 0.314, 0.067, 0.022], 'utility': [0.041], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.149, 0.15, 0.036, 0.016, 0.015, 0.033], 'utility': [-0.025], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.032, 0.01, 0.146, 1.0, 0.016, 0.004, 0.004], 'utility': [0.102], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}} reward={'1': 5.335, '2': 2.917, '3': 4.601, '4': 5.335, '5': 2.075, '6': -0.384, '7': 1.324, '8': 1.928} t=9
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 5, '3': 1, '4': 7, '5': 6, '6': 2, '7': 3, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.176, 1.0, 0.017, 0.005, 0.004, 0.01], 'utility': [-0.105], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.064, 1.0, 0.019, 0.005, 0.005, 0.01, 0.136], 'utility': [0.214], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.558], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.034, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.161], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.02, 0.068, 0.258, 0.073, 0.022], 'utility': [0.054], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.986, 0.559, 1.0, 0.103, 0.035, 0.031, 0.07], 'utility': [-0.197], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.05, 0.015, 0.291, 1.0, 0.02, 0.006, 0.006], 'utility': [0.056], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.147, 1.0, 0.015, 0.004, 0.004, 0.009], 'utility': [-0.011], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.057, 1.0, 0.017, 0.005, 0.004, 0.009, 0.119], 'utility': [0.23], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.526], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.029, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.218], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.022, 0.081, 0.283, 0.069, 0.022], 'utility': [0.049], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.31, 0.401, 0.064, 0.025, 0.022, 0.05], 'utility': [-0.155], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.039, 0.012, 0.201, 1.0, 0.017, 0.005, 0.005], 'utility': [0.082], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}} reward={'1': 5.156, '2': 0.511, '3': 4.286, '4': 5.156, '5': -0.433, '6': -0.592, '7': -0.044, '8': -0.124} t=10
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 5, '3': 1, '4': 7, '5': 6, '6': 3, '7': 4, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.001], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.041, 0.213, 1.0, 0.018, 0.005, 0.005, 0.011], 'utility': [-0.147], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.072, 1.0, 0.02, 0.006, 0.005, 0.011, 0.154], 'utility': [0.199], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.0, 0.001, 0.004, 1.0, 0.006], 'utility': [0.483], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.039, 0.04, 1.0, 0.014, 0.003, 0.002, 0.005], 'utility': [0.09], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.019, 0.058, 0.237, 0.078, 0.023], 'utility': [0.057], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.402, 0.371, 1.0, 0.063, 0.019, 0.017, 0.038], 'utility': [-0.166], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.067, 0.02, 0.442, 1.0, 0.023, 0.008, 0.007], 'utility': [0.022], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.176, 1.0, 0.017, 0.005, 0.004, 0.01], 'utility': [-0.105], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.064, 1.0, 0.019, 0.005, 0.005, 0.01, 0.136], 'utility': [0.214], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.558], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.034, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.161], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.02, 0.068, 0.258, 0.073, 0.022], 'utility': [0.054], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.986, 0.559, 1.0, 0.103, 0.035, 0.031, 0.07], 'utility': [-0.197], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.05, 0.015, 0.291, 1.0, 0.02, 0.006, 0.006], 'utility': [0.056], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.072, 0.214, -0.022, 0.056, 0.054, 0.258, 0.214]}} reward={'1': 4.839, '2': -0.011, '3': 3.985, '4': 4.839, '5': -1.01, '6': -0.351, '7': -0.321, '8': -0.722} t=11
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 5, '3': 1, '4': 7, '5': 6, '6': 3, '7': 4, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.029], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.047, 0.259, 1.0, 0.02, 0.006, 0.005, 0.013], 'utility': [-0.236], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 1.0, 0.022, 0.006, 0.006, 0.013, 0.174], 'utility': [0.185], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.001, 0.001, 0.001, 0.005, 1.0, 0.007], 'utility': [0.481], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.048, 1.0, 0.015, 0.003, 0.003, 0.005], 'utility': [0.019], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.018, 0.051, 0.221, 0.086, 0.024], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.167, 0.227, 1.0, 0.037, 0.011, 0.009, 0.02], 'utility': [-0.085], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.091, 0.027, 0.695, 1.0, 0.028, 0.009, 0.009], 'utility': [-0.017], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.001], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.041, 0.213, 1.0, 0.018, 0.005, 0.005, 0.011], 'utility': [-0.147], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.072, 1.0, 0.02, 0.006, 0.005, 0.011, 0.154], 'utility': [0.199], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.0, 0.001, 0.004, 1.0, 0.006], 'utility': [0.483], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.039, 0.04, 1.0, 0.014, 0.003, 0.002, 0.005], 'utility': [0.09], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.019, 0.058, 0.237, 0.078, 0.023], 'utility': [0.057], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.402, 0.371, 1.0, 0.063, 0.019, 0.017, 0.038], 'utility': [-0.166], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.067, 0.02, 0.442, 1.0, 0.023, 0.008, 0.007], 'utility': [0.022], 'ues_at_bs': [0.25, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.055, 0.199, -0.051, 0.022, 0.057, 0.242, 0.199]}} reward={'1': 4.524, '2': -0.534, '3': 3.698, '4': 4.524, '5': -1.592, '6': 3.415, '7': -0.534, '8': -1.34} t=12
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 7, '3': 4, '4': 7, '5': 6, '6': 3, '7': 4, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.003], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.054, 0.317, 1.0, 0.021, 0.006, 0.006, 0.015], 'utility': [-0.205], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.089, 1.0, 0.023, 0.007, 0.006, 0.014, 0.198], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.011, 0.001, 0.001, 0.001, 0.006, 1.0, 0.008], 'utility': [0.414], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.059, 1.0, 0.016, 0.004, 0.003, 0.006], 'utility': [0.03], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.017, 0.046, 0.209, 0.097, 0.026], 'utility': [0.169], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.072, 0.131, 1.0, 0.021, 0.006, 0.005, 0.01], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.112, 0.033, 1.0, 0.89, 0.031, 0.011, 0.011], 'utility': [-0.051], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.029], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.047, 0.259, 1.0, 0.02, 0.006, 0.005, 0.013], 'utility': [-0.236], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 1.0, 0.022, 0.006, 0.006, 0.013, 0.174], 'utility': [0.185], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.001, 0.001, 0.001, 0.005, 1.0, 0.007], 'utility': [0.481], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.048, 1.0, 0.015, 0.003, 0.003, 0.005], 'utility': [0.019], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.018, 0.051, 0.221, 0.086, 0.024], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.167, 0.227, 1.0, 0.037, 0.011, 0.009, 0.02], 'utility': [-0.085], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.091, 0.027, 0.695, 1.0, 0.028, 0.009, 0.009], 'utility': [-0.017], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.08, -0.017, 0.171, 0.226, 0.185]}} reward={'1': 4.113, '2': -0.44, '3': 3.427, '4': 4.113, '5': -1.407, '6': 3.372, '7': -0.44, '8': -1.327} t=13
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 7, '3': 4, '4': 7, '5': 6, '6': 3, '7': 7, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.061, 0.39, 1.0, 0.023, 0.007, 0.007, 0.017], 'utility': [-0.276], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.1, 1.0, 0.025, 0.008, 0.007, 0.016, 0.223], 'utility': [0.159], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.014, 0.001, 0.001, 0.001, 0.008, 1.0, 0.009], 'utility': [0.394], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.05, 0.072, 1.0, 0.017, 0.004, 0.003, 0.007], 'utility': [-0.034], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.043, 0.2, 0.112, 0.028], 'utility': [0.163], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.075, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.085], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.094, 0.028, 1.0, 0.539, 0.023, 0.008, 0.009], 'utility': [-0.073], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.003], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.054, 0.317, 1.0, 0.021, 0.006, 0.006, 0.015], 'utility': [-0.205], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.089, 1.0, 0.023, 0.007, 0.006, 0.014, 0.198], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.011, 0.001, 0.001, 0.001, 0.006, 1.0, 0.008], 'utility': [0.414], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.059, 1.0, 0.016, 0.004, 0.003, 0.006], 'utility': [0.03], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.017, 0.046, 0.209, 0.097, 0.026], 'utility': [0.169], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.072, 0.131, 1.0, 0.021, 0.006, 0.005, 0.01], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.112, 0.033, 1.0, 0.89, 0.031, 0.011, 0.011], 'utility': [-0.051], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, 0.171, -0.07, -0.051, 0.169, 0.206, 0.171]}} reward={'1': 3.724, '2': -0.559, '3': 3.171, '4': 3.724, '5': -1.491, '6': 3.254, '7': -0.559, '8': -1.485} t=14
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 7, '3': 4, '4': 7, '5': 6, '6': 3, '7': 7, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.007], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.071, 0.481, 1.0, 0.025, 0.008, 0.007, 0.02], 'utility': [-0.256], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.111, 1.0, 0.027, 0.008, 0.007, 0.017, 0.252], 'utility': [0.146], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.018, 0.002, 0.001, 0.002, 0.011, 1.0, 0.011], 'utility': [0.335], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.055, 0.089, 1.0, 0.018, 0.004, 0.004, 0.008], 'utility': [-0.029], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.04, 0.194, 0.132, 0.032], 'utility': [0.153], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.017], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.078, 0.024, 1.0, 0.323, 0.016, 0.006, 0.007], 'utility': [-0.068], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.061, 0.39, 1.0, 0.023, 0.007, 0.007, 0.017], 'utility': [-0.276], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.1, 1.0, 0.025, 0.008, 0.007, 0.016, 0.223], 'utility': [0.159], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.014, 0.001, 0.001, 0.001, 0.008, 1.0, 0.009], 'utility': [0.394], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.05, 0.072, 1.0, 0.017, 0.004, 0.003, 0.007], 'utility': [-0.034], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.043, 0.2, 0.112, 0.028], 'utility': [0.163], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.075, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.085], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.094, 0.028, 1.0, 0.539, 0.023, 0.008, 0.009], 'utility': [-0.073], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, 0.159, -0.075, -0.073, 0.163, 0.186, 0.159]}} reward={'1': 3.282, '2': -0.761, '3': 2.93, '4': 3.282, '5': -0.761, '6': 3.063, '7': -0.761, '8': -1.621} t=15
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 7, '3': 4, '4': 7, '5': 6, '6': 3, '7': 7, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.018], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.081, 0.596, 1.0, 0.028, 0.009, 0.008, 0.023], 'utility': [-0.321], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.123, 1.0, 0.029, 0.009, 0.008, 0.019, 0.284], 'utility': [0.135], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.002, 0.001, 0.002, 0.014, 1.0, 0.012], 'utility': [0.305], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.061, 0.11, 1.0, 0.019, 0.005, 0.004, 0.009], 'utility': [-0.092], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.016, 0.038, 0.191, 0.16, 0.036], 'utility': [0.14], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.056], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.065, 0.02, 1.0, 0.192, 0.012, 0.005, 0.006], 'utility': [-0.042], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.007], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.071, 0.481, 1.0, 0.025, 0.008, 0.007, 0.02], 'utility': [-0.256], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.111, 1.0, 0.027, 0.008, 0.007, 0.017, 0.252], 'utility': [0.146], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.018, 0.002, 0.001, 0.002, 0.011, 1.0, 0.011], 'utility': [0.335], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.055, 0.089, 1.0, 0.018, 0.004, 0.004, 0.008], 'utility': [-0.029], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.04, 0.194, 0.132, 0.032], 'utility': [0.153], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.017], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.078, 0.024, 1.0, 0.323, 0.016, 0.006, 0.007], 'utility': [-0.068], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, 0.146, -0.084, -0.068, 0.153, 0.164, 0.146]}} reward={'1': 2.867, '2': -1.057, '3': 2.704, '4': 2.867, '5': -1.057, '6': 2.804, '7': -1.057, '8': -1.766} t=16
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 2, '3': 4, '4': 7, '5': 6, '6': 3, '7': 7, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.093, 0.742, 1.0, 0.03, 0.01, 0.01, 0.027], 'utility': [-0.136], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.136, 1.0, 0.031, 0.01, 0.009, 0.021, 0.32], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.029, 0.003, 0.002, 0.003, 0.018, 1.0, 0.015], 'utility': [0.252], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.137, 1.0, 0.02, 0.005, 0.004, 0.01], 'utility': [-0.071], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.018, 0.017, 0.038, 0.19, 0.197, 0.042], 'utility': [0.124], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.047], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.017, 1.0, 0.116, 0.009, 0.004, 0.005], 'utility': [0.02], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.018], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.081, 0.596, 1.0, 0.028, 0.009, 0.008, 0.023], 'utility': [-0.321], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.123, 1.0, 0.029, 0.009, 0.008, 0.019, 0.284], 'utility': [0.135], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.002, 0.001, 0.002, 0.014, 1.0, 0.012], 'utility': [0.305], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.061, 0.11, 1.0, 0.019, 0.005, 0.004, 0.009], 'utility': [-0.092], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.016, 0.038, 0.191, 0.16, 0.036], 'utility': [0.14], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.056], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.065, 0.02, 1.0, 0.192, 0.012, 0.005, 0.006], 'utility': [-0.042], 'ues_at_bs': [0.125, 0.125, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, 0.135, -0.1, -0.042, 0.14, 0.143, 0.135]}} reward={'1': 2.429, '2': -1.025, '3': -1.337, '4': 2.429, '5': -1.025, '6': 2.456, '7': -1.025, '8': -0.477} t=17
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 5, '4': 7, '5': 6, '6': 0, '7': 7, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.106, 0.928, 1.0, 0.033, 0.011, 0.011, 0.031], 'utility': [-0.126], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.151, 1.0, 0.033, 0.011, 0.01, 0.023, 0.36], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.038, 0.003, 0.002, 0.004, 0.024, 1.0, 0.017], 'utility': [0.218], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.073, 0.172, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.119], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.02, 0.018, 0.038, 0.192, 0.247, 0.049], 'utility': [0.105], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.07, 0.177, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.242], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.045, 0.015, 1.0, 0.071, 0.006, 0.003, 0.004], 'utility': [0.096], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.093, 0.742, 1.0, 0.03, 0.01, 0.01, 0.027], 'utility': [-0.136], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.136, 1.0, 0.031, 0.01, 0.009, 0.021, 0.32], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.029, 0.003, 0.002, 0.003, 0.018, 1.0, 0.015], 'utility': [0.252], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.137, 1.0, 0.02, 0.005, 0.004, 0.01], 'utility': [-0.071], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.018, 0.017, 0.038, 0.19, 0.197, 0.042], 'utility': [0.124], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.047], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.017, 1.0, 0.116, 0.009, 0.004, 0.005], 'utility': [0.02], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.084, -0.035, 0.02, 0.124, 0.121, -0.032]}} reward={'1': 2.016, '2': -1.793, '3': -1.129, '4': 2.016, '5': -1.793, '6': 2.062, '7': -1.793, '8': -1.952} t=18
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 5, '4': 7, '5': 6, '6': 0, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.011], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.105, 1.0, 0.86, 0.031, 0.011, 0.011, 0.031], 'utility': [-0.122], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.167, 1.0, 0.035, 0.012, 0.011, 0.026, 0.404], 'utility': [-0.012], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.049, 0.004, 0.003, 0.005, 0.031, 1.0, 0.02], 'utility': [0.171], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.08, 0.215, 1.0, 0.023, 0.007, 0.006, 0.014], 'utility': [-0.113], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.022, 0.019, 0.038, 0.195, 0.314, 0.059], 'utility': [0.046], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.18, 0.471, 1.0, 0.039, 0.012, 0.011, 0.028], 'utility': [-0.267], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.026], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.106, 0.928, 1.0, 0.033, 0.011, 0.011, 0.031], 'utility': [-0.126], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.151, 1.0, 0.033, 0.011, 0.01, 0.023, 0.36], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.038, 0.003, 0.002, 0.004, 0.024, 1.0, 0.017], 'utility': [0.218], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.073, 0.172, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.119], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.02, 0.018, 0.038, 0.192, 0.247, 0.049], 'utility': [0.105], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.07, 0.177, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.242], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.045, 0.015, 1.0, 0.071, 0.006, 0.003, 0.004], 'utility': [0.096], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.105, -0.074, -0.098, 0.0, 0.105, 0.101, -0.022]}} reward={'1': 1.597, '2': -2.031, '3': -0.969, '4': 1.597, '5': -2.031, '6': 1.37, '7': -2.031, '8': -2.377} t=19
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 5, '4': 5, '5': 6, '6': 3, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.095, 1.0, 0.683, 0.027, 0.009, 0.009, 0.028], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.184, 1.0, 0.037, 0.013, 0.012, 0.029, 0.453], 'utility': [-0.002], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.062, 0.005, 0.003, 0.006, 0.04, 1.0, 0.023], 'utility': [0.136], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.088, 0.269, 1.0, 0.025, 0.007, 0.006, 0.016], 'utility': [-0.161], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.024, 0.02, 0.039, 0.2, 0.406, 0.071], 'utility': [0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.377, 1.0, 0.887, 0.057, 0.021, 0.02, 0.056], 'utility': [-0.435], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.087], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.011], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.105, 1.0, 0.86, 0.031, 0.011, 0.011, 0.031], 'utility': [-0.122], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.167, 1.0, 0.035, 0.012, 0.011, 0.026, 0.404], 'utility': [-0.012], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.049, 0.004, 0.003, 0.005, 0.031, 1.0, 0.02], 'utility': [0.171], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.08, 0.215, 1.0, 0.023, 0.007, 0.006, 0.014], 'utility': [-0.113], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.022, 0.019, 0.038, 0.195, 0.314, 0.059], 'utility': [0.046], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.18, 0.471, 1.0, 0.039, 0.012, 0.011, 0.028], 'utility': [-0.267], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.026], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.046, -0.067, -0.119, 0.0, 0.0, 0.08, -0.012]}} reward={'1': 1.2, '2': -2.505, '3': -0.828, '4': 1.2, '5': -2.505, '6': 0.948, '7': -2.084, '8': -3.147} t=20
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 5, '4': 5, '5': 6, '6': 3, '7': 2, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.013], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.54, 0.023, 0.008, 0.008, 0.026], 'utility': [-0.181], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.203, 1.0, 0.04, 0.014, 0.013, 0.031, 0.507], 'utility': [-0.038], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.078, 0.006, 0.004, 0.007, 0.052, 1.0, 0.026], 'utility': [0.093], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.096, 0.338, 1.0, 0.027, 0.008, 0.007, 0.018], 'utility': [-0.142], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.027, 0.021, 0.04, 0.206, 0.531, 0.086], 'utility': [-0.003], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.393, 1.0, 0.421, 0.042, 0.017, 0.019, 0.057], 'utility': [-0.215], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.069], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.095, 1.0, 0.683, 0.027, 0.009, 0.009, 0.028], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.184, 1.0, 0.037, 0.013, 0.012, 0.029, 0.453], 'utility': [-0.002], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.062, 0.005, 0.003, 0.006, 0.04, 1.0, 0.023], 'utility': [0.136], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.088, 0.269, 1.0, 0.025, 0.007, 0.006, 0.016], 'utility': [-0.161], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.024, 0.02, 0.039, 0.2, 0.406, 0.071], 'utility': [0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.377, 1.0, 0.887, 0.057, 0.021, 0.02, 0.056], 'utility': [-0.435], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.087], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [0.022, -0.061, -0.157, 0.0, 0.0, 0.06, -0.002]}} reward={'1': 0.807, '2': -2.583, '3': -2.362, '4': 0.807, '5': -2.583, '6': 0.517, '7': -2.268, '8': -2.348} t=21
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 5, '4': 5, '5': 6, '6': 3, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.077, 1.0, 0.426, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.176], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.224, 1.0, 0.042, 0.015, 0.014, 0.035, 0.567], 'utility': [-0.026], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.098, 0.007, 0.005, 0.009, 0.067, 1.0, 0.03], 'utility': [0.059], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.105, 0.424, 1.0, 0.028, 0.009, 0.008, 0.021], 'utility': [-0.176], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.031, 0.023, 0.042, 0.214, 0.702, 0.104], 'utility': [-0.03], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.438, 1.0, 0.232, 0.033, 0.016, 0.019, 0.065], 'utility': [-0.226], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.017, 1.0, 0.038, 0.005, 0.003, 0.004], 'utility': [0.168], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.013], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.54, 0.023, 0.008, 0.008, 0.026], 'utility': [-0.181], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.203, 1.0, 0.04, 0.014, 0.013, 0.031, 0.507], 'utility': [-0.038], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.078, 0.006, 0.004, 0.007, 0.052, 1.0, 0.026], 'utility': [0.093], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.096, 0.338, 1.0, 0.027, 0.008, 0.007, 0.018], 'utility': [-0.142], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.027, 0.021, 0.04, 0.206, 0.531, 0.086], 'utility': [-0.003], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.393, 1.0, 0.421, 0.042, 0.017, 0.019, 0.057], 'utility': [-0.215], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.069], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.003, -0.145, -0.117, 0.0, 0.0, 0.04, -0.038]}} reward={'1': 0.433, '2': -2.04, '3': -2.271, '4': 0.091, '5': -2.04, '6': 0.091, '7': -2.289, '8': -1.226} t=22
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 5, '4': 5, '5': 6, '6': 6, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.049], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.069, 1.0, 0.334, 0.017, 0.006, 0.007, 0.021], 'utility': [-0.17], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.246, 1.0, 0.044, 0.016, 0.015, 0.038, 0.633], 'utility': [-0.018], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.123, 0.008, 0.006, 0.011, 0.085, 1.0, 0.034], 'utility': [-0.015], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.114, 0.531, 1.0, 0.031, 0.01, 0.009, 0.024], 'utility': [-0.144], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.034, 0.025, 0.044, 0.222, 0.935, 0.128], 'utility': [-0.028], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.529, 1.0, 0.152, 0.029, 0.016, 0.022, 0.085], 'utility': [-0.221], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.028, 1.0, 0.034, 0.005, 0.003, 0.005], 'utility': [0.059], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.077, 1.0, 0.426, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.176], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.224, 1.0, 0.042, 0.015, 0.014, 0.035, 0.567], 'utility': [-0.026], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.098, 0.007, 0.005, 0.009, 0.067, 1.0, 0.03], 'utility': [0.059], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.105, 0.424, 1.0, 0.028, 0.009, 0.008, 0.021], 'utility': [-0.176], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '6': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.031, 0.023, 0.042, 0.214, 0.702, 0.104], 'utility': [-0.03], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.438, 1.0, 0.232, 0.033, 0.016, 0.019, 0.065], 'utility': [-0.226], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.017, 1.0, 0.038, 0.005, 0.003, 0.004], 'utility': [0.168], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.25, 0.125], 'util_at_bs': [-0.03, -0.143, -0.061, 0.0, 0.0, 0.022, -0.026]}} reward={'1': -0.62, '2': -2.216, '3': -2.139, '4': -0.607, '5': -2.216, '6': -0.607, '7': -2.189, '8': -1.703} t=23
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 5, '4': 5, '5': 6, '6': 5, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.061, 1.0, 0.261, 0.014, 0.006, 0.006, 0.019], 'utility': [-0.179], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.27, 1.0, 0.047, 0.017, 0.016, 0.042, 0.707], 'utility': [-0.015], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.152, 0.009, 0.007, 0.014, 0.108, 1.0, 0.038], 'utility': [-0.056], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.123, 0.667, 1.0, 0.033, 0.011, 0.01, 0.028], 'utility': [-0.195], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.798, 0.031, 0.021, 0.036, 0.185, 1.0, 0.125], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.68, 1.0, 0.117, 0.029, 0.019, 0.029, 0.131], 'utility': [-0.227], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.117, 0.059, 1.0, 0.038, 0.008, 0.005, 0.009], 'utility': [0.002], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.049], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.069, 1.0, 0.334, 0.017, 0.006, 0.007, 0.021], 'utility': [-0.17], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.246, 1.0, 0.044, 0.016, 0.015, 0.038, 0.633], 'utility': [-0.018], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.123, 0.008, 0.006, 0.011, 0.085, 1.0, 0.034], 'utility': [-0.015], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.114, 0.531, 1.0, 0.031, 0.01, 0.009, 0.024], 'utility': [-0.144], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.034, 0.025, 0.044, 0.222, 0.935, 0.128], 'utility': [-0.028], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.529, 1.0, 0.152, 0.029, 0.016, 0.022, 0.085], 'utility': [-0.221], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.028, 1.0, 0.034, 0.005, 0.003, 0.005], 'utility': [0.059], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.028, -0.136, -0.085, 0.0, 0.0, -0.031, -0.018]}} reward={'1': -1.04, '2': -2.643, '3': -2.175, '4': -0.982, '5': -2.643, '6': -0.982, '7': -2.303, '8': -2.065} t=24
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 6, '3': 5, '4': 5, '5': 5, '6': 2, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.054, 1.0, 0.203, 0.012, 0.005, 0.005, 0.017], 'utility': [-0.197], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.296, 1.0, 0.05, 0.018, 0.018, 0.046, 0.788], 'utility': [-0.015], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.188, 0.011, 0.008, 0.017, 0.137, 1.0, 0.043], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.133, 0.836, 1.0, 0.035, 0.012, 0.011, 0.031], 'utility': [-0.192], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.592, 0.026, 0.017, 0.029, 0.143, 1.0, 0.114], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.888, 1.0, 0.105, 0.032, 0.024, 0.042, 0.235], 'utility': [-0.244], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.215, 0.144, 1.0, 0.047, 0.012, 0.009, 0.018], 'utility': [-0.141], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.061, 1.0, 0.261, 0.014, 0.006, 0.006, 0.019], 'utility': [-0.179], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.27, 1.0, 0.047, 0.017, 0.016, 0.042, 0.707], 'utility': [-0.015], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.152, 0.009, 0.007, 0.014, 0.108, 1.0, 0.038], 'utility': [-0.056], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.123, 0.667, 1.0, 0.033, 0.011, 0.01, 0.028], 'utility': [-0.195], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.798, 0.031, 0.021, 0.036, 0.185, 1.0, 0.125], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.68, 1.0, 0.117, 0.029, 0.019, 0.029, 0.131], 'utility': [-0.227], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.117, 0.059, 1.0, 0.038, 0.008, 0.005, 0.009], 'utility': [0.002], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.04, -0.14, -0.124, 0.0, 0.0, -0.052, -0.015]}} reward={'1': -1.418, '2': -3.284, '3': -2.351, '4': -1.298, '5': -3.284, '6': -1.298, '7': -2.511, '8': -2.884} t=25
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 6, '3': 5, '4': 5, '5': 5, '6': 2, '7': 1, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.1], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.047, 1.0, 0.158, 0.01, 0.004, 0.005, 0.016], 'utility': [-0.223], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.324, 1.0, 0.052, 0.019, 0.019, 0.05, 0.877], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.229, 0.013, 0.01, 0.02, 0.173, 1.0, 0.048], 'utility': [-0.163], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.955, 0.036, 0.012, 0.012, 0.034], 'utility': [-0.236], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.438, 0.022, 0.014, 0.022, 0.11, 1.0, 0.103], 'utility': [-0.096], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.887, 0.092, 0.033, 0.029, 0.06, 0.42], 'utility': [-0.102], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.377, 0.372, 1.0, 0.061, 0.019, 0.016, 0.037], 'utility': [-0.229], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.054, 1.0, 0.203, 0.012, 0.005, 0.005, 0.017], 'utility': [-0.197], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.296, 1.0, 0.05, 0.018, 0.018, 0.046, 0.788], 'utility': [-0.015], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.188, 0.011, 0.008, 0.017, 0.137, 1.0, 0.043], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.133, 0.836, 1.0, 0.035, 0.012, 0.011, 0.031], 'utility': [-0.192], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.592, 0.026, 0.017, 0.029, 0.143, 1.0, 0.114], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.888, 1.0, 0.105, 0.032, 0.024, 0.042, 0.235], 'utility': [-0.244], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.215, 0.144, 1.0, 0.047, 0.012, 0.009, 0.018], 'utility': [-0.141], 'ues_at_bs': [0.125, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.047, -0.152, -0.177, 0.0, 0.0, -0.071, -0.015]}} reward={'1': -2.397, '2': -3.436, '3': -1.804, '4': -2.232, '5': -3.436, '6': -2.232, '7': -1.865, '8': -3.073} t=26
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 6, '3': 5, '4': 5, '5': 5, '6': 2, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.091], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.122, 0.008, 0.003, 0.004, 0.014], 'utility': [-0.286], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.354, 1.0, 0.055, 0.021, 0.021, 0.055, 0.975], 'utility': [-0.15], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.278, 0.015, 0.012, 0.025, 0.218, 1.0, 0.053], 'utility': [-0.187], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.117, 1.0, 0.762, 0.03, 0.011, 0.011, 0.031], 'utility': [-0.25], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.324, 0.018, 0.011, 0.017, 0.085, 1.0, 0.094], 'utility': [-0.095], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.739, 0.08, 0.033, 0.034, 0.083, 0.776], 'utility': [-0.08], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '8': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.601, 0.998, 1.0, 0.078, 0.028, 0.027, 0.072], 'utility': [-0.251], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.1], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.047, 1.0, 0.158, 0.01, 0.004, 0.005, 0.016], 'utility': [-0.223], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.324, 1.0, 0.052, 0.019, 0.019, 0.05, 0.877], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.229, 0.013, 0.01, 0.02, 0.173, 1.0, 0.048], 'utility': [-0.163], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.955, 0.036, 0.012, 0.012, 0.034], 'utility': [-0.236], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.438, 0.022, 0.014, 0.022, 0.11, 1.0, 0.103], 'utility': [-0.096], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.887, 0.092, 0.033, 0.029, 0.06, 0.42], 'utility': [-0.102], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.377, 0.372, 1.0, 0.061, 0.019, 0.016, 0.037], 'utility': [-0.229], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.099, -0.114, -0.229, 0.0, 0.0, -0.12, -0.018]}} reward={'1': -2.493, '2': -4.439, '3': -3.323, '4': -2.196, '5': -4.439, '6': -2.196, '7': -2.93, '8': -3.841} t=27
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 6, '3': 2, '4': 5, '5': 5, '6': 2, '7': 6, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.087], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.093, 0.007, 0.003, 0.003, 0.012], 'utility': [-0.261], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.357, 0.924, 0.054, 0.021, 0.021, 0.055, 1.0], 'utility': [-0.231], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.335, 0.017, 0.014, 0.03, 0.273, 1.0, 0.058], 'utility': [-0.135], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.1, 1.0, 0.61, 0.026, 0.009, 0.009, 0.028], 'utility': [-0.238], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.24, 0.015, 0.009, 0.014, 0.066, 1.0, 0.085], 'utility': [-0.046], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.604, 0.395, 0.047, 0.022, 0.025, 0.074, 1.0], 'utility': [-0.056], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '8': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.311, 1.0, 0.359, 0.035, 0.015, 0.016, 0.05], 'utility': [-0.197], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.091], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.122, 0.008, 0.003, 0.004, 0.014], 'utility': [-0.286], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.354, 1.0, 0.055, 0.021, 0.021, 0.055, 0.975], 'utility': [-0.15], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.278, 0.015, 0.012, 0.025, 0.218, 1.0, 0.053], 'utility': [-0.187], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.117, 1.0, 0.762, 0.03, 0.011, 0.011, 0.031], 'utility': [-0.25], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.324, 0.018, 0.011, 0.017, 0.085, 1.0, 0.094], 'utility': [-0.095], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.739, 0.08, 0.033, 0.034, 0.083, 0.776], 'utility': [-0.08], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}, '8': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.601, 0.998, 1.0, 0.078, 0.028, 0.027, 0.072], 'utility': [-0.251], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.25], 'util_at_bs': [-0.088, -0.192, -0.262, 0.0, 0.0, -0.125, -0.115]}} reward={'1': -1.783, '2': -4.033, '3': -3.203, '4': -2.003, '5': -4.033, '6': -1.888, '7': -2.749, '8': -3.353} t=28
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 6, '3': 5, '4': 1, '5': 6, '6': 2, '7': 6, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.077], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.071, 0.006, 0.002, 0.003, 0.011], 'utility': [0.076], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.351, 0.833, 0.051, 0.02, 0.02, 0.055, 1.0], 'utility': [-0.222], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.401, 0.019, 0.016, 0.036, 0.34, 1.0, 0.064], 'utility': [-0.102], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.488, 0.022, 0.008, 0.008, 0.025], 'utility': [-0.22], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.178, 0.013, 0.007, 0.011, 0.051, 1.0, 0.077], 'utility': [-0.033], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.149, 0.019, 0.01, 0.013, 0.047, 1.0], 'utility': [-0.039], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.121, 0.014, 0.007, 0.008, 0.031], 'utility': [0.072], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.087], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.093, 0.007, 0.003, 0.003, 0.012], 'utility': [-0.261], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.357, 0.924, 0.054, 0.021, 0.021, 0.055, 1.0], 'utility': [-0.231], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.335, 0.017, 0.014, 0.03, 0.273, 1.0, 0.058], 'utility': [-0.135], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.1, 1.0, 0.61, 0.026, 0.009, 0.009, 0.028], 'utility': [-0.238], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.24, 0.015, 0.009, 0.014, 0.066, 1.0, 0.085], 'utility': [-0.046], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.604, 0.395, 0.047, 0.022, 0.025, 0.074, 1.0], 'utility': [-0.056], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}, '8': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.311, 1.0, 0.359, 0.035, 0.015, 0.016, 0.05], 'utility': [-0.197], 'ues_at_bs': [0.375, 0.375, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.1, -0.171, -0.232, 0.0, -0.135, -0.089, -0.143]}} reward={'1': -1.411, '2': 0.025, '3': -0.56, '4': -1.036, '5': 0.025, '6': -0.893, '7': -1.205, '8': 0.158} t=29
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 6, '3': 3, '4': 7, '5': 6, '6': 2, '7': 5, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.082], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.054, 0.005, 0.002, 0.002, 0.009], 'utility': [0.179], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.345, 0.752, 0.048, 0.019, 0.02, 0.054, 1.0], 'utility': [-0.212], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.477, 0.022, 0.019, 0.043, 0.423, 1.0, 0.07], 'utility': [-0.094], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.391, 0.019, 0.007, 0.007, 0.023], 'utility': [-0.149], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.133, 0.01, 0.006, 0.008, 0.039, 1.0, 0.069], 'utility': [0.017], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.086, 0.05, 0.007, 0.004, 0.006, 0.026, 1.0], 'utility': [0.114], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.051, 1.0, 0.038, 0.005, 0.003, 0.004, 0.017], 'utility': [0.179], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.077], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.071, 0.006, 0.002, 0.003, 0.011], 'utility': [0.076], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.351, 0.833, 0.051, 0.02, 0.02, 0.055, 1.0], 'utility': [-0.222], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.401, 0.019, 0.016, 0.036, 0.34, 1.0, 0.064], 'utility': [-0.102], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.488, 0.022, 0.008, 0.008, 0.025], 'utility': [-0.22], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.178, 0.013, 0.007, 0.011, 0.051, 1.0, 0.077], 'utility': [-0.033], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.149, 0.019, 0.01, 0.013, 0.047, 1.0], 'utility': [-0.039], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.121, 0.014, 0.007, 0.008, 0.031], 'utility': [0.072], 'ues_at_bs': [0.5, 0.25, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.025, 0.074, -0.072, 0.0, -0.102, -0.071, -0.13]}} reward={'1': -1.055, '2': 3.586, '3': 1.302, '4': -0.613, '5': 1.399, '6': -0.403, '7': -0.242, '8': 3.586} t=30
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 6, '3': 3, '4': 7, '5': 6, '6': 2, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.068], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.022, 1.0, 0.041, 0.004, 0.002, 0.002, 0.008], 'utility': [0.288], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.339, 0.679, 0.046, 0.018, 0.019, 0.053, 1.0], 'utility': [-0.203], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.563, 0.025, 0.022, 0.052, 0.524, 1.0, 0.076], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.062, 1.0, 0.314, 0.016, 0.006, 0.006, 0.02], 'utility': [-0.171], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.1, 0.009, 0.005, 0.007, 0.031, 1.0, 0.063], 'utility': [0.052], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.025, 0.015, 0.002, 0.001, 0.002, 0.012, 1.0], 'utility': [0.303], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.011, 0.002, 0.001, 0.002, 0.008], 'utility': [0.288], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.082], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.054, 0.005, 0.002, 0.002, 0.009], 'utility': [0.179], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.345, 0.752, 0.048, 0.019, 0.02, 0.054, 1.0], 'utility': [-0.212], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.477, 0.022, 0.019, 0.043, 0.423, 1.0, 0.07], 'utility': [-0.094], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.391, 0.019, 0.007, 0.007, 0.023], 'utility': [-0.149], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.133, 0.01, 0.006, 0.008, 0.039, 1.0, 0.069], 'utility': [0.017], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.086, 0.05, 0.007, 0.004, 0.006, 0.026, 1.0], 'utility': [0.114], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.051, 1.0, 0.038, 0.005, 0.003, 0.004, 0.017], 'utility': [0.179], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.013, 0.179, -0.149, 0.0, -0.094, -0.053, -0.049]}} reward={'1': -0.581, '2': 5.757, '3': 2.188, '4': -0.593, '5': 2.695, '6': -0.426, '7': 1.002, '8': 5.757} t=31
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 7, '5': 6, '6': 2, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.075], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.031, 0.003, 0.001, 0.002, 0.007], 'utility': [0.371], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.333, 0.615, 0.043, 0.018, 0.019, 0.052, 1.0], 'utility': [-0.194], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.66, 0.028, 0.025, 0.062, 0.647, 1.0, 0.082], 'utility': [-0.013], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.253, 0.013, 0.005, 0.006, 0.018], 'utility': [-0.194], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.077, 0.007, 0.004, 0.005, 0.025, 1.0, 0.058], 'utility': [0.082], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.006, 0.004, 0.001, 0.0, 0.001, 0.005, 1.0], 'utility': [0.536], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [0.371], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.068], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.022, 1.0, 0.041, 0.004, 0.002, 0.002, 0.008], 'utility': [0.288], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.339, 0.679, 0.046, 0.018, 0.019, 0.053, 1.0], 'utility': [-0.203], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.563, 0.025, 0.022, 0.052, 0.524, 1.0, 0.076], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.062, 1.0, 0.314, 0.016, 0.006, 0.006, 0.02], 'utility': [-0.171], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.1, 0.009, 0.005, 0.007, 0.031, 1.0, 0.063], 'utility': [0.052], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.025, 0.015, 0.002, 0.001, 0.002, 0.012, 1.0], 'utility': [0.303], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.011, 0.002, 0.001, 0.002, 0.008], 'utility': [0.288], 'ues_at_bs': [0.25, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.01, 0.288, -0.171, 0.0, -0.071, -0.029, 0.05]}} reward={'1': -0.046, '2': 7.413, '3': 4.279, '4': -0.136, '5': 3.652, '6': -0.046, '7': 3.418, '8': 7.413} t=32
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 7, '5': 6, '6': 0, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.051], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.023, 0.002, 0.001, 0.001, 0.006], 'utility': [0.418], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.327, 0.557, 0.041, 0.017, 0.018, 0.052, 1.0], 'utility': [-0.185], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.768, 0.032, 0.029, 0.074, 0.797, 1.0, 0.088], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.045, 1.0, 0.205, 0.011, 0.005, 0.005, 0.017], 'utility': [-0.215], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.06, 0.006, 0.003, 0.005, 0.02, 1.0, 0.055], 'utility': [0.105], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0], 'utility': [0.719], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.003, 1.0, 0.002, 0.0, 0.0, 0.0, 0.004], 'utility': [0.418], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.075], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.031, 0.003, 0.001, 0.002, 0.007], 'utility': [0.371], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.333, 0.615, 0.043, 0.018, 0.019, 0.052, 1.0], 'utility': [-0.194], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.66, 0.028, 0.025, 0.062, 0.647, 1.0, 0.082], 'utility': [-0.013], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.253, 0.013, 0.005, 0.006, 0.018], 'utility': [-0.194], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.077, 0.007, 0.004, 0.005, 0.025, 1.0, 0.058], 'utility': [0.082], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.006, 0.004, 0.001, 0.0, 0.001, 0.005, 1.0], 'utility': [0.536], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [0.371], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.013, 0.371, -0.194, 0.0, -0.013, -0.002, 0.171]}} reward={'1': 0.301, '2': 8.358, '3': 5.443, '4': 0.111, '5': 4.137, '6': 0.301, '7': 5.337, '8': 8.358} t=33
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 7, '5': 6, '6': 0, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.059], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.017, 0.002, 0.001, 0.001, 0.005], 'utility': [0.444], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.321, 0.506, 0.039, 0.016, 0.018, 0.051, 1.0], 'utility': [-0.176], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.887, 0.035, 0.034, 0.088, 0.978, 1.0, 0.095], 'utility': [0.001], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.039, 1.0, 0.166, 0.01, 0.004, 0.004, 0.015], 'utility': [-0.236], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.048, 0.006, 0.003, 0.004, 0.016, 1.0, 0.052], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.003, 1.0], 'utility': [0.663], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.444], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.051], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.023, 0.002, 0.001, 0.001, 0.006], 'utility': [0.418], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.327, 0.557, 0.041, 0.017, 0.018, 0.052, 1.0], 'utility': [-0.185], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.768, 0.032, 0.029, 0.074, 0.797, 1.0, 0.088], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.045, 1.0, 0.205, 0.011, 0.005, 0.005, 0.017], 'utility': [-0.215], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.06, 0.006, 0.003, 0.005, 0.02, 1.0, 0.055], 'utility': [0.105], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0], 'utility': [0.719], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.003, 1.0, 0.002, 0.0, 0.0, 0.0, 0.004], 'utility': [0.418], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.009, 0.418, -0.215, 0.0, -0.009, 0.015, 0.267]}} reward={'1': 0.549, '2': 8.883, '3': 5.504, '4': 0.337, '5': 4.347, '6': 0.549, '7': 4.867, '8': 8.883} t=34
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 4, '3': 3, '4': 7, '5': 6, '6': 0, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.013, 0.001, 0.001, 0.001, 0.005], 'utility': [0.476], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.316, 0.459, 0.037, 0.016, 0.017, 0.051, 1.0], 'utility': [-0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.85, 0.033, 0.032, 0.087, 1.0, 0.835, 0.085], 'utility': [0.011], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 1.0, 0.135, 0.008, 0.003, 0.004, 0.013], 'utility': [-0.257], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.039, 0.005, 0.002, 0.003, 0.014, 1.0, 0.051], 'utility': [0.15], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.476], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.059], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.017, 0.002, 0.001, 0.001, 0.005], 'utility': [0.444], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.321, 0.506, 0.039, 0.016, 0.018, 0.051, 1.0], 'utility': [-0.176], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.887, 0.035, 0.034, 0.088, 0.978, 1.0, 0.095], 'utility': [0.001], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.039, 1.0, 0.166, 0.01, 0.004, 0.004, 0.015], 'utility': [-0.236], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.048, 0.006, 0.003, 0.004, 0.016, 1.0, 0.052], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.003, 1.0], 'utility': [0.663], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.444], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.001, 0.444, -0.236, 0.0, 0.001, 0.027, 0.243]}} reward={'1': 0.771, '2': 9.528, '3': 5.483, '4': 0.551, '5': 4.639, '6': 0.771, '7': 4.069, '8': 9.528} t=35
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 4, '3': 3, '4': 7, '5': 6, '6': 0, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.01, 0.001, 0.001, 0.001, 0.004], 'utility': [0.506], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.31, 0.418, 0.035, 0.015, 0.017, 0.05, 1.0], 'utility': [-0.159], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.794, 0.03, 0.03, 0.084, 1.0, 0.684, 0.074], 'utility': [0.022], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 1.0, 0.111, 0.007, 0.003, 0.003, 0.012], 'utility': [-0.277], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.034, 0.005, 0.002, 0.003, 0.012, 1.0, 0.051], 'utility': [0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.506], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.013, 0.001, 0.001, 0.001, 0.005], 'utility': [0.476], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.316, 0.459, 0.037, 0.016, 0.017, 0.051, 1.0], 'utility': [-0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.85, 0.033, 0.032, 0.087, 1.0, 0.835, 0.085], 'utility': [0.011], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 1.0, 0.135, 0.008, 0.003, 0.004, 0.013], 'utility': [-0.257], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.039, 0.005, 0.002, 0.003, 0.014, 1.0, 0.051], 'utility': [0.15], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.476], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.011, 0.476, -0.257, 0.0, 0.011, 0.039, 0.203]}} reward={'1': 0.943, '2': 10.124, '3': 5.799, '4': 0.74, '5': 4.9, '6': 0.943, '7': 4.156, '8': 10.124} t=36
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 4, '3': 3, '4': 7, '5': 2, '6': 0, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.038], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.008, 0.001, 0.001, 0.001, 0.003], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.305, 0.381, 0.034, 0.015, 0.016, 0.05, 1.0], 'utility': [-0.15], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.738, 0.027, 0.028, 0.081, 1.0, 0.562, 0.065], 'utility': [0.033], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.091, 0.006, 0.003, 0.003, 0.011], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.005, 0.002, 0.003, 0.011, 1.0, 0.052], 'utility': [0.165], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.015], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.01, 0.001, 0.001, 0.001, 0.004], 'utility': [0.506], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.31, 0.418, 0.035, 0.015, 0.017, 0.05, 1.0], 'utility': [-0.159], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.794, 0.03, 0.03, 0.084, 1.0, 0.684, 0.074], 'utility': [0.022], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 1.0, 0.111, 0.007, 0.003, 0.003, 0.012], 'utility': [-0.277], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.034, 0.005, 0.002, 0.003, 0.012, 1.0, 0.051], 'utility': [0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [0.506], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.022, 0.506, -0.277, 0.0, 0.022, 0.047, 0.208]}} reward={'1': 1.066, '2': 2.96, '3': 3.004, '4': 0.904, '5': 2.96, '6': 1.066, '7': 4.241, '8': 2.96} t=37
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 7, '5': 1, '6': 5, '7': 5, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.006, 0.001, 0.0, 0.001, 0.003], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.3, 0.348, 0.032, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.142], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.684, 0.025, 0.026, 0.078, 1.0, 0.463, 0.057], 'utility': [0.045], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.076, 0.005, 0.002, 0.003, 0.01], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.005, 0.002, 0.003, 0.011, 1.0, 0.056], 'utility': [0.165], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.004, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.589], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.02, 0.005, 0.003, 0.006, 0.045], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.038], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.008, 0.001, 0.001, 0.001, 0.003], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.305, 0.381, 0.034, 0.015, 0.016, 0.05, 1.0], 'utility': [-0.15], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.738, 0.027, 0.028, 0.081, 1.0, 0.562, 0.065], 'utility': [0.033], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.091, 0.006, 0.003, 0.003, 0.011], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.005, 0.002, 0.003, 0.011, 1.0, 0.052], 'utility': [0.165], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.015], 'utility': [0.148], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.033, 0.148, 0.0, 0.0, 0.033, 0.053, 0.212]}} reward={'1': 1.137, '2': 1.973, '3': 2.625, '4': 1.038, '5': 1.973, '6': 1.137, '7': 4.47, '8': 1.973} t=38
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 7, '5': 5, '6': 5, '7': 5, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.005, 0.001, 0.0, 0.001, 0.003], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.295, 0.318, 0.03, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.134], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.631, 0.022, 0.025, 0.076, 1.0, 0.383, 0.05], 'utility': [0.056], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.063, 0.005, 0.002, 0.002, 0.009], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.061], 'utility': [0.149], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.01, 0.005, 0.001, 0.001, 0.001, 0.01, 1.0], 'utility': [0.433], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.256, 1.0, 0.053, 0.014, 0.01, 0.017, 0.109], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.006, 0.001, 0.0, 0.001, 0.003], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.3, 0.348, 0.032, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.142], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.684, 0.025, 0.026, 0.078, 1.0, 0.463, 0.057], 'utility': [0.045], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.076, 0.005, 0.002, 0.003, 0.01], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.005, 0.002, 0.003, 0.011, 1.0, 0.056], 'utility': [0.165], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.004, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.589], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.02, 0.005, 0.003, 0.006, 0.045], 'utility': [0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.045, 0.099, 0.0, 0.0, 0.045, 0.057, 0.224]}} reward={'1': 1.156, '2': 0.175, '3': 1.274, '4': 1.144, '5': 0.175, '6': 1.892, '7': 2.996, '8': 0.413} t=39
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 7, '5': 5, '6': 5, '7': 5, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.033], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.004, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.099], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.29, 0.291, 0.029, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.126], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.58, 0.02, 0.023, 0.074, 1.0, 0.318, 0.044], 'utility': [0.025], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.016, 1.0, 0.054, 0.004, 0.002, 0.002, 0.009], 'utility': [-0.099], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.13], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.037, 0.014, 0.003, 0.002, 0.004, 0.024, 1.0], 'utility': [0.235], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.959, 1.0, 0.115, 0.034, 0.025, 0.042, 0.215], 'utility': [0.002], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.005, 0.001, 0.0, 0.001, 0.003], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.295, 0.318, 0.03, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.134], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.631, 0.022, 0.025, 0.076, 1.0, 0.383, 0.05], 'utility': [0.056], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.063, 0.005, 0.002, 0.002, 0.009], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.061], 'utility': [0.149], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.01, 0.005, 0.001, 0.001, 0.001, 0.01, 1.0], 'utility': [0.433], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.256, 1.0, 0.053, 0.014, 0.01, 0.017, 0.109], 'utility': [0.009], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, 0.009, 0.0, 0.0, 0.056, 0.058, 0.15]}} reward={'1': 0.814, '2': -1.303, '3': -0.168, '4': 0.582, '5': -1.303, '6': 0.925, '7': 1.091, '8': -0.672} t=40
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 6, '3': 5, '4': 7, '5': 5, '6': 5, '7': 5, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.207], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.286, 0.267, 0.027, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.118], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.532, 0.018, 0.022, 0.072, 1.0, 0.265, 0.038], 'utility': [0.037], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.046, 0.004, 0.002, 0.002, 0.008], 'utility': [-0.207], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.011, 1.0, 0.078], 'utility': [0.116], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.13, 0.04, 0.008, 0.006, 0.009, 0.052, 1.0], 'utility': [0.055], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.271, 0.059, 0.02, 0.015, 0.025, 0.097], 'utility': [0.037], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.033], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.004, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.099], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.29, 0.291, 0.029, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.126], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.58, 0.02, 0.023, 0.074, 1.0, 0.318, 0.044], 'utility': [0.025], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.016, 1.0, 0.054, 0.004, 0.002, 0.002, 0.009], 'utility': [-0.099], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.13], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.037, 0.014, 0.003, 0.002, 0.004, 0.024, 1.0], 'utility': [0.235], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.959, 1.0, 0.115, 0.034, 0.025, 0.042, 0.215], 'utility': [0.002], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.014, -0.065, 0.0, 0.0, 0.025, 0.041, 0.055]}} reward={'1': 0.991, '2': -2.513, '3': -1.047, '4': 0.737, '5': -2.513, '6': 0.179, '7': 0.052, '8': -1.213} t=41
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 6, '3': 5, '4': 1, '5': 7, '6': 5, '7': 5, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.017], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [-0.307], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.281, 0.245, 0.026, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.11], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.487, 0.017, 0.02, 0.07, 1.0, 0.221, 0.034], 'utility': [0.004], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.013, 1.0, 0.04, 0.003, 0.002, 0.002, 0.007], 'utility': [-0.307], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.006, 0.003, 0.003, 0.012, 1.0, 0.091], 'utility': [0.088], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.426, 0.095, 0.02, 0.014, 0.021, 0.096, 1.0], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.022, 0.01, 0.008, 0.011, 0.033], 'utility': [0.323], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.016], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.207], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.286, 0.267, 0.027, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.118], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.532, 0.018, 0.022, 0.072, 1.0, 0.265, 0.038], 'utility': [0.037], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.046, 0.004, 0.002, 0.002, 0.008], 'utility': [-0.207], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.011, 1.0, 0.078], 'utility': [0.116], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.13, 0.04, 0.008, 0.006, 0.009, 0.052, 1.0], 'utility': [0.055], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.271, 0.059, 0.02, 0.015, 0.025, 0.097], 'utility': [0.037], 'ues_at_bs': [0.25, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.037, -0.126, 0.0, 0.0, 0.037, 0.05, -0.032]}} reward={'1': 0.703, '2': -1.944, '3': -0.592, '4': 3.278, '5': -1.944, '6': -0.695, '7': 0.76, '8': 0.159} t=42
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 6, '3': 5, '4': 6, '5': 7, '6': 5, '7': 1, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [0.289], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.277, 0.225, 0.025, 0.012, 0.015, 0.048, 1.0], 'utility': [-0.103], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.444, 0.015, 0.019, 0.069, 1.0, 0.186, 0.03], 'utility': [0.023], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.289], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.028, 0.007, 0.003, 0.003, 0.012, 1.0, 0.107], 'utility': [0.053], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.152, 0.035, 0.022, 0.032, 0.115, 0.749], 'utility': [-0.046], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.01, 0.005, 0.003, 0.003, 0.003, 0.007], 'utility': [0.455], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.017], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [-0.307], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.281, 0.245, 0.026, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.11], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.487, 0.017, 0.02, 0.07, 1.0, 0.221, 0.034], 'utility': [0.004], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.013, 1.0, 0.04, 0.003, 0.002, 0.002, 0.007], 'utility': [-0.307], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.006, 0.003, 0.003, 0.012, 1.0, 0.091], 'utility': [0.088], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.426, 0.095, 0.02, 0.014, 0.021, 0.096, 1.0], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.022, 0.01, 0.008, 0.011, 0.033], 'utility': [0.323], 'ues_at_bs': [0.125, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.323, -0.097, 0.0, 0.0, 0.004, 0.035, -0.105]}} reward={'1': 0.378, '2': 5.789, '3': 2.796, '4': 2.877, '5': 5.789, '6': -0.555, '7': 1.3, '8': 4.089} t=43
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 6, '5': 1, '6': 5, '7': 3, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.001, 0.003], 'utility': [0.288], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.273, 0.208, 0.024, 0.012, 0.014, 0.048, 1.0], 'utility': [-0.096], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.405, 0.014, 0.018, 0.067, 1.0, 0.157, 0.026], 'utility': [0.04], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.288], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.008, 0.003, 0.004, 0.014, 1.0, 0.126], 'utility': [0.019], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.093, 0.024, 0.015, 0.019, 0.054, 0.241], 'utility': [0.012], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.001, 0.001, 0.0, 0.0, 0.0, 0.001], 'utility': [0.954], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [0.289], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.277, 0.225, 0.025, 0.012, 0.015, 0.048, 1.0], 'utility': [-0.103], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.444, 0.015, 0.019, 0.069, 1.0, 0.186, 0.03], 'utility': [0.023], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.289], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.028, 0.007, 0.003, 0.003, 0.012, 1.0, 0.107], 'utility': [0.053], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.152, 0.035, 0.022, 0.032, 0.115, 0.749], 'utility': [-0.046], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.01, 0.005, 0.003, 0.003, 0.003, 0.007], 'utility': [0.455], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.204, 0.289, 0.0, 0.0, 0.023, 0.019, -0.074]}} reward={'1': 0.031, '2': 5.757, '3': 4.862, '4': 6.713, '5': 5.757, '6': -0.401, '7': 4.415, '8': 9.665} t=44
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 6, '5': 1, '6': 5, '7': 3, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.014], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [0.285], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.269, 0.192, 0.023, 0.011, 0.014, 0.048, 1.0], 'utility': [-0.089], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.369, 0.013, 0.017, 0.067, 1.0, 0.133, 0.023], 'utility': [0.057], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.285], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.033, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.019], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.051, 0.015, 0.009, 0.01, 0.023, 0.077], 'utility': [0.13], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.001, 0.003], 'utility': [0.288], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.273, 0.208, 0.024, 0.012, 0.014, 0.048, 1.0], 'utility': [-0.096], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.405, 0.014, 0.018, 0.067, 1.0, 0.157, 0.026], 'utility': [0.04], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.288], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.008, 0.003, 0.004, 0.014, 1.0, 0.126], 'utility': [0.019], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.093, 0.024, 0.015, 0.019, 0.054, 0.241], 'utility': [0.012], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.001, 0.001, 0.0, 0.0, 0.0, 0.001], 'utility': [0.954], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.483, 0.288, 0.0, 0.0, 0.04, 0.002, -0.042]}} reward={'1': -0.333, '2': 5.697, '3': 5.852, '4': 7.914, '5': 5.697, '6': 0.037, '7': 5.852, '8': 11.296} t=45
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 6, '5': 1, '6': 5, '7': 3, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.005], 'utility': [0.27], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.265, 0.177, 0.022, 0.011, 0.014, 0.048, 1.0], 'utility': [0.068], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.336, 0.012, 0.016, 0.066, 1.0, 0.114, 0.021], 'utility': [0.074], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.014, 1.0, 0.042, 0.004, 0.002, 0.002, 0.008], 'utility': [0.27], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.035, 0.01, 0.004, 0.005, 0.017, 1.0, 0.174], 'utility': [-0.056], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.026, 0.01, 0.006, 0.005, 0.009, 0.025], 'utility': [0.267], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0], 'utility': [0.991], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.014], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [0.285], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.269, 0.192, 0.023, 0.011, 0.014, 0.048, 1.0], 'utility': [-0.089], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.369, 0.013, 0.017, 0.067, 1.0, 0.133, 0.023], 'utility': [0.057], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.285], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.033, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.019], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.051, 0.015, 0.009, 0.01, 0.023, 0.077], 'utility': [0.13], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.565, 0.285, 0.0, 0.0, 0.057, -0.017, 0.02]}} reward={'1': -0.704, '2': 5.404, '3': 8.841, '4': 8.877, '5': 5.404, '6': -0.014, '7': 12.578, '8': 12.578} t=46
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 6, '5': 1, '6': 5, '7': 4, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.004, 0.001, 0.0, 0.001, 0.006], 'utility': [0.252], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.164, 0.021, 0.011, 0.014, 0.048, 1.0], 'utility': [0.075], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.306, 0.011, 0.015, 0.066, 1.0, 0.098, 0.019], 'utility': [0.089], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.049, 0.004, 0.002, 0.002, 0.008], 'utility': [0.252], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.007, 0.004, 0.003, 0.004, 0.01], 'utility': [0.389], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.003, 0.006, 0.009, 0.005, 0.003], 'utility': [0.473], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.005], 'utility': [0.27], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.265, 0.177, 0.022, 0.011, 0.014, 0.048, 1.0], 'utility': [0.068], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.336, 0.012, 0.016, 0.066, 1.0, 0.114, 0.021], 'utility': [0.074], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.014, 1.0, 0.042, 0.004, 0.002, 0.002, 0.008], 'utility': [0.27], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.035, 0.01, 0.004, 0.005, 0.017, 1.0, 0.174], 'utility': [-0.056], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.026, 0.01, 0.006, 0.005, 0.009, 0.025], 'utility': [0.267], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0], 'utility': [0.991], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.629, 0.27, 0.0, 0.0, 0.074, -0.035, 0.068]}} reward={'1': -0.873, '2': 5.043, '3': 6.247, '4': 6.342, '5': 5.043, '6': -0.085, '7': 8.624, '8': 8.624} t=47
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 6, '5': 1, '6': 5, '7': 4, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.025], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.004, 0.001, 0.001, 0.001, 0.008], 'utility': [0.231], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.259, 0.153, 0.02, 0.011, 0.014, 0.048, 1.0], 'utility': [0.081], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.279, 0.01, 0.014, 0.066, 1.0, 0.085, 0.017], 'utility': [0.103], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.058, 0.004, 0.002, 0.002, 0.009], 'utility': [0.231], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.062], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.013, 0.009, 0.004, 0.003, 0.003, 0.006], 'utility': [0.414], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.011, 0.03, 0.057, 0.021, 0.009], 'utility': [0.173], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.004, 0.001, 0.0, 0.001, 0.006], 'utility': [0.252], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.164, 0.021, 0.011, 0.014, 0.048, 1.0], 'utility': [0.075], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.306, 0.011, 0.015, 0.066, 1.0, 0.098, 0.019], 'utility': [0.089], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.049, 0.004, 0.002, 0.002, 0.008], 'utility': [0.252], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.007, 0.004, 0.003, 0.004, 0.01], 'utility': [0.389], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.003, 0.006, 0.009, 0.005, 0.003], 'utility': [0.473], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.431, 0.252, 0.0, 0.0, 0.089, -0.044, 0.075]}} reward={'1': -0.873, '2': 4.624, '3': 4.449, '4': 4.597, '5': 4.624, '6': -0.045, '7': 5.867, '8': 5.867} t=48
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 6, '5': 1, '6': 5, '7': 4, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.005, 0.001, 0.001, 0.001, 0.011], 'utility': [0.208], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.256, 0.142, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.086], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.256, 0.009, 0.014, 0.067, 1.0, 0.074, 0.015], 'utility': [0.116], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 1.0, 0.069, 0.005, 0.002, 0.003, 0.01], 'utility': [0.208], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.018, 0.019, 0.009, 0.005, 0.004, 0.007], 'utility': [0.322], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.024, 0.092, 0.254, 0.057, 0.02], 'utility': [-0.04], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.025], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.004, 0.001, 0.001, 0.001, 0.008], 'utility': [0.231], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.259, 0.153, 0.02, 0.011, 0.014, 0.048, 1.0], 'utility': [0.081], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.279, 0.01, 0.014, 0.066, 1.0, 0.085, 0.017], 'utility': [0.103], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.058, 0.004, 0.002, 0.002, 0.009], 'utility': [0.231], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.062], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.013, 0.009, 0.004, 0.003, 0.003, 0.006], 'utility': [0.414], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.011, 0.03, 0.057, 0.021, 0.009], 'utility': [0.173], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.293, 0.231, 0.0, 0.0, 0.103, -0.044, 0.081]}} reward={'1': -0.873, '2': 4.156, '3': 2.46, '4': 2.655, '5': 4.156, '6': -0.007, '7': 2.827, '8': 2.655} t=49
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 6, '5': 1, '6': 5, '7': 4, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.044], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.005, 0.001, 0.001, 0.002, 0.015], 'utility': [0.182], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.253, 0.133, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.092], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.235, 0.009, 0.013, 0.068, 1.0, 0.065, 0.014], 'utility': [-0.135], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.023, 1.0, 0.083, 0.006, 0.002, 0.003, 0.011], 'utility': [0.182], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.032, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.008], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.031, 0.053, 0.022, 0.009, 0.007, 0.011], 'utility': [0.175], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.042, 0.213, 0.981, 0.117, 0.034], 'utility': [-0.016], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.005, 0.001, 0.001, 0.001, 0.011], 'utility': [0.208], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.256, 0.142, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.086], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.256, 0.009, 0.014, 0.067, 1.0, 0.074, 0.015], 'utility': [0.116], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 1.0, 0.069, 0.005, 0.002, 0.003, 0.01], 'utility': [0.208], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.018, 0.019, 0.009, 0.005, 0.004, 0.007], 'utility': [0.322], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.024, 0.092, 0.254, 0.057, 0.02], 'utility': [-0.04], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.141, 0.208, 0.0, 0.0, 0.116, -0.044, 0.086]}} reward={'1': -0.524, '2': 3.648, '3': 1.666, '4': 0.034, '5': 3.648, '6': 0.261, '7': 1.583, '8': 0.034} t=50
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 6, '5': 1, '6': 5, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.029], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.019], 'utility': [0.155], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.251, 0.124, 0.018, 0.01, 0.013, 0.05, 1.0], 'utility': [0.097], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.217, 0.008, 0.013, 0.07, 1.0, 0.058, 0.013], 'utility': [-0.036], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.101, 0.007, 0.003, 0.003, 0.012], 'utility': [0.155], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.007, 0.003, 0.004, 0.014, 1.0, 0.115], 'utility': [0.016], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.053, 0.155, 0.058, 0.018, 0.012, 0.017], 'utility': [0.022], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.272, 0.01, 0.018, 0.111, 1.0, 0.055, 0.014], 'utility': [0.012], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.044], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.005, 0.001, 0.001, 0.002, 0.015], 'utility': [0.182], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.253, 0.133, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.092], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.235, 0.009, 0.013, 0.068, 1.0, 0.065, 0.014], 'utility': [-0.135], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.023, 1.0, 0.083, 0.006, 0.002, 0.003, 0.011], 'utility': [0.182], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.032, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.008], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.031, 0.053, 0.022, 0.009, 0.007, 0.011], 'utility': [0.175], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.042, 0.213, 0.981, 0.117, 0.034], 'utility': [-0.016], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.079, 0.182, 0.0, 0.0, -0.076, -0.026, 0.092]}} reward={'1': -0.124, '2': 3.11, '3': 0.874, '4': 0.055, '5': 3.11, '6': -0.124, '7': 0.345, '8': 0.055} t=51
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 6, '5': 5, '6': 5, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.007, 0.002, 0.001, 0.003, 0.026], 'utility': [0.127], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.248, 0.116, 0.017, 0.01, 0.013, 0.05, 1.0], 'utility': [0.101], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.201, 0.008, 0.013, 0.073, 1.0, 0.052, 0.012], 'utility': [0.051], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.123, 0.008, 0.003, 0.004, 0.013], 'utility': [0.127], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.006, 0.003, 0.003, 0.012, 1.0, 0.089], 'utility': [0.069], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.085, 0.431, 0.141, 0.032, 0.019, 0.025], 'utility': [0.111], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.069, 0.004, 0.006, 0.046, 1.0, 0.021, 0.005], 'utility': [0.051], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.029], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.019], 'utility': [0.155], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.251, 0.124, 0.018, 0.01, 0.013, 0.05, 1.0], 'utility': [0.097], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.217, 0.008, 0.013, 0.07, 1.0, 0.058, 0.013], 'utility': [-0.036], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.101, 0.007, 0.003, 0.003, 0.012], 'utility': [0.155], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.007, 0.003, 0.004, 0.014, 1.0, 0.115], 'utility': [0.016], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.053, 0.155, 0.058, 0.018, 0.012, 0.017], 'utility': [0.022], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.272, 0.01, 0.018, 0.111, 1.0, 0.055, 0.014], 'utility': [0.012], 'ues_at_bs': [0.25, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.017, 0.155, 0.0, 0.0, -0.012, -0.006, 0.097]}} reward={'1': 0.268, '2': 2.549, '3': 2.125, '4': 1.423, '5': 2.442, '6': 0.268, '7': 2.229, '8': 1.02} t=52
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 6, '5': 5, '6': 5, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.003, 0.034], 'utility': [0.099], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.247, 0.109, 0.017, 0.01, 0.013, 0.051, 1.0], 'utility': [0.105], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.188, 0.008, 0.013, 0.076, 1.0, 0.047, 0.011], 'utility': [0.111], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.036, 1.0, 0.151, 0.009, 0.004, 0.004, 0.014], 'utility': [0.099], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.019, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.103], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.894, 0.111, 1.0, 0.286, 0.047, 0.025, 0.032], 'utility': [0.074], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.016, 0.001, 0.002, 0.015, 1.0, 0.007, 0.001], 'utility': [0.111], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.007, 0.002, 0.001, 0.003, 0.026], 'utility': [0.127], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.248, 0.116, 0.017, 0.01, 0.013, 0.05, 1.0], 'utility': [0.101], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.201, 0.008, 0.013, 0.073, 1.0, 0.052, 0.012], 'utility': [0.051], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.123, 0.008, 0.003, 0.004, 0.013], 'utility': [0.127], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.006, 0.003, 0.003, 0.012, 1.0, 0.089], 'utility': [0.069], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.085, 0.431, 0.141, 0.032, 0.019, 0.025], 'utility': [0.111], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.069, 0.004, 0.006, 0.046, 1.0, 0.021, 0.005], 'utility': [0.051], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.111, 0.127, 0.111, 0.0, 0.051, 0.013, 0.101]}} reward={'1': 0.708, '2': 1.973, '3': 1.788, '4': 1.968, '5': 1.806, '6': 0.708, '7': 1.472, '8': 2.216} t=53
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 4, '5': 5, '6': 5, '7': 4, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.01, 0.002, 0.002, 0.004, 0.045], 'utility': [0.069], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.103, 0.016, 0.009, 0.013, 0.052, 1.0], 'utility': [0.109], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.177, 0.007, 0.013, 0.081, 1.0, 0.043, 0.01], 'utility': [0.139], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.042, 1.0, 0.186, 0.011, 0.004, 0.005, 0.016], 'utility': [0.069], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.016, 0.004, 0.002, 0.002, 0.009, 1.0, 0.052], 'utility': [0.157], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.376, 0.064, 1.0, 0.252, 0.03, 0.014, 0.018], 'utility': [0.084], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.004, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.139], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.003, 0.034], 'utility': [0.099], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.247, 0.109, 0.017, 0.01, 0.013, 0.051, 1.0], 'utility': [0.105], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.188, 0.008, 0.013, 0.076, 1.0, 0.047, 0.011], 'utility': [0.111], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.036, 1.0, 0.151, 0.009, 0.004, 0.004, 0.014], 'utility': [0.099], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.019, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.103], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.894, 0.111, 1.0, 0.286, 0.047, 0.025, 0.032], 'utility': [0.074], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.016, 0.001, 0.002, 0.015, 1.0, 0.007, 0.001], 'utility': [0.111], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.074, 0.099, 0.074, 0.0, 0.111, 0.035, 0.105]}} reward={'1': 1.153, '2': 1.387, '3': 1.925, '4': 2.413, '5': 1.482, '6': 1.153, '7': 1.671, '8': 2.784} t=54
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 3, '4': 4, '5': 5, '6': 5, '7': 4, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.011, 0.003, 0.002, 0.005, 0.06], 'utility': [0.04], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.244, 0.097, 0.016, 0.009, 0.013, 0.053, 1.0], 'utility': [0.112], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.167, 0.007, 0.013, 0.086, 1.0, 0.04, 0.01], 'utility': [0.145], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.04], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.013, 0.003, 0.001, 0.002, 0.007, 1.0, 0.039], 'utility': [0.2], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.179, 0.039, 1.0, 0.23, 0.021, 0.009, 0.011], 'utility': [0.124], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.145], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.01, 0.002, 0.002, 0.004, 0.045], 'utility': [0.069], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.103, 0.016, 0.009, 0.013, 0.052, 1.0], 'utility': [0.109], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.177, 0.007, 0.013, 0.081, 1.0, 0.043, 0.01], 'utility': [0.139], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.042, 1.0, 0.186, 0.011, 0.004, 0.005, 0.016], 'utility': [0.069], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.016, 0.004, 0.002, 0.002, 0.009, 1.0, 0.052], 'utility': [0.157], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.376, 0.064, 1.0, 0.252, 0.03, 0.014, 0.018], 'utility': [0.084], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.004, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.139], 'ues_at_bs': [0.125, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.084, 0.069, 0.084, 0.0, 0.139, 0.058, 0.109]}} reward={'1': 1.645, '2': 0.798, '3': 2.245, '4': 2.901, '5': 1.359, '6': 1.645, '7': 2.481, '8': 2.901} t=55
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 1, '4': 4, '5': 5, '6': 0, '7': 1, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.079], 'utility': [0.027], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.243, 0.092, 0.015, 0.009, 0.013, 0.054, 1.0], 'utility': [0.162], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.159, 0.007, 0.013, 0.093, 1.0, 0.037, 0.01], 'utility': [0.143], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.027], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.01, 0.002, 0.001, 0.001, 0.006, 1.0, 0.028], 'utility': [0.258], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.101, 0.027, 1.0, 0.226, 0.016, 0.007, 0.008], 'utility': [0.162], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.143], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.011, 0.003, 0.002, 0.005, 0.06], 'utility': [0.04], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.244, 0.097, 0.016, 0.009, 0.013, 0.053, 1.0], 'utility': [0.112], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.167, 0.007, 0.013, 0.086, 1.0, 0.04, 0.01], 'utility': [0.145], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.04], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.013, 0.003, 0.001, 0.002, 0.007, 1.0, 0.039], 'utility': [0.2], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.179, 0.039, 1.0, 0.23, 0.021, 0.009, 0.011], 'utility': [0.124], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.145], 'ues_at_bs': [0.0, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.0, 0.04, 0.124, 0.124, 0.145, 0.082, 0.112]}} reward={'1': 2.155, '2': 1.446, '3': 3.246, '4': 2.983, '5': 1.444, '6': 2.155, '7': 3.24, '8': 2.852} t=56
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 0, '4': 4, '5': 5, '6': 2, '7': 1, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.014, 0.004, 0.003, 0.007, 0.103], 'utility': [0.014], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.087, 0.015, 0.009, 0.013, 0.056, 1.0], 'utility': [0.165], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.153, 0.007, 0.013, 0.102, 1.0, 0.035, 0.009], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.014], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.002, 0.001, 0.001, 0.005, 1.0, 0.021], 'utility': [0.311], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.07, 0.022, 1.0, 0.247, 0.014, 0.006, 0.006], 'utility': [0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.079], 'utility': [0.027], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.243, 0.092, 0.015, 0.009, 0.013, 0.054, 1.0], 'utility': [0.162], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.159, 0.007, 0.013, 0.093, 1.0, 0.037, 0.01], 'utility': [0.143], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.027], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.01, 0.002, 0.001, 0.001, 0.006, 1.0, 0.028], 'utility': [0.258], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.101, 0.027, 1.0, 0.226, 0.016, 0.007, 0.008], 'utility': [0.162], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.143], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.162, 0.027, 0.162, 0.162, 0.143, 0.108, 0.162]}} reward={'1': 2.717, '2': 1.281, '3': 3.291, '4': 2.968, '5': 1.304, '6': 2.717, '7': 3.362, '8': 2.807} t=57
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 0, '4': 4, '5': 5, '6': 0, '7': 1, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.044], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.048, 1.0, 0.016, 0.005, 0.004, 0.009, 0.134], 'utility': [-0.001], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.083, 0.015, 0.009, 0.013, 0.057, 1.0], 'utility': [0.166], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.149, 0.007, 0.014, 0.113, 1.0, 0.034, 0.009], 'utility': [0.136], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [-0.001], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.015], 'utility': [0.375], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.059, 0.021, 1.0, 0.297, 0.014, 0.006, 0.006], 'utility': [0.142], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.136], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.014, 0.004, 0.003, 0.007, 0.103], 'utility': [0.014], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.087, 0.015, 0.009, 0.013, 0.056, 1.0], 'utility': [0.165], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.153, 0.007, 0.013, 0.102, 1.0, 0.035, 0.009], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.014], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.002, 0.001, 0.001, 0.005, 1.0, 0.021], 'utility': [0.311], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.07, 0.022, 1.0, 0.247, 0.014, 0.006, 0.006], 'utility': [0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.165, 0.014, 0.168, 0.168, 0.14, 0.136, 0.165]}} reward={'1': 3.311, '2': 1.099, '3': 3.329, '4': 2.925, '5': 0.937, '6': 3.311, '7': 2.842, '8': 2.723} t=58
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 0, '4': 4, '5': 5, '6': 7, '7': 1, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.055, 1.0, 0.018, 0.005, 0.005, 0.011, 0.173], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.079, 0.014, 0.009, 0.013, 0.059, 1.0], 'utility': [0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.145, 0.007, 0.014, 0.126, 1.0, 0.032, 0.009], 'utility': [0.125], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.056, 1.0, 0.265, 0.014, 0.005, 0.006, 0.019], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.01], 'utility': [0.439], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.058, 0.023, 1.0, 0.376, 0.017, 0.007, 0.007], 'utility': [0.093], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.003, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.125], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.044], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.048, 1.0, 0.016, 0.005, 0.004, 0.009, 0.134], 'utility': [-0.001], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.083, 0.015, 0.009, 0.013, 0.057, 1.0], 'utility': [0.166], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.149, 0.007, 0.014, 0.113, 1.0, 0.034, 0.009], 'utility': [0.136], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [-0.001], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.015], 'utility': [0.375], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.059, 0.021, 1.0, 0.297, 0.014, 0.006, 0.006], 'utility': [0.142], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.136], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.001, 0.142, 0.142, 0.136, 0.166, 0.166]}} reward={'1': 3.968, '2': 0.803, '3': 3.358, '4': 2.79, '5': 0.301, '6': 3.968, '7': 1.85, '8': 2.506} t=59
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 0, '4': 4, '5': 7, '6': 7, '7': 1, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.02, 0.006, 0.005, 0.013, 0.223], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.076, 0.014, 0.009, 0.014, 0.061, 1.0], 'utility': [0.169], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.143, 0.007, 0.015, 0.142, 1.0, 0.032, 0.009], 'utility': [0.108], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.306, 0.016, 0.006, 0.006, 0.02], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.515], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.063, 0.028, 1.0, 0.476, 0.022, 0.008, 0.009], 'utility': [0.03], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.006, 0.001, 0.001, 0.011, 1.0, 0.003, 0.001], 'utility': [0.108], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.055, 1.0, 0.018, 0.005, 0.005, 0.011, 0.173], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.079, 0.014, 0.009, 0.013, 0.059, 1.0], 'utility': [0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.145, 0.007, 0.014, 0.126, 1.0, 0.032, 0.009], 'utility': [0.125], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.056, 1.0, 0.265, 0.014, 0.005, 0.006, 0.019], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.01], 'utility': [0.439], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.058, 0.023, 1.0, 0.376, 0.017, 0.007, 0.007], 'utility': [0.093], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.003, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.125], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.168, -0.024, 0.093, 0.093, 0.125, 0.198, 0.168]}} reward={'1': 4.677, '2': 0.496, '3': 3.379, '4': 2.072, '5': -0.432, '6': 4.677, '7': 0.594, '8': 2.158} t=60
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 0, '4': 4, '5': 7, '6': 7, '7': 1, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.071, 1.0, 0.022, 0.007, 0.006, 0.015, 0.286], 'utility': [-0.071], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.073, 0.014, 0.009, 0.014, 0.063, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.016, 0.162, 1.0, 0.031, 0.009], 'utility': [0.103], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.355, 0.018, 0.007, 0.007, 0.022], 'utility': [-0.071], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.002, 1.0, 0.004], 'utility': [0.594], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.012, 0.001, 0.002, 0.022, 1.0, 0.005, 0.001], 'utility': [0.083], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.02, 0.006, 0.005, 0.013, 0.223], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.076, 0.014, 0.009, 0.014, 0.061, 1.0], 'utility': [0.169], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.143, 0.007, 0.015, 0.142, 1.0, 0.032, 0.009], 'utility': [0.108], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.306, 0.016, 0.006, 0.006, 0.02], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.515], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.063, 0.028, 1.0, 0.476, 0.022, 0.008, 0.009], 'utility': [0.03], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.006, 0.001, 0.001, 0.011, 1.0, 0.003, 0.001], 'utility': [0.108], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.169, -0.047, 0.03, 0.03, 0.108, 0.234, 0.169]}} reward={'1': 5.468, '2': 0.18, '3': 3.391, '4': 1.052, '5': -1.482, '6': 5.468, '7': -0.372, '8': 1.866} t=61
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 0, '4': 7, '5': 7, '6': 7, '7': 1, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.052], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.08, 1.0, 0.024, 0.008, 0.007, 0.018, 0.365], 'utility': [-0.096], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.017, 0.186, 1.0, 0.031, 0.009], 'utility': [0.076], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.083, 1.0, 0.413, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.096], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.003], 'utility': [0.686], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.023, 0.002, 0.004, 0.044, 1.0, 0.009, 0.002], 'utility': [0.051], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.071, 1.0, 0.022, 0.007, 0.006, 0.015, 0.286], 'utility': [-0.071], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.073, 0.014, 0.009, 0.014, 0.063, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.016, 0.162, 1.0, 0.031, 0.009], 'utility': [0.103], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.355, 0.018, 0.007, 0.007, 0.022], 'utility': [-0.071], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.002, 1.0, 0.004], 'utility': [0.594], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.012, 0.001, 0.002, 0.022, 1.0, 0.005, 0.001], 'utility': [0.083], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.08, 0.012, 0.093, 0.273, 0.17]}} reward={'1': 6.34, '2': -0.143, '3': 3.395, '4': 0.621, '5': -1.805, '6': 6.34, '7': -0.553, '8': 1.275} t=62
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 0, '4': 6, '5': 7, '6': 7, '7': 1, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.09, 1.0, 0.026, 0.009, 0.008, 0.021, 0.465], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.018, 0.216, 1.0, 0.031, 0.009], 'utility': [0.045], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.097, 1.0, 0.482, 0.023, 0.008, 0.009, 0.026], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.002], 'utility': [0.788], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.042, 0.003, 0.007, 0.086, 1.0, 0.014, 0.004], 'utility': [0.012], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.052], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.08, 1.0, 0.024, 0.008, 0.007, 0.018, 0.365], 'utility': [-0.096], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.017, 0.186, 1.0, 0.031, 0.009], 'utility': [0.076], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.083, 1.0, 0.413, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.096], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.003], 'utility': [0.686], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.023, 0.002, 0.004, 0.044, 1.0, 0.009, 0.002], 'utility': [0.051], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.096, -0.08, -0.002, 0.064, 0.317, 0.17]}} reward={'1': 7.331, '2': -0.468, '3': 3.395, '4': 0.113, '5': -2.13, '6': 7.331, '7': -0.763, '8': 0.113} t=63
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 0, '4': 6, '5': 7, '6': 7, '7': 1, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.061], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.1, 1.0, 0.029, 0.01, 0.009, 0.025, 0.59], 'utility': [-0.144], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.142, 0.009, 0.019, 0.251, 1.0, 0.031, 0.01], 'utility': [0.011], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.112, 1.0, 0.563, 0.026, 0.009, 0.01, 0.029], 'utility': [-0.144], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.0, 1.0, 0.001], 'utility': [0.906], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.025, 1.0, 0.346, 0.018, 0.007, 0.008], 'utility': [0.006], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.075, 0.005, 0.012, 0.162, 1.0, 0.021, 0.006], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.09, 1.0, 0.026, 0.009, 0.008, 0.021, 0.465], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.018, 0.216, 1.0, 0.031, 0.009], 'utility': [0.045], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.097, 1.0, 0.482, 0.023, 0.008, 0.009, 0.026], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.002], 'utility': [0.788], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.042, 0.003, 0.007, 0.086, 1.0, 0.014, 0.004], 'utility': [0.012], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.12, -0.08, -0.017, 0.029, 0.367, 0.17]}} reward={'1': 8.454, '2': -0.792, '3': 3.395, '4': -0.016, '5': -1.882, '6': 8.454, '7': 0.155, '8': -0.016} t=64
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 0, '4': 6, '5': 7, '6': 7, '7': 1, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.111, 1.0, 0.031, 0.011, 0.011, 0.029, 0.745], 'utility': [-0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.252, 0.076, 0.014, 0.009, 0.014, 0.064, 1.0], 'utility': [0.166], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.144, 0.009, 0.021, 0.295, 1.0, 0.032, 0.01], 'utility': [-0.023], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.13, 1.0, 0.658, 0.03, 0.011, 0.011, 0.032], 'utility': [-0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.036, 0.017, 1.0, 0.183, 0.01, 0.004, 0.005], 'utility': [0.112], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.129, 0.008, 0.02, 0.295, 1.0, 0.03, 0.009], 'utility': [-0.078], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.061], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.1, 1.0, 0.029, 0.01, 0.009, 0.025, 0.59], 'utility': [-0.144], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.142, 0.009, 0.019, 0.251, 1.0, 0.031, 0.01], 'utility': [0.011], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.112, 1.0, 0.563, 0.026, 0.009, 0.01, 0.029], 'utility': [-0.144], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.0, 1.0, 0.001], 'utility': [0.906], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.025, 1.0, 0.346, 0.018, 0.007, 0.008], 'utility': [0.006], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.075, 0.005, 0.012, 0.162, 1.0, 0.021, 0.006], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.144, 0.006, 0.009, -0.01, 0.423, 0.17]}} reward={'1': 9.341, '2': -1.141, '3': 3.314, '4': -0.061, '5': -1.5, '6': 9.341, '7': 1.338, '8': -0.061} t=65
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 4, '3': 0, '4': 6, '5': 7, '6': 7, '7': 1, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.075], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.122, 1.0, 0.034, 0.012, 0.012, 0.034, 0.939], 'utility': [-0.192], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.081, 0.015, 0.01, 0.014, 0.064, 1.0], 'utility': [0.161], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.147, 0.01, 0.023, 0.348, 1.0, 0.032, 0.01], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.152, 1.0, 0.769, 0.034, 0.012, 0.012, 0.035], 'utility': [-0.192], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.011, 1.0, 0.086, 0.006, 0.002, 0.003], 'utility': [0.231], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.213, 0.013, 0.032, 0.518, 1.0, 0.041, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.111, 1.0, 0.031, 0.011, 0.011, 0.029, 0.745], 'utility': [-0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.252, 0.076, 0.014, 0.009, 0.014, 0.064, 1.0], 'utility': [0.166], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.144, 0.009, 0.021, 0.295, 1.0, 0.032, 0.01], 'utility': [-0.023], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.13, 1.0, 0.658, 0.03, 0.011, 0.011, 0.032], 'utility': [-0.168], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.036, 0.017, 1.0, 0.183, 0.01, 0.004, 0.005], 'utility': [0.112], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.129, 0.008, 0.02, 0.295, 1.0, 0.03, 0.009], 'utility': [-0.078], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.168, 0.112, 0.044, -0.051, 0.467, 0.166]}} reward={'1': 9.248, '2': -1.488, '3': 3.228, '4': -0.992, '5': -1.023, '6': 9.248, '7': 4.625, '8': -0.992} t=66
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 7, '3': 2, '4': 6, '5': 7, '6': 7, '7': 4, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.084], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.113, 0.848, 0.031, 0.011, 0.012, 0.033, 1.0], 'utility': [-0.059], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.273, 0.087, 0.016, 0.01, 0.015, 0.063, 1.0], 'utility': [0.049], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.15, 0.01, 0.025, 0.412, 1.0, 0.033, 0.011], 'utility': [-0.082], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.178, 1.0, 0.898, 0.039, 0.014, 0.013, 0.038], 'utility': [-0.216], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.007, 1.0, 0.036, 0.003, 0.001, 0.002], 'utility': [0.387], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.34, 0.02, 0.051, 0.881, 1.0, 0.054, 0.02], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.075], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.122, 1.0, 0.034, 0.012, 0.012, 0.034, 0.939], 'utility': [-0.192], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.081, 0.015, 0.01, 0.014, 0.064, 1.0], 'utility': [0.161], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.147, 0.01, 0.023, 0.348, 1.0, 0.032, 0.01], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.152, 1.0, 0.769, 0.034, 0.012, 0.012, 0.035], 'utility': [-0.192], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.011, 1.0, 0.086, 0.006, 0.002, 0.003], 'utility': [0.231], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.213, 0.013, 0.032, 0.518, 1.0, 0.041, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.192, 0.231, -0.05, -0.05, 0.462, 0.161]}} reward={'1': 9.16, '2': -1.429, '3': 0.252, '4': -1.418, '5': 0.748, '6': 9.16, '7': 7.747, '8': -1.418} t=67
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 1, '3': 2, '4': 6, '5': 7, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.089], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.098, 0.677, 0.027, 0.01, 0.01, 0.03, 1.0], 'utility': [-0.058], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.285, 0.093, 0.017, 0.01, 0.015, 0.063, 1.0], 'utility': [0.045], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.153, 0.011, 0.027, 0.491, 1.0, 0.034, 0.011], 'utility': [-0.103], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.199, 0.955, 1.0, 0.043, 0.015, 0.014, 0.04], 'utility': [-0.239], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.008, 0.004, 1.0, 0.014, 0.001, 0.001, 0.001], 'utility': [0.55], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.363, 0.02, 0.055, 1.0, 0.689, 0.048, 0.019], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.084], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.113, 0.848, 0.031, 0.011, 0.012, 0.033, 1.0], 'utility': [-0.059], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.273, 0.087, 0.016, 0.01, 0.015, 0.063, 1.0], 'utility': [0.049], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.15, 0.01, 0.025, 0.412, 1.0, 0.033, 0.011], 'utility': [-0.082], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.178, 1.0, 0.898, 0.039, 0.014, 0.013, 0.038], 'utility': [-0.216], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.007, 1.0, 0.036, 0.003, 0.001, 0.002], 'utility': [0.387], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.34, 0.02, 0.051, 0.881, 1.0, 0.054, 0.02], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.049, -0.138, 0.387, -0.071, -0.071, 0.458, -0.005]}} reward={'1': 9.107, '2': -1.549, '3': 0.215, '4': -1.698, '5': 1.687, '6': 9.107, '7': 11.001, '8': -1.178} t=68
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 2, '4': 6, '5': 7, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.085, 0.542, 0.023, 0.009, 0.009, 0.027, 1.0], 'utility': [-0.054], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.297, 0.101, 0.018, 0.011, 0.015, 0.063, 1.0], 'utility': [-0.004], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.157, 0.012, 0.03, 0.586, 1.0, 0.035, 0.012], 'utility': [-0.12], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.201, 0.822, 1.0, 0.043, 0.014, 0.014, 0.038], 'utility': [-0.262], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.007, 0.001, 0.0, 0.001], 'utility': [0.676], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '8': {'connected': [1, 0, 0, 1, 1, 0, 0], 'dr': [0.343, 0.018, 0.053, 1.0, 0.433, 0.038, 0.016], 'utility': [-0.022], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.089], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.098, 0.677, 0.027, 0.01, 0.01, 0.03, 1.0], 'utility': [-0.058], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.285, 0.093, 0.017, 0.01, 0.015, 0.063, 1.0], 'utility': [0.045], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.153, 0.011, 0.027, 0.491, 1.0, 0.034, 0.011], 'utility': [-0.103], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.199, 0.955, 1.0, 0.043, 0.015, 0.014, 0.04], 'utility': [-0.239], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.008, 0.004, 1.0, 0.014, 0.001, 0.001, 0.001], 'utility': [0.55], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.363, 0.02, 0.055, 1.0, 0.689, 0.048, 0.019], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [0.045, -0.148, 0.55, -0.085, -0.085, 0.455, -0.006]}} reward={'1': 9.4, '2': -1.865, '3': -0.414, '4': -1.418, '5': 2.399, '6': 9.4, '7': 13.514, '8': -1.031} t=69
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 2, '4': 6, '5': 7, '6': 7, '7': 4, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.074, 0.436, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.31, 0.109, 0.019, 0.011, 0.016, 0.063, 1.0], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.162, 0.012, 0.032, 0.701, 1.0, 0.036, 0.013], 'utility': [-0.13], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.204, 0.71, 1.0, 0.043, 0.014, 0.013, 0.036], 'utility': [-0.285], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.006, 0.004, 1.0, 0.005, 0.001, 0.0, 0.001], 'utility': [0.687], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '8': {'connected': [1, 0, 0, 1, 1, 0, 0], 'dr': [0.327, 0.017, 0.052, 1.0, 0.283, 0.03, 0.014], 'utility': [-0.011], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.085, 0.542, 0.023, 0.009, 0.009, 0.027, 1.0], 'utility': [-0.054], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.297, 0.101, 0.018, 0.011, 0.015, 0.063, 1.0], 'utility': [-0.004], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.157, 0.012, 0.03, 0.586, 1.0, 0.035, 0.012], 'utility': [-0.12], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.201, 0.822, 1.0, 0.043, 0.014, 0.014, 0.038], 'utility': [-0.262], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.007, 0.001, 0.0, 0.001], 'utility': [0.676], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}, '8': {'connected': [1, 0, 0, 1, 1, 0, 0], 'dr': [0.343, 0.018, 0.053, 1.0, 0.433, 0.038, 0.016], 'utility': [-0.022], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.013, -0.158, 0.676, -0.071, -0.071, 0.47, -0.029]}} reward={'1': 10.083, '2': -1.939, '3': -0.377, '4': -1.406, '5': 2.368, '6': 10.083, '7': 13.743, '8': -1.003} t=70
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 2, '4': 6, '5': 7, '6': 7, '7': 4, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.323, 0.117, 0.02, 0.011, 0.016, 0.063, 1.0], 'utility': [-0.014], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.166, 0.013, 0.036, 0.839, 1.0, 0.037, 0.013], 'utility': [0.037], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.208, 0.615, 1.0, 0.043, 0.014, 0.013, 0.034], 'utility': [-0.297], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.008, 1.0, 0.007, 0.001, 0.001, 0.001], 'utility': [0.575], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.315, 0.016, 0.053, 1.0, 0.194, 0.025, 0.013], 'utility': [-0.043], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.074, 0.436, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.31, 0.109, 0.019, 0.011, 0.016, 0.063, 1.0], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.162, 0.012, 0.032, 0.701, 1.0, 0.036, 0.013], 'utility': [-0.13], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.204, 0.71, 1.0, 0.043, 0.014, 0.013, 0.036], 'utility': [-0.285], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.006, 0.004, 1.0, 0.005, 0.001, 0.0, 0.001], 'utility': [0.687], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}, '8': {'connected': [1, 0, 0, 1, 1, 0, 0], 'dr': [0.327, 0.017, 0.052, 1.0, 0.283, 0.03, 0.014], 'utility': [-0.011], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.25, 0.25, 0.25], 'util_at_bs': [-0.01, -0.166, 0.687, -0.07, -0.07, 0.504, -0.028]}} reward={'1': 10.274, '2': -2.025, '3': -0.59, '4': 0.213, '5': 1.54, '6': 10.274, '7': 11.497, '8': -0.312} t=71
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 2, '4': 6, '5': 3, '6': 7, '7': 4, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.338, 0.127, 0.021, 0.012, 0.017, 0.063, 1.0], 'utility': [-0.02], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.17, 0.014, 0.039, 1.0, 0.993, 0.039, 0.014], 'utility': [0.03], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.213, 0.536, 1.0, 0.043, 0.014, 0.013, 0.033], 'utility': [-0.1], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.023, 1.0, 0.012, 0.002, 0.002, 0.003], 'utility': [0.307], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.31, 0.015, 0.057, 1.0, 0.139, 0.021, 0.012], 'utility': [-0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.323, 0.117, 0.02, 0.011, 0.016, 0.063, 1.0], 'utility': [-0.014], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.166, 0.013, 0.036, 0.839, 1.0, 0.037, 0.013], 'utility': [0.037], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.208, 0.615, 1.0, 0.043, 0.014, 0.013, 0.034], 'utility': [-0.297], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.008, 1.0, 0.007, 0.001, 0.001, 0.001], 'utility': [0.575], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.315, 0.016, 0.053, 1.0, 0.194, 0.025, 0.013], 'utility': [-0.043], 'ues_at_bs': [0.25, 0.25, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.172, 0.575, -0.003, 0.037, 0.514, -0.031]}} reward={'1': 10.271, '2': -1.098, '3': -0.552, '4': 0.263, '5': 0.283, '6': 10.271, '7': 2.068, '8': -0.16} t=72
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 3, '3': 2, '4': 1, '5': 7, '6': 7, '7': 7, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.019], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.052], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.353, 0.138, 0.022, 0.012, 0.017, 0.063, 1.0], 'utility': [-0.026], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.146, 0.013, 0.035, 1.0, 0.828, 0.034, 0.012], 'utility': [0.025], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.219, 0.47, 1.0, 0.043, 0.014, 0.012, 0.031], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.064, 0.069, 1.0, 0.02, 0.005, 0.004, 0.007], 'utility': [0.018], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.312, 0.016, 0.064, 1.0, 0.106, 0.018, 0.011], 'utility': [-0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.338, 0.127, 0.021, 0.012, 0.017, 0.063, 1.0], 'utility': [-0.02], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.17, 0.014, 0.039, 1.0, 0.993, 0.039, 0.014], 'utility': [0.03], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.213, 0.536, 1.0, 0.043, 0.014, 0.013, 0.033], 'utility': [-0.1], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.023, 1.0, 0.012, 0.002, 0.002, 0.003], 'utility': [0.307], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.31, 0.015, 0.057, 1.0, 0.139, 0.021, 0.012], 'utility': [-0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.075, 0.103, 0.005, 0.03, 0.514, -0.035]}} reward={'1': 10.194, '2': -0.74, '3': -0.558, '4': 0.278, '5': -0.346, '6': 10.194, '7': 0.007, '8': -0.084} t=73
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 3, '3': 2, '4': 1, '5': 7, '6': 7, '7': 7, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.013], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.075, 0.404, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.046], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.368, 0.15, 0.023, 0.013, 0.017, 0.064, 1.0], 'utility': [-0.031], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.032, 1.0, 0.69, 0.029, 0.011], 'utility': [0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.227, 0.414, 1.0, 0.044, 0.014, 0.012, 0.03], 'utility': [-0.059], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [0.942], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.132, 0.196, 1.0, 0.032, 0.009, 0.007, 0.017], 'utility': [-0.035], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.322, 0.017, 0.076, 1.0, 0.086, 0.017, 0.011], 'utility': [-0.004], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.019], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.052], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.353, 0.138, 0.022, 0.012, 0.017, 0.063, 1.0], 'utility': [-0.026], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.146, 0.013, 0.035, 1.0, 0.828, 0.034, 0.012], 'utility': [0.025], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.219, 0.47, 1.0, 0.043, 0.014, 0.012, 0.031], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.064, 0.069, 1.0, 0.02, 0.005, 0.004, 0.007], 'utility': [0.018], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.312, 0.016, 0.064, 1.0, 0.106, 0.018, 0.011], 'utility': [-0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.035, 0.0, 0.008, 0.025, 0.51, -0.039]}} reward={'1': 9.55, '2': -0.909, '3': -0.563, '4': 0.252, '5': -0.994, '6': 9.55, '7': -0.994, '8': -0.093} t=74
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 3, '3': 2, '4': 1, '5': 0, '6': 7, '7': 7, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 0.4, 0.019, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.041], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.384, 0.163, 0.025, 0.014, 0.018, 0.064, 1.0], 'utility': [-0.037], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.109, 0.01, 0.03, 1.0, 0.576, 0.025, 0.01], 'utility': [0.019], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.236, 0.367, 1.0, 0.045, 0.014, 0.012, 0.029], 'utility': [-0.033], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.821], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.242, 0.537, 1.0, 0.046, 0.015, 0.014, 0.035], 'utility': [-0.196], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.34, 0.019, 0.097, 1.0, 0.074, 0.017, 0.012], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.013], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.075, 0.404, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.046], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.368, 0.15, 0.023, 0.013, 0.017, 0.064, 1.0], 'utility': [-0.031], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.032, 1.0, 0.69, 0.029, 0.011], 'utility': [0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.227, 0.414, 1.0, 0.044, 0.014, 0.012, 0.03], 'utility': [-0.059], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [0.942], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.132, 0.196, 1.0, 0.032, 0.009, 0.007, 0.017], 'utility': [-0.035], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.322, 0.017, 0.076, 1.0, 0.086, 0.017, 0.011], 'utility': [-0.004], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.052, -0.047, 0.008, 0.021, 0.478, -0.039]}} reward={'1': 8.281, '2': -0.766, '3': -0.628, '4': 0.187, '5': -1.168, '6': 8.281, '7': -1.517, '8': -0.188} t=75
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 1, '3': 0, '4': 1, '5': 0, '6': 7, '7': 7, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.004], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.087, 0.398, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.04], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.401, 0.177, 0.026, 0.014, 0.019, 0.065, 1.0], 'utility': [-0.044], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.094, 0.009, 0.027, 1.0, 0.482, 0.022, 0.009], 'utility': [0.018], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.248, 0.328, 1.0, 0.047, 0.014, 0.012, 0.028], 'utility': [-0.05], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.714], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.269, 1.0, 0.682, 0.043, 0.016, 0.016, 0.046], 'utility': [-0.275], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.368, 0.023, 0.13, 1.0, 0.067, 0.017, 0.013], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 0.4, 0.019, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.041], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.384, 0.163, 0.025, 0.014, 0.018, 0.064, 1.0], 'utility': [-0.037], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.109, 0.01, 0.03, 1.0, 0.576, 0.025, 0.01], 'utility': [0.019], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.236, 0.367, 1.0, 0.045, 0.014, 0.012, 0.029], 'utility': [-0.033], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.821], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.242, 0.537, 1.0, 0.046, 0.015, 0.014, 0.035], 'utility': [-0.196], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.34, 0.019, 0.097, 1.0, 0.074, 0.017, 0.012], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.037, -0.114, 0.005, 0.019, 0.414, -0.039]}} reward={'1': 7.178, '2': -0.863, '3': -0.751, '4': 0.084, '5': -1.604, '6': 7.178, '7': -2.07, '8': -0.363} t=76
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 1, '3': 0, '4': 1, '5': 0, '6': 7, '7': 2, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.0], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.097, 0.399, 0.02, 0.008, 0.009, 0.026, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.419, 0.193, 0.028, 0.015, 0.019, 0.065, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.081, 0.008, 0.025, 1.0, 0.404, 0.019, 0.008], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.262, 0.296, 1.0, 0.049, 0.014, 0.012, 0.028], 'utility': [-0.016], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.003, 1.0, 0.001], 'utility': [0.621], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.142, 1.0, 0.244, 0.02, 0.008, 0.009, 0.031], 'utility': [-0.254], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.403, 0.028, 0.184, 1.0, 0.064, 0.018, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.004], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.087, 0.398, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.04], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.401, 0.177, 0.026, 0.014, 0.019, 0.065, 1.0], 'utility': [-0.044], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.094, 0.009, 0.027, 1.0, 0.482, 0.022, 0.009], 'utility': [0.018], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.248, 0.328, 1.0, 0.047, 0.014, 0.012, 0.028], 'utility': [-0.05], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.714], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.269, 1.0, 0.682, 0.043, 0.016, 0.016, 0.046], 'utility': [-0.275], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.368, 0.023, 0.13, 1.0, 0.067, 0.017, 0.013], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.045, -0.162, -0.003, 0.018, 0.359, -0.042]}} reward={'1': 6.211, '2': -1.656, '3': -0.957, '4': -0.048, '5': -1.95, '6': 6.211, '7': -2.351, '8': -0.605} t=77
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 1, '3': 0, '4': 1, '5': 0, '6': 7, '7': 7, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.002], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.11, 0.403, 0.021, 0.009, 0.009, 0.028, 1.0], 'utility': [-0.048], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.437, 0.211, 0.03, 0.016, 0.02, 0.066, 1.0], 'utility': [-0.056], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.278, 0.268, 1.0, 0.051, 0.015, 0.012, 0.027], 'utility': [0.065], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.537], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.082, 0.008, 0.004, 0.005, 0.018], 'utility': [-0.371], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.444, 0.036, 0.273, 1.0, 0.064, 0.019, 0.017], 'utility': [-0.072], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.0], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.097, 0.399, 0.02, 0.008, 0.009, 0.026, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.419, 0.193, 0.028, 0.015, 0.019, 0.065, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.081, 0.008, 0.025, 1.0, 0.404, 0.019, 0.008], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.262, 0.296, 1.0, 0.049, 0.014, 0.012, 0.028], 'utility': [-0.016], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.003, 1.0, 0.001], 'utility': [0.621], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.142, 1.0, 0.244, 0.02, 0.008, 0.009, 0.031], 'utility': [-0.254], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.403, 0.028, 0.184, 1.0, 0.064, 0.018, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.135, -0.013, 0.019, 0.311, -0.048]}} reward={'1': 5.349, '2': -1.826, '3': -1.161, '4': -0.228, '5': -1.387, '6': 5.349, '7': -2.352, '8': -0.466} t=78
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 1, '3': 0, '4': 1, '5': 0, '6': 7, '7': 3, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.005], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.128, 0.409, 0.023, 0.009, 0.01, 0.03, 1.0], 'utility': [-0.052], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.456, 0.231, 0.032, 0.016, 0.02, 0.067, 1.0], 'utility': [-0.062], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.298, 0.245, 1.0, 0.054, 0.015, 0.013, 0.027], 'utility': [0.001], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.0, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.462], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.025, 0.003, 0.002, 0.002, 0.009], 'utility': [-0.375], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.491, 0.047, 0.421, 1.0, 0.065, 0.021, 0.02], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.002], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.11, 0.403, 0.021, 0.009, 0.009, 0.028, 1.0], 'utility': [-0.048], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.437, 0.211, 0.03, 0.016, 0.02, 0.066, 1.0], 'utility': [-0.056], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.278, 0.268, 1.0, 0.051, 0.015, 0.012, 0.027], 'utility': [0.065], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.537], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.082, 0.008, 0.004, 0.005, 0.018], 'utility': [-0.371], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.444, 0.036, 0.273, 1.0, 0.064, 0.019, 0.017], 'utility': [-0.072], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}} reward={'1': 4.574, '2': -2.164, '3': -1.24, '4': -0.217, '5': -1.797, '6': 4.574, '7': -2.84, '8': -0.848} t=79
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 1, '3': 0, '4': 1, '5': 0, '6': 7, '7': 3, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.006], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.151, 0.418, 0.025, 0.01, 0.011, 0.033, 1.0], 'utility': [-0.061], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.475, 0.252, 0.034, 0.017, 0.021, 0.067, 1.0], 'utility': [-0.069], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.321, 0.226, 1.0, 0.058, 0.016, 0.013, 0.027], 'utility': [-0.017], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.01, 1.0, 0.003], 'utility': [0.393], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.386], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.54, 0.061, 0.676, 1.0, 0.068, 0.024, 0.024], 'utility': [-0.08], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.005], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.128, 0.409, 0.023, 0.009, 0.01, 0.03, 1.0], 'utility': [-0.052], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.456, 0.231, 0.032, 0.016, 0.02, 0.067, 1.0], 'utility': [-0.062], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.298, 0.245, 1.0, 0.054, 0.015, 0.013, 0.027], 'utility': [0.001], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.0, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.462], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.025, 0.003, 0.002, 0.002, 0.009], 'utility': [-0.375], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.491, 0.047, 0.421, 1.0, 0.065, 0.021, 0.02], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}} reward={'1': 3.87, '2': -2.381, '3': -1.398, '4': -0.28, '5': -2.032, '6': 3.87, '7': -3.099, '8': -1.025} t=80
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 1, '3': 0, '4': 1, '5': 0, '6': 7, '7': 3, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.182, 0.43, 0.028, 0.011, 0.012, 0.037, 1.0], 'utility': [0.002], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.495, 0.277, 0.036, 0.018, 0.022, 0.068, 1.0], 'utility': [-0.075], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.1, 0.01, 0.028, 1.0, 0.539, 0.024, 0.009], 'utility': [0.017], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.348, 0.21, 1.0, 0.062, 0.017, 0.013, 0.027], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.014, 1.0, 0.004], 'utility': [0.33], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.172], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.527, 0.072, 1.0, 0.893, 0.064, 0.024, 0.026], 'utility': [-0.083], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.006], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.151, 0.418, 0.025, 0.01, 0.011, 0.033, 1.0], 'utility': [-0.061], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.475, 0.252, 0.034, 0.017, 0.021, 0.067, 1.0], 'utility': [-0.069], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.321, 0.226, 1.0, 0.058, 0.016, 0.013, 0.027], 'utility': [-0.017], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.01, 1.0, 0.003], 'utility': [0.393], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.386], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.54, 0.061, 0.676, 1.0, 0.068, 0.024, 0.024], 'utility': [-0.08], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}} reward={'1': 3.226, '2': -1.221, '3': -1.343, '4': -0.327, '5': -1.563, '6': 3.226, '7': -1.704, '8': -1.263} t=81
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 1, '3': 0, '4': 1, '5': 6, '6': 7, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.223, 0.443, 0.031, 0.013, 0.014, 0.041, 1.0], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.515, 0.303, 0.038, 0.019, 0.022, 0.069, 1.0], 'utility': [-0.082], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.033, 1.0, 0.742, 0.03, 0.011], 'utility': [0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.379, 0.197, 1.0, 0.067, 0.018, 0.014, 0.027], 'utility': [-0.101], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.311], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.179], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.333, 0.056, 1.0, 0.521, 0.04, 0.016, 0.018], 'utility': [-0.058], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.182, 0.43, 0.028, 0.011, 0.012, 0.037, 1.0], 'utility': [0.002], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.495, 0.277, 0.036, 0.018, 0.022, 0.068, 1.0], 'utility': [-0.075], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.1, 0.01, 0.028, 1.0, 0.539, 0.024, 0.009], 'utility': [0.017], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.348, 0.21, 1.0, 0.062, 0.017, 0.013, 0.027], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.014, 1.0, 0.004], 'utility': [0.33], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.172], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.527, 0.072, 1.0, 0.893, 0.064, 0.024, 0.026], 'utility': [-0.083], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}} reward={'1': 2.9, '2': -1.4, '3': -1.399, '4': -0.103, '5': -1.49, '6': 2.9, '7': -1.886, '8': -1.115} t=82
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 1, '3': 0, '4': 3, '5': 6, '6': 7, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.027], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.279, 0.459, 0.035, 0.015, 0.016, 0.047, 1.0], 'utility': [-0.029], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.536, 0.333, 0.041, 0.02, 0.023, 0.07, 1.0], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.155, 0.013, 0.037, 0.978, 1.0, 0.037, 0.013], 'utility': [0.031], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.416, 0.186, 1.0, 0.073, 0.019, 0.014, 0.028], 'utility': [-0.143], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.318], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.061, 0.007, 0.003, 0.004, 0.016], 'utility': [-0.202], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.201, 0.041, 1.0, 0.293, 0.024, 0.01, 0.012], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.223, 0.443, 0.031, 0.013, 0.014, 0.041, 1.0], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.515, 0.303, 0.038, 0.019, 0.022, 0.069, 1.0], 'utility': [-0.082], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.033, 1.0, 0.742, 0.03, 0.011], 'utility': [0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.379, 0.197, 1.0, 0.067, 0.018, 0.014, 0.027], 'utility': [-0.101], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.311], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.179], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.333, 0.056, 1.0, 0.521, 0.04, 0.016, 0.018], 'utility': [-0.058], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.07, -0.094, -0.079, -0.018, 0.021, 0.145, -0.046]}} reward={'1': 2.9, '2': -1.23, '3': -1.23, '4': 0.205, '5': -1.319, '6': 2.9, '7': -2.313, '8': -0.873} t=83
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 1, '3': 0, '4': 3, '5': 6, '6': 7, '7': 3, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.023], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.354, 0.477, 0.04, 0.017, 0.019, 0.054, 1.0], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.558, 0.366, 0.043, 0.021, 0.024, 0.071, 1.0], 'utility': [-0.095], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.012, 0.031, 0.708, 1.0, 0.034, 0.012], 'utility': [0.047], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.459, 0.177, 1.0, 0.081, 0.021, 0.015, 0.028], 'utility': [-0.145], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.313], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.125, 1.0, 0.185, 0.017, 0.007, 0.008, 0.028], 'utility': [-0.235], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.115, 0.029, 1.0, 0.158, 0.014, 0.006, 0.008], 'utility': [0.033], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.027], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.279, 0.459, 0.035, 0.015, 0.016, 0.047, 1.0], 'utility': [-0.029], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.536, 0.333, 0.041, 0.02, 0.023, 0.07, 1.0], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.155, 0.013, 0.037, 0.978, 1.0, 0.037, 0.013], 'utility': [0.031], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.416, 0.186, 1.0, 0.073, 0.019, 0.014, 0.028], 'utility': [-0.143], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.318], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.061, 0.007, 0.003, 0.004, 0.016], 'utility': [-0.202], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.201, 0.041, 1.0, 0.293, 0.024, 0.01, 0.012], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.024, -0.116, -0.087, -0.0, 0.031, 0.145, -0.026]}} reward={'1': 2.9, '2': -1.562, '3': -1.562, '4': 0.847, '5': -1.108, '6': 2.9, '7': -1.806, '8': -0.159} t=84
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 5, '3': 2, '4': 2, '5': 6, '6': 7, '7': 3, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.067], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.456, 0.495, 0.046, 0.02, 0.022, 0.062, 1.0], 'utility': [-0.068], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.579, 0.403, 0.046, 0.022, 0.025, 0.072, 1.0], 'utility': [-0.055], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.127, 0.01, 0.025, 0.512, 1.0, 0.031, 0.01], 'utility': [0.108], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.509, 0.17, 1.0, 0.089, 0.022, 0.016, 0.029], 'utility': [-0.258], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.001, 0.001, 0.011, 1.0, 0.003], 'utility': [0.425], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.251, 1.0, 0.518, 0.037, 0.014, 0.015, 0.044], 'utility': [-0.276], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.062, 0.019, 1.0, 0.081, 0.008, 0.004, 0.005], 'utility': [0.069], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.023], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.354, 0.477, 0.04, 0.017, 0.019, 0.054, 1.0], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.558, 0.366, 0.043, 0.021, 0.024, 0.071, 1.0], 'utility': [-0.095], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.012, 0.031, 0.708, 1.0, 0.034, 0.012], 'utility': [0.047], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.459, 0.177, 1.0, 0.081, 0.021, 0.015, 0.028], 'utility': [-0.145], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.313], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.125, 1.0, 0.185, 0.017, 0.007, 0.008, 0.028], 'utility': [-0.235], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.115, 0.029, 1.0, 0.158, 0.014, 0.006, 0.008], 'utility': [0.033], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.125, -0.056, 0.04, 0.047, 0.145, -0.055]}} reward={'1': 3.575, '2': -1.844, '3': -1.844, '4': 2.161, '5': -2.351, '6': 3.575, '7': -2.879, '8': -3.098} t=85
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 5, '3': 1, '4': 2, '5': 6, '6': 7, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.596, 0.515, 0.053, 0.023, 0.026, 0.072, 1.0], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.602, 0.444, 0.049, 0.023, 0.025, 0.073, 1.0], 'utility': [-0.145], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.114, 0.009, 0.021, 0.371, 1.0, 0.028, 0.009], 'utility': [0.124], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.566, 0.164, 1.0, 0.1, 0.024, 0.017, 0.03], 'utility': [-0.251], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.472], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.319, 0.722, 1.0, 0.055, 0.018, 0.017, 0.045], 'utility': [-0.222], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.012, 1.0, 0.038, 0.004, 0.002, 0.003], 'utility': [0.168], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.067], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.456, 0.495, 0.046, 0.02, 0.022, 0.062, 1.0], 'utility': [-0.068], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.579, 0.403, 0.046, 0.022, 0.025, 0.072, 1.0], 'utility': [-0.055], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.127, 0.01, 0.025, 0.512, 1.0, 0.031, 0.01], 'utility': [0.108], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.509, 0.17, 1.0, 0.089, 0.022, 0.016, 0.029], 'utility': [-0.258], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.001, 0.001, 0.011, 1.0, 0.003], 'utility': [0.425], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.251, 1.0, 0.518, 0.037, 0.014, 0.015, 0.044], 'utility': [-0.276], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.062, 0.019, 1.0, 0.081, 0.008, 0.004, 0.005], 'utility': [0.069], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.133, -0.155, 0.108, 0.108, 0.179, -0.062]}} reward={'1': 4.408, '2': -1.87, '3': -1.87, '4': 2.489, '5': -1.611, '6': 4.408, '7': -2.297, '8': -2.038} t=86
DEBUG:deepcomp.util.simulation:Step                           action={'1': 0, '2': 5, '3': 2, '4': 2, '5': 6, '6': 7, '7': 6, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.79, 0.536, 0.061, 0.028, 0.031, 0.084, 1.0], 'utility': [0.003], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.624, 0.489, 0.053, 0.024, 0.026, 0.074, 1.0], 'utility': [-0.221], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.102, 0.007, 0.017, 0.269, 1.0, 0.026, 0.008], 'utility': [0.146], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.632, 0.159, 1.0, 0.112, 0.027, 0.018, 0.031], 'utility': [-0.29], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.572], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.191, 0.274, 1.0, 0.04, 0.012, 0.01, 0.023], 'utility': [-0.133], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.006, 1.0, 0.016, 0.002, 0.001, 0.001], 'utility': [0.336], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.596, 0.515, 0.053, 0.023, 0.026, 0.072, 1.0], 'utility': [-0.016], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.602, 0.444, 0.049, 0.023, 0.025, 0.073, 1.0], 'utility': [-0.145], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.114, 0.009, 0.021, 0.371, 1.0, 0.028, 0.009], 'utility': [0.124], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.566, 0.164, 1.0, 0.1, 0.024, 0.017, 0.03], 'utility': [-0.251], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.472], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.319, 0.722, 1.0, 0.055, 0.018, 0.017, 0.045], 'utility': [-0.222], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.012, 1.0, 0.038, 0.004, 0.002, 0.003], 'utility': [0.168], 'ues_at_bs': [0.125, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.016, -0.128, -0.102, 0.124, 0.124, 0.22, -0.081]}} reward={'1': 5.119, '2': -1.378, '3': -1.378, '4': 2.915, '5': -0.422, '6': 5.119, '7': -0.871, '8': -0.584} t=87
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 3, '4': 7, '5': 6, '6': 7, '7': 6, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.525, 0.067, 0.031, 0.034, 0.093, 0.942], 'utility': [0.045], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.647, 0.54, 0.056, 0.025, 0.027, 0.076, 1.0], 'utility': [-0.23], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.091, 0.006, 0.014, 0.196, 1.0, 0.024, 0.007], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.707, 0.156, 1.0, 0.126, 0.029, 0.019, 0.032], 'utility': [-0.343], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.545], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.104, 0.104, 1.0, 0.028, 0.007, 0.005, 0.011], 'utility': [-0.005], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.006, 0.001, 0.0, 0.001], 'utility': [0.463], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.79, 0.536, 0.061, 0.028, 0.031, 0.084, 1.0], 'utility': [0.003], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.624, 0.489, 0.053, 0.024, 0.026, 0.074, 1.0], 'utility': [-0.221], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.102, 0.007, 0.017, 0.269, 1.0, 0.026, 0.008], 'utility': [0.146], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.632, 0.159, 1.0, 0.112, 0.027, 0.018, 0.031], 'utility': [-0.29], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.572], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.191, 0.274, 1.0, 0.04, 0.012, 0.01, 0.023], 'utility': [-0.133], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.006, 1.0, 0.016, 0.002, 0.001, 0.001], 'utility': [0.336], 'ues_at_bs': [0.125, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.003, -0.065, -0.029, 0.146, 0.146, 0.256, -0.109]}} reward={'1': 5.363, '2': -0.477, '3': -0.477, '4': 3.417, '5': 0.799, '6': 5.363, '7': 0.765, '8': 0.765} t=88
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 3, '4': 7, '5': 6, '6': 7, '7': 7, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.4, 0.058, 0.027, 0.03, 0.08, 0.692], 'utility': [0.058], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.67, 0.596, 0.06, 0.026, 0.028, 0.077, 1.0], 'utility': [-0.24], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.082, 0.005, 0.012, 0.144, 1.0, 0.022, 0.006], 'utility': [0.199], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.792, 0.153, 1.0, 0.143, 0.033, 0.021, 0.033], 'utility': [-0.349], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.575], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.052, 0.04, 1.0, 0.019, 0.004, 0.003, 0.005], 'utility': [0.028], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.002, 0.001, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.774], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.525, 0.067, 0.031, 0.034, 0.093, 0.942], 'utility': [0.045], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.647, 0.54, 0.056, 0.025, 0.027, 0.076, 1.0], 'utility': [-0.23], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.091, 0.006, 0.014, 0.196, 1.0, 0.024, 0.007], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.707, 0.156, 1.0, 0.126, 0.029, 0.019, 0.032], 'utility': [-0.343], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.545], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.104, 0.104, 1.0, 0.028, 0.007, 0.005, 0.011], 'utility': [-0.005], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.006, 0.001, 0.0, 0.001], 'utility': [0.463], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.045, 0.045, 0.038, 0.171, 0.171, 0.268, -0.093]}} reward={'1': 5.367, '2': -0.328, '3': -0.328, '4': 3.971, '5': 2.559, '6': 5.367, '7': 3.024, '8': 3.024} t=89
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 3, '4': 7, '5': 6, '6': 7, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.014], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.3, 0.049, 0.024, 0.026, 0.068, 0.501], 'utility': [0.077], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.693, 0.659, 0.064, 0.027, 0.029, 0.078, 1.0], 'utility': [-0.25], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.073, 0.005, 0.01, 0.106, 1.0, 0.02, 0.006], 'utility': [0.228], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.888, 0.151, 1.0, 0.163, 0.036, 0.023, 0.035], 'utility': [-0.411], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.551], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.016, 1.0, 0.013, 0.002, 0.001, 0.002], 'utility': [0.188], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.4, 0.058, 0.027, 0.03, 0.08, 0.692], 'utility': [0.058], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.67, 0.596, 0.06, 0.026, 0.028, 0.077, 1.0], 'utility': [-0.24], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.082, 0.005, 0.012, 0.144, 1.0, 0.022, 0.006], 'utility': [0.199], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.792, 0.153, 1.0, 0.143, 0.033, 0.021, 0.033], 'utility': [-0.349], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.575], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.052, 0.04, 1.0, 0.019, 0.004, 0.003, 0.005], 'utility': [0.028], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.002, 0.001, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.774], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.058, 0.058, 0.151, 0.199, 0.199, 0.268, -0.091]}} reward={'1': 5.37, '2': -0.091, '3': -0.091, '4': 4.552, '5': 4.274, '6': 5.37, '7': 5.184, '8': 5.184} t=90
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 3, '4': 7, '5': 6, '6': 7, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.105], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.222, 0.041, 0.02, 0.023, 0.057, 0.358], 'utility': [0.065], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.717, 0.729, 0.068, 0.029, 0.03, 0.079, 1.0], 'utility': [-0.26], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.066, 0.004, 0.008, 0.08, 1.0, 0.019, 0.005], 'utility': [0.24], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.996, 0.15, 1.0, 0.187, 0.04, 0.025, 0.037], 'utility': [-0.618], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.742], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.008, 1.0, 0.011, 0.002, 0.001, 0.001], 'utility': [-0.03], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.014], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.3, 0.049, 0.024, 0.026, 0.068, 0.501], 'utility': [0.077], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.693, 0.659, 0.064, 0.027, 0.029, 0.078, 1.0], 'utility': [-0.25], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.073, 0.005, 0.01, 0.106, 1.0, 0.02, 0.006], 'utility': [0.228], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.888, 0.151, 1.0, 0.163, 0.036, 0.023, 0.035], 'utility': [-0.411], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.551], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.016, 1.0, 0.013, 0.002, 0.001, 0.002], 'utility': [0.188], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [0.077, 0.077, 0.259, 0.228, 0.228, 0.269, -0.086]}} reward={'1': 6.372, '2': -0.86, '3': -0.86, '4': 4.798, '5': 2.087, '6': 6.372, '7': 2.347, '8': 2.347} t=91
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 3, '4': 4, '5': 2, '6': 7, '7': 7, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.161, 0.033, 0.017, 0.019, 0.047, 0.252], 'utility': [0.106], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.74, 0.807, 0.073, 0.03, 0.031, 0.081, 1.0], 'utility': [-0.27], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.06, 0.003, 0.007, 0.061, 1.0, 0.018, 0.005], 'utility': [0.271], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.134, 0.896, 0.193, 0.04, 0.024, 0.035], 'utility': [-0.365], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.831], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.006, 1.0, 0.014, 0.002, 0.001, 0.001], 'utility': [0.253], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.105], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.222, 0.041, 0.02, 0.023, 0.057, 0.358], 'utility': [0.065], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.717, 0.729, 0.068, 0.029, 0.03, 0.079, 1.0], 'utility': [-0.26], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.066, 0.004, 0.008, 0.08, 1.0, 0.019, 0.005], 'utility': [0.24], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.996, 0.15, 1.0, 0.187, 0.04, 0.025, 0.037], 'utility': [-0.618], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.742], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.008, 1.0, 0.011, 0.002, 0.001, 0.001], 'utility': [-0.03], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.065, 0.0, 0.117, 0.0, 0.24, 0.319, -0.097]}} reward={'1': 7.95, '2': -0.38, '3': -0.38, '4': 5.422, '5': 4.973, '6': 7.95, '7': 5.922, '8': 5.922} t=92
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 2, '4': 4, '5': 6, '6': 7, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.115, 0.027, 0.014, 0.016, 0.038, 0.174], 'utility': [0.153], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.764, 0.895, 0.078, 0.032, 0.032, 0.082, 1.0], 'utility': [-0.057], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.055, 0.003, 0.006, 0.047, 1.0, 0.017, 0.004], 'utility': [0.298], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.12, 0.801, 0.199, 0.041, 0.023, 0.033], 'utility': [-0.269], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.001, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.007, 1.0, 0.026, 0.002, 0.001, 0.002], 'utility': [0.189], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.161, 0.033, 0.017, 0.019, 0.047, 0.252], 'utility': [0.106], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.74, 0.807, 0.073, 0.03, 0.031, 0.081, 1.0], 'utility': [-0.27], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.06, 0.003, 0.007, 0.061, 1.0, 0.018, 0.005], 'utility': [0.271], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.134, 0.896, 0.193, 0.04, 0.024, 0.035], 'utility': [-0.365], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.831], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.006, 1.0, 0.014, 0.002, 0.001, 0.001], 'utility': [0.253], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.106, 0.0, 0.296, 0.0, 0.271, 0.397, -0.082]}} reward={'1': 9.009, '2': 1.666, '3': 0.967, '4': 5.965, '5': 5.367, '6': 9.009, '7': 6.134, '8': 6.134} t=93
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 5, '4': 4, '5': 6, '6': 7, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.041], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.08, 0.021, 0.012, 0.013, 0.03, 0.118], 'utility': [0.207], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.788, 0.992, 0.083, 0.033, 0.033, 0.083, 1.0], 'utility': [-0.052], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.052, 0.003, 0.005, 0.038, 1.0, 0.017, 0.004], 'utility': [0.32], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.108, 0.718, 0.207, 0.041, 0.023, 0.031], 'utility': [-0.368], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.022, 0.009, 1.0, 0.057, 0.004, 0.002, 0.002], 'utility': [0.019], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.099], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.115, 0.027, 0.014, 0.016, 0.038, 0.174], 'utility': [0.153], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.764, 0.895, 0.078, 0.032, 0.032, 0.082, 1.0], 'utility': [-0.057], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.055, 0.003, 0.006, 0.047, 1.0, 0.017, 0.004], 'utility': [0.298], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.12, 0.801, 0.199, 0.041, 0.023, 0.033], 'utility': [-0.269], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.001, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.007, 1.0, 0.026, 0.002, 0.001, 0.002], 'utility': [0.189], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.153, -0.057, 0.307, 0.0, 0.298, 0.45, 0.048]}} reward={'1': 9.591, '2': 2.41, '3': 1.549, '4': 6.402, '5': 4.291, '6': 9.591, '7': 4.343, '8': 4.343} t=94
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 5, '4': 4, '5': 6, '6': 7, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.056], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.055, 0.016, 0.009, 0.011, 0.023, 0.079], 'utility': [0.258], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.737, 1.0, 0.081, 0.031, 0.031, 0.077, 0.908], 'utility': [0.013], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.005, 0.032, 1.0, 0.018, 0.004], 'utility': [0.336], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.097, 0.646, 0.216, 0.042, 0.022, 0.029], 'utility': [-0.23], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.014, 1.0, 0.127, 0.008, 0.003, 0.004], 'utility': [-0.004], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [0.34], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.041], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.08, 0.021, 0.012, 0.013, 0.03, 0.118], 'utility': [0.207], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.788, 0.992, 0.083, 0.033, 0.033, 0.083, 1.0], 'utility': [-0.052], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.052, 0.003, 0.005, 0.038, 1.0, 0.017, 0.004], 'utility': [0.32], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.108, 0.718, 0.207, 0.041, 0.023, 0.031], 'utility': [-0.368], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.022, 0.009, 1.0, 0.057, 0.004, 0.002, 0.002], 'utility': [0.019], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.207, -0.052, 0.217, 0.0, 0.32, 0.48, 0.077]}} reward={'1': 9.442, '2': 5.164, '3': 1.893, '4': 6.71, '5': 1.825, '6': 9.442, '7': 0.712, '8': 0.712} t=95
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 5, '4': 4, '5': 0, '6': 3, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.009], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.036, 0.012, 0.007, 0.008, 0.017, 0.051], 'utility': [0.328], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.682, 1.0, 0.077, 0.03, 0.029, 0.071, 0.817], 'utility': [0.015], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.004, 0.027, 1.0, 0.019, 0.004], 'utility': [0.344], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.089, 0.583, 0.228, 0.042, 0.022, 0.028], 'utility': [-0.246], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.048, 0.02, 1.0, 0.269, 0.013, 0.005, 0.006], 'utility': [-0.018], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.001, 0.001, 1.0, 0.001, 0.0, 0.0, 0.0], 'utility': [0.058], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.056], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.055, 0.016, 0.009, 0.011, 0.023, 0.079], 'utility': [0.258], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.737, 1.0, 0.081, 0.031, 0.031, 0.077, 0.908], 'utility': [0.013], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.005, 0.032, 1.0, 0.018, 0.004], 'utility': [0.336], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.097, 0.646, 0.216, 0.042, 0.022, 0.029], 'utility': [-0.23], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.014, 1.0, 0.127, 0.008, 0.003, 0.004], 'utility': [-0.004], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [0.34], 'ues_at_bs': [0.125, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.258, 0.013, 0.036, 0.0, 0.336, 0.472, 0.013]}} reward={'1': 10.087, '2': 6.563, '3': 2.394, '4': 6.873, '5': 0.613, '6': 10.087, '7': -1.116, '8': -1.37} t=96
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 5, '4': 4, '5': 6, '6': 3, '7': 7, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.023, 0.009, 0.006, 0.006, 0.012, 0.032], 'utility': [0.405], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.631, 1.0, 0.074, 0.028, 0.027, 0.065, 0.735], 'utility': [0.019], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.051, 0.003, 0.004, 0.024, 1.0, 0.021, 0.004], 'utility': [0.344], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.081, 0.529, 0.242, 0.044, 0.022, 0.027], 'utility': [-0.252], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.067, 0.027, 1.0, 0.516, 0.022, 0.008, 0.009], 'utility': [-0.073], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.003, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.015], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.009], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.036, 0.012, 0.007, 0.008, 0.017, 0.051], 'utility': [0.328], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.682, 1.0, 0.077, 0.03, 0.029, 0.071, 0.817], 'utility': [0.015], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.004, 0.027, 1.0, 0.019, 0.004], 'utility': [0.344], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.089, 0.583, 0.228, 0.042, 0.022, 0.028], 'utility': [-0.246], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.048, 0.02, 1.0, 0.269, 0.013, 0.005, 0.006], 'utility': [-0.018], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.001, 0.001, 1.0, 0.001, 0.0, 0.0, 0.0], 'utility': [0.058], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.328, 0.015, -0.068, -0.018, 0.344, 0.504, 0.015]}} reward={'1': 10.026, '2': 8.106, '3': 2.953, '4': 6.88, '5': 0.476, '6': 10.026, '7': -1.918, '8': -2.067} t=97
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 5, '4': 4, '5': 6, '6': 3, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.021], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.014, 0.006, 0.004, 0.005, 0.008, 0.019], 'utility': [0.491], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.582, 1.0, 0.071, 0.026, 0.025, 0.059, 0.66], 'utility': [0.023], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.054, 0.003, 0.004, 0.023, 1.0, 0.025, 0.004], 'utility': [0.337], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.075, 0.482, 0.258, 0.045, 0.022, 0.026], 'utility': [-0.28], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.848], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.102], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.01, 0.009, 1.0, 0.005, 0.001, 0.001, 0.001], 'utility': [0.104], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.003], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.023, 0.009, 0.006, 0.006, 0.012, 0.032], 'utility': [0.405], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.631, 1.0, 0.074, 0.028, 0.027, 0.065, 0.735], 'utility': [0.019], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.051, 0.003, 0.004, 0.024, 1.0, 0.021, 0.004], 'utility': [0.344], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.081, 0.529, 0.242, 0.044, 0.022, 0.027], 'utility': [-0.252], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.067, 0.027, 1.0, 0.516, 0.022, 0.008, 0.009], 'utility': [-0.073], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.003, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.015], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.405, 0.019, -0.103, -0.073, 0.344, 0.501, 0.019]}} reward={'1': 8.691, '2': 9.822, '3': 3.579, '4': 6.73, '5': 1.065, '6': 8.691, '7': -1.901, '8': -1.854} t=98
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 5, '4': 4, '5': 6, '6': 3, '7': 6, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.008, 0.004, 0.003, 0.003, 0.006, 0.011], 'utility': [0.588], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.536, 1.0, 0.068, 0.025, 0.023, 0.054, 0.592], 'utility': [0.028], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.058, 0.003, 0.004, 0.022, 1.0, 0.03, 0.005], 'utility': [0.322], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.07, 0.442, 0.278, 0.047, 0.022, 0.025], 'utility': [-0.356], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.724], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.111], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.021, 1.0, 0.011, 0.002, 0.001, 0.003], 'utility': [0.169], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.021], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.014, 0.006, 0.004, 0.005, 0.008, 0.019], 'utility': [0.491], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.582, 1.0, 0.071, 0.026, 0.025, 0.059, 0.66], 'utility': [0.023], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.054, 0.003, 0.004, 0.023, 1.0, 0.025, 0.004], 'utility': [0.337], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.075, 0.482, 0.258, 0.045, 0.022, 0.026], 'utility': [-0.28], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.848], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.102], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.01, 0.009, 1.0, 0.005, 0.001, 0.001, 0.001], 'utility': [0.104], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.491, 0.023, -0.093, -0.102, 0.337, 0.435, 0.023]}} reward={'1': 7.316, '2': 11.754, '3': 4.288, '4': 6.434, '5': 0.711, '6': 7.316, '7': -2.05, '8': -1.991} t=99
DEBUG:deepcomp.util.simulation:Step                           action={'1': 4, '2': 5, '3': 5, '4': 4, '5': 2, '6': 3, '7': 6, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.012], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.698, 0.033, -0.141, -0.121, 0.3, 0.3, 0.033]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.005, 0.002, 0.002, 0.002, 0.003, 0.006], 'utility': [0.698], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.698, 0.033, -0.141, -0.121, 0.3, 0.3, 0.033]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.493, 1.0, 0.065, 0.023, 0.021, 0.049, 0.531], 'utility': [0.033], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.698, 0.033, -0.141, -0.121, 0.3, 0.3, 0.033]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.065, 0.003, 0.005, 0.022, 1.0, 0.037, 0.006], 'utility': [0.3], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.698, 0.033, -0.141, -0.121, 0.3, 0.3, 0.033]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.065, 0.407, 0.301, 0.049, 0.022, 0.025], 'utility': [-0.374], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.698, 0.033, -0.141, -0.121, 0.3, 0.3, 0.033]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.0, 0.0, 0.0, 0.003, 1.0, 0.003], 'utility': [0.588], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.698, 0.033, -0.141, -0.121, 0.3, 0.3, 0.033]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.121], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.698, 0.033, -0.141, -0.121, 0.3, 0.3, 0.033]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.055, 0.043, 1.0, 0.02, 0.004, 0.003, 0.006], 'utility': [0.07], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.698, 0.033, -0.141, -0.121, 0.3, 0.3, 0.033]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.008, 0.004, 0.003, 0.003, 0.006, 0.011], 'utility': [0.588], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.536, 1.0, 0.068, 0.025, 0.023, 0.054, 0.592], 'utility': [0.028], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.058, 0.003, 0.004, 0.022, 1.0, 0.03, 0.005], 'utility': [0.322], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.07, 0.442, 0.278, 0.047, 0.022, 0.025], 'utility': [-0.356], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.724], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.111], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.021, 1.0, 0.011, 0.002, 0.001, 0.003], 'utility': [0.169], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.588, 0.028, -0.1, -0.111, 0.322, 0.366, 0.028]}} reward={'1': 5.997, '2': 13.958, '3': 5.098, '4': 6.007, '5': 0.613, '6': 5.997, '7': -2.723, '8': -2.826} t=100
INFO:deepcomp.util.simulation:Video saved                    path=/home/abhishek/cmc/result/D3-CoMP/good/videos/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-29_11-21-42.html
INFO:deepcomp.util.simulation:Gif saved                      path=/home/abhishek/cmc/result/D3-CoMP/good/videos/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-29_11-21-42.gif
DEBUG:deepcomp.util.simulation:Episode complete               avg_step_reward=16.296 eps_duration=500.466 scalar_metrics=['sum_utility'] vector_metrics=['dr', 'utility']
INFO:deepcomp.util.simulation:Scalar results                 results={'episode': [0], 'eps_duration_mean': [500.466], 'eps_duration_std': [500.466], 'step_reward_mean': [16.296], 'step_reward_std': [16.98], 'sum_utility_mean': [13.093], 'sum_utility_std': [15.178]}
INFO:deepcomp.util.simulation:Mean results                   results={'episode': 0.0, 'eps_duration_mean': 500.466, 'eps_duration_std': 500.466, 'step_reward_mean': 16.296, 'step_reward_std': 16.98, 'sum_utility_mean': 13.093, 'sum_utility_std': 15.178}
INFO:deepcomp.util.simulation:Simulation complete            avg_eps_reward=1629.6 eps_length=100 num_episodes=1 step_reward_mean=16.296 step_reward_std=0.0
INFO:deepcomp.util.simulation:Starting evaluation            fast_ues=2 num_episodes=100 num_workers=1 slow_ues=5 static_ues=1
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [07:57<00:00,  4.77s/it]
INFO:deepcomp.util.simulation:Scalar results                 results={'episode': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 'eps_duration_mean': [4.522, 5.021, 4.709, 4.869, 4.781, 4.724, 5.556, 4.442, 4.284, 4.3, 4.257, 8.236, 5.789, 4.343, 5.941, 4.573, 4.272, 4.195, 5.266, 4.354, 4.099, 4.329, 5.613, 4.286, 4.365, 5.721, 4.089, 6.054, 4.384, 4.089, 4.212, 4.32, 4.274, 4.526, 6.398, 4.324, 4.168, 6.392, 4.312, 4.584, 4.284, 4.531, 5.631, 5.663, 4.357, 5.938, 4.301, 4.31, 4.23, 4.686, 4.396, 4.307, 4.396, 5.672, 4.36, 6.02, 4.309, 4.212, 4.251, 4.427, 5.721, 4.343, 4.171, 6.643, 4.191, 5.863, 4.335, 4.295, 4.242, 4.345, 6.667, 4.483, 4.281, 4.52, 4.461, 4.186, 4.524, 6.233, 4.569, 4.728, 4.169, 6.084, 4.02, 5.689, 4.499, 4.388, 4.531, 4.558, 4.465, 4.612, 4.243, 4.393, 4.378, 4.283, 4.628, 4.768, 4.727, 4.919, 4.794, 4.747], 'eps_duration_std': [4.522, 5.021, 4.709, 4.869, 4.781, 4.724, 5.556, 4.442, 4.284, 4.3, 4.257, 8.236, 5.789, 4.343, 5.941, 4.573, 4.272, 4.195, 5.266, 4.354, 4.099, 4.329, 5.613, 4.286, 4.365, 5.721, 4.089, 6.054, 4.384, 4.089, 4.212, 4.32, 4.274, 4.526, 6.398, 4.324, 4.168, 6.392, 4.312, 4.584, 4.284, 4.531, 5.631, 5.663, 4.357, 5.938, 4.301, 4.31, 4.23, 4.686, 4.396, 4.307, 4.396, 5.672, 4.36, 6.02, 4.309, 4.212, 4.251, 4.427, 5.721, 4.343, 4.171, 6.643, 4.191, 5.863, 4.335, 4.295, 4.242, 4.345, 6.667, 4.483, 4.281, 4.52, 4.461, 4.186, 4.524, 6.233, 4.569, 4.728, 4.169, 6.084, 4.02, 5.689, 4.499, 4.388, 4.531, 4.558, 4.465, 4.612, 4.243, 4.393, 4.378, 4.283, 4.628, 4.768, 4.727, 4.919, 4.794, 4.747], 'step_reward_mean': [16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296, 16.296], 'step_reward_std': [16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98, 16.98], 'sum_utility_mean': [13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093, 13.093], 'sum_utility_std': [15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178, 15.178]}
INFO:deepcomp.util.simulation:Mean results                   results={'episode': 49.5, 'eps_duration_mean': 4.769, 'eps_duration_std': 4.769, 'step_reward_mean': 16.296, 'step_reward_std': 16.98, 'sum_utility_mean': 13.093, 'sum_utility_std': 15.178}
INFO:deepcomp.util.simulation:Simulation complete            avg_eps_reward=1629.6 eps_length=100 num_episodes=100 step_reward_mean=16.296 step_reward_std=0.0
INFO:deepcomp.util.simulation:Writing scalar results         file=/home/abhishek/cmc/result/D3-CoMP/good/test/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-29_11-21-42.csv
INFO:deepcomp.util.simulation:Writing vector results         file=/home/abhishek/cmc/result/D3-CoMP/good/test/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-29_11-21-42_dr.pkl metric=dr
INFO:deepcomp.util.simulation:Writing vector results         file=/home/abhishek/cmc/result/D3-CoMP/good/test/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-29_11-21-42_utility.pkl metric=utility
INFO:deepcomp.main:Finished                       agent=/home/abhishek/cmc/result/D3-CoMP/good/train/PPO_2022-04-29_09-26-25/PPO_MultiAgentMobileEnv_572f4_00000_0_2022-04-29_09-26-26/checkpoint_000050/checkpoint-50
abhishek@abhishek-pc:~$ 
```








