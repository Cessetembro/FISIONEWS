async function carregarNoticias() {
    try {
        const response = await fetch('feed.json');
        const data = await response.json();
        const container = document.getElementById('news-container');
        container.innerHTML = '';
        data.items.forEach(item => {
            const card = document.createElement('div');
            card.classList.add('card');
            card.innerHTML = `<h2>${item.title}</h2><p>${item.summary}</p><a href="${item.link}" target="_blank">Ler mais</a>`;
            container.appendChild(card);
        });
    } catch (error) {
        console.error('Erro ao carregar notícias', error);
    }
}
carregarNoticias();