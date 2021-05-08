def linha():
    print('=' * 30)


linha()
print('{:^30}'.format('10 TERMOS DE UMA PA'))
linha()
inicio = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
while c < 10:
    print('{}'.format(inicio), end='')
    c += 1
    inicio += razao
    print(' -> ' if c < 10 else '', end='')

# for c in range(inicio, inicio + razao * 10, razao):
#    print('{} -> '.format(c), end='')
# print('ACABOU')
