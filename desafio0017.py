''' faça um programa que leia o comprimento
    do cateto oposto e do cateto
    adjacente de um triangulo retangulo,
     calcule e mostre o comprimneto da hipotenusa.
================================================================'''

''' maneira tradicional sem importação de modulos  ou bibliotecas'''
'''
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o canteto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("o comprimento da hipotenusa é igual {:.2f}".format(hi))
=================================================================
'''

''' metados de importação
==temos apenas um metado hypot

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('O comprimento da hipotenusa é igual a {:.2f}'.format(hi))

================================================================

temos todas as funcionalidades do metados math
'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print('O valor da hipotenusa é igual a {:.2f}'.format(hi))
