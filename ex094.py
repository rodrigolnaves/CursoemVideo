familia = list()
pessoa = dict()
media = soma = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if pessoa['Sexo'] == 'M' or pessoa['Sexo'] == 'F':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    familia.append(pessoa.copy())
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op == 'N' or op == 'S':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if op == 'N':
        break
print('<o>' * 20)
print(f'A) - Ao todo temos {len(familia)} pessoas cadastradas.')
media = soma / len(familia)
print(f'B) - A média de idade é de {media:.2f} anos.')
print(f'C) - As mulheres cadastradas foram: ', end='')
for p in familia:
    if p['Sexo'] == 'F':
        print(p['Nome'], end=' ')
print(f'\nD) - Lista das pessoas que estão acima da média: ')
for p in familia:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print()
print('<< ENCERRADO >>')
