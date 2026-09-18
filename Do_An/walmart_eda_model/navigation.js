// Streamlit scrolls its main container independently of the browser window.
// Wait for the newly selected page to be committed, then reset both surfaces.
(() => {
  // A re-mounted HTML element must not repeat navigation scrolling on filter edits.
  const revision = __NAVIGATION_REVISION__;
  if (window.__walmartNavigationRevision === revision) return;
  window.__walmartNavigationRevision = revision;
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      const main = document.querySelector('[data-testid="stMain"]')
        || document.querySelector('section.main');
      main?.scrollTo({ top: 0, left: 0, behavior: 'instant' });
      document.scrollingElement?.scrollTo({ top: 0, left: 0, behavior: 'instant' });
      window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
    });
  });
})();
