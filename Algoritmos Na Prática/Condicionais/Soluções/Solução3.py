# Sólido, Líquido ou Gasoso
#
# Dificuldade: ☆
#
# Enunciado:
# Na pressão atmosférica normal, a água muda de estado para um sólido a 0°C ou abaixo e um gás a 100°C ou acima. Ele
# permanece líquido em qualquer outra temperatura. Escreva um programa que retornará 'Estado Sólido', 'Estado Líquido'
# ou 'Estado Gasoso' para o usuário, dependendo da temperatura.
#
# +--------------------+------------------+
# | Exemplo de entrada | Exemplo de saída |
# +--------------------+------------------+
# | 150                | Estado Gasoso    |
# +--------------------+------------------+
# | 0                  | Estado Sólido    |
# +--------------------+------------------+
# | 50                 | Estado Líquido   |
# +--------------------+------------------+
#
# DICA: Para ler valores tipo float, use float(input()).
#

T = float(input('Temperatura [ºC]: '))

if(T >= 100):
    print('Estado Gasoso')
elif(T <= 0):
    print('Estado Sólido')
else:
    print('Estado Líquido')