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

    def deletar(self):
        self.delete_instance()


if __name__ == "__main__":
    # Criando as tabelas no banco de dados
    db.connect()
    db.create_tables([Tarefa])

    # Criando uma nova tarefa
    nova_tarefa = Tarefa.criar("Fazer compras", False)

    # Consultando as tarefas
    for tarefa in Tarefa.buscar_todos():
        print(tarefa.titulo, tarefa.completo)

    # Verificando se a lista de tarefas está vazia
    if not Tarefa.buscar_todos().exists():
        print("Sem tarefas")

    # Atualizando uma tarefa
    tarefa_atualizada = Tarefa.buscar_por_titulo("Fazer compras")
    tarefa_atualizada.atualizar(True)

    # Consultando as tarefas
    for tarefa in Tarefa.buscar_todos():
        print(tarefa.titulo, tarefa.completo)

    # Verificando se a lista de tarefas está vazia
    if not Tarefa.buscar_todos().exists():
        print("Sem tarefas")

    # Deletando uma tarefa
    tarefa_para_deletar = Tarefa.buscar_por_titulo("Fazer compras")
    tarefa_para_deletar.deletar()

    # Consultando as tarefas
    for tarefa in Tarefa.buscar_todos():
        print(tarefa.titulo, tarefa.completo)

    # Verificando se a lista de tarefas está vazia
    if not Tarefa.buscar_todos().exists():
        print("Sem tarefas")
