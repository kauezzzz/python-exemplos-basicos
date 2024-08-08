def calcular_comissao(valor_produto, percentual_comissao):
    # Calcula a comissão
    comissao = valor_produto * (percentual_comissao / 100)
    return comissao

# Solicita o valor total das vendas do usuário
valor_produto = float(input("Digite o valor total das vendas: "))

# Solicita a taxa de comissão do usuário
percentual_comissao = float(input("Digite a taxa de comissão (em %): "))

# Calcula a comissão
comissao = calcular_comissao(valor_produto, percentual_comissao)

# Exibe o resultado
print(f"A comissão do vendedor é: R$ {comissao:.2f}")