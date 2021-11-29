#  Desenvolva uma lógica que leia o peso r a altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obsedade
# - acima de 40: obesidade mórbida

peso = float (input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[0;38m Voce está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('\033[0;37m VC ESTA NA FAIXA DE PESO NORMAL')
elif 25 <= imc < 30:
    print('\033[0;35m Vc está em SOBREPESO')
elif 30 <= imc < 40:
    print(' \033[0;33m VC ESTA em OBESIDADE cuidado')
elif imc >= 40:
    print('\033[0;32m Obesidade mórbida')


