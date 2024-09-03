nome = str(input('Qual o nome desse aluno? ')).strip()
n = float(input('Digite a primeira dele(a): '))
n1 = float(input('Digite a segunda dele(a): '))
m = (n1+n)/2

if m >= 6.0:
    print('Sua média foi boa, Você foi aprovado')
elif 3 < m < 6:
    print('Você está de recuperação')
else:
    print('Você está na final')
    
print('A média de {} é {:.1f} '.format(nome, m))