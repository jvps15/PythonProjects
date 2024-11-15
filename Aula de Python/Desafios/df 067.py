n = num = 0
while True:
    num = int(input('Digite um número que você quer ver a tabuada: '))
    if num <= -1:
        break
    n = 0 
    while n <= 10:
        n += 1
        print(f'{n} x {num} = {n * num}')
print('Programa Finalizado!')

