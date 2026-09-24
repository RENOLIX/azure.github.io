const menuButton = document.querySelector('.menu-toggle');
const mobileNav = document.querySelector('.mobile-nav');
if (menuButton && mobileNav) {
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
    mobileNav.hidden = !open;
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !mobileNav.hidden) {
      mobileNav.hidden = true;
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.setAttribute('aria-label', 'Ouvrir le menu');
      menuButton.focus();
    }
  });
}

const form = document.querySelector('#contact-form');
if (form) {
  const params = new URLSearchParams(location.search);
  const product = params.get('produit');
  if (product) form.elements.sujet.value = `Information sur les produits : ${product}`;
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const values = new FormData(form);
    const subject = `[Site Azuré Pharm] ${values.get('sujet')}`;
    const body = `Nom : ${values.get('nom')}\nE-mail : ${values.get('email')}\nTéléphone : ${values.get('telephone') || 'Non indiqué'}\n\nMessage :\n${values.get('message')}`;
    location.href = `mailto:eurlazurepharm@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    document.querySelector('#form-note').textContent = 'Votre message est prêt dans votre application de messagerie. Vérifiez-le puis envoyez-le.';
  });
}
