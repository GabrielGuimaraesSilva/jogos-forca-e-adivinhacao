import random


def jogar_Forca():
    imprime_mensagem_jogo()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas_jogador = 0

    while not enforcou and not acertou:
        chute_jogador = chute_do_jogador()

        if chute_jogador in palavra_secreta:
            marca_chute_correto(chute_jogador, letras_acertadas, palavra_secreta)
        else:
            tentativas_jogador += 1
            desenha_forca(tentativas_jogador)

        enforcou = tentativas_jogador == 10
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


def imprime_mensagem_jogo():
    print("************************************")
    print("*****BEM VINDO AO JOGO DA FORCA*****")
    print("************************************")


def carrega_palavra_secreta():
    arquivo = open(
        r"D:\Gabriel\Códigos\Estudos\game-forca-advinhacao\palavras.txt", "r"
    )
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    letras_acertadas = ["_" for letra in palavra]

    return letras_acertadas


def chute_do_jogador():
    chute_jogador = input("Digite uma letra: ")
    chute_jogador = chute_jogador.strip().upper()

    return chute_jogador


def marca_chute_correto(chute_jogador, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute_jogador == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(tentativas_jogador):
    print("  _______     ")
    print(" |/      |    ")

    if tentativas_jogador == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if tentativas_jogador == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if tentativas_jogador == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if tentativas_jogador == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if tentativas_jogador == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if tentativas_jogador == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if tentativas_jogador == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar_Forca()
