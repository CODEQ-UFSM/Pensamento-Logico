# pegar um vetor e separar em 2 com pares e impares

def separa(vetor):
    pares = []
    impares = []
    for i in vetor:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

A = [1, 4, 3, 6, 8, 5, 2, 4, 5, 7, 0, 3, 4, 2, 6]
par_A, impar_A = separa(A)
print(par_A, impar_A)
