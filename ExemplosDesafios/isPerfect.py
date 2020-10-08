def isPerfect(num):
    acum = 0 # Zerando o acumulador
    for i in range(1, num): # Laço de repetição que vai de 1 até num
        if(num % i == 0): # Verificando se num é divisível por i
            acum = acum + i # Se for divisível, somamos no acumulador
    
    if(acum == num): # Verificando se a soma é igual ao próprio número
        return True # Se for perfeito, retornar verdadeiro
    else:
        return False # Se não for perfeito, retornar falso

print(isPerfect(28))
print(isPerfect(6))
print(isPerfect(496))
print(isPerfect(5))
print(isPerfect(10))
