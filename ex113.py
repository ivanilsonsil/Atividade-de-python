# Tratamento de erros e execeção

# Exemplo
try:
   a = int(input('Numerador: '))
   b = int(input('Denminador: '))
   r = a / b
except Exception as erro:
    print(f'Infelizmente tivemos um problema foi {erro.__class__}')

else:
  print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre! Muito obrigado')