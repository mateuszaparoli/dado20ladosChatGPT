import tkinter as tk
import random

root = tk.Tk()

# Configurando a janela principal
root.title('Sorteio')
root.geometry('500x500')

# Configurando a imagem de fundo
background_image = tk.PhotoImage(file='dragon.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Criando o botão para sortear
def sortear_prato():
    pratos = ['Lasanha', 'Pizza', 'Strogonoff', 'Macarrão', 'Hamburguer', 'Coxinha']
    prato_sorteado = random.choice(pratos)
    sorteio_label = tk.Label(root, text=f'O prato sorteado é: {prato_sorteado}', font=('Helvetica', 18))
    sorteio_label.place(relx=0.5, rely=0.1, anchor='center')
    root.sorteio = sorteio_label

sortear_button = tk.Button(root, text='Sortear', command=sortear_prato, relief='solid', borderwidth=3, font=('Helvetica', 16))
sortear_button.place(relx=0.5, rely=0.5, anchor='center')

# Criando a segunda janela
def nova_janela():
    top = tk.Toplevel()
    top.title('Sorteio')
    top.geometry('500x500')

    # Configurando a imagem de fundo
    background_image = tk.PhotoImage(file='dragon.png')
    background_label = tk.Label(top, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Criando o botão para sortear na segunda janela
    def sortear_prato2():
        pratos = ['Lasanha', 'Pizza', 'Strogonoff', 'Macarrão', 'Hamburguer', 'Coxinha']
        prato_sorteado = random.choice(pratos)
        sorteio_label = tk.Label(top, text=f'O prato sorteado é: {prato_sorteado}', font=('Helvetica', 18))
        sorteio_label.place(relx=0.5, rely=0.1, anchor='center')
        top.sorteio = sorteio_label

    sortear_button2 = tk.Button(top, text='Sortear', command=sortear_prato2, relief='solid', borderwidth=3, font=('Helvetica', 16))
    sortear_button2.place(relx=0.5, rely=0.5, anchor='center')

nova_janela_button = tk.Button(root, text='Nova Janela', command=nova_janela, relief='solid', borderwidth=3, font=('Helvetica', 16))
nova_janela_button.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop()
