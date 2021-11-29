# Crie um programa que leia NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO E cadastre -os
# ( com IDADE) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ANO DE CONTRATAÇÃO e o SALÁRIO. Calcule e acrescente, além da IDADE, com quantos
# anos a pessoa vai se APOSENTAR.

from datetime import datetime # para saber a data atual temos que pega a do computador
dados = dict()
dados['nome'] = str(input('nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc # nesse caso temos o ano atual
dados['cpts'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['cpts'] != 0:
   dados['contratação'] = int(input('Ano de contratação: '))
   dados['salárrio'] = float(input('Salário: R$ '))
   dados['aposentadoria'] = dados['idade'] + (dados['contratação']+ 35) - datetime.now().year
print('-='*15)
for k, v in dados.items():
    print(f' -- {k} tem o valor {v} ')

