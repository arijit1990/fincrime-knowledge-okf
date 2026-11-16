"""Validate the bundle in kb/ against OKF v0.2 conformance (section 11) plus stricter local checks.

Usage: python tools/validate_okf.py [path/to/kb]
Exit code 0 when everything passes; problems are listed otherwise.
"""
import os
import re
import sys
from collections import Counter

import yaml

KB = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kb')
KB = os.path.normpath(KB)
FRONT = re.compile(r'\A---\n(.*?)\n---\n', re.S)
LINK = re.compile(r'\]\(([^)\s]+)\)')
problems = []
types = Counter()
n_files = n_links = 0

for root, _, files in os.walk(KB):
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, KB).replace('\\', '/')
        text = open(path, encoding='utf-8').read()
        n_files += 1
        m = FRONT.match(text)
        if f == 'index.md':
            if m:
                meta = yaml.safe_load(m.group(1)) or {}
                if rel != 'index.md' or set(meta) - {'okf_version'}:
                    problems.append(f'{rel}: index.md may only carry okf_version frontmatter, at the bundle root')
            if rel == 'index.md' and not (m and str((yaml.safe_load(m.group(1)) or {}).get('okf_version')) == '0.2'):
                problems.append('index.md: root should declare okf_version "0.2"')
        elif f == 'log.md':
            if m:
                problems.append(f'{rel}: log.md must not have frontmatter')
            for h in re.findall(r'^## (.+)$', text, re.M):
                if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', h.strip()):
                    problems.append(f'{rel}: log heading not ISO date: {h}')
        else:
            if not m:
                problems.append(f'{rel}: missing frontmatter')
                continue
            try:
                meta = yaml.safe_load(m.group(1))
            except yaml.YAMLError as e:
                problems.append(f'{rel}: unparseable frontmatter: {e}')
                continue
            if not isinstance(meta, dict) or not str(meta.get('type') or '').strip():
                problems.append(f'{rel}: frontmatter lacks a non-empty type')
                continue
            types[meta['type']] += 1
            if meta['type'] == 'Source Document':
                d = os.path.dirname(path)
                prefix = 'text' if meta.get('content_mode') == 'full_text' else 'digest'
                for i in range(1, int(meta.get('parts_total') or 0) + 1):
                    if meta.get('digest_pending_parts'):
                        break  # draft: digest still being produced
                    if not os.path.exists(os.path.join(d, f'{prefix}-{i:03d}.md')):
                        problems.append(f'{rel}: missing part {prefix}-{i:03d}.md')
            for s in meta.get('sources') or []:
                if not s.get('resource'):
                    problems.append(f'{rel}: sources entry without resource')
        for target in LINK.findall(text):
            if re.match(r'[a-z]+:', target) or target.startswith('#'):
                continue
            n_links += 1
            t = target.split('#')[0]
            dest = os.path.normpath(os.path.join(KB, t.lstrip('/')) if t.startswith('/') else os.path.join(root, t))
            if not os.path.exists(dest):
                problems.append(f'{rel}: broken link -> {target}')

print(f'{n_files} markdown files, {n_links} internal links checked')
for t, n in types.most_common():
    print(f'  {n:6d}  {t}')
if problems:
    print(f'\n{len(problems)} problem(s):')
    for p in problems[:200]:
        print('  -', p)
    sys.exit(1)
print('\nOK: bundle conforms to OKF v0.2 and all internal links resolve')
