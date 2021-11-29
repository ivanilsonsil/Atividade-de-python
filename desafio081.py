# Crie un programa que vai ler vários números e colocar em uma lista.
# Depois disso,mostre:

# A> Quantos números foram digitados.

# B> A lista de valores, ordenada  de forma decrescente.

# c> se o valor 5 foi digitdo e está ou não na lista.

list = []
while True:
    list.append (int(input('Digite um valor: ')))
    r = str(input('Quer continuar [S/N]...'))
    if r in 'Nn':
        break
print('-=-'*15)
print(f'Vc digitou {len(list)} elemnetos ...')
list.sort(reverse=True)
print(f'0s valores digitados em ordem decrecente são {list}')
if 5 in list:
    print('O valor ..5.. está na lista..')
else:
    print('O valor ..5.. não está na lista..')



