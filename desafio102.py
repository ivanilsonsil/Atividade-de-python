'''
Crie um programa que tenha uma função fatorial() que recebar dois paramentros:
o primeiro que indique o número a calcular o outro chamdo show
que será um valor lógico(opcional) indicando se será mostrado ou não na tela
o processo de calculo do fatorial
'''




def fato(n, show=True):
    f =1
    for c in range (n,0,-2):
        if show:
            print(c, end="")
            if c > 1:
                print('x', end='')
            else:
                print('=',end='')
        f*=c
    return f

# programar Principal

print(fato(5,show=True))
help(fato)


