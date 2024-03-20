#!/usr/bin/env python
''' shebang ou hashbang. 
Ele é uma convenção em sistemas Unix-like, 
incluindo Linux e macOS, que indica ao 
sistema operacional qual interpretador deve 
ser usado para executar o script.'''
from mrjob.job import MRJob

class WordCount(MRJob):

    def mapper(self, _, line):
        # Remove espaços em branco à direita e à esquerda e divide a linha em palavras
        words = line.strip().lower().split()
        # Emite cada palavra com uma contagem inicial de 1
        for word in words:
            yield word, 1

    def reducer(self, word, counts):
        # Soma as contagens para cada palavra
        yield word, sum(counts)

if __name__ == '__main__':
    WordCount.run()
