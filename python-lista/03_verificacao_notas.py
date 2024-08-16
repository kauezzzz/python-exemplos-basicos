# Função para verificar se uma nota é válida
def nota_valida(nota):
    return 0 <= nota <= 10

# Lista para armazenar as notas
notas = []

# Coletando as 4 notas
for i in range(1, 5):
    nota = float(input(f"Digite a nota {i} (entre 0 e 10): "))
    
    if nota_valida(nota):
        notas.append(nota)
    else:
        print(f"Nota {i} inválida! Por favor, insira um valor entre 0 e 10.")
        break
else:
    # Se todas as notas forem válidas, calcula a média
    media = sum(notas) / len(notas)
    print(f"A média final é: {media:.2f}")