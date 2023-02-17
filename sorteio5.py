# COLOQUEI NO CHATGPT O ERRO QUE ESTAVA ACONTERCENDO E ELE DISSE QUE VAI CONCERTAR, VAMOS VER NO QUE DA
# Eu disse que ainda deu erro,  mostrei o erro e ele disse para instalar o pil pra suportar a imagem em jpg
#já q o tinkter n suporta esse tipo de arquivo

import tkinter as tk
from tkinter import ttk
import random
from PIL import ImageTk, Image

# Inicializando a janela principal
root = tk.Tk()
root.geometry('600x400')
root.title('Sorteio de pratos brasileiros')
root.configure(background='white')
root.sorteio = None

# Definindo a lista de pratos brasileiros
pratos = ['Feijoada', 'Churrasco', 'Acarajé', 'Moqueca', 'Pão de queijo', 'Coxinha', 'Empadão', 'Pastel']

# Função que escolhe um prato aleatório da lista e mostra em uma nova janela
def sortear_prato():
    # Destruir janela anterior
    if root.sorteio is not None:
        root.sorteio.destroy()
    
    # Sortear novo prato
    prato_sorteado = random.choice(pratos)
    
    # Criar nova janela
    nova_janela = tk.Toplevel(root)
    nova_janela.title('Prato sorteado')
    nova_janela.geometry('300x300')
    nova_janela.configure(background='black')
    
    # Estilo da nova janela
    style = ttk.Style(nova_janela)
    style.configure('TLabel', foreground='white', background='black', font=('Helvetica', 16))
    style.configure('TButton', foreground='white', background='gray', font=('Helvetica', 12), borderwidth=0, relief='flat')
    
    # Label com o prato sorteado
    tk.Label(nova_janela, text='O prato sorteado é:', background='black').pack(pady=10)
    tk.Label(nova_janela, text=prato_sorteado, background='black').pack(pady=10)
    
    # Botão "Sortear novamente"
    tk.Button(nova_janela, text='Sortear novamente', command=sortear_prato, style='TButton').pack(pady=10)
    
    # Botão "Voltar para a tela inicial"
    tk.Button(nova_janela, text='Voltar para a tela inicial', command=nova_janela.destroy, style='TButton').pack(pady=10)
    
    # Botão "Encerrar o programa"
    tk.Button(nova_janela, text='Encerrar o programa', command=root.quit, style='TButton').pack(pady=10)
    
    # Salvar referência para a nova janela
    root.sorteio = nova_janela

# Estilo da janela principal
style = ttk.Style(root)
style.configure('TLabel', foreground='black', background='white', font=('Helvetica', 20))
style.configure('TButton', foreground='white', background='gray', font=('Helvetica', 16), borderwidth=0, relief='flat')

# Label com imagem de fundo
image = Image.open("dragon.jpg")
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Botão "Sortear"
sortear_button = tk.Button(root, text='Sortear', command=sortear_prato, style='TButton')
sortear_button.place(relx=0.5, rely=0.5, anchor='center')

# Iniciar a janela principal
root.mainloop()
