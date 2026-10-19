# CausalRadar 日报 - 2026-10-19

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. The Restricted Inverse Optimal Value Problem on Shortest Path under $l_\infty$ Norm on Trees

- 作者：Qiao Zhang, Ying Wang, Xiao Li, Junhua Jia, Xiucui Guan, Panos M. Pardalos｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**8.74**
- 链接：https://arxiv.org/abs/2610.23710v1

> 命中：hit_scenario=['pricing']；hit_abstract=['CATE', 'pricing']

### 背景/问题
We study the restricted inverse optimal value problem on shortest paths under the weighted $l_\infty$ norm on trees (RIOVSPT$_\infty$): adjust edge weights at minimum worst-link cost so that the shortest root--leaf path is lower-bounded by a given value $D$, a restriction on a prescribed path $P_0$. Unlike the $l_1$ version minimizing total adjustment cost, the $l_\infty$ objective controls the worst link, the criterion relevant in bandwidth pricing.

### 方法
未在摘要中明确给出。

### 实验/数据
Experiments on synthetic trees agree with a linear programming baseline and illustrate the two algorithms' distinct runtime profiles.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Experiments on synthetic trees agree with a linear programming baseline and illustrate the two algorithms' distinct runtime profiles.

### 2. Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs

- 作者：Sam Partee, River Stevens, Thierry Damiba, Valerie Fanelle｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**8.74**
- 链接：https://arxiv.org/abs/2610.23707v1

> 命中：hit_scenario=['recommendation']；hit_title=['recommendation']

### 背景/问题
A multi-step agent task fails when a single tool it needs is missing, yet the tools an agent may need are too many to list: the roughly 8,200 tools on the platform we study have definitions that together exceed the context window of any model we evaluate. We present Tool Recommendation, a deployed system that gives an agent all of them, hundreds of times more than a typical MCP server exposes, through a fixed interface of three tools.

### 方法
A multi-step agent task fails when a single tool it needs is missing, yet the tools an agent may need are too many to list: the roughly 8,200 tools on the platform we study have definitions that together exceed the context window of any model we evaluate. We present Tool Recommendation, a deployed system that gives an agent all of them, hundreds of times more than a typical MCP server exposes, through a fixed interface of three tools.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In paired multi-step workflows, its first recommendation covered every required tool in 93% of Codex sessions, and against a fixed list of 100 tools it cut input tokens by 17% with Codex and 40% with Claude Code and the total bill in all 14 runs, by up to 40%, with no change in task completion.

### 3. On the Power of Alternating Local Certification with Constant-Size Certificates

- 作者：Pedro Montealegre, Martín Ríos-Wilson, Jukka Suomela, Guillaume Theyssier｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**8.24**
- 链接：https://arxiv.org/abs/2610.23694v1

> 命中：hit_title=['CATE']；hit_abstract=['CATE']

### 背景/问题
We study alternation hierarchies for distributed decision in anonymous networks with constant-size certificates. A prover and a disprover alternately assign certificates to nodes over a constant number of rounds, after which each node decides whether to accept based on its own input and the certificates observed in its neighborhood.

### 方法
We consider three models: SET, where nodes observe only the set of certificate sequences of their neighbors; MULTISET, where multiplicities are also visible; and PORTS, where neighbors can additionally be distinguished by local port numbers. Despite their severe restrictions, these models are remarkably expressive: LEADER belongs to the third level of SET.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Furthermore, over unbounded input alphabets, PORTS cannot verify that every node has been given the correct network size.

### 4. Agentic AI for Heterogeneous System Design Across Chip, Scale-Up, and Scale-Out Domains

- 作者：Murali Emani, Kashyap R Manjusha｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**4.74**
- 链接：https://arxiv.org/abs/2610.23724v1

> 命中：hit_scenario=['ads']

### 背景/问题
The design space of modern AI/HPC systems has expanded rapidly across compute architectures, including GPUs, dataflow processors, and RISC-V accelerators; memory tech- nologies, including HBM, GDDR, and SRAM; and interconnects such as NVLink, UALink, Infinity Fabric, InfiniBand, Slingshot, and Ultra Ethernet. No single architecture is optimal across LLM training, LLM serving, and AI-coupled HPC workloads, while the resulting combinatorial design space is too large for manual exploration.

### 方法
We present ArchAgent, a hierarchical multi- agent framework in which an LLM-based planner decomposes system design into chip, scale-up, and scale-out subproblems, each handled by specialist agents. A deterministic analytical evaluator closes the loop, ensuring that all performance estimates are derived from analytical models rather than generated by the LLM.

### 实验/数据
The design space of modern AI/HPC systems has expanded rapidly across compute architectures, including GPUs, dataflow processors, and RISC-V accelerators; memory tech- nologies, including HBM, GDDR, and SRAM; and interconnects such as NVLink, UALink, Infinity Fabric, InfiniBand, Slingshot, and Ultra Ethernet.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
On a mixed AI+HPC workload under a 1 MW power budget, ArchAgent discovers heterogeneous designs that achieve a 1.93x weighted geometric mean speedup over a homogeneous GPU baseline, while requiring only 18 evaluations compared with 100 evaluations for hill climbing, which achieves 1.65x speedup.

### 5. Waiting Buys Exactly Two Moments: Endogenous Identification in Prediction-Driven Allocation

- 作者：Rama AlHamidi, Rasul Khanbayov, Erchin Serpedin, Hasan Kurban｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.23830v1

> 命中：hit_abstract=['CATE']

### 背景/问题
A planner with a fixed budget of preventive help must decide whom to help and when. Waiting reveals risk but removes intervention opportunities as higher-risk individuals leave first.

### 方法
We characterize this tradeoff under repeated noisy signals and risk-dependent attrition: in the canonical model, a length-$τ$ observation prefix identifies exactly the latent risk moments $m_j=\mathbb E[p^j]$ for $j=0,\ldots,2τ-1$, buying two new moments per additional period. These identify average next-period attrition among survivors but need not identify allocation welfare or attrition among those prioritized for treatment.

### 实验/数据
Matched experiments separate the effects of estimation, bootstrap averaging, and regret weighting. In our experiments, bootstrap averaging and early stopping improve decisions, while regret weighting adds no improvement in pooled mean squared regret: better statistical fit need not yield better allocation welfare.

### 结果
In our experiments, bootstrap averaging and early stopping improve decisions, while regret weighting adds no improvement in pooled mean squared regret: better statistical fit need not yield better allocation welfare.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The code and artifacts are available at https://github.com/KurbanIntelligenceLab/waiting-buys-two-moments.

### 6. Revisiting the Mass and Scale Dependence of the "Lensing is Low" Effect with DECADE

- 作者：Kimiko Queen, Abigail V. Fisher, Johannes U. Lange｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.23828v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Galaxy-galaxy lensing (GGL) is a critical probe of cosmology and galaxy formation. However, predicted GGL amplitudes tend to be $\sim 20-40\%$ higher than observations, primarily on small scales, a tension called the lensing-is-low problem.

### 方法
If not resolved through astrophysics or measurement systematics, this discrepancy may indicate a tension in our cosmological standard model.

### 实验/数据
We revisit this claim using lensing data from the Dark Energy Camera All Data Everywhere (DECADE) project.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Ultimately, these new results favor a scale dependence in the lensing-is-low problem.

### 7. TUPLE-Bench: Evaluating and Mitigating Privacy-Utility Trade-offs in Typed Decision Models

- 作者：Yiqu Yang, Qiaoyuan Zheng, Yang Tian, Yu Fan, Elliott Ash｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.23668v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Typed decision models often return more than a selected category. They also expose probabilities for each candidate and, sometimes, a separate confidence score.

### 方法
Typed decision models often return more than a selected category. We introduce TUPLE-Bench (Typed decision models' Utility and Privacy Leakage Evaluation Benchmark), a benchmark of paired synthetic cases in which recipients may learn a coarse operational category but not its fine-grained cause. Across nine models, instructions to withhold the cause fail to protect it: 91.88%-99.93% of responses reveal the cause through direct selection or residual scores.

### 实验/数据
These fields support downstream decisions but may reveal information beyond a recipient's authorization. However, confidence fields increase leakage without consistently reducing cost. Our findings highlight the need to audit decision interfaces field by field and workflow by workflow.

### 结果
However, confidence fields increase leakage without consistently reducing cost.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our findings highlight the need to audit decision interfaces field by field and workflow by workflow.

### 8. Survey of Orion Disks with ALMA (SODA) IV: Millimeter variability of protoplanetary disks

- 作者：D. Krebs, A. Hacar, J. Forbrich, S. E. van Terwisga｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.23640v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Context. Short-term millimeter-wavelength variability in Class II young stellar objects (YSOs) has been considered minimal, often dismissed as very rare in ALMA-based studies on short timescales.

### 方法
By computing variability factors and statistical deviations from the mean flux, we identify sources exhibiting significant variability, accounting for noise and calibrator stability. Even with conservative selection criteria, we identify 20 variable sources within the sample (~5.3% of all detections).

### 实验/数据
This study aims to quantify short timescale (~1 hour to ~3 days) millimeter flux variability in unresolved Class II YSO disks observed as part of the SODA survey, leveraging its large dataset to assess the statistical significance of such variability across the LDN 1641 and LDN 1647 regions in Orion.

### 结果
However, recent findings suggest that variability on sub-day timescales is significant. By computing variability factors and statistical deviations from the mean flux, we identify sources exhibiting significant variability, accounting for noise and calibrator stability.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Masses derived from unresolved measurements could potentially be biased by this sort of variability.

### 9. Triangle Covers of Polygons: Approximation Algorithms and Complexity

- 作者：Linda Kleist, Lena Scherzer｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.23634v1

> 命中：hit_abstract=['CATE']

### 背景/问题
We study the geometric set cover problems of covering and partitioning a polygon into a minimum number of triangles. While the decision version of the covering problem is known to be APX-hard and $\exists\mathbb R$-complete (even for polygons without holes and vertices in general position), the computational complexity of partitioning a simple polygon into a minimum number of triangles is open.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
For general polygons, an $O(\log n)$-approximation follows by close inspection of previous work.

### 10. StopWatch: Goal Grounding for Object-goal Navigation

- 作者：Xinhao Liu, Yunsheng Tian, Yuheng Qiu, Pieter Abbeel, Xi Chen, Guanya Shi, Chen Feng｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.23841v1

> 命中：hit_abstract=['policy learning']

### 背景/问题
Pretrained VLMs bring rich world knowledge and semantic priors to object-goal navigation, and fine-tuning a VLM into a navigation policy has become a common recipe. Despite this progress, success rates remain low, and it is unclear which capability these fine-tuned policies lack.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
Explicit grounding substantially improves success and reaches state-of-the-art results on six benchmarks across three scene collections.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our work points to goal grounding as a missing piece of object-goal navigation and offers a simple and effective solution to the task.

### 11. Ionic switching between supermagnetic states

- 作者：Sumaiyatul Ahsan, Yin-Ju Yen, Andrew H. Comstock, Tanya A. Balandin, Jason D. Azoulay, Jamie H. Warner, Dario A. Arena, Faisal M. Alamgir｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23829v1

### 背景/问题
Supermagnetic states are typically set during synthesis. Changing and retaining these states requires sustained external stimulus.

### 方法
The interconversion between SFM and SSG persists at all measured subsequent lithiation-delithiation cycles, creating a general framework for supermagnetic switching.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The interconversion between SFM and SSG persists at all measured subsequent lithiation-delithiation cycles, creating a general framework for supermagnetic switching.

### 12. ENFR: Evidence Networks with Flow-Matched References for Amortized Simulation-Based Model Inference

- 作者：Kai Lehman, Jameson Dong, Carolina Cuesta-Lazaro, Niall Jeffrey, Benjamin D. Wandelt, Francisco Villaescusa-Navarro, Sven Krippendorf, Jochen Weller｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23825v1

### 背景/问题
The evidence, $\mathcal{Z} = p(x | \mathcal{M})$, of a data-generating model $\mathcal{M}$ is a powerful tool in Bayesian frameworks: it enables model inference, model misspecification tests, and goodness-of-fit assessment as an alternative to standard discrepancy statistics, e.g. $χ^2$.

### 方法
The evidence, $\mathcal{Z} = p(x | \mathcal{M})$, of a data-generating model $\mathcal{M}$ is a powerful tool in Bayesian frameworks: it enables model inference, model misspecification tests, and goodness-of-fit assessment as an alternative to standard discrepancy statistics, e.g. In both likelihood-based and simulation-based inference, estimating $\mathcal{Z}$ provides an immediate solution to high-dimensional goodness-of-fit or model misspecification tests: using $\mathcal{Z}(x)$ as the test statistic induces a minimum-volume level-$α$ test. Such tests are essential to assess model fidelity, which is necessary to trust simulation-based parameter inference.

### 实验/数据
The evidence, $\mathcal{Z} = p(x | \mathcal{M})$, of a data-generating model $\mathcal{M}$ is a powerful tool in Bayesian frameworks: it enables model inference, model misspecification tests, and goodness-of-fit assessment as an alternative to standard discrepancy statistics, e.g. In both likelihood-based and simulation-based inference, estimating $\mathcal{Z}$ provides an immediate solution to high-dimensional goodness-of-fit or model misspecification tests: using $\mathcal{Z}(x)$ as the test statistic induces a minimum-volume level-$α$ test. Such tests are essential to assess model fidelity, which is necessary to trust simulation-based parameter inference.

### 结果
We show improvement in estimation of $\mathcal{Z}$ over the flow-based baseline in all applications considered and the best performance of all density estimation methods considered in our benchmarks.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We demonstrate the performance and scaling behavior of these approaches on data from a variety of scientific applications.

### 13. Online Graph Coloring with Random Arrivals

- 作者：Hirotaka Yoneda, Masataka Yoneda｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23824v1

### 背景/问题
We study online graph coloring in the random-arrival model, where the vertices are presented in a uniformly random order. Assuming $n$ and $k$ are known in advance, we present a randomized exponential-time algorithm that colors any $k$-colorable graph on $n$ vertices with $O(k^3 \log^2 k \log^4 n)$ colors in expectation.

### 方法
We study online graph coloring in the random-arrival model, where the vertices are presented in a uniformly random order. Assuming $n$ and $k$ are known in advance, we present a randomized exponential-time algorithm that colors any $k$-colorable graph on $n$ vertices with $O(k^3 \log^2 k \log^4 n)$ colors in expectation.

### 实验/数据
We study online graph coloring in the random-arrival model, where the vertices are presented in a uniformly random order. This is the first online coloring algorithm that uses a polylogarithmic number of colors for all fixed $k \geq 3$, and is better than a known lower bound of $Ω(\log^{k-1} n)$ colors under adversarial arrivals for all fixed $k \geq 6$. For comparison, it is known to be NP-hard to approximate (offline) graph coloring within a factor of $n^{1-\varepsilon}$ for all fixed $\varepsilon > 0$.

### 结果
This is the first online coloring algorithm that uses a polylogarithmic number of colors for all fixed $k \geq 3$, and is better than a known lower bound of $Ω(\log^{k-1} n)$ colors under adversarial arrivals for all fixed $k \geq 6$.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Therefore, our exponential-time online algorithm achieves a performance guarantee beyond the NP-hardness threshold for polynomial-time approximation algorithms.

### 14. On extremal problems related to the Krzyż conjecture

- 作者：Sarah May Instanes, Adrián Llinares, Dragan Vukotić｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23817v1

### 背景/问题
We study general extremal problems similar or closely related to the Krzyż conjecture and establish the structural properties of extremal functions, pointing out some differences with the original Krzyż case. We also introduce a family of more specific problems of this kind, interpolating between the Krzyż problem and the problem of maximizing the constant term, and show that they are closely related to the Krzyż conjecture: the conjecture implies the analogous statement for all of them and, conversely, if one of them has the same extremal value as the Krzyż problem, then this value is $2/e$.

### 方法
This may represent a new approach to attacking the original problem.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we show that for these problems an extremal function whose Taylor coefficients $a_1,\ldots,a_{\lfloor n/3\rfloor}$ vanish must be the conjectured one; as a special case, we obtain a new proof of a recent result of MacDonald.

### 15. Learning Personalized Memory Gating from Delayed One-Sided Feedback

- 作者：Kaixuan Ji, Zixiang Chen, Wenting Zhao, Cheng Qian, Heng Wang, Weizhi Zhang, Jielin Qiu, Liangwei Yang 等｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23812v1

### 背景/问题
Long-term memory enables language-model agents to personalize future interactions, but a finite memory bank cannot preserve every extracted fact. Existing memory gating policies are typically shared across users and therefore fail to account for user-specific patterns of future reuse.

### 方法
Long-term memory enables language-model agents to personalize future interactions, but a finite memory bank cannot preserve every extracted fact. We first propose a retrieval-based labeling strategy that labels each fact by whether it is later retrieved and incorporated into responses. We then formulate online memory gating as contextual apple tasting with delayed one-sided feedback, and propose Warm-Start UCB, which combines offline learning from existing data with online adaptation to the current user.

### 实验/数据
We then formulate online memory gating as contextual apple tasting with delayed one-sided feedback, and propose Warm-Start UCB, which combines offline learning from existing data with online adaptation to the current user. The results of our experiment demonstrate that our method outperforms all baselines under different memory budgets and history lengths, establishing it as a promising personalized memory gating policy.

### 结果
The results of our experiment demonstrate that our method outperforms all baselines under different memory budgets and history lengths, establishing it as a promising personalized memory gating policy.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The results of our experiment demonstrate that our method outperforms all baselines under different memory budgets and history lengths, establishing it as a promising personalized memory gating policy.

### 16. Symplectic Lie groups and nilmanifolds associated with acyclic quivers

- 作者：Yihao Zheng｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23794v1

### 背景/问题
We give combinatorial criteria for the existence of left-invariant symplectic forms on the positive and full path Lie groups of finite acyclic quivers. For the nilpotent positive path Lie groups, the criterion also determines whether their compact quotients admit symplectic forms and forces the nilpotency step to be at most three.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also describe the cohomology rings of the compact symplectic nilmanifolds and determine all Lefschetz ranks.

### 17. Constructions and reductions on the Hornich-Hlawka inequality and its generalizations

- 作者：Seokbin Lee｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23785v1

### 背景/问题
We investigate five open problems concerning the Hornich-Hlawka inequality and its generalizations posed by Marinescu and Niculescu. We give constructive answers to three of them.

### 方法
Second, we present a Nakano space that is not Hornich-Hlawka.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, for $p(\cdot): (0, 1) \to [1, 2]$ measurable and integers $k \geq 0$, we establish a Sobolev-Nakano equivalence: we prove that $W^{k,p(\cdot)}(0,1)$, equipped with the sum of the Luxemburg norms of its derivatives of orders $0, \ldots, k$, is Hornich-Hlawka if and only if $L^{p(\cdot)}(0,1)$ is Hornich-Hlawka.

### 18. Enforcing Code Reasoning in Agentic Scaffold for More Effective Issue Resolution

- 作者：Changshu Liu, Ji young Kim, Alireza Ghazanfari, Saanvi Nallu, Reyhaneh Jabbarvand｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23782v1

### 背景/问题
Reasoning is central to ReAct-based programming agents, yet whether and how they reason about code remains unclear. We study 7,955 issue-resolution trajectories from six single- and multi-agent scaffolds across four programming languages on SWE-bench-Verified, SWE-bench-Pro, and SWE-bench-Lite.

### 方法
We identify 12 forms of code reasoning in 66.95% of trajectories. To address these limitations, we propose DeskCheck, an agentic scaffold that systematically guides code reasoning throughout repository-level issue resolution.

### 实验/数据
Exact McNemar tests show statistically significant improvements across all subject LLMs (p < 10^-10), while repeated experiments support robustness to agent nondeterminism.

### 结果
Code reasoning is associated with higher resolution rates, and its intensity increases with task complexity. On 731 SWE-bench-Pro instances, DeskCheck improves resolution rates over mini-SWE-Agent and Claude Code by 6.29% to 10.53%, at an additional cost of $0.02-$0.28 per instance (average: $0.14). Per-phase analyses show higher method-level localization recall, more successful repairs of imprecisely localized issues, and better detection of missed corner cases in near-correct patches.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These findings motivate systematic code reasoning as a means of improving programming agents.

### 19. Transport and thermalization under noncommuting localized constraints

- 作者：Amir Nesturov, Attila Takács, Lenart Zadnik｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23781v1

### 背景/问题
We investigate the effects of spatially localized conserved quantities on transport and thermalization in quantum and classical many-body systems. We consider several related models: the integrable quantum Volterra model, its nonintegrable classical limit, and two cellular automata derived from the latter.

### 方法
We consider several related models: the integrable quantum Volterra model, its nonintegrable classical limit, and two cellular automata derived from the latter. Although localized constraints are often associated with lattice gauge theories, our models do not admit such an interpretation. In the quantum Volterra model, we derive an exact mapping of the dynamics within each Hilbert-space fragment onto a quantum chiral Potts chain.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, in the cellular automata, we show that, despite leaving transport unaffected, localized constraints lead to a strong breakdown of local ergodicity.

### 20. Polytope Sampling at the Speed of Isoperimetry

- 作者：Anming Gu, Bobby Shi, Kevin Tian, Hubert Yang｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23775v1

### 背景/问题
We give faster algorithms for sampling from the uniform distribution over a polytope. Our main result is an algorithm that, when applied to a polytope with $m$ constraints in $n$ dimensions, uses $m \cdot \mathrm{poly}\log(\frac m δ)$ iterations, each running in time $O(mn^{ω- 1})$, to return a sample within total variation distance $δ$ to the uniform distribution.

### 方法
Our sampler is based on the recent \emph{functional stochastic localization} framework of [GST26], and achieves an iteration count nearly matching the Poincaré constant of the uniform distribution with respect to the logarithmic barrier.

### 实验/数据
未在摘要中明确给出。

### 结果
When $m =O(n)$ and $δ= \mathrm{poly}(\frac 1 n)$, our runtime improves upon all prior works by an $Ω(n^{2/3})$ factor.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our sampler is based on the recent \emph{functional stochastic localization} framework of [GST26], and achieves an iteration count nearly matching the Poincaré constant of the uniform distribution with respect to the logarithmic barrier.

### 21. Not All Actions Contribute Equally: Learning Precise Progress Estimation from Imprecise Demonstrations

- 作者：Huanqian Wang, Boshi Tang, Botong Xiao, Jie Zhang, Yang Yue, Danhua Tao, Shiji Song, Gao Huang｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23769v1

### 背景/问题
Progress estimators play an essential role in providing dense reward signals for reinforcement learning in robotic manipulation, but accurately assessing task progress can be much challenging. Existing methods heavily rely on expert data and naively assume that all actions within a demonstration contribute to task success.

### 方法
To this end, we propose PRIME, a novel progress estimator capable of learning precise progress estimation from imprecise demonstrations by aggregating experience across trajectories.

### 实验/数据
Existing methods heavily rely on expert data and naively assume that all actions within a demonstration contribute to task success. Extensive experiments in both simulation and real world on precise manipulation tasks show that PRIME is consistently effective across diverse tasks, and robust to data with varying degrees of suboptimality.

### 结果
Notably, the advantage of PRIME gets more pronounced in higher-precision scenarios, yielding up to a \(5\times\) improvement in policy success rate over the SFT baselines on charger insertion.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Notably, the advantage of PRIME gets more pronounced in higher-precision scenarios, yielding up to a \(5\times\) improvement in policy success rate over the SFT baselines on charger insertion.

### 22. A Paired RGB-Sonar Dataset for Fish Monitoring with Consumer Sonar

- 作者：Mourad Derbedrosian, Michael Hobley, Pietro Perona｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23759v1

### 背景/问题
Imaging sonar enables underwater observation in conditions where optical imaging is ineffective due to darkness and turbid water. However, imaging-sonar systems previously used for ecological monitoring have typically been expensive, limiting their accessibility.

### 方法
未在摘要中明确给出。

### 实验/数据
We introduce the Huntington and Caltech Koi RGB and Sonar dataset (HaCKRS), which pairs Garmin LiveScope imaging-sonar recordings with top-down RGB video of koi carp. The dataset contains more than 105,000 temporally matched frame pairs, spanning approximately 3.3 hours of recordings across four range and orientation configurations. We provide frame-wise metadata, sonar geometry and coordinate information, synchronization data for all four configurations, and planar registration for the three horizontal configurations.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We intend HaCKRS to support annotation and the development of fish detection, tracking, and counting methods, and investigations into the potential of consumer sonar for ecological monitoring.

### 23. Spectral networks, finite webs, and the $T_3$ cubic differential

- 作者：Omar Kidwai, Guillaume Tahar｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23752v1

### 背景/问题
We describe spectral networks for cubic differentials on $\mathbf{P}^1$ with exactly three poles all of order two, following observations of Hollands-Neitzke. To do so, we give a precise definition and establish some basic properties of a class of finite webs (corresponding to BPS states in physics) in the cubic differential setting, including their non-vanishing central charge.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Physically, this example corresponds to a fundamental building block for a large class of four-dimensional $\mathcal{N}=2$ QFTs with gauge group $\mathrm{SU}(3)$.

### 24. Beyond Multi-Stage Pipelines: A Label-Correlation Ensemble for Multi-Label Retinal Fundus Disease Classification

- 作者：Md Asif Uddin, Jannatul Ferdous, Asif Islam, Zobaer Mahmud Zisan, Promit Ghosh, Shah Ahafik Arman, Niloy Farhan, Rafeed Rahman｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23747v1

### 背景/问题
Retinal fundus images frequently carry more than one disease, and public fundus datasets are heterogeneous and severely long-tailed. Clinical triage suggests a staged design, in which a screening gate, a disease-group router and group-specific classifiers operate in sequence, but it is unclear whether this hierarchy earns its complexity.

### 方法
We present a controlled comparison of three architectures on a unified 39-target label space built from RFMiD 1.0, RFMiD 2.0 and ODIR-5K (12,652 images): (i) a three-stage gated cascade of eight models, (ii) a flat model with 39 independent sigmoid outputs, and (iii) a label-correlation model that replaces the flat linear head with 39 learned label queries and a two-layer transformer decoder. Label-correlation modeling gives the largest single gain, raising the detection rate from 0.621 to 0.682 (0.689 with test-time augmentation). Blending the flat and label-correlation models under four-view test-time augmentation is the best configuration on six of eight metrics (exact match 0.694, micro-F1 0.678, macro-F1 0.456, macro-AUC 0.972).

### 实验/数据
Retinal fundus images frequently carry more than one disease, and public fundus datasets are heterogeneous and severely long-tailed. We also show that ensembling a gated cascade with continuous-output models is harmful, and that per-source negative sampling is needed to remove a dataset shortcut that otherwise yields a spurious AUC of 1.000.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also show that ensembling a gated cascade with continuous-output models is harmful, and that per-source negative sampling is needed to remove a dataset shortcut that otherwise yields a spurious AUC of 1.000.

### 25. The distribution of $αp$ modulo one in real quadratic function fields

- 作者：Esrafil Ali Molla｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23742v1

### 背景/问题
Matomäki proved that if $α\in\R$ is irrational, then there are infinitely many primes $p$ such that $|α-a/p|\le p^{-4/3+\varepsilon}$ for a suitable integer $a$. In \cite{BaMo}, Baier and the author established analogues of this result for $\F_q(T)$ and its imaginary quadratic extensions.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In this paper, we extend it to all real quadratic extensions of $\F_q(T)$.

### 26. The Italian lawmaking process: a unified and structured dataset

- 作者：Matilde Contestabile, Chiara Ferrara, Giovanni Parrillo, Lorenzo Emer, Andrea Vandin｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23741v1

### 背景/问题
The Italian legislative process is documented in detailed parliamentary records hosted in institutional websites. However, much of this information is available only as unstructured text, limiting its systematic reuse.

### 方法
未在摘要中明确给出。

### 实验/数据
The resulting dataset reconstructs the procedural histories of all 5346 Italian laws enacted between 1985 and 2026, spanning parliamentary terms IX to XIX, for overall 101413 events. The dataset supports research in the emerging fields of computational legal and legislative studies, potentially combined with process-oriented data science methods to examine procedural paths and legislative timing across parliamentary terms.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The dataset supports research in the emerging fields of computational legal and legislative studies, potentially combined with process-oriented data science methods to examine procedural paths and legislative timing across parliamentary terms.

### 27. Eulerian ion energisation in three-dimensional hybrid-Vlasov-Maxwell turbulence

- 作者：L. Richard, S. S. Cerri, O. Pezzi, C. Granier, J. M. TenBarge｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23740v1

### 背景/问题
In collisionless plasma turbulence, energy is transferred from electromagnetic fluctuations to the particles. However, the relative contributions of different ion energisation mechanisms remain unclear.

### 方法
未在摘要中明确给出。

### 实验/数据
We investigate ion energisation in three-dimensional hybrid Vlasov--Maxwell simulations of decaying turbulence at $β_{i0}=0.25$ and $β_{i0}=4$, where $β_{i0}$ is the initial ratio of ion thermal to magnetic pressure.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The results also highlight the key role of non-local thermodynamic-equilibrium effects in energy conversion in collisionless plasma turbulence.

### 28. Plancherel Decompositions and Distinctions for $\mathrm{Sp}_{2n}\backslash \mathrm{Gl}_{2n+1}$ and $P(\mathrm{Sp}_{2n})\backslash \mathrm{Gl}_{2n}$

- 作者：Sagnik Mukherjee｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23737v1

### 背景/问题
Let $F$ be a non-Archimedean local field of characteristic zero. We determine the Plancherel decompositions of $\mathrm{Sp}_{2n}(F)\backslash\mathrm{GL}_{2n+1}(F)$ and $P(\mathrm{Sp}_{2n})(F)\backslash\mathrm{GL}_{2n}(F)$, where $P(\mathrm{Sp}_{2n})$ denotes the mirabolic subgroup of $\mathrm{Sp}_{2n}$, and study smooth distinction for both spaces.

### 方法
We carry out the local unfolding procedure of arXiv:1203.0039, Section 9.5, constructing unitary isomorphisms with degenerate Whittaker models by successive Fourier transforms. The isomorphism for the even model is already stated there in Example 9.5.17. Using closed parabolic orbits and local Rankin-Selberg integrals, we prove that all representations induced from these tempered data are distinguished for the corresponding model.

### 实验/数据
Let $F$ be a non-Archimedean local field of characteristic zero. Using closed parabolic orbits and local Rankin-Selberg integrals, we prove that all representations induced from these tempered data are distinguished for the corresponding model.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
For $\mathrm{GL}_5(F)$, however, we prove that an irreducible tempered representation is $\mathrm{Sp}_4(F)$-distinguished if and only if it is induced from tempered representations of $\mathrm{GL}_2(F)$ and $\mathrm{GL}_3(F)$.

### 29. ECG-SDI: Single-lead Electrocardiogram Enables Continuous Sleep Depth Index Profiling and Scalable Digital Biomarkers for Sleep Health

- 作者：Donglin Xie, Qingshuo Zhao, Songchi Zhou, Haoyu Wang, Jingyu Wang, Yuxi Zhou, Thomas Penzel, Shenda Hong｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23727v1

### 背景/问题
Conventional sleep staging provides a coarse-grained representation that obscures within-stage depth variation. We developed ECG-SDI, a single-lead electrocardiography (ECG) framework for continuous sleep-depth profiling and digital biomarker extraction.

### 方法
We developed ECG-SDI, a single-lead electrocardiography (ECG) framework for continuous sleep-depth profiling and digital biomarker extraction. Using 12,392 overnight polysomnographic recordings, we trained and validated a two-stage deep learning model supervised by conventional sleep-stage labels.

### 实验/数据
未在摘要中明确给出。

### 结果
Among 507 participants with paired recordings before and after continuous positive airway pressure (CPAP), normalized sleep-depth area increased by 6.1% and shallow-sleep burden below 0.3 decreased by 16.0%. Exploratory analyses linked reductions in approximate entropy and depth variability to reduced oxygen desaturation and increased sleep efficiency, respectively (Spearman rho = 0.24 and 0.12); both associations remained positive after covariate adjustment. Mean ECG-SDI within N2 increased by 0.017 (95% CI, 0.004-0.030).

### 结论/启示（面向电商发券、定价、营销算法等应用）
These findings support ECG-based sleep phenotyping and further evaluation of CPAP response monitoring at home.

### 30. Recognizing Study Lineage Is Not Enough: Over-Crediting Same-Trial Evidence in LLM-Based Medical Verification

- 作者：Mukand Krishna, Anoushka Harit, Chenghao Xiao, Zhongtian Sun｜年份：2026｜发布时间：2026-10-16｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.23721v1

### 背景/问题
Publication count is not study count. A model can identify shared trial lineage correctly in a direct task yet over-credit a second publication from the same trial when aggregating evidence.

### 方法
A model can identify shared trial lineage correctly in a direct task yet over-credit a second publication from the same trial when aggregating evidence. We evaluate this behavior in medical LLM verification using 14 source-audited clinical families and five model conditions. Other model conditions show mixed behavior, and rejected outputs limit several comparisons.

### 实验/数据
The code and data artifacts are available at https://anonymous.4open.science/r/study-lineage-review-artifact.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The code and data artifacts are available at https://anonymous.4open.science/r/study-lineage-review-artifact.
