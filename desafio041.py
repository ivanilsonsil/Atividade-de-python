# A Confederação nacional de natação precisa de um programa que leia o ano de nascimento de um ;
# um atleta e mostre sua categoria, de acordo com a idade;

# Até 9 anos : MIRIM
# Até 14 anos : INFANTIL
# Até 19 anos: JUNIOR
# Ate 20 anos: SENIOR
# Acima: MASTER

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento # para saber a idade
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação INFANTIL.')
elif idade <= 19:
    print('Classsificação JUNIOR:')
elif idade <= 25:
    print('Clasificação SENIOR:')
else:
    print('Classificação MASTER')
