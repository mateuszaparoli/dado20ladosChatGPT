import tkinter as tk
import random

root = tk.Tk()
historico = []

# Configurando a janela principal
root.title('D20')
root.geometry('500x500')

# Configurando a imagem de fundo
background_image = tk.PhotoImage(file='dragon.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Criando o botão para sortear
def sortear_numero():
    numero_sorteado = random.randint(1, 20)
    historico.append(numero_sorteado)
    resultado_label['text'] = f'O número sorteado é: {numero_sorteado}'

# Criando o botão para exibir o histórico
def abrir_historico():
    historico_window = tk.Toplevel(root)
    historico_window.title('Histórico de Sorteios')
    historico_window.geometry('200x200')
    historico_label = tk.Label(historico_window, text='\n'.join(map(str, historico)))
    historico_label.pack()

sortear_button = tk.Button(root, text='Sortear', command=sortear_numero, relief='solid', borderwidth=3, font=('Helvetica', 16))
sortear_button.place(relx=0.5, rely=0.5, anchor='center')

historico_button = tk.Button(root, text='Histórico', command=abrir_historico, relief='solid', borderwidth=3, font=('Helvetica', 16))
historico_button.place(relx=0.5, rely=0.6, anchor='center')

resultado_label = tk.Label(root, text='', font=('Helvetica', 18))
resultado_label.place(relx=0.5, rely=0.3, anchor='center')

root.mainloop()
