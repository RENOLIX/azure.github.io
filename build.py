from pathlib import Path
from html import escape

ROOT = Path(__file__).parent / "dist"
MAIL = "eurlazurepharm@gmail.com"
PHONE = "0660 456 457"
FACEBOOK = "https://www.facebook.com/share/1R3SXmtx3s/"
INSTAGRAM = "https://www.instagram.com/azurepharm2021?utm_source=qr&stkn=MXd4ZWpmeDU4dXU1Yw=="

nav = [
    ("index.html", "Accueil"),
    ("produits.html", "Nos produits"),
    ("entreprise.html", "Qui sommes-nous"),
    ("recherche.html", "Recherche & développement"),
    ("contact.html", "Contact"),
]

def shell(title, description, current, body):
    links = "".join(f'<a href="{url}"{(" aria-current=\"page\"" if url == current else "")}>{label}</a>' for url, label in nav)
    mobile_links = "".join(f'<a href="{url}"{(" aria-current=\"page\"" if url == current else "")}>{label}</a>' for url, label in nav)
    return f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#101b40">
  <meta name="description" content="{escape(description, quote=True)}">
  <title>{escape(title)} · Azuré Pharm</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23101b40'/%3E%3Cpath d='M12 49 30 13l7 15-7 9-3-7-10 19z' fill='%235d57a5'/%3E%3Cpath d='M31 43c10-15 21-22 27-17 5 5-3 17-17 23l-4-7c10-4 15-10 13-12-3-2-10 4-18 16z' fill='%232d9ddb'/%3E%3C/svg%3E">
  <link rel="stylesheet" href="assets/site.css?v=3">
  <script src="assets/site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#contenu">Aller au contenu</a>
  <div class="topline"><div class="container topline-inner"><span>Fabrication de détergents désinfectants pour le secteur de la santé</span><div><a href="tel:+213660456457">{PHONE}</a><span class="topline-divider">·</span><a href="mailto:{MAIL}">{MAIL}</a></div></div></div>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html" aria-label="Azuré Pharm, accueil"><span class="brand-mark"><img src="assets/azure-pharm-logo.png" alt=""></span><span class="brand-name">AZURÉ <strong>PHARM</strong><small>Votre partenaire de confiance</small></span></a>
      <nav class="desktop-nav" aria-label="Navigation principale">{links}</nav>
      <a class="header-contact" href="contact.html">Nous contacter <span aria-hidden="true">↗</span></a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Ouvrir le menu"><span></span><span></span><span></span></button>
    </div>
    <nav class="mobile-nav" id="mobile-nav" aria-label="Navigation mobile" hidden>{mobile_links}</nav>
  </header>
  <main id="contenu">{body}</main>
  <footer class="site-footer">
    <div class="container footer-main">
      <div class="footer-brand"><div class="footer-brand-name">AZURÉ PHARM<span>.</span></div><p>Votre partenaire de confiance.</p><p>Détergents désinfectants conçus pour les exigences du secteur de la santé.</p></div>
      <div><h2>Explorer</h2><a href="index.html">Accueil</a><a href="produits.html">Nos produits</a><a href="entreprise.html">L’entreprise</a><a href="recherche.html">Recherche & développement</a></div>
      <div><h2>Nous contacter</h2><a href="tel:+213660456457">0660 456 457</a><a href="tel:+213553779211">0553 779 211</a><a href="mailto:{MAIL}">{MAIL}</a><span>Dely Brahim, Alger, Algérie</span></div>
      <div><h2>Suivez-nous</h2><a href="{FACEBOOK}" target="_blank" rel="noopener noreferrer">Facebook ↗</a><a href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer">Instagram ↗</a></div>
    </div>
    <div class="container footer-bottom"><span>© 2026 Azuré Pharm. Tous droits réservés.</span><span>Ouled Moussa · Dely Brahim · Algérie</span></div>
  </footer>
</body>
</html>'''

pages = {
"index.html": ("Accueil", "Azuré Pharm fabrique des détergents désinfectants pour les établissements de santé en Algérie.", '''
<section class="hero"><div class="container hero-grid">
  <div class="hero-copy"><span class="eyebrow"><span class="eyebrow-line"></span> AZURÉ PHARM · DEPUIS 2021</span><h1>L’hygiène au service de la <em>confiance.</em></h1><p>Azuré Pharm produit des détergents désinfectants destinés aux professionnels de santé. Notre engagement : contribuer à des espaces de soins propres et sécuritaires.</p><div class="hero-actions"><a class="button button-primary" href="produits.html">Découvrir nos produits <span aria-hidden="true">↗</span></a><a class="text-link" href="contact.html">Parler à notre équipe <span aria-hidden="true">→</span></a></div><div class="hero-facts"><div><strong>2021</strong><span>Création de l’entreprise</span></div><div><strong>03</strong><span>Familles de produits</span></div><div><strong>Algérie</strong><span>Production locale</span></div></div></div>
  <figure class="hero-visual"><img src="assets/production-illustration.png" alt="Vue illustrative d’une ligne de production de produits d’hygiène"><figcaption>Visuel d’illustration</figcaption></figure>
</div></section>
<section class="section intro-section"><div class="container"><div class="section-heading split-heading"><div><span class="eyebrow">NOTRE MÉTIER</span><h2>Des solutions pensées pour les espaces de soins.</h2></div><p>De l’entretien des sols et surfaces au prétraitement des instruments, nos gammes répondent aux besoins quotidiens des établissements de santé.</p></div><div class="product-grid">
  <a class="product-card" href="produits.html#sols-surfaces"><span class="card-index">01 / SOLS & SURFACES</span><div class="product-icon" aria-hidden="true">✦</div><h3>Détergents désinfectants sols et surfaces</h3><span class="card-link">Découvrir <span aria-hidden="true">↗</span></span></a>
  <a class="product-card" href="produits.html#surfaces-hautes"><span class="card-index">02 / SURFACES HAUTES</span><div class="product-icon" aria-hidden="true">✳</div><h3>Détergents désinfectants surfaces hautes</h3><span class="card-link">Découvrir <span aria-hidden="true">↗</span></span></a>
  <a class="product-card" href="produits.html#instruments"><span class="card-index">03 / INSTRUMENTS</span><div class="product-icon" aria-hidden="true">✣</div><h3>Nettoyants pré-désinfectants des instruments</h3><span class="card-link">Découvrir <span aria-hidden="true">↗</span></span></a>
</div></div></section>
<section class="section mission-band"><div class="container mission-grid"><span class="eyebrow">NOTRE MISSION</span><h2>Un environnement plus sûr pour les patients et le personnel soignant.</h2><p>Depuis 2021, Azuré Pharm concentre son activité sur la fabrication de produits d’hygiène destinés au secteur de la santé, avec une attention particulière portée à la qualité et aux exigences des lieux de soins.</p><a class="button button-outline-light" href="entreprise.html">En savoir plus <span aria-hidden="true">↗</span></a></div></section>
<section class="section"><div class="container location-teaser"><div><span class="eyebrow">ANCRAGE LOCAL</span><h2>Produire en Algérie,<br>au plus près des besoins.</h2><p>Unité de production à Ouled Moussa. Siège social à Dely Brahim, Alger.</p><a class="text-link" href="entreprise.html#implantations">Découvrir notre entreprise <span aria-hidden="true">→</span></a></div><div class="location-photo"><img src="assets/production-illustration.png" alt="Vue illustrative d’une ligne de production de produits d’hygiène"><span>Visuel d’illustration</span></div></div></section>
<section class="contact-strip"><div class="container contact-strip-inner"><div><span class="eyebrow">UN BESOIN, UNE QUESTION ?</span><h2>Échangeons sur vos besoins.</h2></div><a class="button button-white" href="contact.html">Nous contacter <span aria-hidden="true">↗</span></a></div></section>
'''),
"produits.html": ("Nos produits", "Découvrez les trois familles de détergents désinfectants Azuré Pharm pour les espaces de soins et les instruments.", '''
<section class="page-hero"><div class="container"><span class="eyebrow">NOS PRODUITS</span><h1>Des solutions pour chaque geste d’hygiène.</h1><p>Trois familles de produits dédiées aux besoins des hôpitaux, cliniques et collectivités.</p></div></section>
<section class="section"><div class="container product-list">
<article class="product-row" id="sols-surfaces"><div class="product-row-number">01</div><div><span class="eyebrow">SOLS & SURFACES</span><h2>Détergents désinfectants sols et surfaces</h2><p>Une gamme destinée à l’entretien des sols et des surfaces dans les environnements de soins et les espaces collectifs.</p><a class="text-link" href="contact.html?produit=Sols%20et%20surfaces">Demander des informations <span aria-hidden="true">→</span></a></div><div class="product-row-art" aria-hidden="true"><span>01</span><i>✦</i></div></article>
<article class="product-row" id="surfaces-hautes"><div class="product-row-number">02</div><div><span class="eyebrow">SURFACES HAUTES</span><h2>Détergents désinfectants surfaces hautes</h2><p>Des solutions consacrées à l’entretien des surfaces hautes et des zones de contact dans les établissements de santé.</p><a class="text-link" href="contact.html?produit=Surfaces%20hautes">Demander des informations <span aria-hidden="true">→</span></a></div><div class="product-row-art" aria-hidden="true"><span>02</span><i>✳</i></div></article>
<article class="product-row" id="instruments"><div class="product-row-number">03</div><div><span class="eyebrow">INSTRUMENTS</span><h2>Nettoyants pré-désinfectants des instruments</h2><p>Une famille de produits destinée à l’étape de pré-désinfection des instruments utilisés par les professionnels de santé.</p><a class="text-link" href="contact.html?produit=Instruments">Demander des informations <span aria-hidden="true">→</span></a></div><div class="product-row-art" aria-hidden="true"><span>03</span><i>✣</i></div></article>
</div></section><section class="contact-strip"><div class="container contact-strip-inner"><div><span class="eyebrow">INFORMATIONS PRODUITS</span><h2>Vous cherchez une solution adaptée ?</h2></div><a class="button button-white" href="contact.html">Contacter Azuré Pharm <span aria-hidden="true">↗</span></a></div></section>
'''),
"entreprise.html": ("Qui sommes-nous", "Azuré Pharm, entreprise algérienne spécialisée depuis 2021 dans la fabrication de produits d’hygiène pour le secteur de la santé.", '''
<section class="page-hero"><div class="container"><span class="eyebrow">QUI SOMMES-NOUS ?</span><h1>Une entreprise engagée pour l’hygiène des soins.</h1><p>Azuré Pharm accompagne les acteurs de santé avec des produits conçus pour les exigences de leurs environnements.</p></div></section>
<section class="section"><div class="container story-grid"><div><span class="eyebrow">DEPUIS 2021</span><h2>Votre partenaire de confiance.</h2></div><div><p>Azuré Pharm est une entreprise spécialisée dans la fabrication de détergents désinfectants et de dispositifs destinés au secteur de la santé. Sa mission est de contribuer à un milieu propre et sécuritaire pour les patients comme pour le personnel soignant.</p><p>Les produits destinés aux établissements de soins s’inscrivent dans un cadre d’exigences strictes en matière d’hygiène et de qualité. Cette attention guide notre activité au quotidien.</p></div></div></section>
<section class="section pale-section" id="implantations"><div class="container"><div class="section-heading"><span class="eyebrow">NOS IMPLANTATIONS</span><h2>Une présence au cœur de l’Algérie.</h2></div><div class="implant-grid"><div class="implant-image"><img src="assets/production-illustration.png" alt="Maquette illustrative d’une unité de production de produits d’hygiène"><span>Maquette illustrative — unité de production</span></div><div class="implant-info"><div><span class="location-number">01</span><h3>Unité de production</h3><p>Ouled Moussa, Algérie</p></div><div><span class="location-number">02</span><h3>Siège social</h3><p>Dely Brahim, Alger, Algérie</p></div></div></div></div></section>
<section class="section"><div class="container"><div class="section-heading"><span class="eyebrow">DOMAINES D’ACTIVITÉ</span><h2>Au service des professionnels.</h2></div><div class="sector-grid"><div><span>01</span><h3>Hôpitaux</h3></div><div><span>02</span><h3>Cliniques</h3></div><div><span>03</span><h3>Collectivités</h3></div></div><div class="quality-note"><strong>Qualité & normes</strong><p>Références de certification ISO à préciser. Contactez notre équipe pour obtenir les informations et documents à jour.</p></div></div></section>
'''),
"recherche.html": ("Recherche & développement", "Les projets de recherche et développement d’Azuré Pharm accompagnent l’évolution des besoins en hygiène du secteur de la santé.", '''
<section class="page-hero"><div class="container"><span class="eyebrow">RECHERCHE & DÉVELOPPEMENT</span><h1>Faire évoluer les solutions d’hygiène.</h1><p>Azuré Pharm mène des projets de recherche continus pour accompagner les besoins du secteur de la santé.</p></div></section>
<section class="section"><div class="container rd-grid"><div class="rd-graphic" aria-hidden="true"><div class="rd-ring rd-ring-one"></div><div class="rd-ring rd-ring-two"></div><div class="rd-ring rd-ring-three"></div><span>R<span>&</span>D</span></div><div><span class="eyebrow">NOTRE DÉMARCHE</span><h2>Observer, améliorer, avancer.</h2><p>La recherche et le développement occupent une place dans les projets d’Azuré Pharm. Notre ambition est de faire progresser nos solutions en restant attentifs aux usages et aux exigences des professionnels de santé.</p><p>Pour connaître nos produits et nos projets en cours, échangez directement avec notre équipe.</p><a class="button button-primary" href="contact.html">Prendre contact <span aria-hidden="true">↗</span></a></div></div></section>
'''),
"contact.html": ("Contact", "Contactez Azuré Pharm à Dely Brahim, Alger, pour toute question sur ses détergents désinfectants.", '''
<section class="page-hero"><div class="container"><span class="eyebrow">CONTACT</span><h1>Parlons de vos besoins.</h1><p>Une question sur nos produits ou notre activité ? Notre équipe est à votre écoute.</p></div></section>
<section class="section contact-section"><div class="container contact-grid"><div class="contact-details"><span class="eyebrow">NOS COORDONNÉES</span><h2>Restons en contact.</h2><div class="detail-item"><span>E-mail</span><a href="mailto:eurlazurepharm@gmail.com">eurlazurepharm@gmail.com</a></div><div class="detail-item"><span>Téléphone</span><a href="tel:+213660456457">0660 456 457</a><a href="tel:+213553779211">0553 779 211</a></div><div class="detail-item"><span>Siège social</span><strong>Dely Brahim, Alger, Algérie</strong></div><div class="social-row"><a href="https://www.facebook.com/share/1R3SXmtx3s/" target="_blank" rel="noopener noreferrer">Facebook ↗</a><a href="https://www.instagram.com/azurepharm2021?utm_source=qr&amp;stkn=MXd4ZWpmeDU4dXU1Yw==" target="_blank" rel="noopener noreferrer">Instagram ↗</a></div></div><div class="form-card"><h2>Écrivez-nous</h2><p>Complétez le formulaire pour préparer votre message dans votre messagerie.</p><form id="contact-form"><div class="form-two"><label>Nom et prénom <span>*</span><input name="nom" autocomplete="name" required></label><label>Adresse e-mail <span>*</span><input name="email" type="email" autocomplete="email" required></label></div><label>Téléphone<input name="telephone" type="tel" autocomplete="tel"></label><label>Sujet <span>*</span><input name="sujet" required></label><label>Votre message <span>*</span><textarea name="message" rows="6" required></textarea></label><button class="button button-primary" type="submit">Préparer l’e-mail <span aria-hidden="true">↗</span></button><p class="form-note" id="form-note" role="status">Votre application de messagerie s’ouvrira pour l’envoi.</p></form></div></div></section>
'''),
}

for filename, (title, description, body) in pages.items():
    (ROOT / filename).write_text(shell(title, description, filename, body), encoding="utf-8")
