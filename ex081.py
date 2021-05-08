lista = []
op = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op in 'S' or op in 'N':
            break
        else:
            print('Opção inválida')
    if op == 'N':
        break
print('=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')