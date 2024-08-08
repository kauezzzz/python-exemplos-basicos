# Texto onde vamos buscar a palavra
texto = "Ontem eu estava estudando Python."

# Palavra a ser buscada
palavra = "Python"

# Encontrar a posição da palavra no texto
posicao = texto.find(palavra)

# Exibir o resultado
if posicao != -1:
    print(f"A palavra '{palavra}' está na posição {posicao} do texto.")
else:
    print(f"A palavra '{palavra}' não foi encontrada no texto.")