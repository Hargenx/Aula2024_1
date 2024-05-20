from model import Model


class Controller:
    def __init__(self):
        self.model = Model(":memory:")

    def add_item(self, name, quantity):
        self.model.insert_item(name, quantity)

    def get_all_items(self):
        return self.model.get_all_items()

    def update_item_quantity(self, item_id, quantity):
        self.model.update_item_quantity(item_id, quantity)

    def delete_item(self, item_id):
        self.model.delete_item(item_id)
