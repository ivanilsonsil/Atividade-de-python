from ex108 import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)}  é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de  {moeda.moeda(p)}  e {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando  10%, temos R${moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuindo  20%, temos R${moeda.moeda(moeda.diminuir(p,20))}')