from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Obtendo o caminho completo para o arquivo do banco de dados
banco = os.path.abspath(os.path.join(os.path.dirname(__file__), "tarefas.db"))

# Criando a conexão com o banco de dados
engine = create_engine(f"sqlite:///{banco}", echo=True)

# Criando uma instância base para a definição da classe modelo
Base = declarative_base()


# Definindo a classe do modelo
class Tarefa(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    completo = Column(Boolean)

    def __repr__(self):
        return (
            f"<Tarefa(id={self.id}, titulo='{self.titulo}', completo={self.completo})>"
        )


# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criando uma sessão
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    # Criando uma nova tarefa
    nova_tarefa = Tarefa(titulo="Fazer compras", completo=False)
    session.add(nova_tarefa)
    session.commit()

    # Consultando as tarefas
    tarefas = session.query(Tarefa).all()
    for tarefa in tarefas:
        print(tarefa)

    # Atualizando uma tarefa
    tarefa_atualizada = session.query(Tarefa).filter_by(titulo="Fazer compras").first()
    tarefa_atualizada.completo = True
    session.commit()

    # Consultando as tarefas
    tarefas = session.query(Tarefa).all()
    for tarefa in tarefas:
        print(tarefa)

    # Deletando uma tarefa
    tarefa_para_deletar = (
        session.query(Tarefa).filter_by(titulo="Fazer compras").first()
    )
    session.delete(tarefa_para_deletar)
    session.commit()

    # Consultando as tarefas
    tarefas = session.query(Tarefa).all()
    for tarefa in tarefas:
        print(tarefa)

    # Verificando se a lista de tarefas está vazia
    if not tarefas:
        print("Sem tarefas")
