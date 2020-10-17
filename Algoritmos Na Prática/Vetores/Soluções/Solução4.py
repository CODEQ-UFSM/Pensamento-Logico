# Ler e Guardar Idades 2
#
# parar quando idade = 0 e não guardar o 0

vetor = []

print('Digite n <= 0 quando quiser parar!')

idade = int(input())
while idade <= 0:
    vetor.append(idade)
    idade = int(input())

print(vetor)