# CausalRadar 日报 - 2026-10-23

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Plabic promotions beyond cluster: quantum cluster structures and the dual canonical basis

- 作者：Jian-Rong Li, Michael Oren Perlstein, Ran J. Tessler｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**13.00**
- 链接：https://arxiv.org/abs/2610.31655v1

> 命中：hit_scenario=['promotion']；hit_title=['promotion']；hit_abstract=['CATE', 'promotion']

### 背景/问题
Plabic tangles define geometric promotion maps between configurations and, after choosing a lift, between Grassmannians. The main conjecture in \cite{Tangles} is that when the tangle is dominant and solvable the induced algebraic promotion is cluster quasi-homomorphism.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
Plabic tangles define geometric promotion maps between configurations and, after choosing a lift, between Grassmannians. We conjecture that all promotions defined from dominant solvable tangles are naturally lifted to a \emph{quantum cluster quasi homomorphism}, and prove for all cases in the literature that the were shown to be (classical) cluster quasi-homomorphisms.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Lam \cite{LamGP}.

### 2. FairFRESH: A Neuro-Symbolic Framework for Fair and Explainable Household Food Recommendation

- 作者：Kodur Sai Vinay Sathvik, Kakoli Bora, Tejaswini R. M｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**11.00**
- 链接：https://arxiv.org/abs/2610.31506v1

> 命中：hit_scenario=['recommendation']；hit_title=['recommendation']；hit_abstract=['CATE']

### 背景/问题
Recommender systems typically serve one user at a time. However, in households, members share a finite pantry and follow different dietary rules, making independent recommendations prone to resource conflicts and dietary violations.

### 方法
We formulate household food recommendation as constrained fair division and present FairFRESH, a neuro-symbolic framework that learns per-member utilities, allocates foods under explicit welfare objectives, enforces dietary rules through a deterministic filter, and explains recommendations using Shapley and Banzhaf attributions. Theoretically, we show that no finite penalty guarantees compliance near a dietary-rule threshold, establish approximation guarantees for greedy allocation under utilitarian and smoothed Nash objectives in the stock-free model before filtering, and characterize the scale invariance of Nash welfare. On NHANES-derived data, the learned utility model achieves Recall@20 of 0.293, outperforming five learned recommenders (at most 0.244) but not a previous-day repetition heuristic (0.321).

### 实验/数据
On NHANES-derived data, the learned utility model achieves Recall@20 of 0.293, outperforming five learned recommenders (at most 0.244) but not a previous-day repetition heuristic (0.321). In simulation, shared meals reduce pantry use by about one-third, and weekly rotation increases the worst-off member's utility by 38% over the best fixed meal.

### 结果
On NHANES-derived data, the learned utility model achieves Recall@20 of 0.293, outperforming five learned recommenders (at most 0.244) but not a previous-day repetition heuristic (0.321). In simulation, shared meals reduce pantry use by about one-third, and weekly rotation increases the worst-off member's utility by 38% over the best fixed meal.

### 结论/启示（面向电商发券、定价、营销算法等应用）
In simulation, shared meals reduce pantry use by about one-third, and weekly rotation increases the worst-off member's utility by 38% over the best fixed meal.

### 3. Causal inference in staggered adoption panels: The correct comparison set depends on your intervention

- 作者：Ian Lundberg, Yaling Xu｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**10.50**
- 链接：https://arxiv.org/abs/2610.31537v1

> 命中：hit_method=['synthetic control']；hit_title=['causal inference']；hit_abstract=['causal inference']

### 背景/问题
A powerful data structure for causal inference is staggered adoption: many units are observed over many time periods, during which some units adopt an irreversible treatment at various time points while others remain untreated. Popular methods that apply in this setting include difference in difference, fixed effects, matching, and synthetic control.

### 方法
未在摘要中明确给出。

### 实验/数据
A powerful data structure for causal inference is staggered adoption: many units are observed over many time periods, during which some units adopt an irreversible treatment at various time points while others remain untreated.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We highlight that common methods cannot answer the second question because this question requires a time-varying comparison set with time-varying weights.

### 4. A Subjective Bayesian Approach to Address Unchecked Assumptions in a Causal Analysis

- 作者：Jaiyool Kim, Indrabati Bhattacharya, Jonathan R. Bradley｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**7.00**
- 链接：https://arxiv.org/abs/2610.31587v1

> 命中：hit_scenario=['ads']；hit_abstract=['treatment effect']

### 背景/问题
Causal analyses using observational data rely on identifying assumptions that cannot be verified from the observed data alone. When such unchecked assumptions fail, effect estimates may be biased and uncertainty may be understated.

### 方法
Causal analyses using observational data rely on identifying assumptions that cannot be verified from the observed data alone. We propose the Adjusted Model for Unchecked Assumptions (AMUA), a subjective Bayesian framework that propagates uncertainty about the joint validity of key causal assumptions through a two-component posterior mixture. One component corresponds to the standard observational causal model in which the assumptions hold (referred to as the "assumption-hold component"); the other represents a flexibly defined model that allows the causal assumptions to fail (referred to as the "assumption-fail component").

### 实验/数据
Causal analyses using observational data rely on identifying assumptions that cannot be verified from the observed data alone. In simulations with a spatially structured unmeasured confounder, we evaluate bias, interval length, and coverage as $π$ varies.

### 结果
The results show that acknowledging assumption uncertainty can widen intervals, and improve coverage relative to analyses that treat the assumptions as certain.

### 结论/启示（面向电商发券、定价、营销算法等应用）
In a county-level application relating long-term PM$_{2.5}$ exposure to COVID-19 mortality, AMUA shows how posterior conclusions depend on prior confidence in the identifying assumptions.

### 5. A Generalized Framework for Rapid Polarization Response Generation in Wide Field-of-View Compton Polarimeters

- 作者：Mohamed Gamal Zaid, Merlin Kole, Mark McConnell, Fabio Muleri, Hancheng Li｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.31559v1

> 命中：hit_scenario=['ads']

### 背景/问题
Polarimetry is the most direct probe of the unsettled radiation mechanism and magnetic field structure of gamma-ray burst (GRB) prompt emission at the energies where it peaks, tens of keV to about 1 MeV. Compton polarimeters use the azimuthal scattering angle distribution (ASAD), a 180 degree modulation on axis.

### 方法
We evaluate it numerically without approximation over the whole prompt-emission energy band for any incidence and polarization angles, quantify the off-axis harmonics a single modulation factor cannot capture, and verify the model against GEANT4 simulations of an ideal polarimeter. With POLAR as the case study, we present two modes that build the full polarization response with at least 95 percent fewer Monte Carlo simulations.

### 实验/数据
Polarimetry is the most direct probe of the unsettled radiation mechanism and magnetic field structure of gamma-ray burst (GRB) prompt emission at the energies where it peaks, tens of keV to about 1 MeV. For a wide field-of-view planar polarimeter, GRBs arrive off axis, where the Klein-Nishina projection adds harmonics to the ASAD. We evaluate it numerically without approximation over the whole prompt-emission energy band for any incidence and polarization angles, quantify the off-axis harmonics a single modulation factor cannot capture, and verify the model against GEANT4 simulations of an ideal polarimeter.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Both modes are released as open-source software for any planar Compton polarimeter.

### 6. Evaluating the Applicability of LLM Inference Optimizations on Apple Silicon

- 作者：Kyrylo Yemets, Andrii Yaroshevych, Victor Muryn, Ostap Khomenko, Pavlo Kryven, Maksym Kmet, Maksym Shamrai, Mariya Hirna｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.31479v1

> 命中：hit_scenario=['ads']

### 背景/问题
Apple Silicon is among the most widely used platforms for local LLM inference, yet nearly all inference optimizations are designed and validated on server-class NVIDIA GPUs under batched serving workloads. Which optimizations retain their benefits when moved to Apple Silicon, and what determines their applicability?

### 方法
未在摘要中明确给出。

### 实验/数据
Experiments span four Apple machines under a common single-request decode workload, with matched RTX 4090 comparisons where possible.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Across four families, a reported speedup is not a portable property of a technique alone but a joint function of technique, runtime, hardware contract, and workload regime.

### 7. Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning

- 作者：Mahdi Salmani, Adel Javanmard, Devansh Gupta, Meisam Razaviyayn｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.31667v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes the candidate pool after generating only a short prefix, committing further computation only to the surviving candidates.

### 方法
Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. On eight open-weight reasoning models, our method outperforms existing quality-based and diversity-based pruning strategies.

### 实验/数据
未在摘要中明确给出。

### 结果
On eight open-weight reasoning models, our method outperforms existing quality-based and diversity-based pruning strategies.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The gains are particularly pronounced when the pruning procedure keeps a moderate number of partial solutions for continued generation, highlighting the value of directly balancing quality and diversity during pruning.

### 8. OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing

- 作者：Ariel Slepyan, Geeta Chandra Raju Bethala, Jiafeng Gu, Anagha Rajendra Dangle, Yinzhe Zhou, Hongyuan Fu, Jade Sim, Tuhin Basu 等｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.31661v1

> 命中：hit_abstract=['policy learning']

### 背景/问题
We present OpenTac, a novel sensor and a full-stack ecosystem for tactile skins that are highly customizable, scalable, and readily deployed in downstream robot control and learning applications. Our core contribution is twofold.

### 方法
We present OpenTac, a novel sensor and a full-stack ecosystem for tactile skins that are highly customizable, scalable, and readily deployed in downstream robot control and learning applications. First, we develop a scalable resistive tactile skin with a structured deformable overlay that converts tangential loading into spatially varying pressure. We develop an ecosystem around the OpenTac sensor, including the CAD design tool, a sensor simulator, cross-sensor transfer, and fast/adaptive data acquisition.

### 实验/数据
We develop an ecosystem around the OpenTac sensor, including the CAD design tool, a sensor simulator, cross-sensor transfer, and fast/adaptive data acquisition. We characterize the three-dimensional tactile fields produced by OpenTac with a commercial, high-precision force/torque sensor.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We provide all hardware, software, and result videos are at opentac.github.io

### 9. On the Token Collapse Phenomenon in Textual Graph Soft Prompting

- 作者：Andrea Giuseppe Di Francesco, Rishabh Jain, Franco Maria Nardini, Nicola Tonellotto, Pietro Liò, Fabrizio Silvestri｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.31572v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Recent methods for injecting graph structure into LLM prompts include graph soft prompting, in which a graph neural network (GNN) learns graph-specific tokens that capture relational information among entities in textual prompts. G-Retriever combines graph soft prompts with a verbalized description of the same graph to strengthen the textual prompt signal.

### 方法
Across three benchmarks, three graph encoders, two LLM families, and both frozen and LoRA-adapted models, G-Retriever's graph tokens become almost indistinguishable across inputs. We also examine conditions linked to this collapse and propose a two-stage procedure that yields non-collapsed tokens while maintaining competitive performance in most cases. However, token variability alone does not prove that the model uses graph information: via interventions and decoding probes, we show that depending on the configuration, a token can reflect the question, an answer prior, or graph-derived content that the LLM may or may not use.

### 实验/数据
Under the standard setup, swapping a token with the dataset mean, a token from another example, or one derived from a corrupted graph produces no resolved answer-level effect in accuracy. Code to reproduce our experiments is available at https://github.com/difra100/Token_Collapse_KGQA.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Code to reproduce our experiments is available at https://github.com/difra100/Token_Collapse_KGQA.

### 10. DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination

- 作者：Ziyi Jiao, Heng Zhang, Drishti Regmi, Xiaokang Ye, Lianhui Qin, Peter Yichen Chen｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.31511v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Coordinating two players in a cooking task requires a vision-language agent to track changing scene states, sequence recipe steps, and allocate shared resources under a time budget. We introduce an Overcooked-inspired benchmark for evaluating these capabilities in Unreal Engine environments constructed using coding agents.

### 方法
A single vision-language model controls both players from top-down visual observations, selecting high-level actions while the engine executes navigation. The evaluation compares four VLMs on all 20 maps, measuring task score, order completion, delivery precision, action acceptance rate, and model API expenditure. The strongest evaluated model, \texttt{gpt-6-astra}, achieves 26.2\% mean order completion.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Notebook memory has mixed score effects across models, with positive mean differences for Claude and Qwen and negative differences for GPT and Gemini.

### 11. More efficient transportation of causal effects using mediators

- 作者：Xinyi Zhang, Kara E. Rudolph, James Russell Pike, Richard Liu, Michele Santacatterina, Iván Díaz｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.31568v1

> 命中：hit_abstract=['treatment effect']

### 背景/问题
We develop flexible semiparametric estimators of the average treatment effect transported to a target population that leverage mediators to achieve identification, and prior knowledge of population heterogeneity or summary-level statistics to achieve improved efficiency. We first propose a one-step semiparametric estimator that assumes knowledge of the baseline covariates driving the heterogeneity across populations.

### 方法
We develop flexible semiparametric estimators of the average treatment effect transported to a target population that leverage mediators to achieve identification, and prior knowledge of population heterogeneity or summary-level statistics to achieve improved efficiency. We first propose a one-step semiparametric estimator that assumes knowledge of the baseline covariates driving the heterogeneity across populations. This approach improves efficiency by transporting only through these covariates, rather than through the full covariate set.

### 实验/数据
We use simulation to examine finite-sample performance and apply our estimators to a large-scale housing mobility trial (MTO) and a hearing intervention trial (ACHIEVE).

### 结果
We develop flexible semiparametric estimators of the average treatment effect transported to a target population that leverage mediators to achieve identification, and prior knowledge of population heterogeneity or summary-level statistics to achieve improved efficiency. This approach improves efficiency by transporting only through these covariates, rather than through the full covariate set. We then introduce a collaborative one-step semiparametric estimator that also improves efficiency without requiring knowledge of which covariates drive study heterogeneity.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We use simulation to examine finite-sample performance and apply our estimators to a large-scale housing mobility trial (MTO) and a hearing intervention trial (ACHIEVE).

### 12. Ricci flow of Integrable Sigma Models, Hitchin Systems and Quantum Seiberg-Witten theory

- 作者：G. Bonelli, S. Lacroix, T. Pedroni, A. Tanzini｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31672v1

### 背景/问题
We construct a family of integrable 2d sigma models through 4d Chern-Simons theory and show that their classical point-particle reduction corresponds to a Hitchin system. The integrable Hitchin quantisation then provides a natural candidate Hamiltonian for the one-loop reduced dynamics of the sigma models, which coincides with the Perelman operator in all cases examined.

### 方法
We construct a family of integrable 2d sigma models through 4d Chern-Simons theory and show that their classical point-particle reduction corresponds to a Hitchin system. The integrable Hitchin quantisation then provides a natural candidate Hamiltonian for the one-loop reduced dynamics of the sigma models, which coincides with the Perelman operator in all cases examined. For the sausage model, we derive exact quantisation conditions and compute exponentially small corrections essential for the agreement with numerical finite-volume results.

### 实验/数据
This allows us to study the corresponding spectral problems using 4d $\mathcal{N}=2$ gauge theory and 2d conformal field theory methods.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
For the sausage model, we derive exact quantisation conditions and compute exponentially small corrections essential for the agreement with numerical finite-volume results.

### 13. Collapsed translating solitons with planar wings

- 作者：Eddygledson Souza Gama, Francisco Martín, Niels Martin Møller｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31669v1

### 背景/问题
We study complete embedded translating solitons in R^3 with finite genus and finite entropy. We prove that such collapsed translators whose wings are all of planar type (in a weak topological sense) must be vertical flat planes.

### 方法
未在摘要中明确给出。

### 实验/数据
A key ingredient is a sharp new a priori decay estimate in the exterior problem for the horizontal graphical translator equation, showing that bounded solutions to the nonlinear equation, and their gradients, are controlled by multiples of the Green's function of the linear drift Laplacian, regardless of the size of the given L^\infty data.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
As another application, we obtain a full classification of collapsed embedded finite-genus translators of entropy lambda < 3.

### 14. Cost-Aware Abstention for LLM-Based IT Ticket Classification

- 作者：Sachin Gupta｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31657v1

### 背景/问题
Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data.

### 方法
On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four large language models under zero- and few-shot prompting. Under the illustrative cost model (c_ok, c_triage, c_wrong) = (0, 1, 5), TF-IDF with logistic regression and a threshold of 0.60 selected on calibration reduces test cost from 0.763 to 0.472, a 38.1% relative reduction (paired ratio-bootstrap 95% CI [35.7%, 40.4%]), while lowering wrong routes from 15.3% to 3.5%. The findings are scoped to this dataset, prompt design, model endpoints, and illustrative costs; the work is an evaluation framework, not a new abstention algorithm or universal deployment certification.

### 实验/数据
We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. Frozen calibration-selected policies also beat both always-route and always-defer on held-out test data in 14 of 16 settings in a post-hoc cost-parameter analysis. The findings are scoped to this dataset, prompt design, model endpoints, and illustrative costs; the work is an evaluation framework, not a new abstention algorithm or universal deployment certification.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The findings are scoped to this dataset, prompt design, model endpoints, and illustrative costs; the work is an evaluation framework, not a new abstention algorithm or universal deployment certification.

### 15. EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence

- 作者：Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu, Zhongxiang Dai, Shuang Qiu｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31650v1

### 背景/问题
Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true.

### 方法
Tool-using language model agents rely on environmental facts to decide whether an action is permitted. The benchmark reveals substantial variation across the ten models in omission robustness, evidence acquisition, and appropriate action. Recovery access reduces unsafe execution for all ten models, but agents differ in whether they actively obtain the missing facts and use them to act appropriately in both worlds.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Recovery access reduces unsafe execution for all ten models, but agents differ in whether they actively obtain the missing facts and use them to act appropriately in both worlds.

### 16. Magnetic Activity as a Driver of Low-gravity-like Spectral Morphology in Late-M Dwarfs

- 作者：Chia-Lung Lin, Daniel Apai, Benjamin V. Rackham, Prajwal Niraula, Mark S. Giampapa, Ana Glidden, Julien de Wit, Valeriy Vasilyev 等｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31647v1

### 背景/问题
We present a systematic investigation of the connection between magnetic activity and the low-surface-gravity-like near-infrared spectral morphology of late-M dwarfs. Our sample includes TRAPPIST-1 observed with JWST NIRISS/SOSS and 22 late-M dwarfs observed with IRTF/SpeX, together with flare observations from K2, TESS, JWST NIRISS/SOSS, and literature-reported X-ray luminosities.

### 方法
We present a systematic investigation of the connection between magnetic activity and the low-surface-gravity-like near-infrared spectral morphology of late-M dwarfs. Using one-component PHOENIX/NewEra spectral modeling, we find that all targets are better reproduced by lower-surface-gravity model spectra than by models with the expected high gravities of field late-M dwarfs.

### 实验/数据
Using one-component PHOENIX/NewEra spectral modeling, we find that all targets are better reproduced by lower-surface-gravity model spectra than by models with the expected high gravities of field late-M dwarfs. A simplified radiative-transfer experiment further shows that activity-associated heating can produce lower-gravity-like spectral features even when the input surface gravity is fixed.

### 结果
Using one-component PHOENIX/NewEra spectral modeling, we find that all targets are better reproduced by lower-surface-gravity model spectra than by models with the expected high gravities of field late-M dwarfs. The retrieved surface gravities moderately correlate with independently measured gravity-sensitive spectral indices, with the strongest trends seen for FeH$_z$ at 0.998~$μ$m and FeH$_J$ at 1.2~$μ$m, both showing statistically significant Pearson and Spearman correlations with $p<0.005$.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our results suggest that underestimated surface gravities in late-M dwarfs may reflect atmospheres modified by frequent, small-scale magnetic activity, such as microflares, producing emergent spectra that mimic lower-gravity morphology.

### 17. Extending Harmonic Function Methods via Root Locus for Coordinated Path Generation

- 作者：Matteo Frascarelli, Lucia Pallottino, Alberto Landi｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31625v1

### 背景/问题
We consider the offline generation of coordinated paths for N interchangeable robots and N goals in planar environments with polygonal obstacles. After a conformal map to a circular domain, starts and goals become the poles and zeros of a rational function R, and the paths are the branches of its Generalized Root Locus (GRL), i.e.

### 方法
未在摘要中明确给出。

### 实验/数据
We consider the offline generation of coordinated paths for N interchangeable robots and N goals in planar environments with polygonal obstacles.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The method is illustrated on two polygonal workspaces, 100 random instances compared with independent harmonic planning and artificial potentials, and a scene with ten robots and ten obstacles.

### 18. The Asymptotic Number of Anticodes in Hamming Spaces

- 作者：Anna-Lena Horlemann, Ananthakrishnan Ravi｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31618v1

### 背景/问题
In the Hamming space $\mathbb{F}_q^n$, a $d$-anticode is a subset in which every pair of points has Hamming distance at most $d$, or equivalently, a set of diameter at most $d$. Let $m_q(n,d)$ denote the maximum size of a $d$-anticode and let $\mathcal{A}_q(n,d)$ be the family of all $d$-anticodes.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
A random-generator construction further improves the binary lower bound for every fixed linear diameter.

### 结论/启示（面向电商发券、定价、营销算法等应用）
A random-generator construction further improves the binary lower bound for every fixed linear diameter.

### 19. OP-Print: Tracing Membership Imprints in On-Policy Self-Distillation

- 作者：Qi Li, Xinchao Wang｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31616v1

### 背景/问题
On-policy distillation has been widely adopted for alleviating the distribution mismatch of off-policy distillation. Self-distillation further removes the need for an external teacher by using the student's own outputs, enhanced with extra context or demonstrations, as supervision.

### 方法
Motivated by this, we present the first study of membership inference attacks against on-policy self-distillation. We investigate both gray-box and black-box threat models and propose a unified attack framework, named OP-Print. Across diverse models and distillation schemes, all baseline attacks remain essentially at random guessing even under gray-box access, whereas OP-Print is broadly validated to be effective in both gray-box and black-box settings.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Across diverse models and distillation schemes, all baseline attacks remain essentially at random guessing even under gray-box access, whereas OP-Print is broadly validated to be effective in both gray-box and black-box settings.

### 20. How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions

- 作者：Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias, Thaís Gaudêncio, Yuri Malheiros, Barufaldi｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31606v1

### 背景/问题
Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-augmented generation (RAG) system over breast lesion management literature, addressing the dependence of retrieval scores on annotation coverage. Methods: An 18-document corpus and an 18-query development benchmark, with one Yes/No or WH-question per document, were used.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
Ground-truth curation increased evidence spans from 25 to 37 and accepted chunk targets from 36 to 51 without changing retrieval rankings. Expanded relevance annotations increased recognized evidence without changing rankings, highlighting annotation sensitivity.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The small development set and retrieval-informed curation require independent validation, including radiologist assessment of evidence sufficiency.

### 21. A Priori Estimation of the Non-Linear Compression Potential and Quantification of Autoencoder Non-Linearity in Turbulent Flows

- 作者：Niklas Alexander Pissarski, Juan Pablo Murcia Leon, Søren Juhl Andersen｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31605v1

### 背景/问题
Data-driven reduced-order modelling (ROM) of turbulent flows is based on an efficient and physical low-dimensional representation of the flow process. Such a dimension reduction can be achieved using proper orthogonal decomposition (POD) or non-linear autoencoders.

### 方法
Data-driven reduced-order modelling (ROM) of turbulent flows is based on an efficient and physical low-dimensional representation of the flow process. This work proposes the local tangent residual (LTR) as an a priori estimate of the potential benefit of non-linear dimension reduction for a given dataset. The LTR is based on the local geometry of the data points, requiring neither prior model training nor the definition of a threshold parameter.

### 实验/数据
Data-driven reduced-order modelling (ROM) of turbulent flows is based on an efficient and physical low-dimensional representation of the flow process. This work proposes the local tangent residual (LTR) as an a priori estimate of the potential benefit of non-linear dimension reduction for a given dataset. The LTR is based on the local geometry of the data points, requiring neither prior model training nor the definition of a threshold parameter.

### 结果
Capturing the inherent non-linearities in turbulent flows offers the potential for improved compression rates.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The LTR thus enables practitioners in turbulent flow modelling to determine a priori whether non-linear compression is worthwhile, avoiding the substantial computational cost of autoencoder architecture search and hyperparameter tuning in cases where POD already suffices.

### 22. Properties of theories whose algebras are free

- 作者：Tom Leinster, Maia Woolf｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31599v1

### 背景/问题
A hard theorem of Givant classifies the finitary algebraic theories for which every algebra is free. From it, one easily deduces that all such theories are minimal (adding any further equations makes them trivial) and have a well-defined notion of dimension (free algebras on sets of different cardinality are never isomorphic).

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We prove both these properties directly, without the aid of Givant's theorem.

### 23. Sharp fractional Hardy--Maz'ya remainders on half-spaces: angular reduction and energy stability

- 作者：Shengbing Deng, Dehong Yang｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31595v1

### 背景/问题
For $d\geq2$, $0<s<1$, $p>1$, and $τ>0$, we study the sharp half-space remainder \[ [u]_{s,p,+}^p-\mathcal D_{d,s,p}\int_{\mathbb R^d_+}x_d^{-sp}|u|^p\,dx \geqΛ_{d,s,p,τ}\int_{\mathbb R^d_+} \frac{x_d^{τ-sp}|u|^p}{(x_{d-1}^2+x_d^2)^{τ/2}}\,dx. \] We first obtain exact dimensional and angular reductions by an $L^p$ contraction.

### 方法
For $p=2$, we identify the planar sharp coefficient with the simple first eigenvalue of a singular angular operator with compact resolvent.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we prove normalized local limits for the sharp quadratic constant, each fixed fiber eigenvalue, and the dispersion coefficient.

### 24. Upper tail large deviations of regular subgraph counts in sparse random regular graphs

- 作者：Anirban Basak, Shaibal Karmakar｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31590v1

### 背景/问题
For a $Δ$-regular connected graph $H$ we obtain the upper tail large deviations speed and rate function for the number of copies of $H$ in $\mathbb{G}_n^d$, a random $d$-regular graph on $n$ vertices, in the regime $np^{Δ/2} \gg (\log n)^{1/(v_H-2)}$ and $p \ll 1$, where $p:=d/n$ and $v_H$ is the number of vertices, and also identify the typical structure of $\mathbb{G}_n^d$ conditioned on this upper tail event. For $Δ\geq 3$, the speed and the rate function are same with those in the Erdős-Rényi setting.

### 方法
For a $Δ$-regular connected graph $H$ we obtain the upper tail large deviations speed and rate function for the number of copies of $H$ in $\mathbb{G}_n^d$, a random $d$-regular graph on $n$ vertices, in the regime $np^{Δ/2} \gg (\log n)^{1/(v_H-2)}$ and $p \ll 1$, where $p:=d/n$ and $v_H$ is the number of vertices, and also identify the typical structure of $\mathbb{G}_n^d$ conditioned on this upper tail event. Moreover, conditioned on the upper tail event of cycle counts in $\mathbb{G}_n^d$, we show that the random graph contains a disjoint collection of clique and biclique like structures with probability approaching to one, a stark contrast compared to the Erdős-Rényi setting.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In this regime, we further show that almost all of the unlabeled copies of $H$ conditioned on the upper tail event are edge disjoint.

### 25. Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration

- 作者：Deepthika S, Pawni Yadav, B. Sankar｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31579v1

### 背景/问题
Research on sycophancy asks whether large language models (LLMs) bend towards what their users want to hear. We ask the reverse question: when an LLM is confident, consistent, and wrong, do users bend towards it?

### 方法
Research on sycophancy asks whether large language models (LLMs) bend towards what their users want to hear. In a within-subjects experiment, 32 participants learned up to five science topics by chatting with five assistants built on the same model (GPT-5-mini). Absorbed falsehoods were held with high confidence (8.4/10), the modeled confidence advantage of right over wrong answers vanished, and the discrimination of confidence for correctness fell from an AUROC of 0.70 to chance, while post-task trust ratings barely moved.

### 实验/数据
In a within-subjects experiment, 32 participants learned up to five science topics by chatting with five assistants built on the same model (GPT-5-mini).

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We introduce a baseline-corrected Human Deference Index to quantify this human-side sycophancy and argue that trustworthiness is a property of the human-AI pair, that sycophancy evaluations should measure both directions, and that learning interfaces must make reliability legible claim by claim.

### 26. Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via CubeAtlas

- 作者：Xuhui Zuo, Chenjie Cao, Tengfei Wang, Junta Wu, Yisu Zhang, Chunchao Guo｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31565v1

### 背景/问题
Generating 360-degree panoramas requires both local perspective fidelity and global spherical continuity. Existing representations face a trade-off: equirectangular projection (ERP) enables seamless panorama modeling but suffers from severe distortion and a domain gap to pre-trained image generators, whereas cubemaps preserve perspective geometry but often produce inconsistent faces and visible seams.

### 方法
Existing representations face a trade-off: equirectangular projection (ERP) enables seamless panorama modeling but suffers from severe distortion and a domain gap to pre-trained image generators, whereas cubemaps preserve perspective geometry but often produce inconsistent faces and visible seams. We present Squaring-the-Sphere, a panoramic image generation framework built on a novel representation CubeAtlas, which unfolds all cubemap faces into a single compact canvas. It further enables a pretrained diffusion transformer to model the complete panorama jointly in a single pass, without altering the backbone architecture or positional encoding.

### 实验/数据
Experiments on various benchmarks demonstrate that our method improves geometric fidelity, cross-view consistency, and high-resolution visual quality over previous methods.

### 结果
As a result, CubeAtlas achieves better quality than ERP modeling with lower attention computation. Experiments on various benchmarks demonstrate that our method improves geometric fidelity, cross-view consistency, and high-resolution visual quality over previous methods.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Experiments on various benchmarks demonstrate that our method improves geometric fidelity, cross-view consistency, and high-resolution visual quality over previous methods.

### 27. The domination number of the 2-token graph of the complete bipartite graph

- 作者：E. Acosta Troncoso, I. Caldera Caldera, L. M. Rivera｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31557v1

### 背景/问题
For a graph $G$, the $2$-token graph $F_2(G)$ has as vertices all $2$-subsets of $V(G)$, with two such subsets adjacent whenever their symmetric difference is an edge of $G$. In this paper, we determine the domination number of the $2$-token graph of the complete bipartite graph $K_{m,n}$, for all integers $2\le m\le n$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our arguments rely on an explicit characterization of the dominating sets of the $2$-token graph of $K_{m,n}$.

### 28. ArcTN: Efficient Tensor-Network Contraction Planning for Quantum Circuit Simulation

- 作者：Zhengyi Liu, Li Liu, Songtao Liu, Xianglong Liu, Xiangzhen Zhou, Mingyu Huang, Dingchao Gao, Shenggang Ying 等｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31554v1

### 背景/问题
Tensor-network simulation of quantum circuits depends on contraction orders with low computational cost and small intermediate tensors, found without excessive planning time. We present ArcTN, a contraction-order optimization framework with two search presets.

### 方法
We present ArcTN, a contraction-order optimization framework with two search presets.

### 实验/数据
Tensor-network simulation of quantum circuits depends on contraction orders with low computational cost and small intermediate tensors, found without excessive planning time.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
On 672 networks built from 320 MQT Bench circuits, Heavy obtains the lowest geometric-mean FLOPs on the 142 large networks while planning 3.1$\times$ and 31$\times$ faster than Cotengra AutoHQ and Hyper128.

### 29. CAMGen: A Core Change-Aware Multi-View Framework for Commit Message Generation

- 作者：Bo Xiong, Weisheng Chen, Zongen Ren, Yifeng Zhu, Xutian Li, Runbang Yan, Chong Wang, Peng Liang｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31552v1

### 背景/问题
Commit messages help developers understand code changes and support software maintenance. Recent approaches use repository context to improve commit message generation (CMG) with large language models (LLMs).

### 方法
Recent approaches use repository context to improve commit message generation (CMG) with large language models (LLMs). To address this problem, we propose CAMGen, a core change-aware multi-view commit message generation framework that incorporates functional context into generation.

### 实验/数据
The experimental results show that CAMGen outperforms representative CMG baselines across three programming languages.

### 结果
Recent approaches use repository context to improve commit message generation (CMG) with large language models (LLMs). The experimental results show that CAMGen outperforms representative CMG baselines across three programming languages.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results demonstrate the value of functional context and complementary repository information for CMG.

### 30. Fine-Grained Analysis of Catastrophic Forgetting in Continual Learning via Algorithmic Stability

- 作者：Guodong Zheng, Yan Sun, Peng Wang, Enneng Yang, Jiafei Lyu, Xiaochun Cao, Dacheng Tao, Li Shen｜年份：2026｜发布时间：2026-10-22｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.31551v1

### 背景/问题
Understanding catastrophic forgetting, in which learning new tasks degrades performance on previously learned tasks, remains a fundamental challenge in continual learning (CL). Existing theoretical analyses often rely on specific model or task structures and offer limited insight into how iterative optimization affects forgetting.

### 方法
Existing theoretical analyses often rely on specific model or task structures and offer limited insight into how iterative optimization affects forgetting. To address this gap, we develop an algorithmic stability framework for expected population forgetting under SGD without prescribing a particular model architecture.

### 实验/数据
Finally, we conduct experiments on Split CIFAR-100 and Split MiniImageNet to examine the empirical implications of our theoretical findings.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we conduct experiments on Split CIFAR-100 and Split MiniImageNet to examine the empirical implications of our theoretical findings.
