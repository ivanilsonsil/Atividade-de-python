# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,mostre
# os 10 primeiros termos dessa progressão.
print('='*20)
print(' \033[0;32m10 TERMOS DE UMA PA\033[m')
print('='*20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='>')
print('ACABOU')