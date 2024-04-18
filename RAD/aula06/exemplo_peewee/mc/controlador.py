from modelo import Tarefa


class TarefaController:
    @staticmethod
    def criar_tarefa(titulo, completo):
        return Tarefa.create(titulo=titulo, completo=completo)

    @staticmethod
    def buscar_todas_tarefas():
        return Tarefa.select()

    @staticmethod
    def buscar_tarefa_por_titulo(titulo):
        return Tarefa.get(Tarefa.titulo == titulo)

    @staticmethod
    def atualizar_tarefa(titulo, completo):
        tarefa = Tarefa.get(Tarefa.titulo == titulo)
        tarefa.completo = completo
        tarefa.save()

    @staticmethod
    def apagar_tarefa(titulo):
        tarefa = Tarefa.get(Tarefa.titulo == titulo)
        tarefa.delete_instance()
