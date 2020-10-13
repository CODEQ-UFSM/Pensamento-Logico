# Média da turma

qtd = int(input('Digite a quantidade de alunos: '))
i = 0
soma_notas = 0

print('Digite as notas')
while i < qtd:
    soma_notas += float(input())
    i += 1

media = soma_notas/qtd # Neste caso, por que não podemos dividir por i?

print('A média é', media)