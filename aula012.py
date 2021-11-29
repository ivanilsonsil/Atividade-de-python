nome = str(input('Qual é seu none? '))
if nome == 'Gustavo':
    print('Que nome bonito!!')
elif nome == 'Pedro' or nome == 'Aline' or nome == 'Mario' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal !! ')


print('Tenha um bom dia, {}!'.format(nome))

                # Estrutura Aninhada