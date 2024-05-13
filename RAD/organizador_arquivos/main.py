import os
import shutil
import tkinter as tk
from tkinter import filedialog


def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    if diretorio:
        organizar_arquivos(diretorio)


def organizar_arquivos(diretorio):
    # Percorre o diretório especificado
    for root, _, files in os.walk(diretorio):
        for file in files:
            # Obtém a extensão do arquivo
            _, extensao = os.path.splitext(file)
            extensao = extensao.lower()  # Converte para minúsculas para consistência

            # Cria a pasta correspondente se ainda não existir
            pasta_destino = os.path.join(diretorio, extensao[1:])
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            # Move o arquivo para a pasta correspondente
            shutil.move(os.path.join(root, file), os.path.join(pasta_destino, file))


if __name__ == "__main__":
    # Cria a janela principal
    root = tk.Tk()
    root.title("Organizador de Arquivos")

    # Botão para selecionar o diretório
    btn_selecionar = tk.Button(
        root, text="Selecionar Diretório", command=selecionar_diretorio
    )
    btn_selecionar.pack(pady=20)

    # Executa o loop principal da interface gráfica
    root.mainloop()
