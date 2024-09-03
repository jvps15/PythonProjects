print('Seja bem-vindo, siga as instruções abaixo e iremos converter essa distância pra você!!\n')
m = float(input('Digite uma distância em metros:'))
mm = m * 1000
cm = m * 100
dm = m * 10 
dc = m / 10
hc = m / 100
km = m / 1000
print('Abaixo segue as conversões:\n mílimetros = {}\n centímetros = {}\n decímetros = {}\n decametros = {}\n hectametros = {}\n quilometros = {}'.format(mm, cm, dm, dc, hc, km))