#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
# Desconsiderando os espços.

# ex:
# APOS A SOPA
# A SACADA DA CASA

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = juntos[::-1]
print('O inverso de {} é {}'.format(juntos,inverso))
if inverso == juntos:
    print('Temos um palindromo! ')
else:
    print('A frase digitada não é palindrome')




    '''
    for letra in range (len(juntos) -1,-1,-1): >> no lugar codigo substituimos por >>inverso = juntos[:: -1]: <<
        inverso += juntos[letra]
        '''