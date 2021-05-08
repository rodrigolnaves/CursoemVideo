distancia = float(input('Qual a distancia da sua viagem em km? '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O Valor da passagem será de R${:.2f}'.format(preco))
