from random import randint
computador = randint(0, 5)
print('\33[0;34m -=-' * 20)
print('\33[4;33mVou pensar num número de 0 a 5, Você consegue advinhar?')
print('\33[0;34m -=-' * 20)
u = int(input('\33[7;30m Em que número você acha que eu pensei? \33[m'))
c = 0
while u != computador:
    u = int(input('\33[7;30mVixe gatão, errou em, tenta de novo ai: \33[m'))
    c += 1
if c < 3:
    print('Ta vendo tu rato de recife, tu só precisava de um chega pra acertar, tu acertou em {} tentativas'.format(c + 1))
elif c > 3:
    print('meu pirraia, nem jogue no bixo que você só vai perder dinheiro, tu precisou de {} tentativas pra acertar'.format(c + 1))
    
