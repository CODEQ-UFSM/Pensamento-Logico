# Crescente e Decrescente
#
# Dificuldade: ☆☆☆
#
# Enunciado:
# Leia três números inteiros, A, B e C. Em seguida, pergunte ao usuário se quer ordená-los de forma crescente ou
# decrescente. Imprima os três números ordenadamente.
#
# +--------------------------------------------------------------+------------------+
# |                      Exemplo de entrada                      | Exemplo de saída |
# +--------------------------------------------------------------+------------------+
# | A = 9                                                        | 10 9 7           |
# | B = 10                                                       |                  |
# | C = 7                                                        |                  |
# | Crescente ou Decrescente? (Digite C ou D para cada opção): D |                  |
# +--------------------------------------------------------------+------------------+
# | A = 88                                                       | -357 44 88       |
# | B = -357                                                     |                  |
# | C = 44                                                       |                  |
# | Crescente ou Decrescente? (Digite C ou D para cada opção): C |                  |
# +--------------------------------------------------------------+------------------+
# | A = 0                                                        | 55 1 0           |
# | B = 55                                                       |                  |
# | C = 1                                                        |                  |
# | Crescente ou Decrescente? (Digite C ou D para cada opção): D |                  |
# +--------------------------------------------------------------+------------------+
#
# DICA: Para ler valores tipo inteiro, use int(input()).
# DICA: Não esqueça da variável auxiliar.
#

A = int(input('A = '))
B = int(input('B = '))
C = int(input('C = '))
opt = input('Crescente ou Decrescente? (Digite C ou D para cada opção): ')

if opt == 'C':
    if A > B:
        aux = A
        A = B
        B = aux
    if B > C:
        aux = B
        B = C
        C = aux
    if A > B:
        aux = A
        A = B
        B = aux
elif opt == 'D':
    if A < B:
        aux = A
        A = B
        B = aux
    if B < C:
        aux = B
        B = C
        C = aux
    if A < B:
        aux = A
        A = B
        B = aux

print(A, B, C)