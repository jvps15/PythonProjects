s = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while s not in 'MmFf':
   s = str(input('Desculpe, sexo não validado, Digite novamente: ')).strip().upper()[0]
print(' ')
if s in 'M':
    print('Seu sexo é Masculino, logo sexo validado, obrigado pela participação.')
else:
    print('Seu sexo é feminino, valeu pela participação gata!')
print(' ')