import tkinter as tk
from tkinter import messagebox

def pesquisar_email():
    # Obter o valor do campo de e-mail
    email = entry_email.get()

    # Aqui você pode chamar a função que pesquisa o e-mail no outro site
    # Substitua o código abaixo com a chamada real à sua função de pesquisa
    # Exemplo fictício:
    resultado_pesquisa = pesquisar_no_outro_site(email)

    # Exibir resultado em uma caixa de mensagem
    messagebox.showinfo("Resultado da Pesquisa", resultado_pesquisa)

def pesquisar_no_outro_site(email):
    # Substitua este código fictício pela lógica real de pesquisa no seu site
    # Aqui você pode usar bibliotecas como requests para interagir com a web
    # Exemplo fictício:
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

# Iniciar o loop principal da interface gráfica
janela.mainloop()

