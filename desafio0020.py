# o mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Qaurto aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista) # esse comando server para heterogenar as lista
print('A ordem de apresentação será')
print('='*20)
print(lista)

'''outros metados

from random import shuffle

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno:'))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print(' A ordem que apresentamos será?')
print(lista) '''

