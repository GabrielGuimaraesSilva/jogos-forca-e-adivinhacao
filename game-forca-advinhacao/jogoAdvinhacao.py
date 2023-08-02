import random


def jogar_Advinhacao():
    print("******************************************")
    print("*****BEM VINDO AO JOGO DE ADIVINHAÇÃO*****")
    print("******************************************")

    pontos = 0  # Inicializa a pontuação do jogador
    continuar = 0  # Decisão se o jogador quer continuar

    while True:
        total_tentativas = 0  # Iniciando a variavel do número de tentativas do jogador

        nivel = int(
            input("Escolha o nível do jogo: 1-Fácil | 2-Médio | 3-Difícil\n")
        )  # Jogador escolhendo o nível do jogo

        if (
            nivel == 1
        ):  # Se nível fácil, o jogador tem 20 tentativas para acertar um número de entre 1 e 10
            total_tentativas = 20
            numero_secreto = random.randrange(1, 11)
        elif nivel == 2:
            total_tentativas = 10  # Se nível médio, o jogador tem 10 tentativas para acertar um número de entre 1 e 50
            numero_secreto = random.randrange(1, 51)
        else:
            total_tentativas = 5  # Se nível difícil, o jogador tem 5 tentativas para acertar um número de entre 1 e 100
            numero_secreto = random.randrange(1, 101)

        for rodada in range(
            1, total_tentativas + 1
        ):  # Começa a rodada que vai percorrer de 1 até o máximo de tentativas escolhida de acordo com o jogador
            print(f"Tentativa {rodada} de {total_tentativas}")

            if nivel == 1:  # Se jogador escolheu o fácil
                chute_jogador = input(
                    "Digite um número entre 1 e 10 para adivinhar: \n"
                )
            elif nivel == 2:  # Se jogador escolheu o médio
                chute_jogador = input(
                    "Digite um número entre 1 e 50 para adivinhar: \n"
                )
            else:  # Se não vai o difícil
                chute_jogador = input(
                    "Digite um número entre 1 e 100 para adivinhar: \n"
                )

            chute = int(
                chute_jogador
            )  # Convertendo o número que o jogador digitou para um inteiro

            if chute < 1 or chute > (
                10 if nivel == 1 else (50 if nivel == 2 else 100)
            ):  # Verifica se o que o jogador digitou não está ultrapassando o intervalo entre os valores de acordo com a dificuldade escolhida
                print(
                    f"Você deve digitar um número entre 1 e {(10 if nivel == 1 else (50 if nivel == 2 else 100))}\n"
                )
                continue

            acertou = chute == numero_secreto  # Variavel caso o jogador acertou
            maior = chute > numero_secreto  # Variavel de dica
            menor = chute < numero_secreto  # Variavel de dica

            if acertou and nivel == 1:
                print(
                    f"Parabéns você acertou o número secreto que é {numero_secreto}\n"
                )
                pontos += 50  # Adiciona 50 pontos ao acertar o número no nível fácil
                break
            elif acertou and nivel == 2:
                print(
                    f"Parabéns você acertou o número secreto que é {numero_secreto}\n"
                )
                pontos += 100  # Adiciona 100 pontos ao acertar o número no nível médio
                break
            elif acertou and nivel != 1 and nivel != 2:
                print(
                    f"Parabéns você acertou o número secreto que é {numero_secreto}\n"
                )
                pontos += (
                    150  # Adiciona 150 pontos ao acertar o número no nível difícil
                )
                break

            else:
                if maior:
                    print("O número que você chutou é MAIOR que o número secreto\n")
                elif menor:
                    print("O número que você chutou é MENOR que o número secreto\n")

        if acertou and nivel == 1:
            print(
                "Você ganhou 50 pontos, agora você tem o total de {} pontos\n".format(
                    pontos
                )
            )
        elif acertou and nivel == 2:
            print(
                "Você ganhou 100 pontos, agora você tem o total de {} pontos\n".format(
                    pontos
                )
            )
        elif acertou and nivel != 1 and nivel != 2:
            print(
                "Você ganhou 150 pontos, agora você tem o total de {} pontos\n".format(
                    pontos
                )
            )
        else:
            pontos -= 50  # Subtrai 50 pontos se o jogador não acertar
            print("Você perdeu 50 pontos, agora você tem {} pontos\n".format(pontos))

        continuar = int(
            input("Deseja continuar?\n1-SIM 2-NÃO: ")
        )  # Decisão se o jogador quer ou não continuar

        if (
            continuar == 1
        ):  # Caso sim, todo o código irá se repetir, guardando a pontuação do jogador
            continue
        elif continuar == 2:  # Caso não, irá encerrar com a pontuação atual do jogador
            print("Obrigado por jogar, você finalizou com {} pontos".format(pontos))
            break
        else:
            print("Opção inválida. Por favor, digite 1 para continuar ou 2 para sair.")


if __name__ == "__main__":
    jogar_Advinhacao()
