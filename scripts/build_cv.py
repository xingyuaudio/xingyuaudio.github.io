"""Build the two-page general CV from the website's shared content.

Page 1: profile, education, research, professional experience, technical skills.
Page 2: complete grouped publications, followed by academic service.
Requires PyYAML, ReportLab, and DejaVu fonts (CV_FONT_DIR may override the path).
"""
import os
from pathlib import Path
from xml.sax.saxutils import escape
import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
profile = yaml.safe_load((ROOT / '_data/profile.yml').read_text())
background = yaml.safe_load((ROOT / '_data/background.yml').read_text())
cv = yaml.safe_load((ROOT / '_data/cv.yml').read_text())
papers = yaml.safe_load((ROOT / '_data/publications.yml').read_text())
font_root = Path(os.environ.get('CV_FONT_DIR', '/usr/share/fonts/truetype/dejavu'))
for name, filename in [
    ('CVSans', 'DejaVuSans.ttf'), ('CVSans-Bold', 'DejaVuSans-Bold.ttf'),
    ('CVSans-Italic', 'DejaVuSans-Oblique.ttf'), ('CVSerif', 'DejaVuSerif.ttf'),
]:
    pdfmetrics.registerFont(TTFont(name, str(font_root / filename)))
pdfmetrics.registerFontFamily('CVSans', normal='CVSans', bold='CVSans-Bold',
                             italic='CVSans-Italic', boldItalic='CVSans-Bold')
INK, GREEN, MUTED, LINE = '#1d3030', '#21675c', '#526564', '#dce3dc'
WIDTH = A4[0] - 80
styles = {}
for name, size, leading, font, color, after in [
    ('Name', 24, 28, 'CVSerif', INK, 3),
    ('Subtitle', 9, 12, 'CVSans', GREEN, 3),
    ('Links', 7.5, 10, 'CVSans', MUTED, 6),
    ('Section', 10.4, 14, 'CVSans-Bold', GREEN, 4),
    ('Body', 8.35, 11, 'CVSans', INK, 2),
    ('Entry', 8.6, 11.2, 'CVSans-Bold', INK, 0),
    ('Dates', 7.6, 11.2, 'CVSans', MUTED, 0),
    ('Note', 7.3, 9.2, 'CVSans', MUTED, 2),
    ('Group', 9.1, 12, 'CVSans-Bold', GREEN, 4),
    ('PaperTitle', 8.25, 10.4, 'CVSans-Bold', INK, 2),
    ('PaperAuthors', 7.5, 9.1, 'CVSans', MUTED, 1),
    ('PaperVenue', 7.6, 9.2, 'CVSans', MUTED, 4),
]:
    styles[name] = ParagraphStyle(name, fontName=font, fontSize=size, leading=leading,
                                 textColor=colors.HexColor(color), spaceAfter=after)
styles['Dates'].alignment = TA_RIGHT
styles['Bullet'] = ParagraphStyle('Bullet', parent=styles['Body'], leftIndent=9,
                                 firstLineIndent=-7, spaceAfter=3)

def clean(text):
    return str(text).replace('\u2013', '-').replace('\u2014', '-').replace('\u2011', '-')

def esc(text):
    return escape(clean(text))

def p(text, style='Body'):
    return Paragraph(text, styles[style])

def link(url, label, color=GREEN):
    return '<link href="' + escape(url, {'"': '&quot;'}) + '" color="' + color + '">' + esc(label) + '</link>'

def heading(title, dates=''):
    table = Table([[p(esc(title), 'Entry'), p(esc(dates), 'Dates')]],
                  colWidths=[WIDTH - 130, 130], hAlign='LEFT')
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    return table

story = []
def section(title):
    story.extend([Spacer(1, 6), p(esc(title), 'Section')])

def bullet(text):
    return p('&#8226; ' + esc(text), 'Bullet')

story.extend([
    p('Xingyu Chen', 'Name'),
    p('PhD Candidate | University of Technology Sydney', 'Subtitle'),
    p(' / '.join([
        link('https://xingyuaudio.github.io/', 'Website'), link(profile['scholar'], 'Google Scholar'),
        link(profile['github'], 'GitHub'), link(profile['linkedin'], 'LinkedIn'),
        link(profile['institutional_profile'], 'UTS profile / contact'),
    ]), 'Links'),
    p(esc(cv['summary'])),
])

section('Education')
for entry in background['education']:
    story.append(KeepTogether([
        heading(entry['institution'], entry['dates']),
        p(esc(entry['qualification']) + ' - ' + esc(entry['description'])), Spacer(1, 2),
    ]))

section('Research experience')
for project in cv['research']:
    story.append(KeepTogether([
        heading(project['title'], project['dates']),
        *[bullet(text) for text in project['bullets']], Spacer(1, 2),
    ]))

section('Professional experience')
for entry in background['experience']:
    block = [heading(entry['institution'], entry['dates']), p('<i>' + esc(entry['qualification']) + '</i>')]
    if entry.get('description'):
        block.append(p(esc(entry['description'])))
    block.extend(bullet(text) for text in entry.get('bullets', []))
    if entry.get('note'):
        block.append(p(esc(entry['note']), 'Note'))
    block.append(Spacer(1, 2))
    story.append(KeepTogether(block))

section('Technical skills')
for skill in cv['skills']:
    story.append(p('<b>' + esc(skill['label']) + ':</b> ' + esc(skill['value'])))

story.extend([PageBreak(), p('Publications', 'Name')])
index = 0
for category in cv['publication_groups']:
    story.extend([Spacer(1, 4), p(esc(category['title']), 'Group')])
    for item in papers:
        if item['kind'] not in category['kinds']:
            continue
        index += 1
        target = item['links'].get('Paper', item['scholar'])
        title = esc(item['title']).replace('SE_n(3)', 'SE<sub>n</sub>(3)')
        title_link = '<link href="' + escape(target, {'"': '&quot;'}) + '" color="' + INK + '">' + title + '</link>'
        authors = esc(item['authors']).replace('Xingyu Chen', '<b>Xingyu Chen</b>')
        venue = '<i>' + esc(item['venue']) + '</i>, ' + str(item['year']) + '. [' + esc(item['kind']) + ']'
        story.append(KeepTogether([
            p(str(index) + '. ' + title_link, 'PaperTitle'),
            p(authors, 'PaperAuthors'), p(venue, 'PaperVenue'),
        ]))

section('Academic service')
story.append(p('<b>Journal reviewer:</b>'))
for journal in [
    'The Journal of the Acoustical Society of America (JASA)',
    'IEEE Open Journal of Signal Processing (OJSP)',
    'IEEE Signal Processing Letters (SPL)',
]:
    story.append(bullet(journal))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor(LINE))
    canvas.line(40, 30, A4[0] - 40, 30)
    canvas.setFont('CVSans', 7)
    canvas.setFillColor(colors.HexColor(MUTED))
    canvas.drawString(40, 19, 'Xingyu Chen | Updated ' + clean(cv['updated']))
    canvas.drawRightString(A4[0] - 40, 19, str(doc.page))
    canvas.restoreState()

SimpleDocTemplate(str(ROOT / 'files/Xingyu_Chen_CV.pdf'), pagesize=A4, leftMargin=40,
                  rightMargin=40, topMargin=30, bottomMargin=42,
                  title='Xingyu Chen - Curriculum Vitae', author='Xingyu Chen').build(
                      story, onFirstPage=footer, onLaterPages=footer)
print('Updated files/Xingyu_Chen_CV.pdf')
