# Dardos

pontuacao1 = 0
pontuacao2 = 0

print('Digite a pontuação para cada rodada:')
for i in range(0,10):
    jogada = int(input())

    if i%2 == 0:
        pontuacao1 += jogada
    else:
        pontuacao2 += jogada

print('Pontuação final do Jogador 1:',pontuacao1)
print('Pontuação final do Jogador 2:',pontuacao2)

if pontuacao1 > pontuacao2:
    print('Jogador 1 venceu')
else:
    print('Jogador 2 venceu')