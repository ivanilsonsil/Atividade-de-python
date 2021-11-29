# Crie um programa onde o usuario digite uma expressão qualquer que use parenteses.
#  Seu aplicativo deverá analisar se a expresão passada está com os paraenteses abertos e
# fechados na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('A sua expressão está válida :')
else:
    print('A sua expressão está invalida :')




