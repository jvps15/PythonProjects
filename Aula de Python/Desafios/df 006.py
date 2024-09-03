n = int(input('Digite um número:'))

#pow(n, 2) Também é uma forma de escrever um potenciação, {:.2f} define que o número flutuante só tera duas casas decimais

print('O dobro do número infomado é {}, \n O triplo é {} \n E a raíz quadrada é {:.2f}'.format((n*2), (n*3), (pow(n, (1/2)))))