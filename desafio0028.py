# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça
# para o usuario tentar descobrir qual foi o numero escolhido pelo computador. o programa deverá
# escreve na tela se o usuario venceu ou perdeu.


from random import randint
from time import sleep
computador = randint(0,5) # faz o computador "pensar"
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tentar adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('\033[0;31m PARABENS: VOCE CONSEGUIU ME VENCER:')
else:
    print('\033[0;32m GANHEI: EU PENSEI NO NUMERO {} E NÃO NO {} ; '.format(computador,jogador))