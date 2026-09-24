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

const slides = [...document.querySelectorAll('.hero-slide')];
const dots = [...document.querySelectorAll('.hero-dots button')];
if (slides.length && dots.length) {
  let activeSlide = 0;
  let timer;
  const showSlide = index => {
    activeSlide = index;
    slides.forEach((slide, i) => slide.classList.toggle('is-active', i === index));
    dots.forEach((dot, i) => {
      dot.classList.toggle('is-active', i === index);
      if (i === index) dot.setAttribute('aria-current', 'true');
      else dot.removeAttribute('aria-current');
    });
  };
  const start = () => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    timer = window.setInterval(() => showSlide((activeSlide + 1) % slides.length), 6500);
  };
  dots.forEach((dot, index) => dot.addEventListener('click', () => {
    window.clearInterval(timer);
    showSlide(index);
    start();
  }));
  document.addEventListener('visibilitychange', () => {
    window.clearInterval(timer);
    if (!document.hidden) start();
  });
  start();
}

const roadmap = document.querySelector('#roadmap');
const roadmapPath = roadmap?.querySelector('.roadmap-path-progress');
if (roadmap && roadmapPath) {
  const pathLength = roadmapPath.getTotalLength();
  roadmapPath.style.strokeDasharray = String(pathLength);
  const updateRoadmap = () => {
    const bounds = roadmap.getBoundingClientRect();
    const start = window.innerHeight * 0.55;
    const progress = Math.max(0, Math.min(1, (start - bounds.top) / (bounds.height - window.innerHeight * 0.45)));
    roadmapPath.style.strokeDashoffset = String(pathLength * (1 - progress));
  };
  window.addEventListener('scroll', updateRoadmap, { passive: true });
  window.addEventListener('resize', updateRoadmap);
  updateRoadmap();
}

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
