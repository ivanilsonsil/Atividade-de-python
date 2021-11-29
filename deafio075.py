# Desenvolva um programa que leia QUATRO VALORES PELO TECLADO e guarde-os em uma TUPLA. No final,
# mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números paras.

num = (int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')))
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ªposição')
else:
    print('Os valor 3 não foi digitado em nenhuma posição')
print('os valores digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')