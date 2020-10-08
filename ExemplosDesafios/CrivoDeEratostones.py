final = int(input())
limite = int((final)**0.5)

numeros = list(range(2, final + 1))

for i in range(2, limite + 1):
    for j in numeros:
        if j % i == 0 and j != i:
            numeros.remove(j)

print(numeros)
