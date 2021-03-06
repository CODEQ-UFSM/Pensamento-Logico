# Divisível por 13
#
# Dificuldade: ☆
#
# Enunciado:
# Leia um número inteiro e diga se este é divisível por 13.
#
# +--------------------+------------------------+
# | Exemplo de entrada |    Exemplo de saída    |
# +--------------------+------------------------+
# | 117                | É divisível por 13     |
# +--------------------+------------------------+
# | 58                 | Não é divisível por 13 |
# +--------------------+------------------------+
# | 6435               | É divisível por 13     |
# +--------------------+------------------------+
#
# DICA: Para ler valores tipo inteiro, use int(input()).
#

num = int(input('Digite um número:'))

if(num % 13 == 0):
    print('É divisível por 13')
else:
    print('Não é divisível por 13')