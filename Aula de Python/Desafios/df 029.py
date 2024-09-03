v = float(input('Qual a velocidade do carro? '))

#multa
if v > 80:
    m = v - 80
    m1 = m * 7
    print('\33[0;31mVelocidade excedida em {} quilometros!\33[m Será nescessário o pagamento de uma multa de \33[4;32mR${:.2f}\33[m!'.format(m, m1))
else:
    print('\33[4;32mParabéns pela responsabilidade!\33[m')

print('Continue Dirigindo com cuidado!')