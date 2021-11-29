# Aprimore o DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES,incluindo
# um sistema de visualização de DETALHES DO APROVEITAMNETO de cada jogador.

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('nome do jogador:'))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'  Quantas gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S OU N .')
    if resp == 'N':
        break
print('-='*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'* 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostre dados de qual jogador? (999 para para)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f' ERRO! Não existe jogador com código{busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i} fez {g} gols.')
    print('-'*40)
print(' << VOLTE SEMPRE >>')








