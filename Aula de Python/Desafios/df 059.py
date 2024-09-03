from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
menu = 0 
while menu != 5:
    print(''' 
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Mostrar maior
        [ 4 ] Digitar novos números
        [ 5 ] Finalizar programa''')
    menu = int(input('>>>>>> Escolha a opção digitando o número correspondente: '))
    print(' ')
    if menu == 1:
        print('O resultado de {} + {} é {}.'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('O produto de {} x {} é {}.'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é {}.'.format(n1, n2, n1))
        elif n2 > n1:
            print('O maior número entre {} e {} é {}.'.format(n1, n2, n2))
        else:
            print('Entre {} e {} não há maior número já que são iguais.'.format(n1, n2))
    elif menu == 4:
        print('Informe os novos números abaixo:')
        print(' ')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Digite novamente.')
    print('-=' * 10)
    sleep(2)    
print('Programa finalizado!')

