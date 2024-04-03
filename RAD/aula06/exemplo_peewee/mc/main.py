from controlador import TarefaController

if __name__ == "__main__":
    # Criando as tabelas no banco de dados
    from modelo import db, Tarefa

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
