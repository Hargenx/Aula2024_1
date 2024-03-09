class DicionarioSinonimos:
    def __init__(self):
        self.sinonimos = {}
    def adicionar_sinonimos(self, palavra, sinonimos):
        self.sinonimos[palavra] = sinonimos
    def buscar_sinonimos(self, palavra):
        return self.sinonimos.get(palavra, "Palavra não encontrada")
    def remover_palavra(self, palavra):
        if palavra in self.sinonimos:
            del self.sinonimos[palavra]
            print(f"Palavra '{palavra}' e seus sinonimos foram removidos.")
        else:
            print(f"Palavra '{palavra}' não encontrada no dicionário.")

def principal():
    dicionario = DicionarioSinonimos()
    dicionario.adicionar_sinonimos("feliz", ["alegre", "contente"])
    dicionario.adicionar_sinonimos("triste", ["melancólico", "deprimido"])
    print(dicionario.buscar_sinonimos("feliz"))
    print(dicionario.buscar_sinonimos("chateado"))
    dicionario.remover_palavra("triste")

if __name__ == '__main__':
    principal()
