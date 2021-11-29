#podemos utiliza funções no nosso programa para
#que podemos ter maior agilidade rotinas
#
# def mensagem(msg):
#     print('=-='*15)
#     print(msg)
#     print('=-=' * 15)
#
# mensagem('SISTEMA DE ALUNO')
# mensagem(' PYTHON MELHOR LINGUAGEM DE PROGRAMA')
# mensagem(' VAMOS PROGRAMA COM  APENAS TEMOS QUE COMEÇA')

# def soma(*valores):
#     s =0
#     for num in valores:
#         s+=num
#     print(f'A soma entre os valores{valores} temos {s}')
# soma(4,4,4,4,4,4,4,4,4,4,4,6,65)
# soma(4,5,5,5,5,5,5,5)
#


def soma(*valores):
    s = 0
    for num in valores:
        s+=num
    print(f' A soma entre os valores{valores} temos {s}')

# programa pricipal

soma(5,4,4,4,4,4)
soma(5,6,6,6,6)






