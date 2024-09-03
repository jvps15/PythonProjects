frase = input('Qual o seu nome? ').strip()

print('Seu nome somente em letras maiusculas é {}'.format(frase.upper()))
print('Seu nome em letras minusculas é {}'.format(frase.lower()))
print('Seu nome possui {} letras'.format(len(frase) - frase.count(' ')))
frase1 = frase.split()
print('Seu primeiro nome é {} e ele possui {}'.format(frase1[0], len(frase1[0])))