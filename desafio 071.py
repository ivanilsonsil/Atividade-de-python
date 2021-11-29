# Crie um programa que simule o funcionamento de um CAIXA ELETRONICO. No inicio,pergunte
# ao usuário qual será o valor a ser sacado (número interio) e o programa vai informar quantas
# cédulas de cada valor serão entregues.

# obs
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('\033[0;32m')
print('='* 30)
print('{:^30} ' .format('BANCO DO BRASIL'))
print('='* 30)
print('\033[m')
valor = int(input('QUE VALOR VOCE QUER SACAR? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >=ced:
        total -=ced
        totced +=1
    else:
        if totced > 0:
            print(f'total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10 :
            ced = 1
        totced = 0
        if total == 0:
            break
        print('=' * 30)
        print('VOLTE SEMPRE AO BANCO DO BRASIL! TENHA UM BOM DIA!')
