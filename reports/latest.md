# CausalRadar 日报 - 2026-11-02

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Landscape Intervals: A Geometric Framework for Multiparameter Persistence Landscapes

- 作者：Pan Fang, Washington Mio, Tom Needham｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**4.74**
- 链接：https://arxiv.org/abs/2610.42090v1

> 命中：hit_scenario=['ads']

### 背景/问题
Classical persistent homology provides a summary of the multiscale topology of a filtration of a space. These summaries are not naturally valued in a vector space, limiting their direct use in standard machine learning pipelines.

### 方法
On the practical side, we introduce a robust numerical framework for extracting our invariants from real data and for incorporating them into standard machine learning pipelines. The framework is illustrated on surface mesh and medical image data.

### 实验/数据
On the practical side, we introduce a robust numerical framework for extracting our invariants from real data and for incorporating them into standard machine learning pipelines. The framework is illustrated on surface mesh and medical image data.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The framework is illustrated on surface mesh and medical image data.

### 2. ReLift: Dense 3D Tracking as Lifted Trajectory Repair

- 作者：Assaf Singer, Maroun Khriesh, Noam Rotstein, Yoni Kasten, Or Litany｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.42136v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Dense 3D tracking from monocular video requires establishing point correspondences over time, estimating their depth, and inferring their trajectories during occlusion. Existing methods typically learn these tasks jointly, a demanding objective given the scarcity of 4D supervision.

### 方法
We show that strong pretrained 2D trackers and 3D geometry models provide an effective foundation: lifted trajectories, with occluded segments simply interpolated, already rival dedicated 3D trackers using the same geometry. We introduce ReLift, an efficient feed-forward framework that recasts dense 3D tracking as geometric trajectory repair and completion. Using only geometric inputs allows us to train directly on 3D trajectories with simulated lifting errors, decoupling training from images and from any specific tracker or geometry model.

### 实验/数据
未在摘要中明确给出。

### 结果
We show that strong pretrained 2D trackers and 3D geometry models provide an effective foundation: lifted trajectories, with occluded segments simply interpolated, already rival dedicated 3D trackers using the same geometry. However, lifted trajectories inherit correspondence and depth errors, and under occlusion, their depth comes from the occluder rather than the tracked point. We introduce ReLift, an efficient feed-forward framework that recasts dense 3D tracking as geometric trajectory repair and completion.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Visit our supplementry page for more examples and code.

### 3. Instance-dependent sequential limits as an exact information ledger

- 作者：Akshay Balsubramani｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.42133v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Instance-dependent limits for bandit regret, sequential tests, best-arm identification and Markov decision processes are proved by one chain. It runs from a divergence decomposition through data processing to a statistic, a testing step that turns a class guarantee into a requirement on the history, and optimization over alternatives and allocations.

### 方法
For identification among trained models and for Wald's test the largest term is usually the uniform quantification's.

### 实验/数据
It runs from a divergence decomposition through data processing to a statistic, a testing step that turns a class guarantee into a requirement on the history, and optimization over alternatives and allocations. By the chain rule, data processing loses exactly a conditional divergence, which vanishes for arms in natural exponential families at the per-arm counts and reward sums.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
For identification among trained models and for Wald's test the largest term is usually the uniform quantification's.

### 4. Think in 360°: Benchmarking and Bootstrapping Panoramic Video Reasoning

- 作者：Lidong Lu, Lidong Zou, Xinyi Mao, Jiaxin Lv, Zhenquan Li, Liangrui Dong, Tong Lu, Guo Chen｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.42082v1

> 命中：hit_abstract=['CATE']

### 背景/问题
A panoramic video captures all directions around the camera, but relevant evidence can appear in different directions and at different times. Understanding it requires models to connect observations across the viewing sphere and time.

### 方法
Understanding it requires models to connect observations across the viewing sphere and time. Evaluation of 11 proprietary, open-source, and panoramic-specialized models identifies cross-view tracking and sphere-time evidence integration as their weakest capabilities.

### 实验/数据
To strengthen these capabilities, we construct PanoVideoCoT, the first reasoning dataset grounded in real panoramic video, through sphere-time-grounded synthesis that converts verified panoramic observations and successful agentic explorations into 13,465 QA-CoT pairs.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The gains concentrate on the same spatial, cross-view, and temporal capabilities exposed by the benchmark, showing that grounded sphere-time supervision can equip a general video MLLM with panoramic reasoning.

### 5. Proof-Carrying Evolution: Black-Box Search, White-Box Flight

- 作者：Amit Jain, Sergio Sanchez-Hurtado, Victor Rodriguez-Fernandez, Richard Linares｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.42043v1

> 命中：hit_abstract=['CATE']

### 背景/问题
We study whether a language model can help design controllers whose behavior can be formally checked. In proof-carrying evolution (PCE), a search proposes controllers together with their certificates.

### 方法
We study whether a language model can help design controllers whose behavior can be formally checked. In proof-carrying evolution (PCE), a search proposes controllers together with their certificates. Their mathematical forms are fixed; a proposer chooses their numerical parameters together.

### 实验/数据
未在摘要中明确给出。

### 结果
On SO(3), no model detectably outperforms CMA-ES when mixed with classical mutation. When models write every proposal, one tested model improves on CMA-ES and the other performs worse than its mixed variant.

### 结论/启示（面向电商发券、定价、营销算法等应用）
In a docking control with the objective and mutation operator held fixed, retaining certified candidates yields new certified designs in every run; removing this rule yields none.

### 6. GeoFlip: Benchmarking Geometry-Sensitive Physics in Video Generation

- 作者：Yuqi Li, Junming Liu, Bowen Hu, Ruize Niu, Huiran Duan, Yingli Tian, Hao Wu｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.42002v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Video generation models synthesize realistic motion, but can they respond correctly to changes in initial geometry? We introduce GeoFlip, a video generation benchmark centered on physical outcome flips induced by geometry.

### 方法
Video generation models synthesize realistic motion, but can they respond correctly to changes in initial geometry? These pairs test whether models translate geometric differences in the first frame into correct physical evolution. We evaluate 16 models for image to video generation along three dimensions: event correctness, structural integrity, and similarity to reference videos.

### 实验/数据
The benchmark comprises 482 scene pairs and 964 reference videos across six physical categories, with reference outcomes established through procedural scene construction, physics simulation, and numerical validation and verification of physical events.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
By combining controlled geometric interventions, verifiable physical references, and multidimensional evaluation, GeoFlip assesses progress from visual realism toward physical consistency conditioned on geometry.

### 7. Hierarchical World Models with Implicit Dynamics

- 作者：Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, Nicolas Ballas, Mido Assran, Lerrel Pinto, Yann LeCun｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.42146v1

> 命中：hit_abstract=['policy learning']

### 背景/问题
Planning with world models enables test-time adaptation for embodied agents, offering superior generalization over direct policy learning. However, long-horizon tasks remain hindered by cumulative errors and search complexity.

### 方法
Planning with world models enables test-time adaptation for embodied agents, offering superior generalization over direct policy learning. We introduce ID-WM (Implicit Dynamics World Models), a hierarchical world model that decouples state-space reachability from local control. Our framework utilizes a high-level model to sample feasible transitions across the state manifold and a low-level world model as an inverse dynamics solver to ground these transitions into precise actions.

### 实验/数据
未在摘要中明确给出。

### 结果
We demonstrate its effectiveness across three navigation and manipulation suites, achieving a 38.5% improvement over state-of-the-art policy and diffusion-based planners.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Videos can be viewed at https://id-wm.github.io

### 8. Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space

- 作者：Biaoliang Guan, Tingyu Yuan, Wen Ye, Ziming Ji, Xu Yang, Yan Huang, Jihua Zhu, Chaoyang Zhao｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.42021v1

> 命中：hit_abstract=['policy learning']

### 背景/问题
Large-scale egocentric human videos provide rich and scalable manipulation experience for robot policy learning, yet substantial embodiment gaps in visual appearance, kinematic structure, and action spaces hinder effective knowledge transfer. Existing methods often decouple cross-embodiment knowledge alignment from robot policy learning, making it difficult for human manipulation knowledge to directly and fully contribute to robot action learning.

### 方法
To address this issue, we propose Nexus-VLA, a hybrid policy learning framework that enables cross-embodiment knowledge transfer through end-to-end human-robot joint training, allowing human manipulation experience to directly contribute to robot policy learning.

### 实验/数据
Across RoboCasa-GR1, OOD settings, and real-world robot experiments, Nexus-VLA achieves an 80.5% task success rate on RoboCasa-GR1 and demonstrates strong advantages in human-data utilization, learning efficiency, and cross-scenario generalization.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Across RoboCasa-GR1, OOD settings, and real-world robot experiments, Nexus-VLA achieves an 80.5% task success rate on RoboCasa-GR1 and demonstrates strong advantages in human-data utilization, learning efficiency, and cross-scenario generalization.

### 9. GazeRIB: Systematic Evaluation of Multi-Reader Gaze-Guided Chest X-ray Learning

- 作者：Nattakorn Kittisut, Roy M. Gabriel, Marly van Assen, Mohammadreza Zandehshahvar, Carlo N. De Cecco, Elizabeth A. Krupinski, Ali Adibi｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42152v1

### 背景/问题
Radiologists' visual attention can supervise medical image learning, but how reader panel composition affects its value remains untested. We evaluated GazeRIB (Gaze-guided Radiologist-Informed Blackout), which masks unviewed regions during training and uses unmasked images at inference.

### 方法
We compared individual readers with three-, five- and eight-reader panels across seven architectures and 10 seeds, evaluating 910 models on a separate 2,897-CXR cohort for four-class severity prediction.

### 实验/数据
未在摘要中明确给出。

### 结果
Every panel improved macro F1 over the no-gaze baseline by 5.33-7.47 percentage points (pp; Bonferroni-adjusted p < 0.007); no individual reader reached significance on this endpoint. On external validation without retraining, all four panels improved ROC-AUC on SIIM-FISABIO-RSNA by +1.93 to +4.24 pp (p <= 0.004); on MIMIC-Eye no panel differed significantly from baseline, whereas the single-reader average declined (-1.40 pp, p = 0.008).

### 结论/启示（面向电商发券、定价、营销算法等应用）
Reader composition therefore influenced performance, although transfer depended on the cohort.

### 10. Non-sofic Tarski monsters

- 作者：Kıvanç Ersoy｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42140v1

### 背景/问题
We prove the existence of non-sofic Tarski monsters of every sufficiently large prime exponent and of torsion-free non-sofic Tarski monsters. The proof combines a theorem of Sandhu--Thom with quotient theorems of Semenov.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These examples are $ω$-non-sofic, and the locally graded ones contain no minimal non-sofic subgroup.

### 11. On the Iwasawa invariants of admissible quadratic twists of elliptic curves at ordinary Eisenstein primes

- 作者：Mulun Yin｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42137v1

### 背景/问题
We study the Iwasawa $μ$- and $λ$-invariants of quadratic twists of rational elliptic curves at Eisenstein primes $p\geq 3$. We verify Greenberg's $μ=0$ conjecture for all such twists, which gives an Euler system free proof of Mazur's cotorsion conjecture, and study the $λ$-invariants when the twist is admissible in the sense of [GV00].

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
As a consequence, we prove the cyclotomic Iwasawa Main Conjecture and obtain the $p$-part BSD formulae in rank $0$ for admissible twists under mild conditions, covering many elliptic curves of potentially ordinary reduction.

### 12. Baker--Akhiezer sections from Higgs bundles and Landau levels in hyperbolic band theory

- 作者：Duong Dinh, Steven Rayan｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42134v1

### 背景/问题
As observed by Kienzle and the second author, rank-two $\mathcal{O}(3)$-twisted Higgs bundles on the projective line encode all hyperbolic crystals of genus two: the spectral curves are the unit cells, and the Hitchin fibers are the abelian Brillouin zones. In a uniform magnetic field of two flux quanta, the lowest Landau level is one-dimensional at every nonzero momentum, and, as found by Iengo and Li, its dimension jumps to two at the zero momentum.

### 方法
We identify the states of the lowest Landau level with the Baker--Akhiezer sections of the Higgs bundles, and their zeros, the vortices, with the Baker--Akhiezer divisors. A family of nonzero momenta limits to the zero momentum exactly when each of the two vortices approaches the image of the other under the spatial inversion, and the states of the jumped level are labeled by the directions of limiting.

### 实验/数据
In a uniform magnetic field of two flux quanta, the lowest Landau level is one-dimensional at every nonzero momentum, and, as found by Iengo and Li, its dimension jumps to two at the zero momentum.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Such a family of Higgs bundles limits to the Hitchin section, thereby crossing to a lower stratum of the \BB stratification, an example of the phenomenon investigated in terms of Baker--Akhiezer divisors by the first author with Figiel and Teschner.

### 13. Persistence of Unitary Almost Mathieu Operator Gaps Ten Dry Martinis, Five on the Rim

- 作者：Dan S. Borgnia, Matthew Faust, Long Li｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42120v1

### 背景/问题
We determine exactly which gap labels are realized by open spectral gaps for the unitary almost Mathieu operator at every irrational frequency and all coupling constants ($0<λ_1,λ_2\leq1$). When both couplings are strictly less than one, every permitted gap label is realized by an open gap, including in the critical case ($λ_1=λ_2$).

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
When at least one coupling equals one, both lifts of every odd winding label are realized by open gaps, whereas all even winding labels are collapsed.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The proof combines quantitative almost reducibility and Aubry duality with a monotonicity principle for gap heights.

### 14. Band Random Graphs: Connectivity, Geometry, and Transport

- 作者：Shantanav Chakraborty, Kyle Luh, Rudransh Pratap Singh｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42107v1

### 背景/问题
Let $G(n,p,m)$ be the random subgraph of the cycle power $C_n^m$ obtained by retaining each edge independently with probability $p$. We study connectivity, component geometry, and random walks throughout the regime $\log n\ll m<n/2$.

### 方法
Thus, for this random graph model, connectivity has the Erdős--Rényi asymptotics with $2m$ possible neighbours, while distances, relaxation, and hitting times retain the geometry of the underlying cycle.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Thus, for this random graph model, connectivity has the Erdős--Rényi asymptotics with $2m$ possible neighbours, while distances, relaxation, and hitting times retain the geometry of the underlying cycle.

### 15. Charge Pumping Leptogenesis from the Symmetric Mass Generation Phase on a Four-Leg Ladder Lattice

- 作者：Runze Chi, Meng Zeng, Tao Xiang, Yi-Zhuang You, Bertrand I. Halperin, Juven Wang｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42103v1

### 背景/问题
Quantized charge pumping in quantum Hall systems is a bulk topological property, typically manifesting on gapless boundaries as spectral flow through chiral edge modes upon flux insertion. When the boundary is anomaly-free, it can be symmetrically gapped by symmetric mass generation (SMG) interactions.

### 方法
We address this using density-matrix renormalization group simulations of a four-leg ladder quasi-(2+1)d realization of the (1+1)d 3-4-5-0 lattice chiral fermion model with six-fermion interactions at one edge. We also identify spontaneous breaking of the model's $\mathbb{Z}_2$ symmetry above a critical interaction strength. Additionally, we propose an analogy between charge pumping in this model and a topological leptogenesis scenario in the (3+1)d Standard Model.

### 实验/数据
We address this using density-matrix renormalization group simulations of a four-leg ladder quasi-(2+1)d realization of the (1+1)d 3-4-5-0 lattice chiral fermion model with six-fermion interactions at one edge.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In both settings, charge pumping can be associated with a continuous deformation along a classically defined but quantum-anomalous direction, while a discrete subgroup remains an exact quantum symmetry.

### 16. ROOF: Learning Humanoid Fall Recovery under Overhead Constraints

- 作者：Yidan Lu, Jiayuan Yu, Zongrui Cai, Jingwen Sun, Jinrui Han, Jing Wang, Ping Luo, Peng Lu｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42097v1

### 背景/问题
A fallen humanoid beneath an overhead obstacle faces a coupled recovery problem. It must create clearance while organizing support for a stable rise, since attempting to stand before making room can further increase obstruction.

### 方法
To achieve this, a learned motion prior, together with posture-dependent support and joint-stall costs, is proposed to shape a single policy that learns when to clear the obstacle, how to establish support, and when to complete the rise, all using proprioception alone.

### 实验/数据
In simulation, it recovers in 88.5% of trials beneath plates that can only be lifted, compared with 18.9% without geometric guidance, and in 98.6% of trials beneath free plates with randomized size, mass and placement.

### 结果
It must create clearance while organizing support for a stable rise, since attempting to stand before making room can further increase obstruction. In simulation, it recovers in 88.5% of trials beneath plates that can only be lifted, compared with 18.9% without geometric guidance, and in 98.6% of trials beneath free plates with randomized size, mass and placement.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Project page: https://lu-yidan.github.io/ROOF/

### 17. A Counterexample to the Alon-Krivelevich Conjecture and a New Lower Bound for Choosability of Bipartite Graphs

- 作者：Junran Yu, Gexin Yu｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42094v1

### 背景/问题
For an integer $k\ge 2$ and $r^2>2(2k-1)\ln (2k-1)$, we construct a bipartite graph $G$ whose two vertex classes are disjoint copies of the family of all $k$-subsets of a $(2k-1)$-element set, two vertices being adjacent when their sets intersect in at most $r$ elements. Assigning each vertex its corresponding subset as its color list, $G$ is not colorable, and thus its choice number $\ch(G)\ge k+1$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In order to show the uncolorability, we use tools from probability (conditional product measure, nested coupling, and Doob martingale), which we write in an elementary language of weighted counting, and topology (Brouwer fixed-point theorem).

### 18. Rethinking Asymmetry in Self-Supervised 3D Geometry Learning

- 作者：Gyeongjin Kang, Freeman Cheng, Botao Ye, Weijie Lyu, Ming-Hsuan Yang, Eunbyung Park｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42092v1

### 背景/问题
Self-supervised learning relies on asymmetry between what a model observes and what it must explain. Recent methods learn 3D geometry from unposed images by predicting cameras and scene structure, then rendering held-out views.

### 方法
Self-supervised learning relies on asymmetry between what a model observes and what it must explain. We additionally align features with a frozen vision foundation model, which brings further gains. None of these signals requires geometric annotation, and the resulting model improves geometry estimation over prior self-supervised methods.

### 实验/数据
Controlled experiments isolate the contribution of each component, and self-supervised pretraining also improves subsequent supervised training.

### 结果
This improves depth and pose estimation over input-space designs. None of these signals requires geometric annotation, and the resulting model improves geometry estimation over prior self-supervised methods. Controlled experiments isolate the contribution of each component, and self-supervised pretraining also improves subsequent supervised training.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Controlled experiments isolate the contribution of each component, and self-supervised pretraining also improves subsequent supervised training.

### 19. Onset of Radiatively Driven Convection in Ice-Covered Freshwater Lakes

- 作者：Benjamin J. Smith, Bingfei Yan, Till J. W. Wagner, Nimish Pujara, Jennifer A. Franck｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42089v1

### 背景/问题
This work investigates the formation and growth of Rayleigh-Taylor instabilities (RTIs) during the onset of radiatively driven convection (RDC) in seasonally ice-covered freshwater lakes. Two-dimensional direct numerical simulations (DNS) and linear analysis allow for the investigation of how environmental factors, including thermal stratification, water clarity, and solar forcing influence RTI formation.

### 方法
Predictions of RDC onset obtained using the linear model show good agreement with DNS results.

### 实验/数据
Two-dimensional direct numerical simulations (DNS) and linear analysis allow for the investigation of how environmental factors, including thermal stratification, water clarity, and solar forcing influence RTI formation. When the analysis is applied to field measurements of ice-covered lakes, it is found that weakly stratified lakes may take a few hours before RDC onset whereas strongly stratified lakes may not see RDC onset after a full day of clear-sky spring conditions.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
When the analysis is applied to field measurements of ice-covered lakes, it is found that weakly stratified lakes may take a few hours before RDC onset whereas strongly stratified lakes may not see RDC onset after a full day of clear-sky spring conditions.

### 20. Delocalized region of bipartite Erdős-Rényi graphs

- 作者：Johannes Alt, Serafina Wald｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42088v1

### 背景/问题
We consider bipartite Erdős-Rényi graphs $\mathbb{G}(n, p, d/\sqrt{np})$ with two parts of sizes $n$ and $p$, respectively, and edge probability $d/\sqrt{pn}$. We show that for $d > b_* \log (n+p)$ all eigenvectors of its adjacency matrix, with eigenvalues away from zero, are delocalized with high probability.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our results also hold for sparse rectangular random matrices with independent entries.

### 21. Long-time stochasticity for periodic iterations of random surface maps

- 作者：Dmitry Dolgopyat, Bassam Fayad, Alexey Okunev｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42083v1

### 背景/问题
Let $M$ be a closed Riemannian surface, and let $f_1,\ldots,f_s$ be area-preserving $C^2$ diffeomorphisms with fixed positive probabilities such that the resulting random dynamical system is uniformly expanding on average. For each $n$, choose $ω_1,\ldots,ω_n$ independently according to these probabilities and set $F=f_{ω_n}\circ\cdots\circ f_{ω_1}$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The limiting Gaussian has variance $\int_Mφ^2\,d\mathrm{vol}$.

### 22. Constructing Lagrangian surfaces in all symplectic toric $4$-manifolds from multi-grid diagrams

- 作者：Shintaro Fushida-Hardy, Laura Wakelin｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42076v1

### 背景/问题
We present a new diagrammatic construction of Lagrangian surfaces in all symplectic toric $4$-manifolds from objects called multi-grid diagrams. These are a generalisation of triple grid diagrams for Lagrangian surfaces in $\mathbb{CP}^2$ wherein the underlying trisection is replaced by the more general notion of a toric decomposition.

### 方法
We present a new diagrammatic construction of Lagrangian surfaces in all symplectic toric $4$-manifolds from objects called multi-grid diagrams.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We give examples of multi-grid diagrams for Lagrangian surfaces in a range of symplectic toric $4$-manifolds, including Evans' recent non-squeezable Klein bottle in $S^2 \times S^2$.

### 23. Spectra of stochastic matrices with a Toeplitz interior

- 作者：Brecht Verbeken, Vincent Ginis｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42072v1

### 背景/问题
For stochastic matrices of order $n$, the Karpelevič region is the set of all possible eigenvalues. We study matrices whose first and last $m$ rows are arbitrary probability vectors, while the remaining middle rows come from one probability vector by successive cyclic shifts to the right, moving the last entry to the first position each time.

### 方法
Further results describe the smaller regions and the angles at which their boundaries approach roots of unity.

### 实验/数据
未在摘要中明确给出。

### 结果
As $m$ increases, their eigenvalue regions expand from the polygon spanned by the $n$th roots of unity.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Further results describe the smaller regions and the angles at which their boundaries approach roots of unity.

### 24. The Quartic Gap Between Quantum and Dequantized Algorithms for Linear Algebra Is Tight

- 作者：Shouvanik Chakrabarti, Dylan Herman, Junhyung Lyle Kim, Guneykan Ozgul｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42069v1

### 背景/问题
Quantum algorithms for linear algebra that access a matrix $A$ through quantum random access memory (QRAM) prepare quantum states proportional to the solutions of linear systems and related problems. Dequantized classical algorithms, when given sampling and query access to $A$, return sampling and query access to an approximate solution.

### 方法
All of these classical lower bounds follow from the same framework, which is based on a lower bound for sampling from distributions that depend on a fixed set of Fourier coefficients of an unknown Boolean function.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
All of these classical lower bounds follow from the same framework, which is based on a lower bound for sampling from distributions that depend on a fixed set of Fourier coefficients of an unknown Boolean function.

### 25. Counting Square Tilings with a Fixed Set of Polyominoes Is #EXP-Complete

- 作者：Qiuyu Chen, Baao Xie｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42063v1

### 背景/问题
The gap between feasibility and exact counting raises a fundamental question about how much information an input must carry to sustain computational hardness. We show that this separation persists even when the geometric rules are fixed and each instance is specified solely by the binary side length of a square.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The proof develops a two-stage numerical isolation technique that recovers accepting-computation counts from a boundary-amplified Wang system and preserves them through a rigid geometric compiler that controls all noncanonical polyomino tilings.

### 26. Rapid mixing of Potts Glauber dynamics throughout uniqueness

- 作者：Antonio Blanca, Reza Gheissari, Heehyun Park, Xusheng Zhang｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42059v1

### 背景/问题
Sampling from the ferromagnetic $q$-state Potts model is a fundamental problem in statistical physics and approximate counting. Although computationally hard in the worst case, sampling is expected to be efficient throughout the high-temperature uniqueness regime of the model using the natural single-site Glauber dynamics.

### 方法
Sampling from the ferromagnetic $q$-state Potts model is a fundamental problem in statistical physics and approximate counting. Although computationally hard in the worst case, sampling is expected to be efficient throughout the high-temperature uniqueness regime of the model using the natural single-site Glauber dynamics.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The results in this paper were arrived at with the assistance of ChatGPT 5.6 and 6.

### 27. A Charged Compact Star Solution for a Conducting Sphere

- 作者：Kai Lin｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42051v1

### 背景/问题
This paper considers the simplest charged stellar model, namely, a uniform density star with electric charge distributed on its surface. In this model, we treat the uniform density star as a conducting sphere, where all electric charges are uniformly distributed on the surface and represented by a delta function.

### 方法
This paper considers the simplest charged stellar model, namely, a uniform density star with electric charge distributed on its surface. In this model, we treat the uniform density star as a conducting sphere, where all electric charges are uniformly distributed on the surface and represented by a delta function.

### 实验/数据
This is because the electric field itself is also a part of the stress energy tensor $T_{μν}$, acting as a source of gravity. When the gravitational effect of the electric field dominates, the perfect fluid must provide outward pressure to balance the inward gravitational attraction.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The computational results show that the waveforms of quasinormal modes vary with different charges.

### 28. A richness-sensitive Acoustic Biodiversity Index from species-level detections: classifier benchmarking, false-positive control and validation against standard soundscape indices in an African savanna and an urban zoo

- 作者：Muhammad Saeed, Dmitry Mikhaylov, Mohamed H. Alhosani, Yasser F. Al Wahedi, Rory Pilossof, Ahmed Arabi, Walid Shaaba｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42042v1

### 背景/问题
Acoustic indices are widely used as rapid proxies for biodiversity, but they summarise the distribution of sound energy rather than the species producing it and often track richness poorly. We revise and test an Acoustic Biodiversity Index (ABI) built from species-level detections.

### 方法
未在摘要中明确给出。

### 实验/数据
We first benchmarked four classifiers on a strongly labelled tropical dataset (1,216 calls, 24 classes) with recording-grouped cross-validation.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Species-level indices with explicit false-positive control, a declared regional reference pool and effort standardisation provide a more interpretable biodiversity indicator than energy-based acoustic indices.

### 29. Same Question, Different Answers: Auditing Persona-Dependent Variation in Six LLMs on Smoking-Cessation Advice

- 作者：Artin Yousefi, Aizierjiang Aiersilan, Lorien C Abroms, David A Broniatowski｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42039v1

### 背景/问题
Hundreds of millions of people now ask large language model (LLM) chatbots for health advice, which raises a question that is simple to pose and hard to answer: does everyone get the same advice? We audit six widely deployed LLMs from four providers on smoking cessation, a domain with codified clini- cal guidance and substantial public-health stakes, by putting the same four cessation questions to twelve user personas that differ in life stage, self-described expertise, and smoking history, for a total of 2,880 responses.

### 方法
Hundreds of millions of people now ask large language model (LLM) chatbots for health advice, which raises a question that is simple to pose and hard to answer: does everyone get the same advice? What the models say depends on who appears to be asking. Every model named FDA-approved prescription cessation medications less often to teen personas than to adult personas, by 32 to 67 percentage points, and in five of six models a persona presenting health- care expertise received fewer facts than a persona presenting none.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We release all 2,880 responses and the analysis code.

### 30. Berenstein-Zelevinsky polytopes for type $\mathrm{G}_{2}$

- 作者：Thomas Magnuson, Tyrrell McAllister｜年份：2026｜发布时间：2026-10-30｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.42038v1

### 背景/问题
In 2001, Berenstein and Zelevinsky presented a polyhedral model for the problem of computing tensor-product multiplicities for semi\-simple Lie algebras. We provide explicit linear equations and inequalities for Berenstein--Zelevinsky (BZ) polytopes of type-$\mathrm{G}_{2}$ Lie algebras.

### 方法
In 2001, Berenstein and Zelevinsky presented a polyhedral model for the problem of computing tensor-product multiplicities for semi\-simple Lie algebras.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also show that BZ~polytopes of type-$\mathrm{G}_{2}$ Lie algebras can fail to satisfy Ehrhart positivity, in contrast to a conjectured property of BZ~polytopes for all classical types.
