(function () {
  const languageStorageKey = "stardew-wiiu-language";
  const languageButton = document.querySelector(".language-toggle");
  const metaDescription = document.querySelector('meta[name="description"]');
  const requestedLanguage = new URLSearchParams(window.location.search).get("lang");
  let currentLanguage = requestedLanguage === "en" || requestedLanguage === "pt-BR"
    ? requestedLanguage
    : "pt-BR";

  if (requestedLanguage !== "en" && requestedLanguage !== "pt-BR") {
    try {
      const storedLanguage = localStorage.getItem(languageStorageKey);
      if (storedLanguage === "en" || storedLanguage === "pt-BR") {
        currentLanguage = storedLanguage;
      }
    } catch (error) {
      if (error.name !== "SecurityError") throw error;
    }
  }

  const defaults = {
    title: document.title,
    description: metaDescription ? metaDescription.content : "",
    text: new Map(),
    html: new Map(),
    aria: new Map()
  };
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    defaults.text.set(element, element.textContent);
  });
  document.querySelectorAll("[data-i18n-html]").forEach((element) => {
    defaults.html.set(element, element.innerHTML);
  });
  document.querySelectorAll("[data-i18n-aria-label]").forEach((element) => {
    defaults.aria.set(element, element.getAttribute("aria-label"));
  });

  function restoreDefaults() {
    document.title = defaults.title;
    if (metaDescription) metaDescription.content = defaults.description;
    defaults.text.forEach((value, element) => {
      element.textContent = value;
    });
    defaults.html.forEach((value, element) => {
      element.innerHTML = value;
    });
    defaults.aria.forEach((value, element) => {
      element.setAttribute("aria-label", value);
    });
  }

  function applyTranslations(content) {
    document.querySelectorAll("[data-i18n]").forEach((element) => {
      const value = content[element.dataset.i18n];
      if (value !== undefined) element.textContent = value;
    });
    document.querySelectorAll("[data-i18n-html]").forEach((element) => {
      const value = content[element.dataset.i18nHtml];
      if (value !== undefined) element.innerHTML = value;
    });
    document.querySelectorAll("[data-i18n-aria-label]").forEach((element) => {
      const value = content[element.dataset.i18nAriaLabel];
      if (value !== undefined) element.setAttribute("aria-label", value);
    });
  }

  function setLanguage(language) {
    currentLanguage = language;
    try {
      localStorage.setItem(languageStorageKey, language);
    } catch (error) {
      if (error.name !== "SecurityError") throw error;
    }

    const content = window.pageTranslations && window.pageTranslations[language];
    restoreDefaults();
    document.documentElement.lang = language === "en" ? "en" : "pt-BR";

    if (content) {
      if (content.pageTitle) document.title = content.pageTitle;
      if (metaDescription && content.pageDescription) metaDescription.content = content.pageDescription;
      applyTranslations(content);
    }

    if (languageButton) languageButton.textContent = language === "en" ? "PT-BR" : "EN";

    document.querySelectorAll(".lang-link").forEach((link) => {
      const url = new URL(link.href, window.location.href);
      url.searchParams.set("lang", language);
      link.href = url.href;
    });

    const pageUrl = new URL(window.location.href);
    pageUrl.searchParams.set("lang", language);
    history.replaceState(null, "", pageUrl);
  }

  if (languageButton) {
    languageButton.addEventListener("click", () => {
      setLanguage(currentLanguage === "pt-BR" ? "en" : "pt-BR");
    });
  }
  setLanguage(currentLanguage);
})();
