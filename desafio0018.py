'''Faça um programa que leia um angulo
  qualquer e mostre na tela o valor do seno,
 cosseno e tangente desse angulo.
 =========================================================
 '''
''' nesse caso temos quer comverter para radians por o valor dos angulos em °c
seno = math.sin(math.radians(angulo)) pegar o angula digitado
depois converter para radians em seguida o valor convertido calcula o seno dele

'''

import math
print('='*30)
angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print(' O angulo de {} tem SENO de========{:.2f}='.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print(' O angulo de {} tem o COSSENO de =={:.2f}='.format(angulo,cosseno))
tangenta = math.tan(math.radians(angulo))
print(' O angulo de {} tem o TANGENTE de =={:.2f}='.format(angulo,tangenta))
print('='*30)

''' outros métados 

from math import sin,cos,tan

angulo =  float(input('Digite um angulo qualquer: '))
seno = sin(math.radians(angulo))
print('O comprimento do angulo é {} valor do seno igual {:.2f}'.format(angulo,seno))
cosseno = cos(math.radians(angulo))
print('O comprimento do angulo {} valor do cosseno {:.2f}'.format(angulo,cosseno))
tangente = tan(math.radians(angulo))
print(' O comprimento do angulo {} valor do tangente {:.2f}'.format(angulo,tangenta))

'''






