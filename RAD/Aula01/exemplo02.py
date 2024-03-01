from dataclasses import dataclass
@dataclass
class Task:
    titulo: str
    descricao: str
    concluida: bool = False
class TaskManager:
    def __init__(self):
        self.tasks = []
    def adicionar_tarefa(self, task):
        self.tasks.append(task)
    def listar_tarefas(self):
        for task in self.tasks:
            status = "Concluída" if task.concluida else "Pendente"
            print(f"Título: {task.titulo}, Descrição: {task.descricao}, Status: {status}")

    def marcar_concluida(self, titulo):
        for task in self.tasks:
            if task.titulo == titulo:
                task.concluida = True
                print(f"Tarefa '{task.titulo}' marcada como concluída.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.adicionar_tarefa(Task("Fazer compras", "Comprar leite e pão"))
    task_manager.adicionar_tarefa(Task("Estudar Python", "Resolver exercícios"))
    task_manager.listar_tarefas()
    task_manager.marcar_concluida("Fazer compras")
    task_manager.listar_tarefas()
