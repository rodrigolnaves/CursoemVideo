nome = input('Digite o seu nome completo: ')
print('Tudo maiúsculo: {}'.format(nome.upper()))
print('Tudo minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras ao todo, sem considerar espaços: {}'.format(len(nome) - nome.count(' ')))
pnome = nome.split()
print('Seu primeiro nome é {} e a quantidade de letras no primeiro nome: {}'.format(pnome[0], len(pnome[0])))