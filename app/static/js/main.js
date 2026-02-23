(function () {
  const btnSearch = document.querySelector(".btn-search");
  const searchBar = document.querySelector(".mobile-search");

  function closeSearch() {
    if (!searchBar) return;
    searchBar.style.display = "none";
  }

  function openSearch() {
    if (!searchBar) return;
    searchBar.style.display = "block";
    const input = searchBar.querySelector("input");
    if (input) input.focus();
  }

  if (btnSearch && searchBar) {
    btnSearch.addEventListener("click", () => {
      const isOpen = searchBar.style.display === "block";
      if (isOpen) closeSearch();
      else openSearch();
    });
  }

  const clearBtn = document.querySelector(".mobile-search-clear");
  if (clearBtn && searchBar) {
    clearBtn.addEventListener("click", () => {
      const input = searchBar.querySelector("input");
      if (input) input.value = "";
      closeSearch();
    });
  }

  // Register Service Worker
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => {
      navigator.serviceWorker.register("/static/sw.js").catch(() => {});
    });
  }
})();
