r# crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

numero = int(input('\033[1;34mMe diga um numero qualquer:\033[m '))
resultado = numero % 2
if resultado == 0:
    print('\033[0;31mO numero {} é PAR'.format(numero))
else:
    print('\033[1;33mO número IMPAR'.format(numero))