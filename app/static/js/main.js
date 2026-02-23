(function () {
  // Toggle busca no header (se existir)
  const btnSearch = document.querySelector(".btn-search");
  const searchBar = document.querySelector(".mobile-search");

  if (btnSearch && searchBar) {
    btnSearch.addEventListener("click", () => {
      const isOpen = searchBar.style.display === "block";
      searchBar.style.display = isOpen ? "none" : "block";
      const input = searchBar.querySelector("input");
      if (!isOpen && input) input.focus();
    });
  }

  // Nome usuário (se quiser alimentar via server no futuro)
  const userName = document.querySelector(".user-name");
  if (userName && !userName.textContent.trim()) {
    userName.textContent = "Eduardo";
  }

  // Register Service Worker
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => {
      navigator.serviceWorker.register("/static/sw.js").catch(() => {
        // silencioso para não irritar UX
      });
    });
  }
})();
