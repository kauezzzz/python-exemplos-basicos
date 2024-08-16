# Função para exibir o menu e solicitar uma escolha válida
def mostrar_menu():
    print("Escolha uma das opções:")
    print("1 - Eu programo em Python")
    print("2 - Eu programo em PHP")
    print("3 - Eu programo em Java")

# Laço infinito para garantir que o usuário escolha uma opção válida
while True:
    mostrar_menu()
    opcao = input("Digite o número da sua escolha: ")

    if opcao == '1':
        print("Eu estou estudando Python!")
        break
    elif opcao == '2':
        print("Eu estou estudando PHP!")
        break
    elif opcao == '3':
        print("Eu estou estudando Java!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma das opções 1, 2 ou 3.\n")