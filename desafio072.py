# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até
# vinte.

# Seu programa deverá ler um número pelo teclado( entre 0 e 20)
# e mostrá-lo por extenso.

cont = ('zero','um','dois','tres','quatro',
        'cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze','catoze',
        'quinze', 'Dezesseis','dezessete','dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end='')
print(f'voce digitou {cont[num]}')
