# Crie um programa que tenha uma TUPLA única com NOMES DE PRODUTOS  e seus respectivos preços,
# na sequencia.

# No final, mostre uma listagem de preços, organizando os dados em forma TABULAR.


listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Livros', 35.99,
            'Bolsa', 150.99,
            'Canetas', 20.34,
            'Compasso', 10.99,
            'Reguar', 7.65,)
print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*30)
for pos in range (0,len(listagem)):
    if pos % 2 == 0:
         print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')


