# Soma de Pares e ímpares
#
# INTERVALO ABERTO!!

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