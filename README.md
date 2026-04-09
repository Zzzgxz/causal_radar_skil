## CausalRadar（每日增量追踪：营销/电商场景的因果推断热点）

这个仓库模板会**每天增量**检索并整理与「因果推断模型 / 营销算法 / 电商发券与定价」相关的新论文/文章，并输出一份当日 Markdown 报告：

- 数据源（首批）：**arXiv + Semantic Scholar +（可选）Google Scholar**
- 输出：`reports/YYYY-MM-DD.md`（当日报告）与 `reports/latest.md`（最新）
- 增量去重：`data/seen.json` 记录已收录条目（按 `source:id/url` 去重）

> 说明：Google Scholar 没有稳定官方 API，GitHub Actions 环境下**强烈建议**用 SerpAPI（可选）来接入 Scholar；否则默认仍可稳定跑 arXiv + Semantic Scholar。

---

### 1) 快速开始

1. 把本目录作为一个 GitHub 仓库（建议私有）提交。
2. （可选）在仓库 `Settings → Secrets and variables → Actions` 添加密钥：
   - `SERPAPI_KEY`：用于稳定抓取 Google Scholar（推荐）。
   - `OPENAI_API_KEY`：用于生成更像“论文大纲”的结构化文献小结（推荐）。
   - （可选）`OPENAI_BASE_URL`：OpenAI 兼容接口地址（例如自建网关）。
   - （可选）`OPENAI_MODEL`：模型名，默认 `gpt-4o-mini`。
3. 打开 Actions，允许 Workflow 运行，并确保 Workflow 权限为 **Read and write permissions**（用于把报告提交回仓库）。

当日第一次跑完后，在 `reports/` 下就会看到日报与 `latest.md`。

---

### 2) 配置关键词与偏好

编辑 `config.yml`：

- `core_topics`：核心主题（因果推断/营销/电商场景）
- `application_scenarios`：场景（发券、定价、促销、推荐、广告等）
- `methods`：关注的方法词（uplift、CATE、DiD、IV、policy learning…）
- `sources`：启用哪些数据源、每次抓取数量与时间窗口
- `scoring`：排序打分权重（标题/摘要匹配、场景词、方法词、时效性等）

---

### 3) 输出内容结构（文献小结）

每条条目会输出一个“文献小结”，结构尽量对齐论文常见大纲：

1. **背景/问题**
2. **方法**
3. **实验/数据**
4. **结果**
5. **结论/启示**

若配置了 `OPENAI_API_KEY`：会基于标题+摘要生成更完整的结构化小结；否则使用基于摘要的启发式提炼（信息可能更粗略）。

---

### 4) GitHub Actions 定时

定时任务配置在：`.github/workflows/daily.yml`

- 默认每天 UTC 01:00 跑一次
- 你可以改 cron；或在 Actions 页面手动触发

---

### 5) 常见问题

**Q: 为什么我今天没看到 Scholar 的结果？**  
A: 没有设置 `SERPAPI_KEY` 时会跳过 Scholar（防止不稳定/验证码导致 workflow 失败）。

**Q: 如何避免每天重复？**  
A: `data/seen.json` 会持久保存已收录条目；每次运行只会输出“新发现”的条目，并按相关度排序。

