# CausalRadar 日报 - 2026-11-23

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. FairITR: Fairness-Aware Learning of Multicategory Individualized Treatment Rules

- 作者：Zeyu Chen, Wei Qian, Bintong Chen｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**8.24**
- 链接：https://arxiv.org/abs/2611.27894v1

> 命中：hit_title=['CATE']；hit_abstract=['CATE']

### 背景/问题
Individualized treatment rules (ITRs) recommend treatment decisions based on individual characteristics and can improve treatment outcomes beyond traditional one-size-fits-all strategies. However, similar to other commonly used algorithmic decision-making methods, ITRs without considering model fairness may result in unfair decisions across groups defined by sensitive attributes, such as race or gender.

### 方法
However, similar to other commonly used algorithmic decision-making methods, ITRs without considering model fairness may result in unfair decisions across groups defined by sensitive attributes, such as race or gender. To solve this problem, we further propose FairITR, a fairness-aware learning framework that jointly optimizes treatment outcomes and fairness.

### 实验/数据
Extensive experiments on real-world datasets show that FairITR substantially reduces unfairness in ITRs while maintaining competitive treatment values relative to existing baselines.

### 结果
Individualized treatment rules (ITRs) recommend treatment decisions based on individual characteristics and can improve treatment outcomes beyond traditional one-size-fits-all strategies.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Extensive experiments on real-world datasets show that FairITR substantially reduces unfairness in ITRs while maintaining competitive treatment values relative to existing baselines.

### 2. Real-time neuromorphic audio and vision perception for autonomous robotic applications: Integration and experimental evaluation on a rover platform

- 作者：Guillem Fustier-Castillo, Ruben Ribes-Serrano, Javier Naranjo-Alcazar, Vicent Ortiz-Castello, Pedro Zuccarello｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.74**
- 链接：https://arxiv.org/abs/2611.27953v1

> 命中：hit_scenario=['ads']

### 背景/问题
Neuromorphic sensing and computing offer a promising alternative to conventional deep learning pipelines for mobile robots, where perception must run continuously under tight latency and energy constraints. However, most neuromorphic solutions are still evaluated offline or on isolated benchmarks, and their integration into complete robotic systems remains largely unexplored.

### 方法
All models are deployed as containerised services and integrated through ROS~2, and a configurable action dispatcher maps the detected classes to robot behaviours, closing the loop between perception and actuation.

### 实验/数据
However, most neuromorphic solutions are still evaluated offline or on isolated benchmarks, and their integration into complete robotic systems remains largely unexplored.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The platform is demonstrated in a proof-of-concept scenario in which the robot reacts to sound classes detected by both audio pipelines and detects traffic cones with the event camera, showing the feasibility of integrating neuromorphic hardware into a multimodal robotic platform operating in real time.

### 3. What Must a Model Tell a Planner? Outcome Interfaces for Risk-Aware Planning After Robot Damage

- 作者：Hassan Iqbal, Krishna Kumar｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.74**
- 链接：https://arxiv.org/abs/2611.27939v1

> 命中：hit_scenario=['ads']

### 背景/问题
When a robot is damaged, it must decide which routes it can still afford, and the amount of risk it may accept can change from one mission to the next. We argue that whether a learned model helps such a robot depends on its decision interface, that is, on what the model hands to the planner.

### 方法
We argue that whether a learned model helps such a robot depends on its decision interface, that is, on what the model hands to the planner. A decision policy tells the planner what to do, whereas an outcome model, a kind of world model, predicts the consequences of each route. The third is an outcome model that predicts the feasibility and travel time of each route.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Predicting outcomes lets the planner preserve missions by changing routes as risk requirements tighten.

### 4. DiTraR: Diverse Scorers and Transcript-Guided Re-ranking for Video Corpus Moment Retrieval

- 作者：Mohammad Alijanpour Shalmani, Alale Rezvani Boroujeni, Ali Amini｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.74**
- 链接：https://arxiv.org/abs/2611.27931v1

> 命中：hit_scenario=['ads']

### 背景/问题
Video corpus moment retrieval asks a system to find, in a large collection of untrimmed videos with subtitles, the video and the time interval that a natural-language query describes. We find that most top-ranked errors of a strong corpus-level scorer come from choosing the wrong video, not from imprecise boundaries, and that re-weighting the evidence the scorer already uses does not fix them.

### 方法
We present DiTraR, which addresses video selection from two complementary directions. A witness-interval scorer decomposes the query into probes and scores every candidate interval of every corpus video exactly; a multi-scorer energy ensemble averages the energies of independently trained scorers before one exhaustive search; and a transcript verifier, a frozen language model that reads the time-stamped dialogue of the highest-ranked videos, re-orders the moments without changing their boundaries.

### 实验/数据
With all settings frozen on development data and a single evaluation, DiTraR reaches 24.36 and 13.55 R@1 at IoU 0.5 and 0.7 on the TVR validation split.

### 结果
The ensemble improves queries about visual content, the verifier improves queries about dialogue, and their gains largely add up.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The ensemble improves queries about visual content, the verifier improves queries about dialogue, and their gains largely add up.

### 5. How communities help epidemics persist

- 作者：Júlia Komjáthy, Marco Seiler, Daniel Valesin｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.74**
- 链接：https://arxiv.org/abs/2611.27843v1

> 命中：hit_scenario=['ads']

### 背景/问题
Empirical studies show that communities such as households and workplaces strongly influence how an infection spreads and how long it persists in a population. To understand this effect, we study the contact process (SIS epidemic model) on random intersection graphs and their local weak limit.

### 方法
To understand this effect, we study the contact process (SIS epidemic model) on random intersection graphs and their local weak limit.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We compare these findings with known results on the behaviour of the contact process on a "community-free" random graph with similar degree distributions, to highlight the impact of communities.

### 6. Graph Signal Generation via Graph-Aware Diffusion Models

- 作者：Vimal K B, Sergio Rozada, Antonio G. Marques, Elvin Isufi, Hadi J. Rad｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.74**
- 链接：https://arxiv.org/abs/2611.27826v1

> 命中：hit_scenario=['recommendation']

### 背景/问题
Many signals are defined on the nodes of a graph, such as traffic flow at road sensors or user purchases of related products. They are often partly observed, and learning their distribution enables imputing missing values and forecasting future ones.

### 方法
Diffusion models learn such distributions, but their forward noise is independent across nodes and does not depend on the graph. We propose Mode-Adaptive SNR Scheduling (MASS), which assigns each graph frequency its own diffusion rate and keeps all of them at the same SNR.

### 实验/数据
未在摘要中明确给出。

### 结果
GAD with MASS improves recommendation accuracy by 5-19%, reduces traffic-imputation RMSE by up to 7.8% with half as many reverse steps, and improves forecasting MAE and RMSE using only 3 reverse steps.

### 结论/启示（面向电商发券、定价、营销算法等应用）
GAD with MASS improves recommendation accuracy by 5-19%, reduces traffic-imputation RMSE by up to 7.8% with half as many reverse steps, and improves forecasting MAE and RMSE using only 3 reverse steps.

### 7. A Methodologically Rigorous Benchmark of Linear Regression,RNN, and LSTM for S&P 500 Forecasting:Identifying Sources of Performance Inflation in Financial DeepLearning

- 作者：Hari Sitaula, Joseph Opitz｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2611.27978v1

> 命中：hit_abstract=['CATE']

### 背景/问题
This study examines one-day-ahead forecasting of the S&P 500 closing level using a 2006-2025 dataset that includes fundamental price data, macroeconomic indicators, and engineered technical features. We benchmark three model families, namely linear regression, vanilla recurrent neural networks (RNN), and long short-term memory networks (LSTM), within a unified preprocessing and chronological evaluation pipeline.

### 方法
We benchmark three model families, namely linear regression, vanilla recurrent neural networks (RNN), and long short-term memory networks (LSTM), within a unified preprocessing and chronological evaluation pipeline. We identify three sources of result inflation that frequently appear in published methodologies: wavelet-denoised evaluation targets, the absence of a naive persistence baseline, and best-of-N replicate reporting. We then re-evaluate all model families under a corrected protocol that controls for each.

### 实验/数据
This study examines one-day-ahead forecasting of the S&P 500 closing level using a 2006-2025 dataset that includes fundamental price data, macroeconomic indicators, and engineered technical features.

### 结果
We compare models on accuracy, stability across replicates, and architectural depth sensitivity, using the naive persistence forecast (predicting today's close as tomorrow's close) as a primary baseline against which all candidate models must demonstrate improvement.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We compare models on accuracy, stability across replicates, and architectural depth sensitivity, using the naive persistence forecast (predicting today's close as tomorrow's close) as a primary baseline against which all candidate models must demonstrate improvement.

### 8. Recovering buoyancy-glitch parameters in low-luminosity red giants from global stellar properties with machine learning

- 作者：Jiang Chen｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2611.27954v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Buoyancy glitches in red giants provide localized information on the interior structure near the base of the convective envelope, but their properties are typically inferred from dedicated seismic modelling rather than global properties, limiting large-sample applications. We investigate whether the buoyancy-glitch amplitude ($A_g$), location ($W_{\rm g}^{\star}$), and width ($D_g$) can be recovered from global stellar properties using gradient-boosted tree regressors (XGBoost and LightGBM).

### 方法
Buoyancy glitches in red giants provide localized information on the interior structure near the base of the convective envelope, but their properties are typically inferred from dedicated seismic modelling rather than global properties, limiting large-sample applications. The models were trained on a grid of 12580 synthetic stellar models of low-luminosity red giants, with target parameters derived from fits to the local buoyancy frequency profile.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Overall, for the synthetic grid adopted here, these results indicate that global properties provide a direct estimate of the buoyancy-glitch parameters and a way to prioritise dedicated mixed-mode inversions for large asteroseismic samples such as Kepler and PLATO.

### 9. Freedom is all you need

- 作者：Julian Bushelli, James Eldred Pascoe｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2611.27943v1

> 命中：hit_abstract=['CATE']

### 背景/问题
The functional calculus allows for the rigorous analysis of functions of matrices or even operators. The free functional calculus gives the natural class of functions over any category.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
change of coordinates) invariant domains inherits the niceties of complex analysis and large-scale parallel networks, such as automatic analyticity, free universal monodromy, which gives a hypothetical explanation for beneficial overfitting.

### 10. Intervals of limit points for $B_α$-spectral radii

- 作者：Francesco Belardo, Callum Huntington, Elismar R. Oliveira, Vilmar Trevisan｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2611.27937v1

> 命中：hit_abstract=['CATE']

### 背景/问题
For a finite simple graph $G$, let \[ B_α(G)=αA(G)+(1-α)L(G)=(1-α)D(G)+(2α-1)A(G),\qquad 0\leq α\leq 1. \] We study the limit points of the spectral radii of these matrices.

### 方法
These identify which tree and caterpillar results are reparametrizations of earlier work.

### 实验/数据
未在摘要中明确给出。

### 结果
Combining uniform edge subdivisions with generalized Bethe decorations, we improve the Laplacian and signless Laplacian half-line to $[29/5,\infty)$, verified by an exact rational certificate.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The interval theorem also yields half-lines of $A_β$-limit points for every $0\leβ<1$, and of deformed-Laplacian limit points for every nonzero deformation parameter.

### 11. Geometrically Constrained Learning I: Agnostically Learning Adversarially Robust Classifiers

- 作者：Jane Lange, Cassandra Marcussen, Arsen Vasilyan｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2611.27852v1

> 命中：hit_abstract=['CATE']

### 背景/问题
We study agnostic learning under the Gaussian distribution with guarantees on both classification error and robustness to adversarial perturbations. We say that a function has boundary profile $K \ge 1$ if, for all $r > 0$, the probability that a point lies within Euclidean distance $r$ of the classification boundary is at most $Kr$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our algorithm finds a polynomial such that these certified ranges are small, then obtains a robust classifier via randomized rounding and partitioning of the domain.

### 12. What determines the properties of Population III binaries?

- 作者：Neha Singh, Tomasz Bulik｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2611.27820v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Population~III binaries may provide a gravitational-wave probe of the first stellar populations. Uncertain initial binary parameter distributions and evolutionary prescriptions complicate predictions of their remnant masses, birth orbits and formation spins.

### 方法
Varying these model evolutionary parameters (MEPs) jointly is needed to identify which MEPs shape each property and whether their effects persist among binaries that merge. We use \textsc{StarTrack} to evolve $2\times10^6$ initial binaries per model across 1152 configurations spanning eight MEPs. To our knowledge, this is the largest grid of Population~III isolated-binary population-synthesis models to date by number of distinct parameter configurations.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We use variance-based sensitivity analysis to quantify how the initial binary parameter distributions and evolutionary prescriptions affect the predicted BBH properties.

### 13. Nonperturbative Bounds on the Ground-State Energy of Lattice QED

- 作者：Paweł Zin, Andrzej Veitia｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27975v1

### 背景/问题
We establish nonperturbative bounds on the ground-state energy of lattice quantum electrodynamics with naive fermions in Coulomb gauge, within the Gaussian photon approximation. Our central result is a spectral comparison theorem showing that, in the thermodynamic limit, the minimum fermionic energy density over all link configurations coincides with that of the trivial gauge configuration.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finite-lattice counterexamples show that the thermodynamic limit is essential.

### 14. Soft--hard Bayesian inference in heavy-ion collisions

- 作者：L. Du, S. A. Bass, M. Chartier, Y. Chen, Y. -C. Chen, R. Datta, R. Dolan, R. Ehlers 等｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27971v1

### 背景/问题
Bayesian analyses of jet quenching commonly constrain jet--medium interaction parameters using a fixed quark-gluon plasma (QGP) background obtained from a soft-sector calibration. This approach neglects uncertainty in the medium and prevents hard observables from providing additional constraints on its properties.

### 方法
This approach neglects uncertainty in the medium and prevents hard observables from providing additional constraints on its properties.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These findings highlight the difficulty of distinguishing changes in the QGP medium from changes in microscopic jet--medium interaction strength using inclusive suppression measurements alone.

### 15. On the Complete Feature Set for ADHD Classification in Children and Adolescents Based on EEG Signals

- 作者：Javier Sanchis, Álvaro Navarro, Jorge García-Carrasco, Tahar Kechadi, Juan Trujillo｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27970v1

### 背景/问题
Attention-deficit/hyperactivity disorder is a neurodevelopmental condition that can affect attention, activity and impulse control. Electroencephalography (EEG) records brain activity as children and adolescents perform cognitive tasks.

### 方法
未在摘要中明确给出。

### 实验/数据
The dataset links continuous signals to precomputed measurements from 115 feature definitions or templates and records the quality decisions made for each recording. The dataset, curation software and aggregate results for the predictive example are publicly available.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The dataset, curation software and aggregate results for the predictive example are publicly available.

### 16. All stable Schoen--Wolfson cones are minimizing

- 作者：Filippo Gaia, Xuanyu Li, Gerard Orriols｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27966v1

### 背景/问题
In the late nineties, R.~Schoen and J.~Wolfson studied the problem of minimizing the area among Lagrangian surfaces in a Riemannian symplectic $4$-manifold. In their parametric approach, they showed that minimizers are smoothly branched-immersed away from a discrete set of points, where there exists a nonflat tangent cone minimizing the area among Lagrangian disk competitors.

### 方法
In their parametric approach, they showed that minimizers are smoothly branched-immersed away from a discrete set of points, where there exists a nonflat tangent cone minimizing the area among Lagrangian disk competitors.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We settle this question by showing that for each $p \geq 1$, $C_{p,p+1} \cap B_1$ minimizes the area among Lagrangian disks spanning its boundary with degree one.

### 17. Differential Transmutations and First-Passage Expansions for Monomial Brownian Boundaries

- 作者：Gerardo Hernandez-del-Valle｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27958v1

### 背景/问题
Let $P_t=\exp(t\partial_x^2/2)$ be the heat semigroup and let $F(t)=ρt^p$, where $p\ge2$ is an integer. Previous transported-zero theory associates with this boundary a constant-flux solution annihilated by a polynomial-coefficient differential operator of order $2p-1$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The present result is formal at all orders; convergence of the resulting perturbation series is left as a separate analytic problem.

### 18. Load-Following Dynamics of an SMR-Powered All-Electric Ship with Battery Energy Storage

- 作者：Ali Mahboub Rad, Jie Zhang｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27957v1

### 背景/问题
Small modular reactors (SMRs) are being considered as compact, high-energy-density power sources for future all-electric ships. In such systems, propulsion-load variations can propagate through the electrical network, turbine-generator set, steam generator, and reactor, producing coupled nuclear, thermal, mechanical, and electrical transients.

### 方法
The model couples an integral pressurized water reactor, a once-through moving-boundary steam generator, a simplified turbine model, a synchronous generator, an AC shipboard electrical network, an asynchronous propulsion motor, and a grid-connected BESS. These results demonstrate the importance of modeling nuclear-powered electric ships as coupled multi-domain systems and show that BESS integration can improve short-term load-following performance.

### 实验/数据
未在摘要中明确给出。

### 结果
These results demonstrate the importance of modeling nuclear-powered electric ships as coupled multi-domain systems and show that BESS integration can improve short-term load-following performance.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results demonstrate the importance of modeling nuclear-powered electric ships as coupled multi-domain systems and show that BESS integration can improve short-term load-following performance.

### 19. Weighted sum commuting maps with the $(f,g)$-Aluthge transform

- 作者：Jing-Bin Zhou, Shihai Yang｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27949v1

### 背景/问题
Let $\mathbb{M}_n(\mathbb{C})$ denote the algebra of all $n\times n$ complex matrices, where $n\geq2$, and let $Δ_{f,g}$ be the $(f,g)$-Aluthge transform associated with nonnegative continuous functions $f,g$ on $[0,\infty)$ satisfying $f(t)g(t)=t$ for all $t\geq0$. In this paper, we characterize all surjective maps $Φ:\mathbb{M}_n(\mathbb{C}) \to\mathbb{M}_n(\mathbb{C})$ satisfying\[Φ(Δ_{f,g}(αA+βB))=Δ_{f,g}(αΦ(A)+βΦ(B))\]for all $A,B\in\mathbb{M}_n(\mathbb{C})$, where $α,β$ are fixed nonzero real numbers.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
When $f$ is constant, we show that $Φ(A)=S(A)+D$ for all $A$, where $S$ is a surjective $\mathbb{Q}(α,β)$-linear map and $D\in\mathbb{M}_n(\mathbb{C})$ satisfies $(α+β-1)D=0$.

### 20. One partition function call to rule them all: Efficiently computing the equilibrium landscape of multiple nucleic acid strands

- 作者：Ahmed Shalaby, Damien Woods｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27945v1

### 背景/问题
In the nearest neighbour model of DNA/RNA binding, the partition function (PF) is a sum of Boltzmann-weighted free energies of the exponentially large set of secondary structures. Dirks et al.

### 方法
In the nearest neighbour model of DNA/RNA binding, the partition function (PF) is a sum of Boltzmann-weighted free energies of the exponentially large set of secondary structures. Despite the intuition that PF may somehow encode the entire state space, thus far different approaches were required to solve various energy-landscape prediction problems. Our approach unifies the field of energy landscape prediction showing that a single, general, algorithmic framework neatly unifies a large collection of problems that practitioners care about, and required distinct techniques with worse time bounds.

### 实验/数据
Our approach unifies the field of energy landscape prediction showing that a single, general, algorithmic framework neatly unifies a large collection of problems that practitioners care about, and required distinct techniques with worse time bounds.

### 结果
However, we show that magnification allows for efficient decoding of the entire landscape, concretely: a single call to the magnifiable PF efficiently solves and improves upon a large number of problems, giving: - MFE in $O(N^3(c-1)!)$ time, $O(N^2)$ space; a considerable improvement over our $O(N^4(c-1)!)$ time, $O(N^4)$ space result [ICALP 2025].

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our approach unifies the field of energy landscape prediction showing that a single, general, algorithmic framework neatly unifies a large collection of problems that practitioners care about, and required distinct techniques with worse time bounds.

### 21. The Power of Sampling for Finding Far-Apart Bases in Matroids

- 作者：Mayank Goswami, Vasilis Livanos, Pasin Manurangsi, Arturo Merino, GiBeom Park, Adarsh Srinivasan｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27934v1

### 背景/问题
We study the geometry of matroids via the \emph{diameter} and \emph{dispersion} of the metric space of their bases. Given a matroid $M$, we ask if the diameter of its basis-exchange graph $\mathcal{G}(M)$ can be approximated by sampling two uniformly random bases.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
We also improve the $1/6$-approximation for $k$-diversity, for partition matroids and graphic matroids of constant arboricity.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also improve the $1/6$-approximation for $k$-diversity, for partition matroids and graphic matroids of constant arboricity.

### 22. Optimal High-Dimensional Martingale CLTs over Rectangles

- 作者：Zi-Yao Su, Xiuqi Sun｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27929v1

### 背景/问题
We prove Gaussian approximation bounds over rectangles for high-dimensional martingale sums, with lower bounds showing optimality up to powers of $\log n$. The results cover bounded increments, conditional and marginal sub-Gaussian and sub-exponential tails, and uniform $q$th-moment bounds on the largest absolute coordinate for $2<q\le3$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
When $Q=I_d$, the bounded and marginal light-tail rates have no additional factors in $\log n$ if $\log(ed)\ge\{\log(en)\}^2$; the same holds for the finite-moment rates with $2<q\le3$ in every dimension, for all sufficiently large $n$.

### 23. The Thurston algorithm for general entire maps on the complex plane: Existence and uniqueness

- 作者：Sebastian van Strien｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27925v1

### 背景/问题
We prove that a marked topological entire Thurston map $(f,A)$ of stable parabolic type is Thurston equivalent relative to $A$ to a postsingularly finite entire function if and only if it has no Levy cycle relative to $A\cup\{\infty\}$. Here $A$ is a finite forward-invariant set containing the postsingular set.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We compare this geometric argument with the proofs for real entire maps and exponential maps.

### 24. The moments and asymptotic spectral distribution of the Grassmannian ensemble

- 作者：Aryan Gadhave, Asghar Ghorbanpour, Liam Hickey, Masoud Khalkhali, Allison Klingler, Nathan Pagliaroli, Andrew Parks｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27914v1

### 背景/问题
In this paper, we study random density matrices constructed by taking partial traces of projections onto random subspaces of a bipartite Hilbert space $\mathcal{H}_A \otimes \mathcal{H}_{B}$ distributed according to the pushforward measure of the action of the unitary group on the Grassmannian $\text{Gr}_{n}(\mathcal{H}_A \otimes \mathcal{H}_{B})$. This ensemble models a `typical' quantum subspace.

### 方法
This ensemble models a `typical' quantum subspace.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we compute the asymptotic expansion of the average entanglement entropy.

### 25. Star Panoptic Quality: Selectively Evaluating Split and Merged Instances

- 作者：Erik Großkopf, Paula Tamara Buzduga, Hendrik Möller, Florian Kofler｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27913v1

### 背景/问题
Detecting individual instances is crucial for many segmentation problems. However, expert instance annotations are often unavailable, so instances are approximated heuristically (e.g., as connected components of semantic maps), which can merge touching objects or split fragmented ones.

### 方法
We present Star Panoptic Quality (StarPQ), a novel evaluation ramework, which closes this gap in two steps: First, we construct a so-called star forest in the bipartite graph whose clean, merge, and split stars isolate different failure modes.

### 实验/数据
Across various experiments, we demonstrate that StarPQ not only enables targeted penalization or eniency towards specific failure modes, but also serves as a diagnostic tool to reveal their prevalence.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Across various experiments, we demonstrate that StarPQ not only enables targeted penalization or eniency towards specific failure modes, but also serves as a diagnostic tool to reveal their prevalence.

### 26. Functional Depth Is Learned: Isolating the Computation That Layers Produce Only Together

- 作者：JaeSeong Kim, KyungTae Lim｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27911v1

### 背景/问题
Transformer performance scales with depth, but layer count merely counts the opportunities for sequential computation: layers could still behave as nearly independent refinements that barely depend on one another. We study how transformers develop functional depth during pretraining, introducing an exact inclusion-exclusion decomposition that isolates the connected component, i.e., the computation that appears only when a specified set of layers acts together under identity ablation.

### 方法
Second, these connected components are behaviorally consequential under direct intervention: deleting them damages perplexity more than deleting a norm-matched random direction at the same site in all 35 measured model-order cells. Third, pairwise representation similarity is consistently negatively correlated with pairwise connected coordination across seven models, yet the two signals are not interchangeable: similarity- and coordination-based block-removal criteria often agree in Pythia but diverge on Amber.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Together, these results suggest that architectural depth provides the opportunity for sequential computation, while pretraining progressively organizes cross-layer dependencies within that depth.

### 27. Metadata-Private Voice Communication over Tor using Post-Quantum Key Encapsulation

- 作者：Noah Zeinali Yazdi, Samuel Zeinali Yazdi｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27909v1

### 背景/问题
Encrypted voice communication systems commonly protect call content but expose significant metadata, including the network identities of both parties, call timing, and traffic patterns. Simultaneously, advances in quantum computing threaten the asymmetric primitives underlying conventional key exchange, creating a harvest-now, decrypt-later risk for long-lived sensitive communications.

### 方法
未在摘要中明确给出。

### 实验/数据
Encrypted voice communication systems commonly protect call content but expose significant metadata, including the network identities of both parties, call timing, and traffic patterns.

### 结果
Encrypted voice communication systems commonly protect call content but expose significant metadata, including the network identities of both parties, call timing, and traffic patterns.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Empirical evaluation across 45 independently circuit-rebuilt test runs yielded a median one-way audio delay of 355 milliseconds and a median connection setup time of 7.61 seconds on same-region Tor circuits, demonstrating that interactive voice communication over onion routing is practically achievable.

### 28. Data-Adaptive Entropy-Based Moment Reduction for Vlasov-Poisson-Dougherty Dynamics

- 作者：Shiheng Zhang, Jiahao Zhang, Guang Lin｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27904v1

### 背景/问题
We develop a data-adaptive entropy-based moment method for the Vlasov-Poisson-Dougherty system with self-consistent temperature. A positive exponential representation augments the physical moments with data-adapted velocity functions.

### 方法
We develop a data-adaptive entropy-based moment method for the Vlasov-Poisson-Dougherty system with self-consistent temperature.

### 实验/数据
We develop a data-adaptive entropy-based moment method for the Vlasov-Poisson-Dougherty system with self-consistent temperature. A positive exponential representation augments the physical moments with data-adapted velocity functions. With full-grid MUSCL retained, matched drive-switching timings give 1.36-2.89-fold online speedups over the full-order solver using 128-1024 velocity nodes.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
With full-grid MUSCL retained, matched drive-switching timings give 1.36-2.89-fold online speedups over the full-order solver using 128-1024 velocity nodes.

### 29. The Dual-Tier Sentiment Framework: Scalable Multimodal UX Attribution in Web Search

- 作者：Yi Ding, Gaurav Kumar, Rui Min, Isabella Ye, Bhavika Goyal, Emilio Antunez, Huihui Chen, Ke Xu 等｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27899v1

### 背景/问题
Sustaining user experience (UX) quality in large-scale web search requires scalable evaluation. Traditional surveys are slow and bottleneck rapid A/B testing, while automated metrics often lack the granularity to diagnose visual-spatial UX anomalies.

### 方法
To address this, we introduce the Dual-Tier Sentiment Framework, a novel industrial architecture for automated UX attribution. Ultimately, this framework enables scalable, accurate, and diagnostic UX attribution, processing O(100k) live experiment queries daily.

### 实验/数据
Traditional surveys are slow and bottleneck rapid A/B testing, while automated metrics often lack the granularity to diagnose visual-spatial UX anomalies. Through multi-task regularization and contextual feature engineering, this tier achieves a +9.8% PR-AUC gain on over 500,000 held-out records, matching baseline recall on all validated regressions with $\sim$20% relative precision gain among the 12 held-out experiments. Ultimately, this framework enables scalable, accurate, and diagnostic UX attribution, processing O(100k) live experiment queries daily.

### 结果
Enhanced by RL-based automated prompt optimization and an AI judge for win/loss patterns, the MLLM yields a $>$6.5% F1 score improvement, offering deep insights into content quality and layout friction.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Ultimately, this framework enables scalable, accurate, and diagnostic UX attribution, processing O(100k) live experiment queries daily.

### 30. TEA-Bench-BR: Can Coding Agents Turn a Branching Clinical Specification into Correct Code?

- 作者：Marcio Andre de Souza Estevam｜年份：2026｜发布时间：2026-11-20｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2611.27895v1

### 背景/问题
Coding agents increasingly implement rules written by domain experts, and bugs in such code are silent: it runs and returns a plausible answer. We introduce TEA-Bench-BR, a benchmark built on the Brazilian pathway for early autism (TEA) screening: three fictitious instruments with the structure of real ones, a multi-professional referral flow, and export to FHIR R4 with the national RNDS profiles, all specified in Portuguese.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
A contamination probe on a modified PHQ-9 finds no error that follows the original rules.
