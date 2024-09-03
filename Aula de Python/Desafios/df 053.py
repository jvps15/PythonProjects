f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
inverso = ''
for i in range(len(j) - 1, -1, -1):
    inverso += j[i]
print('O inverso de {} é {}'.format(j, inverso))
if inverso == j:
    print('é aquela bomba lá')
else:
    print('num é não pae')