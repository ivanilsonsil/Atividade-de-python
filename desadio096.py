# Faça um programa que tenha uma função chamada área(), que receba
# as dimensões de um terreno rantangulo(largura e comprimento)
# e mostre area do terreno.



def área(larg,comp):
    a = larg*comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')

# programa principal
print('Controle de terreno')
print('=-='*20)
l = float(input('LARGURA (M)'))
c = float(input('COMPRIMENTO (M:)'))
área(l,c)

