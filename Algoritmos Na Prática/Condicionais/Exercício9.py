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