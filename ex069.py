mais18 = homem = mulherMenos20 = 0
while True:
    print('-'*30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade >= 18:
        mais18 += 1
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo in 'M' or sexo in 'F':
            break
        else:
            print('Opção inválida.')
    if sexo == 'M':
        homem += 1
    else:
        if idade < 20:
            mulherMenos20 += 1
    print('-' * 30)
    while True:
        op = str(input('Quer continuar: [S/N] ')).strip().upper()
        if op in 'N' or op in 'S':
            break
        else:
            print('Opção inválida.')
    if op in 'N':
        break
print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulherMenos20} mulheres com menos de 20 anos.')