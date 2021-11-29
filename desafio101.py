#crie um programar que tenhs uma função chamada voto() que vi receber
# como paramentro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO,OPCIONAL E OBRIGATORIO NAS ELEIÇÕES

def voto(ano=0):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16<= idade <18 or idade > 65:
        return f' Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f' Com {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input("Informe seu ano de nascimento?"))
print(voto(nasc))