# Crie um programa que vai ler vários números e coloocar em uma lista.
# Depois disso,crie duas listas extras que vão contar apenas os valores pares e os valores impares
# Digitados, respectivamnete.
 # ao final, mostre das tres listas geradas.
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)

print('-=-'*15)
print(f'A lista completa {num}')
print(f'A lista dos números pares: {pares} ')
print(f'A lista dos números impares: {ímpares}')
