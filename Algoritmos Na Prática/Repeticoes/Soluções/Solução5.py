# Soma de Pares e ímpares
#
# Dificuldade: ☆☆
#
# Enunciado:
# Faça um programa que leia dois valores X1 X2 correspondentes ao intervalo ABERTO (X1, X2). Calcule a soma de todos os
# números pares e a soma de todos os números ímpares e imprima na tela.
#
# +----------------------------------------------+----------------------------------------------------+
# |              Exemplo de entrada              |                  Exemplo de saída                  |
# +----------------------------------------------+----------------------------------------------------+
# | Digite dois valores para formar o intervalo: | Soma de pares no intervalo ( 5 , 25 ): 150         |
# | 5                                            | Soma de ímpares no intervalo ( 5 , 25 ): 165       |
# | 25                                           |                                                    |
# +----------------------------------------------+----------------------------------------------------+
# | 80                                           | Soma de pares no intervalo ( 80 , 1000 ): 248940   |
# | 1000                                         | Soma de ímpares no intervalo ( 80 , 1000 ): 248400 |
# +----------------------------------------------+----------------------------------------------------+
#
# DICA: for i in range(x1, x2+1): ou for i in range(x1, x2): Qual é o certo de se usar?
#

print('Digite dois valores para formar o intervalo:')
x1 = int(input())
x2 = int(input())
soma_par = 0
soma_impar = 0

for i in range(x1, x2+1):
    if i%2 == 0:
        soma_par += i
    else:
        soma_impar += i

print('Soma de pares no intervalo (',x1,',',x2,'):', soma_par)
print('Soma de ímpares no intervalo (',x1,',',x2,'):', soma_impar)