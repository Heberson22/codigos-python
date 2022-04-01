import forca
import adivinha2
import random

def escolha():
    print("**********************************")
    print("********Escolha o seu jogo!*******")
    print("**********************************")

    print("(1)Forca (2)Adivinhação")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando forca!")
        forca.jogar()
    elif jogo == 2:
        print("Jogando advinhação!")
        adivinha2.jogar()

if __name__ == "__main__":
    escolha()