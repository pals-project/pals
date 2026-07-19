// Route the sphinx-book-theme search box to Read the Docs' server-side search.
//
// By default the theme's search box (sidebar + top-bar button) opens the
// theme's built-in client-side search, which is page-granular and does not
// find sub-section headings well. Read the Docs ships a much better
// server-side search, but out of the box it is only reachable from the RTD
// flyout menu and the "/" hotkey. This script makes the existing, prominent
// search box open the RTD server-side search instead.
//
// RTD Addons only run on the hosted readthedocs.io build. On a local
// `make html` build the RTD elements are absent, so we detect that and leave
// the theme's built-in search untouched (no-op fallback).

(function () {
  "use strict";

  // Selectors for the theme's search entry points (sidebar box + top-bar icon).
  var SEARCH_TRIGGERS = ".search-button__button, [role='search'] input";

  function rtdAddonsPresent() {
    // On hosted readthedocs.io builds RTD injects the addons script at serve
    // time (present from load) and the <readthedocs-*> elements at runtime.
    // Local `make html` builds have neither, so search falls back to the theme.
    return !!(
      document.querySelector('script[src*="readthedocs-addons.js"]') ||
      document.querySelector("readthedocs-search, readthedocs-flyout") ||
      window.ReadTheDocsEventData
    );
  }

  function openRtdSearch(event) {
    // Only hijack when the RTD Addons search is actually available.
    if (!rtdAddonsPresent()) {
      return;
    }
    // Prevent the theme's own search modal from also opening.
    event.preventDefault();
    event.stopImmediatePropagation();
    document.dispatchEvent(new CustomEvent("readthedocs-search-show"));
  }

  function wire() {
    document.querySelectorAll(SEARCH_TRIGGERS).forEach(function (el) {
      // Capture phase so we run before the theme's own click handler.
      el.addEventListener("click", openRtdSearch, true);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wire);
  } else {
    wire();
  }
})();
