matriz = [[], [], []]
pares = coluna = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite um valor para [{lin}, {col}]: ')))
        if matriz[lin][col] % 2 == 0:
            pares += matriz[lin][col]
        if col == 2:
            coluna += matriz[lin][col]
print('-+-' * 10)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
print('-+-' * 10)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
