# Repetição Exponencial Triangular

# Dificuldade: ☆☆☆☆
#
# Enunciado:
# Faça um programa que leia um valor. A partir desse valor, imprima a saída como mostrada abaixo:
#
# +--------------------+-----------------------------------+
# | Exemplo de entrada |          Exemplo de saída         |
# +--------------------+-----------------------------------+
# | Linhas: 5          | 1                                 |
# |                    |                                   |
# |                    | 2 4                               |
# |                    |                                   |
# |                    | 3 9 27                            |
# |                    |                                   |
# |                    | 4 16 64 256                       |
# |                    |                                   |
# |                    | 5 25 125 625 3125                 |
# +--------------------+-----------------------------------+
# | Linhas: 3          | 1                                 |
# |                    |                                   |
# |                    | 2 4                               |
# |                    |                                   |
# |                    | 3 9 27                            |
# +--------------------+-----------------------------------+
# | Linhas: 7          | 1                                 |
# |                    |                                   |
# |                    |                                   |
# |                    | 2 4                               |
# |                    |                                   |
# |                    | 3 9 27                            |
# |                    |                                   |
# |                    | 4 16 64 256                       |
# |                    |                                   |
# |                    | 5 25 125 625 3125                 |
# |                    |                                   |
# |                    | 6 36 216 1296 7776 46656          |
# |                    |                                   |
# |                    | 7 49 343 2401 16807 117649 823543 |
# +--------------------+-----------------------------------+
#
# DICA: Para que um print não quebre a linha (lêe-se: "dar um enter"), é preciso escrever print('texto aqui', end=' ')
#       onde o end indica como o print deve terminar.
# DICA: Para intencionalmente quebrar uma linha, use o comando print('\n').
#
# ATENÇÃO: Se você estiver se perguntando "Porque não nos ensinaram a quebrar linha na aula?" você precisa entender que
#          é impossível passar todos os comandos de uma vez só. Além disso, aqui temos uma aplicação para estes
#          comandos, e isso nos dá um motivo para usá-los.
#

qtd = int(input('Linhas: '))
i = 1

for i in range(1, qtd+1):
    for j in range(1, i+1):
        print(i**j,end=' ')

    print('\n')

