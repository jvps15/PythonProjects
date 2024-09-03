#Desafio 28 v2.0
from random import randint
computador = randint(1,10)
print('-=' * 20)
print('Adivinhe um número que eu vou pensar de 1 a 10')
print('-=' * 20)
acertou = False
c = 0
while not acertou:
    u = int(input('Fala o número ai caboclo: '))
    c += 1
    if u == computador:
        acertou = True
    else:
        if u < computador:
            print('Bota um número maior ai boy')
        elif u > computador:
            print('E é o doido é? bota um número menor tabacudo')
if c <= 3:
    print('Eita bixo rochedo do caramba, só precisou de {} tentativas'.format(c))
elif c <= 5:
    print('Tu foi até rochedinho, precisou só de {} tentativas, tá na média'.format(c))
elif c <= 8:
    print('Meus amigo, leve pra casa vá, taca poxa precisasse de {} tentativas'.format(c))
elif c >= 10:
    print('Desista vá, que das duas uma, ou você é burro ou você é doido, precisasse de {} tentativas'.format(c))
