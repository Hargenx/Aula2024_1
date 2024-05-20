import sqlite3


class Model:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS items 
                               (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)"""
        )
        self.conn.commit()

    def insert_item(self, name, quantity):
        self.cursor.execute(
            "INSERT INTO items (name, quantity) VALUES (?, ?)", (name, quantity)
        )
        self.conn.commit()

    def get_all_items(self):
        self.cursor.execute("SELECT * FROM items")
        return self.cursor.fetchall()

    def update_item_quantity(
        self, item_id, quantity
    ):  # Método para atualizar apenas a quantidade do item
        self.cursor.execute(
            "UPDATE items SET quantity=? WHERE id=?", (quantity, item_id)
        )
        self.conn.commit()

    def delete_item(self, item_id):
        self.cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
