# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem Dizendo que ele foi multado.
# A multa vai custar R$7,00 Por cada km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO: VOCE PASSOU DO LIMITE PERMITIDO QUE É DE 80KM/H')
    multa = (velocidade-80)*7
    print('voce dever pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia: derija com segurança:')
