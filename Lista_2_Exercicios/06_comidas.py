comida = input("Indique a comida escolhida: ")

# Função comida
def menu_de_opções(comida):
    match comida:
        case "1" :
            return "Pizza"
        case "2" :
            return "Salada"
        case "3" :
            return "hambúrguer"
        case _:
            return "Não possui essa opção."

# Exibe o resultado da função na tela
print(menu_de_opções(comida))