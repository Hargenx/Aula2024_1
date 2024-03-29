from peewee import Model, SqliteDatabase, CharField, BooleanField
import os

banco = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "tarefas.sqlite")
    )

# Definindo a conexão com o banco de dados
db = SqliteDatabase(banco)

# Criando a classe de modelo
class Tarefas(Model):
    titulo = CharField()
    completo = BooleanField()

class Meta:
    database = db

# Criando as tabelas no banco de dados
db.connect()
db.create_tables([Tarefas])
# Criando uma nova tarefa
nova_tarefa = Tarefas.create(titulo='Fazer compras', completo=False)
# Consultando as tarefas
tarefas = Tarefas.select()
for tarefa in tarefas:
    print(tarefa.titulo, tarefa.completo)
# Verificando se a lista de tarefas está vazia
if not tarefas.exists():
    print('Sem tarefas')

# Atualizando uma tarefa
atualiza_tarefa = Tarefas.get(titulo='Fazer compras')
atualiza_tarefa.completo = True
atualiza_tarefa.save()

# Consultando as tarefas
tarefas = Tarefas.select()
for tarefa in tarefas:
    print(tarefa.titulo, tarefa.completo)
# Verificando se a lista de tarefas está vazia
if not tarefas.exists():
    print('Sem tarefas')

# Deletando uma tarefa
apaga_tarefa = Tarefas.get(titulo='Fazer compras')
apaga_tarefa.delete_instance()
# Consultando as tarefas
tarefas = Tarefas.select()
for tarefa in tarefas:
    print(tarefa.titulo, tarefa.completo)
# Verificando se a lista de tarefas está vazia
if not tarefas.exists():
    print('Sem tarefas')
