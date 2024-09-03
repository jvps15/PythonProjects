n = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO número {} foi divisívél {} vezes'.format(n, tot), end='. ')
if tot == 2:
    print('Por ele mesmo e por um, por isso ele é primo')
else:
    print('Portanto ele não é um número primo')