lista = list()
for c in range(0, 5):
    num = int(input('Digite uma valor: '))
    if c == 0:
        lista.append(num)
        print('Adicionada ao final da lista..')
    else:
        for i in range(0, len(lista)):
            if num <= lista[i]:
                lista.insert(i, num)
                print(f'Adicionado na posição {i} da lista...')
                break
            else:
                if i == (len(lista) - 1):
                    lista.append(num)
                    print('Adicionada ao final da lista..')
                    break
print('=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
