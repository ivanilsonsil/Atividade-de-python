# Faça um programa que mostre a tabuada de varios números, um de cada vez,
# para cada valor digitado pelo usuario. O programa será interrompido quando
# o número solicitado for negativo.

while True:
    n = int(input('Quer ver uma tabuada de qual valor? '))
    if n < 0:
        break
    print('-'* 30)
    for c in range(1,11):
        print(f'{n}x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA DE TABUADA ENCERRADO.')