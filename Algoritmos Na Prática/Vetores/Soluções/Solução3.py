# Lista de Compras
# Falar que precisa usar x = [] no começo

n = int(input('Digite a quantidade de itens: '))
vetor = []

print('Digite',n,'itens')

for i in range(n):
    idade = input()
    vetor.append(idade)

print(vetor)