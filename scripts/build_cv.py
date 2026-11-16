"""Regenerate the public PDF CV from the current verified publication data."""
from pathlib import Path
from xml.sax.saxutils import escape
import yaml
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

root = Path(__file__).resolve().parents[1]
papers = yaml.safe_load((root/'_data/publications.yml').read_text())
profile = yaml.safe_load((root/'_data/profile.yml').read_text())
styles = getSampleStyleSheet()
font_root=Path('/usr/share/fonts/truetype/dejavu')
for name, file in [('CVSans','DejaVuSans.ttf'),('CVSans-Bold','DejaVuSans-Bold.ttf'),('CVSans-Italic','DejaVuSans-Oblique.ttf'),('CVSerif','DejaVuSerif.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(font_root/file)))
pdfmetrics.registerFontFamily('CVSans',normal='CVSans',bold='CVSans-Bold',italic='CVSans-Italic',boldItalic='CVSans-Bold')
ink, green, muted = '#1d3030', '#21675c', '#526564'
for name, size, leading, font, color in [
    ('Name',27,33,'CVSerif',ink),('Subtitle',9,14,'CVSans',green),
    ('Section',13,18,'CVSerif',green),('BodyTextCV',8.5,12,'CVSans',ink),
    ('SmallCV',7.5,10,'CVSans',muted),('PaperTitle',8.5,11.5,'CVSans-Bold',ink)]:
    styles.add(ParagraphStyle(name,fontName=font,fontSize=size,leading=leading,textColor=colors.HexColor(color),spaceAfter=4))

story=[]
def p(text,style='BodyTextCV'):
    return Paragraph(text,styles[style])
def section(title):
    story.extend([Spacer(1,11),p(title,'Section')])
def link(url,label):
    return f'<link href="{escape(url)}" color="{green}">{escape(label)}</link>'
def publication(item,index):
    target=item['links'].get('Paper',item['scholar'])
    title=escape(item['title']).replace('SE_n(3)','SE<sub>n</sub>(3)')
    authors=escape(item['authors']).replace('Xingyu Chen','<b>Xingyu Chen</b>')
    return KeepTogether([p(f'{index}. {title}','PaperTitle'),p(authors,'SmallCV'),
        p(f'<i>{escape(item["venue"])}</i>, {item["year"]}. [{escape(item["kind"])}] '+link(target,'Paper / record'),'SmallCV'),Spacer(1,5)])

story += [p('Xingyu Chen','Name'),p('PhD Candidate | University of Technology Sydney','Subtitle'),
          p('Spatial audio | Personalized HRTFs | Sound field reconstruction | Audio generation','SmallCV'),
          p(' &nbsp; / &nbsp; '.join([link('https://xingyuaudio.github.io/','Website'),link(profile['scholar'],'Google Scholar'),link(profile['github'],'GitHub'),link(profile['linkedin'],'LinkedIn'),link(profile['institutional_profile'],'UTS profile')]),'SmallCV')]
section('Research profile')
story += [p(escape(profile['research_intro'])),p(escape(profile['research_statement']))]
section('Education and research')
story += [p('<b>University of Technology Sydney</b> | 2024 - Present<br/>PhD candidate, Centre for Audio, Acoustics and Vibration.'),
          p('<b>Australian National University</b><br/>MPhil research, Audio &amp; Acoustic Signal Processing Group.<br/>Thesis: <i>Learning-integrated Methods for Spatial Audio Capture and Reproduction</i> (Google Scholar record: 2025).<br/>Bachelor of Engineering (Honours), Mechatronics.')]
section('Academic service')
story += [p('Journal reviewer: The Journal of the Acoustical Society of America (JASA); IEEE Open Journal of Signal Processing (OJSP); IEEE Signal Processing Letters (SPL).')]
section('Earlier experience')
story += [p('<b>Research Assistant</b>, The Chinese University of Hong Kong, Shenzhen (2021 - 2022). Invariant filtering and visual-inertial navigation.'),
          p('<b>Teaching Assistant</b>, Australian National University. ENGN4213: Digital Systems and Microprocessors.')]
section('Recent publications and preprints')
for n,item in enumerate(papers[:3],1):story.append(publication(item,n))
story += [PageBreak(),p('Publications (continued)','Name'),p('Conference papers, earlier work, meeting abstract, and thesis.','SmallCV')]
for n,item in enumerate(papers[3:],4):story.append(publication(item,n))

def footer(canvas,doc):
    canvas.saveState();canvas.setStrokeColor(colors.HexColor('#dce3dc'));canvas.line(43,39,A4[0]-43,39)
    canvas.setFont('CVSans',7.5);canvas.setFillColor(colors.HexColor(muted))
    canvas.drawString(43,27,'Xingyu Chen | Updated November 2026');canvas.drawRightString(A4[0]-43,27,str(doc.page));canvas.restoreState()

SimpleDocTemplate(str(root/'files/Xingyu_Chen_CV.pdf'),pagesize=A4,rightMargin=43,leftMargin=43,topMargin=40,bottomMargin=52,
                  title='Xingyu Chen - Academic CV',author='Xingyu Chen').build(story,onFirstPage=footer,onLaterPages=footer)
print('Updated files/Xingyu_Chen_CV.pdf')
