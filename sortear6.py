#conforme o sortear 5 ainda estava dando erro eu mostrei pro GPT o erro e ele reescreveu o código assim:

import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()

# Configura a folha de estilo
style = ttk.Style(root)
style.configure('TButton', borderwidth=5, relief="raised", foreground='black', background='black', font=('Arial', 14))

# Cria o canvas e adiciona a imagem de fundo
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
background_image = tk.PhotoImage(file='dragon.gif')
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Define a função de sorteio
def sortear_prato():
    pratos = ['lasanha', 'pizza', 'hambúrguer', 'sushi', 'churrasco']
    prato_sorteado = random.choice(pratos)
    
    # Fecha a janela do sorteio anterior, se existir
    if hasattr(root, 'sorteio'):
        root.sorteio.destroy()
    
    # Cria a janela do sorteio
    sorteio_window = tk.Toplevel(root)
    sorteio_window.title("Resultado")
    sorteio_window.geometry("200x100")
    
    # Adiciona o rótulo com o prato sorteado
    resultado_label = tk.Label(sorteio_window, text=f"O prato sorteado é: {prato_sorteado}", font=("Arial", 16))
    resultado_label.pack(pady=20)
    
    # Armazena a janela do sorteio atual para ser fechada na próxima vez que o botão for pressionado
    root.sorteio = sorteio_window

# Cria o botão de sorteio
sortear_button = ttk.Button(root, text='Sortear', command=sortear_prato, style='TButton')
sortear_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
