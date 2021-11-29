# Crie um programa que gerencie o aproveitamneto de um JOGADOR DE FUTABOL. O
# programa vai ler o NOME DO JOGADOR e QUANTAS PARTIDADAS ele jogou. Depois vai ler a
# quantidade de gols feitos em CADA PARTIDA. No final, tudo isso será guardado em um dicionário,
# incluindo o TOTAL DE GOLS feitos durante o campeonato.

jogador = dict()
partidas = list()
jogador['nome'] = str(input('nome:'))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0,tot):
    partidas.append(int(input(f'  Quantas gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*15)
print(jogador)
print('-='*15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*15)
print(f' O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.' )
for i , v in enumerate(jogador['gols']):
   print(f' => Na partidada {i}, fez {v} gols.')
print(f'foi um total de {jogador["total"]}gols.')


