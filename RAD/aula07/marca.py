from dataclasses import dataclass

@dataclass
class Marca:
    id: int
    nome: str
    sigla: str
    __pais_origem: str = "Brasil"

    @property
    def pais_origem(self):
        return self.__pais_origem

    @classmethod
    def set_pais_origem(cls, pais_origem: str):
        cls.__pais_origem = pais_origem
