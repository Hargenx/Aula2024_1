import requests
import pandas as pd


class ProjetoPython:
    def __init__(self, nome):
        self.nome = nome
        self.dados = None

    def entrada_dados(self):
        dados = input("Por favor, insira os dados do projeto: ")
        self.dados = dados

    def captacao_dados_web(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            self.dados = response.text
            print("Dados captados com sucesso!")
        else:
            print("Falha ao captar os dados. Status code:", response.status_code)

    def carregar_dados_artefato(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, "r") as arquivo:
                self.dados = arquivo.read()
                print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado. Verifique o caminho e tente novamente.")

    def salvar_dados_artefato(self, caminho_arquivo):
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write(self.dados)
        print("Dados salvos com sucesso!")

    def exibir_dados(self):
        print("Dados do projeto:", self.dados)


# Exemplo de uso:
projeto = ProjetoPython("Meu Projeto Python")

# Entrada de dados em sistemas de informação
projeto.entrada_dados()

# Captação de dados por scraping
url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp"
projeto.captacao_dados_web(url)

# Manipulação de artefatos de dados (planilhas, textos, arquivos locais)
caminho_arquivo = "dados.txt"
projeto.salvar_dados_artefato(caminho_arquivo)
projeto.carregar_dados_artefato(caminho_arquivo)

# Exibição dos dados do projeto
projeto.exibir_dados()
