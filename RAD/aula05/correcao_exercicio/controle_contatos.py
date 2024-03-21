from contato import Contato

class ControleContatos:
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.carregar_contatos()

    def adicionar_contato(self, contato: Contato):
        self.contatos[contato.email] = contato
        self.salvar_contatos()

    def buscar_contato(self, email: str) -> Contato:
        return self.contatos.get(email)

    def remover_contato(self, email: str):
        if email in self.contatos:
            del self.contatos[email]
            self.salvar_contatos()

    @staticmethod
    def carregar_contatos():
        contatos = {}
        try:
            with open(arquivo, 'r') as arquivo:
                for linha in arquivo:
                    nome, sobrenome, email, telefone = linha.strip().split(',')
                    contato = Contato(nome, sobrenome, email, telefone)
                    contatos[email] = contato
        except FileNotFoundError:
            print("O arquivo de contatos não foi encontrado.")
        except PermissionError:
            print("Permissão negada para acessar o arquivo de contatos.")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar os contatos: {e}")
        return contatos

    @staticmethod
    def salvar_contatos(contatos):
        try:
            with open(arquivo, 'w') as arquivo:
                for _, contato in contatos.items():
                    arquivo.write(f"{contato.nome},{contato.sobrenome},{contato.email},{contato.telefone}\n")
        except Exception as e:
            print(f"Ocorreu um erro ao salvar os contatos: {e}")
