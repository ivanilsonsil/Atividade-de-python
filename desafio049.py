# Refaça o dasafio 009, mostrando a tabuada de um numero que o usuario escolher, só que
# agora utilizando um laço for.

num = int(input('\033[0;36mDigite um número para ver sua tabuada: '))
for c in range(1,11):
    print('\033[0;35m{} x {:2} = {}'.format(num,c,num*c))

