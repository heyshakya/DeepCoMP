```
abhishek@abhishek-pc:~$ deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent multi --separate-agent-nns --workers 2 --dashboard --ue-details --eval 100 --train-steps 50000 --seed 42 --video both --result-dir /home/abhishek/cmc/result/D3-CoMP/decent
2022-04-27 12:29:54,092	WARNING deprecation.py:33 -- DeprecationWarning: `monitor` has been deprecated. Use `record_env` instead. This will raise an error in the future!
== Status ==
Memory usage on this node: 3.7/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 PENDING)
+-------------------------------------+----------+-------+
| Trial name                          | status   | loc   |
|-------------------------------------+----------+-------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | PENDING  |       |
+-------------------------------------+----------+-------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 32000
  custom_metrics:
    eps_sum_utility_max: -4728.048713676094
    eps_sum_utility_mean: -5960.483809230716
    eps_sum_utility_min: -7300.476000033085
    sum_utility_max: 4.292684515759022
    sum_utility_mean: -44.27935894290241
    sum_utility_min: -104.81805438075548
  date: 2022-04-27_12-32-23
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -2061.848333502096
  episode_reward_mean: -3309.894301308426
  episode_reward_min: -4843.356975335734
  episodes_this_iter: 40
  episodes_total: 40
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.0581295490264893
          entropy_coeff: 0.0
          kl: 0.02161639928817749
          model: {}
          policy_loss: -0.02680809423327446
          total_loss: 46474.83984375
          vf_explained_var: 8.285045623779297e-06
          vf_loss: 46474.8515625
      '2':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.0602619647979736
          entropy_coeff: 0.0
          kl: 0.019574319943785667
          model: {}
          policy_loss: -0.025153040885925293
          total_loss: 27755.75390625
          vf_explained_var: 0.003214811207726598
          vf_loss: 27755.7734375
      '3':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.050853967666626
          entropy_coeff: 0.0
          kl: 0.027725953608751297
          model: {}
          policy_loss: -0.03501517325639725
          total_loss: 19525.025390625
          vf_explained_var: -0.0007208854658529162
          vf_loss: 19525.0546875
      '4':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.0495524406433105
          entropy_coeff: 0.0
          kl: 0.029576286673545837
          model: {}
          policy_loss: -0.036528196185827255
          total_loss: 28415.359375
          vf_explained_var: 0.00046262433170340955
          vf_loss: 28415.38671875
      '5':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.0595850944519043
          entropy_coeff: 0.0
          kl: 0.02045758068561554
          model: {}
          policy_loss: -0.027931896969676018
          total_loss: 18996.359375
          vf_explained_var: -0.00034679906093515456
          vf_loss: 18996.3828125
      '6':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.0587453842163086
          entropy_coeff: 0.0
          kl: 0.02139902487397194
          model: {}
          policy_loss: -0.02323339134454727
          total_loss: 33012.39453125
          vf_explained_var: 0.004451478831470013
          vf_loss: 33012.41015625
      '7':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.059544801712036
          entropy_coeff: 0.0
          kl: 0.019870612770318985
          model: {}
          policy_loss: -0.032123956829309464
          total_loss: 42206.8828125
          vf_explained_var: 7.62420313549228e-05
          vf_loss: 42206.91796875
      '8':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.060767650604248
          entropy_coeff: 0.0
          kl: 0.018873130902647972
          model: {}
          policy_loss: -0.03241837024688721
          total_loss: 37441.90234375
          vf_explained_var: 0.0006986683583818376
          vf_loss: 37441.9296875
    num_agent_steps_sampled: 32000
    num_agent_steps_trained: 32000
    num_steps_sampled: 4000
    num_steps_trained: 4000
  iterations_since_restore: 1
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.08527131782946
    ram_util_percent: 77.05348837209301
  pid: 141171
  policy_reward_max:
    '1': 54.41724421391364
    '2': 30.83732371801896
    '3': -141.72642827257113
    '4': 135.28743807419562
    '5': -19.123764004590143
    '6': 110.56678705314292
    '7': -103.86999825312346
    '8': -185.11881774579257
  policy_reward_mean:
    '1': -495.404950479131
    '2': -404.05646580913765
    '3': -384.39590732990905
    '4': -384.76397027278273
    '5': -354.63883521692816
    '6': -328.812274510987
    '7': -470.4091645392781
    '8': -487.4127331502738
  policy_reward_min:
    '1': -951.8518760733281
    '2': -784.0486468438614
    '3': -840.3004589524152
    '4': -849.4278089715713
    '5': -733.6744652112988
    '6': -717.9780569484927
    '7': -773.486812462285
    '8': -803.2529253743414
  sampler_perf:
    mean_action_processing_ms: 0.16735876160583038
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 25.999022507179028
    mean_inference_ms: 5.45256385679307
    mean_raw_obs_processing_ms: 0.583625983619976
  time_since_restore: 94.95307183265686
  time_this_iter_s: 94.95307183265686
  time_total_s: 94.95307183265686
  timers:
    learn_throughput: 146.897
    learn_time_ms: 27229.984
    load_throughput: 2339.311
    load_time_ms: 1709.905
    sample_throughput: 61.454
    sample_time_ms: 65089.227
    update_time_ms: 13.347
  timestamp: 1651042943
  timesteps_since_restore: 0
  timesteps_total: 4000
  training_iteration: 1
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |   ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |      1 |          94.9531 | 4000 | -3309.89 |             -2061.85 |             -4843.36 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 64000
  custom_metrics:
    eps_sum_utility_max: -3161.6103339760634
    eps_sum_utility_mean: -5018.140145558287
    eps_sum_utility_min: -7300.476000033085
    sum_utility_max: 21.814371110063238
    sum_utility_mean: -36.01712767490809
    sum_utility_min: -104.81805438075548
  date: 2022-04-27_12-34-06
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: -665.3816078826866
  episode_reward_mean: -2518.01699736293
  episode_reward_min: -4843.356975335734
  episodes_this_iter: 40
  episodes_total: 80
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 2.0257277488708496
          entropy_coeff: 0.0
          kl: 0.012238791212439537
          model: {}
          policy_loss: -0.016947221010923386
          total_loss: 10794.380859375
          vf_explained_var: 8.977420657174662e-05
          vf_loss: 10794.3935546875
      '2':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.0186686515808105
          entropy_coeff: 0.0
          kl: 0.018244367092847824
          model: {}
          policy_loss: -0.02885567583143711
          total_loss: 11485.7236328125
          vf_explained_var: 0.022343717515468597
          vf_loss: 11485.748046875
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 2.0164408683776855
          entropy_coeff: 0.0
          kl: 0.019793478772044182
          model: {}
          policy_loss: -0.03091934137046337
          total_loss: 4849.30908203125
          vf_explained_var: -0.00034861412132158875
          vf_loss: 4849.333984375
      '4':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9933112859725952
          entropy_coeff: 0.0
          kl: 0.023894699290394783
          model: {}
          policy_loss: -0.03645899146795273
          total_loss: 10834.767578125
          vf_explained_var: 0.00012732898176182061
          vf_loss: 10834.7978515625
      '5':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 2.0292253494262695
          entropy_coeff: 0.0
          kl: 0.02055792696774006
          model: {}
          policy_loss: -0.03285319358110428
          total_loss: 6083.423828125
          vf_explained_var: -3.533978451741859e-05
          vf_loss: 6083.451171875
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 2.0221316814422607
          entropy_coeff: 0.0
          kl: 0.01679779216647148
          model: {}
          policy_loss: -0.02504478022456169
          total_loss: 17440.154296875
          vf_explained_var: 0.020437054336071014
          vf_loss: 17440.17578125
      '7':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.0210516452789307
          entropy_coeff: 0.0
          kl: 0.023863917216658592
          model: {}
          policy_loss: -0.03406701236963272
          total_loss: 24692.88671875
          vf_explained_var: 3.9196784200612456e-05
          vf_loss: 24692.91796875
      '8':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 2.029365301132202
          entropy_coeff: 0.0
          kl: 0.020100824534893036
          model: {}
          policy_loss: -0.029430238530039787
          total_loss: 20175.724609375
          vf_explained_var: 0.001967464806511998
          vf_loss: 20175.748046875
    num_agent_steps_sampled: 64000
    num_agent_steps_trained: 64000
    num_steps_sampled: 8000
    num_steps_trained: 8000
  iterations_since_restore: 2
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.32374100719424
    ram_util_percent: 77.54172661870503
  pid: 141171
  policy_reward_max:
    '1': 134.0203829486046
    '2': 30.83732371801896
    '3': 5.129657275256092
    '4': 135.28743807419562
    '5': 1.968337334933711
    '6': 470.33226401444904
    '7': -103.86999825312346
    '8': -9.828290708400614
  policy_reward_mean:
    '1': -312.6333910596957
    '2': -337.61647633996193
    '3': -292.8840659944585
    '4': -277.70890785802465
    '5': -286.4840423370897
    '6': -172.69329734348895
    '7': -413.8669723956018
    '8': -424.1298440346103
  policy_reward_min:
    '1': -951.8518760733281
    '2': -784.0486468438614
    '3': -840.3004589524152
    '4': -849.4278089715713
    '5': -733.6744652112988
    '6': -717.9780569484927
    '7': -781.0854207751293
    '8': -803.2529253743414
  sampler_perf:
    mean_action_processing_ms: 0.17128508398088807
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 27.269679383792447
    mean_inference_ms: 5.496898724466263
    mean_raw_obs_processing_ms: 0.598127324567512
  time_since_restore: 197.96946382522583
  time_this_iter_s: 103.01639199256897
  time_total_s: 197.96946382522583
  timers:
    learn_throughput: 148.538
    learn_time_ms: 26929.093
    load_throughput: 4650.621
    load_time_ms: 860.1
    sample_throughput: 56.714
    sample_time_ms: 70529.914
    update_time_ms: 13.387
  timestamp: 1651043046
  timesteps_since_restore: 0
  timesteps_total: 8000
  training_iteration: 2
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |   ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |      2 |          197.969 | 8000 | -2518.02 |             -665.382 |             -4843.36 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 96000
  custom_metrics:
    eps_sum_utility_max: -1570.192610335606
    eps_sum_utility_mean: -3816.7209487914656
    eps_sum_utility_min: -7300.476000033085
    sum_utility_max: 27.91629245193677
    sum_utility_mean: -24.37681678391778
    sum_utility_min: -104.81805438075548
  date: 2022-04-27_12-36-04
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 179.15454165326383
  episode_reward_mean: -1641.1573811116034
  episode_reward_min: -4843.356975335734
  episodes_this_iter: 40
  episodes_total: 120
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9860200881958008
          entropy_coeff: 0.0
          kl: 0.014206714928150177
          model: {}
          policy_loss: -0.020461922511458397
          total_loss: 8303.490234375
          vf_explained_var: 0.003376603126525879
          vf_loss: 8303.5068359375
      '2':
        learner_stats:
          cur_kl_coeff: 0.20000000298023224
          cur_lr: 4.999999873689376e-05
          entropy: 1.970454454421997
          entropy_coeff: 0.0
          kl: 0.02241966314613819
          model: {}
          policy_loss: -0.029946396127343178
          total_loss: 4528.22509765625
          vf_explained_var: 0.05957700312137604
          vf_loss: 4528.25048828125
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9760196208953857
          entropy_coeff: 0.0
          kl: 0.016280522570014
          model: {}
          policy_loss: -0.027688469737768173
          total_loss: 2124.9541015625
          vf_explained_var: -0.0001865048543550074
          vf_loss: 2124.976806640625
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.9581373929977417
          entropy_coeff: 0.0
          kl: 0.013708357699215412
          model: {}
          policy_loss: -0.02783099003136158
          total_loss: 3845.7470703125
          vf_explained_var: 0.015724431723356247
          vf_loss: 3845.76904296875
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 2.0009217262268066
          entropy_coeff: 0.0
          kl: 0.011726932600140572
          model: {}
          policy_loss: -0.021572690457105637
          total_loss: 2793.15283203125
          vf_explained_var: 0.00045932683860883117
          vf_loss: 2793.16943359375
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9752033948898315
          entropy_coeff: 0.0
          kl: 0.013950358144938946
          model: {}
          policy_loss: -0.02486654557287693
          total_loss: 18421.8515625
          vf_explained_var: 0.023348549380898476
          vf_loss: 18421.869140625
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9924240112304688
          entropy_coeff: 0.0
          kl: 0.017385423183441162
          model: {}
          policy_loss: -0.03205208480358124
          total_loss: 9143.083984375
          vf_explained_var: 2.8940939955646172e-05
          vf_loss: 9143.1103515625
      '8':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9867416620254517
          entropy_coeff: 0.0
          kl: 0.018350884318351746
          model: {}
          policy_loss: -0.02794918604195118
          total_loss: 7665.1943359375
          vf_explained_var: 0.02810330130159855
          vf_loss: 7665.21728515625
    num_agent_steps_sampled: 96000
    num_agent_steps_trained: 96000
    num_steps_sampled: 12000
    num_steps_trained: 12000
  iterations_since_restore: 3
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.517721518987344
    ram_util_percent: 77.7107594936709
  pid: 141171
  policy_reward_max:
    '1': 254.24517794555214
    '2': 40.89386398590812
    '3': 36.620528875591425
    '4': 223.6466976917678
    '5': 44.74085273463768
    '6': 470.33226401444904
    '7': 27.606814589478066
    '8': 92.5541549017881
  policy_reward_mean:
    '1': -135.9892257401094
    '2': -267.4451579330279
    '3': -202.72425211289826
    '4': -148.62270559757297
    '5': -210.55026030106765
    '6': -31.216855248033138
    '7': -313.49097698301273
    '8': -331.1179471958821
  policy_reward_min:
    '1': -951.8518760733281
    '2': -780.6515469606612
    '3': -840.3004589524152
    '4': -849.4278089715713
    '5': -604.2334691006942
    '6': -717.9780569484927
    '7': -781.0854207751293
    '8': -803.2529253743414
  sampler_perf:
    mean_action_processing_ms: 0.17755291906398443
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 29.157568486742875
    mean_inference_ms: 5.612955713130043
    mean_raw_obs_processing_ms: 0.6171922797098244
  time_since_restore: 315.5116038322449
  time_this_iter_s: 117.54214000701904
  time_total_s: 315.5116038322449
  timers:
    learn_throughput: 147.655
    learn_time_ms: 27090.24
    load_throughput: 6923.359
    load_time_ms: 577.754
    sample_throughput: 51.997
    sample_time_ms: 76928.133
    update_time_ms: 13.544
  timestamp: 1651043164
  timesteps_since_restore: 0
  timesteps_total: 12000
  training_iteration: 3
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |      3 |          315.512 | 12000 | -1641.16 |              179.155 |             -4843.36 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 128000
  custom_metrics:
    eps_sum_utility_max: -893.7435334404817
    eps_sum_utility_mean: -2450.980923310379
    eps_sum_utility_min: -4839.297541918147
    sum_utility_max: 27.91629245193677
    sum_utility_mean: -9.050297247652733
    sum_utility_min: -104.31901659276241
  date: 2022-04-27_12-38-05
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 287.65164250250837
  episode_reward_mean: -690.4317245286345
  episode_reward_min: -2523.2694611335055
  episodes_this_iter: 40
  episodes_total: 160
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9427878856658936
          entropy_coeff: 0.0
          kl: 0.01703340746462345
          model: {}
          policy_loss: -0.02313346229493618
          total_loss: 14018.064453125
          vf_explained_var: 0.0014378986088559031
          vf_loss: 14018.08203125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9391610622406006
          entropy_coeff: 0.0
          kl: 0.016834069043397903
          model: {}
          policy_loss: -0.02960137277841568
          total_loss: 3059.9033203125
          vf_explained_var: 0.07410769909620285
          vf_loss: 3059.927734375
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9309173822402954
          entropy_coeff: 0.0
          kl: 0.01792670600116253
          model: {}
          policy_loss: -0.032830823212862015
          total_loss: 925.5999145507812
          vf_explained_var: -0.00018262671073898673
          vf_loss: 925.6272583007812
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.9251952171325684
          entropy_coeff: 0.0
          kl: 0.014648151583969593
          model: {}
          policy_loss: -0.02699037827551365
          total_loss: 2761.5615234375
          vf_explained_var: 0.00957725290209055
          vf_loss: 2761.582275390625
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.9774693250656128
          entropy_coeff: 0.0
          kl: 0.00875950139015913
          model: {}
          policy_loss: -0.014751018956303596
          total_loss: 1391.61669921875
          vf_explained_var: 0.09813322126865387
          vf_loss: 1391.6273193359375
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9332903623580933
          entropy_coeff: 0.0
          kl: 0.014011712744832039
          model: {}
          policy_loss: -0.02042391523718834
          total_loss: 16679.763671875
          vf_explained_var: 0.030671294778585434
          vf_loss: 16679.779296875
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9427218437194824
          entropy_coeff: 0.0
          kl: 0.015980668365955353
          model: {}
          policy_loss: -0.0274689681828022
          total_loss: 3063.457763671875
          vf_explained_var: 9.157388558378443e-05
          vf_loss: 3063.480224609375
      '8':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.9351071119308472
          entropy_coeff: 0.0
          kl: 0.020604828372597694
          model: {}
          policy_loss: -0.03516257926821709
          total_loss: 5246.427734375
          vf_explained_var: 0.06337258964776993
          vf_loss: 5246.45654296875
    num_agent_steps_sampled: 128000
    num_agent_steps_trained: 128000
    num_steps_sampled: 16000
    num_steps_trained: 16000
  iterations_since_restore: 4
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.42085889570552
    ram_util_percent: 77.72147239263805
  pid: 141171
  policy_reward_max:
    '1': 341.07368727494935
    '2': 40.89386398590812
    '3': 73.726570864846
    '4': 241.08381428877018
    '5': 80.55843434234707
    '6': 470.33226401444904
    '7': 155.18667016403782
    '8': 95.53042429066093
  policy_reward_mean:
    '1': 57.59162621376997
    '2': -184.30248572284967
    '3': -98.0341495190005
    '4': -2.288306318820386
    '5': -129.91568410933144
    '6': 101.23959726075267
    '7': -184.85923751536774
    '8': -249.86308481778764
  policy_reward_min:
    '1': -564.0239202847283
    '2': -475.80223105964114
    '3': -418.56376310553395
    '4': -613.2279297646822
    '5': -411.58230212368125
    '6': -482.53216782531143
    '7': -779.9114991184636
    '8': -564.6755272327684
  sampler_perf:
    mean_action_processing_ms: 0.1849156817721159
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 31.482320098637175
    mean_inference_ms: 5.762629965051908
    mean_raw_obs_processing_ms: 0.6421519086061446
  time_since_restore: 437.0078647136688
  time_this_iter_s: 121.49626088142395
  time_total_s: 437.0078647136688
  timers:
    learn_throughput: 144.115
    learn_time_ms: 27755.519
    load_throughput: 9152.668
    load_time_ms: 437.031
    sample_throughput: 49.616
    sample_time_ms: 80618.745
    update_time_ms: 13.636
  timestamp: 1651043285
  timesteps_since_restore: 0
  timesteps_total: 16000
  training_iteration: 4
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |      4 |          437.008 | 16000 | -690.432 |              287.652 |             -2523.27 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 160000
  custom_metrics:
    eps_sum_utility_max: -157.71414122524467
    eps_sum_utility_mean: -1467.3618136951343
    eps_sum_utility_min: -3492.536165093244
    sum_utility_max: 28.465511591227607
    sum_utility_mean: 0.7091999601241546
    sum_utility_min: -70.40699602956651
  date: 2022-04-27_12-40-17
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 802.6293762099159
  episode_reward_mean: -124.89528020267248
  episode_reward_min: -1786.665734166545
  episodes_this_iter: 40
  episodes_total: 200
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.88063383102417
          entropy_coeff: 0.0
          kl: 0.013274407014250755
          model: {}
          policy_loss: -0.021558620035648346
          total_loss: 14463.0673828125
          vf_explained_var: 0.00018921206356026232
          vf_loss: 14463.083984375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8790639638900757
          entropy_coeff: 0.0
          kl: 0.016604969277977943
          model: {}
          policy_loss: -0.029611650854349136
          total_loss: 1553.876708984375
          vf_explained_var: 0.1601027399301529
          vf_loss: 1553.9013671875
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8829843997955322
          entropy_coeff: 0.0
          kl: 0.017943566665053368
          model: {}
          policy_loss: -0.02630678191781044
          total_loss: 645.9484252929688
          vf_explained_var: -3.314210698590614e-05
          vf_loss: 645.96923828125
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.9006413221359253
          entropy_coeff: 0.0
          kl: 0.01260994840413332
          model: {}
          policy_loss: -0.023807762190699577
          total_loss: 2195.65771484375
          vf_explained_var: -0.005823985207825899
          vf_loss: 2195.67626953125
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.9353078603744507
          entropy_coeff: 0.0
          kl: 0.011432744562625885
          model: {}
          policy_loss: -0.029945479705929756
          total_loss: 867.4286499023438
          vf_explained_var: 0.2645437717437744
          vf_loss: 867.4534301757812
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.89864182472229
          entropy_coeff: 0.0
          kl: 0.015010345727205276
          model: {}
          policy_loss: -0.02076386846601963
          total_loss: 17360.431640625
          vf_explained_var: 0.011126740835607052
          vf_loss: 17360.447265625
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.895659327507019
          entropy_coeff: 0.0
          kl: 0.01641070283949375
          model: {}
          policy_loss: -0.02988211251795292
          total_loss: 1906.7926025390625
          vf_explained_var: 0.0007213777280412614
          vf_loss: 1906.8175048828125
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.9024453163146973
          entropy_coeff: 0.0
          kl: 0.013619699515402317
          model: {}
          policy_loss: -0.026961030438542366
          total_loss: 3088.318603515625
          vf_explained_var: 0.12691885232925415
          vf_loss: 3088.33935546875
    num_agent_steps_sampled: 160000
    num_agent_steps_trained: 160000
    num_steps_sampled: 20000
    num_steps_trained: 20000
  iterations_since_restore: 5
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.45738636363637
    ram_util_percent: 77.71988636363636
  pid: 141171
  policy_reward_max:
    '1': 350.4135902583095
    '2': 37.464134491619234
    '3': 95.61698261528686
    '4': 318.24784596303977
    '5': 82.59569475943923
    '6': 479.6544181080055
    '7': 155.18667016403782
    '8': 95.53042429066093
  policy_reward_mean:
    '1': 174.87513087381973
    '2': -141.46563365095298
    '3': -40.594605536548755
    '4': 75.22080411177583
    '5': -99.4285783889152
    '6': 168.19342512225546
    '7': -72.44829352973356
    '8': -189.247529204373
  policy_reward_min:
    '1': -209.04038462960494
    '2': -466.5567230459069
    '3': -418.56376310553395
    '4': -292.14536541639393
    '5': -344.36903150310036
    '6': -170.96500177760277
    '7': -499.77590934230665
    '8': -484.50102593379796
  sampler_perf:
    mean_action_processing_ms: 0.1909534030551846
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 33.48566511847503
    mean_inference_ms: 5.907101349270813
    mean_raw_obs_processing_ms: 0.6626720598750592
  time_since_restore: 568.5297989845276
  time_this_iter_s: 131.52193427085876
  time_total_s: 568.5297989845276
  timers:
    learn_throughput: 141.442
    learn_time_ms: 28280.218
    load_throughput: 11346.882
    load_time_ms: 352.52
    sample_throughput: 47.218
    sample_time_ms: 84713.444
    update_time_ms: 13.385
  timestamp: 1651043417
  timesteps_since_restore: 0
  timesteps_total: 20000
  training_iteration: 5
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |      5 |           568.53 | 20000 | -124.895 |              802.629 |             -1786.67 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 192000
  custom_metrics:
    eps_sum_utility_max: 430.8132068704351
    eps_sum_utility_mean: -734.1208479984889
    eps_sum_utility_min: -2514.4778030385023
    sum_utility_max: 28.465511591227607
    sum_utility_mean: 7.958647472919248
    sum_utility_min: -70.40699602956651
  date: 2022-04-27_12-42-30
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 818.3218221602087
  episode_reward_mean: 265.02936603405846
  episode_reward_min: -749.7177398319031
  episodes_this_iter: 40
  episodes_total: 240
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8923701047897339
          entropy_coeff: 0.0
          kl: 0.009005029685795307
          model: {}
          policy_loss: -0.01042764913290739
          total_loss: 17537.87890625
          vf_explained_var: -8.277739107143134e-05
          vf_loss: 17537.88671875
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8338109254837036
          entropy_coeff: 0.0
          kl: 0.014589912258088589
          model: {}
          policy_loss: -0.025367505848407745
          total_loss: 512.2122802734375
          vf_explained_var: 0.3420812785625458
          vf_loss: 512.2332763671875
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8716175556182861
          entropy_coeff: 0.0
          kl: 0.014386432245373726
          model: {}
          policy_loss: -0.019801197573542595
          total_loss: 492.6906433105469
          vf_explained_var: 5.699550092685968e-05
          vf_loss: 492.7060852050781
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8615117073059082
          entropy_coeff: 0.0
          kl: 0.012983462773263454
          model: {}
          policy_loss: -0.022766368463635445
          total_loss: 1638.921630859375
          vf_explained_var: -0.006352424621582031
          vf_loss: 1638.9385986328125
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.9217458963394165
          entropy_coeff: 0.0
          kl: 0.008350346237421036
          model: {}
          policy_loss: -0.016624165698885918
          total_loss: 398.78607177734375
          vf_explained_var: 0.4577760100364685
          vf_loss: 398.79888916015625
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.874335527420044
          entropy_coeff: 0.0
          kl: 0.012560115195810795
          model: {}
          policy_loss: -0.0163588710129261
          total_loss: 16870.087890625
          vf_explained_var: 0.0010148921282961965
          vf_loss: 16870.099609375
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.836795687675476
          entropy_coeff: 0.0
          kl: 0.018883654847741127
          model: {}
          policy_loss: -0.03348328918218613
          total_loss: 1713.7318115234375
          vf_explained_var: 0.013683151453733444
          vf_loss: 1713.759521484375
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8853302001953125
          entropy_coeff: 0.0
          kl: 0.01117972657084465
          model: {}
          policy_loss: -0.022529931738972664
          total_loss: 1978.6995849609375
          vf_explained_var: 0.23465962707996368
          vf_loss: 1978.7169189453125
    num_agent_steps_sampled: 192000
    num_agent_steps_trained: 192000
    num_steps_sampled: 24000
    num_steps_trained: 24000
  iterations_since_restore: 6
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.50508474576271
    ram_util_percent: 77.73898305084745
  pid: 141171
  policy_reward_max:
    '1': 371.5703040874523
    '2': 37.464134491619234
    '3': 95.61698261528686
    '4': 318.24784596303977
    '5': 82.59569475943923
    '6': 479.6544181080055
    '7': 155.18667016403782
    '8': 95.90254552790569
  policy_reward_mean:
    '1': 253.47873526325785
    '2': -103.73179636856347
    '3': -1.7762982036291393
    '4': 121.19190385679825
    '5': -71.1834287214634
    '6': 222.80969550916183
    '7': -20.116632548220196
    '8': -135.64281275328324
  policy_reward_min:
    '1': -36.11440343255175
    '2': -371.50048602847295
    '3': -191.91899491763698
    '4': -121.50760027583758
    '5': -245.17923951823298
    '6': -155.78313143142202
    '7': -185.23846139114752
    '8': -395.4820465615862
  sampler_perf:
    mean_action_processing_ms: 0.19564610890495793
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 35.1283397350425
    mean_inference_ms: 6.020918405287359
    mean_raw_obs_processing_ms: 0.6792706172370326
  time_since_restore: 701.149641752243
  time_this_iter_s: 132.61984276771545
  time_total_s: 701.149641752243
  timers:
    learn_throughput: 139.923
    learn_time_ms: 28587.138
    load_throughput: 13534.306
    load_time_ms: 295.545
    sample_throughput: 45.626
    sample_time_ms: 87669.588
    update_time_ms: 13.444
  timestamp: 1651043550
  timesteps_since_restore: 0
  timesteps_total: 24000
  training_iteration: 6
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |      6 |           701.15 | 24000 |  265.029 |              818.322 |             -749.718 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 224000
  custom_metrics:
    eps_sum_utility_max: 498.0624512471209
    eps_sum_utility_mean: -213.90182086079608
    eps_sum_utility_min: -1612.3077390856815
    sum_utility_max: 28.802678897228816
    sum_utility_mean: 11.669691694232563
    sum_utility_min: -70.40699602956651
  date: 2022-04-27_12-44-44
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 933.2316950156489
  episode_reward_mean: 518.4630040100833
  episode_reward_min: -121.06062685456506
  episodes_this_iter: 40
  episodes_total: 280
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8872349262237549
          entropy_coeff: 0.0
          kl: 0.007668931037187576
          model: {}
          policy_loss: -0.009288569912314415
          total_loss: 16246.1982421875
          vf_explained_var: -5.7197386922780424e-05
          vf_loss: 16246.2080078125
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8153542280197144
          entropy_coeff: 0.0
          kl: 0.010725162923336029
          model: {}
          policy_loss: -0.015326293185353279
          total_loss: 448.15325927734375
          vf_explained_var: 0.4299944341182709
          vf_loss: 448.1653137207031
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8423762321472168
          entropy_coeff: 0.0
          kl: 0.012590287253260612
          model: {}
          policy_loss: -0.02024652063846588
          total_loss: 413.33050537109375
          vf_explained_var: 9.93378707789816e-05
          vf_loss: 413.34698486328125
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.829530119895935
          entropy_coeff: 0.0
          kl: 0.013282199390232563
          model: {}
          policy_loss: -0.02055956795811653
          total_loss: 1097.8956298828125
          vf_explained_var: -0.00654781237244606
          vf_loss: 1097.91015625
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.9086579084396362
          entropy_coeff: 0.0
          kl: 0.00886633712798357
          model: {}
          policy_loss: -0.01786518655717373
          total_loss: 362.9049987792969
          vf_explained_var: 0.43125754594802856
          vf_loss: 362.9188537597656
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.838081955909729
          entropy_coeff: 0.0
          kl: 0.012081657536327839
          model: {}
          policy_loss: -0.01636209525167942
          total_loss: 13434.7431640625
          vf_explained_var: 0.0002263630594825372
          vf_loss: 13434.7548828125
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7610507011413574
          entropy_coeff: 0.0
          kl: 0.019968444481492043
          model: {}
          policy_loss: -0.028249453753232956
          total_loss: 1350.458251953125
          vf_explained_var: 0.03909412398934364
          vf_loss: 1350.48046875
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8504791259765625
          entropy_coeff: 0.0
          kl: 0.011524730361998081
          model: {}
          policy_loss: -0.024961255490779877
          total_loss: 1265.28564453125
          vf_explained_var: 0.3254148066043854
          vf_loss: 1265.3052978515625
    num_agent_steps_sampled: 224000
    num_agent_steps_trained: 224000
    num_steps_sampled: 28000
    num_steps_trained: 28000
  iterations_since_restore: 7
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.216201117318434
    ram_util_percent: 77.73407821229051
  pid: 141171
  policy_reward_max:
    '1': 374.09742876839107
    '2': 61.36659150810931
    '3': 90.58064720194473
    '4': 249.5304099098848
    '5': 69.86949074258042
    '6': 365.0914231326921
    '7': 139.44717728547033
    '8': 95.90254552790569
  policy_reward_mean:
    '1': 304.2286342427826
    '2': -73.05446711338513
    '3': 20.95410369786808
    '4': 137.351061690461
    '5': -44.92272612155596
    '6': 256.05088207057486
    '7': 14.134307970182824
    '8': -96.2787924268449
  policy_reward_min:
    '1': 129.87444350917485
    '2': -267.57930519687847
    '3': -103.36697668815081
    '4': 0.6376659288000894
    '5': -230.1471805652655
    '6': 107.5944647397047
    '7': -145.00367281707605
    '8': -331.774390218823
  sampler_perf:
    mean_action_processing_ms: 0.19927250385992132
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 36.45052123604288
    mean_inference_ms: 6.107711714542833
    mean_raw_obs_processing_ms: 0.6923116946250494
  time_since_restore: 834.9966902732849
  time_this_iter_s: 133.84704852104187
  time_total_s: 834.9966902732849
  timers:
    learn_throughput: 138.313
    learn_time_ms: 28919.893
    load_throughput: 15663.937
    load_time_ms: 255.364
    sample_throughput: 44.522
    sample_time_ms: 89842.237
    update_time_ms: 13.604
  timestamp: 1651043684
  timesteps_since_restore: 0
  timesteps_total: 28000
  training_iteration: 7
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |      7 |          834.997 | 28000 |  518.463 |              933.232 |             -121.061 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 256000
  custom_metrics:
    eps_sum_utility_max: 718.7989595077081
    eps_sum_utility_mean: 134.37006309077685
    eps_sum_utility_min: -678.9200240625447
    sum_utility_max: 28.802678897228816
    sum_utility_mean: 16.390731314621018
    sum_utility_min: -16.656875308857373
  date: 2022-04-27_12-47-07
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1039.7426207736314
  episode_reward_mean: 669.2286689111785
  episode_reward_min: 160.247722537384
  episodes_this_iter: 40
  episodes_total: 320
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.886319875717163
          entropy_coeff: 0.0
          kl: 0.010894476436078548
          model: {}
          policy_loss: -0.011916096322238445
          total_loss: 15467.6435546875
          vf_explained_var: -3.2251882657874376e-05
          vf_loss: 15467.6513671875
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7912293672561646
          entropy_coeff: 0.0
          kl: 0.011725646443665028
          model: {}
          policy_loss: -0.01613820157945156
          total_loss: 414.6202087402344
          vf_explained_var: 0.4473528265953064
          vf_loss: 414.63287353515625
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8367787599563599
          entropy_coeff: 0.0
          kl: 0.005231770686805248
          model: {}
          policy_loss: -0.012757489457726479
          total_loss: 389.9934387207031
          vf_explained_var: 0.0007098682690411806
          vf_loss: 390.0046691894531
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.810907244682312
          entropy_coeff: 0.0
          kl: 0.006884895730763674
          model: {}
          policy_loss: -0.013800603337585926
          total_loss: 678.1732177734375
          vf_explained_var: -0.002294138539582491
          vf_loss: 678.183837890625
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8988749980926514
          entropy_coeff: 0.0
          kl: 0.006607985123991966
          model: {}
          policy_loss: -0.012546737678349018
          total_loss: 325.54864501953125
          vf_explained_var: 0.45549601316452026
          vf_loss: 325.5582275390625
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8267349004745483
          entropy_coeff: 0.0
          kl: 0.010923800989985466
          model: {}
          policy_loss: -0.011436451226472855
          total_loss: 12016.2373046875
          vf_explained_var: 7.2479248046875e-05
          vf_loss: 12016.24609375
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7353641986846924
          entropy_coeff: 0.0
          kl: 0.018350008875131607
          model: {}
          policy_loss: -0.027090342715382576
          total_loss: 1004.4932861328125
          vf_explained_var: 0.13167399168014526
          vf_loss: 1004.514892578125
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.818512201309204
          entropy_coeff: 0.0
          kl: 0.01329068187624216
          model: {}
          policy_loss: -0.028058569878339767
          total_loss: 654.6061401367188
          vf_explained_var: 0.44244980812072754
          vf_loss: 654.6283569335938
    num_agent_steps_sampled: 256000
    num_agent_steps_trained: 256000
    num_steps_sampled: 32000
    num_steps_trained: 32000
  iterations_since_restore: 8
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.24427083333333
    ram_util_percent: 77.74791666666668
  pid: 141171
  policy_reward_max:
    '1': 378.8400379125356
    '2': 61.36659150810931
    '3': 98.72220950527452
    '4': 204.24531523911097
    '5': 69.86949074258042
    '6': 365.0914231326921
    '7': 196.6411116527317
    '8': 50.00502575909488
  policy_reward_mean:
    '1': 330.08180966776376
    '2': -59.071746979906685
    '3': 30.046749374064657
    '4': 148.18541173736713
    '5': -33.702091354140855
    '6': 276.41795270398205
    '7': 46.66854415831344
    '8': -69.39796039626509
  policy_reward_min:
    '1': 247.326476759017
    '2': -155.58173146463074
    '3': -47.9050635943319
    '4': 0.6376659288000894
    '5': -110.20602946828767
    '6': 136.80962548901064
    '7': -137.8573390261238
    '8': -226.1086357542355
  sampler_perf:
    mean_action_processing_ms: 0.20240007547256117
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 37.613348793657025
    mean_inference_ms: 6.183067555189586
    mean_raw_obs_processing_ms: 0.7032364573757485
  time_since_restore: 978.2979986667633
  time_this_iter_s: 143.3013083934784
  time_total_s: 978.2979986667633
  timers:
    learn_throughput: 136.894
    learn_time_ms: 29219.592
    load_throughput: 17758.377
    load_time_ms: 225.246
    sample_throughput: 43.198
    sample_time_ms: 92596.824
    update_time_ms: 16.684
  timestamp: 1651043827
  timesteps_since_restore: 0
  timesteps_total: 32000
  training_iteration: 8
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 6.0/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |      8 |          978.298 | 32000 |  669.229 |              1039.74 |              160.248 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 288000
  custom_metrics:
    eps_sum_utility_max: 753.5114074742423
    eps_sum_utility_mean: 345.3369773434451
    eps_sum_utility_min: -405.61995856828656
    sum_utility_max: 28.802678897228816
    sum_utility_mean: 18.137622669043726
    sum_utility_min: -18.373396185126754
  date: 2022-04-27_12-49-31
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1039.7426207736314
  episode_reward_mean: 768.408920088351
  episode_reward_min: 508.3000600613391
  episodes_this_iter: 40
  episodes_total: 360
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.882983684539795
          entropy_coeff: 0.0
          kl: 0.008939833380281925
          model: {}
          policy_loss: -0.008429690264165401
          total_loss: 13723.84375
          vf_explained_var: -1.864279511210043e-05
          vf_loss: 13723.8505859375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7383166551589966
          entropy_coeff: 0.0
          kl: 0.01358728762716055
          model: {}
          policy_loss: -0.02161181904375553
          total_loss: 299.30023193359375
          vf_explained_var: 0.5664007067680359
          vf_loss: 299.3177795410156
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.797481894493103
          entropy_coeff: 0.0
          kl: 0.011462509632110596
          model: {}
          policy_loss: -0.016995128244161606
          total_loss: 407.0870666503906
          vf_explained_var: 0.0065290313214063644
          vf_loss: 407.1007080078125
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7877554893493652
          entropy_coeff: 0.0
          kl: 0.009746024385094643
          model: {}
          policy_loss: -0.02018926292657852
          total_loss: 465.7054443359375
          vf_explained_var: -0.0007764447364024818
          vf_loss: 465.7212829589844
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8773446083068848
          entropy_coeff: 0.0
          kl: 0.008327750489115715
          model: {}
          policy_loss: -0.012103897519409657
          total_loss: 181.5154571533203
          vf_explained_var: 0.6290990114212036
          vf_loss: 181.52378845214844
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8266221284866333
          entropy_coeff: 0.0
          kl: 0.007412961684167385
          model: {}
          policy_loss: -0.008114499039947987
          total_loss: 10934.63671875
          vf_explained_var: 2.5530014681862667e-05
          vf_loss: 10934.642578125
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7127487659454346
          entropy_coeff: 0.0
          kl: 0.01807350479066372
          model: {}
          policy_loss: -0.024869972839951515
          total_loss: 603.408203125
          vf_explained_var: 0.29861071705818176
          vf_loss: 603.4276123046875
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.784986972808838
          entropy_coeff: 0.0
          kl: 0.01134801097214222
          model: {}
          policy_loss: -0.023258544504642487
          total_loss: 618.993896484375
          vf_explained_var: 0.3998342454433441
          vf_loss: 619.0120849609375
    num_agent_steps_sampled: 288000
    num_agent_steps_trained: 288000
    num_steps_sampled: 36000
    num_steps_trained: 36000
  iterations_since_restore: 9
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.4565445026178
    ram_util_percent: 77.74921465968588
  pid: 141171
  policy_reward_max:
    '1': 386.8264626727526
    '2': 61.01941317502633
    '3': 98.72220950527452
    '4': 210.58759132067902
    '5': 69.86949074258042
    '6': 365.0914231326921
    '7': 196.6411116527317
    '8': 49.47637008735963
  policy_reward_mean:
    '1': 341.51091945833383
    '2': -52.27742960369802
    '3': 38.949571772435796
    '4': 160.2516606063824
    '5': -30.698550531742608
    '6': 291.5882878770625
    '7': 66.88863750968093
    '8': -47.804177000103884
  policy_reward_min:
    '1': 252.4665218940231
    '2': -133.33805457908318
    '3': -44.43399419536562
    '4': 87.1335107596237
    '5': -109.27772951674473
    '6': 136.80962548901064
    '7': -68.3147472987151
    '8': -226.1086357542355
  sampler_perf:
    mean_action_processing_ms: 0.20538357100251925
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 38.6943961954635
    mean_inference_ms: 6.257946475528688
    mean_raw_obs_processing_ms: 0.7137385737810523
  time_since_restore: 1121.1269745826721
  time_this_iter_s: 142.8289759159088
  time_total_s: 1121.1269745826721
  timers:
    learn_throughput: 135.997
    learn_time_ms: 29412.386
    load_throughput: 19796.133
    load_time_ms: 202.06
    sample_throughput: 42.224
    sample_time_ms: 94732.343
    update_time_ms: 16.484
  timestamp: 1651043971
  timesteps_since_restore: 0
  timesteps_total: 36000
  training_iteration: 9
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |      9 |          1121.13 | 36000 |  768.409 |              1039.74 |                508.3 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 320000
  custom_metrics:
    eps_sum_utility_max: 959.0258312912525
    eps_sum_utility_mean: 501.8886123397484
    eps_sum_utility_min: -61.07695946169346
    sum_utility_max: 27.841390419717424
    sum_utility_mean: 18.50409490691914
    sum_utility_min: -18.373396185126754
  date: 2022-04-27_12-51-54
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1090.280199405111
  episode_reward_mean: 826.7407954157757
  episode_reward_min: 508.3000600613391
  episodes_this_iter: 40
  episodes_total: 400
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.873653769493103
          entropy_coeff: 0.0
          kl: 0.008280958980321884
          model: {}
          policy_loss: -0.012456947937607765
          total_loss: 12224.3955078125
          vf_explained_var: -1.0898036634898745e-05
          vf_loss: 12224.4072265625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7038673162460327
          entropy_coeff: 0.0
          kl: 0.012753548100590706
          model: {}
          policy_loss: -0.01452938187867403
          total_loss: 208.1817169189453
          vf_explained_var: 0.6481765508651733
          vf_loss: 208.1924285888672
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7947684526443481
          entropy_coeff: 0.0
          kl: 0.012548152357339859
          model: {}
          policy_loss: -0.016562139615416527
          total_loss: 319.964599609375
          vf_explained_var: 0.26811155676841736
          vf_loss: 319.9773864746094
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7695682048797607
          entropy_coeff: 0.0
          kl: 0.011170987971127033
          model: {}
          policy_loss: -0.014076022431254387
          total_loss: 426.39251708984375
          vf_explained_var: -0.00026376594905741513
          vf_loss: 426.4015808105469
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8664149045944214
          entropy_coeff: 0.0
          kl: 0.00930448155850172
          model: {}
          policy_loss: -0.013883295468986034
          total_loss: 160.47802734375
          vf_explained_var: 0.6809830665588379
          vf_loss: 160.48773193359375
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8371024131774902
          entropy_coeff: 0.0
          kl: 0.01242049876600504
          model: {}
          policy_loss: -0.014126078225672245
          total_loss: 9578.314453125
          vf_explained_var: 8.429250556218904e-06
          vf_loss: 9578.326171875
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.706493854522705
          entropy_coeff: 0.0
          kl: 0.011059058830142021
          model: {}
          policy_loss: -0.017420444637537003
          total_loss: 610.1561889648438
          vf_explained_var: 0.3791210949420929
          vf_loss: 610.1703491210938
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7580293416976929
          entropy_coeff: 0.0
          kl: 0.014223387464880943
          model: {}
          policy_loss: -0.028469132259488106
          total_loss: 505.5987854003906
          vf_explained_var: 0.5055888295173645
          vf_loss: 505.6208801269531
    num_agent_steps_sampled: 320000
    num_agent_steps_trained: 320000
    num_steps_sampled: 40000
    num_steps_trained: 40000
  iterations_since_restore: 10
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.28854166666667
    ram_util_percent: 77.75989583333335
  pid: 141171
  policy_reward_max:
    '1': 386.8264626727526
    '2': 16.966011682244364
    '3': 111.98267913020777
    '4': 210.58759132067902
    '5': 42.33972016935706
    '6': 369.9235801353287
    '7': 193.80288695537396
    '8': 108.00877419282548
  policy_reward_mean:
    '1': 349.0538631434832
    '2': -50.72512270134738
    '3': 42.0353399391014
    '4': 161.58312705963397
    '5': -30.06577237264353
    '6': 306.90460865062056
    '7': 79.20210818123856
    '8': -31.247356484311204
  policy_reward_min:
    '1': 283.36520779547374
    '2': -133.33805457908318
    '3': -44.43399419536562
    '4': 62.546377172322785
    '5': -109.27772951674473
    '6': 242.4748223949694
    '7': -18.592965012720565
    '8': -156.49596415145567
  sampler_perf:
    mean_action_processing_ms: 0.20802692473784262
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 39.664677226037746
    mean_inference_ms: 6.327649812052457
    mean_raw_obs_processing_ms: 0.7229941572946467
  time_since_restore: 1264.5823578834534
  time_this_iter_s: 143.45538330078125
  time_total_s: 1264.5823578834534
  timers:
    learn_throughput: 135.554
    learn_time_ms: 29508.539
    load_throughput: 21824.342
    load_time_ms: 183.282
    sample_throughput: 41.424
    sample_time_ms: 96561.756
    update_time_ms: 16.33
  timestamp: 1651044114
  timesteps_since_restore: 0
  timesteps_total: 40000
  training_iteration: 10
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |     10 |          1264.58 | 40000 |  826.741 |              1090.28 |                508.3 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 352000
  custom_metrics:
    eps_sum_utility_max: 959.0258312912525
    eps_sum_utility_mean: 624.214454369267
    eps_sum_utility_min: 158.72114734624316
    sum_utility_max: 27.841390419717424
    sum_utility_mean: 18.172094233323154
    sum_utility_min: -18.373396185126754
  date: 2022-04-27_12-54-20
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1154.3029593445501
  episode_reward_mean: 859.7207739935657
  episode_reward_min: 508.3000600613391
  episodes_this_iter: 40
  episodes_total: 440
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.8668626546859741
          entropy_coeff: 0.0
          kl: 0.009583859704434872
          model: {}
          policy_loss: -0.01187286525964737
          total_loss: 10573.798828125
          vf_explained_var: -6.818002475483809e-06
          vf_loss: 10573.8076171875
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.707664132118225
          entropy_coeff: 0.0
          kl: 0.009342444129288197
          model: {}
          policy_loss: -0.017051370814442635
          total_loss: 232.60169982910156
          vf_explained_var: 0.6307535767555237
          vf_loss: 232.61595153808594
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7952468395233154
          entropy_coeff: 0.0
          kl: 0.012803050689399242
          model: {}
          policy_loss: -0.01753770187497139
          total_loss: 226.63563537597656
          vf_explained_var: 0.43858784437179565
          vf_loss: 226.64935302734375
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7363358736038208
          entropy_coeff: 0.0
          kl: 0.010988696478307247
          model: {}
          policy_loss: -0.018245162442326546
          total_loss: 330.9607849121094
          vf_explained_var: 0.00022595928749069571
          vf_loss: 330.97406005859375
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8514490127563477
          entropy_coeff: 0.0
          kl: 0.006308418232947588
          model: {}
          policy_loss: -0.01601473242044449
          total_loss: 203.4080810546875
          vf_explained_var: 0.6172977685928345
          vf_loss: 203.4212646484375
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7878512144088745
          entropy_coeff: 0.0
          kl: 0.011948551051318645
          model: {}
          policy_loss: -0.015664760023355484
          total_loss: 7995.69384765625
          vf_explained_var: 6.789161488995887e-06
          vf_loss: 7995.70556640625
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6729882955551147
          entropy_coeff: 0.0
          kl: 0.012321768328547478
          model: {}
          policy_loss: -0.018023865297436714
          total_loss: 384.6804504394531
          vf_explained_var: 0.48615187406539917
          vf_loss: 384.6947937011719
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7285100221633911
          entropy_coeff: 0.0
          kl: 0.015717191621661186
          model: {}
          policy_loss: -0.027886781841516495
          total_loss: 243.6455535888672
          vf_explained_var: 0.6139090657234192
          vf_loss: 243.6663360595703
    num_agent_steps_sampled: 352000
    num_agent_steps_trained: 352000
    num_steps_sampled: 44000
    num_steps_trained: 44000
  iterations_since_restore: 11
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 35.978974358974355
    ram_util_percent: 77.81538461538463
  pid: 141171
  policy_reward_max:
    '1': 378.7747864593695
    '2': 53.228779032703926
    '3': 111.98267913020777
    '4': 210.58759132067902
    '5': 68.08377573114646
    '6': 369.9235801353287
    '7': 213.5775684911459
    '8': 108.00877419282548
  policy_reward_mean:
    '1': 354.94171230862594
    '2': -48.458455850887205
    '3': 39.844211308288976
    '4': 166.8130406687891
    '5': -29.42774037209397
    '6': 311.79907807681786
    '7': 87.40451320360366
    '8': -23.195585349578902
  policy_reward_min:
    '1': 284.4813001577453
    '2': -105.54014379176996
    '3': -60.81688938244292
    '4': 62.546377172322785
    '5': -79.13272590966986
    '6': 245.926361354683
    '7': 12.67478694341326
    '8': -156.49596415145567
  sampler_perf:
    mean_action_processing_ms: 0.2101273307028785
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 40.469549634533735
    mean_inference_ms: 6.382710990595515
    mean_raw_obs_processing_ms: 0.7302365003034808
  time_since_restore: 1408.145514011383
  time_this_iter_s: 143.5631561279297
  time_total_s: 1408.145514011383
  timers:
    learn_throughput: 133.946
    learn_time_ms: 29862.761
    load_throughput: 290397.901
    load_time_ms: 13.774
    sample_throughput: 39.476
    sample_time_ms: 101326.649
    update_time_ms: 16.338
  timestamp: 1651044260
  timesteps_since_restore: 0
  timesteps_total: 44000
  training_iteration: 11
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |     11 |          1408.15 | 44000 |  859.721 |               1154.3 |                508.3 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 384000
  custom_metrics:
    eps_sum_utility_max: 1020.3330669398949
    eps_sum_utility_mean: 706.3724918599316
    eps_sum_utility_min: 325.9754607821018
    sum_utility_max: 27.8519433609848
    sum_utility_mean: 18.88354620179266
    sum_utility_min: -8.856092900234987
  date: 2022-04-27_12-56-49
  done: false
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1178.276074629709
  episode_reward_mean: 876.3005434692187
  episode_reward_min: 697.9071727003559
  episodes_this_iter: 40
  episodes_total: 480
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.862334132194519
          entropy_coeff: 0.0
          kl: 0.011883438564836979
          model: {}
          policy_loss: -0.012603992596268654
          total_loss: 9174.912109375
          vf_explained_var: -4.264616109139752e-06
          vf_loss: 9174.9208984375
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7089667320251465
          entropy_coeff: 0.0
          kl: 0.008915075100958347
          model: {}
          policy_loss: -0.013223210349678993
          total_loss: 180.52850341796875
          vf_explained_var: 0.7032256722450256
          vf_loss: 180.53907775878906
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7756448984146118
          entropy_coeff: 0.0
          kl: 0.009852109476923943
          model: {}
          policy_loss: -0.01746947318315506
          total_loss: 249.53538513183594
          vf_explained_var: 0.42929527163505554
          vf_loss: 249.5498809814453
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7212021350860596
          entropy_coeff: 0.0
          kl: 0.006089237984269857
          model: {}
          policy_loss: -0.010469364002346992
          total_loss: 244.99305725097656
          vf_explained_var: 0.3031706213951111
          vf_loss: 245.0008087158203
      '5':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.8392325639724731
          entropy_coeff: 0.0
          kl: 0.006756109651178122
          model: {}
          policy_loss: -0.010816879570484161
          total_loss: 125.51844024658203
          vf_explained_var: 0.7477715611457825
          vf_loss: 125.52620697021484
      '6':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7684425115585327
          entropy_coeff: 0.0
          kl: 0.009483243338763714
          model: {}
          policy_loss: -0.011422988027334213
          total_loss: 6695.5556640625
          vf_explained_var: 3.205191660526907e-06
          vf_loss: 6695.564453125
      '7':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6521384716033936
          entropy_coeff: 0.0
          kl: 0.014831355772912502
          model: {}
          policy_loss: -0.02129918336868286
          total_loss: 350.2177734375
          vf_explained_var: 0.5581590533256531
          vf_loss: 350.23455810546875
      '8':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.7047526836395264
          entropy_coeff: 0.0
          kl: 0.00967060960829258
          model: {}
          policy_loss: -0.02143053151667118
          total_loss: 173.57156372070312
          vf_explained_var: 0.6759705543518066
          vf_loss: 173.58868408203125
    num_agent_steps_sampled: 384000
    num_agent_steps_trained: 384000
    num_steps_sampled: 48000
    num_steps_trained: 48000
  iterations_since_restore: 12
  node_ip: 10.0.3.106
  num_healthy_workers: 2
  off_policy_estimator: {}
  perf:
    cpu_util_percent: 36.596969696969694
    ram_util_percent: 77.83333333333334
  pid: 141171
  policy_reward_max:
    '1': 379.9996923585933
    '2': 53.228779032703926
    '3': 111.1049203386392
    '4': 203.10886955533712
    '5': 68.08377573114646
    '6': 363.6407414594212
    '7': 213.5775684911459
    '8': 54.00505889111178
  policy_reward_mean:
    '1': 358.99425443739494
    '2': -48.8454492482259
    '3': 34.5506397573266
    '4': 170.4929316831263
    '5': -28.242756195847427
    '6': 314.7251468527049
    '7': 90.83254404529818
    '8': -16.206767862559012
  policy_reward_min:
    '1': 303.3015447575422
    '2': -110.50103067498914
    '3': -61.79930702545966
    '4': 120.31077073347635
    '5': -79.13272590966986
    '6': 252.00615257234102
    '7': 12.67478694341326
    '8': -85.68844465198234
  sampler_perf:
    mean_action_processing_ms: 0.21187842418330646
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 41.15895806330439
    mean_inference_ms: 6.4283281774684475
    mean_raw_obs_processing_ms: 0.736408208964024
  time_since_restore: 1556.716356754303
  time_this_iter_s: 148.57084274291992
  time_total_s: 1556.716356754303
  timers:
    learn_throughput: 130.691
    learn_time_ms: 30606.513
    load_throughput: 277999.529
    load_time_ms: 14.389
    sample_throughput: 38.032
    sample_time_ms: 105174.692
    update_time_ms: 16.333
  timestamp: 1651044409
  timesteps_since_restore: 0
  timesteps_total: 48000
  training_iteration: 12
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |     12 |          1556.72 | 48000 |  876.301 |              1178.28 |              697.907 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


Result for PPO_MultiAgentMobileEnv_a3fcd_00000:
  agent_timesteps_total: 416000
  custom_metrics:
    eps_sum_utility_max: 1056.8440858161673
    eps_sum_utility_mean: 781.6352629103111
    eps_sum_utility_min: 484.3216318023563
    sum_utility_max: 27.8519433609848
    sum_utility_mean: 19.536864504264223
    sum_utility_min: -8.856092900234987
  date: 2022-04-27_12-59-14
  done: true
  episode_len_mean: 100.0
  episode_media: {}
  episode_reward_max: 1178.276074629709
  episode_reward_mean: 917.0723937645033
  episode_reward_min: 754.7805288868832
  episodes_this_iter: 40
  episodes_total: 520
  experiment_id: e7eb6542365a40b7aca1c0fcf0476b24
  hostname: abhishek-pc
  info:
    learner:
      '1':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.846374750137329
          entropy_coeff: 0.0
          kl: 0.006767970509827137
          model: {}
          policy_loss: -0.00861415546387434
          total_loss: 7575.19677734375
          vf_explained_var: -2.649522684805561e-06
          vf_loss: 7575.2041015625
      '2':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.6888257265090942
          entropy_coeff: 0.0
          kl: 0.011470437981188297
          model: {}
          policy_loss: -0.016802523285150528
          total_loss: 257.36236572265625
          vf_explained_var: 0.5519177913665771
          vf_loss: 257.3757019042969
      '3':
        learner_stats:
          cur_kl_coeff: 0.30000001192092896
          cur_lr: 4.999999873689376e-05
          entropy: 1.7675007581710815
          entropy_coeff: 0.0
          kl: 0.010507478378713131
          model: {}
          policy_loss: -0.016770143061876297
          total_loss: 175.08399963378906
          vf_explained_var: 0.5867058634757996
          vf_loss: 175.0976104736328
      '4':
        learner_stats:
          cur_kl_coeff: 0.44999998807907104
          cur_lr: 4.999999873689376e-05
          entropy: 1.693199872970581
          entropy_coeff: 0.0
          kl: 0.0075401305221021175
          model: {}
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
    cpu_util_percent: 36.285051546391756
    ram_util_percent: 77.81288659793815
  pid: 141171
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
    mean_action_processing_ms: 0.21331966280919906
    mean_env_render_ms: 0.0
    mean_env_wait_ms: 41.74321014299261
    mean_inference_ms: 6.466655489484297
    mean_raw_obs_processing_ms: 0.7415596071839192
  time_since_restore: 1701.8365452289581
  time_this_iter_s: 145.12018847465515
  time_total_s: 1701.8365452289581
  timers:
    learn_throughput: 128.846
    learn_time_ms: 31044.778
    load_throughput: 275527.308
    load_time_ms: 14.518
    sample_throughput: 37.199
    sample_time_ms: 107529.597
    update_time_ms: 16.312
  timestamp: 1651044554
  timesteps_since_restore: 0
  timesteps_total: 52000
  training_iteration: 13
  trial_id: a3fcd_00000
  
== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 3.0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 RUNNING)
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status   | loc               |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | RUNNING  | 10.0.3.106:141171 |     13 |          1701.84 | 52000 |  917.072 |              1178.28 |              754.781 |                100 |
+-------------------------------------+----------+-------------------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


== Status ==
Memory usage on this node: 5.9/7.6 GiB
Using FIFO scheduling algorithm.
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/2.83 GiB heap, 0.0/1.42 GiB objects
Result logdir: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54
Number of trials: 1/1 (1 TERMINATED)
+-------------------------------------+------------+-------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+
| Trial name                          | status     | loc   |   iter |   total time (s) |    ts |   reward |   episode_reward_max |   episode_reward_min |   episode_len_mean |
|-------------------------------------+------------+-------+--------+------------------+-------+----------+----------------------+----------------------+--------------------|
| PPO_MultiAgentMobileEnv_a3fcd_00000 | TERMINATED |       |     13 |          1701.84 | 52000 |  917.072 |              1178.28 |              754.781 |                100 |
+-------------------------------------+------------+-------+--------+------------------+-------+----------+----------------------+----------------------+--------------------+


2022-04-27 12:59:15,993	INFO tune.py:549 -- Total run time: 1761.95 seconds (1761.11 seconds for the tuning loop).
INFO:deepcomp.util.simulation:Training done                  episode_reward_mean=917.072 episodes_total=520 log_dir=/home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54/PPO_MultiAgentMobileEnv_a3fcd_00000_0_2022-04-27_12-29-54 num_steps_sampled=52000 num_steps_trained=52000 timesteps_total=52000
2022-04-27 12:59:16,222	INFO trainer.py:671 -- Tip: set framework=tfe or the --eager flag to enable TensorFlow eager execution
2022-04-27 12:59:16,222	WARNING deprecation.py:33 -- DeprecationWarning: `monitor` has been deprecated. Use `record_env` instead. This will raise an error in the future!
2022-04-27 12:59:16,222	INFO trainer.py:696 -- Current log_level is ERROR. For more information, set 'log_level': 'INFO' / 'DEBUG' or use the -v and -vv flags.
2022-04-27 13:00:32,132	INFO trainable.py:101 -- Trainable.setup took 75.926 seconds. If your trainable is slow to initialize, consider setting reuse_actors=True to reduce actor creation overheads.
INFO:deepcomp.util.simulation:Loading PPO agent              checkpoint=/home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54/PPO_MultiAgentMobileEnv_a3fcd_00000_0_2022-04-27_12-29-54/checkpoint_000013/checkpoint-13
2022-04-27 13:00:38,645	INFO trainable.py:377 -- Restored on 10.0.3.106 from checkpoint: /home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54/PPO_MultiAgentMobileEnv_a3fcd_00000_0_2022-04-27_12-29-54/checkpoint_000013/checkpoint-13
2022-04-27 13:00:38,645	INFO trainable.py:385 -- Current state after restoring: {'_iteration': 13, '_timesteps_total': None, '_time_total': 1701.8365452289581, '_episodes_total': 520}
INFO:deepcomp.util.simulation:Agent loaded                   agent=PPO checkpoint=None rllib_dir=/home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54/PPO_MultiAgentMobileEnv_a3fcd_00000_0_2022-04-27_12-29-54/checkpoint_000013/checkpoint-13
INFO:deepcomp.util.simulation:Loaded training progress       progress_file=/home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54/PPO_MultiAgentMobileEnv_a3fcd_00000_0_2022-04-27_12-29-54/progress.csv train_iteration=13 train_steps=52000
WARNING:deepcomp.util.simulation:Evaluating with a single worker for reproducibility and compatibility.
INFO:deepcomp.util.simulation:Starting evaluation            fast_ues=2 num_episodes=1 num_workers=1 slow_ues=5 static_ues=1
DEBUG:deepcomp.util.simulation:Step                           action={'1': 6, '2': 3, '3': 2, '4': 6, '5': 3, '6': 5, '7': 1, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.09], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.048, 1.0, 0.01, 0.002, 0.002, 0.004], 'utility': [0.125], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.004, 0.04], 'utility': [0.372], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.003, 1.0, 0.011], 'utility': [0.173], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.016, 1.0, 0.025, 0.004, 0.002, 0.003], 'utility': [0.162], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.03, 0.071, 0.584, 0.654, 0.076, 0.031], 'utility': [-0.178], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.004, 0.008, 0.016, 0.016], 'utility': [0.499], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.028, 0.009, 0.077, 1.0, 0.025, 0.006, 0.005], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '2': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.014, 0.044, 1.0, 0.01, 0.002, 0.002, 0.004], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '3': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.008, 0.002, 0.002, 0.003, 0.035], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.014], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '5': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.039, 0.016, 1.0, 0.029, 0.004, 0.002, 0.003], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '6': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.034, 0.083, 0.787, 0.714, 0.079, 0.033], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.013, 0.007, 0.009, 0.02, 0.055, 0.04], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, '8': {'connected': [0, 0, 0, 0, 0, 0, 0], 'dr': [0.031, 0.011, 0.081, 1.0, 0.029, 0.007, 0.005], 'utility': [-1.0], 'ues_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'util_at_bs': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}} reward={'1': 2.624, '2': 2.867, '3': 7.436, '4': 2.624, '5': 2.867, '6': 1.874, '7': 9.979, '8': -0.796} t=1
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 0, '3': 7, '4': 7, '5': 6, '6': 1, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.247], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.016, 0.053, 1.0, 0.01, 0.003, 0.002, 0.004], 'utility': [0.003], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.024, 1.0, 0.009, 0.002, 0.002, 0.004, 0.046], 'utility': [0.349], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.009], 'utility': [0.576], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.016, 1.0, 0.021, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.027, 0.06, 0.438, 0.595, 0.073, 0.029], 'utility': [-0.038], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.003, 0.002, 0.002, 0.002, 0.004, 0.005], 'utility': [0.566], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.026, 0.008, 0.075, 1.0, 0.021, 0.005, 0.004], 'utility': [0.002], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.09], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.048, 1.0, 0.01, 0.002, 0.002, 0.004], 'utility': [0.125], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.004, 0.04], 'utility': [0.372], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.003, 1.0, 0.011], 'utility': [0.173], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.016, 1.0, 0.025, 0.004, 0.002, 0.003], 'utility': [0.162], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '6': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.03, 0.071, 0.584, 0.654, 0.076, 0.031], 'utility': [-0.178], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.004, 0.008, 0.016, 0.016], 'utility': [0.499], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.028, 0.009, 0.077, 1.0, 0.025, 0.006, 0.005], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.499, 0.372, 0.143, -0.04, -0.178, 0.131, 0.0]}} reward={'1': 3.289, '2': 2.968, '3': 6.99, '4': 3.289, '5': 2.968, '6': 2.463, '7': 5.283, '8': 0.048} t=2
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 7, '4': 7, '5': 6, '6': 6, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.057], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.017, 0.059, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.096], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.027, 1.0, 0.01, 0.003, 0.002, 0.004, 0.053], 'utility': [0.328], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.003, 1.0, 0.008], 'utility': [0.372], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.016, 1.0, 0.019, 0.003, 0.002, 0.003], 'utility': [0.212], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.052, 0.331, 0.538, 0.07, 0.027], 'utility': [-0.022], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.747], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.074, 1.0, 0.018, 0.005, 0.004], 'utility': [0.04], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.247], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.016, 0.053, 1.0, 0.01, 0.003, 0.002, 0.004], 'utility': [0.003], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.024, 1.0, 0.009, 0.002, 0.002, 0.004, 0.046], 'utility': [0.349], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.009], 'utility': [0.576], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.016, 1.0, 0.021, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.027, 0.06, 0.438, 0.595, 0.073, 0.029], 'utility': [-0.038], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.003, 0.002, 0.002, 0.002, 0.004, 0.005], 'utility': [0.566], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.026, 0.008, 0.075, 1.0, 0.021, 0.005, 0.004], 'utility': [0.002], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.264, 0.349, 0.148, 0.002, -0.038, 0.164, 0.0]}} reward={'1': 4.291, '2': 3.087, '3': 6.553, '4': 4.291, '5': 3.087, '6': 3.715, '7': 7.247, '8': 0.808} t=3
DEBUG:deepcomp.util.simulation:Step                           action={'1': 7, '2': 0, '3': 7, '4': 7, '5': 6, '6': 6, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.149], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.019, 0.067, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.012], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.011, 0.003, 0.002, 0.005, 0.061], 'utility': [0.306], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.614], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.017, 1.0, 0.017, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.022, 0.044, 0.253, 0.485, 0.068, 0.026], 'utility': [-0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.727], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.076, 1.0, 0.016, 0.004, 0.003], 'utility': [0.072], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.057], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.017, 0.059, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.096], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.027, 1.0, 0.01, 0.003, 0.002, 0.004, 0.053], 'utility': [0.328], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.003, 1.0, 0.008], 'utility': [0.372], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.016, 1.0, 0.019, 0.003, 0.002, 0.003], 'utility': [0.212], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.052, 0.331, 0.538, 0.07, 0.027], 'utility': [-0.022], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.747], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.074, 1.0, 0.018, 0.005, 0.004], 'utility': [0.04], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.362, 0.328, 0.154, 0.04, -0.022, 0.215, 0.0]}} reward={'1': 4.652, '2': 3.056, '3': 6.125, '4': 4.652, '5': 3.056, '6': 4.751, '7': 7.199, '8': 1.444} t=4
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 7, '4': 7, '5': 6, '6': 6, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.033], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.077, 1.0, 0.012, 0.003, 0.002, 0.006], 'utility': [0.064], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.07], 'utility': [0.285], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.006], 'utility': [0.481], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.018, 1.0, 0.016, 0.003, 0.002, 0.003], 'utility': [0.236], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.02, 0.038, 0.196, 0.435, 0.067, 0.024], 'utility': [0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.003, 0.002, 0.002, 0.004], 'utility': [0.531], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.082, 1.0, 0.015, 0.004, 0.003], 'utility': [0.096], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.149], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.019, 0.067, 1.0, 0.011, 0.003, 0.002, 0.005], 'utility': [0.012], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.011, 0.003, 0.002, 0.005, 0.061], 'utility': [0.306], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.614], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.017, 1.0, 0.017, 0.003, 0.002, 0.003], 'utility': [0.294], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.022, 0.044, 0.253, 0.485, 0.068, 0.026], 'utility': [-0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.001, 0.001, 0.001, 0.001, 0.002], 'utility': [0.727], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.076, 1.0, 0.016, 0.004, 0.003], 'utility': [0.072], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.36, 0.306, 0.153, 0.072, -0.007, 0.233, 0.0]}} reward={'1': 5.139, '2': 3.003, '3': 5.705, '4': 5.139, '5': 3.003, '6': 3.63, '7': 5.376, '8': 1.915} t=5
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 7, '4': 7, '5': 6, '6': 6, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.096], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.089, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.003], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.04, 1.0, 0.013, 0.004, 0.003, 0.006, 0.08], 'utility': [0.281], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.629], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.02, 1.0, 0.015, 0.003, 0.002, 0.003], 'utility': [0.282], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.019, 0.033, 0.153, 0.389, 0.066, 0.023], 'utility': [0.02], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.022, 0.016, 0.007, 0.004, 0.005, 0.01], 'utility': [0.315], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.093, 1.0, 0.014, 0.004, 0.003], 'utility': [0.109], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.033], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.02, 0.077, 1.0, 0.012, 0.003, 0.002, 0.006], 'utility': [0.064], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.07], 'utility': [0.285], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.006], 'utility': [0.481], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.018, 1.0, 0.016, 0.003, 0.002, 0.003], 'utility': [0.236], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.02, 0.038, 0.196, 0.435, 0.067, 0.024], 'utility': [0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.004, 0.003, 0.002, 0.002, 0.004], 'utility': [0.531], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.023, 0.007, 0.082, 1.0, 0.015, 0.004, 0.003], 'utility': [0.096], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.0], 'util_at_bs': [0.269, 0.285, 0.15, 0.096, 0.007, 0.257, 0.0]}} reward={'1': 5.327, '2': 2.847, '3': 5.63, '4': 5.327, '5': 2.847, '6': 2.367, '7': 3.353, '8': 2.183} t=6
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 6, '4': 7, '5': 6, '6': 6, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.017], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.104, 1.0, 0.013, 0.004, 0.003, 0.007], 'utility': [0.028], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.045, 1.0, 0.014, 0.004, 0.003, 0.007, 0.092], 'utility': [0.264], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.53], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.022, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.237], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.028, 0.122, 0.349, 0.066, 0.023], 'utility': [0.031], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.052, 0.017, 0.009, 0.009, 0.019], 'utility': [0.13], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.027, 0.008, 0.113, 1.0, 0.015, 0.004, 0.004], 'utility': [0.111], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.096], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.089, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.003], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.04, 1.0, 0.013, 0.004, 0.003, 0.006, 0.08], 'utility': [0.281], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.629], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.02, 1.0, 0.015, 0.003, 0.002, 0.003], 'utility': [0.282], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.019, 0.033, 0.153, 0.389, 0.066, 0.023], 'utility': [0.02], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.022, 0.016, 0.007, 0.004, 0.005, 0.01], 'utility': [0.315], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.024, 0.008, 0.093, 1.0, 0.014, 0.004, 0.003], 'utility': [0.109], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.168, 0.281, 0.142, 0.109, 0.02, 0.266, 0.281]}} reward={'1': 5.466, '2': 2.651, '3': 5.273, '4': 5.466, '5': 2.651, '6': 1.286, '7': 1.615, '8': 2.225} t=7
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 6, '4': 7, '5': 6, '6': 6, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.123, 1.0, 0.014, 0.004, 0.003, 0.008], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.051, 1.0, 0.016, 0.004, 0.004, 0.008, 0.105], 'utility': [0.247], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.61], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.025, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.256], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.016, 0.025, 0.098, 0.314, 0.067, 0.022], 'utility': [0.041], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.149, 0.15, 0.036, 0.016, 0.015, 0.033], 'utility': [-0.025], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.032, 0.01, 0.146, 1.0, 0.016, 0.004, 0.004], 'utility': [0.102], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.017], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.104, 1.0, 0.013, 0.004, 0.003, 0.007], 'utility': [0.028], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.045, 1.0, 0.014, 0.004, 0.003, 0.007, 0.092], 'utility': [0.264], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.53], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.022, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.237], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.028, 0.122, 0.349, 0.066, 0.023], 'utility': [0.031], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.052, 0.017, 0.009, 0.009, 0.019], 'utility': [0.13], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.027, 0.008, 0.113, 1.0, 0.015, 0.004, 0.004], 'utility': [0.111], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.081, 0.264, 0.133, 0.111, 0.031, 0.273, 0.264]}} reward={'1': 5.47, '2': 2.384, '3': 4.93, '4': 5.47, '5': 2.384, '6': 0.384, '7': 2.006, '8': 2.037} t=8
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 6, '4': 7, '5': 6, '6': 6, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.147, 1.0, 0.015, 0.004, 0.004, 0.009], 'utility': [-0.011], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.057, 1.0, 0.017, 0.005, 0.004, 0.009, 0.119], 'utility': [0.23], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.526], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.029, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.218], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.022, 0.081, 0.283, 0.069, 0.022], 'utility': [0.049], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.31, 0.401, 0.064, 0.025, 0.022, 0.05], 'utility': [-0.155], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.039, 0.012, 0.201, 1.0, 0.017, 0.005, 0.005], 'utility': [0.082], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.063], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.123, 1.0, 0.014, 0.004, 0.003, 0.008], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.051, 1.0, 0.016, 0.004, 0.004, 0.008, 0.105], 'utility': [0.247], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.0, 0.002, 1.0, 0.005], 'utility': [0.61], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.025, 1.0, 0.014, 0.003, 0.002, 0.003], 'utility': [0.256], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.016, 0.025, 0.098, 0.314, 0.067, 0.022], 'utility': [0.041], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.149, 0.15, 0.036, 0.016, 0.015, 0.033], 'utility': [-0.025], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.032, 0.01, 0.146, 1.0, 0.016, 0.004, 0.004], 'utility': [0.102], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.008, 0.247, 0.119, 0.102, 0.041, 0.273, 0.247]}} reward={'1': 5.335, '2': 2.917, '3': 4.601, '4': 5.335, '5': 2.075, '6': -0.384, '7': 1.324, '8': 1.928} t=9
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 6, '4': 7, '5': 6, '6': 6, '7': 3, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.176, 1.0, 0.017, 0.005, 0.004, 0.01], 'utility': [-0.097], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.064, 1.0, 0.019, 0.005, 0.005, 0.01, 0.136], 'utility': [0.214], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.558], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.034, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.169], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.02, 0.068, 0.258, 0.073, 0.022], 'utility': [0.054], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.986, 0.559, 1.0, 0.103, 0.035, 0.031, 0.07], 'utility': [-0.193], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.05, 0.015, 0.291, 1.0, 0.02, 0.006, 0.006], 'utility': [0.053], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.007], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.032, 0.147, 1.0, 0.015, 0.004, 0.004, 0.009], 'utility': [-0.011], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.057, 1.0, 0.017, 0.005, 0.004, 0.009, 0.119], 'utility': [0.23], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.526], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.029, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.218], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.022, 0.081, 0.283, 0.069, 0.022], 'utility': [0.049], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.31, 0.401, 0.064, 0.025, 0.022, 0.05], 'utility': [-0.155], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.039, 0.012, 0.201, 1.0, 0.017, 0.005, 0.005], 'utility': [0.082], 'ues_at_bs': [0.25, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.053, 0.23, 0.104, 0.082, 0.049, 0.267, 0.23]}} reward={'1': 5.156, '2': 0.47, '3': 4.286, '4': 5.156, '5': -0.801, '6': -0.56, '7': -0.147, '8': -0.337} t=10
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 6, '4': 2, '5': 6, '6': 6, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.001], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.041, 0.213, 1.0, 0.018, 0.005, 0.005, 0.011], 'utility': [-0.137], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.072, 1.0, 0.02, 0.006, 0.005, 0.011, 0.154], 'utility': [0.199], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.0, 0.001, 0.004, 1.0, 0.006], 'utility': [0.483], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.039, 0.04, 1.0, 0.014, 0.003, 0.002, 0.005], 'utility': [0.099], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.019, 0.058, 0.237, 0.078, 0.023], 'utility': [0.057], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.402, 0.371, 1.0, 0.063, 0.019, 0.017, 0.038], 'utility': [-0.158], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.067, 0.02, 0.442, 1.0, 0.023, 0.008, 0.007], 'utility': [0.017], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.176, 1.0, 0.017, 0.005, 0.004, 0.01], 'utility': [-0.097], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.064, 1.0, 0.019, 0.005, 0.005, 0.01, 0.136], 'utility': [0.214], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.0, 0.001, 0.003, 1.0, 0.005], 'utility': [0.558], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.036, 0.034, 1.0, 0.014, 0.003, 0.002, 0.004], 'utility': [0.169], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.02, 0.068, 0.258, 0.073, 0.022], 'utility': [0.054], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.986, 0.559, 1.0, 0.103, 0.035, 0.031, 0.07], 'utility': [-0.193], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.05, 0.015, 0.291, 1.0, 0.02, 0.006, 0.006], 'utility': [0.053], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.069, 0.214, -0.04, 0.053, 0.054, 0.258, 0.214]}} reward={'1': 4.839, '2': 0.019, '3': 3.985, '4': 4.839, '5': -1.302, '6': -0.293, '7': -0.323, '8': -0.893} t=11
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 6, '4': 7, '5': 4, '6': 6, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.029], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.047, 0.259, 1.0, 0.02, 0.006, 0.005, 0.013], 'utility': [-0.223], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 1.0, 0.022, 0.006, 0.006, 0.013, 0.174], 'utility': [0.185], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.001, 0.001, 0.001, 0.005, 1.0, 0.007], 'utility': [0.481], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.048, 1.0, 0.015, 0.003, 0.003, 0.005], 'utility': [0.032], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.018, 0.051, 0.221, 0.086, 0.024], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.167, 0.227, 1.0, 0.037, 0.011, 0.009, 0.02], 'utility': [-0.076], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.091, 0.027, 0.695, 1.0, 0.028, 0.009, 0.009], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.001], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.041, 0.213, 1.0, 0.018, 0.005, 0.005, 0.011], 'utility': [-0.137], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.072, 1.0, 0.02, 0.006, 0.005, 0.011, 0.154], 'utility': [0.199], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.0, 0.001, 0.004, 1.0, 0.006], 'utility': [0.483], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.039, 0.04, 1.0, 0.014, 0.003, 0.002, 0.005], 'utility': [0.099], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.019, 0.058, 0.237, 0.078, 0.023], 'utility': [0.057], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.402, 0.371, 1.0, 0.063, 0.019, 0.017, 0.038], 'utility': [-0.158], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.067, 0.02, 0.442, 1.0, 0.023, 0.008, 0.007], 'utility': [0.017], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [-0.05, 0.199, -0.065, 0.017, 0.057, 0.242, 0.199]}} reward={'1': 4.524, '2': -0.41, '3': 3.698, '4': 4.524, '5': -1.779, '6': 3.415, '7': -0.41, '8': -1.455} t=12
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 2, '3': 3, '4': 7, '5': 4, '6': 6, '7': 4, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.003], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.054, 0.317, 1.0, 0.021, 0.006, 0.006, 0.015], 'utility': [-0.118], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.089, 1.0, 0.023, 0.007, 0.006, 0.014, 0.198], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.011, 0.001, 0.001, 0.001, 0.006, 1.0, 0.008], 'utility': [0.414], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.059, 1.0, 0.016, 0.004, 0.003, 0.006], 'utility': [0.059], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.017, 0.046, 0.209, 0.097, 0.026], 'utility': [0.169], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.072, 0.131, 1.0, 0.021, 0.006, 0.005, 0.01], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.112, 0.033, 1.0, 0.89, 0.031, 0.011, 0.011], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.029], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '2': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.047, 0.259, 1.0, 0.02, 0.006, 0.005, 0.013], 'utility': [-0.223], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 1.0, 0.022, 0.006, 0.006, 0.013, 0.174], 'utility': [0.185], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.001, 0.001, 0.001, 0.005, 1.0, 0.007], 'utility': [0.481], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.048, 1.0, 0.015, 0.003, 0.003, 0.005], 'utility': [0.032], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.018, 0.051, 0.221, 0.086, 0.024], 'utility': [0.171], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.167, 0.227, 1.0, 0.037, 0.011, 0.009, 0.02], 'utility': [-0.076], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}, '8': {'connected': [0, 0, 0, 1, 0, 0, 0], 'dr': [0.091, 0.027, 0.695, 1.0, 0.028, 0.009, 0.009], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.171, 0.185, -0.089, -0.024, 0.171, 0.226, 0.185]}} reward={'1': 4.113, '2': -1.087, '3': -1.848, '4': 4.113, '5': -0.643, '6': 3.372, '7': -1.087, '8': -0.706} t=13
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 0, '3': 3, '4': 7, '5': 4, '6': 6, '7': 7, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.061, 0.39, 1.0, 0.023, 0.007, 0.007, 0.017], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.1, 1.0, 0.025, 0.008, 0.007, 0.016, 0.223], 'utility': [-0.067], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.014, 0.001, 0.001, 0.001, 0.008, 1.0, 0.009], 'utility': [0.394], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.05, 0.072, 1.0, 0.017, 0.004, 0.003, 0.007], 'utility': [-0.021], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.043, 0.2, 0.112, 0.028], 'utility': [0.163], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.075, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.094], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.094, 0.028, 1.0, 0.539, 0.023, 0.008, 0.009], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.003], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.054, 0.317, 1.0, 0.021, 0.006, 0.006, 0.015], 'utility': [-0.118], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.089, 1.0, 0.023, 0.007, 0.006, 0.014, 0.198], 'utility': [-0.08], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.011, 0.001, 0.001, 0.001, 0.006, 1.0, 0.008], 'utility': [0.414], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.059, 1.0, 0.016, 0.004, 0.003, 0.006], 'utility': [0.059], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.014, 0.017, 0.046, 0.209, 0.097, 0.026], 'utility': [0.169], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.072, 0.131, 1.0, 0.021, 0.006, 0.005, 0.01], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.112, 0.033, 1.0, 0.89, 0.031, 0.011, 0.011], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.169, -0.099, -0.032, -0.048, 0.169, 0.206, -0.08]}} reward={'1': 3.724, '2': -1.006, '3': -1.701, '4': 3.724, '5': -0.57, '6': 3.254, '7': -1.006, '8': -0.721} t=14
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 0, '3': 3, '4': 7, '5': 4, '6': 6, '7': 7, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.007], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.071, 0.481, 1.0, 0.025, 0.008, 0.007, 0.02], 'utility': [-0.123], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.111, 1.0, 0.027, 0.008, 0.007, 0.017, 0.252], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.018, 0.002, 0.001, 0.002, 0.011, 1.0, 0.011], 'utility': [0.335], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.055, 0.089, 1.0, 0.018, 0.004, 0.004, 0.008], 'utility': [0.0], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.04, 0.194, 0.132, 0.032], 'utility': [0.153], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.05], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.078, 0.024, 1.0, 0.323, 0.016, 0.006, 0.007], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.061, 0.39, 1.0, 0.023, 0.007, 0.007, 0.017], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.1, 1.0, 0.025, 0.008, 0.007, 0.016, 0.223], 'utility': [-0.067], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.014, 0.001, 0.001, 0.001, 0.008, 1.0, 0.009], 'utility': [0.394], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.05, 0.072, 1.0, 0.017, 0.004, 0.003, 0.007], 'utility': [-0.021], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.043, 0.2, 0.112, 0.028], 'utility': [0.163], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.034, 0.075, 1.0, 0.012, 0.003, 0.003, 0.006], 'utility': [0.094], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.094, 0.028, 1.0, 0.539, 0.023, 0.008, 0.009], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.163, -0.094, -0.028, -0.066, 0.163, 0.186, -0.067]}} reward={'1': 3.282, '2': -1.018, '3': -1.555, '4': 3.282, '5': -1.018, '6': 3.063, '7': -1.018, '8': -0.73} t=15
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 0, '3': 3, '4': 7, '5': 4, '6': 6, '7': 7, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.018], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.081, 0.596, 1.0, 0.028, 0.009, 0.008, 0.023], 'utility': [-0.127], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.123, 1.0, 0.029, 0.009, 0.008, 0.019, 0.284], 'utility': [-0.044], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.002, 0.001, 0.002, 0.014, 1.0, 0.012], 'utility': [0.305], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.061, 0.11, 1.0, 0.019, 0.005, 0.004, 0.009], 'utility': [-0.073], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.016, 0.038, 0.191, 0.16, 0.036], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.072], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.065, 0.02, 1.0, 0.192, 0.012, 0.005, 0.006], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.007], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.071, 0.481, 1.0, 0.025, 0.008, 0.007, 0.02], 'utility': [-0.123], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.111, 1.0, 0.027, 0.008, 0.007, 0.017, 0.252], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.018, 0.002, 0.001, 0.002, 0.011, 1.0, 0.011], 'utility': [0.335], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.055, 0.089, 1.0, 0.018, 0.004, 0.004, 0.008], 'utility': [0.0], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.015, 0.016, 0.04, 0.194, 0.132, 0.032], 'utility': [0.153], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.05], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.078, 0.024, 1.0, 0.323, 0.016, 0.006, 0.007], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.153, -0.089, -0.032, -0.055, 0.153, 0.164, -0.055]}} reward={'1': 2.867, '2': -1.076, '3': -1.431, '4': 2.867, '5': -1.076, '6': 2.804, '7': -1.076, '8': -0.703} t=16
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 3, '4': 7, '5': 4, '6': 6, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.093, 0.742, 1.0, 0.03, 0.01, 0.01, 0.027], 'utility': [-0.13], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.136, 1.0, 0.031, 0.01, 0.009, 0.021, 0.32], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.029, 0.003, 0.002, 0.003, 0.018, 1.0, 0.015], 'utility': [0.252], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.137, 1.0, 0.02, 0.005, 0.004, 0.01], 'utility': [-0.077], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.018, 0.017, 0.038, 0.19, 0.197, 0.042], 'utility': [0.124], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.044], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.017, 1.0, 0.116, 0.009, 0.004, 0.005], 'utility': [0.017], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.018], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.081, 0.596, 1.0, 0.028, 0.009, 0.008, 0.023], 'utility': [-0.127], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.123, 1.0, 0.029, 0.009, 0.008, 0.019, 0.284], 'utility': [-0.044], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.002, 0.001, 0.002, 0.014, 1.0, 0.012], 'utility': [0.305], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.061, 0.11, 1.0, 0.019, 0.005, 0.004, 0.009], 'utility': [-0.073], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.017, 0.016, 0.038, 0.191, 0.16, 0.036], 'utility': [0.14], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.072], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.065, 0.02, 1.0, 0.192, 0.012, 0.005, 0.006], 'utility': [-0.024], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.14, -0.085, -0.038, -0.024, 0.14, 0.143, -0.044]}} reward={'1': 2.429, '2': -1.025, '3': -1.296, '4': 2.429, '5': -1.025, '6': 2.456, '7': -1.025, '8': -0.513} t=17
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 0, '3': 3, '4': 7, '5': 4, '6': 6, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.027], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.106, 0.928, 1.0, 0.033, 0.011, 0.011, 0.031], 'utility': [-0.127], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.151, 1.0, 0.033, 0.011, 0.01, 0.023, 0.36], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.038, 0.003, 0.002, 0.004, 0.024, 1.0, 0.017], 'utility': [0.207], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.073, 0.172, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.117], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '6': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [1.0, 0.02, 0.018, 0.038, 0.192, 0.247, 0.049], 'utility': [0.108], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.07, 0.177, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.242], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.045, 0.015, 1.0, 0.071, 0.006, 0.003, 0.004], 'utility': [0.097], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.093, 0.742, 1.0, 0.03, 0.01, 0.01, 0.027], 'utility': [-0.13], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.136, 1.0, 0.031, 0.01, 0.009, 0.021, 0.32], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.029, 0.003, 0.002, 0.003, 0.018, 1.0, 0.015], 'utility': [0.252], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.137, 1.0, 0.02, 0.005, 0.004, 0.01], 'utility': [-0.077], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '6': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.018, 0.017, 0.038, 0.19, 0.197, 0.042], 'utility': [0.124], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.061, 1.0, 0.01, 0.003, 0.002, 0.005], 'utility': [0.044], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.017, 1.0, 0.116, 0.009, 0.004, 0.005], 'utility': [0.017], 'ues_at_bs': [0.125, 0.25, 0.5, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, -0.081, -0.036, 0.017, 0.124, 0.121, -0.032]}} reward={'1': 1.919, '2': -1.792, '3': -1.135, '4': 1.919, '5': -1.792, '6': 2.012, '7': -1.792, '8': -1.945} t=18
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 3, '4': 7, '5': 4, '6': 0, '7': 2, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.026], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.105, 1.0, 0.86, 0.031, 0.011, 0.011, 0.031], 'utility': [-0.199], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.167, 1.0, 0.035, 0.012, 0.011, 0.026, 0.404], 'utility': [-0.072], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.049, 0.004, 0.003, 0.005, 0.031, 1.0, 0.02], 'utility': [0.156], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.08, 0.215, 1.0, 0.023, 0.007, 0.006, 0.014], 'utility': [-0.116], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.022, 0.019, 0.038, 0.195, 0.314, 0.059], 'utility': [0.05], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.18, 0.471, 1.0, 0.039, 0.012, 0.011, 0.028], 'utility': [-0.173], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.025], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.027], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.106, 0.928, 1.0, 0.033, 0.011, 0.011, 0.031], 'utility': [-0.127], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.151, 1.0, 0.033, 0.011, 0.01, 0.023, 0.36], 'utility': [-0.022], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.038, 0.003, 0.002, 0.004, 0.024, 1.0, 0.017], 'utility': [0.207], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.073, 0.172, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.117], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '6': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [1.0, 0.02, 0.018, 0.038, 0.192, 0.247, 0.049], 'utility': [0.108], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.07, 0.177, 1.0, 0.021, 0.006, 0.005, 0.012], 'utility': [-0.242], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.045, 0.015, 1.0, 0.071, 0.006, 0.003, 0.004], 'utility': [0.097], 'ues_at_bs': [0.125, 0.25, 0.5, 0.0, 0.125, 0.375, 0.125], 'util_at_bs': [0.108, -0.074, -0.097, 0.0, 0.108, 0.096, -0.022]}} reward={'1': 1.198, '2': -2.589, '3': -2.581, '4': 1.198, '5': -2.589, '6': 1.15, '7': -2.589, '8': -2.311} t=19
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 3, '4': 5, '5': 4, '6': 5, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.035], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.095, 1.0, 0.683, 0.027, 0.009, 0.009, 0.028], 'utility': [-0.197], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.184, 1.0, 0.037, 0.013, 0.012, 0.029, 0.453], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.062, 0.005, 0.003, 0.006, 0.04, 1.0, 0.023], 'utility': [0.117], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.088, 0.269, 1.0, 0.025, 0.007, 0.006, 0.016], 'utility': [-0.155], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.024, 0.02, 0.039, 0.2, 0.406, 0.071], 'utility': [0.029], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.377, 1.0, 0.887, 0.057, 0.021, 0.02, 0.056], 'utility': [-0.209], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.091], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.026], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.105, 1.0, 0.86, 0.031, 0.011, 0.011, 0.031], 'utility': [-0.199], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.167, 1.0, 0.035, 0.012, 0.011, 0.026, 0.404], 'utility': [-0.072], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.049, 0.004, 0.003, 0.005, 0.031, 1.0, 0.02], 'utility': [0.156], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.08, 0.215, 1.0, 0.023, 0.007, 0.006, 0.014], 'utility': [-0.116], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.022, 0.019, 0.038, 0.195, 0.314, 0.059], 'utility': [0.05], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.18, 0.471, 1.0, 0.039, 0.012, 0.011, 0.028], 'utility': [-0.173], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.025], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.05, -0.148, -0.116, 0.0, 0.0, 0.06, -0.072]}} reward={'1': 0.743, '2': -2.659, '3': -2.571, '4': 0.743, '5': -2.659, '6': 0.704, '7': -2.253, '8': -2.351} t=20
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 3, '4': 5, '5': 4, '6': 5, '7': 1, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.053], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.54, 0.023, 0.008, 0.008, 0.026], 'utility': [-0.181], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.203, 1.0, 0.04, 0.014, 0.013, 0.031, 0.507], 'utility': [-0.038], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.078, 0.006, 0.004, 0.007, 0.052, 1.0, 0.026], 'utility': [0.054], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.096, 0.338, 1.0, 0.027, 0.008, 0.007, 0.018], 'utility': [-0.138], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.027, 0.021, 0.04, 0.206, 0.531, 0.086], 'utility': [-0.118], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '7': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.393, 1.0, 0.421, 0.042, 0.017, 0.019, 0.057], 'utility': [-0.134], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.074], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.035], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.095, 1.0, 0.683, 0.027, 0.009, 0.009, 0.028], 'utility': [-0.197], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.184, 1.0, 0.037, 0.013, 0.012, 0.029, 0.453], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.062, 0.005, 0.003, 0.006, 0.04, 1.0, 0.023], 'utility': [0.117], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.088, 0.269, 1.0, 0.025, 0.007, 0.006, 0.016], 'utility': [-0.155], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.024, 0.02, 0.039, 0.2, 0.406, 0.071], 'utility': [0.029], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.377, 1.0, 0.887, 0.057, 0.021, 0.02, 0.056], 'utility': [-0.209], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.091], 'ues_at_bs': [0.125, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [0.029, -0.153, -0.118, 0.0, 0.0, 0.037, -0.054]}} reward={'1': -0.78, '2': -2.087, '3': -1.952, '4': -0.78, '5': -2.087, '6': -1.475, '7': -2.182, '8': -1.89} t=21
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 3, '4': 5, '5': 4, '6': 5, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.062], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.077, 1.0, 0.426, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.175], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.224, 1.0, 0.042, 0.015, 0.014, 0.035, 0.567], 'utility': [-0.026], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.098, 0.007, 0.005, 0.009, 0.067, 1.0, 0.03], 'utility': [0.012], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.105, 0.424, 1.0, 0.028, 0.009, 0.008, 0.021], 'utility': [-0.177], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.031, 0.023, 0.042, 0.214, 0.702, 0.104], 'utility': [-0.128], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.438, 1.0, 0.232, 0.033, 0.016, 0.019, 0.065], 'utility': [-0.117], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.017, 1.0, 0.038, 0.005, 0.003, 0.004], 'utility': [0.167], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.053], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.54, 0.023, 0.008, 0.008, 0.026], 'utility': [-0.181], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.203, 1.0, 0.04, 0.014, 0.013, 0.031, 0.507], 'utility': [-0.038], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.078, 0.006, 0.004, 0.007, 0.052, 1.0, 0.026], 'utility': [0.054], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.096, 0.338, 1.0, 0.027, 0.008, 0.007, 0.018], 'utility': [-0.138], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.027, 0.021, 0.04, 0.206, 0.531, 0.086], 'utility': [-0.118], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '7': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.393, 1.0, 0.421, 0.042, 0.017, 0.019, 0.057], 'utility': [-0.134], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.042, 0.015, 1.0, 0.059, 0.006, 0.003, 0.003], 'utility': [0.074], 'ues_at_bs': [0.25, 0.375, 0.5, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.126, -0.117, -0.094, 0.0, 0.0, -0.039, -0.038]}} reward={'1': -1.189, '2': -1.677, '3': -1.724, '4': -1.694, '5': -1.677, '6': -1.694, '7': -2.255, '8': -1.23} t=22
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 3, '4': 5, '5': 4, '6': 5, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.069], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.069, 1.0, 0.334, 0.017, 0.006, 0.007, 0.021], 'utility': [-0.17], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.246, 1.0, 0.044, 0.016, 0.015, 0.038, 0.633], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.123, 0.008, 0.006, 0.011, 0.085, 1.0, 0.034], 'utility': [-0.034], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.114, 0.531, 1.0, 0.031, 0.01, 0.009, 0.024], 'utility': [-0.144], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.034, 0.025, 0.044, 0.222, 0.935, 0.128], 'utility': [-0.132], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.529, 1.0, 0.152, 0.029, 0.016, 0.022, 0.085], 'utility': [-0.094], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.028, 1.0, 0.034, 0.005, 0.003, 0.005], 'utility': [0.06], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.062], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.077, 1.0, 0.426, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.175], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.224, 1.0, 0.042, 0.015, 0.014, 0.035, 0.567], 'utility': [-0.026], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.098, 0.007, 0.005, 0.009, 0.067, 1.0, 0.03], 'utility': [0.012], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.105, 0.424, 1.0, 0.028, 0.009, 0.008, 0.021], 'utility': [-0.177], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.031, 0.023, 0.042, 0.214, 0.702, 0.104], 'utility': [-0.128], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.438, 1.0, 0.232, 0.033, 0.016, 0.019, 0.065], 'utility': [-0.117], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.046, 0.017, 1.0, 0.038, 0.005, 0.003, 0.004], 'utility': [0.167], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.123, -0.106, -0.062, 0.0, 0.0, -0.059, -0.026]}} reward={'1': -1.564, '2': -1.794, '3': -1.506, '4': -1.844, '5': -1.794, '6': -1.844, '7': -2.037, '8': -1.702} t=23
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 3, '4': 5, '5': 4, '6': 5, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.078], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.061, 1.0, 0.261, 0.014, 0.006, 0.006, 0.019], 'utility': [-0.179], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.27, 1.0, 0.047, 0.017, 0.016, 0.042, 0.707], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.152, 0.009, 0.007, 0.014, 0.108, 1.0, 0.038], 'utility': [-0.075], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.123, 0.667, 1.0, 0.033, 0.011, 0.01, 0.028], 'utility': [-0.195], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.798, 0.031, 0.021, 0.036, 0.185, 1.0, 0.125], 'utility': [-0.13], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.68, 1.0, 0.117, 0.029, 0.019, 0.029, 0.131], 'utility': [-0.082], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.117, 0.059, 1.0, 0.038, 0.008, 0.005, 0.009], 'utility': [0.002], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.069], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.069, 1.0, 0.334, 0.017, 0.006, 0.007, 0.021], 'utility': [-0.17], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.246, 1.0, 0.044, 0.016, 0.015, 0.038, 0.633], 'utility': [-0.018], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.123, 0.008, 0.006, 0.011, 0.085, 1.0, 0.034], 'utility': [-0.034], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.114, 0.531, 1.0, 0.031, 0.01, 0.009, 0.024], 'utility': [-0.144], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [1.0, 0.034, 0.025, 0.044, 0.222, 0.935, 0.128], 'utility': [-0.132], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.529, 1.0, 0.152, 0.029, 0.016, 0.022, 0.085], 'utility': [-0.094], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.067, 0.028, 1.0, 0.034, 0.005, 0.003, 0.005], 'utility': [0.06], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.113, -0.094, -0.085, 0.0, 0.0, -0.078, -0.018]}} reward={'1': -1.887, '2': -2.161, '3': -1.453, '4': -1.981, '5': -2.161, '6': -1.981, '7': -1.952, '8': -2.339} t=24
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 3, '4': 5, '5': 4, '6': 5, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.084], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.054, 1.0, 0.203, 0.012, 0.005, 0.005, 0.017], 'utility': [-0.197], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.296, 1.0, 0.05, 0.018, 0.018, 0.046, 0.788], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.188, 0.011, 0.008, 0.017, 0.137, 1.0, 0.043], 'utility': [-0.117], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.133, 0.836, 1.0, 0.035, 0.012, 0.011, 0.031], 'utility': [-0.192], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.592, 0.026, 0.017, 0.029, 0.143, 1.0, 0.114], 'utility': [-0.122], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.888, 1.0, 0.105, 0.032, 0.024, 0.042, 0.235], 'utility': [-0.084], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.215, 0.144, 1.0, 0.047, 0.012, 0.009, 0.018], 'utility': [-0.141], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.078], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.061, 1.0, 0.261, 0.014, 0.006, 0.006, 0.019], 'utility': [-0.179], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.27, 1.0, 0.047, 0.017, 0.016, 0.042, 0.707], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.152, 0.009, 0.007, 0.014, 0.108, 1.0, 0.038], 'utility': [-0.075], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.123, 0.667, 1.0, 0.033, 0.011, 0.01, 0.028], 'utility': [-0.195], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.798, 0.031, 0.021, 0.036, 0.185, 1.0, 0.125], 'utility': [-0.13], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.68, 1.0, 0.117, 0.029, 0.019, 0.029, 0.131], 'utility': [-0.082], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.117, 0.059, 1.0, 0.038, 0.008, 0.005, 0.009], 'utility': [0.002], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.106, -0.092, -0.124, 0.0, 0.0, -0.094, -0.015]}} reward={'1': -2.152, '2': -2.752, '3': -1.554, '4': -2.116, '5': -2.752, '6': -2.116, '7': -2.008, '8': -2.943} t=25
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 5, '5': 2, '6': 5, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.092], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.047, 1.0, 0.158, 0.01, 0.004, 0.005, 0.016], 'utility': [-0.252], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.324, 1.0, 0.052, 0.019, 0.019, 0.05, 0.877], 'utility': [-0.036], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.229, 0.013, 0.01, 0.02, 0.173, 1.0, 0.048], 'utility': [-0.154], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.955, 0.036, 0.012, 0.012, 0.034], 'utility': [-0.169], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.438, 0.022, 0.014, 0.022, 0.11, 1.0, 0.103], 'utility': [-0.108], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.887, 0.092, 0.033, 0.029, 0.06, 0.42], 'utility': [-0.13], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.377, 0.372, 1.0, 0.061, 0.019, 0.016, 0.037], 'utility': [-0.21], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.084], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.054, 1.0, 0.203, 0.012, 0.005, 0.005, 0.017], 'utility': [-0.197], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.296, 1.0, 0.05, 0.018, 0.018, 0.046, 0.788], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.188, 0.011, 0.008, 0.017, 0.137, 1.0, 0.043], 'utility': [-0.117], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.133, 0.836, 1.0, 0.035, 0.012, 0.011, 0.031], 'utility': [-0.192], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.592, 0.026, 0.017, 0.029, 0.143, 1.0, 0.114], 'utility': [-0.122], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.888, 1.0, 0.105, 0.032, 0.024, 0.042, 0.235], 'utility': [-0.084], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.215, 0.144, 1.0, 0.047, 0.012, 0.009, 0.018], 'utility': [-0.141], 'ues_at_bs': [0.25, 0.375, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.103, -0.099, -0.177, 0.0, 0.0, -0.108, -0.015]}} reward={'1': -2.357, '2': -3.478, '3': -2.492, '4': -2.364, '5': -3.478, '6': -2.364, '7': -2.458, '8': -3.232} t=26
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 5, '5': 7, '6': 0, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.096], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.122, 0.008, 0.003, 0.004, 0.014], 'utility': [-0.301], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.354, 1.0, 0.055, 0.021, 0.021, 0.055, 0.975], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.278, 0.015, 0.012, 0.025, 0.218, 1.0, 0.053], 'utility': [-0.192], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.117, 1.0, 0.762, 0.03, 0.011, 0.011, 0.031], 'utility': [-0.182], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.324, 0.018, 0.011, 0.017, 0.085, 1.0, 0.094], 'utility': [-0.088], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.739, 0.08, 0.033, 0.034, 0.083, 0.776], 'utility': [-0.18], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '8': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.601, 0.998, 1.0, 0.078, 0.028, 0.027, 0.072], 'utility': [-0.264], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.092], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.047, 1.0, 0.158, 0.01, 0.004, 0.005, 0.016], 'utility': [-0.252], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.324, 1.0, 0.052, 0.019, 0.019, 0.05, 0.877], 'utility': [-0.036], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.229, 0.013, 0.01, 0.02, 0.173, 1.0, 0.048], 'utility': [-0.154], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.955, 0.036, 0.012, 0.012, 0.034], 'utility': [-0.169], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.438, 0.022, 0.014, 0.022, 0.11, 1.0, 0.103], 'utility': [-0.108], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.887, 0.092, 0.033, 0.029, 0.06, 0.42], 'utility': [-0.13], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.377, 0.372, 1.0, 0.061, 0.019, 0.016, 0.037], 'utility': [-0.21], 'ues_at_bs': [0.25, 0.5, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.119, -0.147, -0.21, 0.0, 0.0, -0.118, -0.036]}} reward={'1': -2.507, '2': -4.304, '3': -3.404, '4': -2.576, '5': -4.304, '6': -2.576, '7': -3.222, '8': -3.979} t=27
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 5, '5': 7, '6': 0, '7': 7, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.082], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.093, 0.007, 0.003, 0.003, 0.012], 'utility': [-0.306], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.357, 0.924, 0.054, 0.021, 0.021, 0.055, 1.0], 'utility': [-0.156], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.335, 0.017, 0.014, 0.03, 0.273, 1.0, 0.058], 'utility': [-0.134], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.1, 1.0, 0.61, 0.026, 0.009, 0.009, 0.028], 'utility': [-0.199], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.24, 0.015, 0.009, 0.014, 0.066, 1.0, 0.085], 'utility': [-0.051], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.604, 0.395, 0.047, 0.022, 0.025, 0.074, 1.0], 'utility': [-0.08], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '8': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.311, 1.0, 0.359, 0.035, 0.015, 0.016, 0.05], 'utility': [-0.235], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.096], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.122, 0.008, 0.003, 0.004, 0.014], 'utility': [-0.301], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.354, 1.0, 0.055, 0.021, 0.021, 0.055, 0.975], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '4': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.278, 0.015, 0.012, 0.025, 0.218, 1.0, 0.053], 'utility': [-0.192], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.117, 1.0, 0.762, 0.03, 0.011, 0.011, 0.031], 'utility': [-0.182], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.324, 0.018, 0.011, 0.017, 0.085, 1.0, 0.094], 'utility': [-0.088], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.739, 0.08, 0.033, 0.034, 0.083, 0.776], 'utility': [-0.18], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}, '8': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.601, 0.998, 1.0, 0.078, 0.028, 0.027, 0.072], 'utility': [-0.264], 'ues_at_bs': [0.25, 0.625, 0.375, 0.0, 0.0, 0.375, 0.125], 'util_at_bs': [-0.134, -0.195, -0.249, 0.0, 0.0, -0.125, -0.047]}} reward={'1': -1.778, '2': -4.287, '3': -3.46, '4': -2.187, '5': -4.287, '6': -2.106, '7': -3.152, '8': -3.782} t=28
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 7, '5': 7, '6': 0, '7': 3, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.085], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.071, 0.006, 0.002, 0.003, 0.011], 'utility': [-0.185], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.351, 0.833, 0.051, 0.02, 0.02, 0.055, 1.0], 'utility': [-0.089], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.401, 0.019, 0.016, 0.036, 0.34, 1.0, 0.064], 'utility': [-0.127], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.488, 0.022, 0.008, 0.008, 0.025], 'utility': [-0.106], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.178, 0.013, 0.007, 0.011, 0.051, 1.0, 0.077], 'utility': [-0.033], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.149, 0.019, 0.01, 0.013, 0.047, 1.0], 'utility': [-0.031], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.121, 0.014, 0.007, 0.008, 0.031], 'utility': [-0.201], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.082], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.093, 0.007, 0.003, 0.003, 0.012], 'utility': [-0.306], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.357, 0.924, 0.054, 0.021, 0.021, 0.055, 1.0], 'utility': [-0.156], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.335, 0.017, 0.014, 0.03, 0.273, 1.0, 0.058], 'utility': [-0.134], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.1, 1.0, 0.61, 0.026, 0.009, 0.009, 0.028], 'utility': [-0.199], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.24, 0.015, 0.009, 0.014, 0.066, 1.0, 0.085], 'utility': [-0.051], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '7': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.604, 0.395, 0.047, 0.022, 0.025, 0.074, 1.0], 'utility': [-0.08], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}, '8': {'connected': [1, 1, 1, 0, 0, 0, 0], 'dr': [0.311, 1.0, 0.359, 0.035, 0.015, 0.016, 0.05], 'utility': [-0.235], 'ues_at_bs': [0.375, 0.625, 0.375, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.122, -0.195, -0.247, 0.0, -0.134, -0.089, -0.118]}} reward={'1': -1.628, '2': -2.903, '3': -2.334, '4': -1.817, '5': -2.903, '6': -1.697, '7': -1.539, '8': -2.415} t=29
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 7, '5': 7, '6': 0, '7': 5, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.083], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.054, 0.005, 0.002, 0.002, 0.009], 'utility': [-0.237], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.345, 0.752, 0.048, 0.019, 0.02, 0.054, 1.0], 'utility': [-0.074], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.477, 0.022, 0.019, 0.043, 0.423, 1.0, 0.07], 'utility': [-0.137], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.391, 0.019, 0.007, 0.007, 0.023], 'utility': [-0.038], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.133, 0.01, 0.006, 0.008, 0.039, 1.0, 0.069], 'utility': [0.02], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.086, 0.05, 0.007, 0.004, 0.006, 0.026, 1.0], 'utility': [0.12], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.051, 1.0, 0.038, 0.005, 0.003, 0.004, 0.017], 'utility': [-0.237], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.085], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '2': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.071, 0.006, 0.002, 0.003, 0.011], 'utility': [-0.185], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.351, 0.833, 0.051, 0.02, 0.02, 0.055, 1.0], 'utility': [-0.089], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.401, 0.019, 0.016, 0.036, 0.34, 1.0, 0.064], 'utility': [-0.127], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.086, 1.0, 0.488, 0.022, 0.008, 0.008, 0.025], 'utility': [-0.106], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.178, 0.013, 0.007, 0.011, 0.051, 1.0, 0.077], 'utility': [-0.033], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.149, 0.019, 0.01, 0.013, 0.047, 1.0], 'utility': [-0.031], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.137, 1.0, 0.121, 0.014, 0.007, 0.008, 0.031], 'utility': [-0.201], 'ues_at_bs': [0.375, 0.5, 0.25, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [-0.088, -0.145, -0.145, 0.0, -0.127, -0.081, -0.06]}} reward={'1': -1.332, '2': -2.933, '3': -1.802, '4': -0.655, '5': -2.499, '6': -0.237, '7': 0.933, '8': -2.933} t=30
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 7, '5': 7, '6': 0, '7': 5, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.073], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.022, 1.0, 0.041, 0.004, 0.002, 0.002, 0.008], 'utility': [-0.226], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.339, 0.679, 0.046, 0.018, 0.019, 0.053, 1.0], 'utility': [-0.064], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.563, 0.025, 0.022, 0.052, 0.524, 1.0, 0.076], 'utility': [-0.135], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.062, 1.0, 0.314, 0.016, 0.006, 0.006, 0.02], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.1, 0.009, 0.005, 0.007, 0.031, 1.0, 0.063], 'utility': [0.066], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.025, 0.015, 0.002, 0.001, 0.002, 0.012, 1.0], 'utility': [0.303], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.011, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.226], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.083], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.054, 0.005, 0.002, 0.002, 0.009], 'utility': [-0.237], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.345, 0.752, 0.048, 0.019, 0.02, 0.054, 1.0], 'utility': [-0.074], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.477, 0.022, 0.019, 0.043, 0.423, 1.0, 0.07], 'utility': [-0.137], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.391, 0.019, 0.007, 0.007, 0.023], 'utility': [-0.038], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.133, 0.01, 0.006, 0.008, 0.039, 1.0, 0.069], 'utility': [0.02], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.086, 0.05, 0.007, 0.004, 0.006, 0.026, 1.0], 'utility': [0.12], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.051, 1.0, 0.038, 0.005, 0.003, 0.004, 0.017], 'utility': [-0.237], 'ues_at_bs': [0.25, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.07, -0.147, -0.038, 0.0, -0.137, -0.067, 0.023]}} reward={'1': -0.953, '2': -2.815, '3': -0.736, '4': -0.85, '5': -2.438, '6': -0.386, '7': 2.395, '8': -2.815} t=31
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 7, '5': 7, '6': 0, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.086], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.031, 0.003, 0.001, 0.002, 0.007], 'utility': [-0.223], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.333, 0.615, 0.043, 0.018, 0.019, 0.052, 1.0], 'utility': [-0.057], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.66, 0.028, 0.025, 0.062, 0.647, 1.0, 0.082], 'utility': [-0.136], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.253, 0.013, 0.005, 0.006, 0.018], 'utility': [-0.057], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.077, 0.007, 0.004, 0.005, 0.025, 1.0, 0.058], 'utility': [0.075], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.006, 0.004, 0.001, 0.0, 0.001, 0.005, 1.0], 'utility': [0.536], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [-0.223], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.073], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.022, 1.0, 0.041, 0.004, 0.002, 0.002, 0.008], 'utility': [-0.226], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.339, 0.679, 0.046, 0.018, 0.019, 0.053, 1.0], 'utility': [-0.064], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.563, 0.025, 0.022, 0.052, 0.524, 1.0, 0.076], 'utility': [-0.135], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.062, 1.0, 0.314, 0.016, 0.006, 0.006, 0.02], 'utility': [-0.047], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '6': {'connected': [1, 0, 0, 0, 0, 1, 0], 'dr': [0.1, 0.009, 0.005, 0.007, 0.031, 1.0, 0.063], 'utility': [0.066], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.025, 0.015, 0.002, 0.001, 0.002, 0.012, 1.0], 'utility': [0.303], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.011, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.226], 'ues_at_bs': [0.125, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.066, -0.141, -0.047, 0.0, -0.135, -0.048, 0.12]}} reward={'1': -0.981, '2': -2.798, '3': -0.27, '4': -1.415, '5': -2.467, '6': -0.981, '7': 4.786, '8': -2.798} t=32
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 7, '5': 7, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.065], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.023, 0.002, 0.001, 0.001, 0.006], 'utility': [-0.224], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.327, 0.557, 0.041, 0.017, 0.018, 0.052, 1.0], 'utility': [-0.053], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.768, 0.032, 0.029, 0.074, 0.797, 1.0, 0.088], 'utility': [-0.128], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.045, 1.0, 0.205, 0.011, 0.005, 0.005, 0.017], 'utility': [-0.069], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.06, 0.006, 0.003, 0.005, 0.02, 1.0, 0.055], 'utility': [0.089], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0], 'utility': [0.719], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.003, 1.0, 0.002, 0.0, 0.0, 0.0, 0.004], 'utility': [-0.224], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.086], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.031, 0.003, 0.001, 0.002, 0.007], 'utility': [-0.223], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.333, 0.615, 0.043, 0.018, 0.019, 0.052, 1.0], 'utility': [-0.057], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.66, 0.028, 0.025, 0.062, 0.647, 1.0, 0.082], 'utility': [-0.136], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.253, 0.013, 0.005, 0.006, 0.018], 'utility': [-0.057], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.077, 0.007, 0.004, 0.005, 0.025, 1.0, 0.058], 'utility': [0.075], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.006, 0.004, 0.001, 0.0, 0.001, 0.005, 1.0], 'utility': [0.536], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [-0.223], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.14, -0.057, 0.0, -0.136, -0.049, 0.239]}} reward={'1': -0.694, '2': -2.848, '3': 0.321, '4': -1.161, '5': -2.554, '6': -0.694, '7': 6.658, '8': -2.848} t=33
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 7, '5': 7, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.073], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.017, 0.002, 0.001, 0.001, 0.005], 'utility': [-0.227], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.321, 0.506, 0.039, 0.016, 0.018, 0.051, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.887, 0.035, 0.034, 0.088, 0.978, 1.0, 0.095], 'utility': [-0.119], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.039, 1.0, 0.166, 0.01, 0.004, 0.004, 0.015], 'utility': [-0.081], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.048, 0.006, 0.003, 0.004, 0.016, 1.0, 0.052], 'utility': [0.128], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.003, 1.0], 'utility': [0.663], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.227], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.065], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.023, 0.002, 0.001, 0.001, 0.006], 'utility': [-0.224], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.327, 0.557, 0.041, 0.017, 0.018, 0.052, 1.0], 'utility': [-0.053], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.768, 0.032, 0.029, 0.074, 0.797, 1.0, 0.088], 'utility': [-0.128], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.045, 1.0, 0.205, 0.011, 0.005, 0.005, 0.017], 'utility': [-0.069], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.06, 0.006, 0.003, 0.005, 0.02, 1.0, 0.055], 'utility': [0.089], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.002, 1.0], 'utility': [0.719], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.003, 1.0, 0.002, 0.0, 0.0, 0.0, 0.004], 'utility': [-0.224], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.142, -0.069, 0.0, -0.128, -0.035, 0.333]}} reward={'1': -0.426, '2': -2.929, '3': 0.091, '4': -0.915, '5': -2.669, '6': -0.426, '7': 6.132, '8': -2.929} t=34
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 7, '5': 7, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.056], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.013, 0.001, 0.001, 0.001, 0.005], 'utility': [-0.232], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.316, 0.459, 0.037, 0.016, 0.017, 0.051, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.85, 0.033, 0.032, 0.087, 1.0, 0.835, 0.085], 'utility': [-0.107], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.033, 1.0, 0.135, 0.008, 0.003, 0.004, 0.013], 'utility': [-0.094], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.039, 0.005, 0.002, 0.003, 0.014, 1.0, 0.051], 'utility': [0.137], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.232], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.073], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.017, 0.002, 0.001, 0.001, 0.005], 'utility': [-0.227], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.321, 0.506, 0.039, 0.016, 0.018, 0.051, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.887, 0.035, 0.034, 0.088, 0.978, 1.0, 0.095], 'utility': [-0.119], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.039, 1.0, 0.166, 0.01, 0.004, 0.004, 0.015], 'utility': [-0.081], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.048, 0.006, 0.003, 0.004, 0.016, 1.0, 0.052], 'utility': [0.128], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.002, 0.001, 0.0, 0.0, 0.0, 0.003, 1.0], 'utility': [0.663], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.227], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.146, -0.081, 0.0, -0.119, -0.021, 0.307]}} reward={'1': -0.178, '2': -3.019, '3': -0.253, '4': -0.671, '5': -2.789, '6': -0.178, '7': 5.277, '8': -3.019} t=35
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 7, '5': 7, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.01, 0.001, 0.001, 0.001, 0.004], 'utility': [-0.237], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.31, 0.418, 0.035, 0.015, 0.017, 0.05, 1.0], 'utility': [-0.044], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.794, 0.03, 0.03, 0.084, 1.0, 0.684, 0.074], 'utility': [-0.094], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.028, 1.0, 0.111, 0.007, 0.003, 0.003, 0.012], 'utility': [-0.106], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.034, 0.005, 0.002, 0.003, 0.012, 1.0, 0.051], 'utility': [0.158], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.237], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.056], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.013, 0.001, 0.001, 0.001, 0.005], 'utility': [-0.232], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.316, 0.459, 0.037, 0.016, 0.017, 0.051, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.85, 0.033, 0.032, 0.087, 1.0, 0.835, 0.085], 'utility': [-0.107], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.033, 1.0, 0.135, 0.008, 0.003, 0.004, 0.013], 'utility': [-0.094], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.039, 0.005, 0.002, 0.003, 0.014, 1.0, 0.051], 'utility': [0.137], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.232], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.151, -0.094, 0.0, -0.107, -0.009, 0.264]}} reward={'1': 0.029, '2': -3.12, '3': -0.312, '4': -0.448, '5': -2.919, '6': 0.029, '7': 5.305, '8': -3.12} t=36
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 7, '5': 7, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.008, 0.001, 0.001, 0.001, 0.003], 'utility': [-0.248], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.305, 0.381, 0.034, 0.015, 0.016, 0.05, 1.0], 'utility': [-0.043], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.738, 0.027, 0.028, 0.081, 1.0, 0.562, 0.065], 'utility': [-0.079], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.091, 0.006, 0.003, 0.003, 0.011], 'utility': [-0.248], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.005, 0.002, 0.003, 0.011, 1.0, 0.052], 'utility': [0.155], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.015], 'utility': [-0.248], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.01, 0.001, 0.001, 0.001, 0.004], 'utility': [-0.237], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.31, 0.418, 0.035, 0.015, 0.017, 0.05, 1.0], 'utility': [-0.044], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.794, 0.03, 0.03, 0.084, 1.0, 0.684, 0.074], 'utility': [-0.094], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.028, 1.0, 0.111, 0.007, 0.003, 0.003, 0.012], 'utility': [-0.106], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.034, 0.005, 0.002, 0.003, 0.012, 1.0, 0.051], 'utility': [0.158], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.002, 0.0, 0.0, 0.001, 0.005], 'utility': [-0.237], 'ues_at_bs': [0.0, 0.5, 0.125, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.156, -0.106, 0.0, -0.094, 0.001, 0.265]}} reward={'1': 0.195, '2': -3.932, '3': -0.85, '4': -0.248, '5': -3.932, '6': 0.195, '7': 5.314, '8': -3.932} t=37
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 7, '5': 3, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.006, 0.001, 0.0, 0.001, 0.003], 'utility': [-0.266], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.3, 0.348, 0.032, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.045], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.684, 0.025, 0.026, 0.078, 1.0, 0.463, 0.057], 'utility': [-0.063], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.076, 0.005, 0.002, 0.003, 0.01], 'utility': [-0.266], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.005, 0.002, 0.003, 0.011, 1.0, 0.056], 'utility': [0.157], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.004, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.589], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.02, 0.005, 0.003, 0.006, 0.045], 'utility': [-0.266], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.008, 0.001, 0.001, 0.001, 0.003], 'utility': [-0.248], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.305, 0.381, 0.034, 0.015, 0.016, 0.05, 1.0], 'utility': [-0.043], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.738, 0.027, 0.028, 0.081, 1.0, 0.562, 0.065], 'utility': [-0.079], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.091, 0.006, 0.003, 0.003, 0.011], 'utility': [-0.248], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.005, 0.002, 0.003, 0.011, 1.0, 0.052], 'utility': [0.155], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.003, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.574], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.015], 'utility': [-0.248], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.197, 0.0, 0.0, -0.079, 0.01, 0.266]}} reward={'1': 0.313, '2': -4.211, '3': -0.993, '4': -0.079, '5': -4.211, '6': 0.313, '7': 5.443, '8': -4.211} t=38
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 1, '5': 3, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.005, 0.001, 0.0, 0.001, 0.003], 'utility': [-0.294], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.295, 0.318, 0.03, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.049], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.631, 0.022, 0.025, 0.076, 1.0, 0.383, 0.05], 'utility': [0.056], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.063, 0.005, 0.002, 0.002, 0.009], 'utility': [-0.294], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.061], 'utility': [0.148], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.01, 0.005, 0.001, 0.001, 0.001, 0.01, 1.0], 'utility': [0.433], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.256, 1.0, 0.053, 0.014, 0.01, 0.017, 0.109], 'utility': [-0.294], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.006, 0.001, 0.0, 0.001, 0.003], 'utility': [-0.266], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.3, 0.348, 0.032, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.045], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '4': {'connected': [0, 0, 0, 0, 1, 1, 0], 'dr': [0.684, 0.025, 0.026, 0.078, 1.0, 0.463, 0.057], 'utility': [-0.063], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.076, 0.005, 0.002, 0.003, 0.01], 'utility': [-0.266], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.005, 0.002, 0.003, 0.011, 1.0, 0.056], 'utility': [0.157], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.004, 0.002, 0.0, 0.0, 0.001, 0.005, 1.0], 'utility': [0.589], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.02, 0.005, 0.003, 0.006, 0.045], 'utility': [-0.266], 'ues_at_bs': [0.0, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.0, -0.211, 0.0, 0.0, -0.063, 0.016, 0.272]}} reward={'1': 1.157, '2': -4.657, '3': -1.402, '4': 1.144, '5': -4.657, '6': 2.232, '7': 3.844, '8': -3.501} t=39
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 7, '5': 3, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.03], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.004, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.334], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.29, 0.291, 0.029, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.115], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.58, 0.02, 0.023, 0.074, 1.0, 0.318, 0.044], 'utility': [0.025], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.016, 1.0, 0.054, 0.004, 0.002, 0.002, 0.009], 'utility': [-0.334], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 1], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.137], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.037, 0.014, 0.003, 0.002, 0.004, 0.024, 1.0], 'utility': [0.147], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.959, 1.0, 0.115, 0.034, 0.025, 0.042, 0.215], 'utility': [-0.114], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.005, 0.001, 0.0, 0.001, 0.003], 'utility': [-0.294], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.295, 0.318, 0.03, 0.014, 0.016, 0.049, 1.0], 'utility': [-0.049], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.631, 0.022, 0.025, 0.076, 1.0, 0.383, 0.05], 'utility': [0.056], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.063, 0.005, 0.002, 0.002, 0.009], 'utility': [-0.294], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.061], 'utility': [0.148], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.01, 0.005, 0.001, 0.001, 0.001, 0.01, 1.0], 'utility': [0.433], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}, '8': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.256, 1.0, 0.053, 0.014, 0.01, 0.017, 0.109], 'utility': [-0.294], 'ues_at_bs': [0.125, 0.5, 0.0, 0.0, 0.125, 0.375, 0.25], 'util_at_bs': [0.056, -0.233, 0.0, 0.0, 0.056, 0.058, 0.192]}} reward={'1': 0.881, '2': -4.478, '3': -1.812, '4': 0.229, '5': -4.478, '6': 1.003, '7': 1.125, '8': -3.28} t=40
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 1, '4': 7, '5': 7, '6': 7, '7': 4, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.019], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.382], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.286, 0.267, 0.027, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.032], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.532, 0.018, 0.022, 0.072, 1.0, 0.265, 0.038], 'utility': [0.021], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.046, 0.004, 0.002, 0.002, 0.008], 'utility': [-0.382], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.011, 1.0, 0.078], 'utility': [0.119], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.13, 0.04, 0.008, 0.006, 0.009, 0.052, 1.0], 'utility': [0.055], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.271, 0.059, 0.02, 0.015, 0.025, 0.097], 'utility': [-0.076], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.03], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.004, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.334], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '3': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.29, 0.291, 0.029, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.115], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '4': {'connected': [1, 0, 0, 0, 1, 1, 0], 'dr': [0.58, 0.02, 0.023, 0.074, 1.0, 0.318, 0.044], 'utility': [0.025], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.016, 1.0, 0.054, 0.004, 0.002, 0.002, 0.009], 'utility': [-0.334], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 1], 'dr': [0.026, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.137], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.037, 0.014, 0.003, 0.002, 0.004, 0.024, 1.0], 'utility': [0.147], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [0.959, 1.0, 0.115, 0.034, 0.025, 0.042, 0.215], 'utility': [-0.114], 'ues_at_bs': [0.25, 0.5, 0.0, 0.0, 0.125, 0.375, 0.375], 'util_at_bs': [-0.044, -0.224, 0.0, 0.0, 0.025, 0.044, 0.056]}} reward={'1': 0.993, '2': -4.365, '3': -2.082, '4': -0.329, '5': -4.365, '6': 0.61, '7': -0.257, '8': -2.742} t=41
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 6, '4': 7, '5': 3, '6': 7, '7': 2, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.01], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [-0.438], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.281, 0.245, 0.026, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.095], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.487, 0.017, 0.02, 0.07, 1.0, 0.221, 0.034], 'utility': [0.037], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.013, 1.0, 0.04, 0.003, 0.002, 0.002, 0.007], 'utility': [-0.438], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 1], 'dr': [0.027, 0.006, 0.003, 0.003, 0.012, 1.0, 0.091], 'utility': [0.093], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.426, 0.095, 0.02, 0.014, 0.021, 0.096, 1.0], 'utility': [-0.187], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.022, 0.01, 0.008, 0.011, 0.033], 'utility': [0.092], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.019], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.001, 0.0, 0.0, 0.003], 'utility': [-0.382], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.286, 0.267, 0.027, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.032], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.532, 0.018, 0.022, 0.072, 1.0, 0.265, 0.038], 'utility': [0.021], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.046, 0.004, 0.002, 0.002, 0.008], 'utility': [-0.382], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.026, 0.005, 0.002, 0.003, 0.011, 1.0, 0.078], 'utility': [0.119], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.13, 0.04, 0.008, 0.006, 0.009, 0.052, 1.0], 'utility': [0.055], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.271, 0.059, 0.02, 0.015, 0.025, 0.097], 'utility': [-0.076], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.029, -0.218, 0.0, 0.0, 0.021, 0.05, 0.011]}} reward={'1': 0.833, '2': -4.39, '3': -2.063, '4': 0.36, '5': -4.39, '6': -0.42, '7': -0.511, '8': -2.409} t=42
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 6, '4': 7, '5': 3, '6': 7, '7': 2, '8': 0} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.02], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [-0.292], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.277, 0.225, 0.025, 0.012, 0.015, 0.048, 1.0], 'utility': [-0.0], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.444, 0.015, 0.019, 0.069, 1.0, 0.186, 0.03], 'utility': [0.053], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [-0.292], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.028, 0.007, 0.003, 0.003, 0.012, 1.0, 0.107], 'utility': [0.059], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.152, 0.035, 0.022, 0.032, 0.115, 0.749], 'utility': [-0.23], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.01, 0.005, 0.003, 0.003, 0.003, 0.007], 'utility': [0.367], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.01], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [-0.438], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.281, 0.245, 0.026, 0.013, 0.015, 0.048, 1.0], 'utility': [-0.095], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.487, 0.017, 0.02, 0.07, 1.0, 0.221, 0.034], 'utility': [0.037], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.013, 1.0, 0.04, 0.003, 0.002, 0.002, 0.007], 'utility': [-0.438], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 1], 'dr': [0.027, 0.006, 0.003, 0.003, 0.012, 1.0, 0.091], 'utility': [0.093], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [0.426, 0.095, 0.02, 0.014, 0.021, 0.096, 1.0], 'utility': [-0.187], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}, '8': {'connected': [1, 1, 0, 0, 0, 0, 0], 'dr': [1.0, 0.062, 0.022, 0.01, 0.008, 0.011, 0.033], 'utility': [0.092], 'ues_at_bs': [0.375, 0.5, 0.0, 0.0, 0.125, 0.25, 0.375], 'util_at_bs': [0.012, -0.22, 0.0, 0.0, 0.037, 0.042, -0.063]}} reward={'1': 0.382, '2': -3.889, '3': -0.986, '4': 2.36, '5': -3.889, '6': -0.961, '7': 0.756, '8': 2.796} t=43
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 6, '4': 7, '5': 3, '6': 0, '7': 1, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.011], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.001, 0.003], 'utility': [-0.301], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.273, 0.208, 0.024, 0.012, 0.014, 0.048, 1.0], 'utility': [-0.004], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.405, 0.014, 0.018, 0.067, 1.0, 0.157, 0.026], 'utility': [0.061], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [-0.301], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.008, 0.003, 0.004, 0.014, 1.0, 0.126], 'utility': [0.014], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.093, 0.024, 0.015, 0.019, 0.054, 0.241], 'utility': [-0.1], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.001, 0.001, 0.0, 0.0, 0.0, 0.001], 'utility': [0.804], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.02], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.0, 0.003], 'utility': [-0.292], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.277, 0.225, 0.025, 0.012, 0.015, 0.048, 1.0], 'utility': [-0.0], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.444, 0.015, 0.019, 0.069, 1.0, 0.186, 0.03], 'utility': [0.053], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [-0.292], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.028, 0.007, 0.003, 0.003, 0.012, 1.0, 0.107], 'utility': [0.059], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '7': {'connected': [0, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.152, 0.035, 0.022, 0.032, 0.115, 0.749], 'utility': [-0.23], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.01, 0.005, 0.003, 0.003, 0.003, 0.007], 'utility': [0.367], 'ues_at_bs': [0.375, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.14, -0.194, 0.0, 0.0, 0.053, 0.019, -0.115]}} reward={'1': 0.027, '2': -4.048, '3': 0.112, '4': 3.291, '5': -4.048, '6': -0.506, '7': 2.191, '8': 3.806} t=44
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 6, '4': 7, '5': 7, '6': 0, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.018], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [0.285], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.269, 0.192, 0.023, 0.011, 0.014, 0.048, 1.0], 'utility': [-0.061], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.369, 0.013, 0.017, 0.067, 1.0, 0.133, 0.023], 'utility': [0.077], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.285], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.033, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.015], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.051, 0.015, 0.009, 0.01, 0.023, 0.077], 'utility': [-0.006], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.011], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.004, 1.0, 0.003, 0.0, 0.0, 0.001, 0.003], 'utility': [-0.301], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.273, 0.208, 0.024, 0.012, 0.014, 0.048, 1.0], 'utility': [-0.004], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.405, 0.014, 0.018, 0.067, 1.0, 0.157, 0.026], 'utility': [0.061], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [-0.301], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.03, 0.008, 0.003, 0.004, 0.014, 1.0, 0.126], 'utility': [0.014], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.093, 0.024, 0.015, 0.019, 0.054, 0.241], 'utility': [-0.1], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.001, 0.001, 0.0, 0.0, 0.0, 0.001], 'utility': [0.804], 'ues_at_bs': [0.5, 0.375, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.19, -0.202, 0.0, 0.0, 0.061, 0.001, -0.052]}} reward={'1': -0.33, '2': 5.697, '3': 3.14, '4': 4.344, '5': 5.697, '6': -0.501, '7': 3.14, '8': 5.047} t=45
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 7, '5': 7, '6': 0, '7': 3, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.012], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.005], 'utility': [0.27], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.265, 0.177, 0.022, 0.011, 0.014, 0.048, 1.0], 'utility': [0.082], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.336, 0.012, 0.016, 0.066, 1.0, 0.114, 0.021], 'utility': [0.091], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.014, 1.0, 0.042, 0.004, 0.002, 0.002, 0.008], 'utility': [0.27], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.035, 0.01, 0.004, 0.005, 0.017, 1.0, 0.174], 'utility': [-0.059], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.026, 0.01, 0.006, 0.005, 0.009, 0.025], 'utility': [0.116], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0], 'utility': [0.84], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.018], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.005, 1.0, 0.003, 0.001, 0.0, 0.001, 0.004], 'utility': [0.285], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.269, 0.192, 0.023, 0.011, 0.014, 0.048, 1.0], 'utility': [-0.061], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.369, 0.013, 0.017, 0.067, 1.0, 0.133, 0.023], 'utility': [0.077], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.037, 0.003, 0.001, 0.002, 0.007], 'utility': [0.285], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.033, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.015], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.051, 0.015, 0.009, 0.01, 0.023, 0.077], 'utility': [-0.006], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.252, 0.285, 0.0, 0.0, 0.077, -0.017, -0.034]}} reward={'1': -0.707, '2': 5.404, '3': 4.85, '4': 4.886, '5': 5.404, '6': 0.077, '7': 5.651, '8': 5.651} t=46
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 5, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.026], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.004, 0.001, 0.0, 0.001, 0.006], 'utility': [0.252], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.164, 0.021, 0.011, 0.014, 0.048, 1.0], 'utility': [0.088], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.306, 0.011, 0.015, 0.066, 1.0, 0.098, 0.019], 'utility': [0.105], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.049, 0.004, 0.002, 0.002, 0.008], 'utility': [0.252], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.061], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.007, 0.004, 0.003, 0.004, 0.01], 'utility': [0.239], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.003, 0.006, 0.009, 0.005, 0.003], 'utility': [0.323], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.012], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.006, 1.0, 0.003, 0.001, 0.0, 0.001, 0.005], 'utility': [0.27], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.265, 0.177, 0.022, 0.011, 0.014, 0.048, 1.0], 'utility': [0.082], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.336, 0.012, 0.016, 0.066, 1.0, 0.114, 0.021], 'utility': [0.091], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.014, 1.0, 0.042, 0.004, 0.002, 0.002, 0.008], 'utility': [0.27], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.035, 0.01, 0.004, 0.005, 0.017, 1.0, 0.174], 'utility': [-0.059], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.026, 0.01, 0.006, 0.005, 0.009, 0.025], 'utility': [0.116], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0], 'utility': [0.84], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.283, 0.27, 0.0, 0.0, 0.091, -0.035, 0.082]}} reward={'1': -0.873, '2': 5.043, '3': 3.372, '4': 3.438, '5': 5.043, '6': 0.007, '7': 3.773, '8': 3.773} t=47
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 5, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.024], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.004, 0.001, 0.001, 0.001, 0.008], 'utility': [0.231], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.259, 0.153, 0.02, 0.011, 0.014, 0.048, 1.0], 'utility': [0.094], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.279, 0.01, 0.014, 0.066, 1.0, 0.085, 0.017], 'utility': [0.118], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.058, 0.004, 0.002, 0.002, 0.009], 'utility': [0.231], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.064], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.013, 0.009, 0.004, 0.003, 0.003, 0.006], 'utility': [0.263], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.011, 0.03, 0.057, 0.021, 0.009], 'utility': [0.022], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.026], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.007, 1.0, 0.004, 0.001, 0.0, 0.001, 0.006], 'utility': [0.252], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.164, 0.021, 0.011, 0.014, 0.048, 1.0], 'utility': [0.088], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.306, 0.011, 0.015, 0.066, 1.0, 0.098, 0.019], 'utility': [0.105], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.049, 0.004, 0.002, 0.002, 0.008], 'utility': [0.252], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.061], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.007, 0.004, 0.003, 0.004, 0.01], 'utility': [0.239], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.002, 0.003, 0.006, 0.009, 0.005, 0.003], 'utility': [0.323], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.189, 0.252, 0.0, 0.0, 0.105, -0.044, 0.088]}} reward={'1': -0.873, '2': 4.624, '3': 2.367, '4': 2.46, '5': 4.624, '6': 0.046, '7': 2.487, '8': 2.487} t=48
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 5, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.026], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.005, 0.001, 0.001, 0.001, 0.011], 'utility': [0.208], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.256, 0.142, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.1], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.256, 0.009, 0.014, 0.067, 1.0, 0.074, 0.015], 'utility': [0.129], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 1.0, 0.069, 0.005, 0.002, 0.003, 0.01], 'utility': [0.208], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.062], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.018, 0.019, 0.009, 0.005, 0.004, 0.007], 'utility': [0.172], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.024, 0.092, 0.254, 0.057, 0.02], 'utility': [-0.19], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.024], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.008, 1.0, 0.004, 0.001, 0.001, 0.001, 0.008], 'utility': [0.231], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.259, 0.153, 0.02, 0.011, 0.014, 0.048, 1.0], 'utility': [0.094], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.279, 0.01, 0.014, 0.066, 1.0, 0.085, 0.017], 'utility': [0.118], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.017, 1.0, 0.058, 0.004, 0.002, 0.002, 0.009], 'utility': [0.231], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.064], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.013, 0.009, 0.004, 0.003, 0.003, 0.006], 'utility': [0.263], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.007, 0.011, 0.03, 0.057, 0.021, 0.009], 'utility': [0.022], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.124, 0.231, 0.0, 0.0, 0.118, -0.044, 0.094]}} reward={'1': -0.873, '2': 4.156, '3': 1.241, '4': 1.358, '5': 4.156, '6': 0.083, '7': 1.052, '8': 1.358} t=49
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 5, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.005, 0.001, 0.001, 0.002, 0.015], 'utility': [0.182], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.253, 0.133, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.105], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.235, 0.009, 0.013, 0.068, 1.0, 0.065, 0.014], 'utility': [-0.096], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.023, 1.0, 0.083, 0.006, 0.002, 0.003, 0.011], 'utility': [0.182], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.032, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.009], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.031, 0.053, 0.022, 0.009, 0.007, 0.011], 'utility': [0.024], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.042, 0.213, 0.981, 0.117, 0.034], 'utility': [-0.068], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.026], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.01, 1.0, 0.005, 0.001, 0.001, 0.001, 0.011], 'utility': [0.208], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.256, 0.142, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.1], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.256, 0.009, 0.014, 0.067, 1.0, 0.074, 0.015], 'utility': [0.129], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.02, 1.0, 0.069, 0.005, 0.002, 0.003, 0.01], 'utility': [0.208], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.037, 0.011, 0.004, 0.005, 0.017, 1.0, 0.187], 'utility': [-0.062], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.018, 0.019, 0.009, 0.005, 0.004, 0.007], 'utility': [0.172], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}, '8': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.015, 0.024, 0.092, 0.254, 0.057, 0.02], 'utility': [-0.19], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.053, 0.208, 0.0, 0.0, 0.129, -0.044, 0.1]}} reward={'1': -0.522, '2': 3.648, '3': 0.28, '4': -0.663, '5': 3.648, '6': 0.351, '7': -0.174, '8': -0.663} t=50
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 0, '4': 7, '5': 7, '6': 0, '7': 5, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.03], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.019], 'utility': [0.155], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.251, 0.124, 0.018, 0.01, 0.013, 0.05, 1.0], 'utility': [0.11], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.217, 0.008, 0.013, 0.07, 1.0, 0.058, 0.013], 'utility': [-0.011], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.101, 0.007, 0.003, 0.003, 0.012], 'utility': [0.155], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.007, 0.003, 0.004, 0.014, 1.0, 0.115], 'utility': [0.017], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.053, 0.155, 0.058, 0.018, 0.012, 0.017], 'utility': [-0.128], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.272, 0.01, 0.018, 0.111, 1.0, 0.055, 0.014], 'utility': [-0.01], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.012, 1.0, 0.005, 0.001, 0.001, 0.002, 0.015], 'utility': [0.182], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.253, 0.133, 0.019, 0.01, 0.013, 0.049, 1.0], 'utility': [0.105], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.235, 0.009, 0.013, 0.068, 1.0, 0.065, 0.014], 'utility': [-0.096], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.023, 1.0, 0.083, 0.006, 0.002, 0.003, 0.011], 'utility': [0.182], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.032, 0.009, 0.004, 0.004, 0.015, 1.0, 0.148], 'utility': [-0.009], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.031, 0.053, 0.022, 0.009, 0.007, 0.011], 'utility': [0.024], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [1.0, 0.025, 0.042, 0.213, 0.981, 0.117, 0.034], 'utility': [-0.068], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.009, 0.182, 0.0, 0.0, -0.082, -0.026, 0.105]}} reward={'1': -0.125, '2': 3.11, '3': 0.278, '4': -0.207, '5': 3.11, '6': -0.125, '7': -0.201, '8': -0.207} t=51
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 5, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.007, 0.002, 0.001, 0.003, 0.026], 'utility': [0.127], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.248, 0.116, 0.017, 0.01, 0.013, 0.05, 1.0], 'utility': [0.118], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.201, 0.008, 0.013, 0.073, 1.0, 0.052, 0.012], 'utility': [0.072], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.123, 0.008, 0.003, 0.004, 0.013], 'utility': [0.127], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.006, 0.003, 0.003, 0.012, 1.0, 0.089], 'utility': [0.068], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.085, 0.431, 0.141, 0.032, 0.019, 0.025], 'utility': [-0.205], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.069, 0.004, 0.006, 0.046, 1.0, 0.021, 0.005], 'utility': [0.051], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.03], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.015, 1.0, 0.006, 0.001, 0.001, 0.002, 0.019], 'utility': [0.155], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.251, 0.124, 0.018, 0.01, 0.013, 0.05, 1.0], 'utility': [0.11], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.217, 0.008, 0.013, 0.07, 1.0, 0.058, 0.013], 'utility': [-0.011], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.026, 1.0, 0.101, 0.007, 0.003, 0.003, 0.012], 'utility': [0.155], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.027, 0.007, 0.003, 0.004, 0.014, 1.0, 0.115], 'utility': [0.017], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.053, 0.155, 0.058, 0.018, 0.012, 0.017], 'utility': [-0.128], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}, '8': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.272, 0.01, 0.018, 0.111, 1.0, 0.055, 0.014], 'utility': [-0.01], 'ues_at_bs': [0.5, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.01, 0.155, 0.0, 0.0, -0.011, -0.006, 0.11]}} reward={'1': 0.269, '2': 2.549, '3': 0.52, '4': 0.436, '5': 2.549, '6': 0.269, '7': -0.095, '8': 1.233} t=52
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 3, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.033], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.003, 0.034], 'utility': [0.099], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.247, 0.109, 0.017, 0.01, 0.013, 0.051, 1.0], 'utility': [0.122], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.188, 0.008, 0.013, 0.076, 1.0, 0.047, 0.011], 'utility': [0.127], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.036, 1.0, 0.151, 0.009, 0.004, 0.004, 0.014], 'utility': [0.099], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.019, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.104], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.894, 0.111, 1.0, 0.286, 0.047, 0.025, 0.032], 'utility': [-0.008], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.016, 0.001, 0.002, 0.015, 1.0, 0.007, 0.001], 'utility': [0.111], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.018, 1.0, 0.007, 0.002, 0.001, 0.003, 0.026], 'utility': [0.127], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.248, 0.116, 0.017, 0.01, 0.013, 0.05, 1.0], 'utility': [0.118], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.201, 0.008, 0.013, 0.073, 1.0, 0.052, 0.012], 'utility': [0.072], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.031, 1.0, 0.123, 0.008, 0.003, 0.004, 0.013], 'utility': [0.127], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.023, 0.006, 0.003, 0.003, 0.012, 1.0, 0.089], 'utility': [0.068], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '7': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.085, 0.431, 0.141, 0.032, 0.019, 0.025], 'utility': [-0.205], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.069, 0.004, 0.006, 0.046, 1.0, 0.021, 0.005], 'utility': [0.051], 'ues_at_bs': [0.375, 0.25, 0.0, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [-0.005, 0.127, 0.0, 0.0, 0.062, 0.013, 0.118]}} reward={'1': 0.707, '2': 1.973, '3': 1.814, '4': 1.911, '5': 1.259, '6': 0.707, '7': 1.16, '8': 2.373} t=53
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 4, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.041], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.01, 0.002, 0.002, 0.004, 0.045], 'utility': [0.069], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.103, 0.016, 0.009, 0.013, 0.052, 1.0], 'utility': [0.126], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.177, 0.007, 0.013, 0.081, 1.0, 0.043, 0.01], 'utility': [0.152], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.042, 1.0, 0.186, 0.011, 0.004, 0.005, 0.016], 'utility': [0.069], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.016, 0.004, 0.002, 0.002, 0.009, 1.0, 0.052], 'utility': [0.157], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.376, 0.064, 1.0, 0.252, 0.03, 0.014, 0.018], 'utility': [0.04], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.004, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.139], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.033], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.021, 1.0, 0.008, 0.002, 0.002, 0.003, 0.034], 'utility': [0.099], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.247, 0.109, 0.017, 0.01, 0.013, 0.051, 1.0], 'utility': [0.122], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.188, 0.008, 0.013, 0.076, 1.0, 0.047, 0.011], 'utility': [0.127], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.036, 1.0, 0.151, 0.009, 0.004, 0.004, 0.014], 'utility': [0.099], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.019, 0.005, 0.002, 0.003, 0.01, 1.0, 0.068], 'utility': [0.104], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.894, 0.111, 1.0, 0.286, 0.047, 0.025, 0.032], 'utility': [-0.008], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.016, 0.001, 0.002, 0.015, 1.0, 0.007, 0.001], 'utility': [0.111], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.08, 0.099, -0.008, 0.0, 0.119, 0.035, 0.122]}} reward={'1': 1.153, '2': 1.387, '3': 2.221, '4': 2.44, '5': 1.191, '6': 1.153, '7': 1.791, '8': 2.916} t=54
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 4, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.011, 0.003, 0.002, 0.005, 0.06], 'utility': [0.04], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.244, 0.097, 0.016, 0.009, 0.013, 0.053, 1.0], 'utility': [0.137], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.167, 0.007, 0.013, 0.086, 1.0, 0.04, 0.01], 'utility': [0.163], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.04], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.013, 0.003, 0.001, 0.002, 0.007, 1.0, 0.039], 'utility': [0.201], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.179, 0.039, 1.0, 0.23, 0.021, 0.009, 0.011], 'utility': [0.124], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.145], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.041], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.01, 0.002, 0.002, 0.004, 0.045], 'utility': [0.069], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.245, 0.103, 0.016, 0.009, 0.013, 0.052, 1.0], 'utility': [0.126], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.177, 0.007, 0.013, 0.081, 1.0, 0.043, 0.01], 'utility': [0.152], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.042, 1.0, 0.186, 0.011, 0.004, 0.005, 0.016], 'utility': [0.069], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.016, 0.004, 0.002, 0.002, 0.009, 1.0, 0.052], 'utility': [0.157], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '7': {'connected': [1, 0, 1, 0, 0, 0, 0], 'dr': [0.376, 0.064, 1.0, 0.252, 0.03, 0.014, 0.018], 'utility': [0.04], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.004, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.139], 'ues_at_bs': [0.375, 0.25, 0.125, 0.0, 0.25, 0.25, 0.125], 'util_at_bs': [0.106, 0.069, 0.04, 0.0, 0.146, 0.058, 0.126]}} reward={'1': 1.644, '2': 0.798, '3': 2.918, '4': 3.044, '5': 1.359, '6': 1.644, '7': 2.481, '8': 3.083} t=55
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.079], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.243, 0.092, 0.015, 0.009, 0.013, 0.054, 1.0], 'utility': [0.14], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.159, 0.007, 0.013, 0.093, 1.0, 0.037, 0.01], 'utility': [0.16], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.01, 0.002, 0.001, 0.001, 0.006, 1.0, 0.028], 'utility': [0.258], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.101, 0.027, 1.0, 0.226, 0.016, 0.007, 0.008], 'utility': [0.162], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.143], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.03, 1.0, 0.011, 0.003, 0.002, 0.005, 0.06], 'utility': [0.04], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.244, 0.097, 0.016, 0.009, 0.013, 0.053, 1.0], 'utility': [0.137], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.167, 0.007, 0.013, 0.086, 1.0, 0.04, 0.01], 'utility': [0.163], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.04], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.013, 0.003, 0.001, 0.002, 0.007, 1.0, 0.039], 'utility': [0.201], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.179, 0.039, 1.0, 0.23, 0.021, 0.009, 0.011], 'utility': [0.124], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.145], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.04, 0.124, 0.124, 0.154, 0.082, 0.137]}} reward={'1': 2.155, '2': 1.297, '3': 2.935, '4': 3.015, '5': 1.444, '6': 2.155, '7': 3.24, '8': 3.028} t=56
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.014, 0.004, 0.003, 0.007, 0.103], 'utility': [0.014], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.087, 0.015, 0.009, 0.013, 0.056, 1.0], 'utility': [0.142], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.153, 0.007, 0.013, 0.102, 1.0, 0.035, 0.009], 'utility': [0.157], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.014], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.002, 0.001, 0.001, 0.005, 1.0, 0.021], 'utility': [0.311], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.07, 0.022, 1.0, 0.247, 0.014, 0.006, 0.006], 'utility': [0.168], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.14], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.035, 1.0, 0.012, 0.003, 0.003, 0.006, 0.079], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.243, 0.092, 0.015, 0.009, 0.013, 0.054, 1.0], 'utility': [0.14], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.159, 0.007, 0.013, 0.093, 1.0, 0.037, 0.01], 'utility': [0.16], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.01, 0.002, 0.001, 0.001, 0.006, 1.0, 0.028], 'utility': [0.258], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.101, 0.027, 1.0, 0.226, 0.016, 0.007, 0.008], 'utility': [0.162], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.143], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.027, 0.162, 0.162, 0.151, 0.108, 0.14]}} reward={'1': 2.716, '2': 1.133, '3': 2.946, '4': 2.986, '5': 1.304, '6': 2.716, '7': 3.362, '8': 2.977} t=57
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.044], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.048, 1.0, 0.016, 0.005, 0.004, 0.009, 0.134], 'utility': [-0.001], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.083, 0.015, 0.009, 0.013, 0.057, 1.0], 'utility': [0.144], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.149, 0.007, 0.014, 0.113, 1.0, 0.034, 0.009], 'utility': [0.153], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [-0.001], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.015], 'utility': [0.375], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.059, 0.021, 1.0, 0.297, 0.014, 0.006, 0.006], 'utility': [0.142], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.136], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.041, 1.0, 0.014, 0.004, 0.003, 0.007, 0.103], 'utility': [0.014], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.087, 0.015, 0.009, 0.013, 0.056, 1.0], 'utility': [0.142], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.153, 0.007, 0.013, 0.102, 1.0, 0.035, 0.009], 'utility': [0.157], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [0.014], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.008, 0.002, 0.001, 0.001, 0.005, 1.0, 0.021], 'utility': [0.311], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.07, 0.022, 1.0, 0.247, 0.014, 0.006, 0.006], 'utility': [0.168], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.14], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.15, 0.014, 0.168, 0.168, 0.149, 0.136, 0.142]}} reward={'1': 3.311, '2': 0.951, '3': 2.941, '4': 2.928, '5': 0.937, '6': 3.311, '7': 2.842, '8': 2.888} t=58
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.055, 1.0, 0.018, 0.005, 0.005, 0.011, 0.173], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.079, 0.014, 0.009, 0.013, 0.059, 1.0], 'utility': [0.146], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.145, 0.007, 0.014, 0.126, 1.0, 0.032, 0.009], 'utility': [0.142], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.056, 1.0, 0.265, 0.014, 0.005, 0.006, 0.019], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.01], 'utility': [0.44], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.058, 0.023, 1.0, 0.376, 0.017, 0.007, 0.007], 'utility': [0.093], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.003, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.125], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.044], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.048, 1.0, 0.016, 0.005, 0.004, 0.009, 0.134], 'utility': [-0.001], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.083, 0.015, 0.009, 0.013, 0.057, 1.0], 'utility': [0.144], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.149, 0.007, 0.014, 0.113, 1.0, 0.034, 0.009], 'utility': [0.153], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.049, 1.0, 0.231, 0.013, 0.005, 0.005, 0.018], 'utility': [-0.001], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.004, 1.0, 0.015], 'utility': [0.375], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.059, 0.021, 1.0, 0.297, 0.014, 0.006, 0.006], 'utility': [0.142], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.002, 0.0, 0.0, 0.003, 1.0, 0.001, 0.0], 'utility': [0.136], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.148, -0.001, 0.142, 0.142, 0.144, 0.166, 0.144]}} reward={'1': 3.968, '2': 0.656, '3': 2.887, '4': 2.772, '5': 0.301, '6': 3.968, '7': 1.85, '8': 2.67} t=59
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.02, 0.006, 0.005, 0.013, 0.223], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.076, 0.014, 0.009, 0.014, 0.061, 1.0], 'utility': [0.147], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.143, 0.007, 0.015, 0.142, 1.0, 0.032, 0.009], 'utility': [0.125], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.306, 0.016, 0.006, 0.006, 0.02], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.515], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.063, 0.028, 1.0, 0.476, 0.022, 0.008, 0.009], 'utility': [0.03], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.006, 0.001, 0.001, 0.011, 1.0, 0.003, 0.001], 'utility': [0.108], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.043], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.055, 1.0, 0.018, 0.005, 0.005, 0.011, 0.173], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.079, 0.014, 0.009, 0.013, 0.059, 1.0], 'utility': [0.146], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.145, 0.007, 0.014, 0.126, 1.0, 0.032, 0.009], 'utility': [0.142], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.056, 1.0, 0.265, 0.014, 0.005, 0.006, 0.019], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.0, 0.001, 0.003, 1.0, 0.01], 'utility': [0.44], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.058, 0.023, 1.0, 0.376, 0.017, 0.007, 0.007], 'utility': [0.093], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.003, 0.0, 0.001, 0.005, 1.0, 0.002, 0.0], 'utility': [0.125], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.144, -0.024, 0.093, 0.093, 0.133, 0.198, 0.146]}} reward={'1': 4.677, '2': 0.348, '3': 2.788, '4': 2.135, '5': -0.432, '6': 4.677, '7': 0.594, '8': 2.326} t=60
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 6, '3': 0, '4': 2, '5': 7, '6': 0, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.071, 1.0, 0.022, 0.007, 0.006, 0.015, 0.286], 'utility': [-0.071], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.073, 0.014, 0.009, 0.014, 0.063, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.141, 0.008, 0.016, 0.162, 1.0, 0.031, 0.009], 'utility': [0.083], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.355, 0.018, 0.007, 0.007, 0.022], 'utility': [-0.071], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.002, 1.0, 0.004], 'utility': [0.594], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.036], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.012, 0.001, 0.002, 0.022, 1.0, 0.005, 0.001], 'utility': [0.083], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.02, 0.006, 0.005, 0.013, 0.223], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.241, 0.076, 0.014, 0.009, 0.014, 0.061, 1.0], 'utility': [0.147], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '4': {'connected': [1, 0, 0, 0, 1, 0, 0], 'dr': [0.143, 0.007, 0.015, 0.142, 1.0, 0.032, 0.009], 'utility': [0.125], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.063, 1.0, 0.306, 0.016, 0.006, 0.006, 0.02], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.0, 0.002, 1.0, 0.007], 'utility': [0.515], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.063, 0.028, 1.0, 0.476, 0.022, 0.008, 0.009], 'utility': [0.03], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.006, 0.001, 0.001, 0.011, 1.0, 0.003, 0.001], 'utility': [0.108], 'ues_at_bs': [0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.136, -0.047, 0.03, 0.03, 0.116, 0.234, 0.147]}} reward={'1': 5.467, '2': 0.18, '3': 3.391, '4': 0.872, '5': -1.188, '6': 5.467, '7': -0.712, '8': 1.664} t=61
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 4, '5': 3, '6': 7, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.052], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.08, 1.0, 0.024, 0.008, 0.007, 0.018, 0.365], 'utility': [-0.096], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.017, 0.186, 1.0, 0.031, 0.009], 'utility': [0.076], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.083, 1.0, 0.413, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.003], 'utility': [0.686], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.141], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.023, 0.002, 0.004, 0.044, 1.0, 0.009, 0.002], 'utility': [0.051], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.071, 1.0, 0.022, 0.007, 0.006, 0.015, 0.286], 'utility': [-0.071], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.073, 0.014, 0.009, 0.014, 0.063, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.141, 0.008, 0.016, 0.162, 1.0, 0.031, 0.009], 'utility': [0.083], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '5': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.073, 1.0, 0.355, 0.018, 0.007, 0.007, 0.022], 'utility': [-0.071], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.002, 1.0, 0.004], 'utility': [0.594], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.036], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.012, 0.001, 0.002, 0.022, 1.0, 0.005, 0.001], 'utility': [0.083], 'ues_at_bs': [0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.071, -0.036, -0.036, 0.083, 0.273, 0.17]}} reward={'1': 6.341, '2': 0.193, '3': 3.395, '4': 0.313, '5': -1.636, '6': 6.341, '7': -1.256, '8': 1.275} t=62
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 6, '5': 7, '6': 7, '7': 6, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.09, 1.0, 0.026, 0.009, 0.008, 0.021, 0.465], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.018, 0.216, 1.0, 0.031, 0.009], 'utility': [0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.097, 1.0, 0.482, 0.023, 0.008, 0.009, 0.026], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.002], 'utility': [0.788], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.16], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.042, 0.003, 0.007, 0.086, 1.0, 0.014, 0.004], 'utility': [0.012], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.052], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.08, 1.0, 0.024, 0.008, 0.007, 0.018, 0.365], 'utility': [-0.096], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.017, 0.186, 1.0, 0.031, 0.009], 'utility': [0.076], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.083, 1.0, 0.413, 0.02, 0.007, 0.008, 0.024], 'utility': [-0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.003], 'utility': [0.686], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.141], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.023, 0.002, 0.004, 0.044, 1.0, 0.009, 0.002], 'utility': [0.051], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.07, -0.093, -0.032, 0.064, 0.317, 0.17]}} reward={'1': 7.331, '2': 0.012, '3': 3.395, '4': -0.287, '5': -1.878, '6': 7.331, '7': -1.612, '8': -0.287} t=63
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 6, '3': 0, '4': 6, '5': 7, '6': 7, '7': 6, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.061], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.1, 1.0, 0.029, 0.01, 0.009, 0.025, 0.59], 'utility': [-0.144], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.142, 0.009, 0.019, 0.251, 1.0, 0.031, 0.01], 'utility': [0.011], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.112, 1.0, 0.563, 0.026, 0.009, 0.01, 0.029], 'utility': [-0.079], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.0, 1.0, 0.001], 'utility': [0.906], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.025, 1.0, 0.346, 0.018, 0.007, 0.008], 'utility': [-0.057], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.075, 0.005, 0.012, 0.162, 1.0, 0.021, 0.006], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.055], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.09, 1.0, 0.026, 0.009, 0.008, 0.021, 0.465], 'utility': [-0.12], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.008, 0.018, 0.216, 1.0, 0.031, 0.009], 'utility': [0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.097, 1.0, 0.482, 0.023, 0.008, 0.009, 0.026], 'utility': [-0.048], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.002], 'utility': [0.788], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.072, 0.034, 1.0, 0.58, 0.028, 0.01, 0.011], 'utility': [-0.16], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.042, 0.003, 0.007, 0.086, 1.0, 0.014, 0.004], 'utility': [0.012], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.084, -0.104, -0.057, 0.029, 0.367, 0.17]}} reward={'1': 8.454, '2': -0.357, '3': 3.395, '4': -0.331, '5': -1.795, '6': 8.454, '7': -0.908, '8': -0.331} t=64
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 5, '3': 0, '4': 6, '5': 7, '6': 7, '7': 6, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.111, 1.0, 0.031, 0.011, 0.011, 0.029, 0.745], 'utility': [-0.168], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.252, 0.076, 0.014, 0.009, 0.014, 0.064, 1.0], 'utility': [0.166], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.144, 0.009, 0.021, 0.295, 1.0, 0.032, 0.01], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.13, 1.0, 0.658, 0.03, 0.011, 0.011, 0.032], 'utility': [-0.092], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.036, 0.017, 1.0, 0.183, 0.01, 0.004, 0.005], 'utility': [0.034], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.129, 0.008, 0.02, 0.295, 1.0, 0.03, 0.009], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.061], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.1, 1.0, 0.029, 0.01, 0.009, 0.025, 0.59], 'utility': [-0.144], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.242, 0.071, 0.014, 0.009, 0.014, 0.065, 1.0], 'utility': [0.17], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.142, 0.009, 0.019, 0.251, 1.0, 0.031, 0.01], 'utility': [0.011], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.112, 1.0, 0.563, 0.026, 0.009, 0.01, 0.029], 'utility': [-0.079], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.0, 1.0, 0.001], 'utility': [0.906], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.053, 0.025, 1.0, 0.346, 0.018, 0.007, 0.008], 'utility': [-0.057], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}, '8': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.075, 0.005, 0.012, 0.162, 1.0, 0.021, 0.006], 'utility': [-0.031], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.17, -0.112, -0.068, -0.023, -0.01, 0.423, 0.17]}} reward={'1': 9.34, '2': -0.63, '3': 3.314, '4': -0.491, '5': -1.589, '6': 9.34, '7': -0.407, '8': -0.491} t=65
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 5, '3': 0, '4': 6, '5': 7, '6': 7, '7': 1, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.075], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.122, 1.0, 0.034, 0.012, 0.012, 0.034, 0.939], 'utility': [-0.192], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.081, 0.015, 0.01, 0.014, 0.064, 1.0], 'utility': [0.161], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.147, 0.01, 0.023, 0.348, 1.0, 0.032, 0.01], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.152, 1.0, 0.769, 0.034, 0.012, 0.012, 0.035], 'utility': [-0.109], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.011, 1.0, 0.086, 0.006, 0.002, 0.003], 'utility': [0.161], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.213, 0.013, 0.032, 0.518, 1.0, 0.041, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.111, 1.0, 0.031, 0.011, 0.011, 0.029, 0.745], 'utility': [-0.168], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.252, 0.076, 0.014, 0.009, 0.014, 0.064, 1.0], 'utility': [0.166], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.144, 0.009, 0.021, 0.295, 1.0, 0.032, 0.01], 'utility': [-0.04], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.13, 1.0, 0.658, 0.03, 0.011, 0.011, 0.032], 'utility': [-0.092], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.036, 0.017, 1.0, 0.183, 0.01, 0.004, 0.005], 'utility': [0.034], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.129, 0.008, 0.02, 0.295, 1.0, 0.03, 0.009], 'utility': [-0.039], 'ues_at_bs': [0.125, 0.25, 0.25, 0.375, 0.25, 0.25, 0.125], 'util_at_bs': [0.166, -0.13, -0.029, -0.015, -0.039, 0.467, 0.166]}} reward={'1': 9.249, '2': -0.93, '3': 3.228, '4': -0.992, '5': -1.242, '6': 9.249, '7': 0.525, '8': -0.992} t=66
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 5, '3': 0, '4': 6, '5': 7, '6': 7, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.084], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.113, 0.848, 0.031, 0.011, 0.012, 0.033, 1.0], 'utility': [-0.216], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.273, 0.087, 0.016, 0.01, 0.015, 0.063, 1.0], 'utility': [0.157], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.15, 0.01, 0.025, 0.412, 1.0, 0.033, 0.011], 'utility': [-0.082], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.178, 1.0, 0.898, 0.039, 0.014, 0.013, 0.038], 'utility': [-0.115], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.007, 1.0, 0.036, 0.003, 0.001, 0.002], 'utility': [0.313], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.34, 0.02, 0.051, 0.881, 1.0, 0.054, 0.02], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.075], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.122, 1.0, 0.034, 0.012, 0.012, 0.034, 0.939], 'utility': [-0.192], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.262, 0.081, 0.015, 0.01, 0.014, 0.064, 1.0], 'utility': [0.161], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.147, 0.01, 0.023, 0.348, 1.0, 0.032, 0.01], 'utility': [-0.054], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.152, 1.0, 0.769, 0.034, 0.012, 0.012, 0.035], 'utility': [-0.109], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.023, 0.011, 1.0, 0.086, 0.006, 0.002, 0.003], 'utility': [0.161], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.213, 0.013, 0.032, 0.518, 1.0, 0.041, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.161, -0.15, 0.026, -0.05, -0.05, 0.462, 0.161]}} reward={'1': 9.159, '2': -1.162, '3': 3.137, '4': -1.418, '5': -0.668, '6': 9.159, '7': 1.974, '8': -1.418} t=67
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 5, '3': 0, '4': 6, '5': 7, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.089], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.098, 0.677, 0.027, 0.01, 0.01, 0.03, 1.0], 'utility': [-0.239], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.285, 0.093, 0.017, 0.01, 0.015, 0.063, 1.0], 'utility': [0.152], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.153, 0.011, 0.027, 0.491, 1.0, 0.034, 0.011], 'utility': [-0.103], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.199, 0.955, 1.0, 0.043, 0.015, 0.014, 0.04], 'utility': [-0.121], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.008, 0.004, 1.0, 0.014, 0.001, 0.001, 0.001], 'utility': [0.472], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.363, 0.02, 0.055, 1.0, 0.689, 0.048, 0.019], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.084], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.113, 0.848, 0.031, 0.011, 0.012, 0.033, 1.0], 'utility': [-0.216], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.273, 0.087, 0.016, 0.01, 0.015, 0.063, 1.0], 'utility': [0.157], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.15, 0.01, 0.025, 0.412, 1.0, 0.033, 0.011], 'utility': [-0.082], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.178, 1.0, 0.898, 0.039, 0.014, 0.013, 0.038], 'utility': [-0.115], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.007, 1.0, 0.036, 0.003, 0.001, 0.002], 'utility': [0.313], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.34, 0.02, 0.051, 0.881, 1.0, 0.054, 0.02], 'utility': [-0.06], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.157, -0.166, 0.099, -0.071, -0.071, 0.458, 0.157]}} reward={'1': 9.108, '2': -1.389, '3': 3.041, '4': -1.698, '5': -0.046, '6': 9.108, '7': 3.513, '8': -0.75} t=68
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 5, '3': 0, '4': 6, '5': 7, '6': 7, '7': 4, '8': 1} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.085, 0.542, 0.023, 0.009, 0.009, 0.027, 1.0], 'utility': [-0.262], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.297, 0.101, 0.018, 0.011, 0.015, 0.063, 1.0], 'utility': [0.121], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.157, 0.012, 0.03, 0.586, 1.0, 0.035, 0.012], 'utility': [-0.12], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.201, 0.822, 1.0, 0.043, 0.014, 0.014, 0.038], 'utility': [-0.111], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.007, 0.001, 0.0, 0.001], 'utility': [0.581], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '8': {'connected': [1, 0, 0, 1, 1, 0, 0], 'dr': [0.343, 0.018, 0.053, 1.0, 0.433, 0.038, 0.016], 'utility': [-0.022], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.089], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.098, 0.677, 0.027, 0.01, 0.01, 0.03, 1.0], 'utility': [-0.239], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.285, 0.093, 0.017, 0.01, 0.015, 0.063, 1.0], 'utility': [0.152], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.153, 0.011, 0.027, 0.491, 1.0, 0.034, 0.011], 'utility': [-0.103], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.199, 0.955, 1.0, 0.043, 0.015, 0.014, 0.04], 'utility': [-0.121], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.008, 0.004, 1.0, 0.014, 0.001, 0.001, 0.001], 'utility': [0.472], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}, '8': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.363, 0.02, 0.055, 1.0, 0.689, 0.048, 0.019], 'utility': [-0.066], 'ues_at_bs': [0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.152, -0.18, 0.176, -0.085, -0.085, 0.455, 0.152]}} reward={'1': 9.399, '2': -1.685, '3': 1.46, '4': -1.418, '5': 0.482, '6': 9.399, '7': 4.697, '8': -0.617} t=69
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 0, '4': 6, '5': 7, '6': 7, '7': 4, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.074, 0.436, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.285], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.31, 0.109, 0.019, 0.011, 0.016, 0.063, 1.0], 'utility': [0.114], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.162, 0.012, 0.032, 0.701, 1.0, 0.036, 0.013], 'utility': [-0.13], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.204, 0.71, 1.0, 0.043, 0.014, 0.013, 0.036], 'utility': [-0.08], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.006, 0.004, 1.0, 0.005, 0.001, 0.0, 0.001], 'utility': [0.55], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '8': {'connected': [1, 0, 0, 1, 1, 0, 0], 'dr': [0.327, 0.017, 0.052, 1.0, 0.283, 0.03, 0.014], 'utility': [-0.011], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.085, 0.542, 0.023, 0.009, 0.009, 0.027, 1.0], 'utility': [-0.262], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.297, 0.101, 0.018, 0.011, 0.015, 0.063, 1.0], 'utility': [0.121], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.157, 0.012, 0.03, 0.586, 1.0, 0.035, 0.012], 'utility': [-0.12], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.201, 0.822, 1.0, 0.043, 0.014, 0.014, 0.038], 'utility': [-0.111], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.007, 0.001, 0.0, 0.001], 'utility': [0.581], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}, '8': {'connected': [1, 0, 0, 1, 1, 0, 0], 'dr': [0.343, 0.018, 0.053, 1.0, 0.433, 0.038, 0.016], 'utility': [-0.022], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.049, -0.187, 0.235, -0.071, -0.071, 0.47, 0.121]}} reward={'1': 10.083, '2': -1.672, '3': 1.453, '4': -1.406, '5': 0.521, '6': 10.083, '7': 4.693, '8': -0.592} t=70
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 7, '3': 0, '4': 6, '5': 7, '6': 7, '7': 4, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.323, 0.117, 0.02, 0.011, 0.016, 0.063, 1.0], 'utility': [-0.014], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.166, 0.013, 0.036, 0.839, 1.0, 0.037, 0.013], 'utility': [0.037], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.208, 0.615, 1.0, 0.043, 0.014, 0.013, 0.034], 'utility': [-0.054], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.008, 1.0, 0.007, 0.001, 0.001, 0.001], 'utility': [0.399], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.315, 0.016, 0.053, 1.0, 0.194, 0.025, 0.013], 'utility': [-0.043], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.074, 0.436, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.285], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.31, 0.109, 0.019, 0.011, 0.016, 0.063, 1.0], 'utility': [0.114], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.162, 0.012, 0.032, 0.701, 1.0, 0.036, 0.013], 'utility': [-0.13], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.204, 0.71, 1.0, 0.043, 0.014, 0.013, 0.036], 'utility': [-0.08], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.006, 0.004, 1.0, 0.005, 0.001, 0.0, 0.001], 'utility': [0.55], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}, '8': {'connected': [1, 0, 0, 1, 1, 0, 0], 'dr': [0.327, 0.017, 0.052, 1.0, 0.283, 0.03, 0.014], 'utility': [-0.011], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125], 'util_at_bs': [0.052, -0.183, 0.235, -0.07, -0.07, 0.504, 0.114]}} reward={'1': 10.274, '2': -0.809, '3': -0.59, '4': 0.213, '5': 1.221, '6': 10.274, '7': 3.449, '8': -0.312} t=71
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 0, '4': 7, '5': 7, '6': 7, '7': 4, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.338, 0.127, 0.021, 0.012, 0.017, 0.063, 1.0], 'utility': [-0.02], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.17, 0.014, 0.039, 1.0, 0.993, 0.039, 0.014], 'utility': [0.03], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.213, 0.536, 1.0, 0.043, 0.014, 0.013, 0.033], 'utility': [-0.046], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.023, 1.0, 0.012, 0.002, 0.002, 0.003], 'utility': [0.231], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.31, 0.015, 0.057, 1.0, 0.139, 0.021, 0.012], 'utility': [-0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.323, 0.117, 0.02, 0.011, 0.016, 0.063, 1.0], 'utility': [-0.014], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.166, 0.013, 0.036, 0.839, 1.0, 0.037, 0.013], 'utility': [0.037], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.208, 0.615, 1.0, 0.043, 0.014, 0.013, 0.034], 'utility': [-0.054], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.008, 1.0, 0.007, 0.001, 0.001, 0.001], 'utility': [0.399], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.315, 0.016, 0.053, 1.0, 0.194, 0.025, 0.013], 'utility': [-0.043], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.028, -0.05, 0.172, -0.003, 0.037, 0.514, -0.031]}} reward={'1': 10.271, '2': -0.824, '3': -0.552, '4': 0.263, '5': 0.448, '6': 10.271, '7': 1.85, '8': -0.16} t=72
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 2, '4': 7, '5': 7, '6': 7, '7': 4, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.019], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.052], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.353, 0.138, 0.022, 0.012, 0.017, 0.063, 1.0], 'utility': [-0.026], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.146, 0.013, 0.035, 1.0, 0.828, 0.034, 0.012], 'utility': [0.025], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.219, 0.47, 1.0, 0.043, 0.014, 0.012, 0.031], 'utility': [-0.043], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.064, 0.069, 1.0, 0.02, 0.005, 0.004, 0.007], 'utility': [0.074], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.312, 0.016, 0.064, 1.0, 0.106, 0.018, 0.011], 'utility': [-0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.027], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.338, 0.127, 0.021, 0.012, 0.017, 0.063, 1.0], 'utility': [-0.02], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.17, 0.014, 0.039, 1.0, 0.993, 0.039, 0.014], 'utility': [0.03], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.213, 0.536, 1.0, 0.043, 0.014, 0.013, 0.033], 'utility': [-0.046], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.028, 0.023, 1.0, 0.012, 0.002, 0.002, 0.003], 'utility': [0.231], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.31, 0.015, 0.057, 1.0, 0.139, 0.021, 0.012], 'utility': [-0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.021, -0.048, 0.092, 0.005, 0.03, 0.514, -0.035]}} reward={'1': 10.194, '2': -0.866, '3': -0.558, '4': 0.278, '5': -0.321, '6': 10.194, '7': 0.312, '8': -0.084} t=73
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 2, '4': 7, '5': 7, '6': 7, '7': 7, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.013], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.075, 0.404, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.046], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.368, 0.15, 0.023, 0.013, 0.017, 0.064, 1.0], 'utility': [-0.031], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.032, 1.0, 0.69, 0.029, 0.011], 'utility': [0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.227, 0.414, 1.0, 0.044, 0.014, 0.012, 0.03], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [0.942], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.132, 0.196, 1.0, 0.032, 0.009, 0.007, 0.017], 'utility': [-0.061], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.322, 0.017, 0.076, 1.0, 0.086, 0.017, 0.011], 'utility': [-0.004], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.019], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.071, 0.411, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.052], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.353, 0.138, 0.022, 0.012, 0.017, 0.063, 1.0], 'utility': [-0.026], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.146, 0.013, 0.035, 1.0, 0.828, 0.034, 0.012], 'utility': [0.025], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.219, 0.47, 1.0, 0.043, 0.014, 0.012, 0.031], 'utility': [-0.043], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.064, 0.069, 1.0, 0.02, 0.005, 0.004, 0.007], 'utility': [0.074], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.312, 0.016, 0.064, 1.0, 0.106, 0.018, 0.011], 'utility': [-0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.017, -0.048, 0.016, 0.008, 0.025, 0.51, -0.039]}} reward={'1': 9.55, '2': -0.826, '3': -0.563, '4': 0.252, '5': -0.957, '6': 9.55, '7': -0.957, '8': -0.093} t=74
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 2, '4': 7, '5': 7, '6': 7, '7': 7, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 0.4, 0.019, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.041], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.384, 0.163, 0.025, 0.014, 0.018, 0.064, 1.0], 'utility': [-0.037], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.109, 0.01, 0.03, 1.0, 0.576, 0.025, 0.01], 'utility': [0.019], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.236, 0.367, 1.0, 0.045, 0.014, 0.012, 0.029], 'utility': [-0.043], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.821], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.242, 0.537, 1.0, 0.046, 0.015, 0.014, 0.035], 'utility': [-0.179], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.34, 0.019, 0.097, 1.0, 0.074, 0.017, 0.012], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.013], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.075, 0.404, 0.019, 0.007, 0.008, 0.024, 1.0], 'utility': [-0.046], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.368, 0.15, 0.023, 0.013, 0.017, 0.064, 1.0], 'utility': [-0.031], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.032, 1.0, 0.69, 0.029, 0.011], 'utility': [0.021], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.227, 0.414, 1.0, 0.044, 0.014, 0.012, 0.03], 'utility': [-0.042], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [0.942], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.132, 0.196, 1.0, 0.032, 0.009, 0.007, 0.017], 'utility': [-0.061], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.322, 0.017, 0.076, 1.0, 0.086, 0.017, 0.011], 'utility': [-0.004], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.018, -0.044, -0.052, 0.008, 0.021, 0.478, -0.039]}} reward={'1': 8.281, '2': -0.813, '3': -0.628, '4': 0.187, '5': -1.177, '6': 8.281, '7': -1.531, '8': -0.188} t=75
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 2, '4': 7, '5': 7, '6': 7, '7': 2, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.004], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.087, 0.398, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.051], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.401, 0.177, 0.026, 0.014, 0.019, 0.065, 1.0], 'utility': [-0.044], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.094, 0.009, 0.027, 1.0, 0.482, 0.022, 0.009], 'utility': [0.018], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.248, 0.328, 1.0, 0.047, 0.014, 0.012, 0.028], 'utility': [-0.031], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.714], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.269, 1.0, 0.682, 0.043, 0.016, 0.016, 0.046], 'utility': [-0.202], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.368, 0.023, 0.13, 1.0, 0.067, 0.017, 0.013], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.08, 0.4, 0.019, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.041], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.384, 0.163, 0.025, 0.014, 0.018, 0.064, 1.0], 'utility': [-0.037], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.109, 0.01, 0.03, 1.0, 0.576, 0.025, 0.01], 'utility': [0.019], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.236, 0.367, 1.0, 0.045, 0.014, 0.012, 0.029], 'utility': [-0.043], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.821], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.242, 0.537, 1.0, 0.046, 0.015, 0.014, 0.035], 'utility': [-0.179], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.34, 0.019, 0.097, 1.0, 0.074, 0.017, 0.012], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.023, -0.042, -0.111, 0.005, 0.019, 0.414, -0.039]}} reward={'1': 7.178, '2': -1.515, '3': -0.808, '4': 0.084, '5': -1.671, '6': 7.178, '7': -2.071, '8': -0.363} t=76
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 1, '3': 0, '4': 7, '5': 7, '6': 7, '7': 7, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.0], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.097, 0.399, 0.02, 0.008, 0.009, 0.026, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.419, 0.193, 0.028, 0.015, 0.019, 0.065, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.081, 0.008, 0.025, 1.0, 0.404, 0.019, 0.008], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.262, 0.296, 1.0, 0.049, 0.014, 0.012, 0.028], 'utility': [-0.029], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.003, 1.0, 0.001], 'utility': [0.621], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.142, 1.0, 0.244, 0.02, 0.008, 0.009, 0.031], 'utility': [-0.243], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.403, 0.028, 0.184, 1.0, 0.064, 0.018, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.004], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.087, 0.398, 0.02, 0.008, 0.008, 0.025, 1.0], 'utility': [-0.051], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.401, 0.177, 0.026, 0.014, 0.019, 0.065, 1.0], 'utility': [-0.044], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.094, 0.009, 0.027, 1.0, 0.482, 0.022, 0.009], 'utility': [0.018], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.248, 0.328, 1.0, 0.047, 0.014, 0.012, 0.028], 'utility': [-0.031], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.714], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.269, 1.0, 0.682, 0.043, 0.016, 0.016, 0.046], 'utility': [-0.202], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.368, 0.023, 0.13, 1.0, 0.067, 0.017, 0.013], 'utility': [-0.024], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.034, -0.095, -0.117, -0.003, 0.018, 0.359, -0.047]}} reward={'1': 6.211, '2': -1.661, '3': -0.957, '4': -0.048, '5': -1.957, '6': 6.211, '7': -2.36, '8': -0.605} t=77
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 1, '3': 0, '4': 7, '5': 7, '6': 7, '7': 7, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.002], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.11, 0.403, 0.021, 0.009, 0.009, 0.028, 1.0], 'utility': [-0.048], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.437, 0.211, 0.03, 0.016, 0.02, 0.066, 1.0], 'utility': [-0.056], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.278, 0.268, 1.0, 0.051, 0.015, 0.012, 0.027], 'utility': [0.065], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.537], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.082, 0.008, 0.004, 0.005, 0.018], 'utility': [-0.371], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.444, 0.036, 0.273, 1.0, 0.064, 0.019, 0.017], 'utility': [-0.072], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.0], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.097, 0.399, 0.02, 0.008, 0.009, 0.026, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.419, 0.193, 0.028, 0.015, 0.019, 0.065, 1.0], 'utility': [-0.05], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.081, 0.008, 0.025, 1.0, 0.404, 0.019, 0.008], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.262, 0.296, 1.0, 0.049, 0.014, 0.012, 0.028], 'utility': [-0.029], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.003, 1.0, 0.001], 'utility': [0.621], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.142, 1.0, 0.244, 0.02, 0.008, 0.009, 0.031], 'utility': [-0.243], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.403, 0.028, 0.184, 1.0, 0.064, 0.018, 0.014], 'utility': [-0.045], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.047, -0.106, -0.136, -0.013, 0.019, 0.311, -0.048]}} reward={'1': 5.349, '2': -1.826, '3': -1.161, '4': -0.228, '5': -1.387, '6': 5.349, '7': -2.352, '8': -0.466} t=78
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 0, '4': 6, '5': 7, '6': 7, '7': 3, '8': 3} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.005], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.128, 0.409, 0.023, 0.009, 0.01, 0.03, 1.0], 'utility': [-0.052], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.456, 0.231, 0.032, 0.016, 0.02, 0.067, 1.0], 'utility': [-0.062], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.298, 0.245, 1.0, 0.054, 0.015, 0.013, 0.027], 'utility': [0.001], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.0, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.462], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.025, 0.003, 0.002, 0.002, 0.009], 'utility': [-0.375], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.491, 0.047, 0.421, 1.0, 0.065, 0.021, 0.02], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.002], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.11, 0.403, 0.021, 0.009, 0.009, 0.028, 1.0], 'utility': [-0.048], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.437, 0.211, 0.03, 0.016, 0.02, 0.066, 1.0], 'utility': [-0.056], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.278, 0.268, 1.0, 0.051, 0.015, 0.012, 0.027], 'utility': [0.065], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.537], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.065, 1.0, 0.082, 0.008, 0.004, 0.005, 0.018], 'utility': [-0.371], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}, '8': {'connected': [1, 0, 0, 1, 0, 0, 0], 'dr': [0.444, 0.036, 0.273, 1.0, 0.064, 0.019, 0.017], 'utility': [-0.072], 'ues_at_bs': [0.25, 0.375, 0.125, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.064, -0.118, 0.065, -0.027, 0.019, 0.267, -0.052]}} reward={'1': 4.574, '2': -2.165, '3': -1.24, '4': -0.216, '5': -1.798, '6': 4.574, '7': -2.842, '8': -0.848} t=79
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 0, '4': 6, '5': 7, '6': 7, '7': 3, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.006], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.151, 0.418, 0.025, 0.01, 0.011, 0.033, 1.0], 'utility': [-0.061], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.475, 0.252, 0.034, 0.017, 0.021, 0.067, 1.0], 'utility': [-0.069], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.321, 0.226, 1.0, 0.058, 0.016, 0.013, 0.027], 'utility': [-0.017], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.01, 1.0, 0.003], 'utility': [0.393], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.386], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.54, 0.061, 0.676, 1.0, 0.068, 0.024, 0.024], 'utility': [-0.08], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.005], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.128, 0.409, 0.023, 0.009, 0.01, 0.03, 1.0], 'utility': [-0.052], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.456, 0.231, 0.032, 0.016, 0.02, 0.067, 1.0], 'utility': [-0.062], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.298, 0.245, 1.0, 0.054, 0.015, 0.013, 0.027], 'utility': [0.001], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.0, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.462], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.025, 1.0, 0.025, 0.003, 0.002, 0.002, 0.009], 'utility': [-0.375], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.491, 0.047, 0.421, 1.0, 0.065, 0.021, 0.02], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.067, -0.142, -0.035, -0.026, 0.019, 0.229, -0.057]}} reward={'1': 3.87, '2': -2.38, '3': -1.398, '4': -0.28, '5': -2.032, '6': 3.87, '7': -3.098, '8': -1.026} t=80
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 2, '4': 6, '5': 7, '6': 7, '7': 3, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.182, 0.43, 0.028, 0.011, 0.012, 0.037, 1.0], 'utility': [0.002], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.495, 0.277, 0.036, 0.018, 0.022, 0.068, 1.0], 'utility': [-0.075], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.1, 0.01, 0.028, 1.0, 0.539, 0.024, 0.009], 'utility': [0.017], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.348, 0.21, 1.0, 0.062, 0.017, 0.013, 0.027], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.014, 1.0, 0.004], 'utility': [0.33], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.172], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.527, 0.072, 1.0, 0.893, 0.064, 0.024, 0.026], 'utility': [-0.083], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.006], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.151, 0.418, 0.025, 0.01, 0.011, 0.033, 1.0], 'utility': [-0.061], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.475, 0.252, 0.034, 0.017, 0.021, 0.067, 1.0], 'utility': [-0.069], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.079, 0.008, 0.024, 1.0, 0.393, 0.019, 0.007], 'utility': [0.019], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '5': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.321, 0.226, 1.0, 0.058, 0.016, 0.013, 0.027], 'utility': [-0.017], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.001, 0.0, 0.001, 0.01, 1.0, 0.003], 'utility': [0.393], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.386], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.54, 0.061, 0.676, 1.0, 0.068, 0.024, 0.024], 'utility': [-0.08], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.075, -0.155, -0.049, -0.031, 0.019, 0.194, -0.065]}} reward={'1': 3.226, '2': -1.221, '3': -1.343, '4': -0.327, '5': -1.563, '6': 3.226, '7': -1.704, '8': -1.262} t=81
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 2, '4': 6, '5': 4, '6': 7, '7': 3, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.021], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.223, 0.443, 0.031, 0.013, 0.014, 0.041, 1.0], 'utility': [-0.081], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.515, 0.303, 0.038, 0.019, 0.022, 0.069, 1.0], 'utility': [-0.034], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.033, 1.0, 0.742, 0.03, 0.011], 'utility': [0.021], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.379, 0.197, 1.0, 0.067, 0.018, 0.014, 0.027], 'utility': [-0.101], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.311], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.386], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.333, 0.056, 1.0, 0.521, 0.04, 0.016, 0.018], 'utility': [-0.058], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.008], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.182, 0.43, 0.028, 0.011, 0.012, 0.037, 1.0], 'utility': [0.002], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '3': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [0.495, 0.277, 0.036, 0.018, 0.022, 0.068, 1.0], 'utility': [-0.075], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.1, 0.01, 0.028, 1.0, 0.539, 0.024, 0.009], 'utility': [0.017], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.348, 0.21, 1.0, 0.062, 0.017, 0.013, 0.027], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.006, 0.001, 0.001, 0.001, 0.014, 1.0, 0.004], 'utility': [0.33], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.172], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.527, 0.072, 1.0, 0.893, 0.064, 0.024, 0.026], 'utility': [-0.083], 'ues_at_bs': [0.25, 0.25, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.079, -0.085, -0.077, -0.033, 0.017, 0.161, -0.037]}} reward={'1': 2.9, '2': -2.468, '3': -2.026, '4': -0.103, '5': -1.251, '6': 2.9, '7': -3.345, '8': -0.956} t=82
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 1, '3': 6, '4': 7, '5': 4, '6': 7, '7': 3, '8': 5} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.027], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.279, 0.459, 0.035, 0.015, 0.016, 0.047, 1.0], 'utility': [-0.095], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.536, 0.333, 0.041, 0.02, 0.023, 0.07, 1.0], 'utility': [0.013], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.155, 0.013, 0.037, 0.978, 1.0, 0.037, 0.013], 'utility': [0.031], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.416, 0.186, 1.0, 0.073, 0.019, 0.014, 0.028], 'utility': [-0.143], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.318], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.061, 0.007, 0.003, 0.004, 0.016], 'utility': [-0.389], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.201, 0.041, 1.0, 0.293, 0.024, 0.01, 0.012], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.021], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.223, 0.443, 0.031, 0.013, 0.014, 0.041, 1.0], 'utility': [-0.081], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.515, 0.303, 0.038, 0.019, 0.022, 0.069, 1.0], 'utility': [-0.034], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.126, 0.011, 0.033, 1.0, 0.742, 0.03, 0.011], 'utility': [0.021], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.379, 0.197, 1.0, 0.067, 0.018, 0.014, 0.027], 'utility': [-0.101], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.311], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.019, 1.0, 0.018, 0.002, 0.001, 0.002, 0.008], 'utility': [-0.386], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}, '8': {'connected': [1, 0, 1, 1, 0, 0, 0], 'dr': [0.333, 0.056, 1.0, 0.521, 0.04, 0.016, 0.018], 'utility': [-0.058], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.046, -0.167, -0.079, -0.018, 0.021, 0.145, -0.058]}} reward={'1': 2.9, '2': -1.793, '3': -1.793, '4': 0.205, '5': -1.072, '6': 2.9, '7': -3.135, '8': -0.873} t=83
DEBUG:deepcomp.util.simulation:Step                           action={'1': 2, '2': 1, '3': 6, '4': 7, '5': 6, '6': 7, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.023], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.354, 0.477, 0.04, 0.017, 0.019, 0.054, 1.0], 'utility': [-0.061], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.558, 0.366, 0.043, 0.021, 0.024, 0.071, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.012, 0.031, 0.708, 1.0, 0.034, 0.012], 'utility': [0.047], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.459, 0.177, 1.0, 0.081, 0.021, 0.015, 0.028], 'utility': [-0.145], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.313], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.125, 1.0, 0.185, 0.017, 0.007, 0.008, 0.028], 'utility': [-0.398], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.115, 0.029, 1.0, 0.158, 0.014, 0.006, 0.008], 'utility': [0.033], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.027], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '2': {'connected': [0, 1, 0, 0, 0, 0, 1], 'dr': [0.279, 0.459, 0.035, 0.015, 0.016, 0.047, 1.0], 'utility': [-0.095], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.536, 0.333, 0.041, 0.02, 0.023, 0.07, 1.0], 'utility': [0.013], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.155, 0.013, 0.037, 0.978, 1.0, 0.037, 0.013], 'utility': [0.031], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.416, 0.186, 1.0, 0.073, 0.019, 0.014, 0.028], 'utility': [-0.143], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.318], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.053, 1.0, 0.061, 0.007, 0.003, 0.004, 0.016], 'utility': [-0.389], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.201, 0.041, 1.0, 0.293, 0.024, 0.01, 0.012], 'utility': [-0.032], 'ues_at_bs': [0.125, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [0.013, -0.157, -0.087, -0.0, 0.031, 0.145, -0.041]}} reward={'1': 2.9, '2': -2.06, '3': -2.06, '4': 0.847, '5': -1.098, '6': 2.9, '7': -2.47, '8': -0.159} t=84
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 7, '5': 6, '6': 7, '7': 3, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.067], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.456, 0.495, 0.046, 0.02, 0.022, 0.062, 1.0], 'utility': [-0.068], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.579, 0.403, 0.046, 0.022, 0.025, 0.072, 1.0], 'utility': [-0.055], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.127, 0.01, 0.025, 0.512, 1.0, 0.031, 0.01], 'utility': [0.108], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.509, 0.17, 1.0, 0.089, 0.022, 0.016, 0.029], 'utility': [-0.245], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.001, 0.001, 0.011, 1.0, 0.003], 'utility': [0.425], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.251, 1.0, 0.518, 0.037, 0.014, 0.015, 0.044], 'utility': [-0.296], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.062, 0.019, 1.0, 0.081, 0.008, 0.004, 0.005], 'utility': [0.083], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.023], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.354, 0.477, 0.04, 0.017, 0.019, 0.054, 1.0], 'utility': [-0.061], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.558, 0.366, 0.043, 0.021, 0.024, 0.071, 1.0], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.141, 0.012, 0.031, 0.708, 1.0, 0.034, 0.012], 'utility': [0.047], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.459, 0.177, 1.0, 0.081, 0.021, 0.015, 0.028], 'utility': [-0.145], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.007, 0.001, 0.001, 0.002, 0.017, 1.0, 0.004], 'utility': [0.313], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '7': {'connected': [0, 1, 0, 0, 0, 0, 0], 'dr': [0.125, 1.0, 0.185, 0.017, 0.007, 0.008, 0.028], 'utility': [-0.398], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}, '8': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.115, 0.029, 1.0, 0.158, 0.014, 0.006, 0.008], 'utility': [0.033], 'ues_at_bs': [0.25, 0.375, 0.25, 0.25, 0.125, 0.25, 0.25], 'util_at_bs': [-0.054, -0.168, -0.056, 0.04, 0.047, 0.145, -0.054]}} reward={'1': 3.575, '2': -1.9, '3': -1.9, '4': 2.161, '5': -2.319, '6': 3.575, '7': -2.918, '8': -3.044} t=85
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 7, '5': 2, '6': 7, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.596, 0.515, 0.053, 0.023, 0.026, 0.072, 1.0], 'utility': [-0.074], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.602, 0.444, 0.049, 0.023, 0.025, 0.073, 1.0], 'utility': [-0.065], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.114, 0.009, 0.021, 0.371, 1.0, 0.028, 0.009], 'utility': [0.124], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.566, 0.164, 1.0, 0.1, 0.024, 0.017, 0.03], 'utility': [-0.256], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.472], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.319, 0.722, 1.0, 0.055, 0.018, 0.017, 0.045], 'utility': [-0.211], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.012, 1.0, 0.038, 0.004, 0.002, 0.003], 'utility': [0.158], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.067], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.456, 0.495, 0.046, 0.02, 0.022, 0.062, 1.0], 'utility': [-0.068], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.579, 0.403, 0.046, 0.022, 0.025, 0.072, 1.0], 'utility': [-0.055], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.127, 0.01, 0.025, 0.512, 1.0, 0.031, 0.01], 'utility': [0.108], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.509, 0.17, 1.0, 0.089, 0.022, 0.016, 0.029], 'utility': [-0.245], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.005, 0.001, 0.001, 0.001, 0.011, 1.0, 0.003], 'utility': [0.425], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.251, 1.0, 0.518, 0.037, 0.014, 0.015, 0.044], 'utility': [-0.296], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.062, 0.019, 1.0, 0.081, 0.008, 0.004, 0.005], 'utility': [0.083], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.062, -0.14, -0.152, 0.108, 0.108, 0.179, -0.062]}} reward={'1': 4.408, '2': -1.793, '3': -1.793, '4': 2.489, '5': -1.791, '6': 4.408, '7': -2.196, '8': -2.059} t=86
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 7, '5': 2, '6': 7, '7': 7, '8': 2} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.79, 0.536, 0.061, 0.028, 0.031, 0.084, 1.0], 'utility': [-0.078], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.624, 0.489, 0.053, 0.024, 0.026, 0.074, 1.0], 'utility': [-0.076], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.102, 0.007, 0.017, 0.269, 1.0, 0.026, 0.008], 'utility': [0.146], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.632, 0.159, 1.0, 0.112, 0.027, 0.018, 0.031], 'utility': [-0.301], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.572], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.191, 0.274, 1.0, 0.04, 0.012, 0.01, 0.023], 'utility': [-0.143], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.006, 1.0, 0.016, 0.002, 0.001, 0.001], 'utility': [0.329], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.031], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.596, 0.515, 0.053, 0.023, 0.026, 0.072, 1.0], 'utility': [-0.074], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.602, 0.444, 0.049, 0.023, 0.025, 0.073, 1.0], 'utility': [-0.065], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.114, 0.009, 0.021, 0.371, 1.0, 0.028, 0.009], 'utility': [0.124], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.566, 0.164, 1.0, 0.1, 0.024, 0.017, 0.03], 'utility': [-0.256], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.003, 0.001, 0.0, 0.001, 0.007, 1.0, 0.002], 'utility': [0.472], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.319, 0.722, 1.0, 0.055, 0.018, 0.017, 0.045], 'utility': [-0.211], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.031, 0.012, 1.0, 0.038, 0.004, 0.002, 0.003], 'utility': [0.158], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.069, -0.117, -0.103, 0.124, 0.124, 0.22, -0.069]}} reward={'1': 5.119, '2': -1.721, '3': -1.721, '4': 2.915, '5': -1.072, '6': 5.119, '7': -1.369, '8': -0.765} t=87
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 7, '5': 2, '6': 7, '7': 7, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.525, 0.067, 0.031, 0.034, 0.093, 0.942], 'utility': [-0.056], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.647, 0.54, 0.056, 0.025, 0.027, 0.076, 1.0], 'utility': [-0.064], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.091, 0.006, 0.014, 0.196, 1.0, 0.024, 0.007], 'utility': [0.171], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.707, 0.156, 1.0, 0.126, 0.029, 0.019, 0.032], 'utility': [-0.331], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.545], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.104, 0.104, 1.0, 0.028, 0.007, 0.005, 0.011], 'utility': [-0.019], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.006, 0.001, 0.0, 0.001], 'utility': [0.471], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.06], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.79, 0.536, 0.061, 0.028, 0.031, 0.084, 1.0], 'utility': [-0.078], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.624, 0.489, 0.053, 0.024, 0.026, 0.074, 1.0], 'utility': [-0.076], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.102, 0.007, 0.017, 0.269, 1.0, 0.026, 0.008], 'utility': [0.146], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.632, 0.159, 1.0, 0.112, 0.027, 0.018, 0.031], 'utility': [-0.301], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.572], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '7': {'connected': [0, 1, 1, 0, 0, 0, 0], 'dr': [0.191, 0.274, 1.0, 0.04, 0.012, 0.01, 0.023], 'utility': [-0.143], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.014, 0.006, 1.0, 0.016, 0.002, 0.001, 0.001], 'utility': [0.329], 'ues_at_bs': [0.25, 0.375, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.077, -0.099, -0.038, 0.146, 0.146, 0.256, -0.077]}} reward={'1': 5.363, '2': -1.206, '3': -1.206, '4': 3.417, '5': -0.0, '6': 5.363, '7': 0.804, '8': 0.804} t=88
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 7, '5': 6, '6': 7, '7': 4, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.4, 0.058, 0.027, 0.03, 0.08, 0.692], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.67, 0.596, 0.06, 0.026, 0.028, 0.077, 1.0], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.082, 0.005, 0.012, 0.144, 1.0, 0.022, 0.006], 'utility': [0.199], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.792, 0.153, 1.0, 0.143, 0.033, 0.021, 0.033], 'utility': [-0.355], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.575], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.052, 0.04, 1.0, 0.019, 0.004, 0.003, 0.005], 'utility': [0.043], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.002, 0.001, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.769], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.525, 0.067, 0.031, 0.034, 0.093, 0.942], 'utility': [-0.056], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.647, 0.54, 0.056, 0.025, 0.027, 0.076, 1.0], 'utility': [-0.064], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.091, 0.006, 0.014, 0.196, 1.0, 0.024, 0.007], 'utility': [0.171], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.707, 0.156, 1.0, 0.126, 0.029, 0.019, 0.032], 'utility': [-0.331], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.545], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.104, 0.104, 1.0, 0.028, 0.007, 0.005, 0.011], 'utility': [-0.019], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.005, 0.003, 1.0, 0.006, 0.001, 0.0, 0.001], 'utility': [0.471], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.06, -0.06, 0.04, 0.171, 0.171, 0.268, -0.06]}} reward={'1': 5.367, '2': -1.18, '3': -1.18, '4': 3.971, '5': 1.355, '6': 5.367, '7': 3.044, '8': 3.044} t=89
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 7, '5': 6, '6': 7, '7': 4, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.014], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.3, 0.049, 0.024, 0.026, 0.068, 0.501], 'utility': [-0.034], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.693, 0.659, 0.064, 0.027, 0.029, 0.078, 1.0], 'utility': [-0.077], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.073, 0.005, 0.01, 0.106, 1.0, 0.02, 0.006], 'utility': [0.228], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.888, 0.151, 1.0, 0.163, 0.036, 0.023, 0.035], 'utility': [-0.405], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.551], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.016, 1.0, 0.013, 0.002, 0.001, 0.002], 'utility': [0.176], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.039], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.4, 0.058, 0.027, 0.03, 0.08, 0.692], 'utility': [-0.047], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.67, 0.596, 0.06, 0.026, 0.028, 0.077, 1.0], 'utility': [-0.071], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.082, 0.005, 0.012, 0.144, 1.0, 0.022, 0.006], 'utility': [0.199], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.792, 0.153, 1.0, 0.143, 0.033, 0.021, 0.033], 'utility': [-0.355], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.575], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.052, 0.04, 1.0, 0.019, 0.004, 0.003, 0.005], 'utility': [0.043], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.002, 0.001, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.769], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.059, -0.059, 0.152, 0.199, 0.199, 0.268, -0.059]}} reward={'1': 5.37, '2': -1.105, '3': -1.105, '4': 4.552, '5': 2.641, '6': 5.37, '7': 5.139, '8': 5.139} t=90
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 7, '5': 6, '6': 7, '7': 4, '8': 7} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.105], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.222, 0.041, 0.02, 0.023, 0.057, 0.358], 'utility': [-0.054], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.717, 0.729, 0.068, 0.029, 0.03, 0.079, 1.0], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.066, 0.004, 0.008, 0.08, 1.0, 0.019, 0.005], 'utility': [0.24], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.996, 0.15, 1.0, 0.187, 0.04, 0.025, 0.037], 'utility': [-0.619], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.742], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.008, 1.0, 0.011, 0.002, 0.001, 0.001], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.014], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '2': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [1.0, 0.3, 0.049, 0.024, 0.026, 0.068, 0.501], 'utility': [-0.034], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.693, 0.659, 0.064, 0.027, 0.029, 0.078, 1.0], 'utility': [-0.077], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '4': {'connected': [0, 0, 0, 1, 1, 0, 0], 'dr': [0.073, 0.005, 0.01, 0.106, 1.0, 0.02, 0.006], 'utility': [0.228], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.888, 0.151, 1.0, 0.163, 0.036, 0.023, 0.035], 'utility': [-0.405], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.004, 1.0, 0.002], 'utility': [0.551], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.026, 0.016, 1.0, 0.013, 0.002, 0.001, 0.002], 'utility': [0.176], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.25, 0.375, 0.125, 0.125, 0.25, 0.25], 'util_at_bs': [-0.055, -0.055, 0.257, 0.228, 0.228, 0.269, -0.055]}} reward={'1': 6.372, '2': -0.634, '3': -0.543, '4': 4.798, '5': 1.212, '6': 6.372, '7': 2.443, '8': 2.443} t=91
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 4, '5': 2, '6': 0, '7': 4, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.161, 0.033, 0.017, 0.019, 0.047, 0.252], 'utility': [-0.021], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.74, 0.807, 0.073, 0.03, 0.031, 0.081, 1.0], 'utility': [-0.007], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.06, 0.003, 0.007, 0.061, 1.0, 0.018, 0.005], 'utility': [0.271], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.134, 0.896, 0.193, 0.04, 0.024, 0.035], 'utility': [-0.364], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.831], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.006, 1.0, 0.014, 0.002, 0.001, 0.001], 'utility': [0.246], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.105], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.222, 0.041, 0.02, 0.023, 0.057, 0.358], 'utility': [-0.054], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.717, 0.729, 0.068, 0.029, 0.03, 0.079, 1.0], 'utility': [-0.009], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.066, 0.004, 0.008, 0.08, 1.0, 0.019, 0.005], 'utility': [0.24], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.996, 0.15, 1.0, 0.187, 0.04, 0.025, 0.037], 'utility': [-0.619], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.002, 1.0, 0.001], 'utility': [0.742], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.008, 1.0, 0.011, 0.002, 0.001, 0.001], 'utility': [-0.015], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.032, -0.009, 0.122, 0.0, 0.24, 0.319, -0.032]}} reward={'1': 7.95, '2': -0.28, '3': -0.251, '4': 5.422, '5': 3.418, '6': 7.95, '7': 5.883, '8': 5.883} t=92
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 4, '5': 6, '6': 7, '7': 4, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.099], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.115, 0.027, 0.014, 0.016, 0.038, 0.174], 'utility': [0.02], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.764, 0.895, 0.078, 0.032, 0.032, 0.082, 1.0], 'utility': [-0.004], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.055, 0.003, 0.006, 0.047, 1.0, 0.017, 0.004], 'utility': [0.298], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.12, 0.801, 0.199, 0.041, 0.023, 0.033], 'utility': [-0.271], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.001, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.007, 1.0, 0.026, 0.002, 0.001, 0.002], 'utility': [0.195], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.036], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.161, 0.033, 0.017, 0.019, 0.047, 0.252], 'utility': [-0.021], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.74, 0.807, 0.073, 0.03, 0.031, 0.081, 1.0], 'utility': [-0.007], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.06, 0.003, 0.007, 0.061, 1.0, 0.018, 0.005], 'utility': [0.271], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.134, 0.896, 0.193, 0.04, 0.024, 0.035], 'utility': [-0.364], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.831], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.012, 0.006, 1.0, 0.014, 0.002, 0.001, 0.001], 'utility': [0.246], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [-0.014, -0.007, 0.294, 0.0, 0.271, 0.397, -0.014]}} reward={'1': 9.009, '2': 0.155, '3': 0.107, '4': 5.965, '5': 3.759, '6': 9.009, '7': 6.162, '8': 6.162} t=93
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 4, '5': 6, '6': 3, '7': 4, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.041], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.08, 0.021, 0.012, 0.013, 0.03, 0.118], 'utility': [0.068], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.788, 0.992, 0.083, 0.033, 0.033, 0.083, 1.0], 'utility': [-0.001], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.052, 0.003, 0.005, 0.038, 1.0, 0.017, 0.004], 'utility': [0.32], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.108, 0.718, 0.207, 0.041, 0.023, 0.031], 'utility': [-0.367], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.022, 0.009, 1.0, 0.057, 0.004, 0.002, 0.002], 'utility': [0.014], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.099], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.115, 0.027, 0.014, 0.016, 0.038, 0.174], 'utility': [0.02], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.764, 0.895, 0.078, 0.032, 0.032, 0.082, 1.0], 'utility': [-0.004], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.055, 0.003, 0.006, 0.047, 1.0, 0.017, 0.004], 'utility': [0.298], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.12, 0.801, 0.199, 0.041, 0.023, 0.033], 'utility': [-0.271], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.001, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.015, 0.007, 1.0, 0.026, 0.002, 0.001, 0.002], 'utility': [0.195], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.008, -0.004, 0.308, 0.0, 0.298, 0.45, 0.008]}} reward={'1': 9.591, '2': 0.671, '3': 0.533, '4': 6.402, '5': 2.857, '6': 9.591, '7': 4.315, '8': 4.315} t=94
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 3, '3': 6, '4': 4, '5': 6, '6': 3, '7': 4, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.056], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.055, 0.016, 0.009, 0.011, 0.023, 0.079], 'utility': [0.108], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.737, 1.0, 0.081, 0.031, 0.031, 0.077, 0.908], 'utility': [0.051], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.005, 0.032, 1.0, 0.018, 0.004], 'utility': [0.336], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.097, 0.646, 0.216, 0.042, 0.022, 0.029], 'utility': [-0.231], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.014, 1.0, 0.127, 0.008, 0.003, 0.004], 'utility': [-0.002], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [0.338], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.041], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 1], 'dr': [1.0, 0.08, 0.021, 0.012, 0.013, 0.03, 0.118], 'utility': [0.068], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.788, 0.992, 0.083, 0.033, 0.033, 0.083, 1.0], 'utility': [-0.001], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.052, 0.003, 0.005, 0.038, 1.0, 0.017, 0.004], 'utility': [0.32], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.108, 0.718, 0.207, 0.041, 0.023, 0.031], 'utility': [-0.367], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.022, 0.009, 1.0, 0.057, 0.004, 0.002, 0.002], 'utility': [0.014], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.25], 'util_at_bs': [0.034, -0.001, 0.216, 0.0, 0.32, 0.48, 0.034]}} reward={'1': 9.442, '2': 1.589, '3': 1.306, '4': 6.71, '5': 1.055, '6': 9.442, '7': 0.699, '8': 0.699} t=95
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 6, '4': 4, '5': 6, '6': 3, '7': 4, '8': 6} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.009], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.036, 0.012, 0.007, 0.008, 0.017, 0.051], 'utility': [0.178], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.682, 1.0, 0.077, 0.03, 0.029, 0.071, 0.817], 'utility': [0.053], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.004, 0.027, 1.0, 0.019, 0.004], 'utility': [0.344], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.089, 0.583, 0.228, 0.042, 0.022, 0.028], 'utility': [-0.245], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.048, 0.02, 1.0, 0.269, 0.013, 0.005, 0.006], 'utility': [-0.019], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.001, 0.001, 1.0, 0.001, 0.0, 0.0, 0.0], 'utility': [0.056], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [-0.056], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.055, 0.016, 0.009, 0.011, 0.023, 0.079], 'utility': [0.108], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.737, 1.0, 0.081, 0.031, 0.031, 0.077, 0.908], 'utility': [0.051], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.005, 0.032, 1.0, 0.018, 0.004], 'utility': [0.336], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.097, 0.646, 0.216, 0.042, 0.022, 0.029], 'utility': [-0.231], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '7': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.033, 0.014, 1.0, 0.127, 0.008, 0.003, 0.004], 'utility': [-0.002], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'utility': [0.338], 'ues_at_bs': [0.25, 0.125, 0.375, 0.0, 0.125, 0.25, 0.125], 'util_at_bs': [0.079, 0.051, 0.035, 0.0, 0.336, 0.472, 0.051]}} reward={'1': 10.087, '2': 2.305, '3': 1.681, '4': 6.873, '5': 0.092, '6': 10.087, '7': -1.13, '8': -1.383} t=96
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 6, '4': 4, '5': 2, '6': 4, '7': 6, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.003], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.023, 0.009, 0.006, 0.006, 0.012, 0.032], 'utility': [0.255], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.631, 1.0, 0.074, 0.028, 0.027, 0.065, 0.735], 'utility': [0.055], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.051, 0.003, 0.004, 0.024, 1.0, 0.021, 0.004], 'utility': [0.344], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.081, 0.529, 0.242, 0.044, 0.022, 0.027], 'utility': [-0.252], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.067, 0.027, 1.0, 0.516, 0.022, 0.008, 0.009], 'utility': [-0.073], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.003, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.014], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.009], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.036, 0.012, 0.007, 0.008, 0.017, 0.051], 'utility': [0.178], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.682, 1.0, 0.077, 0.03, 0.029, 0.071, 0.817], 'utility': [0.053], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.05, 0.003, 0.004, 0.027, 1.0, 0.019, 0.004], 'utility': [0.344], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.089, 0.583, 0.228, 0.042, 0.022, 0.028], 'utility': [-0.245], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.048, 0.02, 1.0, 0.269, 0.013, 0.005, 0.006], 'utility': [-0.019], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.001, 0.001, 1.0, 0.001, 0.0, 0.0, 0.0], 'utility': [0.056], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.115, 0.053, -0.069, -0.019, 0.344, 0.504, 0.053]}} reward={'1': 10.026, '2': 3.098, '3': 2.1, '4': 6.88, '5': -0.007, '6': 10.026, '7': -1.923, '8': -2.077} t=97
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 6, '4': 4, '5': 2, '6': 4, '7': 6, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.021], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.014, 0.006, 0.004, 0.005, 0.008, 0.019], 'utility': [0.341], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.582, 1.0, 0.071, 0.026, 0.025, 0.059, 0.66], 'utility': [0.058], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.054, 0.003, 0.004, 0.023, 1.0, 0.025, 0.004], 'utility': [0.337], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.075, 0.482, 0.258, 0.045, 0.022, 0.026], 'utility': [-0.279], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.848], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.102], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.01, 0.009, 1.0, 0.005, 0.001, 0.001, 0.001], 'utility': [0.102], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.003], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.023, 0.009, 0.006, 0.006, 0.012, 0.032], 'utility': [0.255], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.631, 1.0, 0.074, 0.028, 0.027, 0.065, 0.735], 'utility': [0.055], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.051, 0.003, 0.004, 0.024, 1.0, 0.021, 0.004], 'utility': [0.344], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.081, 0.529, 0.242, 0.044, 0.022, 0.027], 'utility': [-0.252], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'utility': [1.0], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.067, 0.027, 1.0, 0.516, 0.022, 0.008, 0.009], 'utility': [-0.073], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.003, 0.003, 1.0, 0.002, 0.0, 0.0, 0.0], 'utility': [0.014], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.155, 0.055, -0.104, -0.073, 0.344, 0.501, 0.055]}} reward={'1': 8.691, '2': 3.986, '3': 2.572, '4': 6.73, '5': 0.476, '6': 8.691, '7': -1.908, '8': -1.863} t=98
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 6, '4': 2, '5': 2, '6': 0, '7': 6, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.008, 0.004, 0.003, 0.003, 0.006, 0.011], 'utility': [0.437], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.536, 1.0, 0.068, 0.025, 0.023, 0.054, 0.592], 'utility': [0.062], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.058, 0.003, 0.004, 0.022, 1.0, 0.03, 0.005], 'utility': [0.322], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.07, 0.442, 0.278, 0.047, 0.022, 0.025], 'utility': [-0.356], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.724], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.111], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.021, 1.0, 0.011, 0.002, 0.001, 0.003], 'utility': [0.168], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.021], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.014, 0.006, 0.004, 0.005, 0.008, 0.019], 'utility': [0.341], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.582, 1.0, 0.071, 0.026, 0.025, 0.059, 0.66], 'utility': [0.058], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.054, 0.003, 0.004, 0.023, 1.0, 0.025, 0.004], 'utility': [0.337], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.075, 0.482, 0.258, 0.045, 0.022, 0.026], 'utility': [-0.279], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.001, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.848], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.102], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.01, 0.009, 1.0, 0.005, 0.001, 0.001, 0.001], 'utility': [0.102], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.199, 0.058, -0.093, -0.102, 0.337, 0.435, 0.058]}} reward={'1': 7.316, '2': 4.987, '3': 3.109, '4': 6.434, '5': 0.295, '6': 7.316, '7': -2.051, '8': -1.993} t=99
DEBUG:deepcomp.util.simulation:Step                           action={'1': 3, '2': 5, '3': 6, '4': 2, '5': 2, '6': 0, '7': 6, '8': 4} done=None next_obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.012], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.307, 0.066, -0.141, -0.121, 0.3, 0.3, 0.066]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.005, 0.002, 0.002, 0.002, 0.003, 0.006], 'utility': [0.547], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.307, 0.066, -0.141, -0.121, 0.3, 0.3, 0.066]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.493, 1.0, 0.065, 0.023, 0.021, 0.049, 0.531], 'utility': [0.066], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.307, 0.066, -0.141, -0.121, 0.3, 0.3, 0.066]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.065, 0.003, 0.005, 0.022, 1.0, 0.037, 0.006], 'utility': [0.3], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.307, 0.066, -0.141, -0.121, 0.3, 0.3, 0.066]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.065, 0.407, 0.301, 0.049, 0.022, 0.025], 'utility': [-0.374], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.307, 0.066, -0.141, -0.121, 0.3, 0.3, 0.066]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.004, 0.0, 0.0, 0.0, 0.003, 1.0, 0.003], 'utility': [0.588], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.307, 0.066, -0.141, -0.121, 0.3, 0.3, 0.066]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.121], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.307, 0.066, -0.141, -0.121, 0.3, 0.3, 0.066]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.055, 0.043, 1.0, 0.02, 0.004, 0.003, 0.006], 'utility': [0.071], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.307, 0.066, -0.141, -0.121, 0.3, 0.3, 0.066]}} obs={'1': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.02, 0.004, 0.003, 0.006, 0.069, 1.0, 0.014], 'utility': [0.008], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '2': {'connected': [1, 0, 0, 0, 0, 0, 0], 'dr': [1.0, 0.008, 0.004, 0.003, 0.003, 0.006, 0.011], 'utility': [0.437], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '3': {'connected': [1, 1, 0, 0, 0, 0, 1], 'dr': [0.536, 1.0, 0.068, 0.025, 0.023, 0.054, 0.592], 'utility': [0.062], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '4': {'connected': [0, 0, 0, 0, 1, 0, 0], 'dr': [0.058, 0.003, 0.004, 0.022, 1.0, 0.03, 0.005], 'utility': [0.322], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '5': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [1.0, 0.07, 0.442, 0.278, 0.047, 0.022, 0.025], 'utility': [-0.356], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '6': {'connected': [0, 0, 0, 0, 0, 1, 0], 'dr': [0.002, 0.0, 0.0, 0.0, 0.001, 1.0, 0.001], 'utility': [0.724], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '7': {'connected': [0, 0, 1, 1, 0, 0, 0], 'dr': [0.085, 0.035, 1.0, 0.821, 0.032, 0.011, 0.012], 'utility': [-0.111], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}, '8': {'connected': [0, 0, 1, 0, 0, 0, 0], 'dr': [0.025, 0.021, 1.0, 0.011, 0.002, 0.001, 0.003], 'utility': [0.168], 'ues_at_bs': [0.25, 0.125, 0.375, 0.125, 0.125, 0.25, 0.125], 'util_at_bs': [0.249, 0.062, -0.1, -0.111, 0.322, 0.366, 0.062]}} reward={'1': 5.997, '2': 6.131, '3': 3.724, '4': 6.007, '5': 0.229, '6': 5.997, '7': -2.722, '8': -2.825} t=100
INFO:deepcomp.util.simulation:Video saved                    path=/home/abhishek/cmc/result/D3-CoMP/decent/videos/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-27_13-00-38.html
INFO:deepcomp.util.simulation:Gif saved                      path=/home/abhishek/cmc/result/D3-CoMP/decent/videos/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-27_13-00-38.gif
DEBUG:deepcomp.util.simulation:Episode complete               avg_step_reward=9.419 eps_duration=519.396 scalar_metrics=['sum_utility'] vector_metrics=['dr', 'utility']
INFO:deepcomp.util.simulation:Scalar results                 results={'episode': [0], 'eps_duration_mean': [519.396], 'eps_duration_std': [519.396], 'step_reward_mean': [9.419], 'step_reward_std': [15.855], 'sum_utility_mean': [9.522], 'sum_utility_std': [15.98]}
INFO:deepcomp.util.simulation:Mean results                   results={'episode': 0.0, 'eps_duration_mean': 519.396, 'eps_duration_std': 519.396, 'step_reward_mean': 9.419, 'step_reward_std': 15.855, 'sum_utility_mean': 9.522, 'sum_utility_std': 15.98}
INFO:deepcomp.util.simulation:Simulation complete            avg_eps_reward=941.9 eps_length=100 num_episodes=1 step_reward_mean=9.419 step_reward_std=0.0
INFO:deepcomp.util.simulation:Starting evaluation            fast_ues=2 num_episodes=100 num_workers=1 slow_ues=5 static_ues=1
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [08:30<00:00,  5.10s/it]
INFO:deepcomp.util.simulation:Scalar results                 results={'episode': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 'eps_duration_mean': [5.609, 4.12, 6.068, 6.511, 4.565, 6.119, 4.761, 4.313, 4.746, 4.66, 4.352, 4.563, 4.616, 7.872, 4.369, 4.6, 4.333, 4.39, 5.944, 5.503, 4.443, 6.066, 4.544, 4.689, 4.823, 4.211, 4.76, 4.599, 5.89, 4.634, 6.425, 4.56, 6.582, 4.728, 4.644, 4.553, 4.519, 4.371, 6.069, 4.841, 4.838, 6.669, 4.474, 6.351, 4.758, 6.732, 5.985, 8.47, 4.421, 4.503, 4.58, 4.77, 6.213, 4.554, 4.571, 4.352, 4.457, 4.583, 4.295, 4.601, 4.832, 4.894, 4.802, 4.962, 4.966, 4.648, 5.882, 6.492, 4.553, 5.867, 4.438, 4.652, 5.936, 4.547, 4.439, 4.801, 6.95, 4.567, 4.666, 4.456, 8.139, 4.712, 6.38, 4.337, 6.043, 6.182, 4.397, 4.636, 4.604, 4.41, 5.773, 4.517, 4.679, 5.973, 4.691, 4.649, 4.532, 4.772, 4.409, 4.721], 'eps_duration_std': [5.609, 4.12, 6.068, 6.511, 4.565, 6.119, 4.761, 4.313, 4.746, 4.66, 4.352, 4.563, 4.616, 7.872, 4.369, 4.6, 4.333, 4.39, 5.944, 5.503, 4.443, 6.066, 4.544, 4.689, 4.823, 4.211, 4.76, 4.599, 5.89, 4.634, 6.425, 4.56, 6.582, 4.728, 4.644, 4.553, 4.519, 4.371, 6.069, 4.841, 4.838, 6.669, 4.474, 6.351, 4.758, 6.732, 5.985, 8.47, 4.421, 4.503, 4.58, 4.77, 6.213, 4.554, 4.571, 4.352, 4.457, 4.583, 4.295, 4.601, 4.832, 4.894, 4.802, 4.962, 4.966, 4.648, 5.882, 6.492, 4.553, 5.867, 4.438, 4.652, 5.936, 4.547, 4.439, 4.801, 6.95, 4.567, 4.666, 4.456, 8.139, 4.712, 6.38, 4.337, 6.043, 6.182, 4.397, 4.636, 4.604, 4.41, 5.773, 4.517, 4.679, 5.973, 4.691, 4.649, 4.532, 4.772, 4.409, 4.721], 'step_reward_mean': [9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419, 9.419], 'step_reward_std': [15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855, 15.855], 'sum_utility_mean': [9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522, 9.522], 'sum_utility_std': [15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98, 15.98]}
INFO:deepcomp.util.simulation:Mean results                   results={'episode': 49.5, 'eps_duration_mean': 5.1, 'eps_duration_std': 5.1, 'step_reward_mean': 9.419, 'step_reward_std': 15.855, 'sum_utility_mean': 9.522, 'sum_utility_std': 15.98}
INFO:deepcomp.util.simulation:Simulation complete            avg_eps_reward=941.9 eps_length=100 num_episodes=100 step_reward_mean=9.419 step_reward_std=0.0
INFO:deepcomp.util.simulation:Writing scalar results         file=/home/abhishek/cmc/result/D3-CoMP/decent/test/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-27_13-00-38.csv
INFO:deepcomp.util.simulation:Writing vector results         file=/home/abhishek/cmc/result/D3-CoMP/decent/test/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-27_13-00-38_dr.pkl metric=dr
INFO:deepcomp.util.simulation:Writing vector results         file=/home/abhishek/cmc/result/D3-CoMP/decent/test/PPO_MultiAgentMobileEnv_large_mixed_8UEs-log-avg_fixed-fixed_42_2022-04-27_13-00-38_utility.pkl metric=utility
INFO:deepcomp.main:Finished                       agent=/home/abhishek/cmc/result/D3-CoMP/decent/train/PPO_2022-04-27_12-29-54/PPO_MultiAgentMobileEnv_a3fcd_00000_0_2022-04-27_12-29-54/checkpoint_000013/checkpoint-13
abhishek@abhishek-pc:~$ 
```


