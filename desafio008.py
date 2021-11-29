# Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milimetros.

medida = float(input('Uma distancia em metros!'))
cm = medida * 100
mm = medida * 1000
dam = medida * 0.1
hm = medida *0.01


print(' A medida de {}m corresponde {}cm {}mm {:.1f}dam {}hm'.format(medida,cm,mm,dam,hm))