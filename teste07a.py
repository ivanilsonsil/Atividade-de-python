n1 = int(input('Digite um valor!!'))
n2 = int(input('Digite outro valor!!'))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1//n2
e = n1 ** n2
rd = n1 % n2

print(' A Soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s,m,d),end='')
print(' Divisão inteira {}, potencia {}, resto da divisao {}'.format(di,e,rd))


