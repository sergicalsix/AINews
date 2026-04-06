const CATEGORY_LABELS = {
  japan: '日本',
  international: '海外',
  company_blog: '企業ブログ',
  arxiv: 'arXiv'
};

let allNews = [];
let currentCategory = 'all';
let currentMaxDays = 3;

async function loadNews() {
  const loading = document.getElementById('loading');
  const empty = document.getElementById('empty');
  const container = document.getElementById('newsContainer');

  try {
    const res = await fetch('data/news.json');
    if (!res.ok) throw new Error('Failed to load');
    const data = await res.json();
    allNews = data.articles || [];
    document.getElementById('lastUpdated').textContent =
      `最終更新: ${data.lastUpdated || '不明'}`;
    loading.style.display = 'none';
    renderNews();
  } catch (e) {
    loading.style.display = 'none';
    empty.style.display = 'block';
    empty.textContent = 'ニュースデータの読み込みに失敗しました。';
    console.error(e);
  }
}

function renderNews() {
  const container = document.getElementById('newsContainer');
  const empty = document.getElementById('empty');

  let filtered = currentCategory === 'all'
    ? allNews
    : allNews.filter(n => n.category === currentCategory);

  if (currentMaxDays > 0) {
    const now = new Date();
    now.setHours(23, 59, 59, 999);
    const cutoff = new Date(now);
    cutoff.setDate(cutoff.getDate() - currentMaxDays);
    filtered = filtered.filter(n => {
      if (!n.date) return false;
      const d = new Date(n.date);
      return d >= cutoff;
    });
  }

  if (filtered.length === 0) {
    container.innerHTML = '';
    empty.style.display = 'block';
    return;
  }

  empty.style.display = 'none';

  container.innerHTML = filtered.map(item => {
    const badge = `<span class="badge ${item.category}">${CATEGORY_LABELS[item.category] || item.category}</span>`;
    const source = item.source ? `<span class="source">${item.source}</span>` : '';
    const date = item.date ? `<span class="date">${item.date}</span>` : '';
    const authors = item.authors ? `<div class="authors">${item.authors}</div>` : '';
    const title = item.title_ja || item.title;
    const link = item.url
      ? `<a href="${item.url}" target="_blank" rel="noopener">${escapeHtml(title)}</a>`
      : escapeHtml(title);

    return `
      <article class="news-card">
        <div class="meta">${badge} ${source} ${date}</div>
        <h3>${link}</h3>
        <div class="summary">${escapeHtml(item.summary || '')}</div>
        ${authors}
      </article>
    `;
  }).join('');
}

function escapeHtml(text) {
  const d = document.createElement('div');
  d.textContent = text;
  return d.innerHTML;
}

// Tab navigation
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    currentCategory = tab.dataset.category;
    renderNews();
  });
});

// Date filter
document.getElementById('dateRange').addEventListener('change', (e) => {
  currentMaxDays = parseInt(e.target.value, 10);
  renderNews();
});

loadNews();
