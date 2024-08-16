# Solicitando ao usuário os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realizando as três somas
soma1 = numero1 + numero2
soma2 = numero1 + 2 * numero2
soma3 = 2 * numero1 + numero2

# Exibindo os resultados das três somas
print(f"Soma 1: {soma1}")
print(f"Soma 2: {soma2}")
print(f"Soma 3: {soma3}")

# Somando os resultados das três somas para o totalizador
totalizador = soma1 + soma2 + soma3

# Exibindo o totalizador
print(f"Total das 3 somas: {totalizador}")