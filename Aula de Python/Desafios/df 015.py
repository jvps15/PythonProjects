#aluguel de carros, sendo dia = 60 + km = 0,15

d = int(input('Quantos dias você ficou com o carro? '))
k = float(input('Quantos quilometros foi rodado com o mesmo? '))

#operação matematica

T = (60 * d) + (k * 0.15)

#print

print('Já que foram {} dias e {} quilometros rodados, o total a pargar é de R${:.2f}'.format(d, k, T))