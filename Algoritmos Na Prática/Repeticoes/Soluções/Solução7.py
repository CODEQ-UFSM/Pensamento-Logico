# Fatorial
#
# Dificuldade: ☆☆
#
# Enunciado:
# Dado um número, imprima seu fatorial
#
# +--------------------+------------------+
# | Exemplo de entrada | Exemplo de saída |
# +--------------------+------------------+
# | 5                  | 5! = 120         |
# +--------------------+------------------+
# | 10                 | 10! = 3628800    |
# +--------------------+------------------+
# | 7                  | 7! = 5040        |
# +--------------------+------------------+
#

n = int(input())
fat = 1

for i in range(0,n+1):
    if i == 0:
        fat = fat * 1
    else:
        fat = fat * i

print('{}! = {}'.format(n, fat))