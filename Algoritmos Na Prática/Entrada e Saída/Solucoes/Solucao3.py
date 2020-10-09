# °C para °F
#
# Dificuldade: ☆
#
# Enunciado:
# Leia o valor da temperatura em °C e converta para °F.
#
# +--------------------+---------------------+
# | Exemplo de entrada |   Exemplo de saída  |
# +--------------------+---------------------+
# | 0                  | 0.0 °C = 32.0 °F    |
# +--------------------+---------------------+
# | 50                 | 50.0 °C = 122.0 °F  |
# +--------------------+---------------------+
# | -70                | -70.0 °C = -94.0 °F |
# +--------------------+---------------------+
#
# DICA: Para ler valores tipo float, use float(input()).
#

C = float(input("T[°C]: "))
F = C * (9 / 5) + 32

print(C, "°C =", F, "°F")