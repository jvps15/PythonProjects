n = num = 0
while True:
    num = int(input('Digite um número que você quer ver a tabuada: ')) 
    while n <= 10:
        n += 1
        print(f'{n} x {num} = {n * num}')
    if num < 0:
        break

