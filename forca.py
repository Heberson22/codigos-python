import random

def jogar():

    print("**********************************")
    print("****Bem vindo ao jogo de forca****")
    print("**********************************")

    arquivo = open("palavra.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        tentativas = 5

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                    print("Letra {} na posição {}".format(letra, index))
                    print("Ainda faltam {} letras".format(str(letras_acertadas.count("_"))))
                index += 1
        else:
            erros += 1
            tentativas -= erros
            print("Letra errada, você tem mais {} tentativas".format(tentativas))

        enforcou = erros == 5
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você Ganhou!!!")
    else:
        print("Você perdeu :(")
    print("Fim de jogo!")

if __name__ == "__main__":
    jogar()