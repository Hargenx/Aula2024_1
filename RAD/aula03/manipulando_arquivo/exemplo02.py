caminho_arquivo = 'RAD/aula03/manipulando_arquivo/nomes.txt'

arquivo = open(caminho_arquivo, 'r')

linha1 = arquivo.readline()
print(f'Linha 1: {linha1}')

linha2 = arquivo.readline()
print(f'Linha 2: {linha2}')

arquivo.close()