# ------------ imports ------------
from arma import punho
from barra_vida import BarraVida


# ------------ parent class setup ------------
class Personagem:
    def __init__(
        self,
        nome: str,
        vida: int,
    ) -> None:
        self.nome = nome
        self.vida = vida
        self.vida_max = vida

        self.arma = punho

    def attack(self, alvo) -> None:
        alvo.vida -= self.arma.dano
        alvo.vida = max(alvo.vida, 0)
        alvo.barra_vida.update()
        print(
            f"{self.nome} dealt {self.arma.dano} dano to "
            f"{alvo.nome} with {self.arma.nome}"
        )


# ------------ subclass setup ------------
class Hero(Personagem):
    def __init__(self, nome: str, vida: int) -> None:
        super().__init__(nome=nome, vida=vida)

        self.arma_padrao = self.arma
        self.barra_vida = BarraVida(self, color="green")

    def equip(self, arma) -> None:
        self.arma = arma
        print(f"{self.nome} equipped a(n) {self.arma.nome}!")

    def drop(self) -> None:
        print(f"{self.nome} dropped the {self.arma.nome}!")
        self.arma = self.arma_padrao


# ------------ subclass setup ------------
class Enemy(Personagem):
    def __init__(
        self,
        nome: str,
        vida: int,
        arma,
    ) -> None:
        super().__init__(nome=nome, vida=vida)
        self.arma = arma

        self.barra_vida = BarraVida(self, color="red")
