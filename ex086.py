matriz = [[], [], []]
resultados = []
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {i}]: ')))
print('-+-' * 10)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()
