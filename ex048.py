print('Mostrar soma de números ímpares e múltiplos de 3:')
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
s = 0
conta = 0
for c in range(i, f + 1):
    if c % 2 == 1 and c % 3 == 0:
        conta +=1
        s += c
print('Total = {}'.format(conta))
print('Soma = {}'.format(s))
print('FIM')
