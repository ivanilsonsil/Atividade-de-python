# Crie um pprograma que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o Usuario quer ou não continuar. no final, mostre:

# Quantas pessoas tem mais de 18 anos.
# Quantas homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.
tot18 = toth = totM20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]')).strip() .upper() [0]
    if idade >= 18:
        tot18+=1
    if sexo == 'M':
        toth+=1
    if sexo == 'F' and idade < 20:
        totM20+=1
    resp = ' '
    while resp not in 'SN':
         resp = str(input('Quer continuar? [S/N] ')).strip() .upper()[0]
    if resp == 'N':
        break
print(f'Total de pessos com mais de 18 anos: {tot18}')
print(f'Ao todo temos {tot18} homens cadastrado')
print(f'temos {totM20} mulheres cadastrado')
