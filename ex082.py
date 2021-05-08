valores = []
pares = []
impares = []
op = ''
while True:
    valores.append(int(input('Digite um número: ')))
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op != '':
            if op in 'S' or op in 'N':
                break
            else:
                print('Opção inválida.')
        else:
            print('Opção inválida.')
    if op == 'N':
        break
# for c in range(0, len(valores)):
#     if valores[c] % 2 == 0:
#         pares.append(valores[c])
#     else:
#         impares.append((valores[c]))
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=-=' * 10)
print(f'A lista completa é: {valores}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')
