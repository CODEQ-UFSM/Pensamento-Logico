# Verificar Área 2
#
# Dificuldade: ☆☆
#
# Enunciado:
# Dois vizinhos estão competindo para saber quem possui o maior terreno. Faça um programa que leia o comprimento e a
# largura de cada terreno e compare a área de ambos. Em seguida, escreva na tela qual é o maior terreno, ou se eles
# são iguais. Desta vez, não deixe o usuário colocar valores menores ou iguais a 0.
#
# +--------------------+----------------------------+
# | Exemplo de entrada |      Exemplo de saída      |
# +--------------------+----------------------------+
# | Terreno 1          | Dados incorretos!          |
# | Comprimento: -1    |                            |
# | Largura: 10        |                            |
# | Terreno 2          |                            |
# | Comprimento: 3     |                            |
# | Largura: 2         |                            |
# +--------------------+----------------------------+
# | Terreno 1          | O primeiro terreno é maior |
# | Comprimento: 20    |                            |
# | Largura: 5         |                            |
# | Terreno 2          |                            |
# | Comprimento: 20    |                            |
# | Largura: 2         |                            |
# +--------------------+----------------------------+
# | Terreno 1          | Dados incorretos!          |
# | Comprimento: 10    |                            |
# | Largura: 6         |                            |
# | Terreno 2          |                            |
# | Comprimento: 2     |                            |
# | Largura: 0         |                            |
# +--------------------+----------------------------+
#
# DICA: Para ler valores tipo float, use float(input()).
#

# Escreva o programa aqui

print('Terreno 1')
comprimento1 = float(input('Comprimento: '))
largura1 = float(input('Largura: '))

print('Terreno 2')
comprimento2 = float(input('Comprimento: '))
largura2 = float(input('Largura: '))

if(comprimento1<=0 or comprimento2<=0 or largura1<=0 or largura2<=0):
    print('Dados incorretos!')
else:
    area1 = comprimento1*largura1
    area2 = comprimento2*largura2

    if(area1 > area2):
        print('O primeiro terreno é maior')
    elif(area1 < area2):
        print('O segundo terreno é maior')
    else:
        print('Os dois tem mesma área')