# Crie um programa que vai gerar CINCO NÚMEROS ALEATORIOS e colocar em uma TUPLA.

# Depois disso, mostre a LISTAGEM DE NÚMEROS gerados e também indique o MENOR e o MAIOR valor que estão
# na tupla.

from random import randint
numeros = (randint(1,10), randint(1,10),  randint(1,10),
           randint(1,10),randint(1,10))
print('Os valores sorteados foram:  ', end='')
for n in numeros:
    print(f'{n}  ', end='')
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
