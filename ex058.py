from random import randint
num = randint(0, 100)
cont = 1
print('Vou pensar em um número entre 0 e 100.')
escolha = int(input('Qual número você acha que eu pensei? '))
while escolha != num:
    if num < escolha:
        escolha = int(input('Menos... Tente mais uma vez: '))
        cont += 1
    else:
        escolha = int(input('Mais... Tente mais uma vez: '))
        cont += 1
print('Acertou com {} tentativas'.format(cont))
