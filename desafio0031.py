# Desenvolva um programa que pergunte a distancia de uma viagem em km.Calcule o preço da passagem
# cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagem mais longas.

distancia = float(input('\033[0;31mQual é a distancia d sua viagem? '))
print('\033[7;37mVoce está preste a começar uma viagem de {}KM.' .format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print('\033[0;36mE o preço da sua passagem será de R$ {:.2f}'.format(preço))


'''
distancia = float(input('Qual é a distancia de sua viagem? '))
print('Voce esta a começa uma viagem de  {}KM.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('preço da sua passagem será de R${:.2f}'.format(preço))
'''


