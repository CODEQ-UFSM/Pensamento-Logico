# Problema da Basileia
#
# Dificuldade: ☆☆
#
# Da Wikipedia:
# O problema de Basileia consiste em encontrar a soma exata dos inversos dos quadrados dos inteiros positivos, isto é,
# a soma exata da série infinita:
#
#  1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ...
#
# Enunciado:
# Dada a quantidade de repetições, calcule uma aproximação para o resultado da série infinita.
# Sabendo que a resposta para o problema é (pi^2)/6, imprima também a aproximação de pi a partir do resultado encontrado.
#
# +-------------------------+--------------------------------------------------------------------------+
# |    Exemplo de entrada   |                             Exemplo de saída                             |
# +-------------------------+--------------------------------------------------------------------------+
# | Qtd. Repetições: 100    | (Pi^2)/6 ~= 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/100^2 = 1.6349839001848923   |
# |                         | Pi ~= 3.1320765318091053                                                 |
# +-------------------------+--------------------------------------------------------------------------+
# | Qtd. Repetições: 500000 | (Pi^2)/6 ~= 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/500000^2 = 1.644932066850254 |
# |                         | Pi ~= 3.141590743731832                                                  |
# +-------------------------+--------------------------------------------------------------------------+
# | Qtd. Repetições: 10     | (Pi^2)/6 ~= 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/10^2 = 1.5497677311665408    |
# |                         | Pi ~= 3.04936163598207                                                   |
# +-------------------------+--------------------------------------------------------------------------+
#
#

stop = int(input('Qtd. Repetições: '))
s = 0.0

for i in range(1, stop+1):
    s += 1/(i**2)

print('(Pi^2)/6 ~= 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/{}^2 = {}'.format(stop,s))

pi = (6*s)**.5
print('Pi ~=', pi)