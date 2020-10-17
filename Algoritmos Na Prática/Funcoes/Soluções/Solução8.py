# EXTRA: Recursão
#
#Aqui dar a definição de recursão e mostrar um exemplo simples EXTRA

def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x - 1) # Chamei a função dentro da própria função!!

x=int(input())
print('{}! = {}'.format(x, fatorial(x)))