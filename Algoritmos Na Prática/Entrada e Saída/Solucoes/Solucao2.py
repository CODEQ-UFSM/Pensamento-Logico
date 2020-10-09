# Calculadora de Exponenciação
#
# Dificuldade: ☆
#
# Enunciado:
# Receba dois números reais, num e exp. Imprima o resutado de num elevado na exp potência.
#
# +--------------------+--------------------+
# | Exemplo de entrada |  Exemplo de saída  |
# +--------------------+--------------------+
# | 5                  | 5.0 ^ 5.0 = 3125.0 |
# | 5                  |                    |
# +--------------------+--------------------+
# | 25                 | 25.0 ^ 0.5 = 5.0   |
# | 0.5                |                    |
# +--------------------+--------------------+
# | 12                 | 12.0 ^ 2.0 = 144.0 |
# | 2                  |                    |
# +--------------------+--------------------+
#
# DICA: Para ler valores tipo float, use int(input()).
#

num = float(input('Número: '))
exp = float(input('Expoente: '))
res = num ** exp

print(num, '^', exp, '=', res)
