sabor = int(input("Indique o sabor desejado: "))

#Função fim de semana
def sabor_pizza(sabor):
    match sabor:
        case 1:
            return print("Mussarela")
        case 2:
            return print("Calabresa")
        case 3:
            return print("Frango c/ catupiry")
        case 4:
            return print("Portuguesa")
        case _:
            return print("Sabor inválido!")
        
        
# Exibe o resultado 
sabor_pizza(sabor)