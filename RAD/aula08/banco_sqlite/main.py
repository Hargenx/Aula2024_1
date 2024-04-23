import sqlite3

class Database:
    def __init__(self, nome_bd):
        try:
            self.conn = sqlite3.connect(nome_bd)
            self.cursor = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print("Erro na conexão com o banco de dados:", e)

    def create_table(self):
        try:
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                idade INTEGER)
                                ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print("Erro na criação da tabela: ", e)

    def close(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print("Erro ao fechar a conexão com o banco de dados:", e)

    def insert_usuario(self, idade):
        try:
            self.cursor.execute("INSERT INTO usuarios (idade) VALUES (?)", (idade,))
            self.conn.commit()
            print("Usuário inserido com sucesso.")
        except sqlite3.Error as e:
            print("Erro ao inserir usuário:", e)

    def get_usuarios(self):
        try:
            self.cursor.execute("SELECT * FROM usuarios")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print("Erro ao buscar usuários:", e)

    def update_usuario(self, id, idade):
        try:
            self.cursor.execute("UPDATE usuarios SET idade=? WHERE id=?", (idade, id))
            self.conn.commit()
            print("Usuário atualizado com sucesso.")
        except sqlite3.Error as e:
            print("Erro ao atualizar usuário:", e)

    def delete_usuario(self, id):
        try:
            self.cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
            self.conn.commit()
            print("Usuário deletado com sucesso.")
        except sqlite3.Error as e:
            print("Erro ao deletar usuário:", e)

# Exemplo de uso
db = Database('./banco.sqlite')

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
