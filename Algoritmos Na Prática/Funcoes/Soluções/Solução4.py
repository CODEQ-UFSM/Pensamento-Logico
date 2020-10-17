
def isEven(n):
    return (n%2 == 0)

vetor = [2, 5, 9, 10, 7, 29, 59, 57]

for j in range(len(vetor)):
    vetor[j] = isEven(vetor[j])

print(vetor)