import json, feedparser, datetime
# Fontes acadêmicas e de pesquisa - URLs abertas e confiáveis
sources = {
    "arXiv Computer Science": "https://export.arxiv.org/rss/cs",
    "MIT News - Health & Medicine": "http://news.mit.edu/rss/topic/health-medicine",
    "NASA Breaking News": "https://www.nasa.gov/rss/dyn/breaking_news.rss",
    "Phys.org": "https://phys.org/rss-feed/",
    "Python Software Foundation": "https://pyfound.blogspot.com/feeds/posts/default?alt=rss"
}
MAX_ITEMS = 30
feed_items = []
for source, url in sources.items():
    try:
        parsed = feedparser.parse(url)
        for entry in parsed.entries[:10]:
            feed_items.append({
                "title": entry.title,
                "summary": entry.summary if hasattr(entry, "summary") else "Resumo não disponível",
                "link": entry.link,
                "source": source,
                "published": entry.published if hasattr(entry, "published") else "Data não informada"
            })
    except Exception as e:
        print(f"Erro ao processar {source}: {e}")
# Limitar aos itens mais recentes
feed_items = feed_items[:MAX_ITEMS]
with open("feed.json", "w", encoding="utf-8") as f:
    json.dump({"updated_at": datetime.datetime.now().isoformat(), "items": feed_items}, f, ensure_ascii=False, indent=4)
print("Feed atualizado com sucesso!")
