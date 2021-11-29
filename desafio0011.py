# faça um programa que leia a largura e a altura de uma parede em
# metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-lá, sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('='*12)
print('sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(larg,alt,area))
tinta = area / 2
print('para pintar essa parede vc precisará de {}L de tintas:'.format(tinta))