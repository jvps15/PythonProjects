cont = s = n = 0
while True:
    n = int(input('Digite um número qualquer(para parar digite 999): '))
    if n == 999:
        break           
    s += n
    cont += 1
print(f'Você digitou {cont} números e a soma deles é {s}')