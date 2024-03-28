import json
from datetime import datetime
import os


def salvar_em_json(dados: dict, nome_arquivo_saida: str) -> None:
    """
    Salva os dados em um arquivo JSON.

    Parâmetros:
        dados (dict): Dados a serem salvos no arquivo JSON.
        nome_arquivo_saida (str): Caminho completo do arquivo de saída.

    Retorna:
        None
    """
    try:
        inicio = datetime.now()

        with open(nome_arquivo_saida, "w") as arquivo:
            json.dump(dados, arquivo)
        fim = datetime.now()
        print(f"Dados salvos com sucesso em '{nome_arquivo_saida}'. Tempo de execução: {fim - inicio}.")
    except IOError:
        print("Erro ao salvar o arquivo JSON.")


# Exemplo de uso:
def carregar_json(nome_arquivo_entrada: str) -> dict:
    """
    Carrega os dados de um arquivo JSON.

    Parâmetros:
        nome_arquivo_entrada (str): Caminho completo do arquivo de entrada.

    Retorna:
        dict: Dados carregados do arquivo JSON.
    """
    try:
        with open(nome_arquivo_entrada, "r") as arquivo:
            return json.load(arquivo)
    except IOError:
        print(f"Erro ao carregar o arquivo JSON '{nome_arquivo_entrada}'.")
        return {}

if __name__ == "__main__":
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    dados_json_entrada = os.path.join(diretorio_atual, "dados_entrada.json")
    nome_arquivo_saida = os.path.join(diretorio_atual, "dados_saida.json")

    dados = carregar_json(dados_json_entrada)

    if dados:
        salvar_em_json(dados, nome_arquivo_saida)
