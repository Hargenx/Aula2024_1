def decorador(func):
    def wrapper():
        print(f"Antes de chamar a funcionalidade: {func.__name__}")
        func()
        print("Depois de chamar a funcionalidade")
    return wrapper

@decorador
def uma_coisa():
    print("Uma coisa")

@decorador
def outra_coisa():
    print("Outra coisa")

if __name__ == "__main__":
    match input("Qual o nome da funcionalidade? "):
        case "uma coisa":
            uma_coisa()
        case "outra coisa":
            outra_coisa()
        case _:
            print("Funcionalidade inválida")