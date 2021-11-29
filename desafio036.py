# Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o saláriio do comprador e em quantos anos ele vai pagar.
# Calcula o valor da prestação mensal, abendo que ela não pode exceder 30% do salario ou então o emprestimo,
# Será negado

casa = float(input('Valor da casa: R$'))
Salario = float(input('Salario do compradro: R$'))
anos = int(input('Quantos anos de finaciamneto?'))
prestação = casa / (anos * 12)
minimo = Salario * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos'.format(casa,anos), end = '')
print('a prestação será de R$ {:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO! ')
else:
    print('Emprestimo NEGADO! ')