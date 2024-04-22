import mysql.connector


class Database:
    def __init__(self, host, user, password, database):
        try:
            self.conn = mysql.connector.connect(host=host, user=user, password=password)
            self.cursor = self.conn.cursor()
            self.create_database(database)
            self.conn.database = database
            self.create_table()
        except mysql.connector.Error as e:
            print("Erro na conexão com o banco de dados:", e)

    def create_database(self, database):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            print(f"Banco de dados '{database}' criado com sucesso.")
        except mysql.connector.Error as e:
            print("Erro na criação do banco de dados: ", e)

    def create_table(self):
        try:
            self.cursor.execute(
                """
                                CREATE TABLE IF NOT EXISTS usuarios (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                idade INT)
                                """
            )
            self.conn.commit()
        except mysql.connector.Error as e:
            print("Erro na criação da tabela: ", e)

    def close(self):
        try:
            self.conn.close()
        except mysql.connector.Error as e:
            print("Erro ao fechar a conexão com o banco de dados:", e)

    def insert_usuario(self, idade):
        try:
            self.cursor.execute("INSERT INTO usuarios (idade) VALUES (%s)", (idade,))
            self.conn.commit()
            print("Usuário inserido com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao inserir usuário:", e)

    def get_usuarios(self):
        try:
            self.cursor.execute("SELECT * FROM usuarios")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except mysql.connector.Error as e:
            print("Erro ao buscar usuários:", e)

    def update_usuario(self, id, idade):
        try:
            self.cursor.execute("UPDATE usuarios SET idade=%s WHERE id=%s", (idade, id))
            self.conn.commit()
            print("Usuário atualizado com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao atualizar usuário:", e)

    def delete_usuario(self, id):
        try:
            self.cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
            self.conn.commit()
            print("Usuário deletado com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao deletar usuário:", e)


# Exemplo de uso
db = Database(
    host="localhost",
    user="root",
    password="",
    database="banco.db",
)

# Inserir um usuário
db.insert_usuario(25)

# Listar todos os usuários
db.get_usuarios()

# Atualizar um usuário
db.update_usuario(1, 30)

# Deletar um usuário
db.delete_usuario(1)

# Fechar conexão com o banco de dados
db.close()
