# Different Experiments and Commands run with the DeepCoMP

## Different variants of DeepCoMP

DeepCoMP has three different varients based on Agent and Policy

- [DeepCoMP](#DeepCoMP)
- [DD-CoMP](#DD-CoMP)
- [D3-CoMP](#D3-CoMP)


## DeepCoMP
DeepCoMP has a central agent using central policy. To run DeepCoMP, use ```--alg ppo --agent central```
- With 500 Steps, resulting a very bad QoE (Quality of Experience)
	- run Linux Command ```deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent central --workers 2 --dashboard --ue-details --eval 100 --train-steps 500 --seed 42 --video both --result-dir /home/abhishek/cmc/result/DeepCoMP/bad```
- With 50000 steps, resulting a decent QoE (Quality of Experience)
	- run Linux Command ```deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent central --workers 2 --dashboard --ue-details --eval 100 --train-steps 50000 --seed 42 --video both --result-dir /home/abhishek/cmc/result/DeepCoMP/decent```
- With 200,000 steps, resulting a good QoE (Quality of Experience)
	- run Linux Command ```deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent central --workers 2 --dashboard --ue-details --eval 100 --train-steps 200000 --seed 42 --video both --result-dir /home/abhishek/cmc/result/DeepCoMP/good```


## DD-CoMP
DD-CoMP has a distributed agents using central policy. To run DD-CoMP, use ```--alg ppo --agent multi```
- With 500 Steps, resulting a very bad QoE (Quality of Experience)
	- run Linux Command ```deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent multi --workers 2 --dashboard --ue-details --eval 100 --train-steps 500 --seed 42 --video both --result-dir /home/abhishek/cmc/result/DD-CoMP/bad```
- With 50000 steps, resulting a decent QoE (Quality of Experience)
	- run Linux Command ```deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent multi --workers 2 --dashboard --ue-details --eval 100 --train-steps 50000 --seed 42 --video both --result-dir /home/abhishek/cmc/result/DD-CoMP/decent```
- With 200,000 steps, resulting a good QoE (Quality of Experience)
	- run Linux Command ```deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent multi --workers 2 --dashboard --ue-details --eval 100 --train-steps 200000 --seed 42 --video both --result-dir /home/abhishek/cmc/result/DD-CoMP/good```


## D3-CoMP
D3-CoMP has a distributed agents using separate policies. To run D3-CoMP, use ```--alg ppo --agent multi --separate-agent-nns```
- With 500 Steps, resulting a very bad QoE (Quality of Experience)
	- run Linux Command ```deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent multi --separate-agent-nns --workers 2 --dashboard --ue-details --eval 100 --train-steps 500 --seed 42 --video both --result-dir /home/abhishek/cmc/result/D3-CoMP/bad```
- With 50000 steps, resulting a decent QoE (Quality of Experience)
	- run Linux Command ```deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent multi --separate-agent-nns --workers 2 --dashboard --ue-details --eval 100 --train-steps 50000 --seed 42 --video both --result-dir /home/abhishek/cmc/result/D3-CoMP/decent```
- With 200,000 steps, resulting a good QoE (Quality of Experience)
	- run Linux Command ```deepcomp --env large --static-ues 1 --slow-ues 5 --fast-ues 2 --alg ppo --agent multi --separate-agent-nns --workers 2 --dashboard --ue-details --eval 100 --train-steps 200000 --seed 42 --video both --result-dir /home/abhishek/cmc/result/D3-CoMP/good```