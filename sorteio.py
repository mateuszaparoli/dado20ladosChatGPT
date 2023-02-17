import tkinter as tk
import random

# Definindo a lista de pratos brasileiros
pratos = ['Feijoada', 'Churrasco', 'Acarajé', 'Moqueca', 'Pão de queijo', 'Coxinha', 'Empadão', 'Pastel']

# Função que escolhe um prato aleatório da lista e mostra em uma nova janela
def sortear_prato():
    prato_sorteado = random.choice(pratos)
    nova_janela = tk.Toplevel(root)
    nova_janela.title('Prato sorteado')
    tk.Label(nova_janela, text='O prato sorteado é:').pack()
    tk.Label(nova_janela, text=prato_sorteado).pack()
    tk.Button(nova_janela, text='Sortear novamente', command=sortear_prato).pack(pady=10)
    tk.Button(nova_janela, text='Voltar para a tela inicial', command=nova_janela.destroy).pack(pady=10)
    tk.Button(nova_janela, text='Encerrar o programa', command=root.quit).pack(pady=10)

# Criando a janela principal
root = tk.Tk()
root.title('Sorteio de pratos brasileiros')

# Criando o botão na janela principal
botao_sortear = tk.Button(root, text='Sortear', command=sortear_prato)
botao_sortear.pack(pady=10)

# Iniciando a janela principal
root.mainloop()