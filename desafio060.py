# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# ex:

# 5! = 5x4x3x2x1 = 120
'''
from math import factorial >>>  solução mais simples utilizando modulos
n = int (input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n,f))
'''

n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else '=' ,end='')
    f = f * c
    c = c - 1
print('{}' .format(f))