# CausalRadar 日报 - 2026-10-21

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Discount Yourself: Self-inclusive Freshness-weighted Gossip for Decentralised Learning under Client Outages

- 作者：Qiyuan Wang, Ke Xiao, Christos Anagnostopoulos｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**9.00**
- 链接：https://arxiv.org/abs/2610.28545v1

> 命中：hit_scenario=['discount']；hit_title=['discount']

### 背景/问题
Decentralised federated learning (DFL) trains personalised models on devices that average with their neighbours rather than with a central server. Real devices, however, are often offline for hours or days, and a client returning from an outage can recover only by aggregating the models its neighbourhood holds.

### 方法
Decentralised federated learning (DFL) trains personalised models on devices that average with their neighbours rather than with a central server. Real devices, however, are often offline for hours or days, and a client returning from an outage can recover only by aggregating the models its neighbourhood holds. We observe that the stalest of these models is usually the client's own, a case that existing staleness-aware rules, which discount only the models a client receives, do not address.

### 实验/数据
Real devices, however, are often offline for hours or days, and a client returning from an outage can recover only by aggregating the models its neighbourhood holds.

### 结果
On three image benchmarks and eight outage processes, including real smartphone availability traces, the lag-based members SFG-L and SFG-Cut consistently outperform decentralised federated averaging and recent age-of-information rules, and ablations show that each principle is necessary.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The analysis also explains why tuned limited merging from gossip learning is effective.

### 2. UniWALM: Unified World Action Language Model for Embodied Robot Control

- 作者：Rahul Sajnani, Diego Romeres, Mingyuan Zhang, Kai Gao, Carl Qi, Baichuan Huang, Srinath Sridhar, Dylan Randle 等｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.28626v1

> 命中：hit_scenario=['ads']

### 背景/问题
Motivated by the human ability to integrate experience across language, perception, and action, we introduce UniWALM, a unified world-action-language model that learns video, action, and language in a single shared representation, where each modality is both a conditioning signal and a supervision target. We ask: can jointly generating language enrich this shared representation, improving manipulation and supporting memory-dependent behavior?

### 方法
Motivated by the human ability to integrate experience across language, perception, and action, we introduce UniWALM, a unified world-action-language model that learns video, action, and language in a single shared representation, where each modality is both a conditioning signal and a supervision target. Unlike prior approaches that attach a reasoning or vision-language model to a video-action backbone and run them as distinct stages, UniWALM unifies all three modalities inside a single mixture-of-transformers backbone whose per-modality diffusion heads co-denoise synchronously, decoding subtask and textual memory in the same pass as action with no separate planning stage; the generated language is re-consumed on the next step, closing a language-as-memory loop without an external planner or memory bank. UniWALM consistently improves over same-backbone baselines (e.g., FastWAM) on compositional pick-and-place (MolmoSpaces) and across the memory-dependent subset of RMBench, where it reaches 34.5% without any pretrained language or reasoning model and exceeds Mem-0's keyframe-equipped setup (28.5%) using only a single anchor frame.

### 实验/数据
未在摘要中明确给出。

### 结果
UniWALM consistently improves over same-backbone baselines (e.g., FastWAM) on compositional pick-and-place (MolmoSpaces) and across the memory-dependent subset of RMBench, where it reaches 34.5% without any pretrained language or reasoning model and exceeds Mem-0's keyframe-equipped setup (28.5%) using only a single anchor frame. On a real-world Find-the-Item task, generating textual memory lifts success from 11.1% to 61.1%, while state-of-the-art VLAs stay at or below chance (<=33.3%).

### 结论/启示（面向电商发券、定价、营销算法等应用）
On a real-world Find-the-Item task, generating textual memory lifts success from 11.1% to 61.1%, while state-of-the-art VLAs stay at or below chance (<=33.3%).

### 3. Weight Placement Is Not Enough: Synchronization in Multi-Node CPU Decoding of Ternary LLMs

- 作者：Runguo Li, Dezhen Lu｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.28620v1

> 命中：hit_scenario=['ads']

### 背景/问题
Ternary LLMs read only a few gigabytes per decoded token, yet on dual-socket servers with four NUMA nodes the fastest ternary runtime we found uses less than half of the memory bandwidth. Placing each weight on the node of the thread that reads it is necessary but not enough: in a decode engine with node-local weights that reuses ik_llama.cpp's kernels, threads on two generations of Xeon servers still spend 20-48% of each token waiting at synchronization points.

### 方法
Per-thread barrier traces show that most of the wait is for the slowest threads of each node; the barriers' own latency (microseconds each, but up to 12% of the token for the smallest model) and serial per-node work are smaller parts. Where decoding is DRAM-bound, the resulting engine is 1.5-2.1x faster than ik_llama.cpp with all cores and 1.5-1.9x faster than ik_llama.cpp at its fastest thread count (3.2x and 2.8x for a small model that runs from the L3 cache), at the same accuracy and with less energy per token.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Where decoding is DRAM-bound, the resulting engine is 1.5-2.1x faster than ik_llama.cpp with all cores and 1.5-1.9x faster than ik_llama.cpp at its fastest thread count (3.2x and 2.8x for a small model that runs from the L3 cache), at the same accuracy and with less energy per token.

### 4. Adaptive Multi-Token Prediction: How far should we go?

- 作者：Emile Anand, Mohammed Rehan Parwani, Xinyuan Cao｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.28619v1

> 命中：hit_scenario=['ads']

### 背景/问题
Multi-token prediction (MTP) can accelerate language-model decoding by drafting several tokens and verifying them in a single target-model pass. However, the best speculation horizon changes with context: longer drafts offer greater amortization when reliable, but can waste compute on suffixes discarded after a rejection.

### 方法
Multi-token prediction (MTP) can accelerate language-model decoding by drafting several tokens and verifying them in a single target-model pass. Across five draft-target pairings built on Llama-3.1-8B-Instruct with Medusa heads, Meta's MTP models, and Qwen3-4B-Inst-2507-MTP, evaluated on AIME 2025 and GSM8K, AMTP decodes up to 4.1x faster than standard decoding and matches or outperforms the fixed window in 8 of 10 settings, with throughput gains of up to 10%.

### 实验/数据
We therefore formulate horizon selection as an online control problem, using verification feedback to learn how far the draft can be trusted in each context, and introduce Adaptive Multi-Token Prediction (AMTP): a lightweight controller that requires no retraining and leaves the exact verifier unchanged. Theoretically, we show that any online learner's prediction error translates into throughput regret against the best horizon for each context, and in turn into a bound on wall-clock completion time. With online gradient descent, this regret is sublinear.

### 结果
Across five draft-target pairings built on Llama-3.1-8B-Instruct with Medusa heads, Meta's MTP models, and Qwen3-4B-Inst-2507-MTP, evaluated on AIME 2025 and GSM8K, AMTP decodes up to 4.1x faster than standard decoding and matches or outperforms the fixed window in 8 of 10 settings, with throughput gains of up to 10%.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Across five draft-target pairings built on Llama-3.1-8B-Instruct with Medusa heads, Meta's MTP models, and Qwen3-4B-Inst-2507-MTP, evaluated on AIME 2025 and GSM8K, AMTP decodes up to 4.1x faster than standard decoding and matches or outperforms the fixed window in 8 of 10 settings, with throughput gains of up to 10%.

### 5. Evolving Agent Interfaces

- 作者：Saaket Agashe, Yuzhe Yang, Gonzalo Gonzalez-Pumariega, Bhuvan Chandra Koduru, Chih-Lun Li, Jiachen Yang, Ang Li, Xin Eric Wang｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.28601v1

> 命中：hit_scenario=['ads']

### 背景/问题
Computer-use agents are limited by the interfaces humans give them. An agent may type a spreadsheet cell by cell when a single line of code would do, or print all two thousand lines of a file through a shell to find one function.

### 方法
Both the interfaces and the knowledge of when to use each are built by hand, which cannot keep pace with new applications, workflows, and models. On OSWorld V2, Agent S4, with Qwen3.8-27B and the evolved repository of interfaces, sets a new state of the art in open-source computer-use agents, reaching 21.3% binary score, 3.8 times the same model with fixed interfaces. On ScienceBoard, the evolved interfaces improve the success rate from 41.4% to 58.6% with the same model.

### 实验/数据
未在摘要中明确给出。

### 结果
On ScienceBoard, the evolved interfaces improve the success rate from 41.4% to 58.6% with the same model. These results suggest that useful interfaces can be evolved from experience, making autonomous interface design a source of improvement complementary to advances in models and harnesses.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We open-source our code at https://github.com/simular-ai/agent-s.

### 6. Dynamic Distances Without Matrix Inverse

- 作者：Jan van den Brand, Adam Karczmarz, Aryan Patel｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2610.28573v1

> 命中：hit_scenario=['ads']

### 背景/问题
We study the fully dynamic exact distance problem in unweighted directed graphs, where the graph undergoes edge insertions and deletions, and the distance between two query vertices must be reported. Under the combinatorial Boolean matrix multiplication conjecture, any subquadratic-time algorithm for this problem must use algebraic techniques.

### 方法
This purely algebraic approach to dynamic distances leads to the fastest dynamic distance algorithm with $O(n^{1.58})$ update time.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
This gives the first subquadratic dynamic algorithm for the Frobenius normal form and characteristic polynomial for generic matrices.

### 7. VLM-Guided Contact Retargeting and Generative Partner Modeling for Humanoid-Human Interaction

- 作者：Yuto Shibata, Kotaro Amaya, Kashu Yamazaki, Lalit Jayanti, Yoshimitsu Aoki, Mariko Isogawa, Katerina Fragkiadaki｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.28523v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Humanoid-human interaction requires robots to operate under severe partial observability: during close physical contact, the human partner is occluded, truncated, or outside the robot's field of view, causing pose estimation to fail and often necessitating external tracking or privileged human state. At the same time, heavy mutual occlusions introduce errors into the human-human motion-capture data used for learning.

### 方法
We present REACT, a framework for learning deployable humanoid-human interaction policies from human-human demonstrations. First, a VLM-guided contact modeling and retargeting pipeline identifies semantically meaningful contacts and transfers them onto humanoid-human geometry while preserving interaction structure. To address severe partial observability, we introduce generative partner-state modeling objectives that predict partner motion from occluded egocentric views.

### 实验/数据
Humanoid-human interaction requires robots to operate under severe partial observability: during close physical contact, the human partner is occluded, truncated, or outside the robot's field of view, causing pose estimation to fail and often necessitating external tracking or privileged human state. At the same time, heavy mutual occlusions introduce errors into the human-human motion-capture data used for learning. We evaluate REACT in simulation and on a real Unitree G1 humanoid across five contact-rich interactions.

### 结果
Semantic contact modeling substantially improves preservation of demonstrated interactions, while generative partner-state modeling improves contact recall on four of five interactions, most under heavy occlusion.

### 结论/启示（面向电商发券、定价、营销算法等应用）
On real hardware, REACT performs all five interactions using onboard sensing alone.

### 8. Shell-model description of collective deformation variables $β$ and $γ$ in $^{164-188}$Hf nuclei

- 作者：Carlos E. Vargas｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.28509v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Symmetry-based models, such as the pseudo-SU(3) scheme, have proved to be highly useful tools for describing the low-energy structure of nuclei in the rare-earth region. This model is employed to study the evolution of the collective deformation variables beta and gamma in the ground state (0+) along the isotopic chain 164-188Hf.

### 方法
Symmetry-based models, such as the pseudo-SU(3) scheme, have proved to be highly useful tools for describing the low-energy structure of nuclei in the rare-earth region. This model is employed to study the evolution of the collective deformation variables beta and gamma in the ground state (0+) along the isotopic chain 164-188Hf. In agreement with experimental data, the maximum deformation beta occurs at N = 100, although the model predicts values that are about 20% smaller.

### 实验/数据
In agreement with experimental data, the maximum deformation beta occurs at N = 100, although the model predicts values that are about 20% smaller.

### 结果
The absence of nucleons in the intruder sector is the most significant limitation of the model.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The absence of nucleons in the intruder sector is the most significant limitation of the model.

### 9. Improved Approximation for Unsplittable Capacitated Vehicle Routing Using Quota Trees

- 作者：Zhenyu Wang｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2610.28501v1

> 命中：hit_abstract=['CATE']

### 背景/问题
In the Unsplittable Capacitated Vehicle Routing Problem (UCVRP), we are given a set $V$ of $n$ clients with normalized demands $d_v \in (0,1]$, a depot $r$, a unit vehicle capacity, and symmetric metric travel costs $c$ on $V \cup \{r\}$. We seek a collection of routes of minimum total cost that start and end at $r$, serve each client's entire demand on a single route, and respect the unit capacity constraint $\sum_{v \in V(R)} d_v \le 1$ on every route $R$, where $V(R)$ denotes the clients served by $R$.

### 方法
This models deliveries from a common depot in which each customer's order must be delivered in a single trip.

### 实验/数据
未在摘要中明确给出。

### 结果
The classical $3.5$-approximation has been improved through several recent advances; in particular, Zhao and Xiao (2026) recently obtained a $(2+\ln 2+\varepsilon)$-approximation.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The remaining clients are served by partitioning a tour constructed using weighted graphic matroid parity.

### 10. Constraints on Millimeter-wave Extragalactic Transient Populations from 4 Years of SPT-3G data

- 作者：S. Guns, C. Tandoi, D. Anbajagane, E. Anderes, A. J. Anderson, B. Ansarinejad, M. Archipley, L. Balkenhol 等｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28633v1

### 背景/问题
Wide-field cosmic microwave background (CMB) instruments have reached sufficient sensitivity and cadence to conduct untargeted millimeter-wave searches for astronomical transients. To date, such searches have primarily discovered stellar flares, while extragalactic detections remain limited to a few flaring blazars and active galactic nuclei.

### 方法
At timescales under one week, predicted detections are dominated by flares from reverse shocks in long-duration GRBs, with some benchmark models predicting rates of ~10 detections per year for the SPT-3G camera on the South Pole Telescope. We update previous simulations by incorporating a more realistic model of the SPT-3G sensitivity, observing cadence, and detection algorithm, resulting in nearly a factor of two improvement in detection sensitivity compared to prior estimates. The most readily detectable model we consider is a 10^52 erg "dirty" GRB with Gamma = 50, whose population we constrain to f_RS <0.09 and N_all-sky <120 bursts/year.

### 实验/数据
Wide-field cosmic microwave background (CMB) instruments have reached sufficient sensitivity and cadence to conduct untargeted millimeter-wave searches for astronomical transients. In contrast, recent simulations suggest that current and future CMB experiments should detect a few to dozens of extragalactic transients per year from sources including gamma-ray bursts (GRBs), tidal disruption events, and fast blue optical transients. We update previous simulations by incorporating a more realistic model of the SPT-3G sensitivity, observing cadence, and detection algorithm, resulting in nearly a factor of two improvement in detection sensitivity compared to prior estimates.

### 结果
We update previous simulations by incorporating a more realistic model of the SPT-3G sensitivity, observing cadence, and detection algorithm, resulting in nearly a factor of two improvement in detection sensitivity compared to prior estimates.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The most readily detectable model we consider is a 10^52 erg "dirty" GRB with Gamma = 50, whose population we constrain to f_RS <0.09 and N_all-sky <120 bursts/year.

### 11. Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets

- 作者：Jad Yammine, Malek Wahidi, Abrar Anwar, Yan Chang, Mihir Acharya, Anthony Rizk｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28624v1

### 背景/问题
Warehouse robot fleets continuously observe operational conditions, but preserving these observations as reusable semantic memory incurs substantial computation, communication, and storage costs. For example, explaining recurring aisle blockages can require reviewing video from multiple robots across several shifts.

### 方法
We present IndustrialRemembr, a shared spatiotemporal memory system that extends NVIDIA ReMEmbR to robot fleets and reduces server-side computation by generating scene descriptions only on demand. The encoding models are re-used to detect people in image patches, zeroing them out to support PII abstraction for GDPR-compliant deployments. This design eliminates caption generation at write time, while cached-token decoding reproduces the unsplit model's output in all 450 tested decodes.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
This design eliminates caption generation at write time, while cached-token decoding reproduces the unsplit model's output in all 450 tested decodes.

### 12. Planning under Noise with Neural Operators

- 作者：Michael Chen, Hong Chul Nam, Xi Deng, Anima Anandkumar｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28623v1

### 背景/问题
Planning under uncertain control execution noise requires reliable feedback policies across diverse environments. We introduce Planning Under Noise (PUN), a neural operator that learns noise-aware value fields for planning in unseen geometries.

### 方法
未在摘要中明确给出。

### 实验/数据
We introduce Planning Under Noise (PUN), a neural operator that learns noise-aware value fields for planning in unseen geometries. Building on an established screened-Poisson formulation of stochastic optimal control, we address two challenges: specifying boundary conditions that support navigation across varying geometries and efficiently computing fields with reliable gradients. PUN amortizes this computation by learning geometry-to-field mappings from noisy, partially converged Monte Carlo labels, avoiding expensive convergence for every training example.

### 结果
Across four noise levels, PUN matches or outperforms all compared planners, achieving 95-100% success on the 4D replanning benchmark while maintaining the lowest runtime.

### 结论/启示（面向电商发券、定价、营销算法等应用）
At the highest tested noise level in 4D, PUN achieves 10.7-60.6% relative gains in success rate over other methods while running 3.29-32.15 times faster.

### 13. MindView: Benchmarking Generative Multi-View Spatial Intelligence

- 作者：Yanbo Wang, Siqi Luo, Siyu Zhang, Chenming Zhu, Wenzhao Zheng, Qian Yu, Juncheng Yan, Bin Fu 等｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28622v1

### 背景/问题
Spatial intelligence has recently been assessed through generative tasks such as spatially grounded image editing, yet language-guided generation of spatially consistent views from partial multi-view observations remains underexplored. We introduce MindView, a benchmark for generative multi-view spatial intelligence with 1,500 samples from 513 scenes across three indoor datasets.

### 方法
These findings motivate us to investigate whether task-specific supervision can improve target-view generation and whether models can use additional multi-view evidence effectively. Beyond these generation gains, the fine-tuned model also yields higher scores on three spatial-understanding benchmarks without training on their annotations, suggesting that learning to generate spatially grounded views may benefit spatial understanding. To improve evidence utilization under expanded context, we propose MindCue, a training-free spatial evidence selector guided by a target-view hypothesis.

### 实验/数据
We introduce MindView, a benchmark for generative multi-view spatial intelligence with 1,500 samples from 513 scenes across three indoor datasets. We therefore fine-tune BAGEL on the MindView training dataset, improving its overall score by 24.3 points and yielding gains across all seven MindView tasks.

### 结果
Evaluation of eleven generators reveals substantial room for improvement on MindView. These findings motivate us to investigate whether task-specific supervision can improve target-view generation and whether models can use additional multi-view evidence effectively. To improve evidence utilization under expanded context, we propose MindCue, a training-free spatial evidence selector guided by a target-view hypothesis.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Overall, MindView provides a concrete testbed for generative multi-view spatial intelligence.

### 14. Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning

- 作者：Zebin Xing, Yuhang Zheng, Yupeng Zheng, Yichen Zhang, Zichen Li, Shangqing Zhou, Yujie Zang, Yuchen Liu 等｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28613v1

### 背景/问题
Evaluating and post-training robot policies through physical interaction is costly and difficult to scale, motivating action-conditioned world models as interactive simulators. However, visually plausible predictions can misrepresent contact dynamics, providing unreliable feedback for policy evaluation and learning.

### 方法
Evaluating and post-training robot policies through physical interaction is costly and difficult to scale, motivating action-conditioned world models as interactive simulators. We introduce PhysCanvas, a state-consistent visuo-tactile world model for contact-rich robot manipulation. Our consistency-aware post-training uses the frozen Scene Reward Model, Modality Reward Model, and State Reward Model to supervise scene preservation, visual-tactile compatibility, and agreement with real task outcomes.

### 实验/数据
未在摘要中明确给出。

### 结果
Across four real-world manipulation tasks, when policies are rolled out in the world model, State Reward Model supervision increases the arithmetic mean of task-wise Pearson correlations between world-model and real-world success rates from 0.602 to 0.885. Policy post-training in the reward-guided world model further increases $π_{0.5}$'s mean real-world success rate from a 59.1% SFT baseline to 70.8%.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Project page: https://zebinx.github.io/PhysCanvas_HomePage/.

### 15. Resolving the extended interstellar medium of infrared galaxies I. Polycyclic aromatic hydrocarbon emission

- 作者：C. M. Lofaro, T. Diaz-Santos, L. Armus, V. Charmandaris, T. Lai, M. Pereira-Santaella, J. McKinney, R. Fernandez-Aranda 等｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28599v1

### 背景/问题
We investigate spatial variations in polycyclic aromatic hydrocarbon (PAH) properties and photoelectric heating efficiency in 67 nearby luminous infrared galaxies from the Great Observatories All-sky LIRG Survey (GOALS). Using mid-infrared spectroscopy from Spitzer and far-infrared cooling-line maps from Herschel, we extract spectra in concentric annuli and matched aperture grids out to about 14 kpc.

### 方法
Beyond about 5 kpc, PAHs become more ionized and approach the starburst locus as the radiation field weakens.

### 实验/数据
Strong active galactic nucleus (AGN) systems show more neutral PAHs and harder radiation fields in their nuclear and inner regions. Beyond about 5 kpc, PAHs become more ionized and approach the starburst locus as the radiation field weakens. Photoelectric heating efficiency increases with radius in both starburst and AGN-hosting galaxies as the radiation field weakens.

### 结果
Photoelectric heating efficiency increases with radius in both starburst and AGN-hosting galaxies as the radiation field weakens.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results provide quantitative, spatially resolved constraints on the extent of AGN effects on dust properties in a population of luminous infrared galaxies.

### 16. Resolving the extended interstellar medium of infrared galaxies II. Fine-structure line emission

- 作者：C. M. Lofaro, T. Diaz-Santos, L. Armus, V. Charmandaris, T. Lai, M. Pereira-Santaella, J. McKinney, R. Fernandez-Aranda 等｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28597v1

### 背景/问题
We investigate how star formation and active galactic nuclei (AGNs) shape the ionized and neutral interstellar medium in 67 nearby luminous and ultraluminous infrared galaxies from the Great Observatories All-sky LIRG Survey (GOALS). Combining mid-infrared (MIR) spectral mapping from the Spitzer Infrared Spectrograph with far-infrared (FIR) spectroscopy from the Herschel Photodetector Array Camera and Spectrometer, we measure fine-structure emission lines in aperture grids extending to projected galactocentric distances of about 14 kpc.

### 方法
We compare the measurements with CLOUDY photoionization models to constrain the ionization parameter, hydrogen density, stellar age, and metallicity.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Together with Paper I, they provide a benchmark for spatially resolved studies of gas and dust in starbursts and AGN-hosting galaxies.

### 17. Entanglement Distribution in Quantum Switch Networks: Memory Limits and Achievability

- 作者：Lei Hu, Alptug Aytekin, Stavros Mitrolaris, Mohamed Nomeir, Subhankar Banerjee, Sennur Ulukus, Saikat Guha｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28596v1

### 背景/问题
We study the minimum persistent memory required to distribute a graph state through a quantum switch. Specifically, consider a central switch that assists $n$ remote users in distributing a graph state, using independently generated user-switch Bell pairs.

### 方法
Recently, new protocols have been proposed to reduce this storage overhead by processing and releasing some switch qubits before all Bell links are available. Remarkably, this optimal protocol can provide substantial memory reductions over existing heuristic approaches. Finally, the same stabilizer-transition framework also provides a direct forward construction for sequential graph-state generation using the minimum number of quantum emitters, equal to the maximum of the height function.

### 实验/数据
We then develop an online stabilizer-transition protocol that attains this limit, which can be implemented in polynomial time in the number of qubits $n$.

### 结果
Moreover, the local-cover method in the state-of-the-art Piecemaker protocol is computationally expensive for general target graphs.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, the same stabilizer-transition framework also provides a direct forward construction for sequential graph-state generation using the minimum number of quantum emitters, equal to the maximum of the height function.

### 18. What Do RTL Repair Benchmarks Actually Measure?

- 作者：Yeyin Eva Zhu, Rishabh Ranawat｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28595v1

### 背景/问题
RTL repair benchmarks should measure whether a model can fix broken RTL given a specification. To this end, we construct and hash-bind RTLRepairDataset, 5,784 (broken, fixed) training pairs; RTLRepairBench, 459 held-out cases with 374 syntactic and 85 behavioral mutations; and an evaluation harness supporting simulation and formal equivalence.

### 方法
RTL repair benchmarks should measure whether a model can fix broken RTL given a specification. We then use this infrastructure to identify two measurement confounds. Second, on 274 mined model failures, the specification-only minus specification-conditioned recovery point estimate ranges from -8.5 to +18.3 percentage points across six models.

### 实验/数据
To this end, we construct and hash-bind RTLRepairDataset, 5,784 (broken, fixed) training pairs; RTLRepairBench, 459 held-out cases with 374 syntactic and 85 behavioral mutations; and an evaluation harness supporting simulation and formal equivalence. First, simulation and formal scoring give opposite signs for the apparent effect of providing a specification in one evaluated cohort; reset-aware rescoring attributes almost all of the simulation-formal disagreement to reset and first-cycle comparison semantics.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We release the benchmark, the training set, construction code, sanitized aggregate evidence, and reproduction materials at https://github.com/Evaaaz/RTLRepairBench.

### 19. Learning the 4D World through Point Trajectory Forecasting

- 作者：Byungwoo Jeon, Sunghwan Hong, Dohyeon Kim, Jonghoon Lee, Jungwoo Park, Inhee Lee, Doosan Baek, Jinil Kim 等｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28594v1

### 背景/问题
Reliable multi-view forecasting requires videos from different cameras to describe the same evolving 3D scene. To this end, we introduce Video-Point Model (VPM), a world model that conditions on multi-view video histories and a language instruction to jointly forecast future videos from arbitrary viewpoints and the 3D trajectories of persistent scene points.

### 方法
To this end, we introduce Video-Point Model (VPM), a world model that conditions on multi-view video histories and a language instruction to jointly forecast future videos from arbitrary viewpoints and the 3D trajectories of persistent scene points. We extend a pretrained world model with camera-conditioned multi-view processing that integrates complementary observations across cameras, and add a trajectory head that predicts how physical points move through time. On VP-WorldBench and existing 4D generation benchmarks, point supervision improves both video fidelity and 3D motion accuracy over a video-only counterpart, and in simulated and real-robot experiments, it also raises the manipulation success of the action-enabled model.

### 实验/数据
To support training and evaluation, we build VPM-Data, a simulation corpus pairing synchronized multi-view videos with persistent point trajectories, and VP-WorldBench, a forecasting benchmark spanning simulated and real environments. On VP-WorldBench and existing 4D generation benchmarks, point supervision improves both video fidelity and 3D motion accuracy over a video-only counterpart, and in simulated and real-robot experiments, it also raises the manipulation success of the action-enabled model.

### 结果
On VP-WorldBench and existing 4D generation benchmarks, point supervision improves both video fidelity and 3D motion accuracy over a video-only counterpart, and in simulated and real-robot experiments, it also raises the manipulation success of the action-enabled model.

### 结论/启示（面向电商发券、定价、营销算法等应用）
On VP-WorldBench and existing 4D generation benchmarks, point supervision improves both video fidelity and 3D motion accuracy over a video-only counterpart, and in simulated and real-robot experiments, it also raises the manipulation success of the action-enabled model.

### 20. Correcting topographic artifacts in three-dimensional ToF-SIMS: A practical guide from data-only reconstruction to correlative AFM

- 作者：Jacob Shusterman, Anton V. Ievlev｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28593v1

### 背景/问题
Three-dimensional time-of-flight secondary ion mass spectrometry (3D ToF-SIMS) builds chemical volumes by stacking images acquired between sputter cycles. Standard reconstruction assumes a flat starting surface and a single sputter rate, so samples with topography, or with layers that sputter at different rates, yield distorted interface positions and depth scales.

### 方法
All three are applied to a model Pt/TaOx/Ta/Pt/Ti crossbar memristor device measured with in situ SIMS/AFM at ten stages, together with the data preparation they share.

### 实验/数据
We group the available corrections by the information they need: the SIMS data alone, atomic force microscopy (AFM) topography before and after the profile, or AFM topography also at intermediate stages. All three are applied to a model Pt/TaOx/Ta/Pt/Ti crossbar memristor device measured with in situ SIMS/AFM at ten stages, together with the data preparation they share. The data-only correction requires no additional instrumentation and restores relative topography, but its depth scale depends on nominal layer thicknesses and remains unconstrained below the last calibrated interface.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
A decision flowchart and a checklist help readers choose, validate and report a correction.

### 21. PaPi: Parallel Picard-Duhamel Integration for Fast Neuro-Spectral Architectures

- 作者：Arthur Bizzi, Márcio Marques, Kleyton Da Costa, Vitor Balestro, Tiago Novello, João M. Pereira, Daniel Yukimura｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28591v1

### 背景/问题
Neuro-spectral architectures (NeuSA) are a class of physics-informed neural networks (PINNs) that have proven effective for solving time-dependent PDEs in the frequency domain. However, training and inference often rely on costly numerical integration of the learned vector field, typically using sequential Runge-Kutta time stepping, which limits temporal parallelism.

### 方法
未在摘要中明确给出。

### 实验/数据
However, training and inference often rely on costly numerical integration of the learned vector field, typically using sequential Runge-Kutta time stepping, which limits temporal parallelism. We introduce PaPi, an integration scheme inspired by weakly nonlinear flows that enables time-Parallel inference through exponential integration and a Duhamel-Picard scheme. Experiments show that PaPi accelerates training and inference by up to two orders of magnitude, achieving training times of under one second for low-dimensional PDE learning problems, while maintaining competitive predictive accuracy.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Experiments show that PaPi accelerates training and inference by up to two orders of magnitude, achieving training times of under one second for low-dimensional PDE learning problems, while maintaining competitive predictive accuracy.

### 22. Two $\operatorname{ReLU}$ Layers is All You Need

- 作者：Florestan Brunck, Christoph Hertrich, Kilian Ruess, Jack Stade, Amir Yehudayoff｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28587v1

### 背景/问题
We prove that every $\operatorname{ReLU}$ network can be exactly simulated by a $\operatorname{ReLU}$ network with two hidden layers. We present two proofs: one that is based on fillings in homological algebra and a direct combinatorial proof.

### 方法
We present two proofs: one that is based on fillings in homological algebra and a direct combinatorial proof.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We present two proofs: one that is based on fillings in homological algebra and a direct combinatorial proof.

### 23. Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation

- 作者：Shu Zhao, Tan Yu｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28586v1

### 背景/问题
Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable, so recent methods keep training inside that region, through episode-length curricula, teacher-guided turns, prefix replay, or teacher intervention where the two disagree.

### 方法
We propose Rollout-to-Scorer Distillation (R2S), which repairs the scorer before distillation by mining high-disagreement states from the untrained student, running teacher takeovers from them, keeping the states where enough takeovers pass a reward-free check such as consensus or an LLM judge, and fine-tuning the teacher to give its takeover-informed scores on every assistant token from the divergence turn onward, without the takeover in context.

### 实验/数据
未在摘要中明确给出。

### 结果
Across three environments, two teachers and four students, R2S outperforms three state-of-the-art agentic-OPD methods in all twelve teacher-student-environment cells, by 12.8 success points on average over the best of them in each cell.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Project page: https://tree-shu-zhao.github.io/r2s/.

### 24. Birthday Estimators Are Uniformly Optimal for Renyi Entropy

- 作者：Maciej Skórski｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28581v1

### 背景/问题
Collisions are a basic probe of unknown distributions, used for testing and for counting substructures in graphs, and they underlie Rényi entropy, a fundamental measure of uncertainty with applications in cryptography, machine learning, physics, and biology. Motivated by this, we study the natural birthday estimator.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our concentration bound rests on a sensitivity analysis of collision count, and the matching lower bound on a sharp analysis of detecting a hidden spike in a plateau distribution.

### 25. A sub-Earth-sized TESS planet candidate in the nearby M-dwarf binary GJ 774, most likely orbiting GJ 774 A (TIC 351339274)

- 作者：Jaden Tripp｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28575v1

### 背景/问题
Small planets transiting the nearest M dwarfs are the terrestrial planets most accessible to detailed characterisation. We report a sub-Earth-sized transiting planet candidate in the wide (17.6") M-dwarf binary GJ 774 at 12.86 pc, most likely orbiting the M2.5 primary GJ 774 A (TIC 351339274).

### 方法
Conditional on a point source at A or at B, the joint host model gives P(A)=0.59-0.97 (0.97 for the native target-pixel baseline). Over all sectors the PRF photometry is consistent with A, but in the out-of-sample 2026 data 40% of the deficit appears at B's position, an unexplained 2-3 sigma (PSF-model and depth dependent) tension with host A.

### 实验/数据
The 2026 data, which entered neither the SPOC search nor our selection, show it at the ephemeris predicted from 2019-2023 data (304 +/- 43 ppm; none of 10^5 phase-scrambled versions of the 2026 data is as deep). Over all sectors the PRF photometry is consistent with A, but in the out-of-sample 2026 data 40% of the deficit appears at B's position, an unexplained 2-3 sigma (PSF-model and depth dependent) tension with host A.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
It is not validated; resolved ground-based photometry of the pair would test host B directly.

### 26. Vanishing Uniform Turán Densities: Characterization and Jumps

- 作者：Hao Lin, Jie Ma, Wenling Zhou｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28574v1

### 背景/问题
Uniform Turán density problems ask for the minimum density threshold that guarantees a copy of a fixed 3-uniform hypergraph $F$ in every sufficiently large 3-uniform hypergraph whose edges are uniformly distributed. This line of research was initiated by Erdős and Sós in the 1980s, who introduced the notion of \emph{vertex-set Turán density} $π_{vvv}(F)$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Together with existing results, these findings complete the picture for all three notions of uniform Turán density at zero.

### 27. Continual Concept Personalization in Diffusion Models via Residual-Space Adaptation

- 作者：Yuzhi Liu, Enis Simsar, Giulia Lanzillotta, Thomas Hofmann｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28567v1

### 背景/问题
Text-to-image personalization aims to equip pretrained diffusion models with the ability to learn user-specific concepts from only a few reference images. Existing methods, however, typically train each concept independently or assume that all concepts are available simultaneously.

### 方法
Text-to-image personalization aims to equip pretrained diffusion models with the ability to learn user-specific concepts from only a few reference images. In practical applications, concepts often arrive sequentially, requiring models to continually learn new subjects, objects, or styles while minimizing interference with previously acquired concepts. We address this continual concept personalization setting by extending residual-space adaptation to the stochastic adaptation process of pretrained diffusion models.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Restricting adaptation to the identified layers by our method preserves nearly the same performance while reducing the number of trainable parameters by up to 72\%, demonstrating that residual-space dynamics can identify the layers that contribute most to continual concept personalization and directly guide more parameter-efficient adaptation.

### 28. Differentiable powder X-ray diffraction enables analysis of evolving structures

- 作者：Xiangyu Yin, Nina Andrejevic, Hemant Sharma, Ming Du, Aileen Luo, Michael Prince, Burak Guzelturk, Xiaoyi Zhang 等｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28564v1

### 背景/问题
Operando and in-situ experiments extend powder X-ray diffraction (PXRD) to materials that evolve during experiments, producing series of hundreds or thousands of patterns. Such series are commonly refined one pattern at a time, so weak signals give noisy structural trajectories.

### 方法
Parametric refinement instead fits a shared model to all patterns, but with most existing programs, changing the model or fitting it efficiently remains challenging. diffPXRD calculates derivatives by automatic differentiation, so a shared model can be changed without new derivative code. In an operando cathode series, a shared lattice model can reduce lattice-parameter variability by 68.4% when 10% of the photon counts are retained.

### 实验/数据
Operando and in-situ experiments extend powder X-ray diffraction (PXRD) to materials that evolve during experiments, producing series of hundreds or thousands of patterns.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also show shared models can describe the precipitation and dissolution of Li2S and reconstruct collective atomic displacements in Ca3Ti2O7.

### 29. Strong Convergence of Fully Discrete Tamed Euler Approximations for Time-Changed Stochastic Delay Differential Equations

- 作者：Ruchun Zuo, Qian Guo｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28552v1

### 背景/问题
We establish the strong convergence of a fully discrete equidistant tamed Euler--Maruyama (ETEM) method for time-changed stochastic delay differential equations (TCSDDEs) with state-dependent $\mathrm{d}t$ drifts. A coupled one-sided condition on the subordinator-driven drift and diffusion allows superlinear coefficients with polynomial growth in both the current and delayed states.

### 方法
未在摘要中明确给出。

### 实验/数据
Numerical experiments illustrate convergence for nonautonomous and multidimensional superlinear delay equations, as well as delay equations with low-regularity time dependence.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Numerical experiments illustrate convergence for nonautonomous and multidimensional superlinear delay equations, as well as delay equations with low-regularity time dependence.

### 30. Cutoff profile for the balanced generalized Bernoulli--Laplace model

- 作者：Ritesh Goenka, Kyprianos-Iason Prodromidis｜年份：2026｜发布时间：2026-10-20｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2610.28550v1

### 背景/问题
We study the balanced generalized Bernoulli--Laplace model introduced by Goenka, Hermon, and Schmid (2025) and establish a Gaussian cutoff profile under spectral conditions satisfied by all reversible chains and the cyclic shift chain. Our method adapts the approach of Olesker-Taylor and Schmid (2026) for the two-urn model, combining concentration around a deterministic trajectory before the cutoff window with an Ornstein--Uhlenbeck approximation near equilibrium.

### 方法
We study the balanced generalized Bernoulli--Laplace model introduced by Goenka, Hermon, and Schmid (2025) and establish a Gaussian cutoff profile under spectral conditions satisfied by all reversible chains and the cyclic shift chain. Our method adapts the approach of Olesker-Taylor and Schmid (2026) for the two-urn model, combining concentration around a deterministic trajectory before the cutoff window with an Ornstein--Uhlenbeck approximation near equilibrium. We also give an instance of this model that exhibits cutoff but has no limit profile.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Further, we determine the mixing time up to an additive constant for every irreducible instance of the model, identifying a $\log \log n$ correction governed by the largest Jordan block size corresponding to the slowest decaying modes.
