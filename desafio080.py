# crie um programa onde o usuário possa digitar cinco valores númericos e
# cadastre-os em uma lista, Já na posição correta de inserção
# sem usar o  sort()).
# No final, mostre a lista ordenada na tela.

list = []
for c in range(0,5):
    n = int(input('Digite um valor...'))
    if c == 0 or n > list [-1]:
        list.append(n)
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos,n)
                break
            pos += 1
print('-='*15)
print(f' valores Digitados em ordem foram {list}...')
