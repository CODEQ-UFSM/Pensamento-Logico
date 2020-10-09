# Aproximação de Stirling
#
# Dificuldade: ☆☆☆☆
#
# Enunciado:
# Em matemática, a aproximação de Stirling é uma aproximação para fatoriais. É uma boa aproximação, levando a
# resultados precisos (não exatos) mesmo para pequenos valores de n.
#
#        _______   /  n  \ n
# n! ~ \/ 2 𝜋 n   |  ---  |
#                  \  e  /
#
# Considerando e = 2.7182818 e 𝜋 = 3.1415926, faça um programa que receba o valor de n e imprima seu fatorial
# aproximado pela fórmula de Stirling.
#
# +--------------------+---------------------------+
# | Exemplo de entrada |      Exemplo de saída     |
# +--------------------+---------------------------+
# | 5                  | 5 ! ~ 118.01917312900217  |
# +--------------------+---------------------------+
# | 10                 | 10 ! ~ 3598695.9648128385 |
# +--------------------+---------------------------+
# | 4                  | 4 ! ~ 23.506175916798625  |
# +--------------------+---------------------------+
#
# DICA: Para ler valores tipo float, use int(input()).
# DICA: Esse exercício é para aprender a utilizar parênteses nas equações
#

# Escreva o programa aqui

n = int(input('Número: '))

factorial =  ((n/2.7182818)**n)*((2*3.1415926*n)**0.5)

print(n,'! ~',factorial)