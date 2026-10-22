# CausalRadar 日报 - 2026-10-22

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. VX-One: Typed, Calibrated Decision Heads for Real-Time Perimeter Triage - An empirical study of unknown-attack honesty, cascade gray zones, and calibration under drift

- 作者：Juan S. Santillana｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**9.00**
- 链接：https://arxiv.org/abs/2610.30090v1

> 命中：hit_scenario=['ads']；hit_title=['ads']

### 背景/问题
Perimeter triage faces a latency/semantics trade-off: signature engines are fast and format-safe but blind to unseen attacks, while generative models are semantic but slow and produce unparseable output. In late 2026 a class of commercial System One decision models (TypeSafe Jev; Microsoft-Decision-1) began selling typed decision primitives - binary gates, closed-set choices, ordinal scores - as product APIs, with no academic treatment.

### 方法
Perimeter triage faces a latency/semantics trade-off: signature engines are fast and format-safe but blind to unseen attacks, while generative models are semantic but slow and produce unparseable output. In late 2026 a class of commercial System One decision models (TypeSafe Jev; Microsoft-Decision-1) began selling typed decision primitives - binary gates, closed-set choices, ordinal scores - as product APIs, with no academic treatment. We present VX-One: a small multi-head network (100K-10M parameters) whose outputs are these primitives - a calibrated gate, a choice over a closed candidate set that always includes an explicit unknown option, and an ordinal score, trained multi-task, temperature-calibrated per head (~0.7-1.7 ms p50 on CPU).

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We provide a measured account of where typed calibrated decisions help perimeter triage, and where they fail.

### 2. From Classifier Heads to Encoder Prototypes: Personalized Federated Learning with Head-Derived Clustering

- 作者：Amirardalan Dehghanpour, Arian Noori, Ehsan Tanghatari, Naimeh Omidvar, Hamid R. Rabiee｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**9.00**
- 链接：https://arxiv.org/abs/2610.30075v1

> 命中：hit_scenario=['ads']；hit_title=['ads']

### 背景/问题
Personalized federated learning must decide which clients should share representations. We introduce HDC-FL (Head-Derived Clustering for Personalized Federated Learning), which reads that decision off a signal shared-encoder training already produces: the client-specific classifi- er heads.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
A controlled donor-swap diagnostic further finds positive donor-ranking associations between head similarity and encoder compatibility in all three settings tested, most clearly under covariate shift.

### 3. Pre-emptive Carbon Aware Scheduling for Edge Workloads

- 作者：Cecilia Chen, Rajni Dabas, Samir Khuller, Emilie Rivkin｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**9.00**
- 链接：https://arxiv.org/abs/2610.29945v1

> 命中：hit_scenario=['ads']；hit_title=['ads']

### 背景/问题
Power grids use a constantly changing mix of fossil fuels and clean renewables like solar and wind. Because of this, the {\em carbon footprint} fluctuates drastically based on time and geographic location.

### 方法
Jobs execute preemptively on a single edge server or are outsourced at job-dependent costs to an unlimited-capacity cloud, modeled as providing instantaneous execution.

### 实验/数据
We complement these theoretical results with experiments on controlled synthetic workloads and production-derived Alibaba traces.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
On synthetic instances, our incremental max-flow implementation is $4.96\times$ faster on average than a direct min-cost flow, while experiements on production-derived workloads evaluate its performance under realistic job structures.

### 4. Injection is all you need: parallel universal logic in high-rate concatenated self-dual codes

- 作者：Joseph Sullivan, David Amaro, Michael A. Perlin｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**8.50**
- 链接：https://arxiv.org/abs/2610.30087v1

> 命中：hit_title=['CATE']；hit_abstract=['CATE']

### 背景/问题
We propose a quantum architecture that achieves addressable and parallel universal fault-tolerant logical in high-rate codes. The codes are obtained from the flexible concatenation of small-distance high-rate self-dual CSS codes.

### 方法
We propose a quantum architecture that achieves addressable and parallel universal fault-tolerant logical in high-rate codes.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In particular, we find that the concatenated cultivation offers at least one order of magnitude spacetime reduction compared to cultivation in the surface code.

### 5. CAQ: Clustered Asymptotically Anytime-Valid Quantile Treatment Effects for Online Experiments

- 作者：Diane Lu, Eric J. Oh｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**6.50**
- 链接：https://arxiv.org/abs/2610.30019v1

> 命中：hit_title=['treatment effect']

### 背景/问题
Confidence sequences let an experiment be monitored continuously without inflating error, but the existing constructions for quantiles assume that observations arrive independently. In online experiments this rarely holds: randomization assigns users, while the metric is computed over the many correlated events each user generates, so intervals built for independent data are too narrow and miss the truth more often than their nominal rate allows.

### 方法
We propose CAQ, a confidence sequence for a quantile that is both robust to this within-user dependence and valid at arbitrary stopping times, together with a sequential test for the difference in a quantile between two treatment arms.

### 实验/数据
Confidence sequences let an experiment be monitored continuously without inflating error, but the existing constructions for quantiles assume that observations arrive independently. In online experiments this rarely holds: randomization assigns users, while the metric is computed over the many correlated events each user generates, so intervals built for independent data are too narrow and miss the truth more often than their nominal rate allows. The width adapts to the dependence actually present, widening beyond the independent-data benchmark only when correlation within users is strong.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In simulations, CAQ is the only method we tested that holds both coverage and false-positive rate at their nominal levels across clustering strengths and heavy-tailed data, while the fixed-horizon baseline fails under continuous monitoring and the independence-assuming sequential baseline fails as within-user correlation grows.

### 6. Charts as Epistemic Actions for Experience-Driven Agentic Data Analysis

- 作者：Xinzhe Wang, Xudong Weng, Zang Li, Shaolei Zhang｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.30072v1

> 命中：hit_scenario=['ads']

### 背景/问题
Data agents built on ReAct-style loops now execute complex analytical workflows over structured data, yet their intermediate reasoning still runs almost entirely through text. Human analysts instead move between numbers, tables, and charts, reading visual evidence to expose trends and anomalies that text summaries drop.

### 方法
We then propose \method{}, which distils two families of experience from conditioned trajectory rollouts. On three held-out benchmarks with four LLM backbones, \method{} raises analytical accuracy and visual evidence quality over matched baselines, and backbones that never drew charts begin using them, all without touching model parameters.

### 实验/数据
Data agents built on ReAct-style loops now execute complex analytical workflows over structured data, yet their intermediate reasoning still runs almost entirely through text. We ask whether charts can serve as internal epistemic actions inside a data agent's reasoning loop, and how to teach an agent to use them.

### 结果
A trajectory judge scores outcomes and labels intermediate steps, and a validation gate admits only experience that improves held-out performance.

### 结论/启示（面向电商发券、定价、营销算法等应用）
On three held-out benchmarks with four LLM backbones, \method{} raises analytical accuracy and visual evidence quality over matched baselines, and backbones that never drew charts begin using them, all without touching model parameters.

### 7. Generalized Coordinate Bethe Ansatz and Quantum Integrability of the Time-Dependent Massive Thirring Model

- 作者：Parameshwar R. Pasnoori｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.29998v1

> 命中：hit_scenario=['ads']

### 背景/问题
We develop a generalized coordinate Bethe-ansatz framework for the massive Thirring model with an explicitly time-dependent fermion mass. Unlike the generalized Bethe ansatz for chiral quantum field theories, where particle transport acts in internal spin spaces and leads to quantum Knizhnik-Zamolodchikov equations, the present construction acts directly on particle coordinates and physical rapidities.

### 方法
We develop a generalized coordinate Bethe-ansatz framework for the massive Thirring model with an explicitly time-dependent fermion mass.

### 实验/数据
Unlike the generalized Bethe ansatz for chiral quantum field theories, where particle transport acts in internal spin spaces and leads to quantum Knizhnik-Zamolodchikov equations, the present construction acts directly on particle coordinates and physical rapidities.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Through the massive-Thirring/sine Gordon equivalence, the result also connects this exact quantum construction to the generalized space-time dependent Lax formalism.

### 8. Temporal Exploration and Rendezvous via Weisfeiler-Leman Colorings

- 作者：Frank Kammer, Sandra Kiefer, Johannes Meintrup｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.30123v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Temporal graphs are graphs whose edge relation changes in discrete time steps. The Temporal Exploration Problem (TEXP) asks for a temporal walk that visits all vertices.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
For small $q$, our bound substantially improves on the known worst-case bound of $Θ(n^2)$ in general connected temporal graphs. Our contribution improves upon these results in several ways.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Third, we provide novel deterministic polynomial-time algorithms for both TEXP and TRP.

### 9. Relation of Rotation and Pulsation Properties in $γ$ Doradus Stars

- 作者：Á. Sódor, E. Plachy, Zs. Bognár｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.30029v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Connection between stellar rotation and pulsation amplitude has been proposed for several types of pulsating variable stars, but no such relation has been established for gamma Doradus stars from spectroscopic v sin i measurements. A high-amplitude gamma Dor subclass was also suggested recently, which had not been explored by spectroscopic means before.

### 方法
Connection between stellar rotation and pulsation amplitude has been proposed for several types of pulsating variable stars, but no such relation has been established for gamma Doradus stars from spectroscopic v sin i measurements. We also performed rotation- and inclination-dependent mode visibility modelling relying on GYRE Hough functions with TAR visibilities for the interpretation of our results. Visibility modelling indicates that these trends cannot be explained by geometric effects alone, suggesting that the intrinsic pulsation amplitudes of gamma Dor stars physically decrease with increasing equatorial rotational velocity.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Furthermore, the strong suppression of zonal dipole mode visibility at high rotation suggests that high-amplitude gamma Dor stars are likely slow rotators or moderate rotators viewed nearly pole-on.

### 10. ExGrad: Beyond Suppression - Explicit Clean-Gradient Subtraction in Adversarial Training

- 作者：Zhiyuan Ye, Xiangyu Zhou, Ji Qi, Hao Zhang, Yi Zhou｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.30018v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Adversarial training derives updates from surrogate losses, but source-loss descent does not directly characterize an update's effect on adversarial margins. We introduce ExGrad (extrapolative gradient recomposition), which constructs clean-input, adversarial-input, and adversarial-weight-perturbed (AWP) gradients.

### 方法
These results identify clean-gradient subtraction as a response-revealed update preference whose strength and clean-robust operating point are controlled by the affine radius.

### 实验/数据
Experiments on CIFAR-10, CIFAR-100, and ImageNet-100 show radius-dependent improvements over AWP.

### 结果
Across affine radii on CIFAR-10, negative clean coefficients rapidly predominate and increase in magnitude with the radius. Cross-zero interventions show that setting the clean coefficient to zero is insufficient: mild subtraction improves PGD-20, while stronger subtraction trades clean accuracy for further PGD-20 gains. Experiments on CIFAR-10, CIFAR-100, and ImageNet-100 show radius-dependent improvements over AWP.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results identify clean-gradient subtraction as a response-revealed update preference whose strength and clean-robust operating point are controlled by the affine radius.

### 11. The Price of Current-Effect Inference in Nonstationary Multi-Armed Bandits

- 作者：Sharan Sahu, Martin T. Wells｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.29982v1

> 命中：hit_abstract=['treatment effect']

### 背景/问题
Adaptive experiments use bandit algorithms to favor interventions with higher expected rewards. However, decision-makers also require reliable inference on current treatment effects: differences between intervention and reference-arm mean rewards at the present time, rather than historical averages.

### 方法
未在摘要中明确给出。

### 实验/数据
Adaptive experiments use bandit algorithms to favor interventions with higher expected rewards. Finally, we show that regret constraints can prevent honest adaptation to unknown smoothness and support our theory with extensive numerical experiments.

### 结果
These objectives conflict: reward maximization favors better interventions, whereas current-effect inference requires continued exploration of potentially suboptimal interventions as outcomes change over time.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we show that regret constraints can prevent honest adaptation to unknown smoothness and support our theory with extensive numerical experiments.

### 12. Optimal galaxy magnification: generalized fundamental-plane residuals and number counts are all you need

- 作者：Kun Xu, Ravi K. Sheth｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30133v1

### 背景/问题
Weak-lensing magnification complements cosmic shear through its effects on galaxy fluxes, sizes, and number counts. We derive the optimal magnification statistics from galaxy properties and show that the optimal measurement can be decomposed into an optimal mean statistic and total number counts.

### 方法
This provides a simple and physically intuitive optimal compression of the full magnification likelihood, avoiding the need to model the potentially high-dimensional galaxy-property distribution, particularly when additional observables are incorporated to reduce the GFP scatter.

### 实验/数据
未在摘要中明确给出。

### 结果
The function $F$ can take any form that reduces the intrinsic scatter and thereby improves magnification precision.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our results demonstrate that GFP residuals and number counts provide an optimal combination for weak-lensing magnification measurements in galaxy surveys.

### 13. ALPS: Visual State Encoders for World Models

- 作者：Yanqing Liu, Letian Zhang, Chengzhi Liu, Zijun Wang, Jieru Mei, Hongliang Fei, Yuyin Zhou, Cihang Xie｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30120v1

### 背景/问题
World models turn visual representations into predictions and actions. We argue that their visual foundation should combine physical-state information, native language alignment, and pixel reconstruction, so that a single representation can support prediction, instruction, and inspection.

### 方法
World models turn visual representations into predictions and actions. In a unified evaluation across fifteen public encoders, ALPS achieves the lowest aggregate LIBERO state-probe error among ViT-B models (matching the 3.5x larger V-JEPA 2-L) while maintaining strong language alignment and accurate pixel reconstruction. Downstream, frozen ALPS tokens reach the highest mean policy success on LIBERO (85.5%) when paired with our native text tower, match or exceed leading encoders on world-model planning across PushT, Wall, and Granular, and allow predicted future tokens to be decoded directly into pixels for visual inspection.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We hope this work helps establish visual pretraining as a shared foundation for understanding, prediction, and action in world models.

### 14. Self-normalized Bernstein Inequalities for Regenerative Processes and Applications to Learning Without Independence

- 作者：Imon Banerjee, Pierre Alquier｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30119v1

### 背景/问题
We prove a self-normalized Bernstein inequality for bounded functions of a regenerative process with independent, identically distributed marked cycles of finite mean length. The bound uses observed cycle lengths and retains explicit terms for truncation and the cycle ending after the observation horizon.

### 方法
未在摘要中明确给出。

### 实验/数据
This is important for applications in machine learning: we prove generalization error bounds for classification with non-i.i.d., regenerative data.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we combine the Bernstein inequality with a regenerative strong approximation to obtain a Gaussian approximation using an observable block variance estimator.

### 15. Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use

- 作者：Yanzhe Chen, Ziyi Yang, Jifeng Zhu, Qiming Huang, Ruihe An, Peiyao Xu, Hesen Yang, Runda Liu 等｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30108v1

### 背景/问题
Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed systems that couple multimodal task reasoning with physical action and revise decisions from the resulting feedback.

### 方法
We introduce PAPAV, a unified capability-centric framework of five recurring functions: Perceive the current state, Anticipate action effects, Plan a feasible course, Act through an interface or body, and Verify the outcome. Defined by function rather than architecture, these capabilities let PAPAV identify what all three share and then compare MMEAs with MMAs and with RSs. These constraints also frame the open challenges we identify.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
PAPAV therefore provides a common basis for designing reliable physical agents and measuring progress across all five capabilities rather than task success alone.

### 16. A linear, second-order, unconditionally energy-stable scalar-auxiliary-variable scheme for the CHQ viscoelastic phase-separation model

- 作者：Ritesh Bhola, Michael te Vrugt｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30077v1

### 背景/问题
The CHQ model describes viscoelastic phase separation in a polymer--solvent mixture: a Cahn--Hilliard equation for the polymer volume fraction $φ$ is two-way coupled, through a phase-dependent cross-diffusion flux, to a damped relaxation equation for a scalar bulk elastic stress $q$. We propose a scalar-auxiliary-variable (SAV) time discretisation of this system, combining the SAV reformulation of the double-well potential with a second-order backward differentiation formula (BDF2) and a second-order extrapolation of all phase-dependent mobilities: a linear, computationally cheaper complement to the reference scheme's fully nonlinear Newton solve.

### 方法
The CHQ model describes viscoelastic phase separation in a polymer--solvent mixture: a Cahn--Hilliard equation for the polymer volume fraction $φ$ is two-way coupled, through a phase-dependent cross-diffusion flux, to a damped relaxation equation for a scalar bulk elastic stress $q$. We propose a scalar-auxiliary-variable (SAV) time discretisation of this system, combining the SAV reformulation of the double-well potential with a second-order backward differentiation formula (BDF2) and a second-order extrapolation of all phase-dependent mobilities: a linear, computationally cheaper complement to the reference scheme's fully nonlinear Newton solve.

### 实验/数据
We propose a scalar-auxiliary-variable (SAV) time discretisation of this system, combining the SAV reformulation of the double-well potential with a second-order backward differentiation formula (BDF2) and a second-order extrapolation of all phase-dependent mobilities: a linear, computationally cheaper complement to the reference scheme's fully nonlinear Newton solve. It also confirms second-order temporal accuracy, including in the steep-interface regime, and agreement with an independently implemented nonlinear Newton--BDF2 solver. Compared with that independent nonlinear Newton--BDF2 solver, at equal grid resolution, the SAV method uses $2.5$--$3.0\times$ fewer linear-solver iterations and $1.7$--$2.0\times$ less wall-clock time.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Compared with that independent nonlinear Newton--BDF2 solver, at equal grid resolution, the SAV method uses $2.5$--$3.0\times$ fewer linear-solver iterations and $1.7$--$2.0\times$ less wall-clock time.

### 17. Loopholing All the Way: Language Modeling with pure Self-Conditioning

- 作者：Adrien Deschenaux, Nadezhda Ilieva, Justin Deschenaux, Manuel Madeira, Dorina Thanou, Aurélien Lucchi, Antonio Orvieto, Caglar Gulcehre 等｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30068v1

### 背景/问题
Recent Diffusion Language Models (DLMs) use Self-Conditioning (SC), or Loopholing, to improve their performance. While SC is traditionally seen as an auxiliary heuristic, its empirical success raises the question: can a continuous generative model be based purely on Self-Conditioning?

### 方法
Recent Diffusion Language Models (DLMs) use Self-Conditioning (SC), or Loopholing, to improve their performance. While SC is traditionally seen as an auxiliary heuristic, its empirical success raises the question: can a continuous generative model be based purely on Self-Conditioning? On Sudoku, LAW outperforms previous Discrete and Continuous Diffusion Models, including Loopholing Discrete Diffusion.

### 实验/数据
未在摘要中明确给出。

### 结果
Recent Diffusion Language Models (DLMs) use Self-Conditioning (SC), or Loopholing, to improve their performance. On Sudoku, LAW outperforms previous Discrete and Continuous Diffusion Models, including Loopholing Discrete Diffusion. Additionally, fine-tuning a pre-trained Uniform Diffusion Model (Duo) with LAW increases its accuracy from 17.2% to 48.1%.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Find our code at https://github.com/ilievanadezhda/law.

### 18. Differential powers of monomial ideals in affine semigroup rings

- 作者：Soumyadeep Misra, Christopher Wong｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30057v1

### 背景/问题
This article gives explicit descriptions for differential powers of monomial ideals in certain (possibly non-normal) affine semigroup rings. We use these descriptions to show that the topologies defined by the ordinary, symbolic, and differential powers of any monomial ideal are all linearly equivalent.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we apply our results to pinched Veronese rings.

### 19. Multiplying matrices via polynomials: exposition and barriers

- 作者：Alimzhan Amanov, Maxim van den Berg, Jeroen Zuiddam｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30054v1

### 背景/问题
We give an exposition of OpenAI's recent proof that the exponent $ω_\mathbb{C}$ of matrix multiplication over the complex numbers satisfies $ω_\mathbb{C}\leq9/4$. Our version of the proof gives $ω_\mathbb{F}\leq9/4$ over every field $\mathbb{F}$.

### 方法
未在摘要中明确给出。

### 实验/数据
Our version of the proof gives $ω_\mathbb{F}\leq9/4$ over every field $\mathbb{F}$.

### 结果
We moreover prove an operational barrier (which can be thought of as coming from an operational asymptotic spectrum) showing that the current analysis of all these upper bounds on $ω_\mathbb{F}$ and $ω_\mathbb{F}(a,b,c)$ is optimal and that in fact the current degeneration ingredients cannot improve the bounds.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We moreover prove an operational barrier (which can be thought of as coming from an operational asymptotic spectrum) showing that the current analysis of all these upper bounds on $ω_\mathbb{F}$ and $ω_\mathbb{F}(a,b,c)$ is optimal and that in fact the current degeneration ingredients cannot improve the bounds.

### 20. Plausible but Unimplantable: A Trustworthiness Audit of Shape Completion Foundation Models for Cranial Defect Reconstruction

- 作者：Marek Wodzinski, Kamil Kwarciak, Daria Hemmerling, Mateusz Daniol｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30035v1

### 背景/问题
A patient who has lost part of the skull vault needs an implant that fits the defect exactly, and such implants are still drawn by hand in CAD by specialists, which makes each case slow and expensive. The task can be considered as a shape completion problem, so pretrained completion models, and now the first shape completion foundation models, look like a way to remove that manual step.

### 方法
The task can be considered as a shape completion problem, so pretrained completion models, and now the first shape completion foundation models, look like a way to remove that manual step. We audited three publicly released pretrained shape completion models, two of them foundation models, applied zero-shot to 239 cranial defects, some carved from public skull datasets and some real post-craniectomy cases. Yet not one output, from any model in any configuration, was implantable: none managed both to stay clear of the bone the patient still has and to place more material than doing nothing, where a task-specific volumetric model, trained for this task and selected on these cases, was implantable on all but one.

### 实验/数据
We audited three publicly released pretrained shape completion models, two of them foundation models, applied zero-shot to 239 cranial defects, some carved from public skull datasets and some real post-craniectomy cases.

### 结果
On the 210 carved defects none of the three improved on doing nothing, and on the 29 real cases only one did so beyond chance.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Substantial research towards trustworthy foundation models for shape completion is still needed.

### 21. Modeling QNMs-Filtered Gravitational Waveforms: Approximation Limits and Filtering Effects

- 作者：Jun-Xi Shi, Zhen-Tao He, Tingyuan Jiang, Yu Tian, Dan-Dan Yuan, Hongbao Zhang｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30031v1

### 背景/问题
The waveform left after quasinormal modes filtering of binary gravitational waveforms, often called the direct wave, has recently attracted considerable debate. Analytic models of this residual waveform involve several levels of approximation, while the effects of filtering on the modeling remain unclear.

### 方法
Analytic models of this residual waveform involve several levels of approximation, while the effects of filtering on the modeling remain unclear. In this paper, we examine the approximation errors, limits of applicability, and role of filtering in these models. We find that the point-particle models examined here show notable discrepancies with the filtered Binary-black-holes waveforms.

### 实验/数据
Our analytic calculations on a Schwarzschild background further show that vacuum perturbations with Gaussian initial data can also exhibit direct-wave-like waveforms after filtering, with their morphology depending on the location of the initial data relative to the light ring.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our analytic calculations on a Schwarzschild background further show that vacuum perturbations with Gaussian initial data can also exhibit direct-wave-like waveforms after filtering, with their morphology depending on the location of the initial data relative to the light ring.

### 22. The recent counterexamples to the Eisenbud-Schreyer-Weyman Ulrich problem (2003) and to Hochster's small Cohen-Macaulay conjecture (1973): a survey, with a generalization to arbitrary dimension

- 作者：Cristian Anghel｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30027v1

### 背景/问题
In September 2026 four preprints and an AI-generated manuscript moved one numerical obstruction from projective geometry to local algebra. For a smooth complex projective surface $Y$ with an ample, globally generated divisor $H$ such that $H^2<σ(Y)$, the signature, one obtains in turn: no Ulrich bundles when $H$ is very ample (Anghel, arXiv:2609.02718; extended to every dimension by Lopez, arXiv:2609.06678), answering negatively the Eisenbud-Schreyer-Weyman question of 2003 for sheaves supported on the whole variety; no arithmetically Cohen-Macaulay bundles, i.e.

### 方法
section rings without graded maximal Cohen-Macaulay modules in characteristic zero (Anghel, arXiv:2609.15589); and complete local domains without small Cohen-Macaulay modules, counterexamples to Hochster's 1973 conjecture, if $K_Y\equiv4H$ (Chen, arXiv:2609.24142, proposed) or $σ>2H^2$ (OpenAI, released 6 October).

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Consequently the completed section rings of all Hesse pairs, including the ball quotient of the first preprint, have no small Cohen-Macaulay module, and products of Hesse surfaces with projective spaces give complete local domains with an isolated singularity, of every dimension $\ge3$, without small Cohen-Macaulay modules.

### 23. Zeros of $E_2$, quasi-periods, and Schwarz maps

- 作者：Abdellah Sebbar｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30025v1

### 背景/问题
We study the zeros of the Eisenstein series $E_2$, their distribution near rational cusps, and the values of modular functions at these zeros. Using Watson's inversion formula, we prove that the number of zeros in $0\leq\operatorname{Re}τ<1$ with imaginary part at least $Y$ satisfies \[ N(Y)=\frac{1}{2πY} +O\!\left(Y^{-1/2}\log\frac1Y\right) \qquad(Y\to0^+).

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we give conditional results on the transcendence of $ρ$ under modular Schanuel and period conjectures, and determine why the associated analytic subgroup fails the rank condition in Waldschmidt's theorem.

### 24. On optimal (v,5,3,1) optical orthogonal codes

- 作者：Laura Johnson, Lorenzo Mella, Anita Pasotti, Emma Smith｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.30003v1

### 背景/问题
In this paper, we establish a tight upper bound for the size of a $(v,5,3,1)$ optical orthogonal code (OOC) and call such a code optimal when it achieves this upper bound. In addition, if an optimal OOC has the property that all non-identity elements of $\mathbb{Z}_v$ are covered by the list of differences of its codeword-sets then it is called perfect.

### 方法
In this paper, we present direct and recursive constructions for infinite classes of optimal and perfect $(v,5,3,1)$-OOCs.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In this paper, we present direct and recursive constructions for infinite classes of optimal and perfect $(v,5,3,1)$-OOCs.

### 25. Pinch-Free Orientations of Polyomino Grid Graphs

- 作者：James Fox, Mirela Damian｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.29994v1

### 背景/问题
We study lattice-based collective construction of a target polyomino on the integer grid, where robots place unit square blocks subject to two physical constraints: the partial structure must remain connected at all times, and no placement may create an unfillable one-cell gap. We present a wavefront sweep algorithm that computes a dependency structure satisfying the local conditions required for safe assembly.

### 方法
We present a wavefront sweep algorithm that computes a dependency structure satisfying the local conditions required for safe assembly.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Given a list of n cells sorted lexicographically by coordinates, the orientation can be computed in O(n) time using O(n) auxiliary space.

### 26. Flowz: When Does Learning Forecast Errors Add Value? Conditional Flow Matching for Financial Price Forecasts

- 作者：Giancarlo Vercellino｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.29991v1

### 背景/问题
Learning a forecasting model's errors offers a modular way to improve its predictive distribution while retaining its underlying dynamics. We study this approach with Flowz, a conditional flow model of direct multi-step price-level residuals fitted using random features and ridge regression.

### 方法
Learning a forecasting model's errors offers a modular way to improve its predictive distribution while retaining its underlying dynamics. We study this approach with Flowz, a conditional flow model of direct multi-step price-level residuals fitted using random features and ridge regression.

### 实验/数据
The experiment uses 24 US stocks selected across four liquidity-volatility strata, 104 common forecast origins, horizons of 5, 10, 20, 40, 80, and 160 trading observations, and three fit seeds. Conditional residual learning is therefore useful for the drifting EWMA specification in this experiment, with gains concentrated at longer horizons.

### 结果
Learning a forecasting model's errors offers a modular way to improve its predictive distribution while retaining its underlying dynamics. The EWMA improvement holds at each fit seed and exceeds the Gaussian control for all 24 stocks in the far band.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Conditional residual learning is therefore useful for the drifting EWMA specification in this experiment, with gains concentrated at longer horizons.

### 27. GhostFaceMPC: Privacy-Preserving Face Recognition with Multi-Party Computation

- 作者：Davide Carnemolla, Dario Catalano, Mario Di Raimondo｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.29987v1

### 背景/问题
Facial recognition has become central to modern authentication systems, security frameworks, and personalized services. However, its widespread adoption is hindered by severe privacy risks, particularly surrounding unauthorized access to sensitive biometric data.

### 方法
Facial recognition has become central to modern authentication systems, security frameworks, and personalized services. We introduce a multi-party computation-friendly quantization of the GhostFaceNet model and circuit optimizations that make face recognition under multi-party computation practical.

### 实验/数据
However, its widespread adoption is hindered by severe privacy risks, particularly surrounding unauthorized access to sensitive biometric data. GhostFaceMPC enables secure processing of facial data across all stages of a face recognition process, from feature extraction and storage to matching, without exposing raw images or biometric embeddings at any stage.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The code is available at https://github.com/crypto-unict/GhostFaceMPC.

### 28. Free-XOR TFHE via Lazy Bootstrapping

- 作者：Ali Ajorian, Osman Biçer｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.29983v1

### 背景/问题
Gate bootstrapping (GB) is a widely used technique in FHEW-like fully homomorphic encryption schemes, such as TFHE, for evaluating Boolean gates while simultaneously reducing the noise of the resulting ciphertext. However, the computational cost of GB is typically dominated by an expensive blind rotation (BR).

### 方法
\cite{chen2024free} proposed a gate bootstrapping framework in which $\txor$ gates can be evaluated simply by adding the two input ciphertexts, resulting in what they call \textit{free-XOR}. In this work, we propose a similar gate bootstrapping framework that supports free evaluation of $\txor$ gates while evaluating \textit{all symmetric binary Boolean gates}, i.e., the 8 gates whose output is identical for the inputs $(0,1)$ and $(1,0)$, using two blind rotations.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In addition to providing broader gate support, our construction is substantially simpler than that of \cite{chen2024free}, both conceptually and in terms of implementation.

### 29. Characters and Polynomiality for Maximal Parabolic Unipotent Radicals in Finite Classical Groups

- 作者：Qingchun Hao, Yang Yang｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.29976v1

### 背景/问题
Characters and Polynomiality for Maximal Parabolic Unipotent Radicals in Finite Classical GroupsLet $q$ be a power of an odd prime. For the unipotent radicals of maximal rational parabolic subgroups of the finite symplectic, orthogonal and unitary groups, we determine all complex irreducible characters, their values, and the number of characters of each degree.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we express the multiplicities through $R$-polynomials, with the unequal parameters $q^2,\dots,q^2,q$ in the unitary case.

### 30. On Divisibility Properties of Zipf Law and Relatives

- 作者：Thierry E Huillet｜年份：2026｜发布时间：2026-10-21｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.29974v1

### 背景/问题
We describe recursive chance mechanisms and processes involving Zipf's law and relatives, all showing up mixing properties, both geometric and Poisson. Relations to Markov processes are explored.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Relations to Markov processes are explored.
