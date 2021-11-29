def aumentar(preco = 0,taxa = 0 , formato=False):
    res = preco+(preco*taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0,taxa = 0, formato = False):
    res = preco - (preco*taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco = 0,formato=False):
    res = preco*2
    return res if not formato else moeda(res)


def metade(preco = 0,formato=False):
    res = preco/2
    return res if not formato else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'Dobro do preço:\t\t{dobro(preço,True)}')
    print(f'Metade do preço:\t\t{metade(preço,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço,taxaa,True)}')
    print(f'{taxar}% de Redução: \t\t{diminuir(preço, taxar, True)}')
    print('-' * 30)