from dataclasses import dataclass
import os

@dataclass
class Estudante:
    nome: str
    idade: int
    curso: str

def salvar_estudantes_em_txt(estudantes: list[Estudante], nome_arquivo: str) -> None:
    """
    Salva os dados dos estudantes em um arquivo de texto.

    Parâmetros:
        estudantes (list): Lista de objetos Estudante a serem salvos no arquivo de texto.
        nome_arquivo (str): Caminho completo do arquivo de saída.

    Retorna:
        None
    """
    try:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        nome_arquivo_saida = os.path.join(diretorio_atual, nome_arquivo)

        with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo:
            for estudante in estudantes:
                arquivo.write(f"Nome: {estudante.nome}\n")
                arquivo.write(f"Idade: {estudante.idade}\n")
                arquivo.write(f"Curso: {estudante.curso}\n")
                arquivo.write("\n")
        print(f"Estudantes salvos em {nome_arquivo_saida}")
    except IOError as e:
        print(f"Erro ao salvar em {nome_arquivo_saida}: {e}")

if __name__ == "__main__":
    estudante1 = Estudante("Raphael", 22, "Ciência da Computação")
    estudante2 = Estudante("Carol", 18, "Nutrição")
    estudantes = [estudante1, estudante2]
    salvar_estudantes_em_txt(estudantes, "estudantes.txt")
