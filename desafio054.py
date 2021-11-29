# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import  date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    nasc = int(input('Em que ano {}º voce nasceu?'.format(c)))
    idade = atual - nasc
    if idade >= 21:
      totmaior += 1
    else:
      totmenor += 1
print(' Tevemos {} pessoas maiores de idade'.format(totmaior))
print(' tevemos {} pessoas menores de idade '.format(totmenor))


