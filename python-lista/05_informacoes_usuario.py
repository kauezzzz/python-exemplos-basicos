# Função para validar o nome
def validar_nome(nome):
    return len(nome) > 3

# Função para validar a idade
def validar_idade(idade):
    return 0 <= idade <= 100

# Função para validar o salário
def validar_salario(salario):
    return salario > 0

# Função para validar o sexo
def validar_sexo(sexo):
    return sexo in ['f', 'm']

# Função para validar o estado civil
def validar_estado_civil(estado_civil):
    return estado_civil in ['s', 'c', 'v', 'd']

# Solicitação e validação do nome
while True:
    nome = input("Digite seu nome (mais que 3 caracteres): ")
    if validar_nome(nome):
        break
    print("Nome inválido! Tente novamente.")

# Solicitação e validação da idade
while True:
    idade = int(input("Digite sua idade (entre 0 e 100): "))
    if validar_idade(idade):
        break
    print("Idade inválida! Tente novamente.")

# Solicitação e validação do salário
while True:
    salario = float(input("Digite seu salário (maior que zero): "))
    if validar_salario(salario):
        break
    print("Salário inválido! Tente novamente.")

# Solicitação e validação do sexo
while True:
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()
    if validar_sexo(sexo):
        break
    print("Sexo inválido! Tente novamente.")

# Solicitação e validação do estado civil
while True:
    estado_civil = input("Digite seu estado civil ('s' para solteiro(a), 'c' para casado(a), 'v' para viúvo(a), 'd' para divorciado(a)): ").lower()
    if validar_estado_civil(estado_civil):
        break
    print("Estado civil inválido! Tente novamente.")

# Exibição das informações válidas
print("\nInformações Validadas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
print(f"Estado Civil: {estado_civil.upper()}")