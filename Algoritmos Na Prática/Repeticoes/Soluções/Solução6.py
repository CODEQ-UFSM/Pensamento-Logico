# Primos
#
# Dificuldade: ☆☆☆
#
# Enunciado:
# Dado um número, imprima todos os seus divisores e diga se este número é primo ou não.
#
# +----------------------+---------------------+
# |  Exemplo de entrada  |   Exemplo de saída  |
# +----------------------+---------------------+
# | Digite um número: 10 | 10 é divisível por: |
# |                      | 1                   |
# |                      | 2                   |
# |                      | 5                   |
# |                      | 10                  |
# |                      | 10 não é primo.     |
# +----------------------+---------------------+
# | Digite um número: 57 | 57 é divisível por: |
# |                      | 1                   |
# |                      | 3                   |
# |                      | 19                  |
# |                      | 57                  |
# |                      | 57 não é primo.     |
# +----------------------+---------------------+
# | Digite um número: 23 | 23 é divisível por: |
# |                      | 1                   |
# |                      | 23                  |
# |                      | 23 é primo.         |
# +----------------------+---------------------+
#

n = int(input('Digite um número: '))
qtd_div = 0

print(n,'é divisível por:')
for i in range(1,n+1):
    if n%i == 0:
        print(i)
        qtd_div += 1

if qtd_div == 2:
    print(n,'é primo.')
else:
    print(n, 'não é primo.')