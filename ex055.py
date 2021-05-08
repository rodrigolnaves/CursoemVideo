maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa? '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso

print('O MAIOR peso lido foi de {}Kg'
      '\nO MENOR peso lido foi de {}Kg'.format(maior, menor))
