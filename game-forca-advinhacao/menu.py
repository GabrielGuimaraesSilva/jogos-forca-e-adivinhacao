import jogoAdvinhacao
import jogoForca

print("******************************************")
print("********BEM VINDO AO MENU DE JOGOS********")
print("******************************************")

escolha = int(input("(1) Jogo forca\n(2) Jogo Adivinhação\n"))

if escolha == 1:
    jogoForca.jogar_Forca()

elif escolha == 2:
    jogoAdvinhacao.jogar_Advinhacao()
