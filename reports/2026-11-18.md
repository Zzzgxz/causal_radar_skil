# CausalRadar 日报 - 2026-11-18

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Inference for Heterogeneous Treatment Effects with Deep Survival Learners

- 作者：Sattwik Ghosal, Xuran Meng, Yuming Sun, Yi Li｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**16.50**
- 链接：https://arxiv.org/abs/2611.23090v1

> 命中：hit_method=['heterogeneous treatment effect']；hit_title=['treatment effect', 'heterogeneous treatment effect']；hit_abstract=['treatment effect', 'CATE']

### 背景/问题
Conditional average treatment effects (CATEs) provide a principled framework for assessing treatment-effect heterogeneity and identifying patients who may benefit from an intervention. For survival outcomes, CATEs may also evolve over time and pose challenges for estimation and inference.

### 方法
Conditional average treatment effects (CATEs) provide a principled framework for assessing treatment-effect heterogeneity and identifying patients who may benefit from an intervention. We propose a deep survival learning framework that combines neural networks for nonparametric covariate effects with a shared spline representation of temporal variation, enabling joint estimation of CATE trajectories. For inference, we develop a subsampled ensemble procedure and establish asymptotic normality for pointwise CATEs, temporal contrasts, and covariate contrasts, including temporal contrasts over shrinking time intervals.

### 实验/数据
Simulations evaluate estimation accuracy, interval coverage, and sensitivity to temporal dimension and basis mismatch. An application to lung cancer survival data illustrates the framework's ability to characterize heterogeneous treatment benefits over time.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
An application to lung cancer survival data illustrates the framework's ability to characterize heterogeneous treatment benefits over time.

### 2. Déjà View: A Shared Working-Memory Model for Visual Tasks

- 作者：Mranmay Shetty, Gabriel Kreiman｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**7.00**
- 链接：https://arxiv.org/abs/2611.23177v1

> 命中：hit_scenario=['ads']；hit_abstract=['CATE']

### 背景/问题
A working-memory model must remember stimuli and use its memory flexibly to perform different tasks. Here we introduce a model of working memory for images that combines dynamic activity with temporary associations between image features.

### 方法
A working-memory model must remember stimuli and use its memory flexibly to perform different tasks. Here we introduce a model of working memory for images that combines dynamic activity with temporary associations between image features. We train the model on five tasks, including remembering a sample while other images are presented, categorizing distractor images while remembering the sample, and determining whether an image is new or has been presented before.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Together, these results demonstrate how a single working-memory system can be flexibly used to perform different tasks, and how its errors depend on both previous images and task demands.

### 3. VIVID: Beyond Static Multi-Image Reasoning with Localized Visual Differences and Textual Entity Dynamics in Video MLLMs

- 作者：Chengqian Ma, Yuanze Zeng, Hongyu Wang, Mingfeng Lin, YiCheng Xiao, Yu Chen, Pengyu Li, WenHao Wang 等｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.23153v1

> 命中：hit_scenario=['ads']

### 背景/问题
Video question answering under tight frame budgets requires preserving localized motion and event order, yet current video multimodal large language models (MLLMs) reduce comprehension to static multi-image reasoning by discarding unselected frames and encoding keyframes independently: (1) Spatially, whole-frame pooling dilutes small moving targets into static backgrounds; (2) Temporally, dropping intermediate frames or averaging tokens erases inter-frame motion, confusing direction, speed, and order. We propose VIVID (Visual Inter-frame Variations and Individual Dynamics), which moves beyond static snapshots like human vision: keyframes capture core states while inter-frame Patch Diffs preserve neighboring changes within $K_f$ keyframes.

### 方法
Video question answering under tight frame budgets requires preserving localized motion and event order, yet current video multimodal large language models (MLLMs) reduce comprehension to static multi-image reasoning by discarding unselected frames and encoding keyframes independently: (1) Spatially, whole-frame pooling dilutes small moving targets into static backgrounds; (2) Temporally, dropping intermediate frames or averaging tokens erases inter-frame motion, confusing direction, speed, and order. We propose VIVID (Visual Inter-frame Variations and Individual Dynamics), which moves beyond static snapshots like human vision: keyframes capture core states while inter-frame Patch Diffs preserve neighboring changes within $K_f$ keyframes.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Adding $0.22\%$ trainable parameters to a frozen $27\text{B}$ backbone, VIVID-Small ($50$ examples, $\sim 1.5$ GPU hours) beats all eleven baselines in overall accuracy across $8,083$ questions and trails only VIVID-Large ($3,600$ examples), which leads on MotionBench, Video-MME, and TempCompass.

### 4. Where Should Physics Enter? Information, Identifiability and Calibration in Probabilistic Sea Surface Temperature Forecasting

- 作者：Parmitha Vangapandu, Jonnakuti Pavan Kumar, Sathwik Narkedimilli, MSVPJ Sathvik, T. M. Balakrishnan Nair, Santanu Bhattacharya｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.23129v1

> 命中：hit_scenario=['ads']

### 背景/问题
Advection-diffusion priors are a common way to make neural sea surface temperature (SST) forecasts physics-informed. We test where such a prior must enter a heteroscedastic ConvLSTM to help, using daily NOAA OISST v2.1 for the Bay of Bengal (1982-2024) and a synthetic benchmark on the same grid with known currents of controlled strength.

### 方法
(v) The defect that matters is lead-dependent miscalibration shared by every model.

### 实验/数据
(i) On real data, a soft advection-diffusion residual with a learned velocity gives no reliable benefit (lead-15 CRPS -0.007 degrees C, 95% interval [-0.022, +0.008]); a plain temporal-smoothness penalty matches it, and equivalence within 3% is not established either. (ii) Learned velocities do not recover the currents, whether placed in the loss, in an explicit transport step, or in a transport step without neural correction: they correlate with the reference no better than a shuffled-date null, even on synthetic data where knowing the currents would improve day-15 forecasts by 16-23%. (iii) Supplied currents help on synthetic data, but mostly as information: giving them to the network as input channels, without transport, recovers 92% of the transport design's lead-5 gain, and a frozen-current numerical forecast does as well as either.

### 结果
(ii) Learned velocities do not recover the currents, whether placed in the loss, in an explicit transport step, or in a transport step without neural correction: they correlate with the reference no better than a shuffled-date null, even on synthetic data where knowing the currents would improve day-15 forecasts by 16-23%.

### 结论/启示（面向电商发券、定价、营销算法等应用）
This version withdraws an earlier claim of an 81% CRPS reduction that came from an uncontrolled comparison.

### 5. Which Past Matters? Training History and Multi-Forecast Horizon in Equity Transformers

- 作者：Chariton Chalvatzis｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.23126v1

> 命中：hit_scenario=['ads']

### 背景/问题
More historical data can improve estimation while introducing relationships that transfer poorly to current market conditions. We therefore examine how training quantity and historical selection interact with forecast horizon in intraday equity prediction.

### 方法
Six-month recency sampling leads individual models at 5-15 minutes, while multi recency configurations lead at 20-30 minutes and uniform configurations at 60-120 minutes. Increasing training quantity does not uniformly improve accuracy while an equal-weight ensemble of all twelve models exceeds every individual mean at 15, 20 and 25 minutes, but not at the remaining horizons. These findings support evaluating historical selection jointly with forecast horizon without identifying a universal policy or a causal benefit from recency.

### 实验/数据
More historical data can improve estimation while introducing relationships that transfer poorly to current market conditions. A monthly walk-forward experiment produces 264 refits and eight cumulative return forecasts from 5 to 120 minutes.

### 结果
More historical data can improve estimation while introducing relationships that transfer poorly to current market conditions. Increasing training quantity does not uniformly improve accuracy while an equal-weight ensemble of all twelve models exceeds every individual mean at 15, 20 and 25 minutes, but not at the remaining horizons.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These findings support evaluating historical selection jointly with forecast horizon without identifying a universal policy or a causal benefit from recency.

### 6. Get Hint-Augmented GRPO Done Right Through Activation Steering

- 作者：Khiem Le, Ting Hua, Nitesh V. Chawla｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.23124v1

> 命中：hit_scenario=['ads']

### 背景/问题
GRPO has become the dominant reinforcement learning method for eliciting reasoning capability in LLMs using verifiable rewards. However, it suffers from a fundamental failure mode: when a training question exceeds the base model's current capability, all generated responses fail and receive zero reward, yielding no gradient signal and stalling further capability expansion.

### 方法
However, it suffers from a fundamental failure mode: when a training question exceeds the base model's current capability, all generated responses fail and receive zero reward, yielding no gradient signal and stalling further capability expansion. In this work, we reinterpret the function of hinting -- not as reducing question difficulty, but as steering model behavior -- and propose ASH (Activation Steering for Hinting), a novel HA-GRPO method built on this view. During training, the model is presented with both hinted and plain questions, while a trainable steering vector is optimized to widen the margins between the model's generation probabilities for responses to the hinted version relative to the plain version, thereby capturing the question-agnostic component of the behavioral shift induced by the hint.

### 实验/数据
Experiments with four LLMs (Qwen3-1.7B/4B-Base, Llama-3.2-1B/3B-Instruct) show that ASH consistently improves pass@$k$ on competition-level mathematics benchmarks (AMC, OlympiadBench, AIME24, AIME25) and out-of-distribution benchmarks (Minerva, GPQA-Diamond).

### 结果
Experiments with four LLMs (Qwen3-1.7B/4B-Base, Llama-3.2-1B/3B-Instruct) show that ASH consistently improves pass@$k$ on competition-level mathematics benchmarks (AMC, OlympiadBench, AIME24, AIME25) and out-of-distribution benchmarks (Minerva, GPQA-Diamond). Notably, it improves average pass@8 of Qwen3-1.7B-Base and Qwen3-4B-Base by \textbf{2.60}\% and \textbf{2.21}\%.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Notably, it improves average pass@8 of Qwen3-1.7B-Base and Qwen3-4B-Base by \textbf{2.60}\% and \textbf{2.21}\%.

### 7. Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models

- 作者：Rui Ning, Om Chabra, Hari Balakrishnan｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.23228v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Applications such as visual accessibility agents and robotics require answering questions about recent video content promptly, over a bounded window of past frames (e.g., the last two minutes). Hybrid vision-language models (VLMs), which interleave attention with linear recurrent layers such as Gated DeltaNet (GDN), are attractive for this setting, but maintaining a sliding window is expensive.

### 方法
Hybrid vision-language models (VLMs), which interleave attention with linear recurrent layers such as Gated DeltaNet (GDN), are attractive for this setting, but maintaining a sliding window is expensive. The reason is that recurrent layers combine all past frames into a shared state, so expiring old frames normally requires re-running the entire window through the model. We present Spool, a training-free framework that caches per-frame state transformations and composes them efficiently as the window advances, removing expired frames from each recurrent layer's state without replaying frames through the backbone.

### 实验/数据
We design a dedicated data structure and GPU kernels to achieve low caching and composition overhead.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Across five open-source hybrid VLMs and four video reasoning benchmarks, Spool achieves the lowest p95 time-to-first-token in all 20 model-benchmark tests, reducing it by a geometric mean of $6.6\times$ over the faster of two recent vLLM baselines, while improving accuracy by 2.3 percentage points on average.

### 8. Higher-Scoring Coding Models Did Not Get More Work Done

- 作者：Yining Hua｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.23216v1

> 命中：hit_method=['difference-in-differences']

### 背景/问题
New coding models advertise themselves on score improvements of coding benchmarks. Yet no study has tested if a model that scores higher on these benchmarks gets more real work done.

### 方法
New coding models advertise themselves on score improvements of coding benchmarks. Yet no study has tested if a model that scores higher on these benchmarks gets more real work done. export control directive banned access to Claude Fable 5 for 19 days, which forced users to switch to other models.

### 实验/数据
We treat this suspension as a natural experiment, where the people and projects stayed the same and only the model changed, so we could isolate the effect of Fable 5 on user productivity.

### 结果
New coding models advertise themselves on score improvements of coding benchmarks. Fitting a difference-in-differences model with developer and date fixed effects, we found that having access to Fable 5 increased the 7-day merge rate of pull requests by only 1.4 percentage points [-1.4; +4.3], which was not statistically significant. Similarly, no significant increases of merge rates were found with the upgrades (weighted mean: -0.9 percentage points [-1.9; +0.2]); all five estimates were negative (95% intervals included 0, did not differ from each other).

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also did not observe a significant increase in the number of pull requests merged per week (+2.4% [-4.9%; +10.2%]).

### 9. Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents

- 作者：Viet K. Nguyen, Mohammad I. Husain｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.23202v1

> 命中：hit_abstract=['CATE']

### 背景/问题
AI agents increasingly collaborate across organizational boundaries, invoking tools and interacting with agents operated by independent entities. Although existing agent frameworks support planning and coordination, they lack a common mechanism for verifying cross-organizational agent identity, execution integrity, and authorization.

### 方法
Although existing agent frameworks support planning and coordination, they lack a common mechanism for verifying cross-organizational agent identity, execution integrity, and authorization. We propose the Agent Trust Infrastructure (ATI), a framework-independent security architecture built on Public Key Infrastructure (PKI), Zero Trust Architecture (ZTA), and remote attestation. Before executing requests, ATI validates agent certificates, verifies approved model, tool, and system-prompt configurations, and enforces authorization through three policy checks.

### 实验/数据
Security experiments involve two organizations and assess 14 attack scenarios and six benign tasks across five agent models, using five attack variations and three repetitions per variation. A panel of judge models evaluates the experimental outcomes.

### 结果
With all enforcement mechanisms enabled, attack containment increases from 43% to 84% (40% to 80% for the 11 attack scenarios evaluated consistently across all configurations), while enforcement introduces approximately 174 microseconds of overhead per request.

### 结论/启示（面向电商发券、定价、营销算法等应用）
ATI is released as an open-source, framework-independent package that uses IETF WIMSE workload token formats for identity and request verification and Entity Attestation Tokens for model, tool, and system-prompt integrity verification.

### 10. Richtmyer-Meshkov instability induced by a Gaussian-kicked rotor-like potential in a three-component Bose-Einstein condensate

- 作者：Susovan Giri｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.23171v1

> 命中：hit_abstract=['CATE']

### 背景/问题
This research investigates the Richtmyer-Meshkov instability within a three-component Bose-Einstein condensate. We offer a kicking potential that replicates the impulsive shock across both interfaces of the three-component BEC to trigger the Richtmyer-Meshkov instability.

### 方法
We propose a hydrodynamic model that indicates the essential criteria for the onset of hydrodynamic instability in the BEC through the application of the hydrodynamic pressure equation. Following this, we introduce a Gaussian-like disruption instigated by the kick rotor model at both interfaces of the confined three-component BEC to explore the time-dependent development of nonlinear hydrodynamic instability patterns, culminating in quantum turbulence and nonlinear configurations at the interfaces.

### 实验/数据
Following this, we introduce a Gaussian-like disruption instigated by the kick rotor model at both interfaces of the confined three-component BEC to explore the time-dependent development of nonlinear hydrodynamic instability patterns, culminating in quantum turbulence and nonlinear configurations at the interfaces.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
This research offers fresh perspectives on the mechanisms of hydrodynamic instability, vortex generation, non-equilibrium pattern evolution, and quantum turbulence in superfluid systems comprising multiple interacting elements.

### 11. A bordism perspective on ends of manifolds

- 作者：Fadi Mezher｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.23166v1

> 命中：hit_abstract=['CATE']

### 背景/问题
We refine the classical pro-homotopy type of the end of a manifold by recording the boundaries of a compact exhaustion together with the bordisms between them. We show that this assignment, the bordism-end, is functorial in embeddings, and independent of the choice of exhaustion.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we set up the pro-end functorially in embeddings, with target the cospan $\infty$-category of pro-spaces, and show that it factors through the bordism-end.

### 12. AI Companions for Young Adult Caregivers: Practical Advice, Emotional Depth, and the Limits of Metric Evaluation

- 作者：Trizal Garg, Xuelong Fu, Dhruv Shah, Jin Huang, Shrigopal Maheshwari, Atiksh Aggarwal, Yash Sinha, Dhruv Kumar 等｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.23147v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Young adult caregivers (YACs) are individuals aged 18 to 25 currently taking care of a family member, partner, or friend facing chronic illness. AI companions designed specifically for YACs remain underexplored in prior works.

### 方法
We present Carebot, it uses an open-weight LLM (Gemma 3-27B) as its base model, on which we compared fine-tuning, retrieval-augmented generation (RAG), and a combination of both. Three well-being experts evaluated these configurations and preferred the fine-tuned model for the warmth of its responses and its actionable advice tailored to YACs. Based on their choice, we adopted the fine-tuned model as Carebot's final configuration and used it for all subsequent evaluations.

### 实验/数据
The fine-tuning was performed based on an existing dataset of conversations with YACs and a psychologist.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We argue that support tools for YACs require situation-sensitive emotional depth and aligned evaluation frameworks to study their effectiveness.

### 13. Tropicalization and slow manifolds: A case study of the Michaelis--Menten reaction

- 作者：Kristian Uldal Kristiansen, Peter Szmolyan｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.23117v1

> 命中：hit_abstract=['CATE']

### 背景/问题
We present a case study of a recently developed approach to multiple-scale systems based on exponential scaling and tropicalization (Kristiansen and Sarantaris, \emph{On a tropicalization of planar polynomial ODEs}). Parameters and variables are scaled exponentially with respect to a small parameter $ε$, so that orders of magnitude become a genuine non-smooth singular limit $ε\to 0$.

### 方法
We present a case study of a recently developed approach to multiple-scale systems based on exponential scaling and tropicalization (Kristiansen and Sarantaris, \emph{On a tropicalization of planar polynomial ODEs}). Here we combine this framework with blow-up and geometric singular perturbation theory.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In particular, there is an asymptotic regime of parameters where there is no global slow manifold of the Michaelis--Menten reaction.

### 14. A Reidemeister-type theorem for vineyards

- 作者：Erin Chambers, Christopher Fillmore, Shankha Shubhra Mukherjee, Rohit Roy, Elizabeth Stephenson, Mathijs Wintraecken｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.23099v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Closed vineyards record how persistent homology changes along a periodic family of filtrations. Their topology can be surprisingly complicated, with recent work showing that vines may exhibit nontrivial monodromy even in very simple settings, and more generally that every link can occur in a closed vineyard.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The 2D case already exhibits very rich behaviour, and we conjecture that in fact it captures all possible generic changes in vineyards.

### 15. CFTs with Large Virasoro Primary Gaps

- 作者：Ziming Ji, Jiahua Tian｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23231v1

### 背景/问题
We construct the first explicit examples of compact unitary bosonic full conformal field theories (CFTs) in two dimensions with a unique vacuum and an all-spin Virasoro-primary gap greater than two. Our constructions use asymmetric orbifolds of lattice CFTs built from even unimodular lattices of sufficiently large minimum norm, ensuring that no charged state lies below the desired gap.

### 方法
未在摘要中明确给出。

### 实验/数据
We construct the first explicit examples of compact unitary bosonic full conformal field theories (CFTs) in two dimensions with a unique vacuum and an all-spin Virasoro-primary gap greater than two.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also obtain two additional examples, with gap three at $(c_L,c_R)=(48,48)$ and gap four at $(c_L,c_R)=(512,512)$.

### 16. Equilibrium Statistics and Stability in Random Two-Population and Three-Population Evolutionary Games

- 作者：Zhao Song, Manh Hong Duong, The Anh Han｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23223v1

### 背景/问题
Multi-population matrix evolutionary games provide a framework for studying adaptation and strategic interactions among heterogeneous agents. When payoffs are uncertain, however, analysing a specified game does not reveal how frequently different evolutionary outcomes occur or how their probabilities depend on modelling assumptions.

### 方法
Multi-population matrix evolutionary games provide a framework for studying adaptation and strategic interactions among heterogeneous agents. When payoffs are uncertain, however, analysing a specified game does not reveal how frequently different evolutionary outcomes occur or how their probabilities depend on modelling assumptions.

### 实验/数据
Monte Carlo simulations support the analytical predictions and quantify multistability, while phase portraits illustrate initial-condition dependence. Under the same Gaussian payoff-sampling protocol, simulations show a lower frequency of fully mixed equilibria but a higher frequency of multistability for three populations than for two.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Under the same Gaussian payoff-sampling protocol, simulations show a lower frequency of fully mixed equilibria but a higher frequency of multistability for three populations than for two.

### 17. An inexact stochastic variance-reduced gradient method for constrained convex finite-sum optimization

- 作者：Zhaosong Lu, Yifeng Xiao｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23221v1

### 背景/问题
In this paper, we study a class of constrained convex finite-sum optimization problems. In many practical applications, all or some of the constraints are hard constraints that represent imperative requirements.

### 方法
While a recently proposed stochastic variance-reduced first-order penalty method can compute an $ε$-SFSO solution, there remains a significant gap between its first-order oracle complexity for computing an $ε$-SFSO solution and that for computing an $ε$-$expected\ feasible\ stochastic\ optimal$ solution, where both the expected constraint violation and the expected optimality gap are bounded by $ε$. To narrow this gap, we propose an inexact stochastic variance-reduced gradient (SVRG) method that significantly improves the previously best-known first-order oracle complexity for computing an $ε$-SFSO solution. Furthermore, when the objective consists of a single function, the proposed method reduces to a novel deterministic first-order method for solving standard convex conic optimization.

### 实验/数据
未在摘要中明确给出。

### 结果
While a recently proposed stochastic variance-reduced first-order penalty method can compute an $ε$-SFSO solution, there remains a significant gap between its first-order oracle complexity for computing an $ε$-SFSO solution and that for computing an $ε$-$expected\ feasible\ stochastic\ optimal$ solution, where both the expected constraint violation and the expected optimality gap are bounded by $ε$. To narrow this gap, we propose an inexact stochastic variance-reduced gradient (SVRG) method that significantly improves the previously best-known first-order oracle complexity for computing an $ε$-SFSO solution. It achieves a significantly lower gradient evaluation complexity with respect to the objective function compared to existing methods, and can outperform them when computing constraint gradients and projections onto the associated cone is cheaper than evaluating the objective gradient.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Preliminary numerical results are presented to illustrate the performance of the proposed method.

### 18. EviSlide-MIL: Multi-Query Pooling and Shared Prediction for Class-Incremental Whole-Slide Image Classification

- 作者：Zhouhan Qian, Sicheng Chen, Chad Wong, Tianyi Zhang, Enhui Chai, Zeyu Liu, Fei Xia｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23212v1

### 背景/问题
Histopathological analysis of whole-slide images (WSIs) plays a critical role in cancer diagnosis, and multiple instance learning (MIL) is widely adopted for WSI analysis under weak supervision. As new tumor subtypes are introduced, extending existing MIL models requires learning new classes while retaining knowledge of previously learned ones.

### 方法
As new tumor subtypes are introduced, extending existing MIL models requires learning new classes while retaining knowledge of previously learned ones. This presents a class-incremental learning challenge, where models must acquire new classes with limited access to historical training data and recognize all learned classes without task identifiers at inference. To address this challenge, we propose \textbf{EviSlide-MIL}, a class-incremental WSI framework that integrates multiple learnable queries per class with a shared prediction module.

### 实验/数据
This presents a class-incremental learning challenge, where models must acquire new classes with limited access to historical training data and recognize all learned classes without task identifiers at inference. Experiments on eight tumor subtypes from The Cancer Genome Atlas demonstrate that EviSlide-MIL achieves improved performance and reduced forgetting compared with competing methods across most learning settings, demonstrating its potential for scalable and knowledge-preserving WSI classification.

### 结果
Experiments on eight tumor subtypes from The Cancer Genome Atlas demonstrate that EviSlide-MIL achieves improved performance and reduced forgetting compared with competing methods across most learning settings, demonstrating its potential for scalable and knowledge-preserving WSI classification.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Code and pretrained models will be released.

### 19. Fine-Tuning Gemma 4 Edge Models for MATLAB Signal-Processing Code with SFT and QLoRA on a Laptop iGPU

- 作者：Mehmet Altan Toksöz｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23205v1

### 背景/问题
Small language models that run on a laptop are attractive for writing signal-processing code offline, but they make systematic errors on digital signal processing (DSP) conventions. We apply supervised fine-tuning (SFT) to the Gemma 4 edge models E2B and E4B with 66 checked examples covering 11 signal-processing MATLAB subtasks, using low-rank adaptation (LoRA) and quantized LoRA (QLoRA) on the integrated GPU (iGPU) of a laptop, and deploy the 8-bit integer (int8) models with the adapters through OpenVINO.

### 方法
Small language models that run on a laptop are attractive for writing signal-processing code offline, but they make systematic errors on digital signal processing (DSP) conventions. We apply supervised fine-tuning (SFT) to the Gemma 4 edge models E2B and E4B with 66 checked examples covering 11 signal-processing MATLAB subtasks, using low-rank adaptation (LoRA) and quantized LoRA (QLoRA) on the integrated GPU (iGPU) of a laptop, and deploy the 8-bit integer (int8) models with the adapters through OpenVINO.

### 实验/数据
Small language models that run on a laptop are attractive for writing signal-processing code offline, but they make systematic errors on digital signal processing (DSP) conventions.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Applied at run time, the adapter costs 17-19% of the generation speed.

### 20. Identifying and Repairing Energy Smells with Agent Skills

- 作者：Mohammadjavad Mehditabar, Saurabhsingh Rajput, Tushar Sharma｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23203v1

### 背景/问题
Energy smells are inefficient implementations that waste energy. Once code reaches production, these smells become costlier and riskier to fix, so energy efficiency checks should shift left, i.e., move earlier in the development lifecycle, to where code is written.

### 方法
To address both limitations, we present DR. GREENS in 18 sessions on three open-source repositories, with two models and three skill configurations. Compared with a baseline skill that lacks the taxonomy, the full skill found more energy smells with verified savings in all three repositories with both models.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
GREENS helps developers detect energy hotspots and fix them reliably without altering program behavior, which makes energy-efficient development more feasible.

### 21. Global genetic inference at the scale of mass disasters

- 作者：Yourie Weesie, Ritsaart Bergsma, Aafko Boonstra｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23194v1

### 背景/问题
DNA-based disaster victim identification is commonly performed sequentially, with matches accepted before all genetic evidence is considered jointly. However, early matches may be incorrect or inconsistent with the globally most likely assignment, and treating them as final can affect subsequent identifications.

### 方法
In this paper, we show that the general joint identification problem is NP-hard and develop a local-to-global framework for joint genetic inference at scale. The framework is not limited to a single global optimum but yields a list of probable alternative assignments, thus providing a flexible tool to be used alongside other forensic evidence.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The framework is not limited to a single global optimum but yields a list of probable alternative assignments, thus providing a flexible tool to be used alongside other forensic evidence.

### 22. WoRD: Diffusion-Based Posterior Inference for Online Goal Recognition

- 作者：Almog Anschel, Sarah Keren｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23192v1

### 背景/问题
Goal recognition is the task of inferring an agent's intended goal from its observed behavior. Most existing work focuses on high-level symbolic recognition, abstracting away the continuous motion through which agents reach their goal.

### 方法
Methods that do reason over continuous trajectories rely on an explicit dynamics model that is hard to acquire and rarely transfers across settings. Neither approach explicitly learns how agents move toward each candidate goal, limiting accuracy on ambiguous trajectory prefixes where such knowledge is most needed. We present WoRD (Waypoint Recognition with Diffusion), which uses a learned trajectory prior to infer the agent's goal from partial observations.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Across all three settings, the same inference procedure preserves calibrated multimodal beliefs through ambiguous prefixes where filter- and classifier-based observers collapse to a single mode or grow overconfident.

### 23. Fold Weighting for Cross-Validation Under Continuous Distributional Drift

- 作者：Yegor Baranovski｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23184v1

### 背景/问题
Cross-validation weights all folds equally, so under drift the oldest folds count as much as the newest. We model drift by a Hölder condition in total variation distance and give finite-sample bounds on the excess deployment risk of the configuration that sliding-window cross-validation selects.

### 方法
We model drift by a Hölder condition in total variation distance and give finite-sample bounds on the excess deployment risk of the configuration that sliding-window cross-validation selects.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Weight on recent folds pays off when a change in the best predictor persists and each period has many observations, and equal weights do best when changes are short-lived.

### 24. Fully Spiking Neural Implementation of Lambda-Calculus Beta-Reduction via Biologically Documented Mechanisms

- 作者：Vladimir A. Lazovskiy, Victor B. Kazantsev, Sergey V. Stasenko｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23182v1

### 背景/问题
We present the first complete implementation of $β$-reduction in the untyped $λ$-calculus using exclusively spiking neural dynamics. Every step of the reduction---redex detection, subterm segmentation, variable-binding detection, De~Bruijn index arithmetic, token copying, and inter-step role maintenance---is performed by leaky integrate-and-fire (LIF) neurons with explicit membrane dynamics, exponential synaptic currents, axonal delays, and pair-based spike-timing-dependent plasticity (STDP).

### 方法
We present the first complete implementation of $β$-reduction in the untyped $λ$-calculus using exclusively spiking neural dynamics.

### 实验/数据
Each neural component maps onto a specific, experimentally documented mechanism: Jeffress-type delay-line coincidence for redex detection; a line-attractor balance counter for subterm segmentation; $θ$--$γ$ cross-frequency coupling for De~Bruijn variable binding; a phase-ring traveling wave for depth-index arithmetic; theta-cycle STDP for token copying; and recurrent persistent firing for role maintenance between reduction steps.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We discuss implications for neuromorphic proof assistants and the neural basis of symbolic reasoning.

### 25. Dynamics-preserving graph sparsification

- 作者：Emmie Fitz-Gibbon, Maximilian Jerdee, Yuanzhao Zhang, Rosemary Braun, Cristopher Moore｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23176v1

### 背景/问题
Many dynamical systems unfold on networks of nodes coupled by edge interactions. This work is motivated by the following question: can we remove most edges from a networked dynamical system without significantly altering its behavior?

### 方法
Although derived in a linear context, we empirically find that DSE sparsification gives similar improvements in the Kuramoto model (a nonlinear system of coupled oscillators), where DSE sparsification approximately preserves the synchronization threshold and, at strong coupling, order-parameter trajectories.

### 实验/数据
Although derived in a linear context, we empirically find that DSE sparsification gives similar improvements in the Kuramoto model (a nonlinear system of coupled oscillators), where DSE sparsification approximately preserves the synchronization threshold and, at strong coupling, order-parameter trajectories.

### 结果
This work is motivated by the following question: can we remove most edges from a networked dynamical system without significantly altering its behavior? Although derived in a linear context, we empirically find that DSE sparsification gives similar improvements in the Kuramoto model (a nonlinear system of coupled oscillators), where DSE sparsification approximately preserves the synchronization threshold and, at strong coupling, order-parameter trajectories.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Although derived in a linear context, we empirically find that DSE sparsification gives similar improvements in the Kuramoto model (a nonlinear system of coupled oscillators), where DSE sparsification approximately preserves the synchronization threshold and, at strong coupling, order-parameter trajectories.

### 26. Finding Patient Zero in Temporal Contact Networks: A Comparative Study

- 作者：Nathan Cincera Brack, Martin Sterchi, Lorenz Hilfiker, Abraham Bernstein｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23175v1

### 背景/问题
Identifying the source of an epidemic, i.e., the patient zero, in a temporal contact network is important for effective outbreak containment and resource allocation. While several methods have been proposed for this task, they have rarely been evaluated under comparable conditions, and no systematic comparison exists for temporal contact networks.

### 方法
Identifying the source of an epidemic, i.e., the patient zero, in a temporal contact network is important for effective outbreak containment and resource allocation. While several methods have been proposed for this task, they have rarely been evaluated under comparable conditions, and no systematic comparison exists for temporal contact networks. We identify scaling these methods to larger networks as the most pressing direction for future work.

### 实验/数据
We address this gap with a comparative study of seven major methods, namely Steiner Tree (ST), Individual-Based Approximation (IBA), Dynamic Message Passing (DMP), Monte Carlo Mean-Field (MCMF), Soft Margin Estimator (SME), Backtracking Network (BN, a graph neural network), and Belief Propagation (BP). In the main experiment, we compare source detection performance for varying basic reproduction numbers. Three complementary experiments on a subset of networks study (i) learning curves, (ii) partial observability, and (iii) parameter misspecification.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We identify scaling these methods to larger networks as the most pressing direction for future work.

### 27. The Pfaffian sector of $\mathrm{SO}(2N)$ BPS cohomology: brane excitations, triality and fortuity

- 作者：Zheng Miao, Yuezhang Tang｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23173v1

### 背景/问题
We study the classical $\frac{1}{16}$-BPS cohomology of $\mathcal{N}=4$ super-Yang-Mills theory with gauge group $\mathrm{SO}(2N)$ in the BMN sector, including the operators built with one $ε$-tensor. These operators are odd under the reflection in $\mathrm{O}(2N)$, carry the $\mathbb{Z}_2$ charge of a D3-brane wrapped on $\mathbb{RP}^3\subset\mathbb{RP}^5$, and form the Pfaffian sector.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
The two classes restrict, along the spinor and the vector embedding of $\mathfrak{so}(7)$ respectively, to the known non-graviton singlet of $\mathrm{SO}(7)$, which is lifted at first order. Their protection is compatible with the lifting in $\mathrm{SO}(7)$ because restriction to a subalgebra does not commute with the quantum corrections to the supercharge.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Their protection is compatible with the lifting in $\mathrm{SO}(7)$ because restriction to a subalgebra does not commute with the quantum corrections to the supercharge.

### 28. Quantum simulation of neutral-meson mixing and decay on a reprogrammable photonic processor

- 作者：Mohd Abu Bakar Siddique, Abrar Al Shadid Abir, A. K. M. Rakib, Mohammad Abrar Kabir, Aseer Imad Keats, Rakibul Hasan Sagor｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23156v1

### 背景/问题
Neutral mesons oscillate into their antiparticles while decaying, so their dynamics is generated by a non-Hermitian effective Hamiltonian which a quantum simulator restricted to unitary operations cannot implement directly. We propose a reprogrammable photonic processor that simulates this open-system evolution through dilation and analyze it at the circuit level.

### 方法
We propose a reprogrammable photonic processor that simulates this open-system evolution through dilation and analyze it at the circuit level.

### 实验/数据
Circuit simulations including coupler, propagation, and bend losses show that one fixed device, reprogrammed only through its control voltages, reproduces the flavor oscillation and decay of neutral kaons and of $B_d$ and $B_s$ mesons, with $x=Δm/Γ$ from 0.77 to 26.9.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The ancillary outputs encode the total decay probability without postselection, and the reported probabilities are normalized to the collected optical power.

### 29. GameRealm: Grounding Visual Learning in Interactive Games

- 作者：Weiguang Zhao, Yifan Wang, Ni Yang, Yating Wang, Xingyu Miao, Yankai Jiang, Mulin Yu, Tao Lu 等｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23140v1

### 背景/问题
Visual foundation models are central to physical intelligence, yet their development remains constrained by fragmented training datasets, inconsistent annotation quality, and limited multimodal supervision. To address these challenges, we introduce GameRealm, a large-scale, richly annotated dataset that grounds visual observations in synchronized, game-native supervision.

### 方法
Visual foundation models are central to physical intelligence, yet their development remains constrained by fragmented training datasets, inconsistent annotation quality, and limited multimodal supervision. To enable scalable acquisition across diverse game environments, we develop a unified data collection pipeline that combines human-operated interaction with agentic exploration. Extensive experiments across diverse visual learning tasks demonstrate that GameRealm consistently strengthens visual foundation models in both visual generation and geometric learning.

### 实验/数据
Visual foundation models are central to physical intelligence, yet their development remains constrained by fragmented training datasets, inconsistent annotation quality, and limited multimodal supervision. To address these challenges, we introduce GameRealm, a large-scale, richly annotated dataset that grounds visual observations in synchronized, game-native supervision. To enable scalable acquisition across diverse game environments, we develop a unified data collection pipeline that combines human-operated interaction with agentic exploration.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results establish GameRealm as a versatile and valuable data resource, unlocking new opportunities for advancing visual intelligence.

### 30. OpenPINN/PINO: An Extensible Open-Source Framework for Agent-Assisted Physics-Informed Neural Networks and Neural Operators

- 作者：Xi Wang, Jun Lu, Cheng Zhang, Xiaoying Zhuang, Timon Rabczuk, Hehua Zhu, Wei Wu, Peinan Li 等｜年份：2026｜发布时间：2026-11-17｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.23135v1

### 背景/问题
Substantial challenges in physics-informed learning have motivated many improvements, but fragmented implementations hinder systematic organization, integration, and comparison. We propose OpenPINN/PINO, an extensible open-source PyTorch framework for physics-informed neural networks and neural operators.

### 方法
We propose OpenPINN/PINO, an extensible open-source PyTorch framework for physics-informed neural networks and neural operators. MethodSpec configures the model, sampling, loss, optimization, and differentiation. Agents translate natural-language descriptions into specifications, flag missing information, and propose solver plans.

### 实验/数据
ProblemSpec defines geometry, governing equations, constitutive relations, parameters, initial and boundary conditions, and optional data.

### 结果
Substantial challenges in physics-informed learning have motivated many improvements, but fragmented implementations hinder systematic organization, integration, and comparison.

### 结论/启示（面向电商发券、定价、营销算法等应用）
After initial training failure, all three runs met the $10\%$ target, with relative $L^2$ displacement errors of $3.51\%$--$6.31\%$.
