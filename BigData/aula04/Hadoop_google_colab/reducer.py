#!/usr/bin/env python
''' shebang ou hashbang. 
Ele é uma convenção em sistemas Unix-like, 
incluindo Linux e macOS, que indica ao 
sistema operacional qual interpretador deve 
ser usado para executar o script.'''
import sys

current_word = None
current_count = 0
word = None

# Lê a entrada de sys.stdin
for line in sys.stdin:
    # Remove espaços em branco à direita e à esquerda
    line = line.strip()

    # Faz o parsing da entrada
    word, count = line.split('\t', 1)

    # Converte a contagem para int
    try:
        count = int(count)
    except ValueError:
        # Se a contagem não for um número, ignora esta linha
        continue

    # Esta parte assume que os dados estão ordenados pelo shuffle/sort, o que é o caso padrão
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Emite a palavra anteriormente processada e sua contagem
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# Emite a última palavra se necessário
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
