# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA A PRIMEIRA E O
# ÚLTIMO NOME SEPARADAMENTE.

# EX Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {} '.format(nome[len(nome)-1]))