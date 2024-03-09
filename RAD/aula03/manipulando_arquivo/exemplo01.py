arquivo = open('RAD/aula03/manipulando_arquivo/nomes.txt', 'w')
arquivo.write('Raphael')
arquivo.close()

arquivo = open('RAD/aula03/manipulando_arquivo/nomes.txt')
print(arquivo.readline())
arquivo.close()