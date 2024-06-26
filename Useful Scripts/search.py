import tkinter as tk
from tkinter import messagebox

def pesquisar_email():
    # Obter o valor do campo de e-mail
    email = entry_email.get()

    # Aqui voc� pode chamar a fun��o que pesquisa o e-mail no outro site
    # Substitua o c�digo abaixo com a chamada real � sua fun��o de pesquisa
    # Exemplo fict�cio:
    resultado_pesquisa = pesquisar_no_outro_site(email)

    # Exibir resultado em uma caixa de mensagem
    messagebox.showinfo("Resultado da Pesquisa", resultado_pesquisa)

def pesquisar_no_outro_site(email):
    # Substitua este c�digo fict�cio pela l�gica real de pesquisa no seu site
    # Aqui voc� pode usar bibliotecas como requests para interagir com a web
    # Exemplo fict�cio:
    resultado = f"Realizando pesquisa para o e-mail: {email}"
    return resultado

# Criar a janela principal
janela = tk.Tk()
janela.title("Pesquisa de E-mail")

# Criar e posicionar os widgets
label_email = tk.Label(janela, text="Digite o e-mail:")
label_email.pack(pady=10)

entry_email = tk.Entry(janela)
entry_email.pack(pady=10)

botao_pesquisar = tk.Button(janela, text="Pesquisar", command=pesquisar_email)
botao_pesquisar.pack(pady=10)

# Iniciar o loop principal da interface gr�fica
janela.mainloop()

