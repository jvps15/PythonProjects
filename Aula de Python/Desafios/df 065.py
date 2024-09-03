resp = 'S'
num = soma = cont = menor = maior = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [N/S] '))
m = soma / cont
print('Você digitou {} números e a média deles é {}'.format(cont, m))
print('O maior número entre eles é {} e o menor é {:.2f}'.format(maior, menor))
print('Acabou')