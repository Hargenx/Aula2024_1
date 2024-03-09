# Tipos de arquivos: texto e binário
# Modos de abertura de arquivos: leitura('r'), escrita('w'), acrescentar('a')
# Exemplo de abertura e leitura de um arquivo de texto
caminho_arquivo = 'RAD/aula03/manipulando_arquivo/exemplo.txt'
# Leitura de todo o arquivo
with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# Exemplo de abertura e escrita em um arquivo de texto
caminho_saida = 'RAD/aula03/manipulando_arquivo/exemplo.txt'
# Escrita em um arquivo (o modo 'w' sobrescreve o arquivo se já existir)
with open(caminho_saida, 'w') as arquivo:
    arquivo.write("Nossa aula!")
# Modo de apêndice para adicionar conteúdo a um arquivo existente
with open(caminho_saida, 'a') as arquivo:
    arquivo.write("\nde python!.")
