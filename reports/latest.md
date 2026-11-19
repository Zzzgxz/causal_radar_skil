# CausalRadar 日报 - 2026-11-19

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Statistical methods for extrapolation from one population to another: a review

- 作者：Lingjiao Wang, Francois Mercier, Astrid Jullion, Xuan Zhu, Christian Rover, Marc Vandemeulebroecke, Martin Posch, Sarah Zohar 等｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**8.50**
- 链接：https://arxiv.org/abs/2611.24850v1

> 命中：hit_abstract=['causal inference', 'treatment effect', 'CATE']

### 背景/问题
Background: Extrapolation refers to statistical approaches that support inference on treatment effects in a target population using data from completed clinical trials conducted in a source population. This is particularly important when only limited data are available in the target population.

### 方法
Background: Extrapolation refers to statistical approaches that support inference on treatment effects in a target population using data from completed clinical trials conducted in a source population. Methods: We conducted a review of statistical methodologies for extrapolation, focusing on approaches that incorporate outcome data from source populations to support inference in target populations. Results: The review identified 218 extrapolation approaches from 159 papers, which can be broadly classified into three main categories: Bayesian, frequentist, and causal inference methods.

### 实验/数据
Background: Extrapolation refers to statistical approaches that support inference on treatment effects in a target population using data from completed clinical trials conducted in a source population. This is particularly important when only limited data are available in the target population. Extrapolation may be based on multiple sources of information, including pharmacokinetic, pharmacodynamic, mechanistic, or clinical outcome data.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
It also discusses key considerations for method selection and current limitations, and highlights priorities for future research, including the development of new extrapolation methods and clinical trial designs that facilitate extrapolation.

### 2. DiWALI: Diffusion Policy Learning in World Models via Latent Action Inference from Human and Robot Play

- 作者：Akshay L Chandra, Iman Nematollahi, Lingyue Zhao, Daria Kulikova, Angela P. Schoellig, Fabien Despinoy, Abhinav Valada｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**6.50**
- 链接：https://arxiv.org/abs/2611.24836v1

> 命中：hit_title=['policy learning']

### 背景/问题
Learning robot manipulation is constrained by the availability of action-labeled robot data, for both imitation and world models. Humans can demonstrate skills in seconds, but their demonstrations lack the required robot actions.

### 方法
Learning robot manipulation is constrained by the availability of action-labeled robot data, for both imitation and world models. We introduce DiWALI, a framework that learns and improves diffusion policies within a world model trained on human and robot play. DiWALI infers latent actions from consecutive frames using an inverse dynamics model, enabling world model training without action labels, and grounds them in robot commands through a decoder trained separately on robot play.

### 实验/数据
Learning robot manipulation is constrained by the availability of action-labeled robot data, for both imitation and world models. Experiments on a physical robot show that skills learned primarily from human demonstrations are further improved in imagination with a world model trained on human and robot play. Together, these results demonstrate that human experience can support both manipulation skill acquisition and subsequent policy improvement, reducing reliance on action-labeled robot data.

### 结果
We introduce DiWALI, a framework that learns and improves diffusion policies within a world model trained on human and robot play. Skill policies are trained over latent actions from action-free human demonstrations and improved with reinforcement learning in imagination. On the CALVIN benchmark, DiWALI policies trained solely from human demonstrations substantially outperform baselines trained with robot demonstrations.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Videos, dataset and code are available at https://diwali.cs.uni-freiburg.de.

### 3. Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent Harnesses

- 作者：Jiahang Lin, Jiahao Chen, Yiding Wang, Shichun Liu, Chengjun Pan, Shihan Dou, Honglin Guo, Yuyang Hu 等｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.24924v1

> 命中：hit_scenario=['ads']

### 背景/问题
Real-world harness engineering is driven by explicit and implicit user requirements, which guide development and validation. However, existing harness evolution methods often overlook implicit requirements and interaction needs, while using a single evolution agent to modify the harness and benchmark scores to select changes.

### 方法
未在摘要中明确给出。

### 实验/数据
In a blind human A/B test, real users prefer AHE-Beta in 31 of 48 valid pairs and rate it higher on all five dimensions, matching the directional preference of the user simulator. The human A/B results show that AHE-Beta achieves its goal of aligning harness evolution with real-world user requirements.

### 结果
Without further evolution, the gains transfer to GLM-5.3 and DeepSeek-V4.1-Flash with pass@1 improvements of 15.8% and 5.3% over Base Harness.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Together, these results show that requirement-centered harness evolution is a more general method for improving agent capabilities.

### 4. Batch-Dynamic Coreness and Applications with Logarithmic Work via Balanced Pressures

- 作者：Quinten De Man, Laxman Dhulipala, Kishen N Gowda, Zhongqi Wang｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.24905v1

> 命中：hit_scenario=['ads']

### 背景/问题
We give a parallel algorithm that maintains a one-sided $(2+\varepsilon)$-approximation of all core numbers under batches of edge insertions and deletions. For fixed $\varepsilon>0$, the expected amortized work is $O(\log n)$ per edge update, and each batch has deterministic polylogarithmic depth.

### 方法
This approximation factor approaches the factor-two limit for polylogarithmic update and query time under the OMv conjecture.

### 实验/数据
未在摘要中明确给出。

### 结果
This improves on the previously known $(4+\varepsilon)$-approximation and $O(\log^2 n)$ amortized work bounds. Our construction also gives a $(1+\varepsilon)$-approximation of the densest-subgraph value with logarithmic expected amortized work and supports batch-dynamic maximal matching, clique counting, forest decomposition, and coloring in low-arboricity graphs with improved or matching work bounds. We give a practical implementation of our batch-dynamic coreness algorithm and find that it is able to achieve smaller empirical error than the state-of-the-art parallel batch-dynamic implementation, while running faster.

### 结论/启示（面向电商发券、定价、营销算法等应用）
On three graphs with up to 1.8 billion edges, it is $9.2\times$ faster than the heuristic baseline.

### 5. Asteroseismology of AI Velorum: a prototype of high-amplitude delta Scuti stars

- 作者：Przemysław Walczak, Jadwiga Daszyńska-Daszkiewicz, Wojciech Niewiadomski, Wojciech Szewczuk｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.24796v1

> 命中：hit_scenario=['ads']

### 背景/问题
AI Velorum is exceptional among high-amplitude δScuti (HADS) stars because of its multimode pulsations. Despite being an excellent target for asteroseismology, this prototype star has not been studied in detail.

### 方法
Seismic modelling was performed within a Bayesian framework supported by Monte Carlo simulations. We confirm the radial nature of the two dominant modes and identify one non-radial mode as most likely an axisymmetric dipole or quadrupole mode. Within the explored parameter space, only OPAL models reproduce the observed position of AI Vel in the HR diagram, whereas OP and OPLIB models are too cool and underluminous.

### 实验/数据
We determine the stellar parameters, age, and evolutionary stage of AI Vel, constrain envelope convection and convective core overshooting, and test three opacity data sets: OPAL, OP, and OPLIB. Seismic modelling was performed within a Bayesian framework supported by Monte Carlo simulations.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The preference for OPAL opacities is consistent with results for several other HADS and SX Phoenicis stars but does not imply a general superiority of OPAL opacities.

### 6. Locally infrared finite two-loop amplitudes for multi Higgs production in association with one jet

- 作者：Aniruddha Venkata｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.24916v1

> 命中：hit_abstract=['CATE']

### 背景/问题
We study the two-loop amplitudes for multi-Higgs production through a massive top-quark loop in association with one jet. We consider the quark-antiquark channel with a final-state gluon, $q\bar q\to g+nH$ although our construction applies to crossed channel as well.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We expect its extension to more complicated processes to eliminate all collinear singularities--particularly in the initial state.

### 7. Bar formation and secular evolution in live Milky Way-like galaxies

- 作者：Eva Durán-Camacho, Sioree Ansar, Paula D. López, Johan H. Knapen, Jesus Falcón-Barroso, Adriana de Lorenzo-Cáceres, Jairo Méndez-Abreu｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.24884v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Context. Bars and their boxy/peanut (B/P) shapes drive the secular evolution of disc galaxies, redistributing angular momentum and reshaping the radial and vertical structure of stellar discs.

### 方法
Only one model shows a clear buckling event; the rest form B/P bulges through smooth secular evolution.

### 实验/数据
We analyse fifteen isolated MW-like hydrodynamical simulations run with AREPO for 3 Gyr, spanning three stellar masses and five bulge fractions, with live stellar, bulge, and dark matter components.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We find a coherent evolutionary sequence linking bar growth, bar slowdown, and B/P assembly, whose timing is set by the initial disc structure rather than by its global kinematic settling.

### 8. On the Validity of Fisher Randomization Tests under the Weak Null

- 作者：Timothy Sudijono, Edgar Dobriban, Eric Tchetgen Tchetgen｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.24821v1

> 命中：hit_abstract=['treatment effect']

### 背景/问题
Consider the problem of testing the Neyman weak null of no sample average treatment effect $H_{0N}:τ= 0$ in randomized experiments with binary outcomes. Although the Fisher Randomization Test (FRT) is typically justified under Fisher's sharp null of no individual treatment effect, we show that it is finite-sample-valid for the weak null $H_{0N}$ in three common combinations of study design and test statistic: 1) balanced completely randomized experiments with the difference-in-means test statistic, 2) matched pairs experiments with the same test statistic, and 3) balanced Bernoulli randomized experiments with the centered Horvitz-Thompson test statistic.

### 方法
未在摘要中明确给出。

### 实验/数据
Consider the problem of testing the Neyman weak null of no sample average treatment effect $H_{0N}:τ= 0$ in randomized experiments with binary outcomes. Although the Fisher Randomization Test (FRT) is typically justified under Fisher's sharp null of no individual treatment effect, we show that it is finite-sample-valid for the weak null $H_{0N}$ in three common combinations of study design and test statistic: 1) balanced completely randomized experiments with the difference-in-means test statistic, 2) matched pairs experiments with the same test statistic, and 3) balanced Bernoulli randomized experiments with the centered Horvitz-Thompson test statistic. As an immediate corollary, Fisher's exact test in a balanced completely randomized experiment is valid under the weak null, and so is McNemar's test in a matched pairs experiment.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In simulation experiments, the FRTs compare favorably to other exact procedures.

### 9. LEMUR: A Searchable Web Archive of Deep Chandra Images of Galaxies and Galaxy Clusters

- 作者：Carter L. Rhea, Julie Hlavacek-Larrondo, Marine Prunier, Hyunseop Choi, Megan Donahue, Christian Thibeault｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24937v1

### 背景/问题
We present LEMUR, a publicly accessible archive of uniformly reduced, deep Chandra images of 2,569 galaxies and galaxy clusters (including groups), comprising 5,505 ACIS observations and 138.8 Ms of exposure. By combining the publicly available imaging observations of each target, we provide background-subtracted, exposure-corrected images in broad, soft, and hard bands at the native ACIS pixel scale of 0.492 arcsec.

### 方法
We present LEMUR, a publicly accessible archive of uniformly reduced, deep Chandra images of 2,569 galaxies and galaxy clusters (including groups), comprising 5,505 ACIS observations and 138.8 Ms of exposure. For every object, we measure an X-ray center at the peak of its diffuse emission, and we provide a morphological similarity search based on embeddings from the AstroCLIP foundation model, in which nearest neighbors share cool-core status in 73% of matched cluster pairs, compared with 51% by chance. The images, along with their counts images, background models, exposure maps, and quick-look stamps, are available through a searchable web archive at https://lemur-archive.lemur-xray.workers.dev/.

### 实验/数据
Our primary goal is to make the wealth of archival Chandra observations accessible to researchers without requiring specialized expertise in X-ray data reduction.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The catalog tables are archived on Zenodo (doi:10.5281/zenodo.24351915), and all code is open source at https://github.com/crhea93/Lemur.

### 10. Jailbreak Detection on Large Language Models via Contrastive Prototype Structures

- 作者：Yan Qiu, Yuanyuan Li｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24936v1

### 背景/问题
Jailbreak attempts and harmful prompts remain a challenge for the safe deployment of large language models. We study whether contrastively learned representations can support safety detection without training an additional downstream classifier.

### 方法
Jailbreak attempts and harmful prompts remain a challenge for the safe deployment of large language models. We propose Jailbreak Detection with Prototype Inference (JDPI), which uses binary safety labels to construct harmful and benign prototypes and makes predictions from relative prototype distances.

### 实验/数据
With dataset-specific adaptation, JDPI exceeds the released Llama Guard 3-8B baseline by 0.173-0.310 in ROC-AUC across the four benchmarks. Across 12 directed transfers, JDPI outperforms the classifier by an average of 1.59 percentage points in accuracy, demonstrating stronger cross-dataset robustness.

### 结果
Across four benchmarks covering different input formats, contrastive fine-tuning improves JDPI's detection accuracy by 9.1-18.0 percentage points. Across 12 directed transfers, JDPI outperforms the classifier by an average of 1.59 percentage points in accuracy, demonstrating stronger cross-dataset robustness.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Across 12 directed transfers, JDPI outperforms the classifier by an average of 1.59 percentage points in accuracy, demonstrating stronger cross-dataset robustness.

### 11. Low Moments, Small Balls and Star Discrepancy

- 作者：Nicola Wengiel｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24934v1

### 背景/问题
Let $D_P$ be the discrepancy function of a configuration $P$ of $N$ points in the $d$-dimensional unit cube, and let $\|D_P\|_q$ be its $L^q$ discrepancy. We prove that for all fixed $d\ge2$ and $0<q\le1$ the $L^q$ discrepancy of every configuration of $N\ge2$ points is at least $c_{d,q}(\log N)^{(d-1)/2}$ with a constant $c_{d,q}>0$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we construct $N$-point sets whose $L^\infty$ discrepancy is $O_d((\log N)^{d-1-1/16})$ in every fixed dimension $d\ge3$; this disproves the conjectured optimality of the order $(\log N)^{d-1}$ of the classical constructions.

### 12. Render the Robot, Generate the World: One Video World Model Across Embodiments

- 作者：Yash Jangir, Karan Mirakhor, Renos Zabounidis, Muhammad Zubair Irshad, Sergey Zakharov, Yonatan Bisk, Homanga Bharadhwaj｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24925v1

### 背景/问题
Predicting the consequences of an agent's actions requires modeling both the body's motion and the environment's response. Most video world models attempt to learn both from numerical actions, even though geometry and kinematics already specify the intended motion.

### 方法
Predicting the consequences of an agent's actions requires modeling both the body's motion and the environment's response. Most video world models attempt to learn both from numerical actions, even though geometry and kinematics already specify the intended motion. We introduce Doppel, an embodiment-agnostic video world model conditioned on camera-aligned renderings of future body configurations and numerical action trajectories.

### 实验/数据
To train on robot datasets without camera extrinsics, we recover camera poses and align rendered trajectories with recorded observations. We jointly train a single shared video backbone and conditioning adapter on eight datasets spanning eight robot and human embodiments, from single- and bimanual robot arms to a dexterous humanoid and human hands and bodies, using about 600 hours of video without embodiment labels. Across three robot-arm datasets, Doppel improves PSNR over action-only baselines by 1.00 dB on held-out trajectories and 1.20 dB under out-of-distribution evaluation, while predicting more consistent object motion.

### 结果
Across three robot-arm datasets, Doppel improves PSNR over action-only baselines by 1.00 dB on held-out trajectories and 1.20 dB under out-of-distribution evaluation, while predicting more consistent object motion. Training on all eight embodiments (Doppel-8) improves robot predictions over the three-robot model (Doppel-3) on four of six evaluation sets.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Project page: https://doppelwm.github.io/.

### 13. Unified Law for Visual Tasks (The Four Laws of Computer Vision)

- 作者：Sen Fang, Yalin Feng, Yancheng Zhang, Yanxin Zhang, Zonglin Lyu, Hongbin Zhong, Liwei Che, Rui Wu 等｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24917v1

### 背景/问题
In this paper, we propose a Unified Law for Visual Tasks, which could be further divided into Four Laws of Computer Vision, with the goal of enabling a single framework or method to uniformly train on and perform nearly all visual tasks. Our starting point is an inspiration and hypothesis: if the world information is encoded into image, which we call World Snapshots, then image processing is world processing, and image generation is World Snapshot generation.

### 方法
In this paper, we propose a Unified Law for Visual Tasks, which could be further divided into Four Laws of Computer Vision, with the goal of enabling a single framework or method to uniformly train on and perform nearly all visual tasks. Furthermore, if all visual and visualization tasks can be reformulated as generation tasks, then a unified method, World Snapshot Models (WSMs), can perform the vast majority of visual tasks, much as large language models have largely unified natural language processing. This paper validates these laws across more than 1,000 trained and evaluated visual tasks (defined by distinct input-output mappings) and presents a unified training framework for future visual-task research and applications.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
This paper validates these laws across more than 1,000 trained and evaluated visual tasks (defined by distinct input-output mappings) and presents a unified training framework for future visual-task research and applications.

### 14. PrismRestore: A Compact Restoration Toolbox for Agentic Image Restoration

- 作者：Zhaocheng Yu, Kui Jiang, Jing Cao, Yiang Chen, Xiaocheng Feng, Junjun Jiang, Xianming Liu｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24915v1

### 背景/问题
Agentic image restoration composes operations to handle mixed degradations, yet its toolbox often requires storing multiple restoration networks. We propose PrismRestore, which constructs a compact bank of callable restoration actions from a single frozen all-in-one model.

### 方法
We propose PrismRestore, which constructs a compact bank of callable restoration actions from a single frozen all-in-one model. Our approach builds on task-dependent yet overlapping channel responses in the shared model. Experiments on synthetic composite-degradation and real-world multi-task benchmarks show improvements over the evaluated all-in-one baselines and restoration quality competitive with multi-model agents.

### 实验/数据
An offline task-prior search uses activation and gradient statistics to group channels with similar response profiles, then searches task-specific modulation coefficients over non-representative channels while leaving representative channels unmodulated. Experiments on synthetic composite-degradation and real-world multi-task benchmarks show improvements over the evaluated all-in-one baselines and restoration quality competitive with multi-model agents.

### 结果
Experiments on synthetic composite-degradation and real-world multi-task benchmarks show improvements over the evaluated all-in-one baselines and restoration quality competitive with multi-model agents.

### 结论/启示（面向电商发券、定价、营销算法等应用）
PrismRestore achieves these results with a single restoration backbone and faster inference than the evaluated agentic baselines.

### 15. Infinite cascades for the defocusing cubic nonlinear Schrödinger equation on the square torus

- 作者：Xi Chen｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24906v1

### 背景/问题
For each $1<s<2$ we construct a solution of the defocusing cubic nonlinear Schrödinger equation on the square two-torus with initial data in $H^s$ whose $H^s$ norm tends to infinity as $t\to+\infty$. The growth can be arbitrarily slow.

### 方法
未在摘要中明确给出。

### 实验/数据
For each $1<s<2$ we construct a solution of the defocusing cubic nonlinear Schrödinger equation on the square two-torus with initial data in $H^s$ whose $H^s$ norm tends to infinity as $t\to+\infty$.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Control on an entire half-line allows successive transfers to retain the coefficients produced earlier.

### 16. Beyond hidden zeros and uniqueness in Tr$(φ^3)$: Block and rod zeros in any Tr$(φ^m)$

- 作者：Laurentiu Rodina｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24897v1

### 背景/问题
Hidden zeros have proven powerful tools for reconstructing amplitudes in Tr$(φ^3)$, a theory of colored scalars with cubic interactions. We show that these structures extend to any Tr$(φ^m)$ theory.

### 方法
未在摘要中明确给出。

### 实验/数据
For every $m\geq4$, including even $m$, we describe a second family of nonlinear \emph{rod zeros} through a rod packing problem.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also conjecture that the block zeros enforce both locality and unitarity for any Tr$(φ^m)$ theory with odd $m$.

### 17. Efficient search for microlensed gravitational-wave signals with matched filtering and a two-image statistic

- 作者：Soumen Roy, Justin Janquart｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24895v1

### 背景/问题
Gravitational waves from compact binary coalescences can be microlensed by compact objects along the line of sight, producing frequency-dependent waveform distortions. As standard matched-filter searches rely on unlensed templates without accounting for lensing effects, microlensed signals can lose signal-to-noise ratio (SNR) through template mismatch and suffer further losses from signal-consistency tests.

### 方法
Therefore, the work proposed here lays the foundation for an effective search and identification of microlensed signals in gravitational-wave data.

### 实验/数据
We quantify both effects for the $\texttt{PyCBC}$ search using microlensed injections in simulated data. Therefore, the work proposed here lays the foundation for an effective search and identification of microlensed signals in gravitational-wave data.

### 结果
At a false-alarm rate of one per day, the relative detection volume improves by about $6\%$ across all injections, and by a factor of $1.9$ for the $10\%$ of injections most affected by lensing. In addition to increased detection capacities, we also show how the detection statistic can be used to establish the lensed nature of the trigger.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Therefore, the work proposed here lays the foundation for an effective search and identification of microlensed signals in gravitational-wave data.

### 18. On Evaluating User Simulators for Interactive Agents

- 作者：Hengguang Zhou, I-Hung Hsu, Li Chen, Priyanshi Shrivastava, Anastasios Angelopoulos, Wei-Lin Chiang, Ion Stoica, Cho-Jui Hsieh｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24892v1

### 背景/问题
User simulators offer a scalable way to evaluate interactive agents, but how to assess their quality remains underexplored. In particular, it is unclear whether existing user simulator evaluation frameworks reliably detect meaningful failures in simulated user behavior.

### 方法
In particular, it is unclear whether existing user simulator evaluation frameworks reliably detect meaningful failures in simulated user behavior. Motivated by these gaps, we propose a new evaluation suite that combines utility of user simulators for evaluating agents and two measures of fidelity to real users: population-level fidelity assesses collective interaction patterns, while trace-level fidelity assesses the preservation of individual users' goals, constraints, and persona.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Evaluating six user simulators on 351 real multi-turn sessions in which 348 distinct users across 23 languages and agents work together to create and refine artifacts such as full-stack web apps, games, design assets, and automated workflows, we find that population-level measures can miss when a simulated user pursues the wrong goal, ignores a constraint, or behaves out of character, highlighting the need to assess fidelity at comprehensive granularities.

### 19. Improved Asymptotic Approximation Guarantees for Continuous-Review Lost-Sales and Dual-Sourcing Inventory Models

- 作者：Weitian Tong, Yao Xu｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24889v1

### 背景/问题
We study continuous-review inventory models with unit Poisson demand and deterministic lead times: single sourcing with lost sales and dual sourcing with backlogging. Xin [Operations Research.

### 方法
We study continuous-review inventory models with unit Poisson demand and deterministic lead times: single sourcing with lost sales and dual sourcing with backlogging. 70(1):111--128 (2022)] establishes an asymptotic approximation factor of 1.79 for each model in its proportional-growth regime.

### 实验/数据
未在摘要中明确给出。

### 结果
Under the same assumptions, we obtain a factor of 1.248977 for the better of base-stock and constant-order policies for lost sales and a factor of 1.599528 for the better of dual-index and tailored base-surge policies for dual sourcing. For sufficiently large fixed backorder penalties, the dual-sourcing factor improves to 1.248977. The improvements follow from stronger lower bounds on the optimal cost.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We retain intermediate constraints on mean inventory for lost sales and use events determined only by future demand to bound backlog costs for dual sourcing.

### 20. Monoculture Robust Learning

- 作者：Lee Cohen, Jon Kleinberg, Omer Reingold｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24881v1

### 背景/问题
We introduce a notion of monoculture robustness in Probably Approximately Correct (PAC) learning, as a way to mitigate the problem of algorithmic monoculture (Kleinberg and Raghavan, 2021): the tendency of models sharing the same components (e.g., training data) to fail on the same inputs. Specifically, we ask whether a learner with access to a single dataset can output $k$ individually accurate hypotheses whose joint failure probability is comparable to training on $k$ independent datasets.

### 方法
We introduce a notion of monoculture robustness in Probably Approximately Correct (PAC) learning, as a way to mitigate the problem of algorithmic monoculture (Kleinberg and Raghavan, 2021): the tendency of models sharing the same components (e.g., training data) to fail on the same inputs.

### 实验/数据
We introduce a notion of monoculture robustness in Probably Approximately Correct (PAC) learning, as a way to mitigate the problem of algorithmic monoculture (Kleinberg and Raghavan, 2021): the tendency of models sharing the same components (e.g., training data) to fail on the same inputs. Specifically, we ask whether a learner with access to a single dataset can output $k$ individually accurate hypotheses whose joint failure probability is comparable to training on $k$ independent datasets.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We complement these positive results with a lower bound: for individual monoculture robustness, we prove a worst-case lower bound showing that, for learners, driving the individual conjunctive error down to $γ$ can require a sample-size multiplier of $t = Ω(\log(1/γ))$.

### 21. Auditing black-box clinical prediction models with a large language model through queries alone: a blinded test with planted flaws

- 作者：Zhiyu Liu, Xinyu Yang｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24877v1

### 背景/问题
Large language models (LLMs) are used to explain clinical prediction models, on the promise that they can say what a model computes, find its faults and even reveal new knowledge in it. We tested the three promises where the answers could be checked.

### 方法
Large language models (LLMs) are used to explain clinical prediction models, on the promise that they can say what a model computes, find its faults and even reveal new knowledge in it. From the International Stroke Trial we trained four kinds of model (logistic regression, explainable boosting machine, gradient-boosted trees, neural network) for two outcomes on patients randomised earlier, planted one flaw in each of 24 copies (an under-predicted subgroup, a reversed risk factor or an implausible step) and mixed them with the 8 clean models. GPT-6 Astra audited each model three times, blind, through a tool that only returned the model's predictions; the judging rules were committed before any run and applied by program.

### 实验/数据
Of 601 unexpected relationships it read out of the clean models, 11% held in patients randomised later (random pairs 6%; a regression scan's shorter list of its strongest candidates, 28%); after a check on the training data, 33% against 30%. With query access alone, an LLM can describe a black-box model faithfully and find nearly every planted flaw, as a purpose-written script also did; its reports of problems must be checked on the model and its discoveries on data.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
With query access alone, an LLM can describe a black-box model faithfully and find nearly every planted flaw, as a purpose-written script also did; its reports of problems must be checked on the model and its discoveries on data.

### 22. Kinetic study of Reaction-Control-Jet Interference in Rarefied Hypersonic Crossflow

- 作者：Alexis Theofilis, Martin Grabe｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24870v1

### 背景/问题
A 1975 wind-tunnel study at the German Aerospace Center (DLR) of a helium jet blowing from a flat plate into a Mach 11 to 12 air crossflow at three freestream densities is revisited using two- and three-dimensional Direct Simulation Monte Carlo (DSMC) computations at Knudsen numbers 0.021 to 0.125. The planar slot used in two-dimensional model computations reproduces the shock topology, the sign and two-lobed structure of the interference pressure and its trend with rarefaction, and its plate-alone boundary layer is consistent with the three-dimensional one and with a similarity solution with slip and temperature jump.

### 方法
The planar slot used in two-dimensional model computations reproduces the shock topology, the sign and two-lobed structure of the interference pressure and its trend with rarefaction, and its plate-alone boundary layer is consistent with the three-dimensional one and with a similarity solution with slip and temperature jump.

### 实验/数据
A 1975 wind-tunnel study at the German Aerospace Center (DLR) of a helium jet blowing from a flat plate into a Mach 11 to 12 air crossflow at three freestream densities is revisited using two- and three-dimensional Direct Simulation Monte Carlo (DSMC) computations at Knudsen numbers 0.021 to 0.125. However, two-dimensional simulations overpredict the peak interference pressure about twelvefold at every condition and carry it farther upstream. Three-dimensional DSMC reproduces the measured interference pressure at all three densities, within 25% at the lobe peak and 3 mm in its position, although two- and three-dimensional simulations overpredict the plate-alone wall pressure by 50 to 75%.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Fully three-dimensional kinetic simulations are underway to extend the present validation to a comparison of jet strength and forces over wider Knudsen number ranges, and to an examination of lateral relief as a reason for the discrepancy.

### 23. The Ceresa Cycle on $X_0^+(p)$

- 作者：Jonathan Grube｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24868v1

### 背景/问题
We consider the curve $X_0^+(p)$ with prime $p$, which is the quotient of the modular curve $X_0(p)$ by the Fricke involution. We describe how one can explicitly calculate the shadow of a Hecke operator on $X_0^+(p)$, which is a rational divisor on $X_0^+(p)$ whose nonvanishing is an obstruction to the Ceresa cycle of $X_0^+(p)$ being torsion in the Chow group of the Jacobian of $X_0^+(p)$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also provide an implementation of this procedure in PARI/GP and SageMath and use this on all primes below 5000.

### 24. Topological Properties of Cones with Small Entropy

- 作者：Lam Doan｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24863v1

### 背景/问题
We show that regular hypercones in $\mathbb{R}^{n+1}$ with small entropy have simple topology. As a result, the link of the given cone is topologically an $(n-1)-$sphere.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Moreover, the space of all links whose associated cones have entropy close to 1 can be retracted onto the space of equatorial spheres, which is homeomorphic to $\mathbb{RP}^n$.

### 25. Communications-free Collective Intelligence Via Allocentric Belief

- 作者：Cameron Mehlman, Arjun Mulchandani, Hovik Grigoryan, Anurag Koyyada, Gregory Falco｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24858v1

### 背景/问题
A team of skilled card players share no information amongst each other, and yet still are able to coordinate their play by watching the same players and reading the same tells. Autonomous systems have failed to exploit this logic, relying instead on explicit communication or complex state estimation schemes that can fail when it matters most.

### 方法
Across five competitive environments allocentric belief alignment outperforms egocentric approaches in collective performance, and even scales to sixty-agent teams where standard methods fail.

### 实验/数据
未在摘要中明确给出。

### 结果
Across five competitive environments allocentric belief alignment outperforms egocentric approaches in collective performance, and even scales to sixty-agent teams where standard methods fail.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results establish a new principle for collective intelligence: in the absence of communication, a shared gaze replaces a shared channel.

### 26. Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling

- 作者：Eugene Agichtein, Charles L. A. Clarke, Kaustubh Dhole, William Stern｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24849v1

### 背景/问题
Large language model (LLM) judges have become a common way to create large-scale relevance judgments for retrieval evaluation. However, each judgment requires a potentially expensive call to a frontier model, and the judgments are hard to interpret and may not be reproducible.

### 方法
Large language model (LLM) judges have become a common way to create large-scale relevance judgments for retrieval evaluation. However, each judgment requires a potentially expensive call to a frontier model, and the judgments are hard to interpret and may not be reproducible. To address these issues, we propose ExecJudges, a method for generating fast, inspectable and scalable judges for automatic relevance labeling.

### 实验/数据
未在摘要中明确给出。

### 结果
Our results suggest that ExecJudges offers a reproducible, inspectable, efficient and cost-effective alternative to LLM judges for labeling deep result pools for system evaluation or ranking improvements.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our results suggest that ExecJudges offers a reproducible, inspectable, efficient and cost-effective alternative to LLM judges for labeling deep result pools for system evaluation or ranking improvements.

### 27. Old Matches, New Frames: Schedule-Gated Stereo Memory from Human Vision to Machine Matching

- 作者：Ruiqi Liu, Yang Lu, Yanlan Kang｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24848v1

### 背景/问题
Human vision and video stereo networks both reuse disparity evidence across time, yet a refresh of the input can invalidate a match formed milliseconds earlier. What tells a system whether an old match still counts?

### 方法
Second, four propositions establish what such data can identify: gating is identified at the level of the refresh schedule, and candidate binding is invisible to standard stimuli but exposed by a single-eye geometry flip that separates the readouts by up to 7.1%.

### 实验/数据
We answer this from limited human data in three steps. Second, four propositions establish what such data can identify: gating is identified at the level of the refresh schedule, and candidate binding is invisible to standard stimuli but exposed by a single-eye geometry flip that separates the readouts by up to 7.1%. Third, the identified rule becomes a two-field stereo memory that separates sample validity from hypothesis support.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
It removes a 50 ms recovery lag after geometry flips, and its regime analysis explains why plain integration stays preferable on MPI-Sintel, where 71.1% of pixels change appearance but not disparity.

### 28. Vibe-Trading: Towards Agent-Native Trading

- 作者：Haozhe Wu, Zhonghang Li, Chao Huang｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24845v1

### 背景/问题
Existing AI agents can retrieve information, call tools, run experiments, and produce multi-step outputs. Yet most are built around relatively static workflows and struggle to preserve reliable state as the environment changes.

### 方法
We present Vibe-Trading, a comprehensive agent-native trading framework and all-in-one workspace for building, evaluating, and evolving agents for financial trading.

### 实验/数据
Existing AI agents can retrieve information, call tools, run experiments, and produce multi-step outputs. A result is useful only when it remains tied to the correct time, data snapshot, and execution context. It unifies market research, financial data, strategy generation, backtesting, portfolio analysis, paper trading, multi-agent collaboration, and optional broker execution.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Together, these designs provide a practical foundation for trading agents whose results can be traced, reproduced, and acted on only under explicit authority.

### 29. Consistent interfacial flow numerics - Part I: The gravity force term

- 作者：Johan Roenby, Konstantinos Missios, Kasper Møller, Sithik Aliyar, Henning Scheufler｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24841v1

### 背景/问题
The OpenFOAM solver interFoam for incompressible two-phase flows combines the single-phase PISO/PIMPLE algorithm for the pressure-velocity coupling with an interface advection step. It relies on the standard finite volume discretisation of the momentum equation, which assumes smooth fields, but across a water-air interface the density jumps by a factor of about 1000.

### 方法
We implement this geometric gravity model in a new solver, interIsoGoam.

### 实验/数据
It relies on the standard finite volume discretisation of the momentum equation, which assumes smooth fields, but across a water-air interface the density jumps by a factor of about 1000.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In Part II we trace this error to the implicit discretisation of the momentum convection term.

### 30. Kaer: Security-Aware Replanning for Multi-Agent Systems

- 作者：Tushin Mallick, Evan Rose, Matthew Laws, Alina Oprea, Cristina Nita-Rotaru｜年份：2026｜发布时间：2026-11-18｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.24839v1

### 背景/问题
One popular architecture for multi-agent systems (MAS) relies on an orchestrator that generates an initial plan, coordinates its execution, and dynamically revises the plan based on agent feedback when tasks cannot be fully specified in advance. This dynamic replanning introduces a critical vulnerability: malicious agents can embed instructions within their feedback to hijack the replanning process.

### 方法
We introduce Kaer, a multi-agent framework featuring security-aware replanning.

### 实验/数据
未在摘要中明确给出。

### 结果
Evaluating Kaer on Cintra against Magentic-One (an undefended MAS) and ControlValve (the state-of-the-art defense) demonstrates that Kaer achieves higher robustness than both systems while maintaining comparable utility to ControlValve.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Although abstract failure templates slightly constrain utility on select tasks, Kaer enables MAS to perform secure, dynamic plan revisions without exposing the orchestrator to untrusted agent feedback.
