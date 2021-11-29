# Refaça o desafio 035 dos triangulos, acrescentando p recurso de mostrar que tipo de
# de triangulo será formado:

# - Equilatero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno : todos os lados diferentes

r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento.'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMA UM TRIANGULO! ' ,end='')
if r1 == r2 == r3:
    print('\033[0;32mEQUILATERO!')
elif r1 != r2 != r3 != r1:
    print('\033[0;33mESCALENO!')
else:
    print('\033[0;34mISOSCELES!')

