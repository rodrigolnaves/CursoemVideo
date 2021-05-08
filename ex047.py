print('Mostrar todos os números pares:')
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
for c in range(i, f + 1):
    if c % 2 == 0:
        print(c, end=' - ')
print('FIM')
