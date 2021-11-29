

# faça um programa que leia um ano qualquer a mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('\033[7;34;42mQue ano quer analisar? coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year # pegar o ano atual configurado na maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #expressão para verificar se o ano é bissexto
    print('\033[4;33;45mO ano {} é Bissexto'.format(ano))
else:
    print('O ano {} NAÕ E BISSEXTO'.format(ano))