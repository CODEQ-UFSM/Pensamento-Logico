# Distância
#
# Dificuldade: ☆☆
#
# Enunciado:
# Leia quatro valores reais, os dois primeiros corresponderão às coordenadas X1, Y1 do primeiro ponto P1(X1, Y1). Os
# dois últimos corresponderão às coordenadas X2, Y2 do segundo ponto P2(X2, Y2). Calcule a distância D entre os dois
# pontos sabendo que D = √((X2-X1)**2 + (Y2-Y1)**2)
#
# +--------------------+-----------------------------------+
# | Exemplo de entrada |          Exemplo de saída         |
# +--------------------+-----------------------------------+
# | 5.0                | A distância é:  5.0               |
# | 7.0                |                                   |
# | 9.0                |                                   |
# | 4.0                |                                   |
# +--------------------+-----------------------------------+
# | 2.5                | A distância é:  10.54371850914088 |
# | 9.6                |                                   |
# | 8.6                |                                   |
# | 1                  |                                   |
# +--------------------+-----------------------------------+
#
# DICA: Para ler valores tipo float, use float(input()).
# DICA: Você irá precisar calcular raiz quadrada de um valor, se não lembrar como fazê-lo utilizando exponenciação,
#       pesquise na internet.
#

X1 = float(input('X1 = '))
Y1 = float(input('Y1 = '))
X2 = float(input('X2 = '))
Y2 = float(input('Y2 = '))

D = ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5

print('A distância é: ', D)