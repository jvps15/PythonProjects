print('-='*30)
print('Sequência de Fibonacci')
print('-='*30)
n = int(input('Quantos números você quer ver? '))
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
c = 2
while c < n:
    t3 = t1 + t2
    print('{} -> '.format(t3),end='')
    t1 = t2
    t2 = t3
    c += 1
print('Fim')
'''while cont < n:
    ts = t1 + t2
    print('{} ->'.format(ts),end='')
    t1 = t2
    t2 = ts
print('Fim!')'''