lista = list()
for pos in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {pos}: ')))
print('*' * 30)
print(f'Você digitou os valores {lista}.')
print(f'O MAIOR valor digitado foi {max(lista)} nas posições: ', end='')
for c in range(0, 5):
    if max(lista) == lista[c]:
        print(f'{c}...', end='')
print(f'\nO MENOR valor digitado foi {min(lista)} nas posições: ', end='')
for c in range(0, 5):
    if min(lista) == lista[c]:
        print(f'{c}...', end='')
