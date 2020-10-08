# Idade em Anos, Meses e Dias
#
# Dificuldade: ☆☆☆
#
# Enunciado:
# Receba a idade do usuário em dias e imprima quantos anos, meses e dias o usuário tem. Desconsidere anos bissextos e
# considere que todos os meses posuem 30 dias.
#
# +--------------------+------------------+
# | Exemplo de entrada | Exemplo de saída |
# +--------------------+------------------+
# | 1500               | Qtd. anos: 4     |
# |                    | Qtd. meses: 1    |
# |                    | Qtd. dias: 10    |
# +--------------------+------------------+
# | 7400               | Qtd. anos: 20    |
# |                    | Qtd. meses: 3    |
# |                    | Qtd. dias: 10    |
# +--------------------+------------------+
# | 20000              | Qtd. anos: 54    |
# |                    | Qtd. meses: 9    |
# |                    | Qtd. dias: 20    |
# +--------------------+------------------+
#
# DICA: Para ler valores tipo float, use int(input()).
# DICA: Tente deixar o código o menor possível, serão utilizadas apenas operações básicas.
#

idade = int(input('Idade: '))

ano = int(idade/365)
mes = int((idade%365)/30)
dia = int((idade%365)%30)

print('Qtd. anos:', ano)
print('Qtd. meses:', mes)
print('Qtd. dias:', dia)