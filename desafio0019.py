# um professor quer sortear um dos seus quatro alunos para apagar o quadro
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random # biblioteca random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1,n2,n3,n4] # para o phyton uma lista ficar entre cochetes...
escolhido = random.choice(lista) # uma escolha dentro da lista <random.choice> escolhe um valor
print('O aluno escolhido foi {}'.format(escolhido))

''' outros métados

from random import choice

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

'''

