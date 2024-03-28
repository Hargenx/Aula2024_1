from dataclasses import dataclass

@dataclass
class Estudante:
    nome: str
    idade: int
    curso: str

def salvar_estudantes_em_txt(estudantes: list[Estudante], nome_arquivo: str) -> None:
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for estudante in estudantes:
                arquivo.write(f"Nome: {estudante.nome}\n")
                arquivo.write(f"Idade: {estudante.idade}\n")
                arquivo.write(f"Curso: {estudante.curso}\n")
                arquivo.write("\n")
        print(f"Estudantes salvos em {nome_arquivo}")
    except IOError as e:
        print(f"Erro ao salvar em {nome_arquivo}: {e}")

if __name__ == "__main__":
    estudante1 = Estudante("Raphael", 22, "Ciência da Computação")
    estudante2 = Estudante("Carol", 18, "Nutrição")
    estudantes = [estudante1, estudante2]
    salvar_estudantes_em_txt(estudantes, "estudantes.txt")
