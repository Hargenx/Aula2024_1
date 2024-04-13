'''from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

# Criando uma instância de Pessoa
pessoa1 = Pessoa(
    cpf=12345678900, nome="Raphael", nascimento=date(1984, 7, 26), oculos=True
)
# Criando uma instância de Marca
marca1 = Marca(id=1, nome="Fiat", sigla="FIA")

# Criando uma instância de Veiculo
veiculo1 = Veiculo(placa="LRW1I27", cor="Cinza", proprietario=pessoa1, marca=marca1)

# Exibindo informações das instâncias
print("Informações do Pessoa:")
print(f"CPF: {pessoa1.cpf}")
print(f"Nome: {pessoa1.nome}")
print(f"Nascimento: {pessoa1.nascimento}")
print(f"Usa óculos: {pessoa1.oculos}")

print("\nInformações da Marca:")
print(f"ID: {marca1.id}")
print(f"Nome: {marca1.nome}")
print(f"Sigla: {marca1.sigla}")

print("\nInformações do Veículo:")
print(f"\tPlaca: {veiculo1.placa}")
print(f"\tCor: {veiculo1.cor}")
print("Proprietário:")
print(f"\tCPF: {veiculo1.proprietario.cpf}")
print(f"\tNome: {veiculo1.proprietario.nome}")
print("Marca:")
print(f"\tID: {veiculo1.marca.id}")
print(f"\tNome: {veiculo1.marca.nome}")
print(f"\tSigla: {veiculo1.marca.sigla}")'''


from banco import BancoDeDados
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

# Criando uma instância da classe BancoDeDados
banco = BancoDeDados()

# Conectando ao banco de dados
banco.conectar()

# Criando as tabelas necessárias
banco.criar_tabelas()

# Inserindo uma pessoa
pessoa1 = Pessoa(cpf=12345678900, nome="Raphael", nascimento="1984-07-26", oculos=True)
banco.inserir_pessoa(pessoa1)

# Inserindo uma marca
marca1 = Marca(id=1, nome="FIAT", sigla="FIA")
banco.inserir_marca(marca1)

# Inserindo um veículo
veiculo1 = Veiculo(placa="LRW1I27", cor="Cinza", proprietario=pessoa1, marca=marca1)
banco.inserir_veiculo(veiculo1)

# Buscando todas as pessoas
print("Pessoas:")
for pessoa in banco.buscar_todas_pessoas():
    print(pessoa)

# Buscando todas as marcas
print("\nMarcas:")
for marca in banco.buscar_todas_marcas():
    print(marca)

# Buscando todos os veículos
print("\nVeículos:")
for veiculo in banco.buscar_todos_veiculos():
    print(veiculo)

# Fechando a conexão com o banco de dados
banco.fechar_conexao()
