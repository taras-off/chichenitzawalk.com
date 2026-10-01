#!/usr/bin/env python3
"""mkbody.py <md> <L.json> <out.html> — markdown-мастер -> HTML-тело статьи."""
import sys, json, io, md2body
md = io.open(sys.argv[1], encoding='utf-8').read()
L  = json.load(io.open(sys.argv[2], encoding='utf-8'))
h  = md2body.build(md, L)
io.open(sys.argv[3], 'w', encoding='utf-8').write(h)
print(sys.argv[3], len(h), 'bytes')
