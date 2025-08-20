import json, feedparser, datetime
# Fontes de notícias generalistas - URLs confiáveis e amplamente acessíveis
sources = {
    "G1 Globo": "https://g1.globo.com/rss/g1/",
    "BBC News World": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "Reuters World News": "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
    "Globo.com": "https://g1.globo.com/dynamo/rss2.xml",
    "BBC News Brasil": "https://feeds.bbci.co.uk/portuguese/rss.xml"
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
