# Variáveis
nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))

# Verifica a idade
if idade >=16:
    print(f"Olá. {nome}! Você tem {idade} anos. Então, você pode votar.")
else:
    print(f"Olá. {nome}! Você tem {idade} anos. Então, você não pode votar.")