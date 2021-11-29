# Melhore jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só
# que agora o jogador vai tentar adivinhar até acerta, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.' )
print('Será que voce conseguer adivinha qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou na {} tentativas parabéns!!! '.format(palpites))
