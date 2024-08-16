# Exibindo o cabeçalho das colunas
print("Nro\tQuad\tCubo")

# Calculando e exibindo os quadrados e cubos para números de 0 a 50
for numero in range(51):
    quadrado = numero ** 2
    cubo = numero ** 3
    print(f"{numero}\t{quadrado}\t{cubo}")