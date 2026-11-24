# CausalRadar 日报 - 2026-11-24

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Head Anything: Correspondence-Guided Joint Generation of 3D Heads from Few Images

- 作者：Umut Kocasari, Bartłomiej Baranowski, Richard Shaw, Eduardo Pérez-Pellitero, Matthias Nießner｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**9.00**
- 链接：https://arxiv.org/abs/2611.31143v1

> 命中：hit_scenario=['ads']；hit_title=['ads']

### 背景/问题
Large image-to-3D generators recover detailed heads from a single photograph but treat every image as a new object. For several images of one person, they hallucinate unseen regions independently without using information from the other images.

### 方法
We present Head Anything, which generates detailed head meshes from a few images with changing expressions and viewpoints. We obtain correspondences by fitting a neural parametric head model to the generator's own single-image outputs, requiring no ground truth at test time. Code and models will be released.

### 实验/数据
Since global attention between images is hard to learn from scarce 3D head data, lightweight correspondence-attention adapters let every 3D token attend only to its corresponding points in the other images.

### 结果
On head scans, Head Anything lowers the head Chamfer distance of the best image-to-3D generator by 32% and its cross-frame inconsistency by 47%, and its meshes improve face tracking.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Code and models will be released.

### 2. Pruning Autonomous Driving VLAs: What to Preserve for Reasoning and Action

- 作者：Seongchan Kim, Soowon Son, Sangoh Kim, Hyunah Ko, Eunbeen Hong, Hyunkoo Lee, Sanghyun Lee, WonJun Moon 等｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.31240v1

> 命中：hit_scenario=['ads']

### 背景/问题
Reasoning vision-language-action (VLA) models for autonomous driving use chain-of-thought (CoT) reasoning to guide action generation, but incur substantial memory and computational costs. We study structured pruning for these models, focusing on preserving both scene understanding and trajectory prediction.

### 方法
Reasoning vision-language-action (VLA) models for autonomous driving use chain-of-thought (CoT) reasoning to guide action generation, but incur substantial memory and computational costs. We study structured pruning for these models, focusing on preserving both scene understanding and trajectory prediction. Our analysis of Taylor importance in Alpamayo-1.5-10B shows that reasoning and trajectory objectives assign different importance to the same vision-language model (VLM) structures.

### 实验/数据
未在摘要中明确给出。

### 结果
At 24.0% total parameter reduction, VLM-only pruning with MoOP performs comparably to or slightly better than the strongest baselines in driving, while retaining 94.0% of the dense model's LingoQA score, far above all other methods. Removing 93.75% of expert MLP channels increases total parameter reduction to 39.4%, with nearly unchanged open-loop errors relative to VLM-only pruning and competitive closed-loop performance.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The resulting model achieves a 1.37x end-to-end inference speedup and 36.6% lower peak memory than the dense model, without post-pruning fine-tuning.

### 3. Topological Fairness in Continuous-State Systems

- 作者：Mahdi Nazeri, Alessandro Abate, Anne-Kathrin Schmuck, Sadegh Soudjani｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.31150v1

> 命中：hit_scenario=['ads']

### 背景/问题
Since the early days of probabilistic programs, fairness has been used to abstract randomness in software. Intuitively, a fair scheduler reproduces the almost-sure behavior of a random choice based solely on the set of possible outcomes, independent of their (often unknown) distribution.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our case studies show that this winning domain is substantially larger than the one obtained with currently available techniques, which detour through a finite abstraction and certify a winning domain that depends on the discretization in a non-monotone way.

### 4. Verifying the Outputs of PDE Solvers: From Finite Elements to Neural Surrogates

- 作者：Konstantinos Dovelos｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.31211v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Physics simulation outputs increasingly come from solvers that no expert inspects, such as third-party packages in automated pipelines, programs written by large language models (LLMs), and learned surrogates. In earlier work on cardiac pulsed field ablation, we proposed that solvers return a certificate with their answers.

### 方法
Physics simulation outputs increasingly come from solvers that no expert inspects, such as third-party packages in automated pipelines, programs written by large language models (LLMs), and learned surrogates. In earlier work on cardiac pulsed field ablation, we proposed that solvers return a certificate with their answers. The guarantee concerns the stated model and holds for any output, wherever its input lies.

### 实验/数据
Physics simulation outputs increasingly come from solvers that no expert inspects, such as third-party packages in automated pipelines, programs written by large language models (LLMs), and learned surrogates. In earlier work on cardiac pulsed field ablation, we proposed that solvers return a certificate with their answers. Specifically, FEniCSx computes both fields and receives the same bounds as our own solver.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
It is informative only when the output is accurate in energy on a grid that resolves the problem.

### 5. ACAP: Asynchronous Coding Agents for Efficient Robot Control

- 作者：Zexin He, Rui Li, Yushi Lan, Chengkai Jin, Zhi Hou, Xingang Pan｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.31205v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Coding agents can construct and revise robot behavior during execution, but using one agent for the whole robot can delay otherwise independent work. We introduce Asynchronous Coding Agents as Policy (ACAP), an asynchronous framework that organizes one robot as a team of persistent agents.

### 方法
We introduce Asynchronous Coding Agents as Policy (ACAP), an asynchronous framework that organizes one robot as a team of persistent agents. We present the framework and a real-world rollout dataset containing observations, generated programs, actions, and feedback to support research on how coding agents reason and act in the physical world.

### 实验/数据
We present the framework and a real-world rollout dataset containing observations, generated programs, actions, and feedback to support research on how coding agents reason and act in the physical world.

### 结果
Across 72 real-world rollouts covering 25 task/platform settings, ACAP reduces task-balanced time cost by 28.2% compared with a single-agent Direct Policy, with improvements across Fully Parallel, Parallel-Sequential, and Collaborative tasks.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We present the framework and a real-world rollout dataset containing observations, generated programs, actions, and feedback to support research on how coding agents reason and act in the physical world.

### 6. TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming

- 作者：Hani Alomari, Md Atabuzzaman, Chris Thomas｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31233v1

### 背景/问题
CLIP-style dual encoders map images and text through two separate towers into a shared embedding space, where the two modalities occupy distinct regions separated by a modality gap. Retrieval fails when wrong matches, or hard negatives, outrank the correct one, and the gap is the usual suspect.

### 方法
Computed in seconds from 25,000 labelled pairs, it requires no model-specific tuning and leaves the architecture and inference cost unchanged.

### 实验/数据
未在摘要中明确给出。

### 结果
Mildly attenuating these directions improves retrieval while largely preserving the gap. Free to edit any component, the agent improves COCO test retrieval on all 13 CLIP checkpoints and edits an output projection in 12 of the 13. TowerBridge improves COCO test retrieval by 16.8 RSUM and Flickr30k test retrieval by 6.6 on average across all 21 evaluated CLIP checkpoints, including 8 unseen by the agent, while limiting any drop in ImageNet zero-shot accuracy to 0.5 points.

### 结论/启示（面向电商发券、定价、营销算法等应用）
It also reduces hubness on all 21 checkpoints and improves retrieval on 4 of 5 dual encoders from other families.

### 7. Euclid Data Release 1 (DR1). Learning machine learning: Investigating the complementarity and biases of strong gravitational lens finding networks on Euclid data

- 作者：Euclid Collaboration, S. H. Vincken, N. E. P. Lines, S. Schuldt, P. Holloway, T. E. Collett, M. Fogliardi, A. Manjón-García 等｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31231v1

### 背景/问题
The Euclid Data Release 1 (DR1) strong lens search presents ECLIPSE, the largest catalogue of strong gravitational lens candidates to date, with >15 000 systems identified across 1900 deg2 of sky. It was constructed using five neural networks applied to approximately 68 million galaxies, followed by citizen science and expert visual inspection.

### 方法
In this work, we compare how the independently developed networks use image information to identify their selection of strong lens candidates.

### 实验/数据
The Euclid Data Release 1 (DR1) strong lens search presents ECLIPSE, the largest catalogue of strong gravitational lens candidates to date, with >15 000 systems identified across 1900 deg2 of sky. The search combines convolutional neural networks and a vision transformer, using the same pool of data but with different image processing and training choices. The results inform how networks should be combined in future Euclid data releases and upcoming wide-field surveys such as LSST or Roman to maximise both completeness and diversity of the recovered lens population.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The results inform how networks should be combined in future Euclid data releases and upcoming wide-field surveys such as LSST or Roman to maximise both completeness and diversity of the recovered lens population.

### 8. Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ

- 作者：Daniel Theron｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31228v1

### 背景/问题
Prompting language models to verbalize stepwise numerical confidence during generation is an increasingly popular approach for triggering backtracking and error correction in agentic reasoning. This strategy presupposes two capabilities: (1) in-situ monitoring fidelity (does confidence drop when an error occurs?) and (2) downstream steering control (does an uncertainty token causally steer the model to repair its error?).

### 方法
Prompting language models to verbalize stepwise numerical confidence during generation is an increasingly popular approach for triggering backtracking and error correction in agentic reasoning. This strategy presupposes two capabilities: (1) in-situ monitoring fidelity (does confidence drop when an error occurs?) and (2) downstream steering control (does an uncertainty token causally steer the model to repair its error?). We evaluated four open-weights models (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B, and Phi-4, 14.7B) across 15,200 math benchmark attempts, isolating 2,017 reasoning errors within each model's capability frontier.

### 实验/数据
未在摘要中明确给出。

### 结果
In contrast, models respond readily to external uncertainty: injecting a low-confidence tag (10%) at the error step significantly increases downstream correction across all models (+3.7 to +22.5 points over format-matched 95% certainty; all $p \le 0.0022$), reaching up to 38.5% under active rethinking instructions.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Inference-time self-correction is thus bottlenecked by in-situ error detection rather than downstream repair capacity: models readily steer toward recovery when prompted with doubt, yet fail to self-monitor during generation.

### 9. Self-Supervised Dataset Distillation via Mutual Information Maximization

- 作者：Mohammad Hossein Moslemi, Mahdi Beitollahi, Zhimin Mei, Jiale Cai, Bissan Ghaddar, Boyu Wang｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31225v1

### 背景/问题
Dataset distillation (DD) aims to compress a large dataset into a small synthetic one that remains effective for training neural networks. Despite its success in supervised learning, DD remains underexplored in self-supervised learning (SSL), where distilled data must preserve the information needed to learn representations that remain consistent across augmentations.

### 方法
To bridge this gap, we introduce Mutual Information Prototype Alignment (MIPA), an efficient SSL dataset distillation approach that optimizes synthetic images to preserve augmentation-invariant information. Evaluations on image classification benchmarks show that synthetic data generated by MIPA yield higher-quality representations than existing distillation approaches while reducing time and storage demands during distillation.

### 实验/数据
Dataset distillation (DD) aims to compress a large dataset into a small synthetic one that remains effective for training neural networks. Despite its success in supervised learning, DD remains underexplored in self-supervised learning (SSL), where distilled data must preserve the information needed to learn representations that remain consistent across augmentations. To bridge this gap, we introduce Mutual Information Prototype Alignment (MIPA), an efficient SSL dataset distillation approach that optimizes synthetic images to preserve augmentation-invariant information.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Evaluations on image classification benchmarks show that synthetic data generated by MIPA yield higher-quality representations than existing distillation approaches while reducing time and storage demands during distillation.

### 10. CTLink: A Text-Prompted Segmentation Model for Linking Radiology Report Findings to 3D Chest CT Scans

- 作者：Mohammed Baharoon, Sung Eun Kim, Mahmoud Hussain Alabbad, Lucas Bijnens, Ali Piracha, Reem Alwasiah, Talal Yahyan, Abdulrahman Alamoudi 等｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31222v1

### 背景/问题
Radiology reports describe findings in text only, without visually marking them on the scan, so readers cannot directly see which abnormality each reported finding refers to. We introduce CTLink, a text-prompted 3D segmentation model that segments findings described in a chest CT report.

### 方法
We introduce CTLink, a text-prompted 3D segmentation model that segments findings described in a chest CT report. On the 200 ReXGroundingCT validation scans, CTLink achieved a hit rate of 0.816, an instance F1 score of 0.456, and a mean Dice score of 0.400, compared with 0.533, 0.175, and 0.234 for VoxTell, a publicly available text-prompted segmentation model (P < .001 for all). On the test set of the MICCAI 2026 ReXGrounding challenge, an ensemble of seven CTLink models achieved the highest hit rate (0.782) and instance F1 score (0.386) of all 48 participating teams.

### 实验/数据
CTLink was trained on 4123 noncontrast chest CT scans with 9547 segmented report findings, including ReXGroundingCTv2, a newly annotated dataset of 1134 scans and 1895 findings with every instance of each finding segmented. The CTLink model weights are available at https://huggingface.co/rajpurkarlab/CTLink, and the dataset at https://huggingface.co/datasets/rajpurkarlab/ReXGroundingCT.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The CTLink model weights are available at https://huggingface.co/rajpurkarlab/CTLink, and the dataset at https://huggingface.co/datasets/rajpurkarlab/ReXGroundingCT.

### 11. Matching Under Metric Privacy

- 作者：Hongyi B. Hu, Dung Nguyen, M. Amin Rahimian｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31208v1

### 背景/问题
We study how to represent and randomize points in $d$-dimensional Euclidean space to obtain accurate bipartite matchings under metric privacy. Given $n$ private and $n$ public points, we analyze local mechanisms that randomize each private point or its distances to the public points.

### 方法
These results show how the application's trust model guides representation and dimension choices for better utility: under local privacy, low-dimensional point representations reduce excess cost, while under central privacy, distance representations achieve the optimal rate even in high dimension.

### 实验/数据
Benchmark experiments support $d\approx\log n$ as a practical guide to the transition between directly randomizing point coordinates and using Gumbel matching.

### 结果
These results show how the application's trust model guides representation and dimension choices for better utility: under local privacy, low-dimensional point representations reduce excess cost, while under central privacy, distance representations achieve the optimal rate even in high dimension.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results show how the application's trust model guides representation and dimension choices for better utility: under local privacy, low-dimensional point representations reduce excess cost, while under central privacy, distance representations achieve the optimal rate even in high dimension.

### 12. Solute-Aware Stochastic Korhonen Model of Electromigration in Wide vs Near-Bamboo Al-Cu Lines

- 作者：Narahara Chari Dingari, David R. Heskett｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31206v1

### 背景/问题
We couple an evolving Cu field to the one-dimensional Korhonen stress equation on random grain maps for wide (10 $μ$m), narrow (3 $μ$m) and near-bamboo Al-Cu lines. Earlier random-microstructure simulations fixed the Cu effect, and most continuum solute models used prescribed structures with all Cu mobile; we join the two and let only dissolved Cu move, the excess staying as immobile precipitate.

### 方法
Earlier random-microstructure simulations fixed the Cu effect, and most continuum solute models used prescribed structures with all Cu mobile; we join the two and let only dissolved Cu move, the excess staying as immobile precipitate. At the test durations the model qualitatively matches the cathode-side damage in narrow lines and the Cu build-up and mid-line peaks in wide lines but not the cathode-side Cu peaks or longer lives of narrow lines.

### 实验/数据
We couple an evolving Cu field to the one-dimensional Korhonen stress equation on random grain maps for wide (10 $μ$m), narrow (3 $μ$m) and near-bamboo Al-Cu lines. Earlier random-microstructure simulations fixed the Cu effect, and most continuum solute models used prescribed structures with all Cu mobile; we join the two and let only dissolved Cu move, the excess staying as immobile precipitate.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
At the test durations the model qualitatively matches the cathode-side damage in narrow lines and the Cu build-up and mid-line peaks in wide lines but not the cathode-side Cu peaks or longer lives of narrow lines.

### 13. JAISP: A Joint Rubin-Euclid Foundation Model for Cross-Instrument Source Detection and Astrometry

- 作者：Shoubaneh Hemmati, George Helou, Yu-Heng Lin, Rachel Akeson, Charles Darren Dowell, Andreas Faisst, Thomas Greene, David Shupe｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31204v1

### 背景/问题
Joint pixel-level processing of Rubin and Euclid imaging promises deeper source detection and the cross-survey consistency that precision cosmology requires. We introduce JAISP (Joint AI Survey Processing), a foundation model that learns a single representation of ten-band imaging: Rubin ugrizy and Euclid VIS, Y, J, and H, from the first public releases over $\approx 0.2$ deg$^2$ of the ECDFS deep field.

### 方法
We introduce JAISP (Joint AI Survey Processing), a foundation model that learns a single representation of ten-band imaging: Rubin ugrizy and Euclid VIS, Y, J, and H, from the first public releases over $\approx 0.2$ deg$^2$ of the ECDFS deep field.

### 实验/数据
We introduce JAISP (Joint AI Survey Processing), a foundation model that learns a single representation of ten-band imaging: Rubin ugrizy and Euclid VIS, Y, J, and H, from the first public releases over $\approx 0.2$ deg$^2$ of the ECDFS deep field. Separating this per-source scatter exposes the cross-survey concordance field: a coherent $9$--$10$ mas offset between the two independently Gaia-registered astrometric solutions, dominated by a component common to all bands. Applied without retraining to a second Euclid Deep Field, both networks perform without measurable loss.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
A single representation learned once from survey pixels thus serves several measurements across the sky.

### 14. On the existence of constants of motion for multipolar test-body dynamics

- 作者：Paul Ramond｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31200v1

### 背景/问题
We show that the conservative equations of motion of an extended test body, with force and torque sourced by spin-induced and adiabatic tidal multipoles of arbitrary order, are the flow of the Hamiltonian $H=-\tfrac12μ^2+μU$, where $μ$ is the body's kinematic mass and all multipoles enter through a covariant scalar potential $U$. For such bodies, a certain notion of mass and a spin norm are shown to be exactly conserved, at all multipolar orders and in any background.

### 方法
We then apply our framework to the Kerr spacetime, and construct extensions of the Carter and Rüdiger constants through hexadecapolar order (quartic in spin).

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In the conservative, test-body limit, black-hole binaries thus carry a dynamical hidden symmetry shared by no other compact objects, which persists to high multipolar order but ultimately breaks.

### 15. Know When to Abstain: Conformal Confidence Estimation for Text-to-SQL

- 作者：Avinash Kumar Singh, Bhaskarjit Sarmah, Stefano Pasquali｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31190v1

### 背景/问题
Text-to-SQL systems often return queries that execute successfully but answer the wrong question. Detecting these errors at deployment is hard because execution correctness is defined against a gold query, which exists only in labeled data.

### 方法
Five different critic models give similar results.

### 实验/数据
Detecting these errors at deployment is hard because execution correctness is defined against a gold query, which exists only in labeled data.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Applied to BIRD without retraining, the confidence scores remain informative (AUROC 0.72, against 0.79 on Spider), but the risk guarantee does not transfer, as expected without exchangeability.

### 16. Self-guided estimation of the stabilizer fidelity with single-copy Pauli measurements

- 作者：M. Torres, J. Gidi, L. Pereira｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31186v1

### 背景/问题
The stabilizer fidelity quantifies the non-stabilizerness of pure states, but it is hard to estimate because it requires optimizing over $2^{O(n^2)}$ stabilizer states for $n$ qubits. Here, we propose a self-guided estimation protocol for the stabilizer fidelity of an unknown state, pure or mixed, which requires only Pauli measurements on single copies.

### 方法
Here, we propose a self-guided estimation protocol for the stabilizer fidelity of an unknown state, pure or mixed, which requires only Pauli measurements on single copies.

### 实验/数据
In numerical simulations of up to 14 qubits, the protocol reached the optimum in all runs, with the number of iterations remaining small and increasing only slightly with $n$.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In numerical simulations of up to 14 qubits, the protocol reached the optimum in all runs, with the number of iterations remaining small and increasing only slightly with $n$.

### 17. CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting

- 作者：Ramraj Chandradevan, Sayontan Ghosh, Vinoth Selvendran｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31185v1

### 背景/问题
Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-GRAFT, a reward-agnostic interventional attribution framework in which an RL-trained agent and its pre-RL initialization jointly generate a single trajectory under closed-loop execution with live retrieval.

### 方法
Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-GRAFT, a reward-agnostic interventional attribution framework in which an RL-trained agent and its pre-RL initialization jointly generate a single trajectory under closed-loop execution with live retrieval. Applying CO-GRAFT to Search-R1 agents across Qwen2.5 and Llama-3.2 models (spanning two sizes, base and instruction-tuned initializations, GRPO and PPO optimizers, and NQ and HotpotQA datasets), we show that query generation never exceeds 15% of the total gain; instead, gains are governed by pre-RL answer validity, search retention, model scale, and fixed task-level search budgets, shifting credit from reasoning toward answer extraction in larger or well-formatted answer response checkpoints while smaller base models rely on reasoning--decision coupling.

### 实验/数据
Applying CO-GRAFT to Search-R1 agents across Qwen2.5 and Llama-3.2 models (spanning two sizes, base and instruction-tuned initializations, GRPO and PPO optimizers, and NQ and HotpotQA datasets), we show that query generation never exceeds 15% of the total gain; instead, gains are governed by pre-RL answer validity, search retention, model scale, and fixed task-level search budgets, shifting credit from reasoning toward answer extraction in larger or well-formatted answer response checkpoints while smaller base models rely on reasoning--decision coupling.

### 结果
Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. Evaluating all 2^4=16 role assignments without modifying weights or retraining defines a cooperative game whose Shapley values decompose the total RL gain across roles, while M"obius interaction terms distinguish standalone role improvements from multi-role coupling.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Applying CO-GRAFT to Search-R1 agents across Qwen2.5 and Llama-3.2 models (spanning two sizes, base and instruction-tuned initializations, GRPO and PPO optimizers, and NQ and HotpotQA datasets), we show that query generation never exceeds 15% of the total gain; instead, gains are governed by pre-RL answer validity, search retention, model scale, and fixed task-level search budgets, shifting credit from reasoning toward answer extraction in larger or well-formatted answer response checkpoints while smaller base models rely on reasoning--decision coupling.

### 18. On-Policy Codec Distillation for Efficient All-in-One Video Generation

- 作者：Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha, Matheus Gadelha, Zezhou Cheng｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31184v1

### 背景/问题
Modern visual generative models operate on tokens, and every visual asset they receive, whether an identity, a scribble, a depth map, or a motion video, is tokenized and appended to the input token sequence. Consequently, conditioning quickly dominates the computation cost.

### 方法
Modern visual generative models operate on tokens, and every visual asset they receive, whether an identity, a scribble, a depth map, or a motion video, is tokenized and appended to the input token sequence. Our key insight is that identifying what is genuinely new is exactly the problem that classical video codecs have long solved. Then, we propose an on-policy self-distillation (OPSD) strategy to train a DiT adapter capable of learning the codec pruning pattern well without quality degradation.

### 实验/数据
未在摘要中明确给出。

### 结果
CodecOPSD also extends to other state-of-the-art pretrained image and video generative models, where its benefit grows further with more conditions, longer frames, and higher resolution.

### 结论/启示（面向电商发券、定价、营销算法等应用）
CodecOPSD also extends to other state-of-the-art pretrained image and video generative models, where its benefit grows further with more conditions, longer frames, and higher resolution.

### 19. Weighted Bergman projection in radial trees

- 作者：Nikolaos Chalmoukis, Matteo Monti｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31182v1

### 背景/问题
We study the Bergman projection $P_ω$ on a radial tree with respect to weighted harmonic Bergman spaces $A^p_ω$, where $ω$ is a positive radial weight. We prove that for all such weights and $1<p<\infty $, the Bergman projection $P_ω$ is bounded from $L^p(ω) $ to $A^p_ω$ and $L^\infty \to \mathcal{B} $, where $\mathcal{B} $ is the Bloch space of the tree.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, in the appendix, we provide an elementary proof of the characterization of the weights $Ω\in L^1(\mathbb{D}) $ for which the Bergman projection from $L^p(Ω) $ to the holomorphic Bergman space $A^p_Ω(\mathbb{D}) $.

### 20. Probabilistic, facility-specific prioritisation of temperate exoplanets for atmospheric characterisation with JWST and the ELT

- 作者：Effy Viridis｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31181v1

### 背景/问题
Deciding which temperate exoplanets to observe first matters for JWST transit spectroscopy and for planned ELT reflected-light instruments, yet signal-to-noise metrics ignore habitability and similarity indices ignore observability. We present an open Monte Carlo framework (UHI v6.1) that builds probabilistic priority lists separately for each facility and composition class, never as a single ranking.

### 方法
We present an open Monte Carlo framework (UHI v6.1) that builds probabilistic priority lists separately for each facility and composition class, never as a single ranking. For each of 6,112 planets in the NASA Exoplanet Archive, 10,000 draws carry catalogue uncertainties through climate, cumulative stellar-XUV atmospheric retention, per-draw rocky, Hycean or gas-rich classes, and a JWST (transiting) or ELT/PCS (non-transiting) detection model, giving each planet a survival probability, a conditional score and a top-N probability.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Code, per-planet posterior summaries, sensitivity tables and maps are public, so observers can rerun the lists under their own instrument assumptions and see which inputs would most change a target's priority.

### 21. Polynomial mixing for 2D Ising with plus boundary conditions

- 作者：Shirshendu Ganguly, Reza Gheissari｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31180v1

### 背景/问题
We study the Glauber dynamics of the 2D Ising model at low temperatures. In the absence of boundary conditions, the mixing time on an $n\times n$ box is exponential in $n$ due to a bottleneck between metastable plus and minus phases.

### 方法
We study the Glauber dynamics of the 2D Ising model at low temperatures. In simpler models of height functions, polynomial bounds tend to rely on exact harmonic properties and connections to a discrete heat equation. We address this via a new multiscale approach to bound mixing times of general disordered random-walk bridges that homogenize to a Brownian bridge at mesoscopic scales.

### 实验/数据
On the rigorous side, the strongest result was a quasi-polynomial mixing time upper bound due to Lubetzky, Martinelli, Sly and Toninelli (2013); a proof of polynomial mixing remained one of the major challenges in the field.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Another notable ingredient is a novel application of censoring to reduce the mixing time problem to proving only a weak Poincaré inequality, or warm-start mixing bound, allowing us to assume suitable regularity conditions on the interface and bubbles.

### 22. Floquet spectra and parameter sensitivity of entanglement in the quantum kicked top

- 作者：Dyari Jarvis, Peter A. Rose, Arjendu K. Pattanayak｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31179v1

### 背景/问题
We investigate the relationship between the Floquet spectrum and the sensitivity of the entanglement landscape to parameter and initial condition change in the quantum kicked top. We focus on the case of four qubits and on locating degeneracies in its Floquet eigenphases using the resultant of its characteristic polynomial $p$ and its derivative $\partial_λp$ and quantitatively map the sensitivity of the entanglement landscape to changes in kicking strength over the sphere of spin coherent initial states.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Since this structure extends to all values of $j$, the central lessons apply completely generally.

### 23. Code-Based Message Authentication with Statistical Guarantees via Coordinate Selection and Masking

- 作者：Hsuan-Po Liu, Hessam Mahdavifar｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31178v1

### 背景/问题
We study message authentication over a public channel against a computationally unbounded adversary. Motivated by low-complexity applications, we consider schemes that leverage off-the-shelf binary linear codes already used for error correction in communication systems.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we evaluate first-order Reed-Muller and Bose-Chaudhuri-Hocquenghem dual subcodes.

### 24. Precision-Aware Learning Rate Transfer Across Block Count in LLM Post-Training

- 作者：Nan Chen, Soledad Villar, Soufiane Hayou｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31166v1

### 背景/问题
The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very sensitive to the learning rate, and tuning it through grid search is costly in both computation and memory. In this work, we propose \textbf{TipSweep}, a method to transfer the learning rate across the number of trainable transformer blocks.

### 方法
The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very sensitive to the learning rate, and tuning it through grid search is costly in both computation and memory. In this work, we propose \textbf{TipSweep}, a method to transfer the learning rate across the number of trainable transformer blocks. Across experiments with models ranging from 1 to 7 billion parameters, we observe that the optimal learning rate follows precision-dependent scaling rules: the optimal rate scales approximately as $k^{-1}$ with float32 (FP32) master weights, but as $k^{-1/2}$ when updates are applied directly to bfloat16 (BF16) weights without a master copy.

### 实验/数据
To do so efficiently, we search for the best learning rate by training only the last $k_0$ blocks (in our experiments, typically $k_0=1$), and provide scaling rules that predict the optimal learning rate when training any set of $k$ blocks, including when $k=L$ (the full transformer). Across experiments with models ranging from 1 to 7 billion parameters, we observe that the optimal learning rate follows precision-dependent scaling rules: the optimal rate scales approximately as $k^{-1}$ with float32 (FP32) master weights, but as $k^{-1/2}$ when updates are applied directly to bfloat16 (BF16) weights without a master copy. We explain both rules using an analytical model that accounts for update rounding, under assumptions supported by profiling experiments.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The second speeds up the search on a high-end GPU by evaluating all candidate learning rates in a single pass over the data, so that a five-candidate search takes about half the GPU hours of one full-depth ($k=L$) run.

### 25. SPROUT: Predicting Objective-Grounded Prompt Utility for Efficient Text-to-Image Preference Tuning

- 作者：Kangping Hu, Akshay Mehra, Stephen Mussmann｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31163v1

### 背景/问题
Preference tuning of text-to-image diffusion models spends most of its compute generating candidate images, yet training prompts are typically sampled uniformly at random, wasting compute generating images that provide too little signal for model alignment. To best utilize the available compute, we study prompt selection, where at each iteration we identify the most useful prompts for preference tuning.

### 方法
Preference tuning of text-to-image diffusion models spends most of its compute generating candidate images, yet training prompts are typically sampled uniformly at random, wasting compute generating images that provide too little signal for model alignment. To best utilize the available compute, we study prompt selection, where at each iteration we identify the most useful prompts for preference tuning. Within this framework, we propose Selection by PRedicting Objective-grounded UTility (SPROUT).

### 实验/数据
未在摘要中明确给出。

### 结果
Fine-tuning Stable Diffusion 1.5 with DGPO on GenEval, SPROUT matches the final score of uniform sampling in about 44% of the iterations and improves the area under the learning curve with respect to both uniform sampling and CGPO, a recent variance-based prompt sampler.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our code is available at https://github.com/ADDAPT-ML/SPROUT.

### 26. Geometry, Reliability, and Spacetime Dynamics of Hyper-Simplex Fractal Networks

- 作者：Hao Xu, Kaiwen Yang, Jiacheng Qian, Yinuo Liu, Chih-Lin I｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31161v1

### 背景/问题
Large-scale, delay-tolerant peer-to-peer networks that need strong consistency usually separate naming, routing, consensus, and ordering into independent layers. To bring deterministic network properties into complex peer-to-peer structures, we unify all four on a single recursive topology.

### 方法
Modeling mutual equality among N peers in Euclidean space requires dimension at least N-1, which prevents flat equal groups from scaling at fixed dimension.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Reversible topology edits generate the Higman-Thompson group V_N on the address boundary, block order characterizes service-topology hosting beyond treewidth, and root-anchored block heights yield persistent spacetime coordinates with compact light-client proofs.

### 27. Reducing RSA-2048 Factoring Resources Below One Billion Toffolis via LLM-Driven Verifiable Quantum Compilation

- 作者：Xiaodi Li, Yuqing Wang, Xue Chen, Yang-Yang Tang, Linghui Chen, Tao Zhang｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31158v1

### 背景/问题
Modular exponentiation dominates the logical cost of factoring 2048-bit RSA integers (RSA-2048) with Shor's algorithm. Recent approaches based on approximate residue number systems (RNS) sharply reduce the required logical qubits, yet still demand billions of Toffoli gates.

### 方法
Recent approaches based on approximate residue number systems (RNS) sharply reduce the required logical qubits, yet still demand billions of Toffoli gates. Here we use large language model (LLM)-driven search to redesign the RNS pipeline across stages and build a deterministic compiler that produces a Pareto frontier of RSA-2048 circuits.

### 实验/数据
Optimizing these circuits is difficult because shared ancilla qubits and measurement-based uncomputation tightly couple the arithmetic stages, while rare overflows in compressed registers occur too infrequently for random simulation to detect.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Relative to Gidney's 2025 baseline under matched adder accounting, our frontier cuts the minimum qubit-Toffoli product by 70.1% and lowers expected factoring Toffolis by up to 78.6% at matched accumulator precision, bringing RSA-2048 factoring below one billion Toffolis for the first time.

### 28. So Many Ways to Multiply $3\times3$ Matrices: A Large Dataset of Rank-23 Schemes

- 作者：Andrew Igorevich Perminov｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31155v1

### 背景/问题
A publicly available dataset of 62029 rank-23 schemes for $3\times3$ matrix multiplication is presented. Every scheme in it has its own rank pattern, an invariant formed by the ranks of the factor matrices of a scheme, so all schemes are pairwise inequivalent.

### 方法
未在摘要中明确给出。

### 实验/数据
A publicly available dataset of 62029 rank-23 schemes for $3\times3$ matrix multiplication is presented. The dataset shows that the number of different rank patterns is much larger than previously known.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The dataset shows that the number of different rank patterns is much larger than previously known.

### 29. Attention Latent Feedback

- 作者：Xuyuan Xiong, Siyu Chen, Mengzhao Chen, Yue Su, Zhuoran Yang, Ping Luo, Xihui Liu｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31154v1

### 背景/问题
During autoregressive decoding, the deeper representations of the previous token have already been computed, yet shallow layers at the current token cannot read them directly because standard self-attention connects positions only at the same depth. We introduce Attention Latent Feedback (ALF), an architecture that allows every sublayer to attend to the outputs of the deeper layers at the previous position.

### 方法
Across mixture-of-experts models with up to 4.0B parameters, ALF lowers held-out loss by 0.022-0.024 nats over the standard residual with about 1.1% decoding FLOP overhead, and consistently outperforms prior final-state feedback across all three scales on both standard and attention residual backbones.

### 实验/数据
未在摘要中明确给出。

### 结果
Across mixture-of-experts models with up to 4.0B parameters, ALF lowers held-out loss by 0.022-0.024 nats over the standard residual with about 1.1% decoding FLOP overhead, and consistently outperforms prior final-state feedback across all three scales on both standard and attention residual backbones. On MoE-1.6B, ALF matches a $1.38\times$ larger baseline token budget, and on MoE-4.0B it lifts average accuracy across seventeen downstream benchmarks from 45.1% to 47.0%.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Analysis further reveals that intermediate and nearby deeper layers drive most of this benefit, allowing a fixed nearest-window variant to retain 89%-94% of the gain at linear read cost while learned attention widens its margin with scale.

### 30. Modularity of Heegner Cycles and Arithmetic Inner Products on Kuga-Sato Varieties

- 作者：Tuoping Du｜年份：2026｜发布时间：2026-11-23｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.31153v1

### 背景/问题
For \(κ\ge2\), the principal part of a weakly holomorphic modular form of weight \(\tfrac32-κ\) determines a linear combination of codimension-\(κ\) Heegner cycles on a compact Kuga--Sato variety. We use isogeny correspondences to prove that every such combination vanishes in the Chow group with complex coefficients.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
We prove an arithmetic inner product formula for theta lifts on the modular curve \(X_0(N)\) and on higher-dimensional Kuga--Sato varieties.

### 结论/启示（面向电商发券、定价、营销算法等应用）
This specialization recovers the Gross--Zagier formula in weight two and the genus-character case of the Gross--Zagier--Zhang formula in higher weight.
