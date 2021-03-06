# Dardos
#
# Dificuldade: ☆☆
#
# Enunciado:
# Dois jogadores possuem 5 dardos, cada. Eles jogam os dados intercaladamente, ou seja, ao jogar um dardo, a próxima
# jogada é do outro jogador. Dada as pontuações de cada jogada, calcule a pontuação de cada jogador e diga quem ganhou.
# O Jogador 1 é o primeiro a jogar.
#
# +--------------------------------------+-----------------------------------+
# |          Exemplo de entrada          |          Exemplo de saída         |
# +--------------------------------------+-----------------------------------+
# | Digite a pontuação para cada rodada: | Pontuação final do Jogador 1: 135 |
# | 5                                    | Pontuação final do Jogador 2: 100 |
# | 10                                   | Jogador 1 venceu                  |
# | 5                                    |                                   |
# | 50                                   |                                   |
# | 50                                   |                                   |
# | 10                                   |                                   |
# | 50                                   |                                   |
# | 5                                    |                                   |
# | 25                                   |                                   |
# | 25                                   |                                   |
# +--------------------------------------+-----------------------------------+
# | Digite a pontuação para cada rodada: | Pontuação final do Jogador 1: 100 |
# | 10                                   | Pontuação final do Jogador 2: 225 |
# | 50                                   | Jogador 2 venceu                  |
# | 10                                   |                                   |
# | 50                                   |                                   |
# | 25                                   |                                   |
# | 25                                   |                                   |
# | 5                                    |                                   |
# | 100                                  |                                   |
# | 50                                   |                                   |
# | 0                                    |                                   |
# +--------------------------------------+-----------------------------------+
#
#

pontuacao1 = 0
pontuacao2 = 0

print('Digite a pontuação para cada rodada:')
for i in range(0,10):
    jogada = int(input())

    if i%2 == 0:
        pontuacao1 += jogada
    else:
        pontuacao2 += jogada

print('Pontuação final do Jogador 1:',pontuacao1)
print('Pontuação final do Jogador 2:',pontuacao2)

if pontuacao1 > pontuacao2:
    print('Jogador 1 venceu')
else:
    print('Jogador 2 venceu')