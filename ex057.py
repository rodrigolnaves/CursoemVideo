sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()
if sexo == 'M':
    print('Você digitou sexo MASCULINO')
else:
    print('Você digitou sexo FEMININO')
