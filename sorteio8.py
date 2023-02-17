#agr pedi pra ele juntar td num  codigo final:

import tkinter as tk
import random

def open_result_window():
    result_window = tk.Toplevel()
    result_window.geometry('500x500')
    result_window.title('Resultado do Sorteio')
    result_window.configure(background='gray')

    # Configurando o label com o resultado do sorteio
    pratos = ['Lasanha', 'Pizza', 'Strogonoff', 'Macarrão', 'Hamburguer', 'Coxinha']
    prato_sorteado = random.choice(pratos)
    sorteio_label = tk.Label(result_window, text=f'O prato sorteado é: {prato_sorteado}', font=('Helvetica', 18))
    sorteio_label.pack(pady=100)

    def close_result_window():
        result_window.destroy()

    # Configurando o botão de fechar a janela
    ok_button = tk.Button(result_window, text='OK', command=close_result_window, font=('Helvetica', 16))
    ok_button.pack(pady=20)

    result_window.protocol("WM_DELETE_WINDOW", close_result_window)

root = tk.Tk()

# Configurando a janela principal
root.title('Sorteio')
root.geometry('500x500')

# Configurando a imagem de fundo
background_image = tk.PhotoImage(file='dragon.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Criando o botão para sortear
sortear_button = tk.Button(root, text='Sortear', command=open_result_window, relief='solid', borderwidth=3, font=('Helvetica', 16))
sortear_button.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
