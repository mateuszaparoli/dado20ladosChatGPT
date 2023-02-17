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
    if hasattr(root, 'sorteio_label'):
        root.sorteio_label.destroy()  # Apaga o resultado anterior
    sorteio_label = tk.Label(root, text=f'O prato sorteado é: {prato_sorteado}', font=('Helvetica', 18), bg='yellow')
    sorteio_label.place(relx=0.5, rely=0.1, anchor='center')
    root.sorteio_label = sorteio_label  # Salva a referência para apagar o resultado

sortear_button = tk.Button(root, text='Sortear', command=sortear_prato, relief='solid', borderwidth=3, font=('Helvetica', 16))
sortear_button.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
