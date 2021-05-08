lista = []
op = ''
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado. Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op in 'S' or op in 'N':
            break
        else:
            print('Opção inválida')
    if op == 'N':
        break
print(('*' * 30))
lista.sort()
print(f'Você digitou os valores: {lista}')
