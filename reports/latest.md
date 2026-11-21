# CausalRadar 日报 - 2026-11-21

- 新增条目数：**30**
- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar

## 运行备注
- 未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。

## 今日新增（按相关度排序）

### 1. Complete Test Suites for Effectful Automata

- 作者：Bálint Kocsis, Rick Koenders, Joshua Moerman, Jurriaan Rot｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**6.87**
- 链接：https://arxiv.org/abs/2611.26535v1

> 命中：hit_scenario=['ads']；hit_abstract=['CATE']

### 背景/问题
Complete test suites for automata are (finite) sets of words that enable testing an implementation against a specification: when a (black-box) automaton passes the test suite, completeness guarantees that it is equivalent to the specification on all (infinitely many) words. A well-known method for constructing complete test suites for deterministic automata is the W-method, used in conformance testing and automata learning.

### 方法
Based on a recent categorical generalisation of the W-method, we propose a framework for~the construction and analysis of test suites for a certain class of effectful automata defined by commutative monads. We show how to apply the framework and derive complete test suites for non-deterministic and weighted automata.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We show how to apply the framework and derive complete test suites for non-deterministic and weighted automata.

### 2. Fast, in-place, and ancilla-free quantum algorithms for integer multiplication and inversion

- 作者：David Halpenny, Adithya Sireesh, Petros Wallden｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**4.87**
- 链接：https://arxiv.org/abs/2611.26605v1

> 命中：hit_scenario=['ads']

### 背景/问题
Arithmetic operations are a fundamental building block in the design of quantum algorithms, with their implementation cost expected to have a significant impact on the viability of a wide variety of quantum applications. In this work, we present novel algorithms for a number of in-place quantum arithmetic operations that are highly efficient in terms of their space and gate count overheads compared to the current state-of-the-art.

### 方法
In this work, we present novel algorithms for a number of in-place quantum arithmetic operations that are highly efficient in terms of their space and gate count overheads compared to the current state-of-the-art. We present our multiplication algorithms as consequences of a single unified theorem, which may find further application within quantum arithmetic.

### 实验/数据
未在摘要中明确给出。

### 结果
Arithmetic operations are a fundamental building block in the design of quantum algorithms, with their implementation cost expected to have a significant impact on the viability of a wide variety of quantum applications. In this work, we present novel algorithms for a number of in-place quantum arithmetic operations that are highly efficient in terms of their space and gate count overheads compared to the current state-of-the-art.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We present our multiplication algorithms as consequences of a single unified theorem, which may find further application within quantum arithmetic.

### 3. Multimodal Error Detection in Chest X-ray Reports: A Large Language Model Reading Image Evidence

- 作者：Yanda Cheng, Bo Wen, Yuhao Lu｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**4.87**
- 链接：https://arxiv.org/abs/2611.26492v1

> 命中：hit_scenario=['ads']

### 背景/问题
Rad-Linter checks chest X-ray reports against image-derived evidence to flag potential errors for review. A pretrained image classifier supplies scores for nine pathologies, and a 1.5B-parameter language model, fine-tuned with LoRA on 1,816 examples, checks their consistency with the report.

### 方法
A pretrained image classifier supplies scores for nine pathologies, and a 1.5B-parameter language model, fine-tuned with LoRA on 1,816 examples, checks their consistency with the report. The same language model without fine-tuning remains near 50% accuracy. These controlled results show that, given the same image-derived scores, a trained language model detects report-score inconsistencies more accurately than the tested rule baseline, with the advantage concentrated in interpreting how findings are worded.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These controlled results show that, given the same image-derived scores, a trained language model detects report-score inconsistencies more accurately than the tested rule baseline, with the advantage concentrated in interpreting how findings are worded.

### 4. Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)

- 作者：Mengxiao Wang, Mahbub Alam, Kalyan Nakka, Nitesh Saxena｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**4.37**
- 链接：https://arxiv.org/abs/2611.26553v1

> 命中：hit_abstract=['CATE']

### 背景/问题
Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause.

### 方法
Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. Incident catalogs collect these reports, and benchmarks record whether agents fail, but neither replicates an incident nor tests the cause its report might identify. In this paper, we present ROGUE-AI (Replication of Agentic Security Events: Audit and Investigation), a multi-agent framework that closes the above gap and rebuilds each reported incident offline together with a matched control that lacks only the blamed cause, and runs agents on both.

### 实验/数据
News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. In this paper, we present ROGUE-AI (Replication of Agentic Security Events: Audit and Investigation), a multi-agent framework that closes the above gap and rebuilds each reported incident offline together with a matched control that lacks only the blamed cause, and runs agents on both. Of the 72 incidents with real-world harm, 62 had no underlying attacker, and in these, agents did what their task asked for but missed an ordinary hazard, such as a database shared with the live site.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Built from real incidents, the ROGUE-AI replications form a reusable audit framework that vendors can rerun before each new release.

### 5. Quasipolynomial pyjamas

- 作者：Sida Li｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26622v1

### 背景/问题
The ``pyjama stripe" $E(\varepsilon)$ is the set of all complex numbers whose real part lies within $\varepsilon$ of the nearest integer. The Pyjama Problem asks whether, for each $\varepsilon > 0$, there exists some union of finitely many rotations of $E(\varepsilon)$ about the origin that covers the plane.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also show that at least $(π/2 + 0.003 + o(1))\varepsilon^{-1}$ rotations are necessary, improving upon the natural lower bound of $(π/2 + o(1))\varepsilon^{-1}$.

### 6. Little Red Dots from Primordial Vacuum Bubbles

- 作者：Miguel Barroso Varela, Katherine Freese, Matthew Kleban, Cameron Norton, Evangelos I. Sfakianakis｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26620v1

### 背景/问题
Quantum tunneling transverse to the inflaton trajectory can produce $10^6$--$10^8M_\odot$ primordial black holes at the abundance of JWST's little red dots, without the enhanced curvature perturbations excluded by limits on CMB spectral distortions. Rare vacuum bubbles nucleate during a brief interval of inflation and later form black holes, with adjustable mass and abundance and a narrow mass spectrum of percent-level width.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
The leading constraint, from accretion, is satisfied for a population matching the bright little red dots even if all the emitted radiation escapes as hard X-rays.

### 7. BRUCE (Bayesian Rio Urban Climate Estimator): spatiotemporal interpolation of air temperature from heterogeneous sensor networks for operational heat monitoring

- 作者：Ayrton Sena Gouveia, Rafael Santos de Oliveira, Lucas Menezes-Silva, Maira Alejandra Moreno Castillo, Felipe de Carvalho Vommaro Marincola, João Henrique de Araújo Morais, Valéria Saraceni, Gislani Mateus Oliveira Aguilar 等｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26612v1

### 背景/问题
Accurate characterization of intra-urban temperature variability is essential for heat-health surveillance, yet official monitoring networks are too sparse to resolve fine-scale gradients, particularly in Global South cities. We present BRUCE, a Bayesian hierarchical spatiotemporal model, fitted with the Integrated Nested Laplace Approximation (INLA) and a Stochastic Partial Differential Equation (SPDE) spatial component, that fuses four heterogeneous temperature sources for Rio de Janeiro, Brazil: official weather stations, low-cost IoT sensors, citizen-science personal weather stations and ERA5-Land reanalysis.

### 方法
We present BRUCE, a Bayesian hierarchical spatiotemporal model, fitted with the Integrated Nested Laplace Approximation (INLA) and a Stochastic Partial Differential Equation (SPDE) spatial component, that fuses four heterogeneous temperature sources for Rio de Janeiro, Brazil: official weather stations, low-cost IoT sensors, citizen-science personal weather stations and ERA5-Land reanalysis. The model accounts for class- and station-specific measurement bias and estimates a continuous spatial field that evolves day to day through an autoregressive (AR1) structure. Applied to 241 primary care territories, BRUCE's posterior exceedance probabilities allowed 96 to be classified with high confidence (model-based classifications), whereas a constant-width interval derived from LCZ4r cross-validation errors supported confident classification of none.

### 实验/数据
The model accounts for class- and station-specific measurement bias and estimates a continuous spatial field that evolves day to day through an autoregressive (AR1) structure. The framework offers a statistically principled, operationally viable basis for intra-urban heat monitoring in data-heterogeneous settings.

### 结果
Fitted independently to nine monthly windows (January, June, November; 2023--2025), the elevation coefficient was significant in all windows and of consistent magnitude in eight ($-$1.08 to $-$1.38 \textdegree{}C per SD).

### 结论/启示（面向电商发券、定价、营销算法等应用）
The framework offers a statistically principled, operationally viable basis for intra-urban heat monitoring in data-heterogeneous settings.

### 8. Bridging the Discovery Gap in Solid Dataspaces with a Semantic Data Catalog

- 作者：Florian Hölken, Alexander Paulus, Tobias Meisen, André Pomp｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26611v1

### 背景/问题
Dataspaces are an emerging concept to enable secure and controlled data sharing between multiple stakeholders. However, most existing dataspace architectures, such as those based on the concepts of IDSA (International Data Spaces Association) and Gaia-X, are heavily concept-driven and require significant effort to implement, making it difficult to quickly build a functional dataspace.

### 方法
Solid (Social Linked Data) offers a compelling alternative by providing a lighter and more practical approach. To address this gap, we present a FAIR-compliant data catalog for Solid. Our catalog follows the FAIR principles (Findability, Accessibility, Interoperability, and Reusability) by integrating semantic models that describe all available data sources within the Solid ecosystem.

### 实验/数据
Dataspaces are an emerging concept to enable secure and controlled data sharing between multiple stakeholders. However, most existing dataspace architectures, such as those based on the concepts of IDSA (International Data Spaces Association) and Gaia-X, are heavily concept-driven and require significant effort to implement, making it difficult to quickly build a functional dataspace. Solid (Social Linked Data) offers a compelling alternative by providing a lighter and more practical approach.

### 结果
However, most existing dataspace architectures, such as those based on the concepts of IDSA (International Data Spaces Association) and Gaia-X, are heavily concept-driven and require significant effort to implement, making it difficult to quickly build a functional dataspace. As a result, managing and locating relevant data across multiple Solid servers and pods becomes a significant barrier to usability. This approach enables enhanced data discovery, improves accessibility through standardized metadata, enhances interoperability between different data sources, and promotes data reuse across applications.

### 结论/启示（面向电商发券、定价、营销算法等应用）
By bridging this critical gap, our catalog improves the usability of Solid-based dataspaces, making them a viable option for decentralized and open data ecosystems, such as smart city applications.

### 9. Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth

- 作者：Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong, Amaël Delaunoy, Stephan R. Richter, Vladlen Koltun｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26603v1

### 背景/问题
We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-frame methods favor sharpness.

### 方法
We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. We release a family of models that define a new Pareto frontier in terms of metric accuracy, sharpness, temporal consistency, and runtime.

### 实验/数据
未在摘要中明确给出。

### 结果
Depth Pro 2 produces depth maps that are metrically accurate, sharp, and temporally consistent all at once, outperforming prior work in all of these dimensions.

### 结论/启示（面向电商发券、定价、营销算法等应用）
We release code and weights at https://apple-aiml-research.github.io/ml-depth-pro-2/

### 10. Local orbital magnetization and Chern markers from equilibrium local currents

- 作者：Henrique P. Veiga, Aires Ferreira, Caio H. Lewenkopf, João M. Viana Parente Lopes｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26599v1

### 背景/问题
Local currents carry the orbital magnetization of a macroscopic sample and are key for modeling inhomogeneous magnetic materials and for understanding magnetoelectric and topological responses. However, producing realistic simulated images of local currents in inhomogeneous systems remains challenging.

### 方法
Local currents carry the orbital magnetization of a macroscopic sample and are key for modeling inhomogeneous magnetic materials and for understanding magnetoelectric and topological responses. Building upon recent work on stochastic estimation methods for tight-binding models, we show that all matrix elements of positive semidefinite operators defined on a lattice can be obtained at once from a single set of filtered random vectors.

### 实验/数据
This eliminates the need for independent simulations previously required for off-diagonal elements, which significantly speeds up the calculation of spatial maps of local currents.

### 结果
This eliminates the need for independent simulations previously required for off-diagonal elements, which significantly speeds up the calculation of spatial maps of local currents.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Hence, it is free of boundary-compensation artifacts, and its sample average converges to the bulk Chern number in a controlled fashion.

### 11. End-to-End Quantum Algorithm for Differential Equations: Application to Simulating a Biomolecular System

- 作者：Mohsen Bagherimehrab, Daniyaal Farooqi, Gavin K. Brennen, Barry C. Sanders, Alán Aspuru-Guzik｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26582v1

### 背景/问题
Quantum algorithms for differential equations have the potential for substantial algorithmic speedups over classical methods. However, they rely on certain assumptions and abstract oracle specifications that leave their practical feasibility and computational advantages for realistic applications unclear.

### 方法
We present a tailored end-to-end quantum algorithm for the linearized Poisson-Boltzmann (LPB) equation, a partial differential equation (PDE) with variable coefficients widely used in simulating a biomolecular system. In particular, we develop a new discrete representation for variable-coefficient PDEs on a grid that enables efficient implementation of the operator oracle, and build on a recent technique based on optimal wavelet preconditioning to generate a quantum solution with a cost independent of the condition number of the discretized operator.

### 实验/数据
未在摘要中明确给出。

### 结果
Our work provides a concrete end-to-end quantum algorithm for a PDE of practical value, demonstrates an exponential improvement in scaling with $N_g$ over classical methods, and provides a foundation for assessing its potential quantum advantage in practice.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Our work provides a concrete end-to-end quantum algorithm for a PDE of practical value, demonstrates an exponential improvement in scaling with $N_g$ over classical methods, and provides a foundation for assessing its potential quantum advantage in practice.

### 12. Amplitude dependent wave envelope type estimates for moment curves and applications

- 作者：Sangwon Jeong, Changkeun Oh｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26581v1

### 背景/问题
We prove amplitude dependent wave envelope type estimates for moment curves in arbitrary dimensions. The proof uses the sharp square function estimates of Maldague and Guth-Maldague.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
This proves the conjecture of Demeter-Guth-Wang on exponential sums in all dimensions.

### 13. Neighbourhood Walkability and Cardiometabolic Morbidity in Greater London: A Fine-Grained Spatial Analysis

- 作者：Benjamin T. Pike, Stephen Law, Sanja Šćepanović, Linus W. Dietz｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26573v1

### 背景/问题
Cardiometabolic diseases are leading causes of ill health, and neighbourhoods that support everyday walking may help reduce them. Studies often report lower disease prevalence in more walkable neighbourhoods.

### 方法
Walkability followed a centre--periphery gradient, with a radial model explaining 74.2\% of its variation. After spatial-error adjustment, no clear association remained for obesity; coefficients for the other seven were reduced by 83--99\% relative to comparable log-scale models.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
These findings caution against interpreting city-wide walkability coefficients as neighbourhood effects independent of wider metropolitan structure, and highlight the need for studies of neighbourhood form and health to disentangle global and local spatial structure explicitly.

### 14. Optimal Control in Pairs Trading with Negative-Power Utility

- 作者：Aleksei Kozhevnikov｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26568v1

### 背景/问题
We solve a finite-horizon consumption and investment problem in a pairs trading model with an Ornstein-Uhlenbeck spread and utility $U(x)=-x^{-γ}$, $γ>0$. Linearizing the Hamilton-Jacobi-Bellman equation gives explicit formulas for the value function and the optimal feedback control.

### 方法
We solve a finite-horizon consumption and investment problem in a pairs trading model with an Ornstein-Uhlenbeck spread and utility $U(x)=-x^{-γ}$, $γ>0$.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also show that the suprema of the negative powers of optimal wealth and consumption are integrable on every finite horizon exactly for orders $0<m\le 1+γ$.

### 15. PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity

- 作者：Hao Vo, Taisei Hanyu, Yuki Ikebe, Pham Tri Quang, Sreevenkata Anjani Tishita Godavarthi, Nghi D. Q. Bui, Daniel Sonntag, Chase Rainwater 等｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26565v1

### 背景/问题
Vision-Language-Action (VLA) models have advanced rapidly in language-conditioned robotic manipulation, yet existing benchmarks mainly evaluate gripper--object contact and largely ignore how objects interact with the environment through gravity, friction, inertia, and mass distribution. As a result, it remains unclear whether current policies truly understand physics or merely interpolate from their training data.

### 方法
Vision-Language-Action (VLA) models have advanced rapidly in language-conditioned robotic manipulation, yet existing benchmarks mainly evaluate gripper--object contact and largely ignore how objects interact with the environment through gravity, friction, inertia, and mass distribution. Our analysis reveals two key bottlenecks: limited robustness of pretrained models, which causes most failures before the throw, and physical blindness, as providing ground-truth physical properties roughly doubles success.

### 实验/数据
As a result, it remains unclear whether current policies truly understand physics or merely interpolate from their training data. All data are generated by a scalable, fully automatic pipeline that combines grasp generation, motion planning, and closed-loop throw optimization under randomized physical properties. Experiments on a humanoid robot and in the real world show the same failure patterns.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We hope PhyDEX will drive the development of physically grounded robot policies.

### 16. MM-SystemOneBias: Evaluating Bias in Multimodal Jev-Style System One Decision Models

- 作者：Jinzhe Li, Qi Wang, Dandan Guo, Li Liu, Yuan Wu, Yi Chang｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26557v1

### 背景/问题
When multimodal decision models determine actions, moderation outcomes, or quality judgments, their reliability depends on preserving semantic decisions across presentation changes, ignoring irrelevant additions, and distinguishing information consistent with task evidence from information that conflicts with it. Existing evaluations study decision-interface biases and multimodal model behavior in separate settings, leaving no common protocol to compare multimodal decision models with their backbones on practical tasks.

### 方法
When multimodal decision models determine actions, moderation outcomes, or quality judgments, their reliability depends on preserving semantic decisions across presentation changes, ignoring irrelevant additions, and distinguishing information consistent with task evidence from information that conflicts with it. Existing evaluations study decision-interface biases and multimodal model behavior in separate settings, leaving no common protocol to compare multimodal decision models with their backbones on practical tasks. We introduce \textbf{MM-SystemOneBias}, which evaluates 13 models on 5,323 original instances from nine public datasets and 11 task scenarios using six paired interventions: option order, option label, external judgment, image--text description, irrelevant information, and rating scale.

### 实验/数据
We introduce \textbf{MM-SystemOneBias}, which evaluates 13 models on 5,323 original instances from nine public datasets and 11 task scenarios using six paired interventions: option order, option label, external judgment, image--text description, irrelevant information, and rating scale.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Among pairs with unchanged semantic decisions, mean absolute changes in answer probabilities range from 4.56 to 11.55 percentage points, revealing input effects that accuracy alone misses.

### 17. Multiplicative Sidon basis

- 作者：Sándor Z. Kiss, Csaba Sándor｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26555v1

### 背景/问题
For a $h \ge 2$ integer a sequence of positive integers $A$ is called asymptotic basis of order $h$ if every sufficiently large positive integer $n$ can be written as a sum of $h$ elements of $A$. We say a sequence of positive integers $A$ is a multiplicative Sidon sequence if all the products of two elements of the sequence $A$ are distinct.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
In this paper we prove the existence of a multiplicative Sidon set which is an asymptotic basis of order 2 by using the probabilistic method.

### 18. Chemical Cartography Across Time: The Age-Dependent Chemical Structure of the Milky Way with a Homogeneous Sample of 580,000 Giants from Five Surveys

- 作者：Jeff Shen, Neige Frankel, David W. Hogg, Joshua S. Speagle, Shirley Ho｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26550v1

### 背景/问题
Mapping the distribution of elements in the Milky Way and understanding how that distribution has changed over time can give us insight into the formation and evolution of our Galaxy. Here we use homogeneously estimated atmospheric parameters, elemental abundances, distances, and ages for ~580,000 giants from five major spectroscopic surveys---all simultaneously placed on a single, self-consistent scale by one model---allowing us, for the first time, to use a large sample of stars with uniform labels and ages that cumulatively span much of the disk to trace how the metallicity structure of the Milky Way depends on stellar age.

### 方法
Here we use homogeneously estimated atmospheric parameters, elemental abundances, distances, and ages for ~580,000 giants from five major spectroscopic surveys---all simultaneously placed on a single, self-consistent scale by one model---allowing us, for the first time, to use a large sample of stars with uniform labels and ages that cumulatively span much of the disk to trace how the metallicity structure of the Milky Way depends on stellar age.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Together, these trends are consistent with an inside-out formation scenario in which the gradient of the star-forming gas has flattened over at least the last ~6 Gyr, while the near-zero gradient of the oldest stars reflects their formation in a well-mixed disk, efficient radial migration, or both.

### 19. The Geometry of Lies: Knowledge and Persona Directions for Detecting Deception in Large Language Models

- 作者：Md. Abdullah Al Zami, Suraiya Shanaz, Mahdi Hasan, Shoaib Ahmed Dipu, Farig Yousuf Sadeque, Md. Sabbir Ahmed｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26545v1

### 背景/问题
Linear probes are the cheapest LLM lie detectors but often fail to transfer across kinds of lie. Label-free directions from honest and deceptive role-play are untested at 70B scale and on lies about knowledge, where a lie and an honest denial can be identical.

### 方法
At each model's middle layer the resulting persona direction ranks lies across Liars' Bench better than single-dataset probes on three of its four models; it fails on Qwen, even when Qwen stays in role far more often. A knowledge direction contrasts questions the model can answer with ones nobody can, each followed by the same scripted denial. It separates lies from identical honest denials on two models and narrowly on a third, but not on the fourth; its other results partly depend on the benchmark's wording.

### 实验/数据
At each model's middle layer the resulting persona direction ranks lies across Liars' Bench better than single-dataset probes on three of its four models; it fails on Qwen, even when Qwen stays in role far more often.

### 结果
At each model's middle layer the resulting persona direction ranks lies across Liars' Bench better than single-dataset probes on three of its four models; it fails on Qwen, even when Qwen stays in role far more often. The sum of the two directions ranks lies better than a supervised probe at the same depth on all four models (on one, both near chance) but is level with the persona direction on Llama's average and behind that probe on held-out lies.

### 结论/启示（面向电商发券、定价、营销算法等应用）
More varied role-play questions do not help the persona direction on Liars' Bench.

### 20. Self-gravity depletes superradiant clouds

- 作者：Mateja Bošković, Lucas Gathercole, Thomas F. M. Spieksma, Samuel J. Witte｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26541v1

### 背景/问题
Superradiant clouds of ultralight scalars around black holes are often modeled as free fields, whose levels grow independently and decay slowly through gravitational-wave emission. We show that this limit is never realized.

### 方法
Superradiant clouds of ultralight scalars around black holes are often modeled as free fields, whose levels grow independently and decay slowly through gravitational-wave emission.

### 实验/数据
Superradiant clouds of ultralight scalars around black holes are often modeled as free fields, whose levels grow independently and decay slowly through gravitational-wave emission.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Any assessment of superradiant signals must therefore account for both self-gravity and the cloud's environment.

### 21. Large $k$-cross-free families

- 作者：Jack H. Koolen, Anyuan Tian｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26539v1

### 背景/问题
Two subsets $A,B$ of a finite set $X$ are crossing if $A\cap B$, $A\setminus B$, $B\setminus A$, and $X\setminus(A\cup B)$ are all nonempty. A family is $k$-cross-free if it contains no $k$ pairwise crossing members.

### 方法
未在摘要中明确给出。

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We also prove an $O(kn\log k)$ upper bound for $k$-cross-free families closed under all cyclic shifts of a fixed cyclic ordering of the ground set.

### 22. LLM GerryMandering: Separating Interactions from Additive Effects in LLM Audits

- 作者：George Rahul, Ronit Jahilal, Bhaskara Hanuma Vedula, Ponnurangam Kumaraguru, Pushkar Shukla｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26538v1

### 背景/问题
Intersectional bias arises when a model treats people who hold several marginalised identities at once differently from what their separate identities would predict. Auditing such intersectional subgroups remains a challenge: their number grows quadratically, and there is no agreed baseline for what independent attributes would predict.

### 方法
Intersectional bias arises when a model treats people who hold several marginalised identities at once differently from what their separate identities would predict. We introduce ADDIS (Additive Intersectional Screen), which fits an additive model over all attributes, scores each subgroup by its Additive Residual Distance (ARD) from that model's prediction, and tests it against a Freedman-Lane null. We then build IndiPersona, 10,000 synthetic Indian personas with six identity attributes, and audit 13 open language models.

### 实验/数据
We test this standard criterion on 150 synthetic datasets built with no interaction. With the shuffle null, it flags 66.1 false subgroups per dataset on average, and at least one in every dataset. When we plant interactions of known size into these datasets, a repaired null lets the criterion recover only 32% of them.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Much of what audits report as intersectional bias can thus arise from independent single-attribute effects alone, yet a small core of interactions survives.

### 23. Anytime-valid inference for time series via self-normalization

- 作者：Tim Kutta, Xiaofeng Shao｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26536v1

### 背景/问题
We develop a self-normalized approach to constructing asymptotic confidence sequences for a broad class of parameters of stationary time series under weak dependence. Our theory covers nonlinear marginal parameters, including quantiles, expectiles and expected shortfall, as well as autoregressive coefficients.

### 方法
We develop a self-normalized approach to constructing asymptotic confidence sequences for a broad class of parameters of stationary time series under weak dependence. We propose two sequential self-normalizers with complementary statistical and computational advantages.

### 实验/数据
Our theory covers nonlinear marginal parameters, including quantiles, expectiles and expected shortfall, as well as autoregressive coefficients. A key advantage is that the construction avoids direct estimation of the long-run variance, which can be particularly challenging for nonlinear parameters under serial dependence. We investigate their finite-sample performance through simulations and illustrate their use in Markov chain Monte Carlo output analysis in the supplementary appendix.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
We investigate their finite-sample performance through simulations and illustrate their use in Markov chain Monte Carlo output analysis in the supplementary appendix.

### 24. On the design of sequential quantum repeaters with error detection

- 作者：Javier Rey-Domínguez, Koji Azuma, Mohsen Razavi｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26537v1

### 背景/问题
Long-distance, trust-free quantum communications rely on the development of scalable quantum repeater schemes. Sequential entanglement generation with error detection is a promising approach that combines manageable implementation requirements with a hop-by-hop architecture compatible with existing classical infrastructure.

### 方法
Sequential entanglement generation with error detection is a promising approach that combines manageable implementation requirements with a hop-by-hop architecture compatible with existing classical infrastructure.

### 实验/数据
未在摘要中明确给出。

### 结果
We find that simple quantum error-detecting codes, such as repetition codes or quantum parity codes, perform well under near-term hardware assumptions and outperform strategies without any encoding. Additionally, we show that moderate improvements in some hardware components can partially mitigate the slow technological progress of others.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Additionally, we show that moderate improvements in some hardware components can partially mitigate the slow technological progress of others.

### 25. Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models

- 作者：Chang Yang, Yao Xuan, Wendan Yan, Nhat Le, Jiang Liu, Longhao Jin, Zhen Peggy Yao, Alireza Vahdatpour 等｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26531v1

### 背景/问题
Large Web platforms operate large fleets of ranking models, each selecting features from a shared pool of tens of thousands. We present an end-to-end agentic system that optimizes features across the fleet under resource constraints shared across models and those set per model, such as feature pipeline cost and serving throughput (QPS), respectively.

### 方法
Large Web platforms operate large fleets of ranking models, each selecting features from a shared pool of tens of thousands. We present an end-to-end agentic system that optimizes features across the fleet under resource constraints shared across models and those set per model, such as feature pipeline cost and serving throughput (QPS), respectively. In this system, LLM agents propose hypotheses, and deterministic tools execute experiments and verify them.

### 实验/数据
In this system, LLM agents propose hypotheses, and deterministic tools execute experiments and verify them. The optimized models were launched, and in online A/B tests they improved a primary online metric by 0.20%.

### 结果
Across production models, the system improves normalized entropy by 0.31% on average within each model's budget, and the trimming step cuts pipeline cost by 2.3% with no regression beyond measurement noise. The optimized models were launched, and in online A/B tests they improved a primary online metric by 0.20%.

### 结论/启示（面向电商发券、定价、营销算法等应用）
The optimized models were launched, and in online A/B tests they improved a primary online metric by 0.20%.

### 26. Thermal-Guided Ensemble Reinforcement Learning for Regime-Adaptive Short-Term GPU Power Forecasting in AI Data Centers

- 作者：Yuanshuo Zhang, Ying Zhang, Ziying Wang, Fanping Sui｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26527v1

### 背景/问题
AI data centers (AIDCs) introduce bursty and regime-dependent load patterns, posing significant challenges for reliable energy management and predictive grid control. To address these challenges, this letter proposes a thermal-guided ensemble reinforcement learning framework for probabilistic AIDC load forecasting.

### 方法
To address these challenges, this letter proposes a thermal-guided ensemble reinforcement learning framework for probabilistic AIDC load forecasting. Case studies on 1-second MIT Supercloud telemetry show that the proposed method reduces the normalized mean absolute error to about 1% across all computing regimes, compared with 4-11% for deep learning-based and ensemble learning benchmarks, and converges faster with narrower prediction intervals than a DRL ensemble without thermal guidance.

### 实验/数据
AI data centers (AIDCs) introduce bursty and regime-dependent load patterns, posing significant challenges for reliable energy management and predictive grid control.

### 结果
AI data centers (AIDCs) introduce bursty and regime-dependent load patterns, posing significant challenges for reliable energy management and predictive grid control.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Case studies on 1-second MIT Supercloud telemetry show that the proposed method reduces the normalized mean absolute error to about 1% across all computing regimes, compared with 4-11% for deep learning-based and ensemble learning benchmarks, and converges faster with narrower prediction intervals than a DRL ensemble without thermal guidance.

### 27. Backtracking Agent Applications Security Incidents

- 作者：Yicheng Cai, Taegyu Kim, Peng Liu｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26525v1

### 背景/问题
Agent applications are increasingly deployed, yet agent-specific attacks pose real threats to them. Upon a security incident, organizations backtrack to identify the CEP (compromise entry point), remediate the damage, and prevent its recurrence.

### 方法
Upon a security incident, organizations backtrack to identify the CEP (compromise entry point), remediate the damage, and prevent its recurrence. In this work, we present Origin, a backtracking tool for the analyst to submit a small number of queries to identify CEPs that existing tools cannot provide. Our approach poses two challenges: (1) define the intermediate abstraction that captures the mapping relationships between the two semantic layers; (2) determine the region-to-variable mapping for constructing the cross-layer graph defined in the intermediate abstraction.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Case studies on five popular agent applications across eight attack incidents show that an analyst using Origin correctly identifies all the CEPs.

### 28. Hamiltonian Stabilization of the Two-Photon Dicke Model

- 作者：Pradip Laha, Kingshuk Adhikary, Subhashish Banerjee, Peter van Loock｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26523v1

### 背景/问题
Collective two-photon light--matter interactions enable pair amplification but can destroy spectral confinement, preventing a stable thermodynamic bright phase. We show that a positive Kac-scaled number-Kerr interaction renders the two-photon Dicke Hamiltonian of \(N\) emitters lower-bounded at all couplings while preserving its generalized \(\mathbb Z_4\) symmetry.

### 方法
Spectral collapse thus becomes the singular zero-Kerr point of a first-order phase diagram, identifying a Hamiltonian route to stabilizing pair amplification.

### 实验/数据
未在摘要中明确给出。

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
Spectral collapse thus becomes the singular zero-Kerr point of a first-order phase diagram, identifying a Hamiltonian route to stabilizing pair amplification.

### 29. The Window Lever: Longer Observation Windows Outweigh the Observed Effects of Data, Capacity, and Architecture in Customer Behavior Forecasting

- 作者：Tara Sowrirajan, Yanqiao Wang｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26521v1

### 背景/问题
In our experiments on long-horizon customer-behavior forecasting, a longer observation window outweighed the observed effects of more data, more capacity and newer architectures. The window is the weeks of history a model sees before the week it forecasts from.

### 方法
The window is the weeks of history a model sees before the week it forecasts from. We therefore report a robust positive association with longer windows and do not identify the magnitude of a calendar-independent history effect. An activity-mixture model predicted +0.014 from 24 to 32 weeks; the weekly-aggregate probe returned -0.0004.

### 实验/数据
In our experiments on long-horizon customer-behavior forecasting, a longer observation window outweighed the observed effects of more data, more capacity and newer architectures. The direction holds on five public datasets, four spanning over a year (ridge and our transformer on all five). On our internal data, longer windows admit up to 10% more and colder training customers, which matching does not fix.

### 结果
未在摘要中明确给出。

### 结论/启示（面向电商发券、定价、营销算法等应用）
A team building on this class of data should start by lengthening the window.

### 30. Hypergraph Hajnal-Szemerédi

- 作者：Michelle Delcourt, Cicely Henderson, Thomas Lesgourgues, Luke Postle｜年份：2026｜发布时间：2026-11-19｜来源：arxiv｜相关度分：**2.37**
- 链接：https://arxiv.org/abs/2611.26513v1

### 背景/问题
A seminal result of Hajnal and Szemerédi from 1970 asserts that every graph on $n$ vertices with $q\;|\;n$ and minimum degree at least $\Big(1-\frac{1}{q}\Big)n$ admits a $K_q$-factor (a collection of vertex-disjoint copies of $K_q$ spanning all vertices). There has been sustained interest in extending this result to hypergraph $K_q^r$-factors.

### 方法
Inspired by the first and fourth author's recent proof of the Nash-Williams' Conjecture, we accomplish this by combining a linear programming framework with ideas from discharging.

### 实验/数据
未在摘要中明确给出。

### 结果
For general $q$ and $r$, Lu and Székely in 2007 showed that every large enough, $r$-graph $G$ with $q\mid v(G)$ and $δ_{r-1}(G) \ge \left(1- \frac{c}{q^{r-1}}\right)v(G)$ admits a $K_q^r$-factor (where $c$ is a constant depending on $r$ but not $q$), and there have been various subsequent improvements to the constant (but not the order) of this bound over the ensuing decades.

### 结论/启示（面向电商发券、定价、营销算法等应用）
Additionally, we establish a technical result about finding large independent sets in sparse, non-uniform hypergraphs, which may be of independent interest.
