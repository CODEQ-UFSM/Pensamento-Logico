# Hipotenusa
#
# Dificuldade: ☆☆
#
# Enunciado:
# Leia dois valores reais que representam os dois catetos de um triângulo, a e b. Imprima o valor da hipotenusa na tela
#
# +--------------------+---------------------------------+
# | Exemplo de entrada |         Exemplo de saída        |
# +--------------------+---------------------------------+
# | 3                  | Hipotenusa = 5                  |
# | 4                  |                                 |
# +--------------------+---------------------------------+
# | 9.6                | Hipotenusa = 12.36931687685298  |
# | 7.8                |                                 |
# +--------------------+---------------------------------+
# | 12                 | Hipotenusa = 15.620499351813308 |
# | 10                 |                                 |
# +--------------------+---------------------------------+
#
# DICA: Para ler valores tipo float, use float(input()).
# DICA: Você irá precisar calcular raiz quadrada de um valor, se não lembrar como fazê-lo utilizando exponenciação,
#       pesquise na internet.
#

a = float(input('a = '))
b = float(input('b = '))

c = (a**2 + b**2)**0.5

print('Hipotenusa = ', c)