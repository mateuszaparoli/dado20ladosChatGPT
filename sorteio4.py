import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random

# Definindo a lista de pratos brasileiros
pratos = ['Feijoada', 'Churrasco', 'Acarajé', 'Moqueca', 'Pão de queijo', 'Coxinha', 'Empadão', 'Pastel']

# Função que escolhe um prato aleatório da lista e mostra em uma nova janela
def sortear_prato():
    # Destruir janela anterior
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
    style.configure('TButton', foreground='white', background='gray', font=('Helvetica', 12))
    
    # Label com o prato sorteado
    tk.Label(nova_janela, text='O prato sorteado é:', background='black').pack(pady=10)
    tk.Label(nova_janela, text=prato_sorteado, background='black').pack(pady=10)
    
    # Botão "Sortear novamente"
    tk.Button(nova_janela, text='Sortear novamente', command=sortear_prato).pack(pady=10)
    
    # Botão "Voltar para a tela inicial"
    tk.Button(nova_janela, text='Voltar para a tela inicial', command=nova_janela.destroy).pack(pady=10)
    
    # Botão "Encerrar o programa"
    tk.Button(nova_janela, text='Encerrar o programa', command=root.quit).pack(pady=10)
    
    # Salvar referência para a nova janela
    root.sorteio = nova_janela

# Criando a janela principal
root = tk.Tk()
root.geometry('600x400')
root.title('Sorteio de pratos brasileiros')

# Criar canvas e inserir imagem do dragão
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()
img = ImageTk.PhotoImage(Image.open('dragon.jpg'))
canvas.create_image(0, 0, anchor='nw', image=img)

# Estilo da janela principal
style = ttk.Style(root)
style.theme_use('clam')

# Novo estilo para o botão
style.configure('Meu.TButton', foreground='black', background='white', font=('Helvetica', 14), borderwidth=0, relief='flat', borderradius=10)

# Criando o botão na janela principal
botao_sortear = ttk.Button(root, text='Sortear', command=sortear_prato, style='Meu.TButton')
botao_sortear.place(relx=0.5, rely=0.5, anchor='center')

# Iniciando a janela principal
root.mainloop()