import json
dados = [{
    'nome': 'Raphael',
    'idade': 39,
    'cidade': 'Rio de Janeiro'
},
{
    'nome': 'Marcia',
    'idade': 49,
    'cidade': 'Rio Grande do sul'
}]
def salvar_em_json(dados: dict) -> str:
    try:
        with open('dados.json', 'w') as arquivo:
            json.dump(dados, arquivo)
        print("Dados salvos em dados.json")
    except IOError as e:
        print(f"Erro ao salvar em dados.json: {e}")
if __name__ == "__main__":
    salvar_em_json(dados)
