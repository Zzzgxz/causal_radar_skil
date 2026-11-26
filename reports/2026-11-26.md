# CausalRadar 日报 - 2026-11-26

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Shape-Aware Three-Way Merge for RDF Knowledge Graphs: The schema defines the conflict: an implementation and evaluation

- 作者：Steve Brown｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**7.00**
- 链接：https://arxiv.org/abs/2611.34870v1

> 命中：hit_scenario=['ads']；hit_abstract=['CATE']

### 背景/问题
Merging RDF serializations creates ordering conflicts and misses semantic ones. We describe and evaluate a three-way merge in which the schema defines a conflict: set algebra combines canonical triples, and a slot is contended only where a SHACL shape bounds its cardinality and both sides' changes cannot stand within that bound.

### 方法
未在摘要中明确给出。

### 实验/数据
In a study of evolving shape contracts, merging shape declarations first handles the tested cardinality changes, while datatype evolution exposes a detector blind spot caught by post-merge validation. Under wrong shapes, a missing bound loses data silently and a spurious one only adds questions.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The supported claim is fewer human decisions with nothing silently lost, for cardinality conflicts in one deployment, not general merge correctness.

### 2. Mixture-of-Loops Transformer

- 作者：Lianghui Zhu, Shijie Wang, Xinggang Wang, Jinze Bai, Bo Wang, Xiang Bai｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.34923v1

> 命中：hit_scenario=['ads']

### 背景/问题
Looped Transformers boost expressivity by reusing shared layers across loops, yet at the cost of efficiency. Pushing their expressivity-efficiency frontier requires rethinking the core mechanism connecting adjacent loops: What should be passed as a Transformer loops?

### 方法
In 400B-token pretraining, U-MoLT outperforms OLMo3 across 700M/1.5B dense and 3B MoE models, achieving 1.7x validation cross-entropy (CE) token efficiency at 700M while improving 3B MoE 10-domain perplexity by 0.75 and 10-task accuracy by 2.1 percentage points. 1,000.6 ms on S-size (~113M) models.

### 实验/数据
未在摘要中明确给出。

### 结果
In 400B-token pretraining, U-MoLT outperforms OLMo3 across 700M/1.5B dense and 3B MoE models, achieving 1.7x validation cross-entropy (CE) token efficiency at 700M while improving 3B MoE 10-domain perplexity by 0.75 and 10-task accuracy by 2.1 percentage points.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Code is available at https://github.com/hustvl/MoLT

### 3. Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs

- 作者：Agelos Kratimenos, Kostas Daniilidis, Evangelos Chatzipantazis｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.34914v1

> 命中：hit_scenario=['ads']

### 背景/问题
Vision-language-action models (VLAs) are capable low-level controllers, but they tie where objects go to the layouts they were trained on: when objects are moved or obstacles block the way, they carry them to the wrong place or into collisions. Fine-tuning on new layouts needs robot data for each one and erodes skills the model already has.

### 方法
Vision-language-action models (VLAs) are capable low-level controllers, but they tie where objects go to the layouts they were trained on: when objects are moved or obstacles block the way, they carry them to the wrong place or into collisions. Fine-tuning on new layouts needs robot data for each one and erodes skills the model already has. All code, models and data will be made public.

### 实验/数据
Fine-tuning on new layouts needs robot data for each one and erodes skills the model already has. On a real Franka, with a prior trained purely in simulation, it guides the frozen DROID π0.5 around an obstacle and to a placement at the limit of the arm's reach, where it otherwise fails. All code, models and data will be made public.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
All code, models and data will be made public.

### 4. The oxygen cold trap in protoplanetary discs

- 作者：Peter Woitke｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.34867v1

> 命中：hit_scenario=['ads']

### 背景/问题
The diffusive transport of oxygen in protoplanetary discs followed by sequestration into ice in the midplane, a process known as the cold trap, can substantially alter the chemical environment where planets form. This paper presents a new time-dependent modelling framework that allows us to consistently simulate kinetic gas-phase chemistry, ice growth and desorption, turbulent diffusive mixing, and gravitational settling of icy particles with a changing particle size distribution over million-year timescales in one-dimensional vertical columns.

### 方法
This paper presents a new time-dependent modelling framework that allows us to consistently simulate kinetic gas-phase chemistry, ice growth and desorption, turbulent diffusive mixing, and gravitational settling of icy particles with a changing particle size distribution over million-year timescales in one-dimensional vertical columns. Applying our model to a T Tauri disc across radii from 1 to 100 au reveals that vertical cold trapping becomes an effective mechanism once the diffusion-to-settling timescale ratio exceeds unity, simultaneously driving the gas-phase C/O up toward unity, and the gas-phase C/H down, by up to two orders of magnitude at large distances. All models feature the development of an upward counter-flux due to the turbulent up-whirling of icy particles followed by ice sublimation above the horizontal icelines, which brings the cold trapping to a halt and eventually establishes a relaxed vertical structure after about $10^4$ to $10^6$ yr, depending on the radial distance.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
However, in none of our models does the C/O ratio exceed unity, which is a consequence of CO-blocking, a chemical process where water molecules naturally stop forming once C/O approaches unity.

### 5. Lattice gauge theory computation of $1/m_Q$ and $1/m_Q^2$ corrections to the quarkonium potential

- 作者：Michael Eichberg, Marc Wagner｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.34836v1

> 命中：hit_scenario=['ads']

### 背景/问题
We compute the static quark-antiquark potential and its $1/m_Q$ and $1/m_Q^2$ corrections, i.e.\ the $1/m_Q$ potential and all $1/m_Q^2$ potentials, which can be expressed in terms of correlators of two field strength insertions, in SU(3) lattice gauge theory and provide parameterizations for quark-antiquark separations $0.2 \, \text{fm} \lesssim r \lesssim 0.7 \, \text{fm}$. The field strength insertions in generalized Wilson loops are renormalized using gradient flow, which also leads to small statistical uncertainties.

### 方法
未在摘要中明确给出。

### 实验/数据
We compute the static quark-antiquark potential and its $1/m_Q$ and $1/m_Q^2$ corrections, i.e.\ the $1/m_Q$ potential and all $1/m_Q^2$ potentials, which can be expressed in terms of correlators of two field strength insertions, in SU(3) lattice gauge theory and provide parameterizations for quark-antiquark separations $0.2 \, \text{fm} \lesssim r \lesssim 0.7 \, \text{fm}$. The field strength insertions in generalized Wilson loops are renormalized using gradient flow, which also leads to small statistical uncertainties. They can easily be converted to specific heavy quark masses, e.g.\ for Born-Oppenheimer effective field theory studies of quarkonium.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
They can easily be converted to specific heavy quark masses, e.g.\ for Born-Oppenheimer effective field theory studies of quarkonium.

### 6. HOG-WAM: Improving Visual Robustness through Future Gradient Prediction

- 作者：Boxuan Dong, Yupeng Qian, Ying Wu, Heshuai Li, Junhao Tan, Zhenxiong Tan, Weijia Wu, Weihao Yu｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.34811v1

> 命中：hit_scenario=['ads']

### 背景/问题
World-action models jointly predict future observations and actions, yet visual corruption can disrupt the resulting policies. We introduce HOG-WAM, which adds future Histograms of Oriented Gradients (HOG) as structural supervision derived directly from demonstration images.

### 方法
World-action models jointly predict future observations and actions, yet visual corruption can disrupt the resulting policies.

### 实验/数据
These findings support future-gradient prediction as complementary supervision for visually robust control, with larger absolute gains on physical tasks than in simulation.

### 结果
Mixed-noise success increases from 78.86% to 82.86% relative to FastWAM, with comparable performance on clean scenes. On LIBERO Plus, overall success increases from 74.49% to 75.26%, with the largest gain under sensor noise, from 74.14% to 78.89%. Across four Franka tasks, average success increases from 40% to 59% under clean observations and from 17% to 24% under noisy observations.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Code is available at https://github.com/iPPLab/HOG-WAM.

### 7. Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video Models

- 作者：Dezhi Luo, Fengyuan Yu, Haotian Zhang, Zehong Zhao, Ran Ji, Siyuan An, Huayi Qin, Qingying Gao 等｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.34813v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Video generation models are increasingly evaluated as visual reasoners: given a first frame and a natural-language prompt, can the model produce the video in which the specified task is carried out? The paradigm is considered advantageous because the reasoning is native to the visual medium, unfolding directly in the frames rather than through language or code.

### 方法
Video generation models are increasingly evaluated as visual reasoners: given a first frame and a natural-language prompt, can the model produce the video in which the specified task is carried out? On VBVR-Pro-Bench (Xu et al., 2026), a 500-instance suite spanning five cognitive categories with symbolic ground truth, the agent receives the same first frame and prompt as the video model, with no access to ground truth, metadata or generation models, and one attempt per instance. Three closed-model agents (Codex with gpt-6-astra, Claude Code with Fable 5.1 and Gemini CLI with Gemini 3.1 Pro) score 0.923, 0.894 and 0.893, each more than 0.22 above the strongest video model.

### 实验/数据
On VBVR-Pro-Bench (Xu et al., 2026), a 500-instance suite spanning five cognitive categories with symbolic ground truth, the agent receives the same first frame and prompt as the video model, with no access to ground truth, metadata or generation models, and one attempt per instance.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We further distinguish depictive programs, which navigate the image to recover a transferable scheme, from propositional programs, which operate on hard-coded values, revealing how visual reasoning unfolds in agent-written programs and what it implies for its nature of reasoning in general.

### 8. The THESAN-ZOOM project: interpreting candidate Population III-enriched absorption line systems during reionization

- 作者：Giulia Pruto, Laura Keating, Rahul Kannan, Ewald Puchwein, Aaron Smith, Enrico Garaldi, Mark Vogelsberger, William McClymont 等｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.34789v1

> 命中：hit_abstract=['CATE']

### 背景/问题
With JWST, metal absorption lines are now being detected at increasingly high redshift, where signatures of the first generation of stars (Population III) may be observable. Interpreting observations of possible Pop III-enriched gas is challenging, as metals released by stars inevitably mix with pristine gas accreting onto galaxies and recycled gas from different episodes of star formation.

### 方法
By running an additional simulation with an updated THESAN-ZOOM model containing Pop III stars, we show that this has a large impact on the simulated abundance ratios, pushing them closer to those observed in potential Pop III-enriched gas.

### 实验/数据
With THESAN-ZOOM, a set of high-resolution radiation hydrodynamical zoom-in simulations of galaxies, we investigate the metal abundance patterns observable in absorption. As our fiducial simulations do not include Pop III enrichment channels, our primary goal is to test how galaxy formation processes can shape observed abundance ratios. In our simulations, a larger dispersion in abundance ratio distributions (often interpreted as possible evidence of pollution from the first stellar populations) naturally arises with increasing redshift, when the metallicity and dust content are lower.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
By running an additional simulation with an updated THESAN-ZOOM model containing Pop III stars, we show that this has a large impact on the simulated abundance ratios, pushing them closer to those observed in potential Pop III-enriched gas.

### 9. A Mesh for Every Moment

- 作者：Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34939v1

### 背景/问题
We present MEMO (a Mesh for Every MOment), a method that reconstructs the geometry of complete dynamic scenes, captured by multiple synchronized cameras, and extracts a mesh at every frame. Existing dynamic Gaussian splatting methods either model appearance alone or target isolated objects segmented by foreground masks, and all of them recover meshes by TSDF fusion or Poisson reconstruction, whose fixed grids limit the detail they can capture.

### 方法
We present MEMO (a Mesh for Every MOment), a method that reconstructs the geometry of complete dynamic scenes, captured by multiple synchronized cameras, and extracts a mesh at every frame. Existing dynamic Gaussian splatting methods either model appearance alone or target isolated objects segmented by foreground masks, and all of them recover meshes by TSDF fusion or Poisson reconstruction, whose fixed grids limit the detail they can capture. At the core of MEMO is a per-Gaussian motion model inspired by Gaussian processes, which represents each Gaussian's position and rotation over time as a combination of temporal Gaussian kernels.

### 实验/数据
The model keeps every Gaussian a valid surface element throughout the sequence and carries an implicit representation of the dynamic geometry, so a mesh can be derived at any time from a field defined by the Gaussians. We evaluate MEMO on Blender-Moments, a new benchmark of nine animated scenes with ground-truth meshes at every frame, and on two real-world datasets.

### 结果
MEMO reconstructs the most accurate geometry among state-of-the-art methods, and remains competitive in novel-view synthesis and training time.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Project page: https://memo-4d.github.io

### 10. Attack Policy Selection can Mislead Monitor Evaluators

- 作者：Charlie Griffin, Oliver Makins, Asa Cooper Stickland, Alessandro Abate, Yarin Gal, Abby D'Cruz, Xander Davies｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34934v1

### 背景/问题
AI monitors, classifiers that flag dangerous behaviour by AI agents, are often evaluated against transcripts generated by attack policies acting as proxies for dangerous behaviour in deployment. We evaluate an ex-production OpenAI monitor as a case study and find that measured false negative rate is highly sensitive to both the method used to generate attack policies and the level of optimisation applied within that method.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Making convincing arguments remains an open problem.

### 11. $μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents

- 作者：Qihao Lin, Guanxu Chen, Shuhang Zheng, Xiaoya Lu, Jingyi Yang, Terumi Chiba, Wenyi Yu, Chao Zhang 等｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34920v1

### 背景/问题
Voice agents in shared spaces must satisfy interdependent multi-user requests while upholding per-user authority, privacy, and task constraints. Existing evaluations offer limited coverage when participants react throughout a session.

### 方法
Across 13 voice agents, proprietary systems peak at 62.24\% tool-free and 65.44\% tool-augmented success, while open-weight models remain below 20\%. ATC diagnostics show that open-weight models lag primarily in multi-turn attribution and threading, and controlled contrasts reveal that larger groups consistently degrade joint task success across capable systems.

### 实验/数据
By coupling reactive multi-user simulation with verifiable session-level outcomes, $μ$-Bench provides a rigorous testbed for shared voice agents.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
By coupling reactive multi-user simulation with verifiable session-level outcomes, $μ$-Bench provides a rigorous testbed for shared voice agents.

### 12. Memory Is Not Ground Truth: Revising Navigation Authority under Unreliable VLM Evidence for Persistent Semantic Navigation

- 作者：Sumukh Shrote, Shenbagaraj Kannapiran, Eric Eaton, Camillo Jose Taylor｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34915v1

### 背景/问题
Vision-language models (VLMs) enable robots to reason about semantic and spatio-temporal context, verify task-relevant objects, and guide sensing and navigation. Persistent memory can reduce redundant search for field robots, but when should a memory continue to guide behavior?

### 方法
Vision-language models (VLMs) enable robots to reason about semantic and spatio-temporal context, verify task-relevant objects, and guide sensing and navigation. In three matched real-robot decision contexts, an episode-local baseline selected a stale memory as its navigation objective in every case, whereas our method selected semantic frontiers in all three.

### 实验/数据
Persistent memory can reduce redundant search for field robots, but when should a memory continue to guide behavior? Our experiments show why this evidence can remain ambiguous under VLM-based perception. False-negative rates vary substantially across objects, nearby revisits often reproduce the same detector outcome, and some matched target-present and target-removed experiments yield identical miss histories.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results support revising memory actionability rather than interpreting failed detection as object absence.

### 13. The thermodynamic budget of objectivity

- 作者：Wonyong Chung｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34909v1

### 背景/问题
An event becomes a fact when enough independent records of it exist such that no operation is possible that leaves all observers ignorant of it again. Records are physical, and creating, keeping, and destroying them have thermodynamic costs.

### 方法
We compute these costs exactly in a minimal broadcast model with a driven central qubit writing records into $N$ initially thermal registers, with work sources and baths at temperature $T$.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Records in re-thermalizing media are nonequilibrium steady states, and the minimal power to maintain a record at $(R,δ)$ is the known two-state driving bound evaluated at the record-quality boundary.

### 14. Product-Linear POSIX Parsing

- 作者：Yuya Uezato｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34904v1

### 背景/问题
POSIX regular-expression matching reports capture spans determined by the parse tree that its disambiguation rules select. Thompson's classical construction decides whether an expression $E$ matches a text $w$ in product-linear time, $O(|E|\,|w|)$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
It implements POSIX selection with lists of end positions of the open subexpressions, which it compares and updates in constant time.

### 15. ProbFaS: Probabilistic Video Frame Selection for MLLMs via Multi-Fidelity Calibration

- 作者：Tianru Zhang, Mayank Nautiyal, Hugo Eidmann, Prashant Singh, Ekta Vats｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34903v1

### 背景/问题
Processing long videos with multimodal large language models (MLLMs) is prohibitively expensive, making informative frame selection essential for accurate video understanding. The default uniform sampling often misses task-relevant keyframes, while recent training-free selectors instead pick frames by how well each one matches the question under an image-text alignment (ITA) score.

### 方法
Processing long videos with multimodal large language models (MLLMs) is prohibitively expensive, making informative frame selection essential for accurate video understanding. We present ProbFaS, a training- and label-free probabilistic pipeline that fuses both signals for key frame selection.

### 实验/数据
未在摘要中明确给出。

### 结果
Across Video-MME, MLVU and LongVideoBench, ProbFaS is the most accurate among fourteen state-of-the-art training-free selectors and uniform sampling in 13 of 15 settings (8-128 frames), outperforming the strongest baseline by up to 3.1 percentage points.

### 结论/启示（面向电商发券、定价、营销算法等应用）
On MLVU and LongVideoBench, 32 ProbFaS frames match or surpass the top baseline at 128 frames and uniform sampling with up to 768 frames.

### 16. The Splash population confined to the Milky Way bar region

- 作者：Aakash Pandey, Ortwin Gerhard｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34890v1

### 背景/问题
We investigate the chemo-dynamical properties of in-situ stars in the Galactic bar region (central $5$ kpc), specifically the inner Galactic counterpart of the solar-neighbourhood Splash population (in situ halo). We use a sample of APOGEE DR17 red giants with Gaia astrometry and AstroNN distances, and separate bulge/bar stellar populations dynamically using a normalised time-averaged bar-frame angular momentum, $\mathcal{V}_φ$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
The presence of a significant central Splash underscores the role of the Gaia-Sausage-Enceladus merger in the early history of the Galaxy.

### 结论/启示（面向电商发券、定价、营销算法等应用）
At metallicities [Fe/H] $<0.3$, we find no additional classical bulge population in these maps beyond the central Splash and proto-Galactic populations $-$ the high-$α$ bulge appears to have evolved from the early high-$α$ disc.

### 17. Atheism and Cross-Country National Cognitive Skills: Evidence from a Beta Regression Analysis

- 作者：Tatiene C. Souza, Francisco Cribari-Neto｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34885v1

### 背景/问题
This study performs a beta regression analysis to investigate how country-level cognitive skills---measured using harmonized large-scale international educational assessments and expressed on an IQ-type scale---are associated with the prevalence of atheism in 131 countries. We find that this association is nonlinear: at low levels of cognitive skills, increases are associated with lower expected levels of atheism, whereas beyond a threshold, they are associated with higher expected atheism rates.

### 方法
We estimate elasticities of expected atheism rates with respect to cognitive skills for all countries in the sample and introduce the concept of the atheism gap to identify countries where observed prevalence is substantially higher or lower than predicted by their conditioning variables.

### 实验/数据
We find that this association is nonlinear: at low levels of cognitive skills, increases are associated with lower expected levels of atheism, whereas beyond a threshold, they are associated with higher expected atheism rates.

### 结果
We find that this association is nonlinear: at low levels of cognitive skills, increases are associated with lower expected levels of atheism, whereas beyond a threshold, they are associated with higher expected atheism rates.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We estimate elasticities of expected atheism rates with respect to cognitive skills for all countries in the sample and introduce the concept of the atheism gap to identify countries where observed prevalence is substantially higher or lower than predicted by their conditioning variables.

### 18. Letter of Intent: AN Underground Belayed In-Shaft (ANUBIS) detector

- 作者：ANUBIS Collaboration｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34882v1

### 背景/问题
Long-lived particles (LLPs) arise naturally in many extensions of the Standard Model, notably in models with dark matter candidates or motivated by baryogenesis. LLPs produced at or above the electroweak scale with decay lengths of tens of metres escape the general-purpose LHC detectors and cannot be produced at sufficient rates in forward and beam-dump experiments.

### 方法
Long-lived particles (LLPs) arise naturally in many extensions of the Standard Model, notably in models with dark matter candidates or motivated by baryogenesis. This Letter of Intent proposes the ANUBIS detector, which would instrument the ceiling of the ATLAS cavern and the bottom of its access shafts with about 1600~m$^2$ of resistive plate chambers in two tracking layers about 1~m apart, using the air-filled volume above the ATLAS detector as decay volume.

### 实验/数据
LLPs produced at or above the electroweak scale with decay lengths of tens of metres escape the general-purpose LHC detectors and cannot be produced at sufficient rates in forward and beam-dump experiments. The ANUBIS detector exploits the full ATLAS event information to suppress backgrounds, and exchanges triggers with the ATLAS experiment. The detector design, trigger concept, integration with the ATLAS experiment and a timeline towards installation in LHC Long Shutdown 4 are presented.

### 结果
With 3~ab$^{-1}$ at the High-Luminosity LHC, it would improve the sensitivity to exotic Higgs-boson decays into long-lived scalars by two to three orders of magnitude, probe heavy neutral leptons of all three flavours down to mixings of about $2\times10^{-8}$, and extend the reach for axion-like particles.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The detector design, trigger concept, integration with the ATLAS experiment and a timeline towards installation in LHC Long Shutdown 4 are presented.

### 19. Towards Closing the Performance Gap in Cross-Modal Place Recognition

- 作者：Ofer Idan, Dan Badur, Yoli Shavit｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34877v1

### 背景/问题
Cross-modal place recognition (CMPR) matches natural language descriptions against databases of geo-tagged reference images, enabling localization without visual queries. Despite its potential for language-guided navigation, existing vision-language models lag far behind visual place recognition (VPR) baselines, even after task adaptation.

### 方法
Despite its potential for language-guided navigation, existing vision-language models lag far behind visual place recognition (VPR) baselines, even after task adaptation. To address this challenge, we propose CrossPlace, a two-stage CMPR framework.

### 实验/数据
Cross-modal place recognition (CMPR) matches natural language descriptions against databases of geo-tagged reference images, enabling localization without visual queries.

### 结果
Through systematic analysis, we isolate the drivers of retrieval accuracy and show that visual token density provides the largest performance improvement, while text encoder capacity and task fine-tuning offer complementary gains. Across all existing and new benchmarks, CrossPlace achieves double-digit Recall@1 improvements over prior cross-modal methods, closes the gap to unimodal text retrieval, and narrows it to unimodal VPR.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Code and benchmarks are available at https://github.com/oferidan1/CrossPlace

### 20. SoK: When FL Clients Cannot Train -- Delegated Federated Learning for IoT

- 作者：Hamed Mohammed Alkharsh, Aydin Abadi, Jakub Szelag, Suleiman Muhammad Sabo, Ishak Semuel Beno｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34876v1

### 背景/问题
Federated learning (FL) assumes that a client can perform the computation required to produce its own contribution. This assumption is often unrealistic for resource-constrained Internet of Things (IoT) devices, motivating designs that delegate some or all client-side training to more capable parties.

### 方法
We develop a framework that examines three dimensions over the same delegated transition: delegate-view privacy, delegated attribution, and constrained-owner feasibility.

### 实验/数据
We systematize this setting as delegated federated learning (Delegated FL), where data ownership and execution of owner-attributed learning are separated.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our findings demonstrate why individually established guarantees do not necessarily support the same end-to-end claim and motivate evaluating privacy, attribution, and residual owner cost over the same delegated transition.

### 21. Exact monogamy of steering and remote Wigner negativity for multimode Gaussian nodes

- 作者：Sudip Chakrabarty｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34874v1

### 背景/问题
Optical quantum networks route correlations through nodes that hold several modes and are linked to many neighbors. Steering is the correlation behind one-sided device-independent tasks and behind the remote preparation of non-Gaussian states.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results determine exactly how many neighbors one multimode node can serve with steering and with remote Wigner negativity.

### 22. RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies

- 作者：Insup Lee, Hojin Jeon, Sunguk Shin, Seoungbin Bae, Taekwan Kim, Jinwoo Shin, Dongsu Han｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34864v1

### 背景/问题
Since vision-language-action (VLA) policies can inherit the slow pace of human demonstrations, accelerating these demonstrations before fine-tuning can lead to faster VLA policies without an additional speed-selection module at deployment. Several offline speedup methods have focused on identifying segments that require less precision and assigning predefined speedup factors to the segments.

### 方法
Several offline speedup methods have focused on identifying segments that require less precision and assigning predefined speedup factors to the segments. To this end, this paper presents RePace, an offline reasoning framework that determines how much to accelerate each part of a demonstration. Given the task instruction, a pretrained language model uses the visual context and original motion of successive windows to interpret these candidate retiming effects and select a speedup profile for the complete episode.

### 实验/数据
Several offline speedup methods have focused on identifying segments that require less precision and assigning predefined speedup factors to the segments. To this end, this paper presents RePace, an offline reasoning framework that determines how much to accelerate each part of a demonstration. Experimental results demonstrate that RePace outperforms the baselines in overall task execution efficiency on both LIBERO and RoboCasa-Kitchen.

### 结果
Experimental results demonstrate that RePace outperforms the baselines in overall task execution efficiency on both LIBERO and RoboCasa-Kitchen.

### 结论/启示（面向电商发券、定价、营销算法等应用）
On all three tasks with a gripper-equipped Franka Research 3 arm, RePace matches or exceeds the acceleration baselines in success rate and completes successful trials faster.

### 23. Focus Only on What's Important: Training-Free Focus Maps for Frozen Vision Transformers in Long-Video Object Segmentation

- 作者：Harsha Karipineni, Rajesh Reddy Chintha｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34863v1

### 背景/问题
Vision transformers are strong but costly image encoders for video object segmentation. Training-free token merging cuts compute uniformly across the frame, including on tracked objects.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Code: https://github.com/boletoms/focused-cv

### 24. An offset--drift Kalman filter for continuous emotion recognition and annotation from sparse human reviews

- 作者：Jie Dong, Mahdi Zareei｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34857v1

### 背景/问题
Continuous emotion recognition tracks how emotion changes over time, but its predictions often deviate from human ratings, and the traces it is trained on are rated in real time by several annotators, which is slow and costly. A few human reviews could help with both, but rejection only decides which predictions to hand over and adaptation adjusts the model or its outputs; neither uses reviews to correct unreviewed windows directly.

### 方法
A few human reviews could help with both, but rejection only decides which predictions to hand over and adaptation adjusts the model or its outputs; neither uses reviews to correct unreviewed windows directly. We propose a Kalman-filter correction that models the predictor's error as a per-part offset plus a slow drift, estimates it from the reviewed windows and corrects every unreviewed window online, leaving the predictor unchanged.

### 实验/数据
We propose a Kalman-filter correction that models the predictor's error as a per-part offset plus a slow drift, estimates it from the reviewed windows and corrects every unreviewed window online, leaving the predictor unchanged.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The same correction serves annotation: with 20% of windows reviewed, the completed trace comes closer to the raters.

### 25. On Zappa--Szép products of multiplicative racks

- 作者：Akihiro Takano｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34851v1

### 背景/问题
We study Zappa--Szép products of multiplicative racks, namely monoids equipped with compatible rack operations. We characterize multiplicative rack structures on Zappa--Szép products of monoids and prove that every exact factorization of multiplicative racks induces a canonical exact factorization of their universal groups.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we use a layered central-quotient construction to obtain finite and infinite non-cancellative multiplicative quandles with non-group factors and nontrivial Zappa--Szép actions, all directly indecomposable as monoids.

### 26. Quot schemes on projective space

- 作者：Ritvik Ramkumar｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34844v1

### 背景/问题
We develop general methods for studying Quot schemes on projective space, including a new construction of components with no common neighbours. We show that the radius of Hilbert and Quot schemes can grow linearly with the dimension of the subschemes being parametrized, and construct the first examples of Hilbert schemes of curves with radius two.

### 方法
We develop general methods for studying Quot schemes on projective space, including a new construction of components with no common neighbours.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In most cases, we give explicit geometric descriptions in terms of products of generalized flag varieties and projective bundles over Grassmannians.

### 27. A Reconfigurable Four-State Sensor Based on Orthogonal Thermal and Chemical Stimuli

- 作者：Ashfaq Ur Rahman Ifty, Sadia Basher, Abdullah Al Zayed, Mohammad Abrar Kabir, Rakibul Hasan Sagor｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34834v1

### 背景/问题
This article presents a novel four-state refractive index (RI) sensor based on distinct phases of palladium (Pd) and vanadium dioxide (VO$_2$), controlled by orthogonal thermal and chemical stimuli. This is a numerical, simulation-only study: all results are obtained from two-dimensional finite-element method (FEM) simulations.

### 方法
The proposed sensor achieves a peak sensitivity of 2871 nm/RIU for the undoped reference configuration and 2798 nm/RIU for the practical W-doped device, together with a peak CSS of 16,872 nm/RIU, establishing it as a multi-state reconfigurable platform with reduced thermal crosstalk and potential applications in industrial safety monitoring and optical logic gates.

### 实验/数据
This is a numerical, simulation-only study: all results are obtained from two-dimensional finite-element method (FEM) simulations.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The proposed sensor achieves a peak sensitivity of 2871 nm/RIU for the undoped reference configuration and 2798 nm/RIU for the practical W-doped device, together with a peak CSS of 16,872 nm/RIU, establishing it as a multi-state reconfigurable platform with reduced thermal crosstalk and potential applications in industrial safety monitoring and optical logic gates.

### 28. Not all world models can doubt: how training objective and architecture shape epistemic uncertainty in JEPA and RSSM world models

- 作者：Simon Baur, Wojciech Samek, Jackie Ma｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34830v1

### 背景/问题
World models predict how an environment responds to actions, so that candidate actions can be evaluated before execution. Executed actions, or decisions, taken in this manner are only as reliable as the model's predictive capabilities, and predictions in turn are only reliable within the model's experience.

### 方法
World models predict how an environment responds to actions, so that candidate actions can be evaluated before execution. Executed actions, or decisions, taken in this manner are only as reliable as the model's predictive capabilities, and predictions in turn are only reliable within the model's experience. In this work we offer an extensive empirical study on how training objectives and architectures shape epistemic uncertainty of world models.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We further show that this translates to gaps in five uncertainty related downstream tasks, from unfamiliar-state detection to uncertainty-penalised planning: the RSSM uncertainty misses deviations that its own posterior registers, whereas the JEPA uncertainty reports what its model sees.

### 29. The Linguistic Knowledge Benchmark: Do Language Models Know the Foundations of Early-Grade Literacy?

- 作者：Maxime Lelièvre, Alasdair Mackintosh, Dominic Andrews, Tobias Murray, Moritz Boos, Oliver G. B. Garrod｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34823v1

### 背景/问题
Many languages of instruction in low- and middle-income countries (LMICs) are poorly represented in the data used to train language models. Before these models can support early-grade literacy in such languages, we need to know whether they hold the linguistic knowledge of each language that literacy teaching relies on.

### 方法
Many languages of instruction in low- and middle-income countries (LMICs) are poorly represented in the data used to train language models. Before these models can support early-grade literacy in such languages, we need to know whether they hold the linguistic knowledge of each language that literacy teaching relies on. To test this, we present the Linguistic Knowledge Benchmark and the reproducible, largely automated pipeline that turns curriculum documents, teacher guides and pupil books into a vetted question set organised on a fixed grid of nine linguistic domains and seven grade levels.

### 实验/数据
Many languages of instruction in low- and middle-income countries (LMICs) are poorly represented in the data used to train language models.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
This is the first rung of a three-level evaluation ladder for measuring and generating decodable text to support foundational literacy.

### 30. LoopTitan: What Does Parameter Revisit Buy a Mixture-of-Experts?

- 作者：Zichen Tian, Yudong Lu, Xuansheng Wu, Na Zou, Xia Hu, Guanchu Wang, Qianru Sun｜年份：2026｜发布时间：2026-11-25｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.34821v1

### 背景/问题
Looped Mixture-of-Experts (MoE) architectures revisit layer parameters across depths. This design increases effective depth without adding parameters.

### 方法
Accordingly, we propose LoopTitan-Base as a stronger MoE baseline. We open-source LoopTitan and release 17 pretrained models (including LoopTitan-Base and the control).

### 实验/数据
Our experiment record is public as GitHub issues, with predictions pre-registered and the full exploration history kept.

### 结果
This design increases effective depth without adding parameters. First, at matched budgets, we decompose the state-of-the-art looped recipe, with revisit last.

### 结论/启示（面向电商发券、定价、营销算法等应用）
This is our Phase 1 technical report, laying the foundation for follow-up studies.
