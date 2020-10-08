# Área e Volume
#
# Dificuldade: ☆
#
# Enunciado:
# Sabemos que a fórmula para calcular a área de um círculo é area = 𝜋 * raio**2 e para calcular o volume de uma esfera
# é volume = (4*𝜋*r**3)/3. Dado o raio como entrada, imprima o valor da área e do volume. (Considere pi 𝜋 = 3.1415926).
#
# +--------------------+----------------------------+
# | Exemplo de entrada |      Exemplo de saída      |
# +--------------------+----------------------------+
# | 2                  | Área:  12.5663704          |
# |                    | Volume:  33.51032106666667 |
# +--------------------+----------------------------+
# | 5                  | Área:  78.539815           |
# |                    | Volume:  523.5987666666666 |
# +--------------------+----------------------------+
#
# DICA: Para ler valores tipo float, use float(input()).
#

r = float(input('Digite o valor do raio: '))
pi = 3.1415926

print('Área: ', pi*r**2)
print('Volume: ', (4*pi*r**3)/3)