from random import randint
comp=randint(1,50)
tentativas=5
print("Digite um numero entre 1 e 50: ")
while tentativas >0:
    jogador=int(input("TENTATIVA: {}/5: Digite seu palpite:".format(6-tentativas)))
    if jogador==comp:
        print("Você acertou!!Eu escolhi {} e você {}".format(comp,jogador))
        break
    elif jogador < comp:
        print("Tente Novamente, o numero é maior!")
    else:
        print("Tente Novamente!O numero é um pouco menor!")
    tentativas-=1
if tentativas==0:
    print("GAME OVER, suas tentativas acabaram!O numero era {}".format(comp))