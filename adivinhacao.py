print("**********************************")
print("*Bem vindo ao jogo de adivinhação*")
print("**********************************")

numero_secreto = 22
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Rodada {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite o seu número: ")
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou :)")
        break
    else:
        if(maior):
            print("Você errou! O chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! O chute foi menor que o número secreto")
    rodada = rodada + 1

print("Fim de jogo")