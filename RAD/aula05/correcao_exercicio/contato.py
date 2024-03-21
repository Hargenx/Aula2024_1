from dataclasses import dataclass

@dataclass
class Contato:
    nome: str
    sobrenome: str
    email: str
    telefone: str

    def __str__(self:  'Contato') -> str:
        return f"{self.nome} {self.sobrenome}\nEmail: {self.email}\nTelefone: {self.telefone}"
