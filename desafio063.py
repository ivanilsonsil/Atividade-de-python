# escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
# elementos de uma Sequencia de fibonacci.

# ex:

# 0 > 1 > 1 > 2 > 3 > 5 > 8
print('-=-'*10)
print('\033[0;32m SEQUENCIA DE FIBONACCI \033[m:')
print('-=-'*10)
n = int(input('Quantos termos voce que mostrar?  '))
t1 = 0
t2 = 1
print('-=-'*10)
print( '{} > {}'.format(t1,t2),end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' > {} '.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('='*30)


