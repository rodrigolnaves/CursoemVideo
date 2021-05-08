import random
a1 = input('Digite o primeiro nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o terceiro nome: ')
a4 = input('Digite o quarto nome: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
# print('A ordem de apresentação será: {}'.format(random.sample([a1, a2, a3, a4], k=4)))
#print(random.sample([a1, a2, a3, a4], k=4))
