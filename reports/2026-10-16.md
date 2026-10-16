# CausalRadar 日报 - 2026-10-16

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Grounding Generative Verification in 3D Content

- 作者：Shuanglin Li, Jiaying Lin, Shuquan Ye｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.22360v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Recent advances in multimodal large language models (MLLMs) and 3D generation have expanded 3D understanding and synthesis. However, beyond visual fidelity, task-specific correctness grounded in 3D evidence remains a major challenge.

### 方法
Recent advances in multimodal large language models (MLLMs) and 3D generation have expanded 3D understanding and synthesis. A human study reveals a 21.6 percentage-point gap between humans and the strongest tested model, GPT-6 Astra, while explanation-aware analysis exposes weaknesses in rejection reliability. We develop a scalable pipeline combining multi-view fact extraction, controlled 3D editing, and native annotations to produce 14,126 training examples with contradiction explanations and linked counterfactuals.

### 实验/数据
Together, our benchmark, analysis, and data pipeline establish a foundation for models to reflect on 3D content through reliable verification feedback.

### 结果
In human-labeled sixteen-candidate pools, oracle selection improves complete factual success from 26.7% to 90.0%.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Together, our benchmark, analysis, and data pipeline establish a foundation for models to reflect on 3D content through reliable verification feedback.

### 2. Knowledge That Is Linear Before Fine-Tuning Generalizes After It

- 作者：Faridoun Mehri, Hinrich Schütze｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.22300v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Not all facts a language model can recall support further learning equally well. We distinguish active facts, which support generalization beyond their own recall, from inert facts, which can be recalled but do not support such generalization in a given task.

### 方法
Not all facts a language model can recall support further learning equally well. We fine-tune the model on the new relation for a subset of subjects, without telling it the original relation or the relabeling rule, and test whether it assigns the corresponding labels to held-out subjects that share an answer in the original relation. Across eleven language models and 70 relations, how linearly readable the original relation is in pretrained representations strongly predicts this generalization.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Whether a new relation generalizes depends less on whether its facts can be recalled than on how readily their shared structure can be read out linearly.

### 3. LEASH: Uncertainty-Aware Weak-to-Strong Escalation and Oversight for Computer-Use Agents

- 作者：Qingni Wang, Changdae Oh, Yuzhe Yang, Sharon Li, Jiachen Yang, Ang Li, Xin Eric Wang｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.22280v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Computer-use agents increasingly tackle long-horizon tasks, where running a frontier model at every step is expensive and a small open-weight model alone often fails. Weak-to-strong escalation offers a middle ground where a weak agent acts by default and hands control to a strong one only when needed.

### 方法
Computer-use agents increasingly tackle long-horizon tasks, where running a frontier model at every step is expensive and a small open-weight model alone often fails. To this end, we propose LEASH, a training-free framework that unleashes the strong agent only when the weak agent's latent uncertainty signals it is needed, and keeps it on a leash afterward. Specifically, we compare the weak model's hidden states with those from its past successful and failed trajectories, and a state that looks more like the failures signals higher uncertainty.

### 实验/数据
Experiments on OSWorld across four contemporary model backbones show that LEASH consistently improves over standalone weak agents and outperforms random escalation by 6.55--11.94 points at matched escalation rates.

### 结果
Experiments on OSWorld across four contemporary model backbones show that LEASH consistently improves over standalone weak agents and outperforms random escalation by 6.55--11.94 points at matched escalation rates.

### 结论/启示（面向电商发券、定价、营销算法等应用）
With Qwen3.5-35B-A3B, LEASH achieves 73.66% task success at $0.4117 per task, matching always-on Claude Opus 5 (72.90%) while reducing inference cost by 19.2%.

### 4. Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Legal Guidelines

- 作者：Florian Lercher, Karan Mahesh, Yujun Huang, Meshal Alharbi, Runyu Zhang, Hanna Krasowski, Michael R. Benjamin, Matthias Althoff 等｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.22277v1

> 命中：hit_abstract=['CATE']

### 背景/问题
When robots are deployed in the real-world, they must interact with other agents and accomplish their own goals while adhering to legal constraints. These potentially conflicting objectives are often only partially prioritized, making scalarized objectives or fully specified hierarchies unsuitable.

### 方法
We present a framework for multi-agent motion planning under legal requirements based on games with partially ordered preferences (posetal games). We apply the framework to maritime navigation, systematically lifting pairwise traffic rules to multi-vessel encounters.

### 实验/数据
未在摘要中明确给出。

### 结果
We apply the framework to maritime navigation, systematically lifting pairwise traffic rules to multi-vessel encounters.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results indicate that guideline-based posetal games offer an auditable route from partially specified laws to multi-agent motion planning.

### 5. Topology-Inspired Fine-Tuning for Wind-Field Super-Resolution

- 作者：Arjun Dadhwal, Brian Summa｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.22262v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Scientific super-resolution (SR) models are typically optimized with pointwise reconstruction losses, yet scientific interpretation often hinges on extrema, connected regions, and multiscale scalar structure. We characterize this tension with pretrained CNN and GAN wind-field SR models.

### 方法
Scientific super-resolution (SR) models are typically optimized with pointwise reconstruction losses, yet scientific interpretation often hinges on extrema, connected regions, and multiscale scalar structure. We characterize this tension with pretrained CNN and GAN wind-field SR models.

### 实验/数据
We characterize this tension with pretrained CNN and GAN wind-field SR models. Motivated by this disagreement, we fine-tune the pretrained CNN with differentiable topology-inspired auxiliary losses on scalar speed, gradient magnitude, soft high-speed level sets, and local maxima, and with fixed-pair supervision, which constrains predicted values and persistence at ground-truth persistence-pair endpoints located offline with the Topology ToolKit. A loss study of 16 fine-tuning configurations, each compared with a matched standard fine-tuning control that uses only the original reconstruction loss, on a fixed 168-field benchmark (with topology evaluated on a fixed 160 by 160 subregion of each field), shows that, among the scalar-field losses, gradient supervision provides the strongest PD improvement but does not improve mean MT distance, whereas fixed-pair supervision gives the largest and most consistent joint improvement in PD and MT distances.

### 结果
A loss study of 16 fine-tuning configurations, each compared with a matched standard fine-tuning control that uses only the original reconstruction loss, on a fixed 168-field benchmark (with topology evaluated on a fixed 160 by 160 subregion of each field), shows that, among the scalar-field losses, gradient supervision provides the strongest PD improvement but does not improve mean MT distance, whereas fixed-pair supervision gives the largest and most consistent joint improvement in PD and MT distances. Mean MT distance also improves, but on only 91 of those 150 fields, indicating that PD and MT capture complementary structure.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Mean MT distance also improves, but on only 91 of those 150 fields, indicating that PD and MT capture complementary structure.

### 6. Geometric Graph Representations via Compact SAT Encodings

- 作者：L. Sunil Chandran, Rishikesh Gajjala, Suraj Kumar Sahoo, Aatman Supkar｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.22241v1

> 命中：hit_abstract=['CATE']

### 背景/问题
We present compact SAT encodings and certifying exact solvers for boxicity and cubicity. The boxicity of a graph is the minimum dimension in which it is the intersection graph of axis-aligned boxes; cubicity is defined analogously using unit cubes.

### 方法
We present compact SAT encodings and certifying exact solvers for boxicity and cubicity. Satisfying models are decoded into independently checked geometric representations, while unsatisfiable instances used as lower-bound evidence carry mechanically verified DRAT certificates.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
This disproves the conjecture of Caoduro and Sebo that $\operatorname{boxicity}(K(n,k))=n-k$ for all $k\ge3$ and $n\ge2k+1$.

### 7. WaveLLM: Wavelet-Domain LLM Entropy Modeling for Lossless Image Compression

- 作者：Yue Yu, Bowei Kang, Changsheng Gao, Dong Liu, Xiaoyan Sun｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.22232v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Lossless image compression fundamentally relies on accurate entropy modeling, driving a recent shift toward large language model (LLM)-based methods. However, existing approaches mainly emphasize the modeling capacity of LLMs while directly serializing images into pixel or residual sequences, leaving heterogeneous signal patterns entangled within a single prediction stream.

### 方法
Lossless image compression fundamentally relies on accurate entropy modeling, driving a recent shift toward large language model (LLM)-based methods. However, existing approaches mainly emphasize the modeling capacity of LLMs while directly serializing images into pixel or residual sequences, leaving heterogeneous signal patterns entangled within a single prediction stream. In this paper, we argue that effective entropy modeling depends not only on model capacity, but also on the predictability of the input representation.

### 实验/数据
未在摘要中明确给出。

### 结果
Built on Llama-3.2-3B with LoRA adaptation, WaveLLM achieves 2.51, 2.24, and 2.27 bpsp on Kodak, CLIC.pro, and DIV2K, respectively, outperforming the PixelCNN-based codec using the same wavelet transform by 0.43, 0.36, and 0.46 bpsp, and surpassing recent LLM-based lossless compressors on all three benchmarks.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Built on Llama-3.2-3B with LoRA adaptation, WaveLLM achieves 2.51, 2.24, and 2.27 bpsp on Kodak, CLIC.pro, and DIV2K, respectively, outperforming the PixelCNN-based codec using the same wavelet transform by 0.43, 0.36, and 0.46 bpsp, and surpassing recent LLM-based lossless compressors on all three benchmarks.

### 8. Dexterity from Supervised Play

- 作者：Botao He, Yiming Dou, Yiannis Aloimonos, Jitendra Malik, Akash Sharma, Ruoshi Liu｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.22340v1

> 命中：hit_abstract=['policy learning']

### 背景/问题
How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation? We present DSP: Dexterity from supervised play, a framework in which a robot learns a play policy from minutes of human play through behavior cloning, then deploys it autonomously to collect hours of interaction data to train a world model.

### 方法
We present DSP: Dexterity from supervised play, a framework in which a robot learns a play policy from minutes of human play through behavior cloning, then deploys it autonomously to collect hours of interaction data to train a world model. During inference, the same play policy then guides model-predictive control (MPC) by proposing candidate action sequences for evaluation under the learned world model. To accelerate inference, we also introduce a method for distilling a closed-loop, goal-conditioned policy through self-play within the learned world model.

### 实验/数据
We present DSP: Dexterity from supervised play, a framework in which a robot learns a play policy from minutes of human play through behavior cloning, then deploys it autonomously to collect hours of interaction data to train a world model. We evaluate this framework on underactuated pushing and any-to-any in-hand pose reorientation with a multifingered hand, in simulation and real world. In real world experiment, our method outperforms hindsight behavior cloning by 69.6% in success rate and achieves comparable success to reinforcement learning with 490 times less interaction data.

### 结果
In real world experiment, our method outperforms hindsight behavior cloning by 69.6% in success rate and achieves comparable success to reinforcement learning with 490 times less interaction data.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results demonstrate that supervised play can autonomously collect interaction data, guide model-based planning, and enable policy learning without any task-specific demonstrations or sim-to-real transfer.

### 9. SoftCache: Adaptive Step Size Caching for Diffusion Transformers

- 作者：Shimon Malnick, Nadav Orenstein, Ohad Fried, Shai Avidan｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22369v1

### 背景/问题
Diffusion and flow models generate a sample over iterative steps, each a full pass through a large network, and that pass dominates generation cost. Training-free caching accelerates them by reusing activations from recent evaluations instead of recomputing them.

### 方法
Diffusion and flow models generate a sample over iterative steps, each a full pass through a large network, and that pass dominates generation cost. We propose SoftCache, which performs soft caching: instead of a binary switch, the headroom sets how far each cached step goes.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
SoftCache requires no training and adds no per-backbone settings: on FLUX for images and on HunyuanVideo and Wan2.1 for video, at speedups from $3.5\times$ to $6.9\times$, it is ahead of every baseline on all four fidelity metrics.

### 10. Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation

- 作者：Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li, Lingchen Yang, Longteng Duan, Ying Xue 等｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22363v1

### 背景/问题
We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed actions; and Plan, which jointly generates action trajectories and their anticipated visual consequences conditioned on an initial image, a language instruction, and an optional visual goal. Our model integrates a compact, structured 3D action representation into a pretrained video diffusion transformer through a mixture-of-transformers architecture with shared base weights, modality-specific adaptation, and bidirectional visual-action attention.

### 方法
We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed actions; and Plan, which jointly generates action trajectories and their anticipated visual consequences conditioned on an initial image, a language instruction, and an optional visual goal. Our model integrates a compact, structured 3D action representation into a pretrained video diffusion transformer through a mixture-of-transformers architecture with shared base weights, modality-specific adaptation, and bidirectional visual-action attention. Experiments show that unified training improves all three capabilities over single-mode training, including gains in planning quality under a vision-language model evaluation.

### 实验/数据
Experiments show that unified training improves all three capabilities over single-mode training, including gains in planning quality under a vision-language model evaluation. Through unified training, our model outperforms specialized baselines on 3D hand reconstruction and action-conditioned video prediction across four datasets, while producing goal-directed manipulation videos with stronger instruction adherence and action progression than video-generation baselines.

### 结果
Experiments show that unified training improves all three capabilities over single-mode training, including gains in planning quality under a vision-language model evaluation. Through unified training, our model outperforms specialized baselines on 3D hand reconstruction and action-conditioned video prediction across four datasets, while producing goal-directed manipulation videos with stronger instruction adherence and action progression than video-generation baselines.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Project Page: https://p3-wam.pages.dev/

### 11. Integral and higher-genus quantum McKay correspondence in type D

- 作者：Andrea Brini, Jingxiang Ma｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22359v1

### 背景/问题
We establish Iritani's integral form of the $\mathbb{C}^\times$-equivariant Crepant Transformation Conjecture (CTC) for the minimal resolution of the surface singularity $\mathbb{C}^2/\mathbb{BD}_{4n}$, where $\mathbb{BD}_{4n}$ is the binary dihedral group of order $4n$. We then use Givental's quantisation formalism to prove the all-genus full-descendent CTC in that case.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
As an application, we deduce the Bryan-Cadman-Young degree-zero form of the orbifold Gromov-Witten/Donaldson-Thomas correspondence for the Calabi-Yau 3-orbifold $[\mathbb{C}^2/\mathbb{BD}_{4n}] \times \mathbb{C}$.

### 12. PathFM: Fast Generative Forecasting of Multivariate Trajectories

- 作者：Jiachen Yao, Xiyuan Zhang, Annan Yu, Boran Han, Abdul Fatir Ansari, Shuai Zhang, Michael Bohlke-Schneider, Bernie Wang｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22358v1

### 背景/问题
Time series foundation models are becoming increasingly popular for general-purpose forecasting. However, most leading models predict marginal quantiles, leaving the dependence structure of future trajectories unspecified.

### 方法
Time series foundation models are becoming increasingly popular for general-purpose forecasting. However, most leading models predict marginal quantiles, leaving the dependence structure of future trajectories unspecified. To model this dependence, we introduce PathFM, a trajectory-based forecasting model that uses flow matching to generate complete future paths.

### 实验/数据
Experiments on chaotic systems further show that our flow model sustains long-run variability, while strong baselines rapidly collapse.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
PathFM makes generative time series forecasting both competitive and practical, enabling diverse downstream applications.

### 13. Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation

- 作者：Tianxing Chen, Wenwei Lin, Chuqiao Lyu, Peicheng Xiang, Junyuan Tang, Tian Nian, Zijian Cai, Kehe Ye 等｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22342v1

### 背景/问题
Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways.

### 方法
We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways.

### 实验/数据
To scale this supervision, we build HumanTouch, a 1,000-hour dataset of full-hand tactile human manipulation, and pretrain Spark-0 on it together with egocentric video, robot data, and simulation. Compared with vision-only pretraining on the same data and compute with touch discarded, retaining the touch of 1,000 hours of HumanTouch raises vision-only success on Ego Humanoid from 52.5% to 71.7%, and success on SparkArena-Real, where touch is also used at deployment, from 44.0% to 52.0%, indicating that touch serves not only as a policy input but also as scalable supervision for dexterous visuomotor pretraining.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The Website is available at: https://xsparkai.com/Spark-0.

### 14. Illumination-Aware Active Perception for Spacecraft Inspection

- 作者：Sagarika Rao Valluri, Benjamin Riviere｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22335v1

### 背景/问题
Harsh and rapidly varying orbital illumination introduces failure modes during spacecraft inspection. Existing planners rely on line-of-sight inspection metrics which perform occlusion checks against a known target and conflate geometric visibility with task-relevant information.

### 方法
We propose an inspection-planning framework that replaces geometric visibility with a learned measure of camera information derived from a classifier variational autoencoder (VAE) that operates directly on the captured image. The encoder model is trained to classify spacecraft surface components from rendered patches, and its total latent variance is used to learn the varying illumination of said components, replacing binary visibility checks with a continuous, image-grounded quantity. We evaluate the approach by implementing a Guidance, Navigation, and Control architecture in a photorealistic physics simulator, and vary lighting and viewing geometries with multiple orbits.

### 实验/数据
未在摘要中明确给出。

### 结果
We show that, although all approaches successfully maximize their own objective, our approach results in better illumination: a mean brightness of $0.57$, with $81.6\%$ of observations above $0.25$, compared with $0.02$ ($3.0\%$) for geometric planning with an illumination band and $0.04$ ($6.0\%$) for purely geometric planning.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We show that, although all approaches successfully maximize their own objective, our approach results in better illumination: a mean brightness of $0.57$, with $81.6\%$ of observations above $0.25$, compared with $0.02$ ($3.0\%$) for geometric planning with an illumination band and $0.04$ ($6.0\%$) for purely geometric planning.

### 15. Evaluation Awareness Beyond English: Do LLMs Act Differently When Tested in Indic Languages?

- 作者：Trizal Garg, Sibayan Mitra, Arya Karanjkar, Advait Singh, Jagat Sesh Challa, Yash Sinha, Siddharth Mehrotra, Dhruv Kumar 等｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22333v1

### 背景/问题
Large language models (LLMs) can often tell when they are being tested. This ability, known as evaluation awareness, can lead models to act more cautiously during safety evaluations than in real use.

### 方法
Large language models (LLMs) can often tell when they are being tested. This ability, known as evaluation awareness, can lead models to act more cautiously during safety evaluations than in real use. Existing work has studied evaluation awareness almost entirely in English, although models serve users in many languages.

### 实验/数据
未在摘要中明确给出。

### 结果
This increase appears in all four models and all six languages.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results suggest that safety evaluations in Indic languages may not reflect how models treat their everyday users.

### 16. Magic in quantum trajectory unravelings of noisy random quantum circuits

- 作者：Sara Santos, Alessio Paviglianiti, Vincenzo Savona｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22318v1

### 背景/问题
The quantum-trajectory description of a noisy quantum circuit is not unique: every Kraus representation of the noise channel defines a different unraveling, i.e., a different ensemble of pure states that averages to the same density matrix. While all unravelings share the same expectation values of observables, they generally differ in the amount of quantum resources carried by the individual trajectories.

### 方法
未在摘要中明确给出。

### 实验/数据
Since the cost of stabilizer-based classical simulation grows exponentially with the magic of the state, these high-magic trajectories, rather than the average, control the simulation cost. Our results delineate the potential and the limitations of unraveling optimization as a route to the classical simulation of noisy quantum dynamics with stabilizer methods.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our results delineate the potential and the limitations of unraveling optimization as a route to the classical simulation of noisy quantum dynamics with stabilizer methods.

### 17. MindEval2: Clinically Grounded Patients and Rubrics for Evaluating Language Models in Mental Health Support

- 作者：John Mendonça, Daniel Tschernutter, José Pombal, Areti Vassilopoulos, Catarina Botelho, Ignacio Sarasua, Maya D'Eon, Nuno Guerreiro 等｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22314v1

### 背景/问题
With people increasingly turning to AI chatbots for mental health support, the need to evaluate these tools is becoming more pressing. Recent benchmarks attempt to mimic a realistic setting by simulating multi-turn interactions with synthetic patients and evaluating them with an LLM-as-a-judge.

### 方法
To bridge these gaps, we introduce MindEval2, an evaluation framework that consists of two components: Mental Health Quality Rubrics (MHQR), for evaluation, and MindSim, for patient simulation. The harness also contains a memory component that is updated between each interaction, enabling MindEval2 to model the longitudinal aspect of mental health. We evaluate 18 proprietary and open-weight models on MindEval2, finding that while frontier models have largely improved on issues related to surface level quality and boundaries, guidance calibration remains the dominant failure mode across all models, accounting for most of the quality gap.

### 实验/数据
To bridge these gaps, we introduce MindEval2, an evaluation framework that consists of two components: Mental Health Quality Rubrics (MHQR), for evaluation, and MindSim, for patient simulation.

### 结果
We evaluate 18 proprietary and open-weight models on MindEval2, finding that while frontier models have largely improved on issues related to surface level quality and boundaries, guidance calibration remains the dominant failure mode across all models, accounting for most of the quality gap.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We evaluate 18 proprietary and open-weight models on MindEval2, finding that while frontier models have largely improved on issues related to surface level quality and boundaries, guidance calibration remains the dominant failure mode across all models, accounting for most of the quality gap.

### 18. Near-Optimal Parallel $M$-Matrix Scaling

- 作者：Chih-Hung Liu, Aaron Sidford, Ta-Wei Tu｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22302v1

### 背景/问题
In this paper we consider the problem of computing a positive diagonal scaling of a $d \times d$ symmetric $M$-matrix so that all row and column sums are $1$. We provide a poly-logarithmic iteration algorithm that solves this problem to high accuracy, where the cost of each iteration is dominated by the cost of solving a Laplacian system.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
This improves upon the recent $\tilde{O}(d^{1/3})$ iteration bound of [Vladu STOC 2025] and yields a randomized algorithm for the problem that runs in near-linear time and poly-logarithmic parallel depth.

### 结论/启示（面向电商发券、定价、营销算法等应用）
This improves upon the recent $\tilde{O}(d^{1/3})$ iteration bound of [Vladu STOC 2025] and yields a randomized algorithm for the problem that runs in near-linear time and poly-logarithmic parallel depth.

### 19. AI Consilium: a Benchmark of LLM Clinical Multidisciplinary Second Opinions

- 作者：Alexey A. Bokov, Ivan I. Panin, Nikolay B. Nechaev, Mikhail Yu. Valkov, Valeria Yu. Chernina, Natalia Gombolevskaya, Ayyaz Hussain, Vladimir M. Agafonov 等｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22298v1

### 背景/问题
Large language models (LLMs) can generate differential diagnoses for complex cases, but a useful second opinion must also be factually grounded, clinically coherent, actionable, and safe. We developed a multidimensional benchmark using 300 diagnostically resolved NEJM--MedQA cases: 110 for physician reference ratings and Judge calibration and 190 for held-out evaluation.

### 方法
Large language models (LLMs) can generate differential diagnoses for complex cases, but a useful second opinion must also be factually grounded, clinically coherent, actionable, and safe. We developed a multidimensional benchmark using 300 diagnostically resolved NEJM--MedQA cases: 110 for physician reference ratings and Judge calibration and 190 for held-out evaluation. Eight single-model pipelines generated independent role-specific opinions and interactive-consilium reports under free-form and structured clinical-reasoning conditions.

### 实验/数据
未在摘要中明确给出。

### 结果
Compared with the structured pre-consilium primary-role opinion, the complete structured synthesis had higher pooled scores across all five shared criteria, with the largest increases in problem prioritization, factual grounding, and reasoning coherence.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These findings show that the benchmark can distinguish model capability, the contribution of multidisciplinary synthesis, criterion-specific effects of response structure, deliberation dynamics, and inference requirements within one common-case evaluation.

### 20. Backward Compatibility in Zero-Bit Neural Audio Watermarking

- 作者：Admir Krnić, Kosta Pavlović, Petar Nedić, Željko Bolević, Slavko Kovačević, Igor Djurović｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22296v1

### 背景/问题
Neural watermarking systems are typically trained as tightly coupled embedder-detector pairs and implicitly assume static deployment. In real-world deployments, embedders and detectors are frequently updated and selectively decoupled for security and versioning purposes, which can break detection in previously embedded content and, more critically, increase false-positive rates on embedders that a given detector is intentionally not intended to recognize.

### 方法
A training framework is proposed that pairs a new detector with a sequence of frozen legacy embedders (its legacy chain), using a performance-weighted sampling strategy so that the detector retains accuracy across all earlier versions. The combined approach restores near-perfect TNR with no measurable cost to detection accuracy or perceptual audio quality.

### 实验/数据
未在摘要中明确给出。

### 结果
In real-world deployments, embedders and detectors are frequently updated and selectively decoupled for security and versioning purposes, which can break detection in previously embedded content and, more critically, increase false-positive rates on embedders that a given detector is intentionally not intended to recognize.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The combined approach restores near-perfect TNR with no measurable cost to detection accuracy or perceptual audio quality.

### 21. EliteReplay: Preserving Diverse Solutions in RL Post-Training via Quality-Diversity Search

- 作者：Hanane Nour Moussa, Doeun Lee, Sachin Kumar｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22290v1

### 背景/问题
Reinforcement learning has become a common post-training technique to improve the accuracy of LLMs on verifiable tasks. However, such training can narrow the set of solutions the model can produce.

### 方法
However, such training can narrow the set of solutions the model can produce. Several approaches have attempted to address this behavior-sharpening effect, but they often optimize metrics that do not reflect the diversity of correct solutions. Ideally, we want a model that can produce multiple good solutions, not only a single reliable one.

### 实验/数据
未在摘要中明确给出。

### 结果
Reinforcement learning has become a common post-training technique to improve the accuracy of LLMs on verifiable tasks. The result is a post-trained model that improves accuracy while preserving more of the base model's solution diversity. It preserves most of the base model's correct strategies, outperforming existing methods in strategy retention.

### 结论/启示（面向电商发券、定价、营销算法等应用）
This diversity translates into practical benefits on ambiguous questions, where EliteReplay covers both interpretations nearly twice as often as the strongest baseline on AmbiQT.

### 22. Extending Donaldson's HyperKähler Structure via Minimal Surfaces into $\mathrm{PSL}(2,\mathbb{C})$

- 作者：Christian El Emam, Filippo Mazzoli, Nicholas Rungi, Andrea Seppi, Andrea Tamburelli｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22288v1

### 背景/问题
We construct a deformation space for minimal immersions into $\mathrm{PSL}(2,\mathbb{C})$ with its holomorphic Killing form, and define an explicit, mapping class group invariant, complex hyperKähler structure on such deformation space. Such complex hyperKähler structure restricts to: Donaldson's hyperKähler structure on a totally real copy of almost-Fuchsian space, Mazzoli-Seppi-Tamburelli's para-hyperKähler structure on a totally real copy of maximally globally hyperbolic $\mathbb{A}\mathrm{d}\mathbb{S}^3$ manifolds, and Loustau-Sanders' complex bi-Kähler structure on a holomorphic copy of quasi-Fuchsian space.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We discuss other geometric aspects of this space, such as the Hamiltonian property of a natural $\mathbb{C}^*$-action, involving the Goldman symplectic form and a complex-valued area functional.

### 23. Subgraph Counting with Local Node Differential Privacy

- 作者：Sofya Raskhodnikova, Adam Smith, Connor Wagaman, Anatoly Zavyalov｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22278v1

### 背景/问题
We study the problem of approximately counting subgraphs under local node differential privacy (LNDP), a recently introduced model that enforces strong privacy guarantees in analyses of distributed social networks. We design a noninteractive $(\varepsilon,0)$-LNDP algorithm that, given any public $k$-node template graph $H$, counts occurrences of $H$ in a sensitive undirected $n$-node graph with additive error $O(n^{k-\frac{1}{2}}/\varepsilon^{k-1})$, for any constant $k$.

### 方法
We study the problem of approximately counting subgraphs under local node differential privacy (LNDP), a recently introduced model that enforces strong privacy guarantees in analyses of distributed social networks.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Previous separations either only involved $\mathrm{poly}(1/\varepsilon)$ factors or only applied to promise problems.

### 24. MJev-Spatial: System One Spatial Intelligence via Native Attention Matching

- 作者：Luozheng Qin, Yuhan Zhu, Changhai Zhou, Qian Qiao, Jun Gao, Yuhua Zhou, Harry Zhang, Xiangyu Zeng 等｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22276v1

### 背景/问题
Spatial intelligence lets an agent perceive and act in the physical world, and many of its judgments must be made at interaction rates: which spatial relation holds, how far an object is, or where to place it. Vision-language models (VLMs) produce these answers by free-form text generation, paying for autoregressive decoding and answer parsing even though the output space is compact: one of a few options, a scalar, or a 2D point.

### 方法
Vision-language models (VLMs) produce these answers by free-form text generation, paying for autoregressive decoding and answer parsing even though the output space is compact: one of a few options, a scalar, or a 2D point. In light of this, we introduce MJev-Spatial, a System 1 multimodal decision model that tackles all three types of spatial understanding tasks within a unified classification framework. Built on Qwen3.5-4B and trained on 12.3M question-answer pairs converted from existing spatial datasets, MJev-Spatial achieves the highest overall score (65.64%) among eight tested models, ranks first on seven of twelve benchmarks, and outperforms its unmodified autoregressive base model on all twelve, while running 2.5 times faster than the fastest autoregressive baseline and 5.6 times faster than the base model.

### 实验/数据
To train on heterogeneous spatial data efficiently, we supervise all coarse-to-fine stages jointly with teacher forcing in one forward pass, and combine this with length-aware global batching and cross-GPU load balancing, raising training throughput by 30.8% over the original batching strategy. Built on Qwen3.5-4B and trained on 12.3M question-answer pairs converted from existing spatial datasets, MJev-Spatial achieves the highest overall score (65.64%) among eight tested models, ranks first on seven of twelve benchmarks, and outperforms its unmodified autoregressive base model on all twelve, while running 2.5 times faster than the fastest autoregressive baseline and 5.6 times faster than the base model.

### 结果
Built on Qwen3.5-4B and trained on 12.3M question-answer pairs converted from existing spatial datasets, MJev-Spatial achieves the highest overall score (65.64%) among eight tested models, ranks first on seven of twelve benchmarks, and outperforms its unmodified autoregressive base model on all twelve, while running 2.5 times faster than the fastest autoregressive baseline and 5.6 times faster than the base model.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Built on Qwen3.5-4B and trained on 12.3M question-answer pairs converted from existing spatial datasets, MJev-Spatial achieves the highest overall score (65.64%) among eight tested models, ranks first on seven of twelve benchmarks, and outperforms its unmodified autoregressive base model on all twelve, while running 2.5 times faster than the fastest autoregressive baseline and 5.6 times faster than the base model.

### 25. Minimizing Age of Incorrect Information in Pull-Based Remote Estimation of a Markov Source

- 作者：Ismail Cosandal, Sennur Ulukus, Nail Akar｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22265v1

### 背景/问题
In this paper, we consider a discrete-time pull-based remote estimation system involving an information source and a remote monitor where the information source is a finite-state irreducible discrete-time Markov chain (DTMC) process. In this system, the remote monitor sends a pull request towards the source which responds by sampling its process so as to transmit the sampled values towards the monitor through a delay channel, encapsulated in information packets.

### 方法
For remote estimation, we use the maximum a posteriori (MAP) estimator, and for quantifying its performance, we use the mean age of incorrect information (MAoII) which is a recently proposed freshness and mismatch metric that penalizes an incorrect estimation along with its duration. For the ZD model, we propose a semi-Markov decision process (SMDP) formulation of the problem, which allows us to find the optimum observation-dependent pull policy. On the other hand, the UD channel prevents the monitor from possessing perfect information on the actual AoII process at any given time, and the SMDP formulation of the ZD channel cannot readily be used for the UD model.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Subsequently, we propose a belief-dependent policy obtained via the belief-MDP formulation and a constrained deep reinforcement learning (CDRL) algorithm.

### 26. Explore Once, Evaluate Many: Multiple Policy Evaluation for Stochastic Linear Bandits

- 作者：Spyros Dragazis, Yilei Chen, Aldo Pacchiano｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22252v1

### 背景/问题
We study how to evaluate $K$ target policies simultaneously in stochastic contextual bandits with linear reward structure. Given a known $d$-dimensional feature map and reward-free access to policy queries, we propose PRISMA (Policy evaluation through Regularized Information Sharing and Mixture Allocation), an algorithm that estimates every target policy's value to accuracy $\varepsilon$ with probability at least $1-δ$.

### 方法
Given a known $d$-dimensional feature map and reward-free access to policy queries, we propose PRISMA (Policy evaluation through Regularized Information Sharing and Mixture Allocation), an algorithm that estimates every target policy's value to accuracy $\varepsilon$ with probability at least $1-δ$. Our method combines reward-free planning, a regularized sampling design, and a single ridge regression estimator shared across all target policies.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Policy-query costs are accounted for separately, with $K$ queries per shared planning context.

### 27. Tree Edit Distance: Near-Linear-Time Approximate, Sublinear, and Dynamic

- 作者：Bingbing Hu, Tomasz Kociumaka, Jakob Nogler, Barna Saha｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22250v1

### 背景/问题
Tree edit distance (TED), the analog of string edit distance (ED) for hierarchical data, is the minimum number of node insertions, deletions, and substitutions transforming one labeled rooted ordered tree into another. We narrow polynomial gaps between TED and ED in near-linear-time approximation, sublinear algorithms, and dynamic algorithms.

### 方法
It combines structural properties previously achieved only in isolation, providing a framework for transferring algorithmic ideas from ED to TED, with additional ingredients addressing the obstacles in each computational setting.

### 实验/数据
Tree edit distance (TED), the analog of string edit distance (ED) for hierarchical data, is the minimum number of node insertions, deletions, and substitutions transforming one labeled rooted ordered tree into another.

### 结果
This improves the previous near-linear-time $O(\sqrt n)$-approximation [Boroujeni et al., STOC'19] and brings TED to parity with ED in this regime up to polylogarithmic factors. The approximation improves prior dynamic guarantees [Das et al., FOCS'25] and cannot be significantly improved in any parameter regime without a breakthrough for static $(1+\varepsilon)$-approximation of ED.

### 结论/启示（面向电商发券、定价、营销算法等应用）
It combines structural properties previously achieved only in isolation, providing a framework for transferring algorithmic ideas from ED to TED, with additional ingredients addressing the obstacles in each computational setting.

### 28. Language Is a Security Surface for Agent Guards

- 作者：Hasan Demirkiran, Jens Ernstberger｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22244v1

### 背景/问题
Step-level guards decide, before each tool call, whether an agent's next action is safe given the user's request and the trajectory so far. Users write those requests in many languages, while guard prompts and the benchmarks on which purpose-built guards are trained and evaluated are English.

### 方法
Across 19 guards, from frontier APIs to 4B open models and four purpose-built agent guards, most open, small and purpose-built guards change verdicts under translation beyond their own noise floor, and the effect grows with the rarity of the language: among the nine guards below 13B parameters, the mean placebo-adjusted flip rate rises from +1.5 pp on French to +4.4 pp on Amharic.

### 实验/数据
未在摘要中明确给出。

### 结果
The direction of the damage tends to follow guard size: open guards of 12-30B parameters block more benign steps (up to +5.0 pp false positives), and every significant loss of recall is in a guard below 10B (up to -7.4 pp).

### 结论/启示（面向电商发券、定价、营销算法等应用）
We release the benchmark and all 489k verdicts.

### 29. Shortcut Sensitivity in Agent-Safety Evaluations

- 作者：Hasan Demirkiran, Jens Ernstberger｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22243v1

### 背景/问题
AI agents take actions through tools. Some actions are sensitive, so guards that supervise them must themselves be evaluated reliably.

### 方法
We introduce a three-level shortcut-auditing framework and audit completed LinuxArena trajectories and two TS-Bench-derived step datasets.

### 实验/数据
Yet the data used to evaluate a guard can include cues that make labels predictable without measuring the intended safety construct, and those cues can also influence guard decisions. We introduce a three-level shortcut-auditing framework and audit completed LinuxArena trajectories and two TS-Bench-derived step datasets.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We recommend domain group holdouts, evaluation-unit metrics, and placebo-controlled paired interventions.

### 30. SurvICL: a Foundation Model for in-context Survival Analysis

- 作者：Julie Alberge, Linus Bleistein, Judith Abécassis, Marine Le Morvan, Gaël Varoquaux, David Holzmüller｜年份：2026｜发布时间：2026-10-15｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.22242v1

### 背景/问题
Tabular foundation models (TFMs) now outperform gradient-boosted trees in classification and regression. Yet in survival analysis, which predicts when an event occurs from censored data, often on small clinical cohorts, we find that no existing TFM beats the half-century-old Cox model.

### 方法
Tabular foundation models (TFMs) now outperform gradient-boosted trees in classification and regression. Yet in survival analysis, which predicts when an event occurs from censored data, often on small clinical cohorts, we find that no existing TFM beats the half-century-old Cox model. Unlike most other survival models, SurvICL is trained with a plain quantile regression loss, which is possible because its synthetic pre-training data generator can provide uncensored event times.

### 实验/数据
Yet in survival analysis, which predicts when an event occurs from censored data, often on small clinical cohorts, we find that no existing TFM beats the half-century-old Cox model. SurvICL is pretrained on purely synthetic datasets generated from a novel flexible proportional-odds prior that outperforms other prior types in our ablation study. Unlike most other survival models, SurvICL is trained with a plain quantile regression loss, which is possible because its synthetic pre-training data generator can provide uncensored event times.

### 结果
Tabular foundation models (TFMs) now outperform gradient-boosted trees in classification and regression. SurvICL is pretrained on purely synthetic datasets generated from a novel flexible proportional-odds prior that outperforms other prior types in our ablation study. On the 63 datasets held out from all design decisions, SurvICL outperforms 20 tree-based, deep, and foundation-model baselines without any tuning: it wins 82.9\% of pairwise comparisons in integrated Brier score, against 71.3\% for the runner-up, the Cox model, and is the first model to rank above Cox on small datasets.

### 结论/启示（面向电商发券、定价、营销算法等应用）
On the 63 datasets held out from all design decisions, SurvICL outperforms 20 tree-based, deep, and foundation-model baselines without any tuning: it wins 82.9\% of pairwise comparisons in integrated Brier score, against 71.3\% for the runner-up, the Cox model, and is the first model to rank above Cox on small datasets.
