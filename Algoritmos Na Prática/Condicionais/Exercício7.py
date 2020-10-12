# Triângulos
#
# Dificuldade: ☆☆☆
#
# Encunciado:
# O programa deve ler três valores correspondentes ao lado de um triângulo. Em seguida, deve colocá-los em ordem
# decrescente e determinar qual o tipo de triângulo formado.
# Se A ≥ B+C, o triângulo não pode ser formado.
# Se A2 = B2 + C2, é um triângulo retângulo
# Se A2 > B2 + C2, é um triângulo obtusângulo
# Se A2 < B2 + C2, é um triângulo acutângulo
# Diga também se o triângulo é isóceles ou equilátero
#
# +--------------------+---------------------------------+
# | Exemplo de entrada |         Exemplo de saída        |
# +--------------------+---------------------------------+
# | Lado 1: 50         | Não é possível formar triângulo |
# | Lado 2: 99         |                                 |
# | Lado 3: 1          |                                 |
# +--------------------+---------------------------------+
# | Lado 1: 5          | Retângulo                       |
# | Lado 2: 13         |                                 |
# | Lado 3: 12         |                                 |
# +--------------------+---------------------------------+
# | Lado 1: 20         | Acutângulo                      |
# | Lado 2: 20         | Isóceles                        |
# | Lado 3: 10         |                                 |
# +--------------------+---------------------------------+
#
# DICA: Não se esqueça de ordenar A,B e C.
#

a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))