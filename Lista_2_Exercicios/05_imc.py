# Solicita ao usuário seu peso e altura
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Classifica o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Exibe a classificação
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}.")