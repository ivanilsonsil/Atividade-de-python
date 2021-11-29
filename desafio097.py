# Faça um programa que tenha uma função chamada escrever(),
# que receba um texto qualquer como parametro e mostre
# uma mensagem com tamanho adaptável.

#==============

def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f' {msg}')
    print('~'*tam)


# PROGRAMA PRINCIPAL

escreva('GUSTAVO GUANABARA')
escreva(' CURSO DE PYTHON NO YOUTUBE')
escreva('Cev')


# PROGRAMA PRINCIPAL



