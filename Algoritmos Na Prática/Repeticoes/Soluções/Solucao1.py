# Castigo
#
# Dificuldade: ☆
#
# Enunciado:
# Você deve cumprir o castigo que é escrever X vezes uma frase. Faça um programa para cumprir o castigo no seu lugar
# usando estruturas de repetição. Devem ser informado ao programa qual a frase e qual a quantidade de vezes que deve ser
# repetida.
#
# +--------------------------------------------------+----------------------------------+
# |                Exemplo de entrada                |         Exemplo de saída         |
# +--------------------------------------------------+----------------------------------+
# | Digite a frase: Eu não devo fazer tal coisa      | Eu não devo fazer tal coisa      |
# | Digite a quantidade de vezes: 8                  | Eu não devo fazer tal coisa      |
# |                                                  | Eu não devo fazer tal coisa      |
# |                                                  | Eu não devo fazer tal coisa      |
# |                                                  | Eu não devo fazer tal coisa      |
# |                                                  | Eu não devo fazer tal coisa      |
# |                                                  | Eu não devo fazer tal coisa      |
# |                                                  | Eu não devo fazer tal coisa      |
# +--------------------------------------------------+----------------------------------+
# | Digite a frase: Programação me ajuda a trapacear | Programação me ajuda a trapacear |
# | Digite a quantidade de vezes: 1500               | Programação me ajuda a trapacear |
# |                                                  | Programação me ajuda a trapacear |
# |                                                  | Programação me ajuda a trapacear |
# |                                                  | Programação me ajuda a trapacear |
# |                                                  | Programação me ajuda a trapacear |
# |                                                  | Programação me ajuda a trapacear |
# |                                                  | Programação me ajuda a trapacear |
# |                                                  | Programação me ajuda a trapacear |
# |                                                  | ... x 1500                       |
# +--------------------------------------------------+----------------------------------+
#
# DICA: Você pode usar for() ou while()
#

# Escreva o programa aqui

frase = input('Digite a frase: ')
qtd = int(input('Digite a quantidade de vezes: '))

# Usando FOR
for i in range(0, qtd):
    print(frase)

# Usando WHILE (você precisa tirar o # do começo da linha para funcionar)
#i = 0
#while i < qtd:
#    print(frase)
#    i += 1