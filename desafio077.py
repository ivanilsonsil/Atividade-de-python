# Crie um programa que tenha TUPLA com VÁRIAS PALAVRAS (não usar acentos).
# Depois disso, voce deve mostrar, para cada palavra, quais são as suas VOGAIS.


palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'esetudar', 'praticar',
            'trabalho', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\n Na palavras {p.upper()} temos' ,end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


