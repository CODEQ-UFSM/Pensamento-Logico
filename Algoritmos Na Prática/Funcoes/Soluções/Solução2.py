# Comparar Números

# Não usar return

def comparar(n1,n2):
    if n1 > n2:
        print('Primeiro é maior')
    elif n2 > n1:
        print('Segundo é maior')
    else:
        print('São iguais')

comparar(int(input()), int(input()))