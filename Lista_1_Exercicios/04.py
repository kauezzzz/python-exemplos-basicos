# Solicita as quatro notas do usuário e armazena em uma lista
notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(4)]

# Calcula a média das notas
media = sum(notas) / 4

# Exibe o resultado
print(f"A média das quatro notas é: {media:.2f}")