# def fatorial(num=1):
#     f=1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# print(f' {f1} e {f2}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número:'))
if par(num):
    print('É PAR')
else:
    print('NÃO É PAR')