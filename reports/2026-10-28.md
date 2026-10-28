# CausalRadar 日报 - 2026-10-28

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation

- 作者：Nesta Midavaine, Floris Fok, Paulo Mendes, Joao Silva, Önder Akaçık, Dimas Lima, Zülküf Genç｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**17.00**
- 链接：https://arxiv.org/abs/2610.37570v1

> 命中：hit_scenario=['promotion']；hit_method=['uplift']；hit_title=['promotion', 'uplift']；hit_abstract=['promotion']

### 背景/问题
We present LCM-Promo, an LLM-based uplift model for promotion allocation. LCM-Promo is a task-specific Large Commerce Model (LCM): a finetuned LLM trained on transactional commerce data to predict user intent and promotion response.

### 方法
We present LCM-Promo, an LLM-based uplift model for promotion allocation. LCM-Promo is a task-specific Large Commerce Model (LCM): a finetuned LLM trained on transactional commerce data to predict user intent and promotion response.

### 实验/数据
LCM-Promo is a task-specific Large Commerce Model (LCM): a finetuned LLM trained on transactional commerce data to predict user intent and promotion response. In a production A/B test on churn reactivation, LCM-Promo increased conversion by 1% and reduced promotion cost by 6% relative to the Segment-EMA production baseline.

### 结果
We present LCM-Promo, an LLM-based uplift model for promotion allocation. In a production A/B test on churn reactivation, LCM-Promo increased conversion by 1% and reduced promotion cost by 6% relative to the Segment-EMA production baseline.

### 结论/启示（面向电商发券、定价、营销算法等应用）
In a production A/B test on churn reactivation, LCM-Promo increased conversion by 1% and reduced promotion cost by 6% relative to the Segment-EMA production baseline.

### 2. Global minimax rates for heterogeneous treatment effect estimation

- 作者：Shuhan Liu, Matey Neykov｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**16.50**
- 链接：https://arxiv.org/abs/2610.37496v1

> 命中：hit_method=['heterogeneous treatment effect']；hit_title=['treatment effect', 'heterogeneous treatment effect']；hit_abstract=['treatment effect', 'CATE']

### 背景/问题
Recent work established minimax rates for pointwise estimation of the conditional average treatment effect (CATE), but the fundamental limits under global losses remained unresolved. We derive matching minimax lower and upper bounds under the $L_2$ and $L_\infty$ risks on certain covariate-density and support classes.

### 方法
For the lower bounds, we develop a many-fuzzy-hypotheses method that replaces each fixed alternative in a multiple-hypothesis construction with a mixture over nuisance functions that leaves its CATE unchanged.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The resulting rates show that the pointwise elbow phenomenon persists globally: the $L_2$ transition threshold is unchanged, while the $L_\infty$ rate has an additional logarithmic factor and a transition threshold adjusted by $1-\log\log n/\log n$.

### 3. REGER: Modeling inter-item Relations with Semantic IDs for Generative Recommendation

- 作者：Yuxi Huang, Silin Zhou, Chenhao Wang, Zihan Li, Gangming Guo, Pei Ke, Shen Gao, Shuo Shang｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**9.00**
- 链接：https://arxiv.org/abs/2610.37584v1

> 命中：hit_scenario=['recommendation']；hit_title=['recommendation']

### 背景/问题
Personalized recommendation depends on learning semantic and collaborative relations among items from online content and user interactions. Generative recommendation (GR) offers a promising paradigm by autoregressively generating discrete semantic IDs (SIDs) of items.

### 方法
However, randomly initialized SID token embeddings and GR models trained from scratch do not directly inherit the semantic relations inherent in items, while inter-item collaborative relations are learned largely implicitly through token-level attention and next-token supervision. To address this limitation, we propose REGER, a unified framework that explicitly incorporates inter-item relations into semantic pretraining, history encoding, and SID generation. We pretrain the GR model through generative semantic retrieval, enabling it to inherit inter-item semantic similarity by learning to generate semantic neighbors' SIDs.

### 实验/数据
Personalized recommendation depends on learning semantic and collaborative relations among items from online content and user interactions. Extensive experiments on real-world datasets demonstrate consistent improvements over existing GR baselines and support the effectiveness of the proposed preference distillation.

### 结果
Extensive experiments on real-world datasets demonstrate consistent improvements over existing GR baselines and support the effectiveness of the proposed preference distillation.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Extensive experiments on real-world datasets demonstrate consistent improvements over existing GR baselines and support the effectiveness of the proposed preference distillation.

### 4. Practical Guidelines for Goodness-of-Fit Testing for Right-Censored Data

- 作者：Arnau Gómez-Català, Guadalupe Gómez Melis, Klaus Langohr｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**7.00**
- 链接：https://arxiv.org/abs/2610.37513v1

> 命中：hit_scenario=['recommendation']；hit_abstract=['CATE']

### 背景/问题
In survival studies, right censoring often prevents the observation of subjects' complete outcomes, complicating inference about the underlying distribution. Evaluating whether a given distribution adequately fits right-censored data is therefore essential.

### 方法
In this work, we present a comparative assessment of three classical goodness-of-fit tests adapted for right-censored data: Kolmogorov-Smirnov, Anderson-Darling, and Cramér-von Mises. The results identify the settings in which each test exhibits superior performance, providing practical, evidence-based recommendations for test selection in survival analysis. These recommendations are summarized as user-oriented guidelines and complemented by a concise graphical cheat sheet, enabling practitioners to quickly identify the most suitable test for their specific application.

### 实验/数据
Evaluating whether a given distribution adequately fits right-censored data is therefore essential. However, guidance on the relative performance of available goodness-of-fit tests under different data conditions remains limited. In this work, we present a comparative assessment of three classical goodness-of-fit tests adapted for right-censored data: Kolmogorov-Smirnov, Anderson-Darling, and Cramér-von Mises.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These recommendations are summarized as user-oriented guidelines and complemented by a concise graphical cheat sheet, enabling practitioners to quickly identify the most suitable test for their specific application.

### 5. Resurgence of Black Holes in Thermal OPE

- 作者：Alba Grassi, Hewei Frederic Jia｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.37554v1

> 命中：hit_scenario=['ads']

### 背景/问题
The momentum-space thermal OPE generically gives an asymptotic high-energy expansion of thermal two-point functions. We study the resurgent structure of this expansion in holographic CFTs at infinite and finite volume, whose dual bulk geometries are planar and spherical AdS black holes, respectively.

### 方法
Using exact WKB analysis, we identify the locations of the associated Borel singularities as WKB actions between the AdS boundary and distinguished points in the complex radial plane, which include the black hole singularity in certain regimes. Furthermore, we identify a complex-frequency chamber in the timelike momentum regime where Borel resummation of the high-energy expansion reconstructs the full thermal two-point function.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We further derive Stokes jumps that determine the non-perturbative contributions required upon crossing the boundary of this chamber.

### 6. GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting

- 作者：Joseph Natter, Long Vu, Yifan Zhang, Bobin Deng, Kun Suo, Rui Wu｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.37598v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly.

### 方法
Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly. To combine graph-aware traffic modeling with zero-shot adaptation, we introduce the Graph-Aware Spatiotemporal Prior-Data Fitted Network (GAS-PFN).

### 实验/数据
Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly. Prior-Data Fitted Networks (PFNs) offer a zero-shot alternative by learning in-context inference from synthetic task priors, which provide an explicit mechanism for encoding domain-specific assumptions. To combine graph-aware traffic modeling with zero-shot adaptation, we introduce the Graph-Aware Spatiotemporal Prior-Data Fitted Network (GAS-PFN).

### 结果
These results indicate that aligning PFN priors and inference architectures with graph structure improves in-context learning for zero-shot traffic forecasting.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results indicate that aligning PFN priors and inference architectures with graph structure improves in-context learning for zero-shot traffic forecasting.

### 7. EgoThumb: A Vision-Driven Supernumerary Robotic Thumb for Autonomous Grasp and Holding Assistance

- 作者：Jianyu Hou, Jiawei Fu, Weikang Wan, Minghui Jiang, Jiajun Li, Hao Su｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.37582v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Supernumerary robotic fingers augment human dexterity by enabling a single hand to perform complex "hold-and-manipulate" tasks that typically require bimanual coordination. However, existing devices are often hindered by bulky hardware that limits interaction to large objects and rely on explicit hand motion triggers that lack environmental context.

### 方法
To address these challenges, we present EgoThumb, a fully open-source, vision-driven supernumerary robotic thumb.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
All hardware designs and software implementations are fully open-sourced at https://ego-thumb.github.io.

### 8. Predict the Swing, Match the Speed: Robotic Pipe Stabbing With Learned Stereo Vision and Residual Reinforcement Learning

- 作者：Mohamed Ashraf Mostafa, Taher El-Fakharany, Samir Khaled｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.37535v1

> 命中：hit_abstract=['CATE']

### 背景/问题
A joint of pipe run into the hole swings from the elevator over the well and strikes a fixed stabbing guide at whatever speed the swing has. StabBot, a robotic stabbing system, predicts the swing and meets the pipe at its own speed.

### 方法
All results come from a 1:4 Froude-scaled MuJoCo model and are reported at full scale.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
All results come from a 1:4 Froude-scaled MuJoCo model and are reported at full scale.

### 9. An EVM-Cosmos Bridge for Atomic, Semantic-Preserving Transfer of Environmental Tokens

- 作者：Sebastian Pandolfi, Guzmán Llambías, Laura González｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37663v1

### 背景/问题
Transferring semantically typed tokens between heterogeneous blockchains (e.g. EVM and Cosmos ecosystems) raises two problems: semantic mixing, the loss of a token's domainspecific meaning in transit (e.g., CO2 removals issued under different methodologies), and atomicity despite divergent consensus and timing assumptions.

### 方法
We propose a bridge that addresses both.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also document the integration failure modes of Cosmos originated messaging, whose dominant operational risk proves to be relay eligibility rather than latency.

### 10. When Should We Intervene at Test Time?

- 作者：Jiahao Zhang, Xinling Wen, Liangliang Li, Yu Chen｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37658v1

### 背景/问题
Test-time adaptation helps a deployed model respond to changing inputs, but the same intervention can rescue one batch and damage the next. Updating normalization statistics, for example, can improve corrupted images yet fail when a batch contains mostly one class.

### 方法
Test-time adaptation helps a deployed model respond to changing inputs, but the same intervention can rescue one batch and damage the next. Average accuracy hides these failures and cannot tell a model when to use an intervention.

### 实验/数据
Experiments show that this control turns an intervention that loses accuracy overall into a useful choice on selected batches.

### 结果
Updating normalization statistics, for example, can improve corrupted images yet fail when a batch contains mostly one class. The same feedback therefore improves both the choice made now and the predictions available to later batches.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The same feedback therefore improves both the choice made now and the predictions available to later batches.

### 11. Attention as Lattice Gauge Theory: Relations Interact Only Through Wilson Loops

- 作者：Aakash Sarkar, Ananya Mukherjee, Motoshige Sato｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37656v1

### 背景/问题
Relations compose through the entity they share - Alice is Bob's mother and Bob is Carol's father, so Alice is Carol's grandmother - and the order matters, since a father's mother is not a mother's father; verifying a composed relation means closing the loop. We show that if each entity's coordinate frame may be rotated independently (per-entity frame freedom), three things follow.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
With no training and composition alone, it infers unobserved $S_4$ relations on sparse graphs at 0.88 with a fifth of the edges corrupted, at or slightly below specialist synchronization algorithms, where every commutative architecture is capped at 0.083; its holonomy score flags corrupted triangles at AUC 0.99 where commuting scores are capped at 0.76 by a second selection rule, and it separates clusters without labels.

### 12. Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions

- 作者：Anouar Imel, Imad Charradi, Abderrahman Sghir, Khalil El Khammar｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37624v1

### 背景/问题
When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria.

### 方法
Across Qwen2.5-7B, Llama-3.1-8B, and two DeepSeek models, both heuristics fail in predictable places. The decision model adds a third failure, a form of social proof: it gives extra weight to facts attributed to many agents.

### 实验/数据
未在摘要中明确给出。

### 结果
Rarest-first selection is no better than random selection on average and wins only where the rare facts happen to be the useful ones.

### 结论/启示（面向电商发券、定价、营销算法等应用）
In natural discussions the evidence is lost before any memory acts: the complete transcript yields lower accuracy than no notes at all.

### 13. A Quiet Night in the Millihertz Sky? LISA Forecasts from LIGO/Virgo/KAGRA Populations

- 作者：Ignacio Magaña Hernandez, Antonella Palmese｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37617v1

### 背景/问题
The high-mass black hole population inferred from ground-based observations can substantially affect the number of binaries detectable by the Laser Interferometer Space Antenna (LISA). We use population constraints based on data from the latest LIGO/Virgo/KAGRA Gravitational-Wave Transient Catalog (GWTC-5.0), as well as constraints from the O3 search for intermediate-mass black hole binaries, to forecast the number and masses of binary black holes detectable by LISA.

### 方法
The alternative population models we consider use a broken power law with two or three Gaussian peaks for either the primary-mass distribution or a common mass distribution for both black holes. For the three-peak model with the common mass distribution, extrapolating from $300$ to $1000M_\odot$ roughly doubles the median expected number of LISA detections to $\sim14$.

### 实验/数据
We use population constraints based on data from the latest LIGO/Virgo/KAGRA Gravitational-Wave Transient Catalog (GWTC-5.0), as well as constraints from the O3 search for intermediate-mass black hole binaries, to forecast the number and masses of binary black holes detectable by LISA.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Ground-based measurements of the high-mass population can therefore inform both LISA forecasts and the prospects for observing the same binaries through inspiral and merger.

### 14. Iwahori Whittaker functions for unramified quasi-split groups

- 作者：Solomon Friedberg, Claire Frechette, Henrik P. A. Gustafsson｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37614v1

### 背景/问题
Let $\mathbf{G}$ be a connected unramified quasi-split reductive group defined over a nonarchimedean local field $F$. This paper concerns the Iwahori Whittaker functions attached to the unramified principal series of $\mathbf{G}(F)$.

### 方法
未在摘要中明确给出。

### 实验/数据
Let $\mathbf{G}$ be a connected unramified quasi-split reductive group defined over a nonarchimedean local field $F$.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In doing so we build on the work for split groups of Brubaker, Bump and Licata; the new feature here is the appearance of a Hecke algebra with unequal parameters.

### 15. Stability of Axion--SU(2) Chromomagnetic Condensates with Stochastic Spin-2 Dressing

- 作者：Sha Azyzy, Azadeh Maleknejad, Vahid Kamali｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37610v1

### 背景/问题
We investigate whether a stochastic spin-2 gauge-field background can stabilize the chromomagnetic condensate of axion--SU(2) Yang--Mills theory at fixed axion Noether charge in flat spacetime. By coarse-graining the gauge field, we uncover a new class of statistically homogeneous and isotropic spin-2-dressed chromomagnetic condensates satisfying the classical background equations.

### 方法
Statistical positivity constrains the otherwise undetermined higher-point contributions through model-independent consistency conditions, without fixing their detailed momentum dependence.

### 实验/数据
We investigate whether a stochastic spin-2 gauge-field background can stabilize the chromomagnetic condensate of axion--SU(2) Yang--Mills theory at fixed axion Noether charge in flat spacetime. By coarse-graining the gauge field, we uncover a new class of statistically homogeneous and isotropic spin-2-dressed chromomagnetic condensates satisfying the classical background equations. First, at the mean-field (Hartree) level, we determine the fluctuation spectrum and the region where all modes remain positively gapped.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The results are relevant to non-Abelian gauge condensates in early-universe cosmology, including inflation, dark energy, and primordial gravitational waves, and to QCD-like gauge sectors above confinement where thermal effects are subleading.

### 16. A unified coarse-grained neural network potential for the dynamics of biomolecular complexes

- 作者：Antonio Mirarchi, Stephen E. Farr, Adrià Peréz, Gianni De Fabritiis｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37606v1

### 背景/问题
The behavior of biomolecular complexes is governed by chemically specific interactions and often involves rare events that atomistic molecular dynamics struggle to capture within accessible timescales. Here we introduce AMARO v2.0, a coarse-grained neural network potential that retains all heavy atoms and treats solvent implicitly.

### 方法
The model preserves folded proteins and captures key features of protein conformational free-energy landscapes. The same framework also recovers a reference binding pose in TYK2 and supports binding free-energy estimation for both trypsin-benzamidine and TYK2-EJM31, although the resulting values are more energetically favorable than the experimental references.

### 实验/数据
The same framework also recovers a reference binding pose in TYK2 and supports binding free-energy estimation for both trypsin-benzamidine and TYK2-EJM31, although the resulting values are more energetically favorable than the experimental references.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Together, these results support AMARO v2.0 as a shared heavy-atom potential for biomolecular complex dynamics.

### 17. Cosmological Constraints on Interacting Dark Matter with SPT-3G D1

- 作者：Cynthia Trendafilova, Fei Ge, Ali Rida Khalife, Christian L. Reichardt｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37604v1

### 背景/问题
Models of the dark sector in which the dark matter participates in nontrivial interactions can create detectable signatures in cosmological observables, providing non-terrestrial means of probing the nature of dark matter. In this work, we test dark matter-baryon scattering, dark matter-dark radiation interactions, and dark matter annihilation using measurements of the CMB and BAO.

### 方法
Models of the dark sector in which the dark matter participates in nontrivial interactions can create detectable signatures in cosmological observables, providing non-terrestrial means of probing the nature of dark matter. We leverage the latest SPT-3G D1 CMB measurements of the primary anisotropies, alongside the D1 MUSE lensing data, to set up-to-date bounds on these models. The improved sensitivity to the first two models is in particular driven by the precision measurements of CMB lensing at small scales provided by SPT-3G D1 MUSE lensing data.

### 实验/数据
We leverage the latest SPT-3G D1 CMB measurements of the primary anisotropies, alongside the D1 MUSE lensing data, to set up-to-date bounds on these models. From the combination of Planck, ACT DR6, and SPT-3G D1 data, we constrain the velocity-independent dark matter-baryon scattering cross-section to $σ_\mathrm{DM-b} < 4.6\times10^{-26}~\mathrm{cm^2}$, the dark matter-dark radiation momentum transfer rate to $Γ_\mathrm{0,nadm}<5.2\times10^{-8}\,\text{Mpc}^{-1}$, and the effective dark matter annihilation parameter, quantifying the fractional thermally averaged cross-section, to $p_\mathrm{ann}<3.7\times10^{-28}~\mathrm{cm^3/s/GeV}$, all at the 95% confidence level. The improved sensitivity to the first two models is in particular driven by the precision measurements of CMB lensing at small scales provided by SPT-3G D1 MUSE lensing data.

### 结果
The improved sensitivity to the first two models is in particular driven by the precision measurements of CMB lensing at small scales provided by SPT-3G D1 MUSE lensing data. Future CMB and BAO measurements will provide better clarity on reconciling this discrepancy and enhance our ability to test dark matter interactions.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Future CMB and BAO measurements will provide better clarity on reconciling this discrepancy and enhance our ability to test dark matter interactions.

### 18. The Acridine Polymorph Landscape: Characterization and Selective Control by Additives

- 作者：Adam Lahouari, Hengyu Zhou, Nikolaos Galanakis, Michael Kilgour, Daisuke Kuroshima, Jihye Han, Bart Kahr, Mark E. Tuckerman 等｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37597v1

### 背景/问题
Polymorphism in molecular crystals presents a major challenge for controlling crystallization. Here, we combine experiment and theory to characterize the polymorph landscape of acridine and investigate its selective control by additives.

### 方法
未在摘要中明确给出。

### 实验/数据
Here, we combine experiment and theory to characterize the polymorph landscape of acridine and investigate its selective control by additives. Melt crystallization experiments resolve the previously unknown structure of form VIII, while topological crystal structure prediction recovers all seven known unsolvated polymorphs with determined crystal structures. Combining a fine-tuned machine-learned interatomic potential with anharmonic free energy calculations reproduces the experimentally observed stability relationships and reveals a shallow free energy landscape.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Together, these results provide a comprehensive picture of acridine polymorphism, linking crystal structure, thermodynamic stability, and additive-controlled crystallization.

### 19. The UKIRT M33 Monitoring Project - VII. A 15-year K-band photometric catalogue of long-period variable stars in the central kiloparsec of M33

- 作者：Mina Alizadeh, Atefeh Javadi, Yousefali Abedini, Fatemeh Nikzat, Hedieh Abdollahi, Jacco Th. van Loon｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37591v1

### 背景/问题
We present a homogenised K-band photometric catalogue for the central ${\approx}12$ arcmin$^2$ (${\approx}0.9$ kpc$^2$) of the Triangulum spiral galaxy M33, combining four independent PSF-based near-infrared datasets obtained with UKIRT between 2003 and 2018. These comprise the 2003-2007 UIST multi-epoch monitoring survey, the 2005 UFTI K-band mosaic (for which we present new PSF photometry), new WFCAM PSF reductions for the four central tiles, and a single K-band epoch from the 2018 UKIRT Hemisphere Survey (UHS DR3).

### 方法
We present a homogenised K-band photometric catalogue for the central ${\approx}12$ arcmin$^2$ (${\approx}0.9$ kpc$^2$) of the Triangulum spiral galaxy M33, combining four independent PSF-based near-infrared datasets obtained with UKIRT between 2003 and 2018. These comprise the 2003-2007 UIST multi-epoch monitoring survey, the 2005 UFTI K-band mosaic (for which we present new PSF photometry), new WFCAM PSF reductions for the four central tiles, and a single K-band epoch from the 2018 UKIRT Hemisphere Survey (UHS DR3). Cross-matching with archival Spitzer IRAC photometry yields 156 matched stars, of which 120 satisfy $\langle K\rangle - [3.6] > 0.5$ mag, identifying dust-enshrouded AGB candidates inaccessible to all-sky optical surveys.

### 实验/数据
We present a homogenised K-band photometric catalogue for the central ${\approx}12$ arcmin$^2$ (${\approx}0.9$ kpc$^2$) of the Triangulum spiral galaxy M33, combining four independent PSF-based near-infrared datasets obtained with UKIRT between 2003 and 2018. Photometric homogenisation onto the 2MASS/Vega system via 82 low-scatter calibration stars removes systematic inter-dataset offsets of up to 0.22 mag.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The full catalogue is available at the Centre de Données astronomiques de Strasbourg (CDS).

### 20. Every route counts, but some count more: a max-plus view of the C. elegans brain

- 作者：Emma Reyner-Fuentes, Sebastian Rudolph, Carmen Peláez-Moreno, Francisco J. Valverde-Albacete｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37587v1

### 背景/问题
Brains do not simply add up every signal they receive: they select which routes dominate. Yet connectomes are usually analyzed with tools that sum over all paths and place neural states in Euclidean spaces, blurring the feedback circuits that may sustain internal states.

### 方法
We propose a model in which the functional connectome of Caenorhabditis elegans emerges from the time-varying combination of electrical, synaptic, monoaminergic, neuropeptidergic and hormonal layers, and analyze five networks within this framework.

### 实验/数据
Each collapses onto a handful of dominant feedback loops, which recover well-characterized circuits and point to new candidates for experimental study. Unlike linear spectra, these structures keep the biological meaning of the data, and their order-based description suggests that brain states live in lattices rather than Euclidean spaces.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Unlike linear spectra, these structures keep the biological meaning of the data, and their order-based description suggests that brain states live in lattices rather than Euclidean spaces.

### 21. Timestral

- 作者：Adrien Petralia, Alexandre Gavaudan, Artjom Joosen, Etienne Goffinet, Richard Kurle, Yassine El Ouahidi, Yassir Bendou, Abdelaziz Bounhar 等｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37585v1

### 背景/问题
We introduce Timestral, a family of four time series foundation models for probabilistic forecasting, with 5M, 28M, 123M, and 209M parameters. Timestral sets a new state of the art on GIFT-Eval, TIME, and fev-bench, where Timestral-209M and Timestral-123M take the top two places on every metric.

### 方法
We introduce Timestral, a family of four time series foundation models for probabilistic forecasting, with 5M, 28M, 123M, and 209M parameters. We achieve this with three ingredients: Decoupled Horizon Forecasting (DHF), which separates prediction tokens from the causally encoded context, so that longer horizons are trained without masking context and each observed value is both a forecast target and context for later forecasts; a covariate framework that natively supports known-future covariates within a causal architecture; and a two-stage pipeline that pretrains exclusively on a diverse, large-scale synthetic corpus before post-training on a mix of real and synthetic data with extended context. This report describes the model design and its benchmark results.

### 实验/数据
We achieve this with three ingredients: Decoupled Horizon Forecasting (DHF), which separates prediction tokens from the causally encoded context, so that longer horizons are trained without masking context and each observed value is both a forecast target and context for later forecasts; a covariate framework that natively supports known-future covariates within a causal architecture; and a two-stage pipeline that pretrains exclusively on a diverse, large-scale synthetic corpus before post-training on a mix of real and synthetic data with extended context.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Weights for all four models are available on Hugging Face and inference code on GitHub.

### 22. Spectral Braids: A Topological Descriptor for Dynamic Directed Networks

- 作者：Mehmet Emin Aktas, Esra Akbas｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37580v1

### 背景/问题
Eigenvalues are a workhorse of graph machine learning: spectral clustering, spectral graph neural networks, and graph kernels all summarize a network by the eigenvalues of a matrix. These eigenvalues are almost always treated as a static list of numbers.

### 方法
We propose spectral braids, a methodology for dynamic directed networks: each snapshot is aggregated into a community-level transition matrix, its complex eigenvalues are tracked over time, and the braid they trace is read off as a word. Our experimental results show that the proposed features reach 97.1% accuracy on four classes, against 44.5% for the best feature set that does not track eigenvalues, and that the Burau features also separate networks containing the same events in a different order, which simple counts of crossings cannot do.

### 实验/数据
We evaluate the method on dynamic network classification, using synthetic networks of online communities whose labels describe how the network evolved between the same starting and ending states. Our experimental results show that the proposed features reach 97.1% accuracy on four classes, against 44.5% for the best feature set that does not track eigenvalues, and that the Burau features also separate networks containing the same events in a different order, which simple counts of crossings cannot do. To the best of our knowledge, this is the first study that defines braids and braid monodromy on graph data and uses them as features for learning on dynamic networks.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
To the best of our knowledge, this is the first study that defines braids and braid monodromy on graph data and uses them as features for learning on dynamic networks.

### 23. TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information

- 作者：Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz, Yubin Kim, Taekyun Lee, Kaiqing Zhang, Asuman Ozdaglar｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37571v1

### 背景/问题
Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation.

### 方法
We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-making problems constructed from real-world legal, finance, medical, and software engineering corpora. TeamGym introduces a method to identify a minimal set of facts, each element of which is necessary and all of which are collectively sufficient for a correct final decision, which we call pivotal information. This enables TeamGym to both control the distribution of pivotal information and track how well agents identify and integrate pivotal information when making team decisions.

### 实验/数据
Across two policy-training experiments, we find that training improves final-decision quality and induces emergent coordination in participation, speaker selection, and communication, even though the reward evaluates only the final decision.

### 结果
Across two policy-training experiments, we find that training improves final-decision quality and induces emergent coordination in participation, speaker selection, and communication, even though the reward evaluates only the final decision.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Across two policy-training experiments, we find that training improves final-decision quality and induces emergent coordination in participation, speaker selection, and communication, even though the reward evaluates only the final decision.

### 24. ReferStream: Interactive Subject Injection for Streaming Video Generation

- 作者：Shuolin Xu, Guanyuan Li, Boyu Li, Kelu Yao, Xiaogang Xu, Hongchuan Yu, Shuicheng Yan, Xiaobin Hu｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37566v1

### 背景/问题
Injecting new subjects naturally during streaming video generation requires integrating newly supplied visual references into the existing video while preserving established subjects and the scene. Encoding references independently of the current scene provides little guidance for this integration, while keeping their features in persistent memory can interfere with established context.

### 方法
We propose ReferStream, a framework that requires no additional training and combines reference construction using the current scene with transient cache injection.

### 实验/数据
Experiments on ReferStream Bench show higher scores for text adherence, subject similarity, and count accuracy than the compared baselines, including offline methods given all references in advance.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Project page: https://xushuolin.github.io/ReferStream/.

### 25. Essential norms of fractional Volterra-type operators

- 作者：Álvaro Miguel Moreno｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37548v1

### 背景/问题
Given a radial doubling weight $μ$ on the unit disk $\mathbb{D}$ and $f(z)=\sum_{n=0}^\infty \hat{f}(n)z^n\in\mathcal{H}(\mathbb{D})$, the fractional derivative of $f$ induced by $μ$ is $$ D^μ(f)(z) = \sum_{n=0}^\infty \frac{\hat{f}(n)}{μ_{2n+1}}z^n, $$ where $μ_{2n+1}=\int_0^1 r^{2n+1}μ(r)\,dr$ are the odd moments of $μ$. The fractional integral of $f$ induced by $μ$ is $I^μ(f)(z)=\sum_{n=0}^\infty μ_{2n+1}\hat{f}(n)z^n$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Later, we study the same questions for $V_{μ,g}:H^p\to H^q$ and $V_{μ,g}:A^p_α\to A^q_α$, characterizing their boundedness and compactness and estimating their essential norms for all $0<p,q<\infty$.

### 26. Relative distality and incidence bounds in positive characteristic

- 作者：Mira Tartarotti｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37532v1

### 背景/问题
We prove Szemerédi-Trotter-type incidence bounds for algebraic relations in any field $F$ admitting a valuation with finite residue field. This includes $\mathbb F_q(t)$, $\mathbb F_q((t))$, and all finitely generated extensions of finite fields.

### 方法
As the central ingredient of the proof, we introduce the model-theoretic notion of distality relative to a definable set.

### 实验/数据
We prove Szemerédi-Trotter-type incidence bounds for algebraic relations in any field $F$ admitting a valuation with finite residue field. This includes $\mathbb F_q(t)$, $\mathbb F_q((t))$, and all finitely generated extensions of finite fields. We begin developing this notion and prove that the theory of algebraically closed valued fields is distal relative to the residue field.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
An application of a result of Chernikov, Peterzil, and Starchenko, based on work of Chernikov, Galvin, and Starchenko, yields our incidence bounds.

### 27. Electron-to-Muon Forward Annihilation at High Energy

- 作者：Maximilian Delto, Alexander A. Penin, Lorenzo Tancredi｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37531v1

### 背景/问题
We study the high-energy behavior of electron-to-muon annihilation in forward kinematics in QED with two massive lepton species. Using effective field theory renormalization group techniques we derive the all-order asymptotic behavior of the annihilation amplitude through the next-to-leading logarithmic approximation.

### 方法
未在摘要中明确给出。

### 实验/数据
Using effective field theory renormalization group techniques we derive the all-order asymptotic behavior of the annihilation amplitude through the next-to-leading logarithmic approximation.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The goal of this paper is to elaborate on various technical details that we omitted in the original presentation of our results in arXiv:2510.04914.

### 28. "Helium Enrichment Law": The Relation Between Helium and Metal Enrichment in Stars in FIRE-3 Simulations of Milky Way-mass Galaxies

- 作者：Pratik J. Gandhi, Earl P. Bellinger, Andrew Wetzel, Jeremy Bailin, Sarbani Basu, Isabella L. Trierweiler, Francisco J. Mercado｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37529v1

### 背景/问题
Helium abundance is a key input to stellar models that are used to infer accurate ages, masses, and compositions for individually resolved stars in the Milky Way (MW), underpinning Galactic archaeology. Since spectroscopically measuring He abundances is difficult, stellar models often assume a fixed "chemical enrichment law" dY/dZ (the slope linearly relating a star's helium mass fraction Y to its metal mass fraction Z).

### 方法
Helium abundance is a key input to stellar models that are used to infer accurate ages, masses, and compositions for individually resolved stars in the Milky Way (MW), underpinning Galactic archaeology. Since spectroscopically measuring He abundances is difficult, stellar models often assume a fixed "chemical enrichment law" dY/dZ (the slope linearly relating a star's helium mass fraction Y to its metal mass fraction Z).

### 实验/数据
Using the FIRE-3 cosmological baryonic zoom-in simulations, we investigate helium versus metal enrichment in the stars of MW-mass galaxies. Our simulations produce a range of dY/dZ slopes slopes with best-fit values of ~0.75-2.1 depending on the age of the stars considered at present day; on average consistent with the range of values from MW observations but with no single "universal" enrichment law. The dY/dZ slope also shows galaxy-to-galaxy variance in our simulations, and to leading order increases over cosmic time within the same galaxy, based on the peculiarities of the formation histories of each MW-mass system.

### 结果
If incorrect, this assumption can introduce significant systematics in inferring stellar properties. The dY/dZ slope also shows galaxy-to-galaxy variance in our simulations, and to leading order increases over cosmic time within the same galaxy, based on the peculiarities of the formation histories of each MW-mass system.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Despite choosing a fixed set of nucleosynthetic yields for stellar feedback processes in FIRE-3, we predict variance in dY/dZ for stars in MW-mass galaxies, and observations of MW stars must be interpreted in this context.

### 29. Extending the W3C Data Privacy Vocabulary to Cover the German Health Data Use Act - Lessons Learned

- 作者：Julian Flake, Christian Henke, Alessandra S. Kuntz, Matthias Löbe, Harshvardhan J. Pandit, Christian Draeger｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37527v1

### 背景/问题
Finding, sharing, and reusing data requires common interoperable vocabularies to adequately describe machine-actionable data policies. Semantic Web standards are a proven way to express such information describing data access and reuse.

### 方法
In this work, we present the creation of a DPV extension representing the German Health Data Use Act (Gesundheitsdatennutzungsgesetz (GDNG)) that has been set into force in March 2024.

### 实验/数据
Finding, sharing, and reusing data requires common interoperable vocabularies to adequately describe machine-actionable data policies. Semantic Web standards are a proven way to express such information describing data access and reuse. The Data Privacy Vocabulary (DPV) represents a community standard for privacy, data protection, and related topics.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
All extensions were released as draft extensions with the latest DPV version 2.3, released 25th of February 2026.

### 30. Fisher Completions and Statistical Regularization of Wrapped Gaussian Families

- 作者：Gunhee Cho, Hyun Chul Jang｜年份：2026｜发布时间：2026-10-27｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.37526v1

### 背景/问题
We determine the intrinsic Fisher completion of the full-covariance wrapped Gaussian family on a fixed torus and relate its geometry to uniform estimation. The completion is homeomorphic to the total-variation closure.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
A common-phase example illustrates how partially uniform limits can retain relative-phase information while remaining uniformly estimable.
