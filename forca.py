#Código de @arthurbarcala.
#Por favor não roube :)
import random

#Escolher uma palavra
bancoPalavras = ("instituto", "empresa", "escola", "programação", "python", "linguagem", "computador", "teclado", "pneumoultramicroscopicossilicovulcanoconiótico", "café", "depressão", "suicídio", "morte", "insanidade")
palavra = bancoPalavras[random.randint(0, len(bancoPalavras))]
palavraOculta = []
letrasInvalidas = []
vidas = 6
acertos = 0

#do (isso seria o do/while se tivesse no python)
for yay in range(0, len(palavra)):
    palavraOculta.append("_")
# fazer o usuário inserir uma letra
print(f"vidas: {vidas}, acertos: {acertos}")
print(f"Palavra: {palavraOculta}")
print(f"Letras inválidas: {letrasInvalidas}")
letra = input("Insira uma letra:\n")
# verificar se a letra inserida está na palavra
if letra in palavra and letra not in letrasInvalidas:
    for x in range(0, len(palavra)):
        if palavra[x] == letra:
            palavraOculta[x] = letra
            acertos += 1
    letrasInvalidas.append(letra)
    # Se não estiver, perde uma vida.
elif letra in letrasInvalidas:
    print("Essa letra ja foi!!")
else:
    vidas -= 1
    letrasInvalidas.append(letra)

while vidas > 0 and acertos < len(palavra):
    # fazer o usuário inserir uma letra
    print(f"vidas: {vidas}, acertos: {acertos}")
    print(f"Palavra: {palavraOculta}")
    print(f"Letras inválidas: {letrasInvalidas}")
    letra = input("Insira uma letra:\n")
    # verificar se a letra inserida está na palavra
    if letra in palavra and letra not in letrasInvalidas:
        for x in range(0, len(palavra)):
            if palavra[x] == letra:
                palavraOculta[x] = letra
                acertos += 1
        letrasInvalidas.append(letra)
        # Se não estiver, perde uma vida.
    elif letra in letrasInvalidas:
        print("Essa letra ja foi!!")
    else:
        vidas -= 1
        letrasInvalidas.append(letra)

#Se revelar todas as letras ganha o jogo
if acertos == len(palavra):
    print("Parabéns!! Você acertou a palavra!")
    print(f"A palavra é {palavra}")
if vidas == 0:
    print("Você perdeu!!")
    print(f"A palavra era {palavra}")
#Se perder todas as vidas perde!
