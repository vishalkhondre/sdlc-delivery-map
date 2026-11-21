/* Navigation and theme enhance static HTML. Topic and map links also work offline. */
(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const byId = id => document.getElementById(id);
  const siteRoot = document.body.dataset.root || '';
  byId('theme-toggle')?.addEventListener('click', () => {
    const root = document.documentElement;
    const current = root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    const next = current === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('delivery-map-theme', next); } catch (error) { /* optional storage */ }
  });

  const search = byId('topic-search');
  document.addEventListener('keydown', event => {
    if (event.key !== '/' || event.ctrlKey || event.metaKey || event.altKey || event.target.matches('input, textarea, select, [contenteditable]')) return;
    event.preventDefault();
    if (search) search.focus();
    else window.location.href = siteRoot + 'topics.html#topic-search';
  });
  if (search) {
    const phase = byId('phase-select');
    const rows = [...document.querySelectorAll('.topic-row')];
    const groupHeadings = [...document.querySelectorAll('[data-index-phase]')];
    const fold = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    const searchIndex = rows.map(row => ({row, text: fold(row.dataset.text), phase: row.dataset.phase}));
    const params = new URLSearchParams(window.location.search);
    search.value = params.get('q') || '';
    phase.value = params.get('phase') || '';
    function filter(updateLocation) {
      const tokens = fold(search.value.trim()).split(/\s+/).filter(Boolean);
      const found = new Set();
      let count = 0;
      for (const item of searchIndex) {
        const matches = (!phase.value || item.phase === phase.value) && tokens.every(token => item.text.includes(token));
        item.row.hidden = !matches;
        if (matches) { count++; found.add(item.phase); }
      }
      for (const section of groupHeadings) section.hidden = !found.has(section.dataset.indexPhase);
      byId('result-count').textContent = count + (count === 1 ? ' topic' : ' topics');
      byId('no-results').hidden = count > 0;
      if (updateLocation && window.location.protocol !== 'file:') {
        const next = new URL(window.location.href);
        if (search.value) next.searchParams.set('q', search.value);
        else next.searchParams.delete('q');
        if (phase.value) next.searchParams.set('phase', phase.value);
        else next.searchParams.delete('phase');
        next.hash = '';
        window.history.replaceState({}, '', next);
      }
    }
    search.addEventListener('input', () => filter(true));
    phase.addEventListener('change', () => filter(true));
    byId('clear-search').addEventListener('click', () => { search.value = ''; phase.value = ''; filter(true); search.focus(); });
    filter(false);
    if (window.location.hash === '#topic-search') search.focus();
  }

  const map = byId('delivery-map');
  if (map) {
    const figure = byId('map');
    const canvas = byId('map-canvas');
    const expand = byId('map-expand');
    let zoom = 100;
    let expanded = false;
    const steps = [100, 125, 150, 200, 250, 300, 400, 500];
    function setZoom(value) {
      zoom = value;
      map.style.width = zoom + '%';
      canvas.classList.toggle('is-zoomed', zoom > 100);
      byId('zoom-level').textContent = zoom + '%';
      byId('zoom-out').disabled = zoom <= steps[0];
      byId('zoom-in').disabled = zoom >= steps[steps.length - 1];
      if (zoom === 100) { canvas.scrollTop = 0; canvas.scrollLeft = 0; }
    }
    function toggleExpand(value) {
      expanded = value;
      figure.classList.toggle('map-dialog', expanded);
      document.body.classList.toggle('map-dialog-open', expanded);
      expand.setAttribute('aria-pressed', String(expanded));
      expand.querySelector('span').textContent = expanded ? 'Close' : 'Expand';
      const background = document.querySelectorAll('.topbar,.site-footer,.intro,.route-section,.lookup-links,.skip');
      background.forEach(el => { el.inert = expanded; });
      if (expanded) {
        figure.setAttribute('role', 'dialog');
        figure.setAttribute('aria-modal','true');
        figure.setAttribute('aria-label','Expanded delivery map');
      } else {
        figure.removeAttribute('role');
        figure.removeAttribute('aria-modal');
        figure.removeAttribute('aria-label');
      }
      expand.focus();
    }
    expand.addEventListener('click',()=>toggleExpand(!expanded));
    byId('zoom-in').addEventListener('click',()=>setZoom(steps[Math.min(steps.indexOf(zoom)+1, steps.length-1)]));
    byId('zoom-out').addEventListener('click',()=>setZoom(steps[Math.max(steps.indexOf(zoom)-1, 0)]));
    byId('zoom-fit').addEventListener('click',()=>setZoom(100));
    document.addEventListener('keydown', event => {
      if (!expanded) return;
      if (event.key === 'Escape') { event.preventDefault(); toggleExpand(false); return; }
      if(event.key !== 'Tab') return;
      const focusables = [...figure.querySelectorAll('a[href], button:not([disabled]), [tabindex="0"]')];
      const first=focusables[0],last=focusables[focusables.length-1];
      if (event.shiftKey && document.activeElement===first){ event.preventDefault(); last.focus(); }
      if (!event.shiftKey && document.activeElement===last){ event.preventDefault(); first.focus(); }
    });
    setZoom(100);
  }
})();
