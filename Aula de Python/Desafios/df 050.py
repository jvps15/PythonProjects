s = 0
cont = 0 
for c in range(1, 7):
    num = int(input('Digite o {}° número: '.format(c)))
    if num % 2 == 0:
        s = s + num
        cont = cont + 1 
print('A soma dos {} PARES é {}'.format(cont, s))
     