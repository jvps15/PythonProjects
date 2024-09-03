num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Ele tem {} unidades'.format(u))
print('Posui {} dezenas'.format(d))
print('Tem {} centenas'.format(c))
print('E tem {} milhares'.format(m))