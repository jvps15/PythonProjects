from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('-=' * 20)
print('       JOKENPO!!!')
print('-=' * 20)
print(' ')
print('''Suas opções:
      [ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] Tesoura ''')
j = int(input('Sua escolha: '))
print('-=' * 20)
print(' ')
if comp == 0:
    if j == 0:
        print('O Computador jogou {}, então vocês EMPATARAM!'.format(itens[0]))
    elif j == 1:
        print('O Computador jogou {}, então Você GANHOU'.format(itens[0]))
    elif j == 2:
        print('O Computador jogou {}, então Você PERDEU'.format(itens[0]))
    else:
         print('JOGADAD INVALIDA')
elif comp == 1:
    if j == 0:
         print('O Computador jogou {}, então você PERDEU!'.format(itens[1]))
    elif j == 1:
         print('O Computador jogou {}, então vocês EMPATARAM!'.format(itens[1]))
    elif j == 2:
         print('O Computador jogou {}, então você GANHOU!'.format(itens[1]))
    else:
         print('JOGADAD INVALIDA')
elif comp == 2:
    if j == 0:
         print('O Computador jogou {}, então você GANHOU!'.format(itens[2]))
    elif j == 1:
         print('O Computador jogou {}, então você PERDEU!'.format(itens[2]))
    elif j == 2:
         print('O Computador jogou {}, então vocês EMPATARAM!'.format(itens[2]))
    else:
         print('JOGADAD INVALIDA')
print(' ')
print('-=' * 20)
print(' ')

    