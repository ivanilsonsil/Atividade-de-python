# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
print('='*24)

real = float(input('Quanto dinheiro voce tem na carteira? R$ '))
dolar = real / 5.35
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real,dolar))

print('='*24)