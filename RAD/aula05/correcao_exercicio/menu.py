from contato import Contato
from controle_contatos import ControleContatos
import os

def menu():
    caminho = os.path.dirname(os.path.abspath(__file__))
    arquivo_nome = os.path.join(caminho, "contatos.txt")
    controle = ControleContatos(arquivo_nome)

    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Remover Contato")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        match escolha:
            case '1':
                nome = input("Nome: ")
                sobrenome = input("Sobrenome: ")
                email = input("Email: ")
                telefone = input("Telefone: ")
                contato = Contato(nome, sobrenome, email, telefone)
                controle.adicionar_contato(contato)
                print("Contato adicionado com sucesso!")

            case '2':
                email = input("Digite o email do contato a ser buscado: ")
                contato = controle.buscar_contato(email)
                if contato:
                    print("Contato encontrado:")
                    print(contato)
                else:
                    print("Contato não encontrado.")

            case '3':
                email = input("Digite o email do contato a ser removido: ")
                controle.remover_contato(email)
                print("Contato removido com sucesso!")

            case '4':
                print("Saindo do programa.")
                break

            case _:
                print("Opção inválida. Tente novamente.")