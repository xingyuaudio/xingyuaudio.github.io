(() => {
  'use strict';
  const tools = document.querySelector('.publication-tools');
  if (!tools) return;
  const buttons = Array.from(tools.querySelectorAll('[data-topic]'));
  const papers = Array.from(document.querySelectorAll('#publication-list .publication'));
  const groups = Array.from(document.querySelectorAll('.year-group'));
  const search = document.getElementById('paper-search');
  const count = document.getElementById('results-count');
  const empty = document.getElementById('empty-state');
  let topic = 'All';
  const initial = new URLSearchParams(window.location.search).get('topic');
  if (buttons.some(button => button.dataset.topic === initial)) topic = initial;
  function filter() {
    const query = search.value.trim().toLocaleLowerCase();
    let shown = 0;
    papers.forEach(paper => {
      const visible = (topic === 'All' || paper.dataset.topic === topic) && paper.textContent.toLocaleLowerCase().includes(query);
      paper.hidden = !visible;
      if (visible) shown += 1;
    });
    groups.forEach(group => { group.hidden = !Array.from(group.querySelectorAll('.publication')).some(paper => !paper.hidden); });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.topic === topic)));
    count.textContent = `${shown} of ${papers.length} records`;
    empty.hidden = shown !== 0;
  }
  buttons.forEach(button => button.addEventListener('click', () => {
    topic = button.dataset.topic;
    const url = new URL(window.location.href);
    if (topic === 'All') url.searchParams.delete('topic'); else url.searchParams.set('topic', topic);
    window.history.replaceState(null, '', url);
    filter();
  }));
  search.addEventListener('input', filter);
  tools.hidden = false;
  filter();
})();
