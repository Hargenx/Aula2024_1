caminho_arquivo = 'RAD/aula03/manipulando_arquivo/nomes.txt'

with open(caminho_arquivo, 'r') as arquivo:
    linha1 = arquivo.readline()
    print(f'Linha 1: {linha1}')

    linha2 = arquivo.readline()
    print(f'Linha 2: {linha2}')