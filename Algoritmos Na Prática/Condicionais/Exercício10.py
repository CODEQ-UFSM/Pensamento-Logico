# Pedra, papel ou tesoura 2: Jogador vs. Máquina
#
# Dificuldade: ☆☆☆☆☆
#
# Enunciado:
# Receba uma palavra (string), contendo "Pedra", "Papel" ou "Tesoura". Esta string representa a jogada do jogador.
# O computador irá gerar um número aleatório entre 1 e 3, e, com isso, você deve atribuir 1 para "Pedra", 2 para "Papel"
# e 3 para "Tesoura". Imprima qual jogador ganhou ou se deu empate. Se o jogador digitar uma opção que não existe,
# escreva: "Essa jogada não é válida".
#
# A função que gera o número inteiro aleatório é randint(). Não exclua a linha 'from random import randint'
#
# +--------------------------+--------------------+
# |    Exemplo de entrada    |  Exemplo de saída  |
# +--------------------------+--------------------+
# | Jogador: Pedra           | Jogador ganhou.    |
# | Computador jogou Tesoura |                    |
# +--------------------------+--------------------+
# | Jogador: Papel           | Empate             |
# | Computador jogou Papel   |                    |
# +--------------------------+--------------------+
# | Jogador: Papel           | Computador ganhou. |
# | Computador jogou Tesoura |                    |
# +--------------------------+--------------------+
#
# DICA: Para ler strings, basta de utilizar o comando input().
# Dica: Lembre-se de que, ao trabalhar com strings, devemos utilizar aspas ''.
#

from random import randint # Não apagar esta linha

jog = input('Jogador: ')
comp = randint(1,3)

if comp == 1:
    #...