# Faça um algoritmo que leia o salário de um funcionario e mostre seu desconto novo salario, com 15% de desconto

sal = float(input('Digite o seu salário R$ '))
novo = sal + (sal * 15 / 100)
print('O salário que custava R${:.2f} com aumento de 15% seu salário agora é de R${:.2f}'.format(sal,novo))