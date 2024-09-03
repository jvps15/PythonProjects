from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano 
atual = date.today().year
print('Você nasceu em {} e tem {} em {}.'.format(ano, idade, atual))
if idade < 18:
    print('Você ainda não precisa se alistar')
    n = 18 - idade
    print('Você so precisará se alistar em {} quando tiver 18.'.format(atual + n ))
elif idade > 18:
    print('Você ja deveria ter se alistado!')
    n1 = idade - 18
    print('Você deveria ter se alistado em {}'.format(atual - n1))
else:
    print('Você deve se alistar IMEDIATAMENTE!')