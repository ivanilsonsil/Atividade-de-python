# faça um programa que leia tres numeros e mostre qual é o maior e que é o menor

a = int(input('\033[0;31mPrimeiro valor:'))
b = int(input('\033[0;32mSegundo valor:'))
c = int(input('\033[1;33mTerceiro valor:'))
# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    # verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(' \033[0;37mo menor valor digtado foi {}'.format(menor))
print(' \033[0;32mo maior valor digitado foi {}'.format(maior))