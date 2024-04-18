import csv
import os

dados = [
    ["Nome", "Idade"],
    ["Raphael", "39"],
    ["Sara", "67"],
    ["Caroline", "30"],
    ["Gilson", "67"],
]


def salvar_em_csv(dados: list, nome_arquivo_saida: str) -> None:
    """
    Salva os dados em um arquivo CSV.

    Parâmetros:
        dados (list): Dados a serem salvos no arquivo CSV.
        nome_arquivo_saida (str): Caminho completo do arquivo de saída.

    Retorna:
        None
    """
    try:
        with open(nome_arquivo_saida, "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(dados)
        print(f"Dados salvos em {nome_arquivo_saida}")
    except IOError as e:
        print(f"Erro ao salvar em {nome_arquivo_saida}: {e}")


if __name__ == "__main__":
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    nome_arquivo_saida = os.path.join(diretorio_atual, "pessoas.csv")

    salvar_em_csv(dados, nome_arquivo_saida)
