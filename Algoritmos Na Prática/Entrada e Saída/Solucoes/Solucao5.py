# Probabilidade do Impostor
#
# Dificuldade: ☆☆
#
# Enunciado:
# Você está jogando Among Us e quer saber qual a probabilidade de certo jogador ser um impostor. Faça um
# programa que receba a quantidade de impostores e a quantidade de jogadores e imprima a probabilidade.
#
# +--------------------+-----------------------------+
# | Exemplo de entrada |       Exemplo de saída      |
# +--------------------+-----------------------------+
# | 2                  | A probabilidade é de 40.0 % |
# | 5                  |                             |
# +--------------------+-----------------------------+
# | 3                  | A probabilidade é de 30.0 % |
# | 10                 |                             |
# +--------------------+-----------------------------+
# | 3                  | A probabilidade é de 50.0 % |
# | 6                  |                             |
# +--------------------+-----------------------------+
#

qtd_impostor = int(input('Quantidade de impostores: '))
qtd_jogador = int(input('Quantidade de jogadores: '))

prob = 100*(qtd_impostor/qtd_jogador)

print('A probabilidade é de', prob, '%')