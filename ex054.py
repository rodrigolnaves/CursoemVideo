from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Qual a idade da {}ª pessoa? '.format(c)))
    if date.today().year - ano >= 21:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'
      '\nE também tivemos {} pessoas menores de idade'.format(maior, menor))
