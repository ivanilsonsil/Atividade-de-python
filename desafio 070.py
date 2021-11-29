#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuario vai continuar. No final, mostre:

# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$1000.
# Qual é o nome do produto mais barato.
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont+= 1
    total += preço
    if preço > 1000:
        totmil+= 1
    if cont == 1 or preço < menor :
        menor =  preço
        barato = produto
    resp=' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'\033[0;32m Total da comprar foi de R${total} ')
print(f'\033[0;31m temos {totmil} produtos custando mais de R$1000.00 ')
print(f' O produto mais barato custam R$ {menor:.2f}')
