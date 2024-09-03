s = 0
maior = 0
mediaidade = 0
nomedomaisvelho = ''
countf = 0
menor = 0
for p in range(1,5):
    print('------- {}° Pessoa -------'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    s += idade
    if p == 1 and sexo in 'Mm':
        maior = idade
        nomedomaisvelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomedomaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        menor = idade 
        countf += 1

mediaidade = s / 4
print('A média de idade do grupo é de {} anos, '.format(mediaidade), end='')
print('o homem mais velho se chama {} e ele tem {} anos'.format(nomedomaisvelho, maior))
print('e tem {} mulheres abaixo de 20 anos.'.format(countf))
    

