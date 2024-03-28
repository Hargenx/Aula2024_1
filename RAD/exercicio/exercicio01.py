from dataclasses import dataclass
import os
@dataclass
class Pessoa:
    nome: str
    idade: int
def salvar_em_txt(pessoas: list[Pessoa], nome_arquivo: str) -> None:
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for pessoa in pessoas:
                arquivo.write(f'Nome: {pessoa.nome}, Idade: {pessoa.idade}\n')
        print("Dados salvos em pessoas.txt")
    except IOError as e:
        print(f"Erro ao salvar em pessoas.txt: {e}")
if __name__ == "__main__":
    pessoas = [Pessoa("Raphael", 39), Pessoa("Caroline", 30)]
    diretorio_atual = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "pessoas.txt")
    )
    salvar_em_txt(pessoas, diretorio_atual)
