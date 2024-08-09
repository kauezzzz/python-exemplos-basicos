valor = int(input("Informe o valor: "))

# Uso do If ternario
teste = "Situação normal! if" if valor < 100 else "Situação: Pré-diabetes!" if valor in range (100,125) else "Diabetes"

# Exibição
print(teste)