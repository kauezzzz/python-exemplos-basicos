# Definindo a taxa de câmbio (1 dólar = 0.85 euros)
taxa_de_cambio = 0.85

# Solicita ao usuário o valor em dólares
valor_em_dolar = float(input("Digite o valor em dólares: "))

# Converte para euros
valor_em_euro = valor_em_dolar * taxa_de_cambio

# Exibe o resultado
print(f"{valor_em_dolar} dólares é equivalente a {valor_em_euro:.2f} euros.")