# Ordenação de Livros
#
# Sem usar coisas


vetor = [14, 50, 73, 2, 87, 3, 100] # Vetor com altura dos livros

n = len(vetor) # Quantidade de livros

for i in range(n):
    for j in range(n-1):
        if vetor[j]>vetor[j+1]:
            aux = vetor[j]
            vetor[j] = vetor[j+1]
            vetor[j+1] = aux

print(vetor)