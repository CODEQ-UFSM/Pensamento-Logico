# Média da turma
#
# Dificuldade: ☆☆
#
# Enunciado:
# Faça um programa que leia a quantidade de alunos N de uma turma, em seguida, leia N notas (float) e calcule a média.
#
# +-----------------------------------+-----------------------------+
# |         Exemplo de entrada        |       Exemplo de saída      |
# +-----------------------------------+-----------------------------+
# | Digite a quantidade de alunos: 5  | A média é 7.540000000000001 |
# | Digite as notas                   |                             |
# | 10                                |                             |
# | 8.5                               |                             |
# | 4                                 |                             |
# | 8.2                               |                             |
# | 7                                 |                             |
# +-----------------------------------+-----------------------------+
# | Digite a quantidade de alunos: 10 | A média é 7.1               |
# | Digite as notas                   |                             |
# | 8                                 |                             |
# | 7                                 |                             |
# | 8                                 |                             |
# | 7                                 |                             |
# | 6                                 |                             |
# | 5                                 |                             |
# | 6                                 |                             |
# | 5                                 |                             |
# | 9                                 |                             |
# | 10                                |                             |
# +-----------------------------------+-----------------------------+
#
# DICA: Para ler valores tipo float, use float(input()).
#

qtd = int(input('Digite a quantidade de alunos: '))
i = 0
soma_notas = 0

print('Digite as notas')
while i < qtd:
    soma_notas += float(input())
    i += 1

media = soma_notas/qtd # Neste caso, por que não podemos dividir por i?

print('A média é', media)