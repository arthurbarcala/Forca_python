import random

#lista de palavras
palavras = ["ansiedade", "aplaudir", "bumerangue", "orquestra", "grelha", "lobisomem", "tela", "grama", "holanda", "pelicano", "leme", "exceder"]

palavraEscolhida = palavras[random.randint(0, 11)] #sorteia uma palavra da lista
palavraCensurada = "_"*len(palavraEscolhida)
vidas = 6
boneco = " ________\n|		|\n|\n|\n|\n|"
letraAdvinhada = ""
letrasInvalidas = []

print(boneco)
print("--------------------")
print(palavraCensurada)
print("Advinhe uma letra:")
letraAdvinhada = input();

for x in palavraEscolhida:
    cont = 0
    if letraAdvinhada in palavraEscolhida:
        if letraAdvinhada == x:
            cont+=1
            palavraCensurada[cont] = letraAdvinhada
        else:
            cont+=1
    else:
        print("Letra invalida!")
        letrasInvalidas.append(x)
