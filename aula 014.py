'''
for c in range(1,10):
    print(c)
print('FIM')
============================
c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')

'''
'''
n = 1
while n != 0: # enquanto o numero for diferente de 0 ele vai ficar lendo o numero. chamamos esse codigo 
    # de fleg ou ponto de parada
    n = int(input('Digite um valor: '))
print('Fim')
'''
'''
r ='S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N] ')).upper()
print('Fim')

'''
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0: # se o resto da divisão por dois for igual a zero ele será par
            par = par + 1
        else:
            impar = impar + 1
print('Voce digitou {} números pares e {} números imparares! '.format(par,impar))