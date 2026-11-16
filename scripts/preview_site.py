"""Render the new HTML/Liquid pages for local QA without a Ruby installation.

This is a lightweight preview; GitHub Pages remains the authoritative Jekyll build.
Requires PyYAML and python-liquid. Output is ignored by git.
"""
from pathlib import Path
import re, shutil, json
from collections import OrderedDict
import yaml
from liquid import Environment, DictLoader

root=Path(__file__).resolve().parents[1]
out=root/'_site'
def preprocess(text):
    return re.sub(r'{%\s*include ([\w./-]+)\s*%}',r"{% include '\1' %}",text)
def group_by(items,key):
    groups=OrderedDict()
    for item in items:groups.setdefault(str(item[key]),[]).append(item)
    return [dict(name=key,items=values) for key,values in groups.items()]
env=Environment(loader=DictLoader({p.name:preprocess(p.read_text()) for p in (root/'_includes').glob('*.html')}))
env.filters['group_by']=group_by
config=yaml.safe_load((root/'_config.yml').read_text())
config['data']={p.stem:yaml.safe_load(p.read_text()) for p in (root/'_data').glob('*.yml')}
for page_path in (root/'_pages').iterdir():
    text=page_path.read_text()
    if not text.startswith('---'):continue
    _,front,body=text.split('---',2)
    page=yaml.safe_load(front)
    if page.get('layout')!='academic':continue
    page['url']=page['permalink']
    context=dict(site=config,page=page)
    content=env.from_string(preprocess(body)).render(**context)
    html=env.from_string(preprocess((root/'_layouts/academic.html').read_text())).render(**context,content=content)
    target=out/(page['url'].lstrip('/') or 'index.html')
    if target.suffix!='.html':target=target/'index.html'
    target.parent.mkdir(parents=True,exist_ok=True);target.write_text(html)
    for alias in page.get('redirect_from',[]):
        dest=out/alias.lstrip('/')
        if dest.suffix!='.html':dest=dest/'index.html'
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(f'<!doctype html><meta http-equiv="refresh" content="0;url={page["url"]}"><a href="{page["url"]}">Continue</a>')
for name in ['assets','images','files']:shutil.copytree(root/name,out/name,dirs_exist_ok=True)
print('Rendered preview to _site/')
