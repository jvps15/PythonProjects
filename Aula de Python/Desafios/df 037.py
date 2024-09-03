n = int(input('Digite um número inteiro qualquer: '))
print('''Digite um dos números abaixo para escolher uma das opções:
      [ 1 ] Converter para Binário
      [ 2 ] Converter para Octal
      [ 3 ] Converter para Hexadecimal''')
print(' ')
escolha = int(input('Qual a sua escolha? '))
print(' ')
if escolha == 1:
    print('{} Convertido para Binário é {}.'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} Convertido para Octal é {}.'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} Convertido para Hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção invalida! tente novamente')
print(' ')
