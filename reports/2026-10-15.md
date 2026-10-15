# CausalRadar 日报 - 2026-10-15

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance

- 作者：Zhefei Gong, Hefeifei Jiang, Zehao Wang, Jiachen Li｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**11.00**
- 链接：https://arxiv.org/abs/2610.20607v1

> 命中：hit_scenario=['ads']；hit_title=['policy learning']；hit_abstract=['CATE']

### 背景/问题
Mobile Manipulation (MoMa) is a cornerstone of autonomous robotic systems, yet real-world fine-tuning remains a formidable challenge because of high-dimensional action spaces and intricate coupling between heterogeneous modules. In this paper, we propose HiRe-MoMa (Hierarchical Residual Mobile Manipulation), a systematic framework for stable and sample-efficient real-world fine-tuning of complex MoMa systems.

### 方法
In this paper, we propose HiRe-MoMa (Hierarchical Residual Mobile Manipulation), a systematic framework for stable and sample-efficient real-world fine-tuning of complex MoMa systems. To improve sample efficiency in data-expensive real-world settings, we propose Expert-Guided Value Alignment, which leverages sparse human interventions with under 20% training coverage to reshape the critic's value landscape, effectively guiding autonomous exploration through expert priors. To our knowledge, this is among the first frameworks to enable efficient on-robot fine-tuning for mobile manipulation in the real world, providing a practical paradigm for deploying complex robotic systems in dynamic, human-centric environments.

### 实验/数据
To improve sample efficiency in data-expensive real-world settings, we propose Expert-Guided Value Alignment, which leverages sparse human interventions with under 20% training coverage to reshape the critic's value landscape, effectively guiding autonomous exploration through expert priors. Extensive real-world experiments on the TIAGo++ platform demonstrate that HiRe-MoMa consistently enhances task performance with only around 30 minutes of online interaction, regardless of the base policy architecture.

### 结果
To improve sample efficiency in data-expensive real-world settings, we propose Expert-Guided Value Alignment, which leverages sparse human interventions with under 20% training coverage to reshape the critic's value landscape, effectively guiding autonomous exploration through expert priors.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Further details can be found on our project website: https://hire-moma.github.io/

### 2. CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation

- 作者：Xiaoli Xu, Zhengtao Wu, Zhengze Xu, Tao Liu, Yongchao Du, Zuan Gao, Xingjian Wang, Hao Yan 等｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**6.50**
- 链接：https://arxiv.org/abs/2610.20603v1

> 命中：hit_abstract=['CATE', 'e-commerce']

### 背景/问题
We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists through an iterative closed loop of VLM and LLM roles scored by a reference-free rubric.

### 方法
We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists through an iterative closed loop of VLM and LLM roles scored by a reference-free rubric. The framework runs in production at a scale of millions of main images per day with a latency of a few seconds per image, which we believe makes it among the first systems of this kind to operate at commercial scale.

### 实验/数据
Our framework is organized along a three-stage pipeline of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists through an iterative closed loop of VLM and LLM roles scored by a reference-free rubric.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
It also matches much larger closed-source models, and beats several of them at Instruction Following and Product Integration - the two properties that determine whether an image can be published.

### 3. Your Transformer Is Secretly Elastic

- 作者：Walter Simoncini, Dheeraj Varghese, Gertjan J. Burghouts, Cees G. M. Snoek｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.20588v1

> 命中：hit_scenario=['ads']

### 背景/问题
Scaling up transformers has produced models with broad capabilities, deployed across heterogeneous hardware and fluctuating workloads. Yet, model families offer only a few fixed sizes (e.g., S, B, L), forcing users to commit to a model based on hardware and latency constraints.

### 方法
Scaling up transformers has produced models with broad capabilities, deployed across heterogeneous hardware and fluctuating workloads. Yet, model families offer only a few fixed sizes (e.g., S, B, L), forcing users to commit to a model based on hardware and latency constraints. We introduce a retraining-free method that elastifies pre-trained transformers into a single model that adapts on-the-fly across a continuum of computational budgets.

### 实验/数据
未在摘要中明确给出。

### 结果
Across 27 vision and text transformer encoders ranging from 22M to 8B parameters, our method yields smooth degradation up to 60% sparsity and outperforms one-shot baselines under deep pruning.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Elastic models are produced in minutes, with construction time scaling sub-linearly with parameter count.

### 4. Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation

- 作者：Weijie Wang, Haomin Zhang, Ye Li, Akide Liu, Zeyu Zhang, Haoyu Zhao, Yefei He, Donny Y. Chen 等｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.20571v1

> 命中：hit_scenario=['ads']

### 背景/问题
Long-form agentic video generation must turn a screenplay into shots that remain spatially and temporally consistent across nonconsecutive requests. Passing prompts or recent frames between shots does not provide a shared spatial frame for revisiting a scene or a time-indexed record for replaying an earlier event.

### 方法
We present Any Time, Any Space (ATAS), which compiles a screenplay into shot requests with explicit location, camera, and event-time references.

### 实验/数据
未在摘要中明确给出。

### 结果
Across four video generators, ATAS improves all reported cross-shot consistency measures and achieves the highest aggregate benchmark score for each backbone. It also outperforms the compared agents and 3D-guided methods on target-image spatial revisit, leads three event-recapture criteria, and receives the highest human ratings on all six criteria.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The video results and code are available on our project page: https://lhmd.top/atas/.

### 5. Minimal Resolutions of $k$-divisible and $(k-1)$-dominant Ideals

- 作者：Patrick Welte, Guillermo Alesandroni｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.20565v1

> 命中：hit_scenario=['ads']

### 背景/问题
We introduce invariants we call $k$-divisibility and $d$-dominance, which are combinatorial constraints on the minimal generators of monomial ideals. We then prove that $k$ (respectively, $d$) is an upper bound (respectively, lower bound) for the projective dimension of a $k$-divisible (respectively, $d$-dominant) monomial ideal.

### 方法
This framework allows us to prove a conjecture made by Alesandroni.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also prove that for all $q,k,d$ in the range $1\leq d<k \leq q-1$, there exist monomial ideals that are $k$-divisible and $d$-dominant with $q$ minimal generators.

### 6. JetStream: Generating Verified Query Accelerators for Existing Database Systems

- 作者：Akhilesh Balasingam, Amadou Ngom, Geoffrey X. Yu, Tim Kraska｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.20527v1

> 命中：hit_scenario=['ads']

### 背景/问题
Recent work has shown that LLMs can synthesize highly specialized database systems for fixed workloads, but these systems replace the DBMS's native storage and assume static data: users must migrate their data, often give up ad-hoc queries, and lose acceleration once the data changes. We present JetStream, which instead generates query-specific accelerators that extend an existing DBMS.

### 方法
We present JetStream, which instead generates query-specific accelerators that extend an existing DBMS.

### 实验/数据
Recent work has shown that LLMs can synthesize highly specialized database systems for fixed workloads, but these systems replace the DBMS's native storage and assume static data: users must migrate their data, often give up ad-hoc queries, and lose acceleration once the data changes.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
On TPC-H at SF=20, JetStream achieves a $315 \times$ geomean read speedup over DuckDB ($93 \times$ verified) and retains $120 \times$ under a continuous update stream of 10,000 modified rows per second.

### 7. Manacá-1B-Instruct-2: Reproducible Safety Alignment for a Native Brazilian-Portuguese LLM. Negative DPO Results, a Controlled Composition Scan, and a Silent Failure Mode of the LLM Judge

- 作者：Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio André Machado Porto｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.20570v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Brazilian Portuguese remains underserved by open-source language models, and the few that are safety-aligned rarely document what did not work or validate comparisons with statistical significance. We present Manacá-1B-Instruct-2, the second-generation post-training alignment of Manacá-1B (1.72B parameters, trained from scratch for PT-BR), with an SFT corpus of 291,223 examples.

### 方法
Brazilian Portuguese remains underserved by open-source language models, and the few that are safety-aligned rarely document what did not work or validate comparisons with statistical significance. We present Manacá-1B-Instruct-2, the second-generation post-training alignment of Manacá-1B (1.72B parameters, trained from scratch for PT-BR), with an SFT corpus of 291,223 examples. The final model is compared against four external PT-BR models on the same items, with Wilson confidence intervals and paired McNemar tests with Holm-Bonferroni correction: the lower bound of its safety interval (94.1%) lies above the upper bound of all four baselines.

### 实验/数据
A controlled scan of the fraction of general data in the safety-SFT mix (10% to 60%) reveals a non-monotonic over-refusal curve with a knee point at 40-50%. All code, raw data, logs, and scripts that produce every reported number are publicly released.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
All code, raw data, logs, and scripts that produce every reported number are publicly released.

### 8. Scaling Discovery Requires Forgetting

- 作者：Shangyin Tan, Ben Zhou, Lakshya A Agrawal, Jialin Zhang, Yilin Chen, Qiuyang Mang, Donghyun Lee, Dennis Jacob 等｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.20563v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Automated research with LLM agents has shown promising results in various domains. Through iterative refinement and scored verifiers, LLM agents are capable of discovering new ideas.

### 方法
We implement forgetting in a team of agents with communication and evaluate it on four tasks spanning heuristic programming, kernel optimization and model training.

### 实验/数据
未在摘要中明确给出。

### 结果
Beyond this point, additional budget brings little further improvement. The results show up to 15% improvement compared to parallel agents, and up to 39% compared to a single agent.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our results suggest that, for open-ended discovery, what an agent is allowed to remember matters as much as how much compute it is given.

### 9. Decoupled Marginal Sharpening for Training-Free Inference-Time Scaling

- 作者：Weixin Wang, Wei Deng, Anderson Schneider, Yuriy Nevmyvaka, Pan Xu, Andrew Bennett｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.20483v1

> 命中：hit_abstract=['CATE']

### 背景/问题
We study how to improve LLM reasoning at inference time without updating model weights or using external reward models. Recent reward-free power-sampling methods define the sequence-level power target $π_α(y\mid x)\propto p_0(y\mid x)^α$, where $α>1$, which increases the relative probability of completions that are already likely under the base model.

### 方法
We study how to improve LLM reasoning at inference time without updating model weights or using external reward models. Recent reward-free power-sampling methods define the sequence-level power target $π_α(y\mid x)\propto p_0(y\mid x)^α$, where $α>1$, which increases the relative probability of completions that are already likely under the base model. To address these challenges, we propose Decoupled Marginal Sharpening (DMS), which separately controls how strongly the model favors particular reasoning paths and how strongly it favors final answers after aggregating support across those paths.

### 实验/数据
Experiments on MATH500, GPQA-Diamond, HumanEval, and AIME24/25 across three base models show that DMS achieves the highest mean pass@1 among the compared methods in all tasks.

### 结果
We study how to improve LLM reasoning at inference time without updating model weights or using external reward models. Recent reward-free power-sampling methods define the sequence-level power target $π_α(y\mid x)\propto p_0(y\mid x)^α$, where $α>1$, which increases the relative probability of completions that are already likely under the base model.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Experiments on MATH500, GPQA-Diamond, HumanEval, and AIME24/25 across three base models show that DMS achieves the highest mean pass@1 among the compared methods in all tasks.

### 10. LHAASO Constraints on New-Source Cosmic Rays:Abundance Scenarios and Injection Spectral Indices

- 作者：Xu-Lin Dong, Pei-Pei Zhang, Qi-Ling Chen, Shu-Wang Cu, Yi-Qing Guo｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.20477v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Recent LHAASO observations indicate that microquasars and massive star clusters contribute to Galactic cosmic rays, and likely also to the pre-knee spectral hardening. Their markedly different astrophysical environments, compared with supernova remnants (SNRs), may imprint distinct cosmic-ray abundances.

### 方法
We constrain injection spectral indices using LHAASO proton, helium, and all-particle spectra, and use their <lnA> data for model discrimination.

### 实验/数据
We constrain injection spectral indices using LHAASO proton, helium, and all-particle spectra, and use their <lnA> data for model discrimination. Under the assumption of a unified heavy-element injection spectrum, Case-2 fits the <lnA> data significantly better than Case-1, but at the cost of large, physically unmotivated differences between heavy-element and He injection indices.

### 结果
Under the assumption of a unified heavy-element injection spectrum, Case-2 fits the <lnA> data significantly better than Case-1, but at the cost of large, physically unmotivated differences between heavy-element and He injection indices. We predict that if the new-source composition follows Case-1, the individual elemental spectral indices before the knee should remain nearly consistent; if it follows Case-2, the Mg, Si, and Fe spectra will be significantly softer than those of He, C, and O.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Future element-resolved energy-spectrum measurements by HERD and LHAASO will provide a decisive test of this discriminating feature.

### 11. A global analysis of ${\bar B}\to DP$ and ${\bar B} \to {\bar D} P$ decays

- 作者：Bhubanjyoti Bhattacharya, Rida Boumris, David London｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20611v1

### 背景/问题
Recently, a fit to the 15 measured branching ratios of ${\bar B} \to D P$ decays ($B = \{B^+, B^0, B_s^0\}$, $D = \{D^0, D^+, D_s^+\}$, $P \in \{π, K\}$) was performed under the assumption of flavor SU(3) symmetry [SU(3)$_F$]. A terrible fit was found: there was a $> 5σ$ disagreement with the SU(3)$_F$ limit of the Standard Model [SM$_{\rm{SU(3)}_F}$].

### 方法
A terrible fit was found: there was a $> 5σ$ disagreement with the SU(3)$_F$ limit of the Standard Model [SM$_{\rm{SU(3)}_F}$].

### 实验/数据
We again find a $> 5σ$ disagreement with the SM$_{\rm{SU(3)}_F}$, and we find that the data can be explained if $\sim 60\%$ SU(3)$_F$-breaking effects are included.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We again find a $> 5σ$ disagreement with the SM$_{\rm{SU(3)}_F}$, and we find that the data can be explained if $\sim 60\%$ SU(3)$_F$-breaking effects are included.

### 12. SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving

- 作者：Shaoyuan Xie, Zihan Zhang, Jingxuan Wang, Jiashu Qu, Xiaoqing Liang, Lingdong Kong, Junchi Lu, Henrik I. Christensen 等｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20609v1

### 背景/问题
Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructions. However, this open-ended interface exposes a new vulnerability surface: an inattentive driver may issue instructions that are unsafe given the current scene, and a malicious user may issue dangerous ones on purpose.

### 方法
Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructions. We present the first benchmark suite that evaluates navigation following and conflict awareness together, along with adversarial robustness. Existing VLAs fall short on both: SimLingo completes no language-instructed lane change in closed loop, and all models degrade sharply under conflicting signals.

### 实验/数据
未在摘要中明确给出。

### 结果
SafeDriveVLA reaches 88.16 Driving Score (DS) and 68.64% Success Rate (SR) on Bench2Drive, lifts closed-loop language following by 49.3% and reduces collisions under unsafe instructions from 60 to 38 compared to the best SimLingo variant.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Video demonstrations are available on our project page.

### 13. The existence of small defining polynomials for number fields

- 作者：Manjul Bhargava, Sameera Vemulapalli｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20600v1

### 背景/问题
We prove that every number field of degree $n$ and absolute discriminant $D$ has a defining integral polynomial of degree $n$ whose coefficients are all $O_n(\sqrt D)$ in size, thus resolving a 1998 conjecture of Ruppert. Our proof compares ideal lattices with their trace duals, via which we handle all number fields with the exception of CM fields whose maximal totally real subfields have small discriminant.

### 方法
未在摘要中明确给出。

### 实验/数据
We prove that every number field of degree $n$ and absolute discriminant $D$ has a defining integral polynomial of degree $n$ whose coefficients are all $O_n(\sqrt D)$ in size, thus resolving a 1998 conjecture of Ruppert. Our proof compares ideal lattices with their trace duals, via which we handle all number fields with the exception of CM fields whose maximal totally real subfields have small discriminant. We then treat the remaining fields by averaging completed Epstein zeta functions over all possible ideal classes and archimedean scalings, for which we make critical use of Hecke's formula and the subconvexity theorem of Michel and~Venkatesh.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our proof does not use the Quasi-Riemann Hypothesis.

### 14. DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning

- 作者：Qihang Cao, Haoyuan Li, Zihan Guo, Sensen Gao, Zihui Gao, Huixin Zhang, Fan He, Jianhua Han 等｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20598v1

### 背景/问题
Achieving general spatial intelligence requires a unified understanding of both static 3D and dynamic 4D. However, we find that existing models struggle to excel at both: 3D post-training can weaken dynamic understanding, while 4D-specialized models often lack strong static 3D reasoning.

### 方法
However, we find that existing models struggle to excel at both: 3D post-training can weaken dynamic understanding, while 4D-specialized models often lack strong static 3D reasoning. To address this interference, we propose DynThinker, a unified framework for jointly strengthening static and dynamic spatial reasoning. Across ten metrics spanning nine static 3D and dynamic 4D benchmarks, DynThinker achieves the highest average score among all evaluated models.

### 实验/数据
未在摘要中明确给出。

### 结果
Notably, DynThinker achieves 56.0 on ReVSI, 67.2 on DSR-Bench, and 51.2 and 40.1 under the sample-wise and group-wise evaluation protocols of DSI-Bench, respectively, setting new state-of-the-art results among the compared open-source models across all four evaluations within a unified model.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Notably, DynThinker achieves 56.0 on ReVSI, 67.2 on DSR-Bench, and 51.2 and 40.1 under the sample-wise and group-wise evaluation protocols of DSI-Bench, respectively, setting new state-of-the-art results among the compared open-source models across all four evaluations within a unified model.

### 15. Continuum Attention

- 作者：Afshin Khadangi｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20586v1

### 背景/问题
We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve. Each query induces an exponential relevance density along the curve.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These findings motivate continuous integration as a promising attention alternative while leaving larger scale generalization open.

### 16. All Serrin bands are unduloidal

- 作者：Laurent Hauswirth, Pablo Mira｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20581v1

### 背景/问题
We show that any Serrin domain in $\mathbb{R}^2$ with two boundary components is a member of the canonical unduloidal family

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We show that any Serrin domain in $\mathbb{R}^2$ with two boundary components is a member of the canonical unduloidal family

### 17. Decay-Ramsey Sequences

- 作者：Francesco Di Braccio, Simon Griffiths, Pedram Noohi, Leo Versteegen｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20577v1

### 背景/问题
Given a sequence $\mathbf{a}=(a_i)_{i\geq 1}$ of positive real numbers, we say that a colouring $c:E(K_n)\to \mathbb{N}$ is $\mathbf{a}$-bounded if the proportion of edges coloured $i$ is at most $a_i$, for all $i$. We write \[ \mathbf{a}\, \to\, K_k \] if, for all sufficiently large $n$, all $\mathbf{a}$-bounded colourings $c:E(K_n)\to \mathbb{N}$ contain a monochromatic $K_k$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In this short paper we introduce the question of determining which sequences are Decay-Ramsey and present some initial results.

### 18. Complex generalized spin-c Killing spinors in low dimensions

- 作者：José Luis Carmona Jiménez, Alejandro Gil-García, C. S. Shahbazi｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20568v1

### 背景/问题
We classify all complex generalized spin-c Killing spinors with complex Killing function $iμ-α$ on complete Riemannian surfaces, presenting an explicit list of all possible cases. We show that, contrary to previous statements in the literature, there exist complex generalized spin-c Killing spinors on Riemannian surfaces for which $αμ\not\equiv0$.

### 方法
未在摘要中明确给出。

### 实验/数据
In addition, we construct a geodesically incomplete Riemannian three-manifold equipped with a complex generalized spin-c Killing spinor for which neither $μ$ nor $α$ vanishes identically, and then prove that this is not possible if the characteristic vector field of the associated trans-Sasakian structure is complete.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results settle a conjecture by Große and Nakad (Results in Mathematics, 2015) stating that on two- and three-dimensional Riemannian manifolds the complex Killing function of any complex generalized spin-c Killing spinor must be either globally real or globally imaginary.

### 19. Proof of the Penrose Conjecture for Maximally Parameterized Initial Data Sets

- 作者：Hubert Bray, Tuan Dolmen, Marcus Khuri, David Schmidt｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20559v1

### 背景/问题
We prove the spacetime Penrose inequality for asymptotically flat initial data sets $(M^n,g,k)$ in all dimensions $n\geq 3$, under the dominant energy condition, for data admitting the 'maximally parameterized form' defined in equation (4.7). In this case, the second fundamental form $k$ is locally parameterized by $n(n+1)/2$ functions, giving the same formal local functional degrees of freedom as an arbitrary symmetric $2$-tensor.

### 方法
The proof is based on a new 1-parameter family of generalized Schoen-Yau identities and their gauge-invariant specialization, inspired by the generalized Jang framework of Bray-Khuri [8, 9].

### 实验/数据
We prove the spacetime Penrose inequality for asymptotically flat initial data sets $(M^n,g,k)$ in all dimensions $n\geq 3$, under the dominant energy condition, for data admitting the 'maximally parameterized form' defined in equation (4.7). For maximally parameterized data, these identities produce a Riemannian comparison metric \[ \bar g=g+β\otimesβ\] with nonnegative scalar curvature $R_{\bar{g}} \geq 0$.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Essentially, we believe this is what the OpenAI paper [27] posted last week on October 6, 2026 claims to have done.

### 20. PrismaCoder: Pushing the Boundaries of Open Multimodal Code Intelligence through Decomposed Rubric Synthesis

- 作者：Qiushi Sun, Jingyang Gong, Yang Liu, Qiaosheng Chen, Zhangyue Yin, Zixian Huang, Hanxu Hu, Jing Xiong 等｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20538v1

### 背景/问题
Multimodal code intelligence connects the symbolic world of programs with the visual world their execution creates. Interest in this capability is burgeoning, as models are increasingly asked to produce charts, webpages, animations, and semi-structured documents.

### 方法
Interest in this capability is burgeoning, as models are increasingly asked to produce charts, webpages, animations, and semi-structured documents. Recently, proprietary models have pushed far ahead, producing interactive artifacts even from a text description or a screenshot alone. On the model side, we train PrismaCoder-9B and PrismaCoder-35B on this data and release both.

### 实验/数据
Yet their data and training remain closed, and open progress is held back by the quantity and quality of available data and by the pipelines and methods for producing it. To push open progress further, we start from the data side with PrismaForge, a hierarchical data pipeline centered on a synthesized rubric that decomposes these factors into checkable criteria. Leveraging PrismaForge for data synthesis and filtering, we build PrismaCoder-2M, the most diverse open dataset for multimodal code intelligence and the largest to date.

### 结果
Our analyses further show that the proposed rubric-based pipeline improves multimodal coding performance across model backbones.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We release our code and data at https://qiushisun.github.io/PrismaCoder-Home/.

### 21. Intermediate memory costs of quantum channel synthesis with a protected subsystem

- 作者：Kai Liu, Deguang Han｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20536v1

### 背景/问题
A quantum memory can preserve a subsystem perfectly while discarding information needed by a later operation. We study the total intermediate dimension required for channel synthesis when the first stage protects a $b$-dimensional subsystem and has a prescribed noncommutative graph imposing full confusability on an $a$-dimensional control register.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
For $η<1$, the gap persists under sufficiently small perturbations of the target branches.

### 22. Effects of quadratic frequency chirping and carrier-envelope phase on Schwinger pair production in polarized electric fields

- 作者：Abhinav Jangir｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20529v1

### 背景/问题
We investigate electron-positron pair production in spatially homogeneous, time-dependent polarized electric fields using the Dirac-Heisenberg-Wigner formalism, focusing on the effects of symmetric and asymmetric quadratic frequency chirping and the carrier-envelope phase (CEP). Our analysis reveals how these field parameters govern both the momentum-space structure and the overall yield of the produced pairs.

### 方法
Our findings establish a theoretical framework for exploring external-field configurations that optimize the yield of Schwinger pair production.

### 实验/数据
We investigate electron-positron pair production in spatially homogeneous, time-dependent polarized electric fields using the Dirac-Heisenberg-Wigner formalism, focusing on the effects of symmetric and asymmetric quadratic frequency chirping and the carrier-envelope phase (CEP). Our analysis reveals how these field parameters govern both the momentum-space structure and the overall yield of the produced pairs. Our findings establish a theoretical framework for exploring external-field configurations that optimize the yield of Schwinger pair production.

### 结果
The total pair yield increases with chirp strength, with symmetric chirping consistently producing a higher yield than asymmetric chirping for the parameter range considered.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our findings establish a theoretical framework for exploring external-field configurations that optimize the yield of Schwinger pair production.

### 23. Lluna: Collaborative Unimodal Models for Missing-Modality Inference

- 作者：Haoyue Bai, Yinyi Luo, Heqing Huang, Xiaoyuan Yi, James Evans, Jindong Wang｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20526v1

### 背景/问题
Pretrained unimodal models offer a flexible route to multimodal prediction through collaboration, but this collaboration can become less accurate than a surviving unimodal model when modalities are missing. We study this setting using fixed surviving-model anchors and find that collaborative gains can weaken or reverse as inputs disappear, even when the anchor's own input is unchanged.

### 方法
Pretrained unimodal models offer a flexible route to multimodal prediction through collaboration, but this collaboration can become less accurate than a surviving unimodal model when modalities are missing. We study this setting using fixed surviving-model anchors and find that collaborative gains can weaken or reverse as inputs disappear, even when the anchor's own input is unchanged. We propose Lluna, which combines a direct private prediction path from adapted unimodal features with a common graph-based collaboration branch that provides a residual correction.

### 实验/数据
Across eight datasets spanning affective computing, scene understanding, and medical prediction, Lluna achieves the best evaluated average performance over non-full input states, improving Mean-Missing by 4.26\% on average relative to the strongest evaluated baseline.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Code is available at https://github.com/AIFrontierLab/Lluna.

### 24. Probabilistic AI models outperform numerical weather prediction models on record breaking heat extremes

- 作者：Jakob Benjamin Wessel, Fiona Spuler, Christopher A. T. Ferro, Marlene Kretschmer, Sebastian Sippel｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20519v1

### 背景/问题
AI weather prediction (AIWP) models have emerged as a key complement to physics-based numerical weather prediction (NWP) models, and now often outperform them on aggregate skill. Yet, several studies report that physics-based models still forecast extreme events better, in particular record-breaking extremes, based on the evaluation of deterministic forecasts.

### 方法
AI weather prediction (AIWP) models have emerged as a key complement to physics-based numerical weather prediction (NWP) models, and now often outperform them on aggregate skill. Yet, several studies report that physics-based models still forecast extreme events better, in particular record-breaking extremes, based on the evaluation of deterministic forecasts. Here we evaluate heat extreme forecasts from probabilistic AIWP models over global land and show that they clearly outperform the ECMWF IFS ensemble, both raw and post-processed, including for record-breaking events, in all regions and at all lead times considered.

### 实验/数据
未在摘要中明确给出。

### 结果
AI weather prediction (AIWP) models have emerged as a key complement to physics-based numerical weather prediction (NWP) models, and now often outperform them on aggregate skill. Yet, several studies report that physics-based models still forecast extreme events better, in particular record-breaking extremes, based on the evaluation of deterministic forecasts. Here we evaluate heat extreme forecasts from probabilistic AIWP models over global land and show that they clearly outperform the ECMWF IFS ensemble, both raw and post-processed, including for record-breaking events, in all regions and at all lead times considered.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Instead, a fair evaluation of extremes necessitates probabilistic verification.

### 25. The Wealth of Agents: Scaling Agentic AI Across Developers

- 作者：Austin W. Hanjie, Carlos E. Jimenez, Zirui Wang, Karthik Narasimhan｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20518v1

### 背景/问题
Today's agentic systems are typically designed, built, and deployed by single developers with full control over all participating agents. While this simplifies development, it limits the potential scale of agentic systems.

### 方法
We construct empirical and theoretical models of developers to compare MDAs with single-developer agentic systems (SDAs). Our theoretical models show how MDAs can incentivize specialization and encourage more efficient use of aggregated developer resources.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Put together, our results make a preliminary case for MDAs as a new scaling axis by enabling developers with diverse capabilities and resources to advance agentic AI collaboratively.

### 26. Can bosenovae deplete the galactic dark matter?

- 作者：Samuel Gómez Gómez, Joshua Eby｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20507v1

### 背景/问题
No: neither through the bosenovae of gravitational atoms formed around stars and compact objects, nor through those of boson stars formed in the galactic dark-matter halo. We assume that all the dark matter consists of ultralight bosons with attractive self-interactions, which can be captured in the gravitational potential of astrophysical objects or condense into self-gravitating configurations.

### 方法
We bound the mass that a single object can eject and sum it over realistic models of the Milky Way and of other types of galaxies.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
For boson stars feeding on the rest of the halo, these would radiate at most $\sim3\times10^{-5}$ of the Milky-Way halo and $0.1\%$ of a DF2-like one.

### 27. Structural identification in general crystalline systems via Voronoi cell topology

- 作者：Emanuel A. Lazar, Chris H. Rycroft｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20498v1

### 背景/问题
Widely used methods for identifying crystal structure in atomistic simulations are limited in practice to a handful of simple structures, leaving many important crystalline systems without automated classification techniques. Voronoi topology analysis offers a route to classifying arbitrary crystalline and defect environments, but realizing this potential first requires enumerating the Voronoi cell topologies that can arise under thermal perturbation of a structure of interest.

### 方法
Widely used methods for identifying crystal structure in atomistic simulations are limited in practice to a handful of simple structures, leaving many important crystalline systems without automated classification techniques. We present an algorithm that deterministically enumerates all Voronoi cell topologies arising from generic infinitesimal perturbations of an arbitrary crystal structure, producing structural classifiers that extend automated identification to general crystalline systems. We demonstrate the approach on several structures of general interest.

### 实验/数据
Widely used methods for identifying crystal structure in atomistic simulations are limited in practice to a handful of simple structures, leaving many important crystalline systems without automated classification techniques.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We demonstrate the approach on several structures of general interest.

### 28. Hindsight-Privileged RLVR: Single-Rollout Token Credit Without Group Sampling

- 作者：Wei Chen, Yubing Wu, Zhou Xu, Haoyue Zhang, Delu Zeng, Jiahao Wang, Junmei Yang, Pan tiewen 等｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20497v1

### 背景/问题
Reinforcement learning with verifiable rewards (RLVR) trains language models from checked task outcomes, but assigning a terminal reward to individual reasoning tokens or actions remains difficult. Group-relative methods such as Group Relative Policy Optimization (GRPO) sample several attempts per prompt, but lose their reward-based learning signal when all attempts receive the same outcome.

### 方法
Reinforcement learning with verifiable rewards (RLVR) trains language models from checked task outcomes, but assigning a terminal reward to individual reasoning tokens or actions remains difficult. We propose Hindsight-Privileged RLVR (HP-RLVR), a single-rollout method that turns a completed trajectory's own future into token-level update weights.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In ALFWorld, $43.2\%$ (4B) and $49.0\%$ (8B) of GRPO's gradient-norm records are zero, versus none for HP-RLVR.

### 29. On Complexity of Gaussian Sampling

- 作者：Huanjian Zhou, Taiji Suzuki｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20492v1

### 背景/问题
We study the number of exact matrix-vector queries needed to sample a centered $d$-dimensional Gaussian with condition number at most $κ$ to total variation error $\varepsilon$. The best known algorithm uses $O(\min\{d,\sqrtκ\log(\frac{d}{\varepsilon})\})$ queries, while the known lower bounds do not grow as $\varepsilon\to0$ and match this bound only for $κ\le d^{1/5-δ}$ at constant accuracy.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
This gives an $Ω_δ(\sqrtκ\log d)$ lower bound at constant accuracy that holds even when the spectrum of the precision matrix is known to the algorithm.

### 30. Transference principles for divergence sets of dispersive equations and their applications

- 作者：Utsav Dewan｜年份：2026｜发布时间：2026-10-14｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.20480v1

### 背景/问题
In this article, we study the fractal refinement of the Carleson's problem: (1) We introduce an equivalence relation on linear dispersive PDEs on $\mathbb{R}^{n}$ based on the high-frequency oscillation of their Fourier multipliers, proving that equations in the same class share the same Hausdorff dimension of divergence sets. As applications, we estimate these dimensions for abstract dispersive families.

### 方法
未在摘要中明确给出。

### 实验/数据
(2) Next, we study the effect of radial symmetry by obtaining dimension estimates for fractional Schrödinger equations with concave phase and radial initial data.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In the process, we also obtain a quantitative result on the singular sets of Sobolev functions, in the spirit of Žubrinić, which may be of independent interest.
