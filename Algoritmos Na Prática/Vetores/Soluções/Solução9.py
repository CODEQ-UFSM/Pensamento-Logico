# Multiplicação de vetores

X1 = [1, 3, 5, 13]
X2 = [7, 8, 9, 10]

if len(X1) == len(X2):
    A = 0
    for i in range(len(X1)):
        A += X1[i]*X2[i]

    print(A)
else:
    print('Não é possível fazer esta operação.')