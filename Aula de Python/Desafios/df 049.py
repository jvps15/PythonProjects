print('-=' * 20)
print('             TABUADA')
print('-=' * 20)
print(' ')
n = int(input('Digite um número: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, (c * n)))