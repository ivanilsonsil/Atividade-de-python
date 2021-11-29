# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario
# se elas podem ou não formar um triangulo.
print('-='*20)
print(' Analisador de Tiangulos' )
print('-='*20)
r1 = float(input('\033[0;37;41mPrimeiro segmento: '))
r2 = float(input('\033[1;35;43msegundo segmento: '))
r3 = float(input('\033[7;37;47mterceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('\033[0;32m os segmentos acima PODEM FORMA UM TRIANGULO!')
else:
    print('\033[0;35mos segmentos acima NÃO PODEM FORMAR TRIANGULO')

