#Faça um mini-sistema que utilize 0 interactive do python
# usuario vai digita o comando e o manual vai aparecer
#quando o usuario digitar a paravra "fim' o programa se
#encerrará.


def comando(com):
    help(com)

def titulo(msg,cor = 0):
    tam = len(msg)
    print('==' * tam)
    print(msg)
    print('==' * tam)


# programa principal

comando =""
while True:
    titulo('sistema de ajuda pyhelp')
    comando = str(input("Função ou Biblioteca>"))
    if comando.upper() == 'FIM':
        break
    else:
        comando()


titulo('ate logo')