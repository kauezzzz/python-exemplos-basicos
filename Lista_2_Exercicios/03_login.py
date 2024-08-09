# Solicita ao usuário o nome de usuário
nome_usuario = input("Digite o nome de usuário: ")

# Solicita ao usuário a senha
senha = input("Digite a senha: ")

# Verifica se o nome de usuário e a senha são corretos
if nome_usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")