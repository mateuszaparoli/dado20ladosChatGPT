import tkinter as tk
import random

# Função que cria a segunda janela
def nova_janela(prato_sorteado):
    # Cria uma nova janela
    janela = tk.Toplevel(root)
    janela.geometry('500x500')
    
    # Configura a imagem de fundo da janela
    background_image = tk.PhotoImage(file='dragon.png')
    background_label = tk.Label(janela, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    
    # Cria um label com o prato sorteado
    sorteio_label = tk.Label(janela, text=f'O prato sorteado é: {prato_sorteado}', font=('Helvetica', 18))
    sorteio_label.place(relx=0.5, rely=0.1, anchor='center')
    janela.sorteio = sorteio_label
    
    # Cria um botão para sortear na janela
    sortear_button = tk.Button(janela, text='Sortear novamente', command=sortear_prato, relief='solid', borderwidth=3, font=('Helvetica', 16))
    sortear_button.place(relx=0.5, rely=0.5, anchor='center')

# Função para sortear um prato e mostrar na nova janela
def sortear_prato():
    pratos = ['Lasanha', 'Pizza', 'Strogonoff', 'Macarrão', 'Hamburguer', 'Coxinha']
    prato_sorteado = random.choice(pratos)
    nova_janela(prato_sorteado)

# Configurando a janela principal
root = tk.Tk()
root.title('Sorteio')
root.geometry('500x500')

# Configurando a imagem de fundo
background_image = tk.PhotoImage(file='dragon.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Criando o botão para sortear na janela principal
sortear_button = tk.Button(root, text='Sortear', command=sortear_prato, relief='solid', borderwidth=3, font=('Helvetica', 16))
sortear_button.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
