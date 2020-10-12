# Triângulos
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
#


a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

# Primeiro, vamos ordenar os valores em ordem decrescente:
if (a < b):
    x = a
    a = b
    b = x
if (b < c):
    x = b
    b = c
    c = x
if (a < b):
    x = a
    a = b
    b = x;

if (a >= b + c):
    print("Não é possível formar triângulo")
elif (a * a == b * b + c * c):
    print("Retângulo")
elif (a * a > b * b + c * c):
    print("Obtusângulo")
elif (a * a < b * b + c * c):
    print("Acutângulo")

if (a == b and b == c):
    print("Equilátero")
elif (a == b or b == c):
    print("Isóceles")