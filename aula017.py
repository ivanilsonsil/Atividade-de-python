
a = [2,3,4,7]
b = a [:] # b receber todos os elementos de a, nesse caso vou pegar todos os valores de a e jogr para b
# desse jeito podemos fazer ligações entre listas . CRIANDO UMA COPIA...
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista b: {b}')




'''
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


''
valores = list()
valores.append(5)
valores.append(6)
valores.append(7)
for c,v in enumerate (valores):
   print(f'Na posição {c} encontrei o valor {v}!')
print('Chequei ao final da lista.')

'''





'''

num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 5 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
num.remove(4)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
'''

