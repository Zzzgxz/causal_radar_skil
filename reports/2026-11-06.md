# CausalRadar 日报 - 2026-11-06

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Muir: Linear Attention with Sensitivity-Allocated Gating and Matched-Filter Readout

- 作者：Tushaar Gangavarapu, Gil Tabak, Clemens JS Schaefer｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**8.50**
- 链接：https://arxiv.org/abs/2611.08376v1

> 命中：hit_title=['CATE']；hit_abstract=['CATE']

### 背景/问题
Linear attention compresses context into a fixed-size key-value state for linear-time training and constant-memory inference. Gated delta-rule models decay this state and erase its prediction for an incoming key before writing a new value; Gated DeltaNet-2 (GDN-2) generalizes this with channel-wise decay and decoupled, full-rank erase and write gates.

### 方法
Gated delta-rule models decay this state and erase its prediction for an incoming key before writing a new value; Gated DeltaNet-2 (GDN-2) generalizes this with channel-wise decay and decoupled, full-rank erase and write gates.

### 实验/数据
未在摘要中明确给出。

### 结果
Across 166M-1.34B parameters, Muir lowers perplexity by 1.8-2.0% over GDN-2 and 2.5-3.6% over Transformer, raises commonsense accuracy by up to 1.9 points, and improves extractive recall over GDN-2. At 1.34B, Muir outperforms both baselines on multi-hop and multi-needle recall, extrapolates 2,560x from its 4K training length to 10M-token streams without perplexity drift, and maintains near-100% passkey retrieval to 1M tokens with static readout.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Muir achieves these gains while matching GDN-2 throughput, reaching its 100B-token validation loss 1.2x faster, and training 2.7x faster than Transformer at 32K.

### 2. Polarity Classification with Multitask Learning Syntax Augmentation

- 作者：Muhammad Imran, Carlos Gómez-Rodríguez｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**7.00**
- 链接：https://arxiv.org/abs/2611.08323v1

> 命中：hit_scenario=['ads']；hit_abstract=['CATE']

### 背景/问题
Sentiment Analysis (SA) is a fundamental NLP task concerned with the identification and categorization of subjective information in text. While lexicon-based methods offer transparency, they often struggle with linguistic phenomena such as negation and intensification.

### 方法
We propose and compare two strategies for integrating syntactic knowledge into a neural sentiment analysis model under unified Multi-Task Learning (MTL).

### 实验/数据
We evaluate eleven datasets spanning seven languages---the MARC corpus (English, Spanish, French, German) and seven datasets from SemEval-2022 Task 10 (English, Spanish, Norwegian, Basque, Catalan)---using four established SEL encodings. With the relative encoding, Contrastive-MTL outperforms a syntax-naive baseline on 10 of 11 datasets and surpasses the external rule-based pipeline (SELSP) that parses at inference on all six datasets where the latter applies, while being 1.5--9$\times$ faster at evaluation. Standard-MTL is more dataset- and encoding-dependent.

### 结果
Syntactic parsing has been integrated into SA pipelines to address this, but conventional parsers introduce significant computational overhead. Recent work shows that reformulating dependency parsing as a Sequence Labeling (SEL) task can improve efficiency. With the relative encoding, Contrastive-MTL outperforms a syntax-naive baseline on 10 of 11 datasets and surpasses the external rule-based pipeline (SELSP) that parses at inference on all six datasets where the latter applies, while being 1.5--9$\times$ faster at evaluation.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results show implicit syntactic supervision during training can match or exceed explicit parsing at inference without computational overhead.

### 3. Spectral Regimes of Truncated sinc-Power and Pulse-Train Kernels: Edge Exponents, Per-Edge Plunges, and the Landau-Widom Limit

- 作者：Unnikrishna Pillai｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**6.50**
- 链接：https://arxiv.org/abs/2611.08401v1

> 命中：hit_title=['CATE']

### 背景/问题
A signal band-limited to one rectangular band and observed through a finite window is the classical concentration problem of Slepian, Landau, Pollak, and Widom. The eigenvalues of the operator cluster near one and near zero, separated by a transition called the plunge.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
For the single band, classical results place all eigenfilter zeros on the unit circle, with more of them inside the band as the order rises, so the dominant eigenvectors act as lowpass filters.

### 4. OraRefer: Segmentation-Guided Multi-Photograph Fusion for Oral Cancer Screening with Guaranteed Patient-Level Sensitivity

- 作者：Rupam Mukherjee, Mehakdeep Singh, Shirin Dasgupta, Subhamoy Mandal｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**5.00**
- 链接：https://arxiv.org/abs/2611.08360v1

> 命中：hit_scenario=['ads']

### 背景/问题
Oral cancer and the oral potentially malignant disorders (OPMD) that can precede it are visible on the oral mucosa, which makes smartphone photographs a promising tool for screening. Deep learning models for this task classify individual photographs.

### 方法
Deep learning models for this task classify individual photographs. We propose OraRefer, a patient-level screening model that reads each photograph with a segmentation-guided foundation model that conditions its class decision on the predicted lesion, combines all photographs of a patient with risk factors, and refers through a threshold with a finite-sample sensitivity guarantee. The model localizes the mouth itself, so inference needs no annotation.

### 实验/数据
未在摘要中明确给出。

### 结果
On 3000 photographs of 714 patients, patient-level fusion reaches an AUROC of 0.919 and outperforms attention-based multiple-instance learning.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Because the threshold is calibrated without retraining, each clinic can set its own guaranteed operating point on a local calibration sample.

### 5. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization

- 作者：Qile Jiang, George Em Karniadakis｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.08483v1

> 命中：hit_abstract=['CATE']

### 背景/问题
LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for each round and must repeat this generation many times to maintain population diversity.

### 方法
We present SwarmEvolve, a framework in which hundreds of low-cost agents per round work in swarms, reason in latent space without decoding to text, and share information by passing KV caches. On 21 problems in mathematical discovery and scientific computing, SwarmEvolve gets the highest average score and needs a median of only 3 to 8 minutes to reach the best scores that other state-of-the-art frameworks reach in 60 minutes. Our work shows that agent swarms that communicate in latent space offer a fast, low-cost approach to program search for scientific problems.

### 实验/数据
未在摘要中明确给出。

### 结果
LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. On 21 problems in mathematical discovery and scientific computing, SwarmEvolve gets the highest average score and needs a median of only 3 to 8 minutes to reach the best scores that other state-of-the-art frameworks reach in 60 minutes. On several problems, SwarmEvolve with Qwen3 8B improves on the solutions that AlphaEvolve first found with frontier LLMs.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our work shows that agent swarms that communicate in latent space offer a fast, low-cost approach to program search for scientific problems.

### 6. Same Behavior, Different Mechanism: What Finite Experiments Can Certify About Integrated Information

- 作者：Linqian Wu, Diaoxuan He｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.08469v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Interpretability, AI auditing and assessments of machine consciousness increasingly rest on mechanism-level quantities: functionals of a system's causal transition law that describe how it computes, not what it outputs. Experiments see that law only through finite, partial and noisy interventions.

### 方法
The measure has sharp edges: because $\varphi$ selects a partition, and the cause and effect it specifies, by one criterion and reports another, infinitesimal changes of mechanism that cross an edge change it by 25-100% at 99% of the edges we found in random networks, and about 1% of surrogate models that fit interventional data almost perfectly misreport it by more than 20%.

### 实验/数据
Experiments see that law only through finite, partial and noisy interventions. We ask when such a quantity is identifiable from an experiment's access, continuous in the mechanism and certifiable from finite data, and answer exactly for a deliberately demanding case - the integrated information $\varphi$ of integrated information theory - in stochastic networks of four and five units with known ground truth. The measure has sharp edges: because $\varphi$ selects a partition, and the cause and effect it specifies, by one criterion and reports another, infinitesimal changes of mechanism that cross an edge change it by 25-100% at 99% of the edges we found in random networks, and about 1% of surrogate models that fit interventional data almost perfectly misreport it by more than 20%.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Measurability is thus a design question with computable answers.

### 7. Synaptic Multi-Weight Wafer-Scale Domain Wall Magnetic Tunnel Junctions Driven by Spin Orbit Torque

- 作者：Nicholas Zogbi, Domenico Giuliano, Vaishnavi Kateel, Van Dai Nguyen, Jyotirmoy Chatterjee, Alvaro Palomino, Robert Carpenter, Siddharth Rao 等｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.08405v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Spintronic synaptic devices based on magnetic random access memory (MRAM) are a rapidly evolving class within the analog neuromorphic architecture. However, obtaining the multi-weight or analog behavior desired for improved neural network inference accuracy in scaled MRAM remains a challenge.

### 方法
未在摘要中明确给出。

### 实验/数据
By varying the applied in-plane field, multi-weight resistance states emerge through domain wall nucleation and pinning. Electromagnetic simulations indicate the multiple states are due to domain wall nucleation mediated by in-plane field and applied voltage. Implementation of the measured multi-weight devices in a neural network yields a 96.1% inference accuracy using the MNIST dataset if all devices provide the same number of multi-weight states.

### 结果
However, obtaining the multi-weight or analog behavior desired for improved neural network inference accuracy in scaled MRAM remains a challenge.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Overall, this work demonstrates a route towards multi-weight artificial synapse MRAM, establishing a path towards scalable neuromorphic systems based on spintronics.

### 8. RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines

- 作者：Roko Parac, Christos Ziakas, Leo Ardon, Alessandra Russo｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.08308v1

> 命中：hit_abstract=['policy learning']

### 背景/问题
Reward machines (RMs) have been proposed as a reward formulation in reinforcement learning (RL) to capture non-Markovian tasks where credit assignment depends on history. By representing reward functions as automata, RMs expose the task's temporal structure and allow such rewards to be handled within a Markovian framework.

### 方法
Reward machines (RMs) have been proposed as a reward formulation in reinforcement learning (RL) to capture non-Markovian tasks where credit assignment depends on history. By representing reward functions as automata, RMs expose the task's temporal structure and allow such rewards to be handled within a Markovian framework. In this work, we address this limitation by proposing RM-VLM, a novel approach in which a large language model (LLM) generates an RM from a natural-language task description, and a vision-language model (VLM) acts as the labelling function, grounding the RM's propositions over image-based observations during RM-guided policy learning.

### 实验/数据
Our experimental results show that RM-VLM consistently achieves higher task success rates than existing VLM-based reward methods across all tested domains.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our experimental results show that RM-VLM consistently achieves higher task success rates than existing VLM-based reward methods across all tested domains.

### 9. Dualities in one-dimensional quantum lattice models: Lie groups, Schur-Weyl duality and symmetry breaking

- 作者：Dante Bosgoed, Frank Verstraete, Laurens Lootens｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.08293v1

> 命中：hit_abstract=['CATE']

### 背景/问题
We present a systematic framework for gauging continuous symmetries, and show that the Schur-Weyl duality arises naturally as a realization of this construction with open boundary conditions. Restricting to compact Lie group symmetries, we construct dual models for one-dimensional quantum lattice models exhibiting those symmetries.

### 方法
We present a systematic framework for gauging continuous symmetries, and show that the Schur-Weyl duality arises naturally as a realization of this construction with open boundary conditions. Restricting to compact Lie group symmetries, we construct dual models for one-dimensional quantum lattice models exhibiting those symmetries. With closed boundary conditions, we can relate the full spectrum of these dual theories by considering all possible twisted boundary conditions.We illustrate how the Peter-Weyl transform appears when the duality acts on the boundary Hilbert space of a $G$-symmetric model.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We illustrate these results for $U(1)$- and $SU(2)$-symmetric quantum lattice models.

### 10. Latent RL Priors for Data-Efficient Dexterous Manipulation

- 作者：Yixiao Wang, Peiyi Chen, Mustafa Mukadam, Shreekant Gayaka, Masayoshi Tomizuka, Son Tran｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**4.50**
- 链接：https://arxiv.org/abs/2611.08458v1

> 命中：hit_abstract=['policy learning']

### 背景/问题
Learning dexterous manipulation from limited visual demonstrations is challenging because policies must acquire both perceptual grounding and precise control, while reinforcement learning (RL) in simulation can acquire rich control behaviors from large-scale interaction with privileged information. We introduce \textbf{Latent RL Prior}, a two-stage framework that reuses this control knowledge for data-efficient visual policy learning.

### 方法
We introduce \textbf{Latent RL Prior}, a two-stage framework that reuses this control knowledge for data-efficient visual policy learning. Across three simulated tasks, our method outperforms full-parameter fine-tuning of $π_{0.5}$ and GR00T N1.7 in the low-data regime; on door lifting and bimanual assembly, it surpasses full-data baselines using $10\times$ and $5\times$ fewer demonstrations, respectively.

### 实验/数据
Learning dexterous manipulation from limited visual demonstrations is challenging because policies must acquire both perceptual grounding and precise control, while reinforcement learning (RL) in simulation can acquire rich control behaviors from large-scale interaction with privileged information. We introduce \textbf{Latent RL Prior}, a two-stage framework that reuses this control knowledge for data-efficient visual policy learning. Across three simulated tasks, our method outperforms full-parameter fine-tuning of $π_{0.5}$ and GR00T N1.7 in the low-data regime; on door lifting and bimanual assembly, it surpasses full-data baselines using $10\times$ and $5\times$ fewer demonstrations, respectively.

### 结果
Across three simulated tasks, our method outperforms full-parameter fine-tuning of $π_{0.5}$ and GR00T N1.7 in the low-data regime; on door lifting and bimanual assembly, it surpasses full-data baselines using $10\times$ and $5\times$ fewer demonstrations, respectively. Further analysis shows that direct visual-to-latent conditioning improves adaptation performance and training stability over routing visual predictions through the pretrained state encoder.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Project website: https://yixiaowang7.github.io/latent-rl-prior-page/.

### 11. Do You Miss the Nights We Spent Crafting Figures? Rethinking Teaser and Framework Figures in the Age of Generative AI

- 作者：Xiaoqi Zhao, Youwei Pang, Kailai Zhou｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08486v1

### 背景/问题
Scientific figures give research ideas a visual form through choices of abstraction, composition, and emphasis. Generative AI offers new ways to realize these choices, raising questions about explanatory clarity and purposeful visual expression.

### 方法
We examine these questions through a visual retrospective of 371 motivation and framework figures from 200 papers. Gains in the six-dimension average are larger for main-sample motivation figures than for frameworks. These model-based findings support researcher-led design, with AI assisting exploration and authors retaining responsibility for explanatory purpose, composition, and scientific relationships.

### 实验/数据
未在摘要中明确给出。

### 结果
Revisions increase mean clarity ratings by 0.428 points and decrease aesthetic coherence ratings by 0.111 points on a five-point scale.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The accompanying atlas and evaluation records are available at https://ntu-ai4x.github.io/Rethinking_Figures/index_en.html.

### 12. Joint Bayesian Inference for Extraction of Charmonium Long Distance Matrix Elements Using PYTHIA

- 作者：Yubo Liu, Rongrong Ma｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08463v1

### 背景/问题
We present a joint Bayesian extraction of the nonrelativistic QCD long-distance matrix elements (LDMEs) for $J/ψ$, $ψ(2S)$, and $χ_c$ production, using short-distance coefficients and feed-down structure implemented in PYTHIA 8.317. Rather than fitting each charmonium state separately, we construct channel-resolved responses that link parent production to daughter feed-down and infer all LDMEs simultaneously from 286 prompt charmonium measurements in $pp$ collisions at $\sqrt{s}=5.02$-13 TeV at the LHC.

### 方法
We present a joint Bayesian extraction of the nonrelativistic QCD long-distance matrix elements (LDMEs) for $J/ψ$, $ψ(2S)$, and $χ_c$ production, using short-distance coefficients and feed-down structure implemented in PYTHIA 8.317.

### 实验/数据
The extracted LDMEs provide a good description of the data, with an overall $χ^2/\mathrm{ndf}=1.18$. Using the extracted LDMEs, we predict prompt $J/ψ$ and $ψ(2S)$ cross sections at high transverse momentum in $pp$ collisions at $\sqrt{s}=200$ GeV, which can be tested with RHIC data.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Using the extracted LDMEs, we predict prompt $J/ψ$ and $ψ(2S)$ cross sections at high transverse momentum in $pp$ collisions at $\sqrt{s}=200$ GeV, which can be tested with RHIC data.

### 13. ReproBridge: Building Reproducibility into ML Research Artifacts

- 作者：Yubo Wang, Rui Meng, Jaehyun Nam, Tomas Pfister, Jinsung Yoon｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08452v1

### 背景/问题
Reproducing machine learning experiments requires reconstructing procedures from information scattered across papers, released code, and supporting artifacts. For coding agents, reproduction success can therefore depend on their ability to fill in missing details, rather than on the released artifacts alone.

### 方法
Across four evaluated models, refined artifacts raise mean reproduction success from 76.4% to 92.6% and reduce downstream API spending by 19.7% on average. The cross-model success-rate spread narrows from 21.6 to 3.9 percentage points, with all four models achieving mean success rates above 90%. These results suggest that preserving execution knowledge helps even models with lower raw-code success reproduce experiments more reliably and at lower API cost.

### 实验/数据
Reproducing machine learning experiments requires reconstructing procedures from information scattered across papers, released code, and supporting artifacts. We define a standardized artifact design comprising a refined codebase, environment setup, experiment launchers, and a reproduction guide, and introduce ReproBridge, an agent workflow for constructing these refined reproducible artifacts. ReproBridge-Bench provides 1,029 tasks from 387 experiments across 36 papers, anchored by five human-verified reference scores per task.

### 结果
We ask whether preserving recovered procedures and decisions improves subsequent independent reproduction.

### 结论/启示（面向电商发券、定价、营销算法等应用）
These results suggest that preserving execution knowledge helps even models with lower raw-code success reproduce experiments more reliably and at lower API cost.

### 14. Gelfand numbers of Schatten class embeddings in the quasi-Banach range

- 作者：Joscha Prochno｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08448v1

### 背景/问题
We prove Conjecture 1.4 of Prochno and Strzelecki [J. Approx.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The proof is deterministic and is based on Hilbert--Schmidt projections on rectangular matrix spaces.

### 15. Label-Wording Augmentation in a Typed-Decision Encoder: Gains on Unfamiliar Words, Not on Abbreviations or Codes

- 作者：Vladimir Beskorovainyi｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08439v1

### 背景/问题
Typed-decision models score options that the caller supplies at request time, so their accuracy depends on label wording that the model's developer does not control. We compare two releases of a 307M-parameter multilingual cross-encoder, Ru-Jev, trained on thirteen Russian-language tasks; the later release adds an augmentation that presents labels in several surface forms.

### 方法
Typed-decision models score options that the caller supplies at request time, so their accuracy depends on label wording that the model's developer does not control.

### 实验/数据
Holding questions fixed and varying only how eighteen routing labels are worded, we evaluate ten label vocabularies, produced by three separate processes and checked for overlap with the training data, with five candidates per question and, for eight of them, also with eighteen. On two datasets neither release saw, accuracy moves by -8.4 and +5.6 points.

### 结果
On abbreviations and opaque codes it gives no usable gain: on abbreviations it is not better, and worse on the clean slice, and on opaque codes both releases stay at or below chance once labels related to training options are removed.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also report four evaluation hazards from comparing the two releases.

### 16. Torsion talks only to spin: the CMB temperature as a test of energy exchange in Einstein-Cartan cosmology

- 作者：Fernando Izaurieta, Samuel Lepe, Cristian Quinzacara｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08422v1

### 背景/问题
The cosmic microwave background temperature at $z=0.886$ is known to $2\%$ from molecular absorption towards PKS~1830$-$211; CO absorbers and Sunyaev-Zel'dovich clusters extend the measurement to $z\simeq3$. We use them on a question that cosmologies with torsion leave open.

### 方法
If the photons stay a blackbody, as FIRAS requires of any source set by local conditions, the model predicts a background colder than $T_{0}(1+z)$ by $7\%$ at $z\simeq0.9$ and by $8.5\%$ at $z\gtrsim3$, with no free parameter.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
If dark matter carries the spin instead, $H(z)$ moves by less than $10^{-4}$ below $z=3$ at the fitted parameters and $T(z)$ is standard again.

### 17. Low-Temperature Sampling via Equilibrium Disagreements

- 作者：Andreas Galanis, Daniel Stefankovic｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08416v1

### 背景/问题
We develop a new framework for sampling at low temperatures using Glauber dynamics. In this regime, the coexistence of competing modes (commonly referred to as phases) creates bottlenecks that can make worst-case mixing exponentially slow.

### 方法
We develop a new framework for sampling at low temperatures using Glauber dynamics. The main new ingredient in our framework is to relate convergence within a phase to the geometry of disagreements between two independent configurations drawn from that phase. As applications of our approach, we consider three canonical models on random regular graphs that have been central to low-temperature sampling, and establish fast convergence from natural initialisations of Glauber dynamics for every fixed degree.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also give an $n^{2+o(1)}$-time algorithm that combines phase samples into samples from the full distribution, avoiding in particular time-costly approximations of the corresponding partition functions to the target sampling accuracy.

### 18. Shades and Convexity of Hypersurfaces

- 作者：Mohammad Ghomi｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08415v1

### 背景/问题
Let $f\colon M^n\to\mathbf{R}^{n+1}$, $n\geq2$, be a smooth immersion of a closed oriented manifold, with Gauss map $ν\colon M\to\mathbf{S}^n$. For each unit vector $u$, the shade $S_u\subset M$ is the set of points where $ν$ makes an acute angle with $u$.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Wente in all dimensions.

### 19. A Multimodal Haptic Interface for Simultaneous Softness and Thermal Modulation

- 作者：Joshua Brown, Fernando Bello, Lynette Jones｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08398v1

### 背景/问题
Haptic interactions, such as touching an object in virtual reality, involve detecting a plethora of sensations through the skin. Whilst tactile displays exist to simulate and manipulate all of these cues individually, little progress has been made constructing devices that can control multiple cues simultaneously.

### 方法
未在摘要中明确给出。

### 实验/数据
This work advances the design of multimodal tactile displays with applications to perceptual research, medical simulation, and affective haptics.

### 结果
Mechanical evaluations demonstrate controllable stiffness increase of 300%, whilst thermal characterisation showed strong surface uniformity and a range of achievable temperatures from 10°C up to 50°C, with closed-loop control maintaining a 0.2°C error from a setpoint.

### 结论/启示（面向电商发券、定价、营销算法等应用）
This work advances the design of multimodal tactile displays with applications to perceptual research, medical simulation, and affective haptics.

### 20. Recalibration-Aware Optimization of ZEFOZ Operating Points in $^{167}\mathrm{Er}^{3+}:\mathrm{Y}_2\mathrm{SiO}_5$ for Quantum Memories

- 作者：Shashank Srivastava｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08396v1

### 背景/问题
Erbium-doped solids like $^{167}\mathrm{Er}^{3+}:\mathrm{Y}_2\mathrm{SiO}_5$ have properties that make them suitable for quantum-network memories, however, their unquenched effective electronic spin causes rapid magnetic decoherence. Operating at Zero First-Order Zeeman (ZEFOZ) points allows us to mitigate this, where we evaluate the ZEFOZ landscape for Site-2 $^{167}\mathrm{Er}^{3+}$ by incorporating a full-Hessian spin-Hamiltonian treatment with the anisotropic magnetic-field covariance derived from the native $^{89}\mathrm{Y}$ crystal lattice directly.

### 方法
Operating-point screening criteria were adopted to devise a Pareto-optimal frontier of four transition pairs to balance modeled Y-only magnetic pure-dephasing lifetimes ($T_{φ,Y}^{(2)}$) against microwave control authority. The $ε_{14}\leftrightarrowε_{15}$ transition exhibits the longest modeled Y-bath-induced quadratic pure-dephasing time, $T_{φ,Y}^{(2)}>2.2\times10^5~\mathrm{s}$, while the $ε_{12}\leftrightarrowε_{13}$ transition stood out, achieving a Rabi frequency coefficient of $1.248 \times 10^5~\mathrm{Hz/mT}$. The intended operation near $10~\mathrm{mK}$ must be taken into account for the suppression of Er-induced spectral diffusion through electronic-spin polarization, while the extended Y-bath pure-dephasing timescales also remain conditional on the adopted temporal-correlation model.

### 实验/数据
Operating at Zero First-Order Zeeman (ZEFOZ) points allows us to mitigate this, where we evaluate the ZEFOZ landscape for Site-2 $^{167}\mathrm{Er}^{3+}$ by incorporating a full-Hessian spin-Hamiltonian treatment with the anisotropic magnetic-field covariance derived from the native $^{89}\mathrm{Y}$ crystal lattice directly. An assumption-based Hamiltonian-uncertainty analysis demonstrates that while uncompensated deviations shift the ZEFOZ condition away from its nominal magnetic-field coordinate, the shifted operating points can be recovered via numerical vector-field recalibration. The Pareto-optimal coordinates were mathematically recovered for all sampled Hamiltonian perturbations, and the $84.1^{\mathrm{st}}$-percentile field relocations ranged from $10.95$ to $27.97~\mathrm{mT}$.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The intended operation near $10~\mathrm{mK}$ must be taken into account for the suppression of Er-induced spectral diffusion through electronic-spin polarization, while the extended Y-bath pure-dephasing timescales also remain conditional on the adopted temporal-correlation model.

### 21. Extensions to the Navier-Stokes-Fourier Equations for Rarefied Transport: Entropy Variable Formulation, Heat Transfer and Dispersion of a Non-Linear Entropy Stable Closure

- 作者：Frimpong A. Baidoo, Narayana R. Aluru, Thomas J. R. Hughes, Michael R. A. Abdelmalik｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08395v1

### 背景/问题
We assess the non-linear version of the Entropy Stable Extension to the Navier-Stokes-Fourier equations which were originally derived in arXiv:2407.17334. Using an identity for the derivative of the inverse of linearized collision operator, we show that the Entropy Stable Extension takes the form of a fourth-order quasi-cubic system of equations when written in entropy variables.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
This quasi-linear approximation is applied to the stationary heat transfer between parallel plates where we find that a specification of the boundary conditions that interpolates between the continuum and collisions limits can yield temperature profiles that better agree with DSMC predictions than Navier-Stokes-Fourier equations with Smoluchowski boundary conditions, while also giving a heat flux prediction that better agrees with the Sherman-Lees heat flux than the Navier-Stokes-Fourier prediction.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We conclude with a brief study of dispersion of plane waves according to the linearized equations in one dimension where we show that all frequency modes are stable and relate this to entropy stability.

### 22. Algorithmic Construction of Vector-Valued Modular Forms and Application to an $A_4\times\mathbb{Z}_4$-invariant Model of Leptons

- 作者：Q. Bonnefoy, M. Rausch de Traubenberg, V. Saulquin｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08387v1

### 背景/问题
We present an algorithmic procedure that constructs the Vector-Valued Modular Forms (VVMFs) of finite modular groups, as well as its implementation in a companion code. The usual method consists in building the first few VVMFs, whose tensor products then generate the others.

### 方法
We present an algorithmic procedure that constructs the Vector-Valued Modular Forms (VVMFs) of finite modular groups, as well as its implementation in a companion code. We address the difficulty of systematically finding the minimal set of VVMFs that suffices to produce all higher-weight ones, and we propose a method to identify it that makes use of the Burnside-Brauer theorem. Our approach reproduces the known results for the finite modular groups explored in the recent phenomenological literature on modular flavor symmetries, and works for additional groups which we tested.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We illustrate our algorithm and the working of our code by studying a model of leptons based on the unexplored finite modular group $A_4\times\mathbb{Z}_4$.

### 23. Hybrid Machine Learning for Imbalanced Landing-Phase Safety Event Prediction from Flight Data

- 作者：Taha Asghar, Bilal Mufti, Syed Qasim Zaheer, Luqman Ahmed｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08386v1

### 背景/问题
Landing-phase safety-event prediction requires the detection of rare abnormal approaches within strongly imbalanced multivariate flight data. Capturing coupled temporal behavior while distinguishing event-specific signatures across airport operating contexts remains a central modeling challenge.

### 方法
Landing-phase safety-event prediction requires the detection of rare abnormal approaches within strongly imbalanced multivariate flight data. Capturing coupled temporal behavior while distinguishing event-specific signatures across airport operating contexts remains a central modeling challenge. This study proposes an interpretable hybrid feature-fusion framework for multiclass landing-phase safety-event prediction.

### 实验/数据
Landing-phase safety-event prediction requires the detection of rare abnormal approaches within strongly imbalanced multivariate flight data. Airport-level comparisons reveal benefits from local specialization at the two airports with larger datasets and from pooled training at the airport with the smallest dataset. The framework provides an interpretable approach to rare-event detection and practical guidance for adapting flight-data monitoring models to airport-level data availability.

### 结果
Component comparisons establish the importance of class weighting and show that continuous feature fusion outperforms reconstruction-error-only and hard-gate alternatives.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The framework provides an interpretable approach to rare-event detection and practical guidance for adapting flight-data monitoring models to airport-level data availability.

### 24. Space of Geometric Gibbs Measures: Uniqueness, Ergodicity, and Teichmüller Complex Manifold Structure

- 作者：Yunping Jiang｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08384v1

### 背景/问题
Building on our previous work, in which geometric Gibbs measures were introduced to complete the space of classical Gibbs measures under the Teichmüller metric, we establish the uniqueness of geometric Gibbs measures in this paper. This result completes the construction of a Teichmüller complex manifold structure on the space of all geometric Gibbs measures.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Finally, we establish a foundation for the systematic study of the ergodic properties of geometric Gibbs measures.

### 25. FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous Federated Learning

- 作者：Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08383v1

### 背景/问题
Federated learning servers combine client models with a fixed aggregation rule, and each rule in common use is designed for one kind of heterogeneity. We study whether a large language model (LLM) that inspects the client models can choose the rule itself, without any training on the server.

### 方法
Federated learning servers combine client models with a fixed aggregation rule, and each rule in common use is designed for one kind of heterogeneity. We study whether a large language model (LLM) that inspects the client models can choose the rule itself, without any training on the server. We evaluated FedReason with Claude Opus 5.5 on CIFAR-10 and CIFAR-100 with ResNet-18 under Dirichlet label skew, width-heterogeneous sub-models and Byzantine clients, in 168 runs against 14 baselines.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
A 60-round run cost 0.79 USD in API fees on average.

### 26. SLA: Scaling Spatial-Language-Action Model via Continual Pre-training

- 作者：Fuhao Li, Wenxuan Song, Qizhou Huang, Ziyang Zhou, Jingbo Wang, Junwu E, Pengwei Wang, Yan Wang 等｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08373v1

### 背景/问题
Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation.

### 方法
Developing spatial understanding as a transferable foundation-model capability therefore calls for learning from broader robot experience. We present SLA, a Spatial-Language-Action Model that scales implicit spatial alignment to continual pre-training and maintains it during downstream post-training. Initialized from a pretrained pi05 policy, SLA jointly optimizes action prediction and alignment between intermediate visual embeddings and spatial representations from a frozen 3D perception model.

### 实验/数据
We curate and unify heterogeneous robot datasets to support spatial learning across diverse embodiments, tasks, and scenes.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
All auxiliary components are used only during training, allowing direct reuse of pretrained VLA weights and preserving the original inference architecture.

### 27. MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation

- 作者：Sateesh Kumar, Arnav Balaji, Arpit Bahety, Skand Peri, Georgios Pavlakos, Roberto Martín-Martín｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08372v1

### 背景/问题
Visuomotor policies trained through imitation learning are highly sensitive to changes in camera viewpoint. This is particularly problematic for mobile manipulation (MoMa), where robots rarely execute manipulation from the exact same base pose used during demonstration collection due to navigation uncertainty, localization drift, and environmental constraints.

### 方法
Recent approaches use novel-view synthesis (NVS) to augment demonstrations with unseen viewpoints, but they assume static scenes and therefore fail to re-render the manipulated object during the post-contact interaction phase, leaving the most critical parts of the demonstration unaugmented. We present MOMASPLAT, a novel-view demonstration augmentation framework for mobile manipulation that synthesizes full manipulation trajectories from unseen robot base poses, including dynamic object interactions. MOMASPLAT combines 3D Gaussian Splatting, feed-forward 3D foundation models, and kinematics-based action retargeting to separately reconstruct the scene and manipulated object, render them from novel viewpoints, and generate geometrically consistent synthetic demonstrations paired with transformed actions.

### 实验/数据
Our key insight is that standard MoMa data collection naturally provides the multiview observations needed to reconstruct both the static scene and the manipulated object in 3D. We evaluate MOMASPLAT on five real-world mobile manipulation tasks involving both rigid and articulated objects across three scenes, and validate the fidelity of its synthesized demonstrations against ground truth in simulation. MOMASPLAT substantially improves robustness to unseen base poses, more than doubling the average success rate of the strongest baseline and maintaining non-trivial success at large base displacements where all baselines fail, while reducing the need for largescale real-world data collection.

### 结果
MOMASPLAT substantially improves robustness to unseen base poses, more than doubling the average success rate of the strongest baseline and maintaining non-trivial success at large base displacements where all baselines fail, while reducing the need for largescale real-world data collection.

### 结论/启示（面向电商发券、定价、营销算法等应用）
MOMASPLAT substantially improves robustness to unseen base poses, more than doubling the average success rate of the strongest baseline and maintaining non-trivial success at large base displacements where all baselines fail, while reducing the need for largescale real-world data collection.

### 28. Lord of the Precision, the Two Floats: Double-Word Arithmetic for Complex Numbers

- 作者：František Stloukal, Fabienne Jézéquel｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08371v1

### 背景/问题
Datacenter GPUs increasingly favour low-precision floating-point formats, offering higher throughput than FP64. Double-word (DW) arithmetic represents numbers as unevaluated sums of two floating-point values, providing higher accuracy.

### 方法
We present the first error analysis of complex DW multiplication and division.

### 实验/数据
Datacenter GPUs increasingly favour low-precision floating-point formats, offering higher throughput than FP64.

### 结果
In the high-energy physics code MadGraph7, FP32-based DW arithmetic achieves up to 2.9x and 2.1x higher throughput than FP64 on NVIDIA L40S and AMD Radeon Pro W7900 GPUs, respectively, while losing approximately 1.4 correct significant digits.

### 结论/启示（面向电商发券、定价、营销算法等应用）
In the high-energy physics code MadGraph7, FP32-based DW arithmetic achieves up to 2.9x and 2.1x higher throughput than FP64 on NVIDIA L40S and AMD Radeon Pro W7900 GPUs, respectively, while losing approximately 1.4 correct significant digits.

### 29. Unifying Central Flow, Rod Flow, and the Edge Coupling

- 作者：Eric Regis, Sinho Chewi｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08358v1

### 背景/问题
At the edge of stability, the iterates of gradient descent oscillate along the sharp directions of the Hessian. This poses a significant challenge for continuous-time models as the usual continuous-time approximation -- the gradient flow -- admits no oscillations.

### 方法
This poses a significant challenge for continuous-time models as the usual continuous-time approximation -- the gradient flow -- admits no oscillations. Several continuous-time models have been proposed to capture the behavior at the edge of stability, among them central flow and rod flow. Although both models can be interpreted as performing a coarse-graining in time, the connection between them remains poorly understood.

### 实验/数据
We verify the derived flows experimentally on representative neural network architectures, where they track the discrete iterates throughout all phases of training -- including the transition from the stable regime to the edge of stability.

### 结果
This poses a significant challenge for continuous-time models as the usual continuous-time approximation -- the gradient flow -- admits no oscillations.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We verify the derived flows experimentally on representative neural network architectures, where they track the discrete iterates throughout all phases of training -- including the transition from the stable regime to the edge of stability.

### 30. Twisted Yangians of quasi-split type DI and Drinfeld type current relations

- 作者：Vidas Regelskis｜年份：2026｜发布时间：2026-11-05｜来源：arxiv｜相关度分：**2.50**
- 链接：https://arxiv.org/abs/2611.08357v1

### 背景/问题
We study the twisted Yangian associated with the quasi-split symmetric pair $(\mathfrak{o}_{2n}, \mathfrak{o}_{n-1}\oplus \mathfrak{o}_{n+1})$ of type DI. Working in the transposed $R$-matrix presentation of arXiv:2607.14692, we show that the generating matrix $S(u)$ admits no Gaussian decomposition.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
With quasi-split type AIII (Lu and Zhang), this completes the explicit comparison for the classical quasi-split types with a nontrivial diagram involution.
