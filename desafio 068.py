# Faça um programa que jogue par ou impar como computador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitorias
# consecutivas que ele conquistou  no final do jogo.

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo =' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper() [0]
    print(f'Voce jogou {jogador} e o computador {computador}.total de {total}' , end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU!')
            v+= 1
        else:
            print('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!')
            v+= 1
        else:
            print('VOCE PERDEU!')
            break
    print('Vamos jogar novamnete...')
print(f'GAME OVER! voce VENCEU {v} vezes.')
