# Recíproco de Fibonacci em Vetor

qtd = int(input('Quantidade de termos: '))

vetor = []
i = 0
ant = 0
prox = 0

while i < qtd:

    prox = prox + ant
    ant = prox - ant
    if prox == 0:
        prox += 1

    vetor.append(1 / prox)

    i += 1

print(vetor)
print(sum(vetor))