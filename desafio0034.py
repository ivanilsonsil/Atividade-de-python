#Escreva um programa que  pergunte o salario de um funcionario e calcule o valor do seu aumento.
# para salario superiores a R$1.250,00, calcule um aumento de 10%.
# para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('\033[1;35mQual é o salario do funcionario? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario - (salario * 10 / 100)
print('\033[0;36mQuem ganhar R$ {:.2f} passa a receber {:.2f} agora.'.format(salario, novo))

