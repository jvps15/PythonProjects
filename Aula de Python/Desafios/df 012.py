p = float(input('Digite o preço do produto e mostraremos o preço do mesmo com 5% de desconto:'))
p1 = p * 5 / 100
print('O valor da roupa com desconto fica R${:.2f}'.format((p-p1)))