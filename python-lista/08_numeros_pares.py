# Inicializando a lista com valores de 1 a 10
numeros = list(range(1, 11))

# Exibindo apenas os números pares
print("Números pares:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)