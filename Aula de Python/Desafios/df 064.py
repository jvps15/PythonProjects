cont = num = soma = 0
num = int(input('Digite um número[Digiti 999 para parar o programa]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número[Digiti 999 para parar o programa]: '))
print('Você digitou {} números e a soma deles é {}.'.format(cont, soma))
print('Acabou!')
    