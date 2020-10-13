# Fibonacci

qtd = int(input('Quantidade de termos: '))

i = 0
ant = 0 #
prox = 0

while i < qtd:
    print(prox)

    prox = prox + ant # A
    ant = prox - ant

    if prox == 0:
        prox += 1

    i += 1