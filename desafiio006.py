# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.


n = int(input('Digite um numero!'))
d = n * 2
t = n * 3
r = n**(1/2)
print('O Dobro de {} vale {}.'.format(n,d))
print('O triplo de {} vale {}.' .format(n,t))
print('A rais quadrada {} vale {:.3f}' .format(n,r))

# outros métados menos espaço na mémoria

# n = int(input('Digite um valor!')
# print(' dobro de {} vale {}.' .format(n(n*2)))
# print(' o triplo de {} vale{} raiz qua de {} vale{}.' .format(n,(n*3), n,(n**(1/2)))) esse ou esse pow(n,(1/2))))