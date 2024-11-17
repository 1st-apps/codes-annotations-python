import random as r

palavra = "Python e muito bom"

#Gera um índice aleatório dentro do tamanho da palavra
indiceEscolhido = r.randrange(len(palavra))

#Acessa a letra correspondente ao índice
letraEscolhida = palavra[indiceEscolhido]

print(palavra[0:4]) #Imprimir do [0] até a posição [4] - [Pyth]
print(f"Letra escolhida da palavra: {palavra} : {letraEscolhida}") 