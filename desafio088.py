# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa
# vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 6 para
# cada jogo, cadastrando tudo em uma lista composta.

from random import randint # gerar números aleátorios
from time import sleep
lista = list()
jogos = list()
print('-='*15)
print('      JOGA NA MEGA SENA     ')
print('-='*15)
quant = int(input('Quantos jogos vc quer que eu sorteie? '))
tot = 1  # total de vezes que vai sortear
while tot <= quant: # enquanto o total for menor igual a quantidade
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista: # se num náo estiver na lista
            lista.append(num) # vai adicionar o num na lista
            cont += 1
        if cont >= 6:
            break
    lista.sort() # ordena os números
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='* 3, f'SORTEANDO {quant} JOGOS', '=-'* 3)
for i , l in enumerate(jogos):  # para cada indice da lista enumerate dos jogos
    print(f'Jogos {i+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE!>', '-='*5)
print('-='*5, '< OBRIGADO POR PARTICIPAR >', '-='*5)


