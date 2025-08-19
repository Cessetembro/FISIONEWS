# update_feed.py
import json, datetime, feedparser

# Fontes (pode ajustar depois)
SOURCES = {
    "PubMed":   "https://pubmed.ncbi.nlm.nih.gov/rss/search/1kY91pu7vBZiKMcK2hTq42zbmX9/?limit=10",
    "COFFITO":  "https://www.coffito.gov.br/nsite/feed/",
    "Medscape": "https://www.medscape.com/rss/siteindex/0",
}

MAX_ITEMS = 30
items = []

for src_name, url in SOURCES.items():
    try:
        rss = feedparser.parse(url)
        for e in rss.entries[:10]:
            items.append({
                "title":   e.get("title", "Sem título"),
                "summary": e.get("summary", "Resumo não disponível"),
                "link":    e.get("link", "#"),
                "source":  src_name,
                "published": e.get("published", ""),
            })
    except Exception as ex:
        print(f"[WARN] Falha em {src_name}: {ex}")

# Mantém até 30 (simples); se quiser ordenar por data, dá pra evoluir depois
items = items[:MAX_ITEMS]

with open("feed.json", "w", encoding="utf-8") as f:
    json.dump(
        {"updated_at": datetime.datetime.utcnow().isoformat() + "Z", "items": items},
        f, ensure_ascii=False, indent=2
    )

print(f"✅ {len(items)} itens gravados em feed.json")
