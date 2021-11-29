# Faça um programa que leia NOME É MÉDIA de um aluno,
# Guardando também a SITUAÇÃO em um DICIONÁRIO.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('NOME: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*15)
for k, v in aluno.items():
    print(f'{k} = {v} ')






