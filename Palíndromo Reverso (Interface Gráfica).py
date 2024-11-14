import tkinter as tk
from tkinter import messagebox

def verificar_palindromo():
    palavra = entrada.get()
    palavra_min = palavra.lower()
    palavra_invertida = palavra_min[::-1]

    if palavra_min == palavra_invertida:
        resultado = "A palavra é palíndromo."
    else:
        resultado = "A palavra não é palíndromo."

    # Exibir a mensagem com o resultado
    messagebox.showinfo("Resultado", f"{resultado}\n\nSua palavra: {palavra}\nInversão: {palavra_invertida}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Verificador de Palíndromo")
janela.geometry("400x300")
janela.configure(bg="#f0f8ff")

# Estilizando a fonte
fonte_titulo = ("Helvetica", 16, "bold")
fonte_texto = ("Helvetica", 12)

# Criar título
titulo = tk.Label(janela, text="Verificador de Palíndromo", bg="#f0f8ff", font=fonte_titulo, fg="#2e8b57")
titulo.pack(pady=20)

# Criar campo de entrada
entrada = tk.Entry(janela, font=fonte_texto, width=30)
entrada.pack(pady=10)

# Criar botão para verificar
botao_verificar = tk.Button(janela, text="Verificar", command=verificar_palindromo, bg="#3cb371", fg="white", font=fonte_texto)
botao_verificar.pack(pady=20)

# Executar a aplicação
janela.mainloop()
