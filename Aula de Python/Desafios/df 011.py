print('Atenção!!! Todas as medidas a seguir devem ser dadas em metro!')

#input pra definir variavel de altura e comprimento da parede

h = float(input('Digite a Altura da sua parede:'))
c = float(input('Digite o comprimento da sua parede:'))

#Calculo da area da parede 

a = h * c 

#definir litros de tintas nescesarios 

l = a / 2

#print de exibição de litros de tinta nesces

print('Para pintar sua parede você precisara de {:.1f} litros de tinta'.format(l))