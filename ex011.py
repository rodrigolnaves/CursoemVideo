altura = float(input('Digite em metros a altura da parede: '))
largura = float(input('Digite em metros a largura da parede: '))
area = altura * largura
tinta = area / 2
print('A parede tem {} metros de altura e {} metros de largura.\n'
      'A sua área corresponde a {}m².\n'
      'Portanto, serão necessários {} litros de tinta para pintar a parede toda.'.format(altura, largura, area, tinta))
