# CausalRadar 日报 - 2026-10-12

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Designing Protein Structures from Natural Language

- 作者：Joseph Lee, Yanjing Li, Bo Qiang, Gregory Lau, Allyson Ettinger, Noah A. Smith, Rory Donovan-Maiye, David Baker 等｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**6.74**
- 链接：https://arxiv.org/abs/2610.13917v1

> 命中：hit_scenario=['ads']；hit_abstract=['CATE']

### 背景/问题
A central challenge in de novo protein design is generating proteins with desired structural and functional properties. Existing design models typically require a dedicated input representation for each property, limiting the design objectives they support.

### 方法
Existing design models typically require a dedicated input representation for each property, limiting the design objectives they support. We develop Prompteina, the first all-atom structure generation model that supports new and broader design objectives specified in natural language, analogous to text-to-image generation. We adapt Proteina-Complexa, a pretrained structure generation model, through text-conditioned pretraining and finetuning that aligns residues with their corresponding text.

### 实验/数据
To train Prompteina, we construct Prompteina-Data, a paired text--protein structure dataset of 1.8M structures and 50M+ captions describing global and residue-specific structural and functional properties. Finally, we experimentally validate Prompteina designs against GM2A, a target with no reported de novo binders.

### 结果
Prompteina outperforms baselines on 15 of 18 structural properties and generates proteins that more closely match descriptions of their intended functions. In binder design, it leads baselines on at least 13 of 20 targets and improves interface confidence by 14\% over the strongest baseline.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results establish natural language as an effective and powerful conditioning interface for protein structure generation.

### 2. Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer Selection

- 作者：Juan Terven, Diana-Margarita Córdova-Esparza, Ruben Gomez, Carlos Miranda Rocha, Julio-Alejandro Romero-González, Edgar Chavez-Urbiola｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**6.24**
- 链接：https://arxiv.org/abs/2610.13821v1

> 命中：hit_title=['policy learning']

### 背景/问题
A useful language model should know when to answer and when to say "I don't know." Can we improve that decision by training the model itself or by training a separate component to check its answers? We study both approaches on Qwen3-14B for factual questions, using a score that rewards correct answers, penalizes mistakes, and allows abstention.

### 方法
A useful language model should know when to answer and when to say "I don't know." Can we improve that decision by training the model itself or by training a separate component to check its answers? We study both approaches on Qwen3-14B for factual questions, using a score that rewards correct answers, penalizes mistakes, and allows abstention. Across three training seeds and two held-out confidence thresholds, a learned answer selector improves threshold-averaged utility over the original model's calibrated confidence filter.

### 实验/数据
Our results support learning to select answers in this setting while showing that reliable abstention across datasets remains unresolved.

### 结果
A useful language model should know when to answer and when to say "I don't know." Can we improve that decision by training the model itself or by training a separate component to check its answers? Across three training seeds and two held-out confidence thresholds, a learned answer selector improves threshold-averaged utility over the original model's calibrated confidence filter. On TriviaQA, mean coverage increases from 20.2% to 30.9%, while the pooled error rate among scored answers decreases from 23.0% to 14.5% under exact-match grading.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our results support learning to select answers in this setting while showing that reliable abstention across datasets remains unresolved.

### 3. The Redshift-Space Galaxy Power Spectrum at Two-Loop Order

- 作者：Oliver H. E. Philcox｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**4.74**
- 链接：https://arxiv.org/abs/2610.13867v1

> 命中：hit_scenario=['ads']

### 背景/问题
Contemporary large-scale structure analyses center around the galaxy power spectrum, modeled with one-loop perturbation theory. This description naturally breaks down at large wavenumbers, prohibiting the extraction of cosmological information from small-scale clustering.

### 方法
Contemporary large-scale structure analyses center around the galaxy power spectrum, modeled with one-loop perturbation theory. In this work, we present a complete model for the redshift-space galaxy power spectrum up to two-loop order, derived in the framework of the Effective Field Theory of Large Scale Structure. Our model additionally encodes all deterministic contributions to the one-loop bispectrum and trispectrum (as well as the tree-level quadspectrum and pentaspectrum), which depend on many of the same parameters.

### 实验/数据
In this work, we present a complete model for the redshift-space galaxy power spectrum up to two-loop order, derived in the framework of the Effective Field Theory of Large Scale Structure. The approach is validated using power spectra measured from high-resolution simulations, considering both dark matter and realistic galaxy samples.

### 结果
The extension to two-loop order greatly increases the range of scales over which the power spectrum can be modeled, with $k_{\rm max}$ rising from $0.2h\,\mathrm{Mpc}^{-1}$ to $0.34h\,\mathrm{Mpc}^{-1}$ for a luminous red galaxy sample at $z=0.5$. Much of the additional information is absorbed by the numerous fifth-order biases and counterterms; for this reason, constraints on $σ_8$ are not significantly enhanced by the inclusion of two-loop terms.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Future work will assess the full implications of the two-loop model for cosmological parameter inference, both alone and in combination with higher-order statistics.

### 4. Robust Golden Ratio universality as a consequence of a circulant symmetry

- 作者：Luka Paljk, Johannes Schmidt, Vladislav Popkov｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**4.74**
- 链接：https://arxiv.org/abs/2610.13842v1

> 命中：hit_scenario=['ads']

### 背景/问题
We find a robust scenario for the emergence of the Golden Ratio (GR) dynamical universality class, characterized by the dynamical exponent $z \equiv \varphi=\frac{1}{2}(1+\sqrt{5})$. Previously, its emergence required fine-tuning of system parameters.

### 方法
We introduce a multilane exclusion process with Bernoulli stationary measure as a minimal, parameter-free model, which features GR universality for all conserved modes, most of which are doubly degenerate.

### 实验/数据
Our predictions, based on mode-coupling theory generalized to treat degenerate conserved modes, are corroborated by large-scale Monte Carlo simulations.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our predictions, based on mode-coupling theory generalized to treat degenerate conserved modes, are corroborated by large-scale Monte Carlo simulations.

### 5. Maximally antiflat fixed-particle-number fermionic states

- 作者：Rahul Gupta, Arya Haghighian, James D. Whitfield｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.13903v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Fermionic Gaussian states are completely characterized by their two-point correlations, making the covariance matrix a natural reference for quantifying non-Gaussian structure. Motivated by fermionic antiflatness, we study its extremal form for pure number-conserving states and ask which states can be maximally antiflat and how they can be constructed.

### 方法
Combining this framework with a Hilbert--Schmidt estimate of Christiansen for truncated two-body correlations, we obtain an upper bound on the connected quartic structure in terms of first antiflatness.

### 实验/数据
Maximally antiflat states with identical one-body data can exhibit distinct connected four-point correlations, which we characterize through the four-point Majorana Wick error and, equivalently, the connected two-body reduced density matrix cumulant.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our results establish both a complete characterization of maximal fermionic antiflatness at fixed particle number and a constrained hierarchy linking covariance-level flatness to higher-order non-Gaussian correlations.

### 6. BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi-Fidelity Evaluation

- 作者：Fabio Hübel, Adam Lilja, Yue Yin, Siming He, Claire Tomlin, Shankar Sastry, Jonas Frey, Marco Pavone｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.13862v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Deploying language-model agents onboard mobile robots requires task reasoning and responsive execution within limited compute and memory. We propose BT-Agent, an onboard architecture combining LLM-driven task decisions with predefined behavior-tree (BT) skills.

### 方法
Deploying language-model agents onboard mobile robots requires task reasoning and responsive execution within limited compute and memory. We propose BT-Agent, an onboard architecture combining LLM-driven task decisions with predefined behavior-tree (BT) skills. We demonstrate fully onboard operation with a 9B model on a quadruped across five task categories.

### 实验/数据
Text supports 10.9$\times$ higher evaluation throughput, while simulation reveals how perception and motion failures change task outcomes.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Ablations identify structured tool calls and informative failure feedback as the most useful components.

### 7. Insights from the stability of methanol maser flare properties I: G9.62+0.20E

- 作者：S. P. van den Heever, D. J. van der Walt｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.13774v1

> 命中：hit_abstract=['CATE']

### 背景/问题
The brightest 6.7 GHz methanol maser in the Galaxy is associated with the high-mass star-forming region (HMSFR) G009.62+0.20E. Additionally, this methanol maser shows periodic flaring observed at 6.7 and 12.2 GHz.

### 方法
Several models have been hypothesized to explain the periodicity, including periodic accretion, spiral shocks in the gaps of circumbinary disks, pulsating stars, dicke's superradiance, and a colliding wind binary (CWB) system. From these results, it is argued for or against any of the mechanisms that have been proposed to explain the periodicity. After careful consideration of the proposed mechanisms for periodic methanol masers, we conclude that all but one, the CWB model, have been ruled out as a possible driver of this flare profile.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
It has also been established that the CWB model can qualitatively explain the flare profile of the periodic methanol masers.

### 8. TeV Gamma-Ray Emission in the DA 495 Region from HAWC Observations of J1952+2924, J1954+2837, and J1958+2848

- 作者：R. Alfaro, C. Alvarez, E. Anita-Rangel, M. Araya, J. C. Arteaga-Velázquez, D. Avila Rojas, H. A. Ayala Solares, R. Babu 等｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.13771v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Previous observations of the DA 495 region, which contains the pulsar wind nebula (PWN) DA 495 and other very-high-energy (VHE; $>100~\textrm{GeV}$) gamma-ray emitters, showed inconsistent results across different VHE experiments, including differences in the measured flux of DA 495 and in the number of reported sources. Our new dedicated analysis using 3071 days of HAWC data resolves these discrepancies.

### 方法
We identify three extended sources, HAWC J1952+2924 (DA 495), HAWC J1954+2837, and HAWC J1958+2848, all with curved spectra, and find a hint of a fourth source.

### 实验/数据
Previous observations of the DA 495 region, which contains the pulsar wind nebula (PWN) DA 495 and other very-high-energy (VHE; $>100~\textrm{GeV}$) gamma-ray emitters, showed inconsistent results across different VHE experiments, including differences in the measured flux of DA 495 and in the number of reported sources. Our new dedicated analysis using 3071 days of HAWC data resolves these discrepancies. For DA 495, a multi-wavelength analysis, including our results, radio, X-ray, and other gamma-ray data, reveals that its extended emission is best described by leptonic interactions with an inferred magnetic field of $B\sim10~μ\textrm{G}$ and that hadronic components are not required.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results reinforce the interpretation of DA 495 as a leptonic-dominated PWN and add two candidates to the growing population of TeV halos.

### 9. Asymmetric Information in Dynamic Lending Games

- 作者：Kristijan Atanasov, Frederik Mallmann-Trenn, Carmine Ventre｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**4.24**
- 链接：https://arxiv.org/abs/2610.13759v1

> 命中：hit_abstract=['CATE']

### 背景/问题
We study a dynamic lending game with limited but reusable supply. Borrower arrivals and loan durations are stochastic.

### 方法
We identify sufficient mathematical regimes in which this phenomenon occurs.

### 实验/数据
未在摘要中明确给出。

### 结果
Interestingly, in the case of asymmetric information disclosure, total payoffs can increase, while total lending remains the same.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Wider access to supply information need not lower those fees: its effect depends on who receives the information and the balance between demand and supply.

### 10. Splat2Act: From Captured Scenes to Personalized VLA Manipulation

- 作者：Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13945v1

### 背景/问题
A user who brings a generalist manipulation policy into their home or office wants it to pick up their objects from their shelves, counters, and tables. Yet even a strong generalist like $π_{0.5}$ achieves 0% pickup success in our captured deployment scenes without adaptation, and collecting real demonstrations in every user's environment is prohibitively expensive.

### 方法
We present Splat2Act, an automated real-to-sim-to-real pipeline that personalizes a pretrained vision-language-action (VLA) policy to a specific scene and object set using only a handheld phone scan and images of the user's objects.

### 实验/数据
Unlike prior real-to-sim work that reconstructs individual tabletops, Splat2Act operates on building-scale indoor environments: it builds a photorealistic digital twin with 3D Gaussian Splatting and collision geometry, automatically discovers tabletop and non-tabletop receptacles, constructs feasible pickup tasks, and generates successful demonstrations with a privileged simulation oracle, with only scene and object capture required from a human. These results suggest that automated real-to-sim-to-real training can personalize VLA manipulation policies using only simulation-oracle data.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results suggest that automated real-to-sim-to-real training can personalize VLA manipulation policies using only simulation-oracle data.

### 11. A Riesz-Map Preconditioned Extragradient Method for Price Formation in Mean Field Games

- 作者：Yeva Gevorgyan, Diogo Gomes｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13934v1

### 背景/问题
We develop and analyze a projected extragradient method, preconditioned by a Riesz map, for a first-order price-formation mean field game in one space dimension. The model couples Hamilton--Jacobi--Bellman and transport equations through a global market-clearing constraint.

### 方法
We develop and analyze a projected extragradient method, preconditioned by a Riesz map, for a first-order price-formation mean field game in one space dimension. The model couples Hamilton--Jacobi--Bellman and transport equations through a global market-clearing constraint.

### 实验/数据
We develop and analyze a projected extragradient method, preconditioned by a Riesz map, for a first-order price-formation mean field game in one space dimension. A monotone weak formulation incorporates the mixed initial--terminal data.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Price errors and value-function errors measured away from low-density regions decay approximately at first order under refinement, while density errors decrease more slowly.

### 12. The Haagerup VOA at $c=8$

- 作者：Andrew Riesen｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13933v1

### 背景/问题
We announce an explicit construction of a unitary, strongly rational vertex operator algebra $U$ of central charge $8$ inside $V_{E_6\oplus A_2}$, with a ribbon equivalence $\mathrm{Rep}(U)\simeq Z(\mathcal H_3)$ realizing the Haagerup double. The vertex algebra is generated by six affine currents and three specified weight-two fields; its weight-one Lie algebra is $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$, at levels $1$ and $39$.

### 方法
未在摘要中明确给出。

### 实验/数据
The vertex algebra is generated by six affine currents and three specified weight-two fields; its weight-one Lie algebra is $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$, at levels $1$ and $39$.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We outline the argument, which combines exact lattice calculations, an all-weight strong-generation induction and $C_2$-cofiniteness, semisimple descent for a full corner of Zhu's algebra, modular Galois symmetry, and holomorphic $E_8$ extensions.

### 13. Chronos Policy: Learning Robot Policies on Physical Time

- 作者：Changhao Wang, Jaden Clark, Shuran Song｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13929v1

### 背景/问题
Robot policies often convert sensing and control into fixed-rate observation-action sequences, leaving physical time implicit in sequence position. This assumption breaks when observation rates or delays vary, or when inference latency changes.

### 方法
未在摘要中明确给出。

### 实验/数据
This also enables learning from asynchronous, multi-rate data without forcing all measurements onto a fixed temporal grid. Across simulation and real-world experiments, Chronos Policy improves performance on dynamic tasks, where observation-to-action timing is critical, and on multisensory tasks, where the relative timing between observations matters.

### 结果
Across simulation and real-world experiments, Chronos Policy improves performance on dynamic tasks, where observation-to-action timing is critical, and on multisensory tasks, where the relative timing between observations matters.

### 结论/启示（面向电商发券、定价、营销算法等应用）
On standard quasi-static tasks, it preserves nominal performance while improving robustness to changes in sensing and inference timing.

### 14. On some rigidity results for high-dimensional confoliations

- 作者：Fabio Gironella, Seungook Yu｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13927v1

### 背景/问题
The main result is an obstruction to the presence of contact regions for c-symplectic confoliations in any odd ambient dimension. As a first application, we prove a 5-dimensional analogue (under stronger assumptions) of a Reeb stability theorem for confoliations in dimension 3 due to Eliashberg and Thurston.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Lastly, we describe several natural classes of examples of these types of contact approximations of c-symplectic confoliations.

### 15. KL Before and After Mixing: A Round-Complexity Separation in Parallel Sampling

- 作者：Tianyi Wu｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13924v1

### 背景/问题
A parallel sampler can choose at random which coordinates to generate together. For a target $p$ and the output law $q_U$ of a schedule $U$ drawn afresh for each output, we compare the schedule-averaged divergence $\mathbb{E}_U D_{\mathrm{KL}}(p\|q_U)$ with the output-law divergence $D_{\mathrm{KL}}(p\|\mathbb{E}_U q_U)$, in nats.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Prior work implies the order of the schedule-averaged cost on the balanced target and its $O_\varepsilon((\log n)^2)$ upper bounds on both extensions.

### 16. A Comprehensive JWST Slitless Spectroscopic Census of $\sim$12,000 Emission-Line Galaxies at Redshift $0\sim9$ in COSMOS

- 作者：Shuqi Fu, Zijian Zhang, Danyang Jiang, Jie Chen, Linhua Jiang, Chenxi Bao, Yihe Wang, Ronaldo Laishram｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13920v1

### 背景/问题
Emission-line galaxies provide key diagnostics of star formation, chemical enrichment, and AGN activity across cosmic time. We present a systematic census of emission-line sources using JWST/NIRCam wide-field slitless spectroscopy (WFSS) from the COSMOS-3D program, which covers a large contiguous area of 0.33 deg$^2$ and provides F444W grism spectroscopy over $3.9$--$5.1\ μ$m.

### 方法
We present a systematic census of emission-line sources using JWST/NIRCam wide-field slitless spectroscopy (WFSS) from the COSMOS-3D program, which covers a large contiguous area of 0.33 deg$^2$ and provides F444W grism spectroscopy over $3.9$--$5.1\ μ$m. To address source confusion inherent to slitless spectroscopy, we develop a multi-step identification framework that combines information from spectra, images, spectral energy distributions, and spatial distributions. We introduce convolutional neural network and large language model to emulate the human identification process and improve efficiency.

### 实验/数据
We present a systematic census of emission-line sources using JWST/NIRCam wide-field slitless spectroscopy (WFSS) from the COSMOS-3D program, which covers a large contiguous area of 0.33 deg$^2$ and provides F444W grism spectroscopy over $3.9$--$5.1\ μ$m. By combining slitless spectroscopy with deep multi-band imaging data, we construct a homogeneous spectroscopic sample of 12,275 objects at redshift 0--9. This catalog provides a key reference dataset for studies of galaxy evolution and AGN activity, and demonstrates the power of WFSS for constructing large, unbiased spectroscopic samples over wide areas.

### 结果
We introduce convolutional neural network and large language model to emulate the human identification process and improve efficiency.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The full catalog will be publicly available online upon publication.

### 17. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness

- 作者：Daniel Szelogowski｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13918v1

### 背景/问题
Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothalamic leaky integrate-and-fire spiking neural network.

### 方法
Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothalamic leaky integrate-and-fire spiking neural network.

### 实验/数据
The synthetic local field potential converges closely with empirical human electroencephalography spectra from the PhysioNet Sleep-EDF database across all canonical frequency bands (spectral mean absolute error of 0.33--0.35). Simulations reveal that sleep duration fails to predict restorative recovery: paradoxical insomnia achieves normal total sleep time (21.15 h) yet yields low restoration (37.6%) from unsuppressed cortical beta-band intrusion, whereas hypocretin deficiency in narcolepsy produces severe nocturnal fragmentation (781 min of wake after sleep onset) and 35 sleep-onset rapid eye movement periods.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
DyssomniaNN provides an in silico platform for mechanistic sleep research and virtual neuropharmacology.

### 18. Where to Look Matters: Rethinking Sub-Volume Sampling in 3D Medical Self-supervised Learning

- 作者：Junkai Liu, Le Zhang｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13915v1

### 背景/问题
Self-supervised learning on 3D medical images commonly relies on random sub-volume sampling during pretraining. However, random cropping implicitly treats all spatial regions as equally worth observing, despite anatomical priors and spatial redundancy that make regions inherently unequal in their value for representation learning.

### 方法
We propose \textbf{\method}, a plug-and-play framework that replaces random cropping with an offline coarse-to-fine probe bank guided by \textit{anatomy-awareness}, \textit{informativeness}, and \textit{diversity}.

### 实验/数据
We propose \textbf{\method}, a plug-and-play framework that replaces random cropping with an offline coarse-to-fine probe bank guided by \textit{anatomy-awareness}, \textit{informativeness}, and \textit{diversity}. Extensive experiments across multiple 3D medical SSL backbones and downstream tasks demonstrate that \method-\lite consistently improves transfer performance over random sampling.

### 结果
To this end, we first show through controlled crop-quality manipulations that better sub-volumes lead to better downstream transfer, revealing the observation policy as an overlooked bottleneck in 3D medical SSL. Extensive experiments across multiple 3D medical SSL backbones and downstream tasks demonstrate that \method-\lite consistently improves transfer performance over random sampling.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Mechanistic analyses further attribute these gains to more anatomically plausible and informative observations, reduced spatial redundancy, more efficient learning dynamics, and more structured representations.

### 19. Property $R_\infty$ for Artin and Coxeter groups whose outer automorphisms are length-preserving

- 作者：Ignat Soroko｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13904v1

### 背景/问题
We prove that every length-preserving automorphism of a nonspherical Artin or Coxeter group has infinite Reidemeister number. As a consequence, we establish property $R_\infty$ for large-type free-of-infinity Artin groups, infinite strongly rigid Coxeter groups, and infinite virtually abelian Coxeter groups, including all affine Coxeter groups.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also prove that the automorphism group of every infinite irreducible non-affine strongly rigid Coxeter group is acylindrically hyperbolic.

### 20. Nimbus Studio reproduces reference BCI decoding pipelines: a validation study on public benchmarks across protocols and paradigms

- 作者：Sergey Musienko｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13894v1

### 背景/问题
Nimbus Studio is a visual pipeline platform for brain-computer interface (BCI) experiments: researchers assemble preprocessing, feature extraction, decoding, and evaluation over public benchmark datasets or their own recordings, with cross-validated evaluation protocols (including leave-one-subject-out), BIDS export, and bring-your-own Python model classes. Whether its numbers can be trusted is a fair question for any such platform.

### 方法
Nimbus Studio is a visual pipeline platform for brain-computer interface (BCI) experiments: researchers assemble preprocessing, feature extraction, decoding, and evaluation over public benchmark datasets or their own recordings, with cross-validated evaluation protocols (including leave-one-subject-out), BIDS export, and bring-your-own Python model classes. The stochastic deep models agreed within seed-to-seed training variability, estimated with multi-seed reruns on each side.

### 实验/数据
Nimbus Studio is a visual pipeline platform for brain-computer interface (BCI) experiments: researchers assemble preprocessing, feature extraction, decoding, and evaluation over public benchmark datasets or their own recordings, with cross-validated evaluation protocols (including leave-one-subject-out), BIDS export, and bring-your-own Python model classes. We answer it with a parity study: six standard BCI decoding pipelines (CSP+LDA, Riemannian MDM, tangent-space logistic regression through the platform's bring-your-own-code node, P300 xDAWN+LDA, and the deep ShallowConvNet and EEGNet) were evaluated on three public datasets (motor-imagery BNCI-2014-001/004; P300 BNCI-2014-009) under two protocols (per-subject session holdout and pooled leave-one-subject-out cross-validation via the platform's planned-CV driver), once through Nimbus Studio's execution engine and once through independent, hand-written reference implementations built directly on MNE-Python, scikit-learn, pyriemann, and braindecode.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The platform is available at https://studio.nimbusbci.com/, and the complete harness and per-subject results accompany this paper for independent verification.

### 21. Unifying spherical convolutions through lifting

- 作者：J. D. McEwen｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13892v1

### 背景/问题
We develop a unified description of convolution on the sphere by lifting to the rotation group. A number of definitions of spherical convolution have been proposed, differing in whether the kernel is axisymmetric or directional, whether the output is on the sphere or the rotation group, whether the signals carry spin, and in their computational cost.

### 方法
We develop a unified description of convolution on the sphere by lifting to the rotation group. A number of definitions of spherical convolution have been proposed, differing in whether the kernel is axisymmetric or directional, whether the output is on the sphere or the rotation group, whether the signals carry spin, and in their computational cost. We present harmonic-space algorithms for the exact and efficient computation of lifted spherical convolutions of band-limited fields by appealing to sampling theorems on the sphere and rotation group.

### 实验/数据
Regarding the sphere as the homogeneous space $S^2 \cong \text{SO(3)}/\text{SO(2)}$, we lift a spin $s$ field to the rotation group, convolve on $\text{SO(3)}$, and project back to the sphere through the adjoint of the lift for a potentially different spin $s'$. For maps between fields of fixed input and output spin, we prove that directional kernels, output on the sphere and equivariance cannot be achieved simultaneously. We make explicit that spin fields are sections of associated line bundles, linking the physics and bundle literatures, and express the spin rotation phase as the character of the twist of the section.

### 结果
We develop a unified description of convolution on the sphere by lifting to the rotation group. Regarding the sphere as the homogeneous space $S^2 \cong \text{SO(3)}/\text{SO(2)}$, we lift a spin $s$ field to the rotation group, convolve on $\text{SO(3)}$, and project back to the sphere through the adjoint of the lift for a potentially different spin $s'$. We recover every rotation-equivariant convolution considered previously through constraints on the kernel, spin choices and inclusion or omission of the lift and projection.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we illustrate the operators on fields measured on the Earth and on the celestial sky.

### 22. Counterexamples to Minkowski-type inequalities and the Rees converse for modules via mixed Buchsbaum-Rim Multiplicities

- 作者：V. H. Jorge Perez｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13888v1

### 背景/问题
In this paper, we explore mixed Buchsbaum--Rim multiplicities of finite-colength submodules of free modules over Noetherian local rings. We extend the Hilbert-polynomial construction to submodules in arbitrary homogeneous degrees and prove a product formula for the resulting coefficients.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The general converse problem in dimension at least two is stated at the end.

### 23. Ground states and sharp logarithmic Sobolev inequalities for logarithmic Schrödinger equations with partial confinement

- 作者：Baihong Li, Jarosław Mederski, Xiangjian Zeng｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13887v1

### 背景/问题
We study the logarithmic Schrödinger equation with an arbitrary positive semidefinite quadratic potential and a periodic potential in the unconfined directions. The main variational difficulty is to turn a constrained minimizer into a critical point when the energy is extended-valued and not of class $C^1$ on the natural Hilbert space.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
When the periodic component is constant, we also establish existence and classify all normalized ground states at every prescribed positive mass, with explicit formulas for the minimum energy and the associated Lagrange multiplier.

### 24. Bicycle Race: small two-block codes on the Pareto frontier

- 作者：Gideon Lee｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13880v1

### 背景/问题
Two-block group-algebra codes are among the simplest quantum LDPC codes, and many of them are translation invariant on a twisted torus, which suits neutral-atom arrays and other platforms with movable qubits. We ask how far they go at small sizes when searched systematically across all groups.

### 方法
未在摘要中明确给出。

### 实验/数据
Using the group algebra and the census data to steer a statistical search finds four to fifteen times as many good codes as uniform draws in equal time. All codes are available in a public database.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
All codes are available in a public database.

### 25. Precision Tokenization for Multi-Modal Data in High Energy Physics

- 作者：Jeffrey Krupa, Samuel Klein, Nilotpal Kakati, Daniel Murnane, Baran Hashemi, Eilam Gross, Lukas Heinrich, Michael Kagan｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13876v1

### 背景/问题
Foundation models have recently gained significant attention in fields such as high energy physics (HEP). The tokenizers that convert detector data into discrete inputs for such models, however, are comparatively unexplored.

### 方法
Foundation models have recently gained significant attention in fields such as high energy physics (HEP). The tokenizers that convert detector data into discrete inputs for such models, however, are comparatively unexplored. We demonstrate the approach on four modalities covering two different simulated detectors that vary in complexity.

### 实验/数据
Foundation models have recently gained significant attention in fields such as high energy physics (HEP). The tokenizers that convert detector data into discrete inputs for such models, however, are comparatively unexplored. This paper addresses this gap by learning discrete and compressed tokenized representations of HEP datasets.

### 结果
Foundation models have recently gained significant attention in fields such as high energy physics (HEP).

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also present heptokens, an open-source library for tokenizing HEP data.

### 26. Modular Properties of Generalised Gibbs Ensembles: The Deformed KdV Hierarchy

- 作者：Faisal Karimi｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13875v1

### 背景/问题
We construct a set of conserved charges which are deformations of quantum KdV charges. They are associated with the modular transformation of a GGE with the spin-$σ$ KdV charge inserted with chemical potential $α_σ$.

### 方法
We show that the eigenvalues of these deformed charges can be obtained from the thermodynamic Bethe Ansatz in two models. In the Lee-Yang model, we find numerical agreement through cubic order in the spin-$5$ deformation for the first few charges evaluated on low-lying states.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In the Lee-Yang model, we find numerical agreement through cubic order in the spin-$5$ deformation for the first few charges evaluated on low-lying states.

### 27. No advantage from classical assistance for energy-constrained bosonic dephasing channels

- 作者：Amir Arqand, Graeme Smith｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13854v1

### 背景/问题
We prove that four capacities of single-mode bosonic dephasing channels coincide under an average photon-number constraint: the unassisted quantum capacity, the unassisted private capacity, the two-way classically assisted quantum capacity, and the two-way public-classically assisted private capacity. The assistance may be interactive: the parties can exchange classical messages between channel uses and choose subsequent inputs based on earlier outcomes.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also show that both chain rules are attained by canonical purifications of finite-energy Fock-diagonal states.

### 28. Clique and chromatic numbers of graph powers: spectral bounds and anticodes

- 作者：Aida Abiad, Gabriel Coutinho, Hitesh Kumar, Emanuel Juliano, Michael Tait｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13852v1

### 背景/问题
Using spectral and polynomial methods, we show several sharp spectral bounds for the clique and chromatic numbers of graph powers that only use spectral information from the original graph. In particular, we strengthen earlier spectral-radius estimates to obtain an asymptotically sharp colouring bound for general graph powers, and prove a sharp bound for powers of line graphs with a complete characterisation of equality.

### 方法
Regarding the connection between the clique and coloring parameters of graph powers, we propose a spectral analogue of Wegner's conjecture, determine the extremal values for graph squares, and establish the conjecture for all powers when the spectral-radius bound is sufficiently small.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we connect our spectral polynomial method with coding theory: we prove that for distance-regular graphs, optimisation over the adjacency algebra recovers Delsarte's linear programming bound for anticodes.

### 29. Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge Update Efficiency

- 作者：Sheng Zhao, Yuhao Zhu｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13835v1

### 背景/问题
An ideal (language) model must continually update its knowledge. Existing work largely focuses on making these updates efficient after training.

### 方法
An ideal (language) model must continually update its knowledge. Models trained on chronologically ordered knowledge specialize in the most recently encountered knowledge; we call them specialists. In contrast, models trained on the same knowledge in randomly shuffled order perform well across all represented time periods; we call them generalists.

### 实验/数据
Guided by these findings, we design a strategy for organizing pre-training data that preserves stable historical knowledge while enabling efficient updates to current knowledge.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Project page: https://horizon-lab.org/specialist/

### 30. Bourgain-Rosenthal-Schechtman spaces in rearrangement-invariant and Hardy spaces

- 作者：Konstantinos Konstantos, Pavlos Motakis, Thomas Speckhofer｜年份：2026｜发布时间：2026-10-09｜来源：arxiv｜相关度分：**2.24**
- 链接：https://arxiv.org/abs/2610.13833v1

### 背景/问题
In 1981, Bourgain, Rosenthal, and Schechtman constructed uncountably many pairwise non-isomorphic complemented subspaces of $L_p$ for $1 < p < \infty$, $p \neq 2$. We extend their construction to rearrangement-invariant spaces and Hardy spaces.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
On the other hand, we give sufficient conditions which imply that in certain spaces close to $L_1$ and $H^1$, these subspaces fail to be complemented.
