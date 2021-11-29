# Faça um programa que tenha uma função chamada maior(),que recebar varios
# paramentros com valores inteiros.
#
# seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* num): # DESENPACOTAMENTO
    cont = maior = 0
    print('-=-'*15)
    print('\n Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ' , flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram informados {cont} valores ao todo...')
    print(f' O maior valor informado foi {maior}')



# programa principal

maior (1,2,3,4,5)
maior(4,4,5,6,8)
maior(7,8,9)
maior(4)
maior(0)