import csv

dados = [
    ['Nome', 'Idade'],
    ['Raphael', '39'],
    ['Maria', '25'],
    ['Carla', '37'],
    ['Amanda', '42']
]

def salvar_em_csv(dados):
    try:
        with open('pessoas.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(dados)
        print("Dados salvos em pessoas.csv")
    except IOError as e:
        print(f"Erro ao salvar em pessoas.csv: {e}")

if __name__ == "__main__":
    salvar_em_csv(dados)
