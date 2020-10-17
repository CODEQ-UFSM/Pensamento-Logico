# Classificação par ou ímpar

vetor = [10, 5, 3, -90, 34, 75, 1]
par = []
impar = []

for i in vetor:
    if i%2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(par)
print(impar)