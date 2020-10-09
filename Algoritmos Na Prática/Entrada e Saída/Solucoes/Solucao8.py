# Número de Euler
#
# Dificuldade: ☆☆☆
#
# Enunciado:
# Leia um valor x. Use esse valor para aproximar o número de Euler e.
# Lembre-se de que quando x -> inf, u = e
#      /      1  \ x
# u =  | 1 + --- |
#      \      x  /
#
# +--------------------+-------------------------------------+
# | Exemplo de entrada |           Exemplo de saída          |
# +--------------------+-------------------------------------+
# | 1                  | Aproximação: e = 2                  |
# +--------------------+-------------------------------------+
# | 2                  | Aproximação: e = 2.25               |
# +--------------------+-------------------------------------+
# | 5                  | Aproximação: e = 2.4883199999999994 |
# +--------------------+-------------------------------------+
# | 1000               | Aproximação: e = 2.7169239322355936 |
# +--------------------+-------------------------------------+
# | 10000000           | Aproximação: e = 2.7182816941320818 |
# +--------------------+-------------------------------------+
#
# DICA: Para ler valores tipo float, use float(input()).
# DICA: Lembre-se do uso dos parênteses
#

x = float(input('x = '))

e = (1+1/x)**x

print('Aproximação: e =', e)