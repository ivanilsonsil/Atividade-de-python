# Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da tabela do CAMPEONATO BRASILEIRO
# DE FUTEBOL, na ordem de colocação. Depois mostre:

# A) Apenas os 5 PRIMEIROS COLOCADOS.
# B) Os ÚLTIMOS 4 colocados da tabela.
# C) Uma lista com os times em ORDEM ALFABÉTICA.
# D) Em qual POSIÇÃO na tabela está o time da chapecoense.

classi = ('São Paulo', 'Internacional','Atlético-MG','flamengo','Palmeiras',
          'Gremeio','Fluminense','Santos','Corinthians','Athetico-PR',
          'Ceará SC', 'Bragantino','Atlético-GO', 'Sport Recife','Vasco da gama',
          'Fortaleza','Bahia','Goiás','coritiba', 'Botafogo')


print('==================\033[0;33mCLASSIFICAÇÃO DO BRASILEIRÃO\033[m=================')

#for c in classi :
    #print(c)
print('-='*20)
print(f'Lista de Times:{classi}')
print('-='*20)
print(f'\033[0;34mOs 5ª primeiros colocados {classi[0:5]}\033[m')
print('-='*20)
print(f'\033[0;32m últimos 4ª Colocados.{classi[16:]}\033[m')
print('-='*20)
print(f'\033[0;31mTimes em ordem alfabética: {sorted(classi)}\033[m')
print('-='*20)
print(f'O palmeiras está na {classi.index("Palmeiras")+1}ªposição')

