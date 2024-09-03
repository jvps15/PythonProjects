casa = int(input('Qual é o valor da casa? R$')) 
salario = int(input('Sálario do comprador? R$')) 
anos = int(input('Quantos anos de financiamento? '))
meses = anos * 12
parcela = casa / meses
print('Para pagar um casa de R$\033[0;32m{}\33[m em \033[0;32m{}\33[m anos, será nescessário uma parcela mensal de R$\033[0;32m{:.2f}\33[m.'.format(casa, anos, parcela))
if parcela > salario * 30/100:
    print('\033[0;31mEMPRESTIMO NEGADO!\33[m')
else:
    print('\033[0;32mEMPRESTIMO APROVADO!\33[m')
