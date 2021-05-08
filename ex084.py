pessoas = []
ind = []
op = ''
maior = menor = 0
nomeMaior = []
nomeMenor = []
while True:
    ind.append(str(input('Nome: ')))
    ind.append(float(input('Peso: ')))
    pessoas.append(ind.copy())
    ind.clear()
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op in 'S' or op in 'N':
            break
        else:
            print('Opção inválida.', end='')
    if op == 'N':
        break
print('=-=' * 20)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
for c, p in enumerate(pessoas):
    if c == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]
# for c, p in enumerate(pessoas):
#     if maior == p[1]:
#         nomeMaior.append(p[0])
#     if menor == p[1]:
#         nomeMenor.append(p[0])
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for c, p in enumerate(pessoas):
    if maior == p[1]:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menor} Kg. Peso de ', end='')
for c, p in enumerate(pessoas):
    if menor == p[1]:
        print(f'{p[0]}', end=' ')
