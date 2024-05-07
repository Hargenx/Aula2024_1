# ------------ class setup ------------
class Arma:
    def __init__(self, nome: str, tipo_arma: str, dano: int, valor: int) -> None:
        self.nome = nome
        self.tipo_arma = tipo_arma
        self.dano = dano
        self.valor = valor


# ------------ object creation ------------
espada_aco = Arma(nome="Espada de aço", tipo_arma="corte", dano=5, valor=10)

arco_curto = Arma(nome="Arco Curto", tipo_arma="tiro", dano=4, valor=8)

punho = Arma(nome="Punho", tipo_arma="pancada", dano=2, valor=0)
