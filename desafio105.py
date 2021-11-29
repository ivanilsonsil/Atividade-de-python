#Exercício Python 105: Faça um programa
# que tenha uma função notas() que pode receber várias notas de
# alunos e vai retornar um dicionário com as seguintes
# informações:

#Quantidades de notas
# a maior nota
#a menor nota
#a media da turma
#a situação (opcional)

def notas(*n,sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] ='BOA'
        elif r['media'] >= 5:
           r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r





    return r



# programar Principal

resp = notas(5.5,2.5,9,8.5, sit=True)
print(resp)