import math
valor = math.radians(float(input('Digite o valor do ângulo: ')))
print('Seno = {:.2f}\n'
      'Conseno = {:.2f}\n'
      'Tangente = {:.2f}'
      ''.format(math.sin(valor), math.cos(valor), math.tan(valor)))
