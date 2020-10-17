
# Definição da função que retorna True se número é primo
def isPrime(n):
    qtd_div = 0
    for i in range(1, n + 1):
        if n % i == 0:
            qtd_div += 1

    return qtd_div == 2


vetor = [2, 5, 9, 10, 7, 29, 59, 57]

for j in range(len(vetor)):
    vetor[j] = isPrime(vetor[j])

print(vetor)