#Analizador de triangulos
print('-=' * 20)
print('      ANALIZADOR DE TRIÂNGULOS')
print('-=' * 20)
print(' ')
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: ')) 
r3 = float(input('terceiro Segmento: ')) 
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Esses segmentos PODEM FORMAR UM TRIÂNGULO', end='')
    if r1 == r2 == r3:
        print(', e esse Triângulo será EQUILATERO.')
    elif r1 != r2 != r3 != r1:
        print(', e esse triângulo é ESCALENO.')
    else:
        print(', e esse Triângulo é ISOCELES')
else:
    print('Os Segmentos Acima não pode formar um Triângulo.')
