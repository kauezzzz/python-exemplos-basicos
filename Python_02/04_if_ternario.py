velocidade = int(input("Informe a velocidade: "))

# Uso do If ternário
alerta = "Alta velocidade! Multado." if velocidade > 60 else "Dentro do limite de velocidade."

# Exibição
print(alerta)