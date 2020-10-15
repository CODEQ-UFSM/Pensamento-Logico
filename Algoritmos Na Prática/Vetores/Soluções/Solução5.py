# Absoluto em Vetor

V = [-10, 6, 3, 0, -130, 30, 9, -50, 50]
n = len(V)

for i in range(n):
    if V[i] < 0:
        V[i] = -V[i]

print(V)