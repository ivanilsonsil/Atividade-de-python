# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag)

n = s = cont = 0
while True :
    n = int(input('\033[0;34mDigite um valor (999 para parar):'))
    if n == 999:
        break
    s+= n
    cont += 1
print(f'\033[0;36m A soma dos {cont} valores foi  {s}!!')

