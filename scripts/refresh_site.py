"""Build the profile content from the verified Google Scholar snapshot (2026-11-16).

Run from the repository root: python scripts/refresh_site.py
Only Python's standard library and PyYAML are needed for the website sources.
"""
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHOLAR = 'https://scholar.google.com.au/citations?user=u7YilpkAAAAJ&hl=en'
PROFILE = 'https://profiles.uts.edu.au/student_Xingyu.Chen-8'

def paper(id, title, authors, venue, year, kind, topic, citation, summary='', featured=False, **links):
    return dict(id=id, title=title, authors=authors, venue=venue, year=year, kind=kind,
                topic=topic, scholar=SCHOLAR+'&view_op=view_citation&citation_for_view=u7YilpkAAAAJ:'+citation,
                summary=summary, featured=featured, links=links)

papers = [
    paper('fd-conformer', 'Exploring frequency-domain feature modeling for head-related transfer functions magnitude upsampling',
          'Xingyu Chen, Hanwen Bi, Fei Ma, Sipei Zhao, Eva Cheng, Ian S. Burnett',
          'The Journal of the Acoustical Society of America, 160(5), 3663–3674', 2026, 'Journal', 'HRTF', '4TOpqqG69KYC',
          'Explicitly modeling dependencies across frequency improves HRTF reconstruction from sparse spatial measurements.', True,
          Paper='https://doi.org/10.1121/10.0047189', Preprint='https://arxiv.org/abs/2602.11670', Code='https://github.com/xingyuaudio/FD-Conformer'),
    paper('driftaudio', 'DriftAudio: Marginal Drifting for Distributional Post-Training of One-Step Text-to-Audio Generators',
          'Xingyu Chen, Fei Ma, Sipei Zhao', 'arXiv:2609.27598', 2026, 'Preprint', 'Audio generation', '_kc_bZDykSQC',
          'Distributional post-training improves pretrained text-to-audio generators while preserving one-step inference.', True,
          Paper='https://arxiv.org/abs/2609.27598', Code='https://github.com/xingyuaudio/DriftAudio', Demo='https://xingyuaudio.github.io/driftaudio-demo/'),
    paper('geoatt', 'HRTF Upsampling Across Varying Measurement Configurations with Geometry-Aware Query-Conditioned Aggregation',
          'Xingyu Chen, Hanwen Bi, Sipei Zhao, Fei Ma, Eva Cheng, Ian S. Burnett', 'arXiv:2609.25995', 2026, 'Preprint', 'HRTF', 'YOwf2qJgpHMC',
          'GeoAtt uses geometry-aware, query-conditioned aggregation to support varying measurement counts and layouts with a single model.', True,
          Paper='https://arxiv.org/abs/2609.25995', Code='https://github.com/xingyuaudio/GeoAtt-HRTF'),
    paper('region-to-region', 'Permutation-Invariant Physics-Informed Neural Network for Region-to-Region Sound Field Reconstruction',
          'Xingyu Chen, Sipei Zhao, Fei Ma, Eva Cheng, Ian S. Burnett', '31st International Congress on Sound and Vibration (ICSV31), 1–8',
          2025, 'Conference', 'Sound field', 'kNdYIx-mwKoC',
          'A permutation-invariant model combines acoustic reciprocity and the Helmholtz equation for reconstruction across source and receiver regions.', True,
          Paper='https://arxiv.org/abs/2601.19491'),
    paper('ramdc', 'RAMDC: Room-Aware Multi-Device Clustering for Large Scale Teleconferencing',
          'Yile Angela Zhang, Wei-Ting Lai, Amy Bastine, Xingyu Chen, Lachlan I. Birnie, Thushara D. Abhayapala, Prasanga N. Samarasinghe',
          'APSIPA Annual Summit and Conference (APSIPA ASC), 447–452', 2025, 'Conference', 'Sound field', '3fE2CSJIrl8C',
          'Acoustic responses identify devices sharing a room to help reduce cross-device feedback in teleconferencing.',
          Paper='https://ieeexplore.ieee.org/abstract/document/11249230/', PDF='https://www.apsipa.org/proceedings/2025/papers/APSIPA2025_P458.pdf'),
    paper('thesis', 'Learning-integrated Methods for Spatial Audio Capture and Reproduction', 'Xingyu Chen',
          'MPhil thesis, Australian National University', 2025, 'Thesis', 'Sound field', 'MXK_kJrjxJIC',
          'Deep learning for sound field estimation, HRTF interpolation, and speech enhancement on drones.'),
    paper('drone', 'Monaural speech enhancement on drone via Adapter based transfer learning',
          'Xingyu Chen, Hanwen Bi, Wei-Ting Lai, Fei Ma', '18th International Workshop on Acoustic Signal Enhancement (IWAENC), 85–89',
          2024, 'Conference', 'Speech', '0EnyYjriUFMC',
          'Adapter-based transfer learning adapts a pretrained speech enhancement model to drone noise.',
          Paper='https://arxiv.org/abs/2405.10022'),
    paper('srp', 'Source localization by multidimensional steered response power mapping with sparse Bayesian learning',
          'Wei-Ting Lai, Lachlan Birnie, Xingyu Chen, Amy Bastine, Thushara D. Abhayapala, Prasanga N. Samarasinghe',
          '18th International Workshop on Acoustic Signal Enhancement (IWAENC), 31–35',
          2024, 'Conference', 'Sound field', '5nxA0vEk-isC'),
    paper('sphere', 'Sound field estimation around a rigid sphere with physics-informed neural network',
          'Xingyu Chen, Fei Ma, Amy Bastine, Prasanga Samarasinghe, Hanchi Sun', 'APSIPA Annual Summit and Conference (APSIPA ASC)',
          2023, 'Conference', 'Sound field', 'ufrVoPGSRksC',
          'Physical constraints guide sound field estimation around a rigid sphere from limited spatial measurements.',
          PDF='/files/Sound_Field_Estimation_around_a_Rigid_Sphere_with_Physics_informed_Neural_Network.pdf', Code='https://github.com/xingyuaudio/pinn_estimation'),
    paper('spherical-cnn', 'Head-related transfer function interpolation with a spherical CNN',
          'Xingyu Chen, Fei Ma, Yile Zhang, Amy Bastine, Prasanga N. Samarasinghe', 'arXiv:2309.08290',
          2023, 'Preprint', 'HRTF', 'YsMSGLbcyi4C',
          'Spherical convolution captures the spatial structure of HRTFs through spherical harmonic representations.',
          Paper='https://arxiv.org/abs/2309.08290', Code='https://github.com/xingyuaudio/HRTF-SCNN'),
    paper('pinn-hrtf', 'Spatial Upsampling of Head-Related Transfer Functions Using a Physics-Informed Neural Network',
          'Fei Ma, Thushara D. Abhayapala, Prasanga N. Samarasinghe, Xingyu Chen', 'arXiv:2307.14650',
          2023, 'Preprint', 'HRTF', 'WF5omc3nYNoC',
          'The Helmholtz equation provides a physical constraint for reconstructing HRTFs at unmeasured directions.',
          Paper='https://arxiv.org/abs/2307.14650', Code='https://github.com/feima1024/PINN-for-HRTF-upsampling'),
    paper('asa-abstract', 'Head-related transfer functions upsampling with physics-informed spherical convolutional neural network',
          'Xingyu Chen, Fei Ma, Prasanga N. Samarasinghe',
          'The Journal of the Acoustical Society of America, 154(4_supplement), A183',
          2023, 'Meeting abstract', 'HRTF', 'eQOLeE2rZwMC',
          Paper='https://doi.org/10.1121/10.0023204'),
    paper('invariant-ekf', 'Closed-Form Error Propagation on SE_n(3) Group for Invariant EKF With Applications to VINS',
          'Xinghan Li, Haoyuan Jiang, Xingyu Chen, Hui Kong, Junfeng Wu',
          'IEEE Robotics and Automation Letters, 7(4), 10705–10712', 2022, 'Journal', 'Other', '9yKSN-GCB0IC',
          PDF='/files/Closed-Form_Error_Propagation_on_SE_n3_Group_for_Invariant_EKF_With_Applications_to_VINS.pdf'),
]
# Keep authors exactly as recorded by Scholar where a full name was not verified.
papers[-1]['authors'] = 'X. Li, H. Jiang, Xingyu Chen, H. Kong, J. Wu'
papers[8]['authors'] = 'Xingyu Chen, Fei Ma, Amy Bastine, Prasanga Samarasinghe, H. Sun'

def write(path, content):
    target = ROOT/path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.strip()+'\n')

write('_data/publications.yml', yaml.safe_dump(papers, sort_keys=False, allow_unicode=True, width=120))
write('_data/profile.yml', yaml.safe_dump(dict(name='Xingyu Chen', role='PhD Candidate', institution='University of Technology Sydney',
     scholar=SCHOLAR, institutional_profile=PROFILE, github='https://github.com/xingyuaudio', orcid='https://orcid.org/0000-0001-5711-7996',
     linkedin='https://www.linkedin.com/in/xingyu-chen-2b8618259/', research_intro='I study how machines can reconstruct and generate sound in ways that are grounded in the physical world and meaningful to human listeners.',
     research_statement='Sound is shaped by sources, environments, and listeners. A recording captures only a partial observation of their interaction. My research asks how to represent this underlying structure so that we can infer beyond what is observed and generate sound with meaningful control. I am interested in what should be constrained by acoustics, what should be learned from data, and what must be preserved for human perception.', updated='November 2026'), sort_keys=False))
write('_pages/about.html', '''
---
layout: academic
title: About
permalink: /
nav: about
redirect_from: [/about/, /about.html]
---
<section class="hero" aria-labelledby="intro-title">
  <div class="hero-copy">
    <p class="eyebrow">SPATIAL AUDIO · MACHINE LEARNING</p>
    <h1 id="intro-title">Xingyu Chen</h1>
    <p class="role">PhD Candidate <span>/</span> University of Technology Sydney</p>
    <p class="intro">{{ site.data.profile.research_intro | escape }}</p>
    <p>{{ site.data.profile.research_statement | escape }}</p>
    {% include contact.html %}
    <div class="profile-links"><a class="button" href="{{ site.data.profile.scholar }}">Google Scholar <span aria-hidden="true">↗</span></a><a href="{{ site.data.profile.github }}">GitHub ↗</a><a href="{{ site.data.profile.linkedin }}">LinkedIn ↗</a><a href="{{ site.data.profile.institutional_profile }}">UTS profile ↗</a><a href="/cv/">CV →</a></div>
  </div>
  <aside class="portrait-card"><img src="/images/profile.jpg" alt="Xingyu Chen profile image" width="300" height="300"><div><span class="small-label">RESEARCH FOCUS</span><p>Learning to capture,<br>reconstruct, and generate sound.</p></div></aside>
</section>
<section class="section" aria-labelledby="research-title">
  <div class="section-heading"><h2 id="research-title">Research directions</h2><span class="section-note">Acoustics meets learning</span></div>
  <div class="research-grid">
    <a class="research-card" href="/publications/?topic=HRTF"><span class="card-index">01 / PERSONALIZATION</span><h3>Personalized spatial audio</h3><p>HRTF reconstruction from sparse measurements, with frequency-domain and geometry-aware modeling.</p><span class="card-arrow" aria-hidden="true">↗</span></a>
    <a class="research-card" href="/publications/?topic=Sound%20field"><span class="card-index">02 / RECONSTRUCTION</span><h3>Sound field learning</h3><p>Physics-informed models that incorporate wave propagation, spatial structure, and acoustic reciprocity.</p><span class="card-arrow" aria-hidden="true">↗</span></a>
    <a class="research-card" href="/publications/?topic=Audio%20generation"><span class="card-index">03 / GENERATION</span><h3>Efficient audio generation</h3><p>One-step text-to-audio synthesis and distributional post-training of pretrained audio generators.</p><span class="card-arrow" aria-hidden="true">↗</span></a>
  </div>
</section>
<section class="section" aria-labelledby="selected-title">
  <div class="section-heading"><h2 id="selected-title">Selected work</h2><a class="text-link" href="/publications/">All publications →</a></div>
  {% for paper in site.data.publications %}{% if paper.featured %}{% include publication-card.html %}{% endif %}{% endfor %}
</section>
<section class="section service-section" id="service" aria-labelledby="service-title">
  <div><p class="eyebrow">ACADEMIC SERVICE</p><h2 id="service-title">Journal reviewer</h2></div>
  {% include reviewer-list.html %}
</section>
''')
write('_pages/publications.html', '''
---
layout: academic
title: Publications
permalink: /publications/
nav: publications
redirect_from: [/markdown/, /markdown.html, /md/]
---
<header class="page-heading"><p class="eyebrow">RESEARCH OUTPUT</p><h1>Publications</h1><p>Work on spatial audio, acoustic reconstruction, and audio generation.<br>Full citation records are available on <a href="{{ site.data.profile.scholar }}">Google Scholar ↗</a>.</p></header>
<div class="publication-tools" hidden>
  <div class="filter-buttons" role="group" aria-label="Filter publications by topic">
    <button type="button" data-topic="All" aria-pressed="true">All</button><button type="button" data-topic="HRTF" aria-pressed="false">HRTF</button><button type="button" data-topic="Sound field" aria-pressed="false">Sound field</button><button type="button" data-topic="Audio generation" aria-pressed="false">Audio generation</button><button type="button" data-topic="Speech" aria-pressed="false">Speech</button><button type="button" data-topic="Other" aria-pressed="false">Other</button>
  </div>
  <label class="search-label">Search publications<input type="search" id="paper-search" placeholder="Title, author, or venue…" autocomplete="off"></label>
</div>
<p class="results-count" id="results-count" aria-live="polite">13 records · journal and conference papers, preprints, a meeting abstract, and a thesis</p>
<div id="publication-list">
{% assign years = site.data.publications | group_by: 'year' %}
{% for year in years %}<section class="year-group" aria-labelledby="year-{{ year.name }}"><h2 class="year-heading" id="year-{{ year.name }}">{{ year.name }}</h2>{% for paper in year.items %}{% include publication-card.html %}{% endfor %}</section>{% endfor %}
</div>
<p class="empty-state" id="empty-state" hidden>No matching publications. Try another topic or search term.</p>
<p class="source-note">Publication records checked against Google Scholar in November 2026. Preprints, meeting abstracts, and the thesis are labeled separately.</p>
<script src="/assets/js/publications.js" defer></script>
''')
write('_pages/cv.html', '''
---
layout: academic
title: CV
permalink: /cv/
nav: cv
redirect_from: [/resume, /resume/]
---
<header class="page-heading"><p class="eyebrow">CURRICULUM VITAE</p><h1>Xingyu Chen</h1><p>PhD Candidate, University of Technology Sydney</p><a class="button" href="/files/Xingyu_Chen_CV.pdf">Download PDF CV ↓</a></header>
<section class="section"><h2>Research profile</h2><p>{{ site.data.cv.summary | escape }}</p></section>
<section class="section"><h2>Education</h2>{% for entry in site.data.background.education %}{% include background-row.html %}{% endfor %}</section>
<section class="section"><h2>Research experience</h2>{% for project in site.data.cv.research %}<div class="cv-row"><div class="cv-date">{{ project.dates | escape }}</div><div><h3>{{ project.title | escape }}</h3><ul class="cv-bullets">{% for bullet in project.bullets %}<li>{{ bullet | escape }}</li>{% endfor %}</ul><div class="paper-links">{% for link in project.links %}<a href="{{ link[1] }}">{{ link[0] }} ↗</a>{% endfor %}</div></div></div>{% endfor %}</section>
<section class="section"><h2>Professional experience</h2>{% for entry in site.data.background.experience %}{% include background-row.html %}{% endfor %}</section>
<section class="section"><h2>Technical skills</h2>{% for skill in site.data.cv.skills %}<p class="cv-skill"><strong>{{ skill.label | escape }}:</strong> {{ skill.value | escape }}</p>{% endfor %}</section>
<section class="section cv-publications-section" id="cv-publications"><h2>Publications</h2>{% for category in site.data.cv.publication_groups %}<div class="cv-publication-group"><h3>{{ category.title | escape }}</h3>{% for paper in site.data.publications %}{% if category.kinds contains paper.kind %}{% include cv-publication.html %}{% endif %}{% endfor %}</div>{% endfor %}</section>
<section class="section"><h2>Academic service</h2><h3>Journal reviewer</h3>{% include reviewer-list.html %}</section>
<section class="section"><h2>Professional links</h2><div class="profile-links"><a href="{{ site.data.profile.scholar }}">Google Scholar ↗</a><a href="{{ site.data.profile.linkedin }}">LinkedIn ↗</a><a href="{{ site.data.profile.institutional_profile }}">UTS profile ↗</a><a href="{{ site.data.profile.github }}">GitHub ↗</a><a href="{{ site.data.profile.orcid }}">ORCID ↗</a></div></section>
''')
write('_includes/reviewer-list.html', '''
<ul class="reviewer-list"><li>The Journal of the Acoustical Society of America <span>JASA</span></li><li>IEEE Open Journal of Signal Processing <span>OJSP</span></li><li>IEEE Signal Processing Letters <span>SPL</span></li></ul>
''')
write('_includes/publication-card.html', '''
<article class="publication" id="{{ paper.id }}" data-topic="{{ paper.topic | escape }}">
  <div class="publication-meta"><span class="pub-kind{% if paper.kind == 'Preprint' %} preprint{% endif %}">{{ paper.kind }}</span><span>{{ paper.year }}</span><span class="pub-topic">{{ paper.topic }}</span></div>
  <h3><a href="{% if paper.links.Paper %}{{ paper.links.Paper }}{% else %}{{ paper.scholar }}{% endif %}">{{ paper.title | escape }}</a></h3>
  <p class="authors">{{ paper.authors | escape | replace: 'Xingyu Chen', '<strong>Xingyu Chen</strong>' }}</p>
  <p class="venue">{{ paper.venue | escape }}</p>
  {% if paper.summary != '' %}<p class="paper-summary">{{ paper.summary | escape }}</p>{% endif %}
  <div class="paper-links" aria-label="Publication resources">{% for link in paper.links %}<a href="{{ link[1] }}">{{ link[0] }} <span aria-hidden="true">↗</span></a>{% endfor %}<a href="{{ paper.scholar }}">Scholar <span aria-hidden="true">↗</span></a></div>
</article>
''')
write('_layouts/academic.html', '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% if page.nav != 'about' %}{{ page.title | escape }} | {% endif %}Xingyu Chen · Spatial Audio &amp; Machine Learning</title>
  <meta name="description" content="Xingyu Chen is a PhD candidate at the University of Technology Sydney, researching spatial audio, personalized HRTFs, sound field reconstruction, and efficient audio generation.">
  <link rel="canonical" href="{{ site.url }}{{ page.url }}"><meta property="og:type" content="website"><meta property="og:title" content="{{ page.title | escape }} | Xingyu Chen"><meta property="og:description" content="Spatial audio, personalized HRTFs, sound field reconstruction, and efficient audio generation."><meta property="og:url" content="{{ site.url }}{{ page.url }}"><meta property="og:image" content="{{ site.url }}/images/profile.jpg"><meta name="theme-color" content="#f8f9f6">
  <link rel="icon" href="/images/xc.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/css/academic.css?v={{ site.time | date: '%Y%m%d%H%M%S' }}">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"Xingyu Chen","url":"https://xingyuaudio.github.io/","jobTitle":"PhD Candidate","affiliation":{"@type":"Organization","name":"University of Technology Sydney"},"sameAs":["https://scholar.google.com.au/citations?user=u7YilpkAAAAJ&hl=en","https://github.com/xingyuaudio","https://orcid.org/0000-0001-5711-7996","https://www.linkedin.com/in/xingyu-chen-2b8618259/","https://profiles.uts.edu.au/student_Xingyu.Chen-8"]}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="header-inner"><a class="wordmark" href="/" aria-label="Xingyu Chen, home"><span class="monogram" aria-hidden="true">xc.</span><span>Xingyu Chen</span></a><nav aria-label="Main navigation"><a href="/"{% if page.nav == 'about' %} aria-current="page"{% endif %}>About</a><a href="/publications/"{% if page.nav == 'publications' %} aria-current="page"{% endif %}>Publications</a><a href="/cv/"{% if page.nav == 'cv' %} aria-current="page"{% endif %}>CV</a><a href="/#service">Service</a></nav></div></header>
<main id="main" class="container">{{ content }}</main>
<footer class="site-footer"><div class="footer-inner"><div><strong>Xingyu Chen</strong><p>Spatial audio &amp; machine learning<br>University of Technology Sydney</p></div><div><a href="{{ site.data.profile.scholar }}">Google Scholar ↗</a><a href="{{ site.data.profile.github }}">GitHub ↗</a><a href="{{ site.data.profile.linkedin }}">LinkedIn ↗</a><a href="{{ site.data.profile.institutional_profile }}">UTS profile ↗</a></div><p class="footer-note">Updated November 2026<br>© 2026 Xingyu Chen</p></div></footer>
</body>
</html>
''')
write('_pages/sitemap.md', '''
---
layout: academic
title: Sitemap
permalink: /sitemap/
---
<header class="page-heading"><h1>Sitemap</h1></header><ul><li><a href="/">About</a></li><li><a href="/publications/">Publications</a></li><li><a href="/cv/">CV</a></li><li><a href="/#service">Academic service</a></li></ul>
''')
write('_pages/404.md', '''
---
layout: academic
title: Page not found
permalink: /404.html
sitemap: false
---
<header class="page-heading"><p class="eyebrow">404</p><h1>Page not found</h1><p>This page may have moved. Find the latest research on the <a href="/">homepage</a> or browse <a href="/publications/">publications</a>.</p></header>
''')
write('_data/navigation.yml', 'main:\n  - title: About\n    url: /\n  - title: Publications\n    url: /publications/\n  - title: CV\n    url: /cv/\n  - title: Service\n    url: /#service')

# Remove replaced or unpersonalized template pages from the published site.
for name in ['about.md', 'markdown.md', 'publications.md', 'cv.md', 'archive-layout-with-content.md',
             'category-archive.html', 'collection-archive.html', 'non-menu-page.md', 'page-archive.html',
             'portfolio.html', 'tag-archive.html', 'talkmap.html', 'talks.html', 'terms.md', 'year-archive.html']:
    (ROOT/'_pages'/name).unlink(missing_ok=True)
(ROOT/'_publications/paper1.md').unlink(missing_ok=True)

# Keep the established Jekyll build and correct its public metadata.
config = yaml.safe_load((ROOT/'_config.yml').read_text())
config.update(title='Xingyu Chen', description='Spatial audio, personalized HRTFs, sound field reconstruction, and efficient audio generation.',
              repository='xingyuaudio/xingyuaudio.github.io', timezone='Australia/Sydney', analytics={'provider':False})
config['author'].update(bio='PhD Candidate · Spatial Audio & Machine Learning', employer='University of Technology Sydney')
config['exclude'] = list(dict.fromkeys(config.get('exclude', [])+['scripts','tmp','talkmap','talkmap.py','talkmap.ipynb','markdown_generator','README.md']))
write('_config.yml', yaml.safe_dump(config, sort_keys=False, allow_unicode=True))
write('README.md', '''
# Xingyu Chen — academic website

Public website: https://xingyuaudio.github.io/

An English academic profile covering spatial audio, personalized HRTFs, sound field reconstruction, and efficient audio generation.

## Updating content

- `_pages/about.html`: biography and research directions.
- `_data/publications.yml`: canonical publication records, resources, summaries, and homepage selection (`featured: true`). Keep journal papers, conference papers, preprints, abstracts, and theses labeled correctly.
- `_data/profile.yml`: professional links.
- `_data/cv.yml`: general CV summary, three research areas, technical skills, and publication categories.
- `_data/background.yml`: education and research / industry experience, listed separately in the web CV and PDF CV.
- `_includes/reviewer-list.html`: journal review service.
- `_includes/contact.html`: collaboration invitation and an email contact link to the official UTS profile. No email address is displayed, encoded, or embedded in the contact section.
- `_pages/cv.html` and `files/Xingyu_Chen_CV.pdf`: web and downloadable CV.
- `assets/css/academic.css`: responsive design; `assets/js/publications.js`: progressive publication filters.

The baseline records were checked directly against Google Scholar on 16 November 2026. Citation counts are intentionally not copied, since they change over time. No unpublished projects or unverified contact addresses are listed.

GitHub Pages builds the existing Jekyll site from `master`. With Ruby/Bundler installed, run `bundle install` and `bundle exec jekyll serve` to preview locally. `scripts/refresh_site.py` regenerates the initial November 2026 snapshot and overwrites the associated source files; use it only when intentionally rebuilding that snapshot. `scripts/build_cv.py` regenerates the PDF from the current publication data (requires PyYAML and ReportLab).

The previous `/markdown/`, `/md/`, `/about/`, and `/resume` URLs redirect to their current pages. Existing paper PDF paths and the portrait are preserved.

Based on AcademicPages / Minimal Mistakes. See `LICENSE` for the original MIT license.
''')
print(f'Prepared {len(papers)} verified publication records and refreshed website content.')
