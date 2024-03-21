#!/usr/bin/env python
''' shebang ou hashbang. 
Ele é uma convenção em sistemas Unix-like, incluindo Linux e macOS, que indica ao 
sistema operacional qual interpretador deve ser usado para executar o script.'''
import sys
import re

# Expressão regular para separar palavras
WORD_RE = re.compile(r"[\w']+")
for line in sys.stdin:
    # Remove espaços em branco à direita e à esquerda e divide a linha em palavras
    words = WORD_RE.findall(line.strip().lower())
    # Emite cada palavra com uma contagem inicial de 1
    for word in words:
        print('%s\t%s' % (word, 1))
