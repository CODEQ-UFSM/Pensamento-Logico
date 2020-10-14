# Tabuada
#
# Sem repetição exemplo 4x5 e 5x4

for i in range(1, 11):
    for j in range(1, 11):
        if j >= i:
            print(i,'x',j,'=',i*j)
    print('\n')