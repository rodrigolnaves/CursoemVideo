print('-'*40)
print('{:^40}'.format('SEQUÊNCIA DE FIBONACCI'))
print('-'*40)
termo = int(input('Quantos termos você quer mostrar? '))
c = 1
primeiro = 0
segundo = 1
soma = 0
while c <= termo:
    print('{}'.format(primeiro), end=' -> ')
    soma = primeiro + segundo
    primeiro = segundo
    segundo = soma
    c += 1
print('FIM')
