cidade = str(input('Digite o nome de uma cidade: ')).strip().split()
print('A cidade comeca com a palavra "Santo"? {}'.format(cidade[0].upper() == 'SANTO'))
