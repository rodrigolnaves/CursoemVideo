nome = str(input('Digite o nome completo: ')).strip()
print('Nome completo é: {}'.format(nome))
primeiro = (nome.split())[0]
ultimo = (nome.split()[-1])
print('Primeiro nome: {}'.format(primeiro))
print('Último nome: {}'.format(ultimo))
