# Problema da Basileia
#
# Dificuldade: ☆☆
#
# Da Wikipedia:
# O problema de Basileia consiste em encontrar a soma exata dos inversos dos quadrados dos inteiros positivos, isto é,
# a soma exata da série infinita:
#
#  1 + 1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ...
#
# Enunciado:
# Dada a quantidade de repetições, calcule uma aproximação para o resultado da série infinita.
# Sabendo que a resposta para o problema é (pi^2)/6, imprima também a aproximação de pi a partir do resultado encontrado.
# Considere que a quantidade de repetições será sempre maior que 3.
#
# +-------------------------+--------------------------------------------------------------------------+
# |    Exemplo de entrada   |                             Exemplo de saída                             |
# +-------------------------+--------------------------------------------------------------------------+
# | Qtd. Repetições: 100    | (Pi^2)/6 ~= 1 + 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/100^2 = 1.634983900184892|
# |                         | Pi ~= 3.1320765318091053                                                 |
# +-------------------------+--------------------------------------------------------------------------+
# | Qtd. Repetições: 500000 | (Pi^2)/6 ~= 1 + 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/500000^2 = 1.644932066850|
# |                         | Pi ~= 3.141590743731832                                                  |
# +-------------------------+--------------------------------------------------------------------------+
# | Qtd. Repetições: 10     | (Pi^2)/6 ~= 1 + 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/10^2 = 1.5497677311665408|
# |                         | Pi ~= 3.04936163598207                                                   |
# +-------------------------+--------------------------------------------------------------------------+
#
#