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
def sortear_numero():
    numero_sorteado = random.randint(1, 20)
    historico.append(numero_sorteado)
    if hasattr(root, 'sorteio_label'):
        root.sorteio_label.pack_forget()
    sorteio_label = tk.Label(root, text=f'O número sorteado é: {numero_sorteado}', font=('Helvetica', 18))
    sorteio_label.pack()
    root.sorteio_label = sorteio_label

sortear_button = tk.Button(root, text='Sortear', command=sortear_numero, relief='solid', borderwidth=3, font=('Helvetica', 16))
sortear_button.place(relx=0.5, rely=0.5, anchor='center')

historico = []

def exibir_historico():
    historico_str = '\n'.join(str(n) for n in historico)
    historico_label = tk.Label(root, text=historico_str, font=('Helvetica', 16))
    historico_label.pack()
    root.historico = historico_label

historico_button = tk.Button(root, text='Exibir histórico', command=exibir_historico, relief='solid', borderwidth=3, font=('Helvetica', 16))
historico_button.place(relx=0.5, rely=0.8, anchor='center')

root.mainloop()
