#!/usr/bin/env python3
"""Lint del wiki: enlaces rotos, páginas huérfanas, confianza baja, frontmatter faltante.
Uso: python3 lint.py"""
import os, re, sys, collections

BASE = os.path.dirname(os.path.abspath(__file__))
SKIP = {'.obsidian', '.git', 'raw'}
LINK = re.compile(r'\[\[([^\]\|]+?)\\?(?:\|[^\]]*)?\]\]')   # tolera el escape \| de las tablas

def main():
    files = {}
    for r, d, fs in os.walk(BASE):
        d[:] = [x for x in d if x not in SKIP]
        for f in fs:
            if f.endswith('.md'):
                files[f[:-3]] = os.path.join(r, f)

    inbound = collections.defaultdict(set)
    broken, baja, sin_fm = collections.defaultdict(list), [], []

    for name, p in files.items():
        txt = open(p).read()
        body = re.sub(r'```.*?```', '', txt, flags=re.S)      # ignora bloques de código
        body = re.sub(r'`[^`\n]*`', '', body)                 # ...y código en línea
        for t in (m.strip() for m in LINK.findall(body)):
            (inbound[t].add(name) if t in files else broken[t].append(name))
        rel = os.path.relpath(p, BASE)
        if rel.startswith('wiki/') and os.path.basename(p) not in ('index.md', 'log.md'):
            if not txt.startswith('---'):
                sin_fm.append(rel)
            elif 'confianza: baja' in txt.split('---')[1]:
                baja.append(rel)

    def seccion(titulo, items):
        print(f"\n{titulo} ({len(items)})")
        for i in items:
            print("   ", i)

    seccion("ENLACES ROTOS", [f"{t}  ← {', '.join(sorted(set(s)))}" for t, s in sorted(broken.items())])
    seccion("HUÉRFANAS", sorted(n for n in files if n not in inbound and n not in ('index', 'log', 'CLAUDE')))
    seccion("CONFIANZA BAJA (necesitan fuente)", sorted(baja))
    seccion("SIN FRONTMATTER", sorted(sin_fm))
    print(f"\n{len(files)} archivos .md indexados.")
    return 1 if broken or sin_fm else 0

sys.exit(main())
