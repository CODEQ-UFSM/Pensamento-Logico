# Pedra, papel ou tesoura 2: Jogador vs. Computador
#
# Dificuldade: ☆☆☆☆
#

from random import randint # Não apagar esta linha

jog = input('Jogador: ')
comp = randint(1,3)

if comp == 1:
    comp = 'Pedra'
elif comp == 2:
    comp = 'Papel'
elif comp == 3:
    comp = 'Tesoura'

print('Computador jogou', comp)

if jog == comp:
    print("Empate")
elif jog == "Pedra":
    if comp == "Papel":
        print("Computador ganhou.")
    else:
        print("Jogador ganhou.")
elif jog == "Papel":
    if comp == "Tesoura":
        print("Computador ganhou.")
    else:
        print("Jogador ganhou.")
elif jog == "Tesoura":
    if comp == "Pedra":
        print("Computador ganhou.")
    else:
        print("Jogador ganhou.")
else:
    print("Essa jogada não é válida")