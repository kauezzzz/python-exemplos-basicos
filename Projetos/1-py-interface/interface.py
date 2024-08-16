import tkinter as tk

# Função para tranferir texto do input para label
def mostrar_mensagem():
    texto = caixa_texto.get() # Obter o texto da caixa de texto 
    label_resultado.config(text=texto) # Atualiza o texto do label


# Janela principal
janela = tk.Tk()
janela.title("Exemplo de interface")
janela.geometry("400x150")

# Criar uma caixa de texto para entrada
caixa_texto = tk.Entry(janela, width=60)
caixa_texto.pack(pady=10)

# Criar um botão
botao = tk.Button(janela, text= "Mostrar Texto", command=mostrar_mensagem)
botao.pack(pady=5)

# Criar um Rótulo para mostrar o resultado "Label"
label_resultado = tk.Label(janela, text="") 
label_resultado.pack(pady=5)

# Executar a janela principal
janela.mainloop()