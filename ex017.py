from math import hypot
cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
print('A hipotenusa é igual a: {:.2f}.'.format(hypot(cat_oposto, cat_adjacente)))
