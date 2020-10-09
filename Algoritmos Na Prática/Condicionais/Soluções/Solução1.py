# Verificar Área
#
# Dificuldade: ☆
#
# Enunciado:
# Dois vizinhos estão competindo para saber quem possui o maior terreno. Faça um programa que leia o comprimento e a
# largura de cada terreno e compare a área de ambos. Em seguida, escreva na tela qual é o maior terreno, ou se eles
# são iguais.
#
# +--------------------+----------------------------+
# | Exemplo de entrada |      Exemplo de saída      |
# +--------------------+----------------------------+
# | Terreno 1          | O segundo tem maior área   |
# | Comprimento: 10    |                            |
# | Altura: 5          |                            |
# | Terreno 2          |                            |
# | Comprimento: 20    |                            |
# | Altura: 5          |                            |
# +--------------------+----------------------------+
# | Terreno 1          | O primeiro terreno é maior |
# | Comprimento: 20    |                            |
# | Largura: 5         |                            |
# | Terreno 2          |                            |
# | Comprimento: 20    |                            |
# | Largura: 2         |                            |
# +--------------------+----------------------------+
# | Terreno 1          | Os dois tem mesma área     |
# | Comprimento: 10    |                            |
# | Largura: 6         |                            |
# | Terreno 2          |                            |
# | Comprimento: 3     |                            |
# | Largura: 20        |                            |
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

area1 = comprimento1*largura1
area2 = comprimento2*largura2

if(area1 > area2):
    print('O primeiro terreno é maior')
elif(area1 < area2):
    print('O segundo terreno é maior')
else:
    print('Os dois tem mesma área')