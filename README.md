# Xingyu Chen — academic website

Public website: https://xingyuaudio.github.io/

An English academic profile covering spatial audio, personalized HRTFs, sound field reconstruction, and efficient audio generation.

## Updating content

- `_pages/about.html`: biography and research directions.
- `_data/publications.yml`: canonical publication records, resources, summaries, and homepage selection (`featured: true`). Keep journal papers, conference papers, preprints, abstracts, and theses labeled correctly.
- `_data/profile.yml`: professional links.
- `_data/background.yml`: education and research / industry experience, listed separately in the web CV and PDF CV.
- `_includes/reviewer-list.html`: journal review service.
- `_pages/cv.html` and `files/Xingyu_Chen_CV.pdf`: web and downloadable CV.
- `assets/css/academic.css`: responsive design; `assets/js/publications.js`: progressive publication filters.

The baseline records were checked directly against Google Scholar on 16 November 2026. Citation counts are intentionally not copied, since they change over time. No unpublished projects or unverified contact addresses are listed.

GitHub Pages builds the existing Jekyll site from `master`. With Ruby/Bundler installed, run `bundle install` and `bundle exec jekyll serve` to preview locally. `scripts/refresh_site.py` regenerates the initial November 2026 snapshot and overwrites the associated source files; use it only when intentionally rebuilding that snapshot. `scripts/build_cv.py` regenerates the PDF from the current publication data (requires PyYAML and ReportLab).

The previous `/markdown/`, `/md/`, `/about/`, and `/resume` URLs redirect to their current pages. Existing paper PDF paths and the portrait are preserved.

Based on AcademicPages / Minimal Mistakes. See `LICENSE` for the original MIT license.
