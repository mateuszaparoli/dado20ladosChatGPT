#agr pedir pra colocar o fundo de dragão nas duas telas e pra ter um botão sortear tbm na segunda tela

import tkinter as tk
import random

class SorteioJanela(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Sorteio')
        self.geometry('500x500')

        # Configurando a imagem de fundo
        self.background_image = tk.PhotoImage(file='dragon.png')
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Criando o botão para sortear
        sortear_button = tk.Button(self, text='Sortear', command=self.sortear_prato, relief='solid', borderwidth=3, font=('Helvetica', 16))
        sortear_button.place(relx=0.5, rely=0.5, anchor='center')

    # Lógica para sortear o prato
    def sortear_prato(self):
        pratos = ['Lasanha', 'Pizza', 'Strogonoff', 'Macarrão', 'Hamburguer', 'Coxinha']
        prato_sorteado = random.choice(pratos)
        sorteio_label = tk.Label(self, text=f'O prato sorteado é: {prato_sorteado}', font=('Helvetica', 18))
        sorteio_label.place(relx=0.5, rely=0.5, anchor='center')
        self.sorteio = sorteio_label


class SorteioApp:
    def __init__(self, root):
        self.root = root

        # Configurando a janela principal
        self.root.title('Sorteio')
        self.root.geometry('500x500')

        # Configurando a imagem de fundo
        background_image = tk.PhotoImage(file='dragon.png')
        background_label = tk.Label(self.root, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        # Criando o botão para sortear
        sortear_button = tk.Button(self.root, text='Sortear', command=self.abrir_janela_sorteio, relief='solid', borderwidth=3, font=('Helvetica', 16))
        sortear_button.place(relx=0.5, rely=0.5, anchor='center')

    def abrir_janela_sorteio(self):
        # Abrindo a janela de sorteio
        sorteio_janela = SorteioJanela(self.root)
        sorteio_janela.grab_set()

if __name__ == '__main__':
    root = tk.Tk()
    app = SorteioApp(root)
    root.mainloop()
