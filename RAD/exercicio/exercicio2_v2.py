import json

def salvar_em_json(dados: dict, nome_arquivo_saida: str) -> None:
    try:
        with open(nome_arquivo_saida, "w") as arquivo:
            json.dump(dados, arquivo)
        print(f"Dados salvos com sucesso em '{nome_arquivo_saida}'.")
    except IOError:
        print("Erro ao salvar o arquivo JSON.")

# Exemplo de uso:
def carregar_json(nome_arquivo_entrada: str) -> dict:
    try:
        with open(nome_arquivo_entrada, "r") as arquivo:
            return json.load(arquivo)
    except IOError:
        print(f"Erro ao carregar o arquivo JSON '{nome_arquivo_entrada}'.")
        return None
if __name__ == "__main__":
    dados_json_entrada = "dados_entrada.json"
    dados = carregar_json(dados_json_entrada)

    if dados:
        nome_arquivo_saida = "dados_saida.json"
        salvar_em_json(dados, nome_arquivo_saida)