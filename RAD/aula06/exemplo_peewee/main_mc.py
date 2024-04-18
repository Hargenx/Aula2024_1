from peewee import Model, SqliteDatabase, CharField, BooleanField
import os

# Obtendo o caminho completo para o arquivo do banco de dados
banco = os.path.abspath(os.path.join(os.path.dirname(__file__), "tarefas_mc.sqlite"))

# Definindo a conexão com o banco de dados
db = SqliteDatabase(banco)


# Definindo a classe de modelo
class Tarefa(Model):
    titulo = CharField()
    completo = BooleanField()

    class Meta:
        database = db

    @classmethod
    def criar(cls, titulo, completo):
        try:
            nova_tarefa = cls.create(titulo=titulo, completo=completo)
            return nova_tarefa
        except Exception as e:
            print(f"Erro ao criar tarefa: {e}")

    @classmethod
    def buscar_todos(cls):
        return cls.select()

    @classmethod
    def buscar_por_titulo(cls, titulo):
        return cls.get(cls.titulo == titulo)

    def atualizar(self, completo):
        self.completo = completo
        self.save()

    def apagar(self):
        self.delete_instance()


# Controlador
class TarefaController:
    @staticmethod
    def criar_tarefa(titulo, completo):
        return Tarefa.criar(titulo, completo)

    @staticmethod
    def buscar_todas_tarefas():
        return Tarefa.buscar_todos()

    @staticmethod
    def buscar_tarefa_por_titulo(titulo):
        return Tarefa.buscar_por_titulo(titulo)

    @staticmethod
    def atualizar_tarefa(titulo, completo):
        tarefa = Tarefa.buscar_por_titulo(titulo)
        tarefa.atualizar(completo)

    @staticmethod
    def apagar_tarefa(titulo):
        tarefa = Tarefa.buscar_por_titulo(titulo)
        tarefa.apagar()


if __name__ == "__main__":
    # Criando as tabelas no banco de dados
    db.connect()
    db.create_tables([Tarefa])

    # Criando uma nova tarefa
    TarefaController.criar_tarefa("Fazer compras", False)

    # Consultando as tarefas
    for tarefa in TarefaController.buscar_todas_tarefas():
        print(tarefa.titulo, tarefa.completo)

    # Verificando se a lista de tarefas está vazia
    if not TarefaController.buscar_todas_tarefas():
        print("Sem tarefas")

    # Atualizando uma tarefa
    TarefaController.atualizar_tarefa("Fazer compras", True)

    # Consultando as tarefas
    for tarefa in TarefaController.buscar_todas_tarefas():
        print(tarefa.titulo, tarefa.completo)

    # Verificando se a lista de tarefas está vazia
    if not TarefaController.buscar_todas_tarefas():
        print("Sem tarefas")

    # Deletando uma tarefa
    TarefaController.apagar_tarefa("Fazer compras")

    # Consultando as tarefas
    for tarefa in TarefaController.buscar_todas_tarefas():
        print(tarefa.titulo, tarefa.completo)

    # Verificando se a lista de tarefas está vazia
    if not TarefaController.buscar_todas_tarefas():
        print("Sem tarefas")
