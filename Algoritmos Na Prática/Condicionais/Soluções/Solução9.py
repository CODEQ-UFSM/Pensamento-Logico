# Pedra, papel ou tesoura
#
# Dificuldade: ☆☆
#

jog1 = input('Jogador 1:')
jog2 = input('Jogador 2:')


if jog1 == jog2:
    print("Empate")
elif jog1 == "Pedra":
    if jog2 == "Papel":
        print("Jogador 2 ganhou.")
    else:
        print("Jogador 1 ganhou.")
elif jog1 == "Papel":
    if jog2 == "Tesoura":
        print("Jogador 2 ganhou.")
    else:
        print("Jogador 1 ganhou.")
elif jog1 == "Tesoura":
    if jog2 == "Pedra":
        print("Jogador 2 ganhou.")
    else:
        print("Jogador 1 ganhou.")
else:
    print("Essa jogada não é válida")