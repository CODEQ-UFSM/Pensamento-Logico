# Ano Bissexto
#
# Dificuldade: ☆☆☆☆
#
# Enunciado:
# Faça um programa que receba um valor referente a certo ano. Em seguida, diga se este ano é bissexto ou não.
#
# Definição do Wikipedia: Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, um
# dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não
# são múltiplos de 400).
# Ou seja, Anos bissextos são múltiplos de 4, não múltiplos de 100 (1900 não é bissexto) e múltiplos de 400
# 2000 é bissexto).

ano = int(input('Qual ano? '))

if(ano%400 == 0):
    print('Bissexto!')
elif(ano%100 == 0):
    print('Não é Bissexto.')
elif(ano%4 == 0):
    print('Bissexto!')
else:
    print('Não é Bissexto.')