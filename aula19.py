'''
pessoas = {'nome': 'del','sexo':'M', 'idade': 22}
print(f'O {pessoas ["nome"]} tem {pessoas["idade"]} anos.')

pessoas = {'nome': 'Gustavo','sexo': 'M','idade': 22}
print(pessoas.items())

pessoas = {'nome': 'Gustavo','sexo': 'M','idade': 22}
del pessoas['idade']
for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas = {'nome': 'Gustavo','sexo': 'M','idade': 22}
pessoas['nome'] = 'iara' # substituir nome
print(pessoas)
'''
'''
pessoas = {'nome': 'Gustavo','sexo': 'M','idade': 22}
pessoas['peso'] = 98.5 # podemos adicionar elemento
for k, v in pessoas.items():
    print(f'{k} = {v}')
    
'''

# AGORA EREMOS CRIAR UM DICIONÁRIO DENTRO DE UMA LISTA
'''
brasil = []
estado1 ={'uf': 'Rio de janeiro', 'Sigla':'SP'}
estado2 ={'uf': 'São paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

'''
'''
estado = dict()
brasil = list()
for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
'''
