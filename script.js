async function loadFeed() {
  const container = document.getElementById("news-container");
  container.innerHTML = "<p>⏳ Carregando notícias...</p>";

  try {
    const res = await fetch("./feed.json?_=" + Date.now()); // evita cache
    if (!res.ok) throw new Error("Falha ao carregar feed.json");
    const data = await res.json();

    if (!data.items || data.items.length === 0) {
      container.innerHTML = "<p>Nenhuma notícia disponível no momento.</p>";
      return;
    }

    container.innerHTML = "";

    data.items.forEach(item => {
      const card = document.createElement("div");
      card.className = "news-card";

      const pubDate = new Date(item.published);
      const pubStr = pubDate.toLocaleDateString("pt-BR", {
        day: "2-digit",
        month: "short",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit"
      });

      card.innerHTML = `
        <h3><a href="${item.link}" target="_blank">${item.title}</a></h3>
        <p class="summary">${item.summary || "Resumo não disponível"}</p>
        <div class="meta">
          <span class="source">📌 ${item.source}</span>
          <span class="date">🕒 ${pubStr}</span>
        </div>
      `;

      container.appendChild(card);
    });

  } catch (err) {
    container.innerHTML = `<p>⚠️ Erro: ${err.message}</p>`;
    console.error(err);
  }
}

document.addEventListener("DOMContentLoaded", loadFeed);
