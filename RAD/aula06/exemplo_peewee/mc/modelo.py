from peewee import Model, SqliteDatabase, CharField, BooleanField
import os

# Obtendo o caminho completo para o arquivo do banco de dados
banco = os.path.abspath(os.path.join(os.path.dirname(__file__), "tarefas.sqlite"))

# Definindo a conexão com o banco de dados
db = SqliteDatabase(banco)


# Definindo a classe de modelo
class Tarefa(Model):
    titulo = CharField()
    completo = BooleanField()

    class Meta:
        database = db
