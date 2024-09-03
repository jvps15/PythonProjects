from datetime import date
print('-=' * 20)
print('       CLASSIFICADOR DE ATLETA')
print('-=' * 20)
print(' ')
ano = int(input('Em que ano Você nasceu? '))
idade = date.today().year - ano
print(' ')
if idade == 9:
    print('Você tem {} anos então se clasifica como MIRIM'.format(idade)) 
elif idade > 9 and idade <= 14:
    print('Você tem {} anos então se clasifica como INFANTIL'.format(idade))
elif idade > 14 and idade <= 18:
    print('Você tem {} anos então se clasifica como JUNIOR'.format(idade))
elif idade > 18 and idade <= 25:
    print('Você tem {} anos então se clasifica como SENIOR'.format(idade))
elif idade > 25:
    print('Você tem {} anos então se clasifica como MASTER'.format(idade))
else:
    print('!!!' * 10)
    print(' ')
    print('OPA! Parece que você não tem idade o sufiente :(')
print(' ')
