pessoa = [0, 0, 0]
totalIdade = 0
media = 0
nomeVelho = ''
idadeVelho = 0
mMenor20 = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    pessoa[0] = str(input('Nome: ')).strip()
    pessoa[1] = int(input('Idade: '))
    pessoa[2] = str(input('Sexo [M/F]: ')).strip().upper()
    totalIdade += pessoa[1]
    if pessoa[2] == 'F' and pessoa[1] < 20:
        mMenor20 += 1
    if pessoa[2] == 'M' and pessoa[1] > idadeVelho:
        idadeVelho = pessoa[1]
        nomeVelho = pessoa[0]
media = totalIdade / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(idadeVelho, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mMenor20))
