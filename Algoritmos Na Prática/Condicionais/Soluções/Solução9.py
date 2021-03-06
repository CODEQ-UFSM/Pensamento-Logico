# Pedra, papel ou tesoura
#
# Dificuldade: ☆☆☆☆
#
# Enunciado:
# Receba duas palavras (strings), contendo "Pedra", "Papel" ou "Tesoura". Cada string representa a jogada de cada
# jogador. Imprima qual jogador ganhou ou se deu empate. Se o jogador digitar uma opção que não existe,
# escreva: "Essa jogada não é válida".
#
# +--------------------+--------------------------+
# | Exemplo de entrada |     Exemplo de saída     |
# +--------------------+--------------------------+
# | Jogador 1:Pedra    | Jogador 1 ganhou.        |
# | Jogador 2:Tesoura  |                          |
# +--------------------+--------------------------+
# | Jogador 1:Papel    | Jogador 2 ganhou.        |
# | Jogador 2:Tesoura  |                          |
# +--------------------+--------------------------+
# | Jogador 1:Lagarto  | Essa jogada não é válida |
# | Jogador 2:Papel    |                          |
# +--------------------+--------------------------+
#
# DICA: Para ler strings, basta de utilizar o comando input().
# Dica: Lembre-se de que, ao trabalhar com strings, devemos utilizar aspas ''.
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