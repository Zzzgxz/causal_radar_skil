#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CausalRadar: 每日增量检索 + 相关度排序 + 结构化文献小结（Markdown 输出）

运行方式：
  python run.py

环境变量（可选）：
  SERPAPI_KEY        - 接入 Google Scholar（SerpAPI）
  OPENAI_API_KEY     - 启用 LLM 生成更像论文大纲的结构化小结
  OPENAI_BASE_URL    - OpenAI 兼容接口基址（默认 https://api.openai.com/v1）
  OPENAI_MODEL       - 覆盖 config.yml 的模型名
"""

from __future__ import annotations

import dataclasses
import datetime as dt
import json
import math
import os
import re
import sys
from typing import Any, Dict, Iterable, List, Optional, Tuple

import feedparser
import requests
import yaml
from dateutil import parser as date_parser


ROOT = os.path.dirname(os.path.abspath(__file__))


def _read_yaml(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _read_json(path: str, default: Any) -> Any:
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: str, obj: Any) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def _write_text(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def _today_utc() -> dt.date:
    return dt.datetime.now(dt.timezone.utc).date()


def _parse_date(s: Optional[str]) -> Optional[dt.datetime]:
    if not s:
        return None
    try:
        d = date_parser.parse(s)
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d.astimezone(dt.timezone.utc)
    except Exception:
        return None


def _days_ago(d: Optional[dt.datetime]) -> Optional[int]:
    if d is None:
        return None
    now = dt.datetime.now(dt.timezone.utc)
    return max(0, int((now - d).total_seconds() // 86400))


def _norm_text(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip()


@dataclasses.dataclass
class Item:
    source: str
    uid: str  # source 内唯一 id（例如 arXiv id、S2 paperId、URL hash）
    title: str
    authors: List[str]
    year: Optional[int]
    abstract: str
    url: str
    published_at: Optional[dt.datetime]
    extra: Dict[str, Any] = dataclasses.field(default_factory=dict)

    @property
    def dedup_key(self) -> str:
        return f"{self.source}:{self.uid}"


# ---------------------------
# 抓取：arXiv
# ---------------------------


def fetch_arxiv(cfg: Dict[str, Any], queries: List[str]) -> List[Item]:
    scfg = cfg["sources"]["arxiv"]
    if not scfg.get("enabled", True):
        return []

    max_results = int(scfg.get("max_results", 40))
    lookback_days = int(scfg.get("lookback_days", 14))

    # arXiv API：按 submittedDate 倒序取；再按 lookback_days 过滤
    results: List[Item] = []
    for q in queries:
        # arXiv query 语法参考：http://export.arxiv.org/api/help/api/user-manual
        # 这里用 all: 进行全文字段匹配；用 OR 组合少量关键词
        url = (
            "http://export.arxiv.org/api/query?"
            f"search_query={q}"
            f"&start=0&max_results={max_results}"
            "&sortBy=submittedDate&sortOrder=descending"
        )
        feed = feedparser.parse(url)
        for e in feed.entries:
            published = _parse_date(getattr(e, "published", None))
            da = _days_ago(published)
            if da is not None and da > lookback_days:
                continue

            arxiv_id = ""
            if hasattr(e, "id"):
                arxiv_id = str(e.id).rsplit("/", 1)[-1]

            title = _norm_text(getattr(e, "title", ""))
            abstract = _norm_text(getattr(e, "summary", ""))
            authors = [a.name for a in getattr(e, "authors", []) if getattr(a, "name", None)]

            link = ""
            if hasattr(e, "link"):
                link = str(e.link)
            year = published.year if published else None

            results.append(
                Item(
                    source="arxiv",
                    uid=arxiv_id or link or title,
                    title=title,
                    authors=authors,
                    year=year,
                    abstract=abstract,
                    url=link,
                    published_at=published,
                    extra={"raw_query": q},
                )
            )

    # 去重（同一 arXiv id 多 query 命中）
    uniq: Dict[str, Item] = {}
    for it in results:
        if it.dedup_key not in uniq:
            uniq[it.dedup_key] = it
    return list(uniq.values())


# ---------------------------
# 抓取：Semantic Scholar
# ---------------------------


def fetch_semantic_scholar(cfg: Dict[str, Any], query: str) -> List[Item]:
    scfg = cfg["sources"]["semantic_scholar"]
    if not scfg.get("enabled", True):
        return []

    max_results = int(scfg.get("max_results", 40))
    lookback_days = int(scfg.get("lookback_days", 21))

    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": max_results,
        "fields": "title,authors,year,abstract,url,publicationDate,externalIds",
    }
    headers = {"User-Agent": "CausalRadar/1.0 (daily-research-tracker)"}
    r = requests.get(url, params=params, headers=headers, timeout=60)
    r.raise_for_status()
    data = r.json()

    items: List[Item] = []
    for p in data.get("data", []):
        published = _parse_date(p.get("publicationDate"))
        da = _days_ago(published)
        if da is not None and da > lookback_days:
            continue

        paper_id = p.get("paperId") or (p.get("externalIds") or {}).get("DOI") or p.get("url") or p.get("title")
        authors = [a.get("name") for a in (p.get("authors") or []) if a.get("name")]
        items.append(
            Item(
                source="semanticscholar",
                uid=str(paper_id),
                title=_norm_text(p.get("title") or ""),
                authors=authors,
                year=p.get("year"),
                abstract=_norm_text(p.get("abstract") or ""),
                url=p.get("url") or "",
                published_at=published,
                extra={},
            )
        )
    return items


# ---------------------------
# 抓取：Google Scholar（可选，SerpAPI）
# ---------------------------


def fetch_google_scholar_serpapi(cfg: Dict[str, Any], query: str) -> Tuple[List[Item], str]:
    scfg = cfg["sources"]["google_scholar"]
    if not scfg.get("enabled", True):
        return [], "disabled"

    api_key = os.environ.get("SERPAPI_KEY", "").strip()
    if not api_key:
        return [], "missing_SERPAPI_KEY"

    max_results = int(scfg.get("max_results", 20))
    lookback_days = int(scfg.get("lookback_days", 14))

    # SerpAPI: https://serpapi.com/google-scholar-api
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_scholar",
        "q": query,
        "api_key": api_key,
        # 用 as_ylo 约束年份（lookback_days 粗略按年；精确增量仍靠 seen 去重）
    }
    r = requests.get(url, params=params, timeout=60)
    r.raise_for_status()
    data = r.json()

    items: List[Item] = []
    for res in (data.get("organic_results") or [])[:max_results]:
        title = _norm_text(res.get("title") or "")
        link = res.get("link") or ""
        snippet = _norm_text(res.get("snippet") or "")

        # Scholar 通常不给结构化摘要，这里用 snippet 作为弱摘要
        # 发布时间字段不稳定，尽量解析 res.get("publication_info", {}).get("summary")
        pub_summary = ((res.get("publication_info") or {}).get("summary") or "")
        published = _parse_date(pub_summary)
        da = _days_ago(published)
        if da is not None and da > lookback_days:
            continue

        authors: List[str] = []
        if " - " in pub_summary:
            authors_part = pub_summary.split(" - ", 1)[0]
            # 粗略按逗号切
            authors = [a.strip() for a in authors_part.split(",") if a.strip()]

        items.append(
            Item(
                source="googlescholar",
                uid=link or title,
                title=title,
                authors=authors,
                year=None,
                abstract=snippet,
                url=link,
                published_at=published,
                extra={"publication_info": pub_summary},
            )
        )

    return items, "ok"


# ---------------------------
# 相关度排序 / 小结生成
# ---------------------------


def _keyword_hit(text: str, keyword: str) -> bool:
    if not keyword:
        return False
    return keyword.lower() in (text or "").lower()


def score_item(cfg: Dict[str, Any], it: Item) -> Tuple[float, Dict[str, Any]]:
    qcfg = cfg["queries"]
    scfg = cfg["scoring"]
    w = scfg["weights"]

    title = it.title or ""
    abstract = it.abstract or ""
    title_l = title.lower()
    abstract_l = abstract.lower()

    def count_hits(keywords: Iterable[str], text_l: str) -> Tuple[int, List[str]]:
        hits = []
        for kw in keywords:
            if kw and kw.lower() in text_l:
                hits.append(kw)
        # 按去重后的命中计数（避免同义词重复多次算分，可以在 config 里自己细化）
        uniq = []
        seen = set()
        for h in hits:
            hl = h.lower()
            if hl not in seen:
                uniq.append(h)
                seen.add(hl)
        return len(uniq), uniq

    n_title, hit_title = count_hits(qcfg["core_topics"] + qcfg["application_scenarios"] + qcfg["methods"], title_l)
    n_abs, hit_abs = count_hits(qcfg["core_topics"], abstract_l)
    n_scenario, hit_scenario = count_hits(qcfg["application_scenarios"], title_l + " " + abstract_l)
    n_method, hit_method = count_hits(qcfg["methods"], title_l + " " + abstract_l)

    score = 0.0
    score += w["title_keyword"] * n_title
    score += w["abstract_keyword"] * n_abs
    score += w["scenario_keyword"] * n_scenario
    score += w["method_keyword"] * n_method

    # 时效性奖励：指数衰减（越新越高）
    days = _days_ago(it.published_at)
    if days is not None:
        half_life = float(scfg.get("recency_half_life_days", 10))
        # 0 天 -> 1，half_life -> 0.5
        rec = math.exp(-math.log(2.0) * (days / max(1e-6, half_life)))
        score += float(w["recency_bonus"]) * rec

    if it.source == "arxiv":
        score += float(w.get("source_bonus_arxiv", 0.0))
    elif it.source == "semanticscholar":
        score += float(w.get("source_bonus_semanticscholar", 0.0))
    elif it.source == "googlescholar":
        score += float(w.get("source_bonus_scholar", 0.0))

    debug = {
        "hit_title": hit_title,
        "hit_abstract": hit_abs,
        "hit_scenario": hit_scenario,
        "hit_method": hit_method,
        "days_ago": days,
    }
    return score, debug


def llm_available(cfg: Dict[str, Any]) -> bool:
    if not cfg.get("summarization", {}).get("use_llm_if_available", True):
        return False
    return bool(os.environ.get("OPENAI_API_KEY", "").strip())


def llm_summarize(cfg: Dict[str, Any], it: Item) -> str:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.environ.get("OPENAI_MODEL") or cfg.get("summarization", {}).get("llm", {}).get("model", "gpt-4o-mini")
    max_chars = int(cfg.get("summarization", {}).get("llm", {}).get("max_chars_per_paper", 6000))

    content = {
        "title": it.title,
        "authors": it.authors[:10],
        "year": it.year,
        "source": it.source,
        "url": it.url,
        "abstract": it.abstract[:max_chars],
    }

    prompt = f"""
你是研究助理。请严格基于给定信息（主要是摘要）生成“文献小结”，不要编造未提供的实验细节/数据集/结果数值。
输出使用中文，且必须按以下小标题组织（没有信息就写“未在摘要中明确给出”）：

### 背景/问题
### 方法
### 实验/数据
### 结果
### 结论/启示（面向电商发券、定价、营销算法等应用）

给定信息（JSON）：
{json.dumps(content, ensure_ascii=False, indent=2)}
""".strip()

    url = f"{base_url}/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是严谨的学术研究助理。"},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }
    r = requests.post(url, headers=headers, json=payload, timeout=120)
    r.raise_for_status()
    data = r.json()
    text = ((data.get("choices") or [{}])[0].get("message") or {}).get("content") or ""
    return text.strip()


def heuristic_summarize(it: Item) -> str:
    """
    在没有 LLM 的情况下：尽量从摘要中提炼结构化小结（粗略，且只基于摘要）。
    """
    abs_text = _norm_text(it.abstract or "")
    sents = re.split(r"(?<=[。！？.!?])\s+", abs_text)
    sents = [s.strip() for s in sents if s.strip()]

    def pick(predicate) -> List[str]:
        out = []
        for s in sents:
            if predicate(s.lower()):
                out.append(s)
        return out

    background = sents[:2] if sents else ["未提供摘要。"]
    method = pick(lambda x: any(k in x for k in ["we propose", "we present", "we develop", "our method", "propose", "framework", "approach", "model", "identify"]))
    exp = pick(lambda x: any(k in x for k in ["experiment", "dataset", "data", "field", "online", "offline", "simulation", "ab test", "a/b"]))
    results = pick(lambda x: any(k in x for k in ["outperform", "improve", "better", "state-of-the-art", "significant", "increase", "lift", "效果", "提升", "显著"]))
    conclusion = sents[-1:] if sents else []

    def fmt(lines: List[str]) -> str:
        if not lines:
            return "未在摘要中明确给出。"
        return " ".join(lines[:3])

    return "\n".join(
        [
            "### 背景/问题",
            fmt(background),
            "",
            "### 方法",
            fmt(method),
            "",
            "### 实验/数据",
            fmt(exp),
            "",
            "### 结果",
            fmt(results),
            "",
            "### 结论/启示（面向电商发券、定价、营销算法等应用）",
            fmt(conclusion),
        ]
    ).strip()


def summarize(cfg: Dict[str, Any], it: Item) -> str:
    if llm_available(cfg):
        try:
            return llm_summarize(cfg, it)
        except Exception as e:
            # 兜底：避免 workflow 失败
            return heuristic_summarize(it) + f"\n\n> 注：LLM 小结失败，已回退到启发式摘要。错误：{e}"
    return heuristic_summarize(it)


def build_queries(cfg: Dict[str, Any]) -> Dict[str, Any]:
    """
    将 config.yml 的关键词组合成：
    - arXiv 的 query 列表（少量、短一些，避免过长）
    - S2 / Scholar 的 query 字符串
    """
    qcfg = cfg["queries"]
    core = qcfg["core_topics"][:3]
    scen = qcfg["application_scenarios"][:5]
    meth = qcfg["methods"][:5]

    # arXiv query：使用 all: 并用 OR 组合
    def arxiv_or(parts: List[str]) -> str:
        # all:"xxx" OR all:"yyy"
        safe = []
        for p in parts:
            p = p.strip()
            if not p:
                continue
            if " " in p:
                safe.append(f'all:"{p}"')
            else:
                safe.append(f"all:{p}")
        if not safe:
            return ""
        return "(" + "+OR+".join(safe) + ")"

    arxiv_queries = []
    # 组合 2~3 个 query，兼顾覆盖面与长度
    arxiv_queries.append(arxiv_or(["causal inference", "uplift modeling"]) + "+AND+" + arxiv_or(scen))
    arxiv_queries.append(arxiv_or(["policy learning", "treatment effect", "CATE"]) + "+AND+" + arxiv_or(["marketing", "pricing", "e-commerce"]))
    arxiv_queries.append(arxiv_or(meth) + "+AND+" + arxiv_or(["coupon", "pricing", "promotion"]))

    # S2/Scholar query：用自然语言检索串即可
    s2_query = " OR ".join([f'"{x}"' for x in core]) + " AND (" + " OR ".join([f'"{x}"' for x in scen]) + ")"
    scholar_query = "causal inference marketing pricing coupon e-commerce uplift CATE"

    return {"arxiv_queries": arxiv_queries, "s2_query": s2_query, "scholar_query": scholar_query}


def render_report(
    cfg: Dict[str, Any],
    date_: dt.date,
    ranked: List[Tuple[float, Item, Dict[str, Any], str]],
    notes: List[str],
) -> str:
    lines: List[str] = []
    lines.append(f"# CausalRadar 日报 - {date_.isoformat()}")
    lines.append("")
    lines.append(f"- 新增条目数：**{len(ranked)}**")
    lines.append(f"- 数据源：arXiv / Semantic Scholar /（可选）Google Scholar")
    lines.append("")
    if notes:
        lines.append("## 运行备注")
        for n in notes:
            lines.append(f"- {n}")
        lines.append("")

    lines.append("## 今日新增（按相关度排序）")
    lines.append("")

    if not ranked:
        lines.append("今日未发现新的高相关条目（或全部已收录）。")
        return "\n".join(lines).strip() + "\n"

    for idx, (score, it, debug, summ) in enumerate(ranked, start=1):
        lines.append(f"### {idx}. {it.title}")
        lines.append("")
        meta = []
        if it.authors:
            meta.append("作者：" + ", ".join(it.authors[:8]) + (" 等" if len(it.authors) > 8 else ""))
        if it.year:
            meta.append(f"年份：{it.year}")
        if it.published_at:
            meta.append(f"发布时间：{it.published_at.date().isoformat()}")
        meta.append(f"来源：{it.source}")
        meta.append(f"相关度分：**{score:.2f}**")
        lines.append("- " + "｜".join(meta))
        if it.url:
            lines.append(f"- 链接：{it.url}")
        lines.append("")
        # 命中信息（便于你校验排序是否合理）
        hits = []
        for k in ["hit_scenario", "hit_method", "hit_title", "hit_abstract"]:
            if debug.get(k):
                hits.append(f"{k}={debug.get(k)}")
        if hits:
            lines.append("> 命中：" + "；".join(hits))
            lines.append("")
        lines.append(summ.strip())
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def main() -> int:
    cfg = _read_yaml(os.path.join(ROOT, "config.yml"))
    q = build_queries(cfg)

    state_path = os.path.join(ROOT, "data", "seen.json")
    state = _read_json(state_path, {"seen": []})
    seen = set(state.get("seen") or [])

    notes: List[str] = []

    # 1) 拉取候选
    items: List[Item] = []
    # 重要：在 GitHub Actions 上，任何单一数据源的偶发失败（限流/网络波动）
    # 不应该导致整次任务失败。因此这里对各数据源做容错，失败则记备注并继续。
    try:
        items.extend(fetch_arxiv(cfg, q["arxiv_queries"]))
    except Exception as e:
        notes.append(f"arXiv 抓取失败（已跳过）：{type(e).__name__}: {e}")

    try:
        items.extend(fetch_semantic_scholar(cfg, q["s2_query"]))
    except Exception as e:
        notes.append(f"Semantic Scholar 抓取失败（已跳过）：{type(e).__name__}: {e}")

    try:
        scholar_items, scholar_status = fetch_google_scholar_serpapi(cfg, q["scholar_query"])
        if scholar_status != "ok":
            if scholar_status == "missing_SERPAPI_KEY":
                notes.append("未设置 SERPAPI_KEY：已跳过 Google Scholar（建议使用 SerpAPI 以保证稳定）。")
            elif scholar_status == "disabled":
                notes.append("Google Scholar 数据源被禁用。")
            else:
                notes.append(f"Google Scholar 抓取状态：{scholar_status}")
        items.extend(scholar_items)
    except Exception as e:
        notes.append(f"Google Scholar 抓取失败（已跳过）：{type(e).__name__}: {e}")

    # 2) 过滤增量（仅保留未见过的）
    only_new = bool(cfg.get("output", {}).get("include_only_new_items", True))
    fresh: List[Item] = []
    for it in items:
        if only_new and it.dedup_key in seen:
            continue
        # 基本质量过滤：无标题的跳过
        if not it.title:
            continue
        fresh.append(it)

    # 3) 相关度打分、排序、小结
    ranked_raw: List[Tuple[float, Item, Dict[str, Any]]] = []
    for it in fresh:
        score, debug = score_item(cfg, it)
        ranked_raw.append((score, it, debug))

    ranked_raw.sort(key=lambda x: x[0], reverse=True)

    max_items = int(cfg.get("output", {}).get("max_items_in_report", 30))
    ranked_raw = ranked_raw[:max_items]

    ranked: List[Tuple[float, Item, Dict[str, Any], str]] = []
    for score, it, debug in ranked_raw:
        summ = summarize(cfg, it)
        ranked.append((score, it, debug, summ))

    # 4) 输出报告 + 更新增量状态
    date_ = _today_utc()
    report_text = render_report(cfg, date_, ranked, notes)

    reports_dir = cfg.get("output", {}).get("reports_dir", "reports")
    report_path = os.path.join(ROOT, reports_dir, f"{date_.isoformat()}.md")
    latest_path = os.path.join(ROOT, cfg.get("output", {}).get("latest_report", "reports/latest.md"))

    _write_text(report_path, report_text)
    _write_text(latest_path, report_text)

    # 更新 seen：把本次“新增”写入（无论是否最终进入 topN，都算已见过）
    for it in fresh:
        seen.add(it.dedup_key)
    _write_json(state_path, {"seen": sorted(seen)})

    print(f"Wrote report: {os.path.relpath(report_path, ROOT)}")
    print(f"Updated state: {os.path.relpath(state_path, ROOT)} (seen={len(seen)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
