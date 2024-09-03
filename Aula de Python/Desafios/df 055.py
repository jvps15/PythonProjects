maior = 0 
menor = 0
for p in range(1,6):
    peso = float(input('Quanhto pesa a {}° pessoa? '.format(p)))
    if p == 1: #estamos supondo que o maior e menor peso é o primeiro
        maior = peso 
        menor = peso 
    else: #agora estamos comferindo pra saber se ele realmente sera o menor e maior
        if peso > maior: 
            maior = peso
        if peso < menor:
            menor = peso 
print('O maior peso registrado foi {} e o menor foi {}'.format(maior, menor))