#jeito importando biblioteca
'''from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f)'''

#jeito com while

n = int(input('digite um número: '))
f = n
c = 1
print(' Calculando...  {}! = '.format(n),end='')
while f > 0:
    print('{}'.format(f), end=' ')
    print('x' if f > 1 else '=', end=' ')
    c *= f
    f -= 1
print(c)

# jeito com for
'''n = int(input('Digite um número: '))
c = n
f = 1
for c in range (n, 0, -1):
    print('{}'.format(n), end=' ')
    print('x' if n > 1 else '=', end=' ')
    f *= n
    n -= 1
print(f)'''

