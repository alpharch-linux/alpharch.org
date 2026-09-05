'use strict';
const search = document.getElementById('providerSearch');
if (search) {
  const category = document.getElementById('categoryFilter');
  const available = document.getElementById('availableOnly');
  const rows = [...document.querySelectorAll('.provider')];
  const filter = () => {
    const terms = search.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
    let count = 0;
    for (const row of rows) {
      row.hidden = !terms.every(term => row.dataset.search.includes(term)) ||
        (category.value && row.dataset.category !== category.value) ||
        (available.checked && !['existing','limited'].includes(row.dataset.status));
      if (!row.hidden) count++;
    }
    for (const section of document.querySelectorAll('.provider-section')) {
      section.hidden = ![...section.querySelectorAll('.provider')].some(row => !row.hidden);
    }
    document.getElementById('resultCount').textContent = `${count} provider guide${count === 1 ? '' : 's'}`;
    document.getElementById('noResults').hidden = count !== 0;
  };
  search.addEventListener('input', filter);
  category.addEventListener('change', filter);
  available.addEventListener('change', filter);
}
document.getElementById('printGuide')?.addEventListener('click', () => {
  const closed = [...document.querySelectorAll('details:not([open])')];
  closed.forEach(item => item.open = true);
  window.addEventListener('afterprint', () => closed.forEach(item => item.open = false), {once:true});
  window.print();
});
