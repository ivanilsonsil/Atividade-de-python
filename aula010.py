n1 = float(input('Digite primeira nota!'))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua media foi de {:.1f}'.format(m))
if m >= 6.0 :
    print('boa nota , parabéns!')
else:
    print('sua nota está abaixo, estuder mais!')
