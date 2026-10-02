#!/usr/bin/env python3
"""Audit V4 documentation and publication boundaries without third-party packages."""
from __future__ import annotations
import argparse
import json
import re
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote

PRIVATE_IP = re.compile(r'\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b')
MAC = re.compile(r'\b(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b')
UUID = re.compile(r'\b[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}\b')
SECRET = re.compile(r'-----BEGIN (?:[A-Z ]*PRIVATE KEY)-----|\bgh[pousr]_[A-Za-z0-9]{20,}|\bgithub_pat_[A-Za-z0-9_]{20,}|\bxox[baprs]-[A-Za-z0-9-]{20,}')
ASSIGNMENT = re.compile(r'(?im)^\s*(?:password|passwd|api_key|access_token|private_key)\s*[:=]\s*(\S+)')
LINK = re.compile(r'!?\[[^\]]*\]\(([^\n)]+)\)')
STATUSES = {
 'Document status': {'Draft','Current','Needs Review','Superseded','Archived'},
 'Service status': {'Idea','Planned','In Progress','Implemented','Validated','Operational','Paused','Blocked','Retired','Rejected'},
 'System status': {'Idea','Planned','In Progress','Implemented','Validated','Operational','Paused','Blocked','Retired','Rejected'},
 'Decision status': {'Proposed','Accepted','Rejected','Superseded','Deprecated'},
 'Validation status': {'Not Started','In Progress','Passed','Failed','Blocked','Not Applicable','Passed with Exception'},
}
def visible(s):
    output=[];fenced=False
    for line in s.splitlines():
        if re.match(r'^\s*(```|~~~)',line):fenced=not fenced;continue
        if not fenced:output.append(line)
    return '\n'.join(output)
def anchors(s):
    result=set();counts={}
    for title in re.findall(r'^#{1,6}\s+(.+)$',visible(s),re.M):
        slug=title.lower().replace('`','').replace('*','')
        slug=''.join(c for c in slug if c in ' -_' or unicodedata.category(c)[0] in 'LN').replace(' ','-')
        n=counts.get(slug,0);counts[slug]=n+1;result.add(slug+(f'-{n}' if n else ''))
    return result
def main():
    parser=argparse.ArgumentParser();parser.add_argument('repository',nargs='?',default='.');parser.add_argument('--private',action='store_true')
    args=parser.parse_args();root=Path(args.repository).resolve();errors=[];md_count=0;svg_count=0
    required=['README.md','docs/README.md','docs/validation/v4-baseline.md','docs/release/v4-document-audit.md','docs/release/pruning-recommendations.md','assets/diagrams/hero.svg','.github/workflows/documentation-audit.yml']
    for p in required:
        if not (root/p).is_file():errors.append(f'Missing required file: {p}')
    if (root/'private').exists() and not args.private:errors.append('Private companion directory present in public tree')
    for p in sorted(root.rglob('*')):
        if not p.is_file() or '.git' in p.parts or '__pycache__' in p.parts:continue
        rel=p.relative_to(root);private=rel.parts[0]=='private'
        if p.suffix in {'.db','.sqlite','.jsonl','.unifi','.pem','.key'} or p.name=='.env' or p.name.startswith('.env.') and p.name!='.env.example':
            errors.append(f'Forbidden data/credential artifact: {rel}')
        try:s=p.read_text()
        except UnicodeDecodeError:
            if p.suffix not in {'.png','.jpg','.jpeg','.webp'}:errors.append(f'Unreviewed binary: {rel}')
            continue
        if SECRET.search(s):errors.append(f'Secret-shaped content: {rel}')
        for value in ASSIGNMENT.findall(s):
            if not (value.startswith('<') or value in {'...','"..."',"'...'"}):errors.append(f'Credential assignment requires review: {rel}')
        if not(private and args.private):
            for label,pattern in [('private IPv4',PRIVATE_IP),('MAC',MAC),('UUID',UUID)]:
                if pattern.search(s):errors.append(f'Public {label} pattern: {rel}')
        if any(l.rstrip()!=l for l in s.splitlines()):errors.append(f'Trailing whitespace: {rel}')
        if not s.endswith('\n'):errors.append(f'Missing final newline: {rel}')
        if p.suffix=='.svg':
            svg_count+=1
            try:
                element=ET.fromstring(s)
                if not element.tag.endswith('svg'):errors.append(f'Not SVG: {rel}')
                if element.find('{http://www.w3.org/2000/svg}title') is None or element.find('{http://www.w3.org/2000/svg}desc') is None:errors.append(f'Missing accessible title/description: {rel}')
                if re.search(r'<(?:script|foreignObject)\b|(?:href|src)\s*=\s*["\'](?:https?:|file:|javascript:)',s,re.I):errors.append(f'Unsafe/external SVG content: {rel}')
            except ET.ParseError as e:errors.append(f'SVG parse failure: {rel}: {e}')
        if p.suffix!='.md':continue
        md_count+=1;v=visible(s)
        if len(re.findall(r'^# ',v,re.M))!=1:errors.append(f'Expected one H1: {rel}')
        if not s.strip():errors.append(f'Empty document: {rel}')
        for field,allowed in STATUSES.items():
            for value in re.findall(r'^\|\s*'+re.escape(field)+r'\s*\|\s*([^|]+)\|', '\n'.join(v.splitlines()[:25]), re.M):
                if value.strip() not in allowed:errors.append(f'Invalid {field}: {rel}')
        if 'standards/templates' in rel.as_posix():continue
        for raw in LINK.findall(v):
            target=raw.strip()
            if '<' in target or '>' in target or re.match(r'^[a-zA-Z]+:',target):continue
            path,_,fragment=target.partition('#');path=unquote(path.split('?',1)[0])
            resolved=(p.parent/path).resolve() if path else p
            if not resolved.is_relative_to(root):errors.append(f'Link escapes tree: {rel}: {target}')
            elif not resolved.exists():errors.append(f'Broken link: {rel}: {target}')
            elif fragment and resolved.suffix=='.md' and unquote(fragment) not in anchors(resolved.read_text()):errors.append(f'Broken fragment: {rel}: {target}')
    try:json.loads((root/'.markdownlint.json').read_text())
    except (OSError,ValueError) as e:errors.append(f'Markdown configuration: {e}')
    print(f'V4 audit: {md_count} Markdown files; {svg_count} SVG assets; {len(errors)} errors')
    for error in errors:print('ERROR:',error)
    return bool(errors)
if __name__=='__main__':raise SystemExit(main())
