#P.A com while

p = int(input('Qual o primeiro termo da progressão: '))
r = int(input('Qual a razão dessa progressão: '))
c  = 0 
total = 0
mais = 10
print('Os 10 primeiros termos dessa P.A são os seguintes:')
print(' ')
while mais != 0:
    total += mais
    while c < total:
        p += r
        c += 1
        print('{} ->'.format(p), end=' ')
    print('PAUSA')
    print(' ')
    mais = int(input('Quantos números a mais você quer? '))
print('FIM!')
    