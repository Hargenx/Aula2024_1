import tkinter as tk
from tkinter import messagebox
from controller import Controller


class View:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD com Tkinter e SQLite")
        self.root.geometry("380x330") 
        self.root.resizable(False, False) 

        self.controller = Controller()

        # Centralizando a janela
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        position_right = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.root.winfo_screenheight() / 2 - window_height / 2)
        self.root.geometry("+{}+{}".format(position_right, position_down))

        # Estilizando os widgets
        self.root.configure(bg="#f0f0f0")
        self.label_font = ("Helvetica", 12)
        self.entry_font = ("Helvetica", 11)
        self.button_font = ("Helvetica", 11, "bold")

        # Criando os widgets
        self.name_label = tk.Label(
            root, text="Nome:", font=self.label_font, bg="#f0f0f0"
        )
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(root, font=self.entry_font)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.quantity_label = tk.Label(
            root, text="Quantidade:", font=self.label_font, bg="#f0f0f0"
        )
        self.quantity_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.quantity_entry = tk.Entry(root, font=self.entry_font)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = tk.Button(
            root, text="Adicionar", font=self.button_font, command=self.add_item
        )
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.items_listbox = tk.Listbox(root, font=self.entry_font, width=40, height=8)
        self.items_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        self.items_listbox.bind(
            "<<ListboxSelect>>", self.select_item
        )  # Adicionando evento de seleção de item

        self.update_button = tk.Button(
            root, text="Atualizar", font=self.button_font, command=self.update_item
        )
        self.update_button.grid(row=4, column=0, pady=10)

        self.delete_button = tk.Button(
            root, text="Deletar", font=self.button_font, command=self.delete_item
        )
        self.delete_button.grid(row=4, column=1, pady=10)

        self.refresh_list()

    def add_item(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        if name and quantity:
            self.controller.add_item(name, quantity)
            self.refresh_list()
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")
            self.name_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def refresh_list(self):
        self.items_listbox.delete(0, tk.END)
        items = self.controller.get_all_items()
        for item in items:
            self.items_listbox.insert(tk.END, f"{item[0]} - {item[1]} ({item[2]})")

    def select_item(self, event):
        selected_item = self.items_listbox.curselection()
        if selected_item:
            item = self.items_listbox.get(selected_item[0])
            item_id, name, quantity = (
                item.split()[0],
                " ".join(item.split()[1:-2]),
                item.split()[-1][1:-1],
            )
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, name)
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(tk.END, quantity)

    def update_item(self):
        selected_item = self.items_listbox.curselection()
        if selected_item:
            item_id = self.items_listbox.get(selected_item[0]).split()[0]
            quantity = self.quantity_entry.get()
            if quantity:
                self.controller.update_item_quantity(item_id, quantity)
                self.refresh_list()
                messagebox.showinfo("Sucesso", "Quantidade atualizada com sucesso!")
                self.quantity_entry.delete(0, tk.END)
                self.name_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Por favor, preencha o campo de quantidade.")
        else:
            # Verificando se a quantidade foi alterada mesmo sem um item selecionado
            if self.quantity_entry.get():
                messagebox.showerror("Erro", "Por favor, selecione um item para atualizar.")
            else:
                messagebox.showerror("Erro", "Por favor, preencha o campo de quantidade.")

    def delete_item(self):
        selected_item = self.items_listbox.curselection()
        if selected_item:
            item_id = self.items_listbox.get(selected_item[0]).split()[0]
            self.controller.delete_item(item_id)
            self.refresh_list()
            messagebox.showinfo("Sucesso", "Item deletado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, selecione um item para deletar.")


if __name__ == "__main__":
    root = tk.Tk()
    view = View(root)
    root.mainloop()
