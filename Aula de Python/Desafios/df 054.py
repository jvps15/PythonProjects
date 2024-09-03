from datetime import date
c1 = 0
c2 = 0 
atual = date.today().year
for i in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
    idade = atual - ano
    if idade >= 21:
        c1 += 1
    else:
        c2 += 1 
print('Ao todo tivemos {} de maiores e {} de menores'.format(c1, c2))