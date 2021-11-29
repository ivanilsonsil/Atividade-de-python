# Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será
# a base de conversão;
 # -1 para binário
 # -2 para octal
 # -3 para hexadecimal

num = int(input('Digite um numero inteiro:'))
print('''escolha uma das Bases para fazer conversão:
[1] para BINARIO
[2] para OCTAL
[3] para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('\033[0;31m{} conversão para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('\033[0;37m{} conversão para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opção == 3 :
    print('\033[0;34m{} conversão para HEXADECIMAL é igual a {} ' .format(num,hex(num)[2:]))
else:
    print('opção invalida. tente novamnete: ')