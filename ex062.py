print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
inicio = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contTermo = 10
c = 1
termo = 10
while termo != 0:
    while c <= termo:
        print('{}'.format(inicio), end=' -> ')
        c += 1
        inicio += razao
    print('PAUSA')
    termo = int(input('Quantos termos você quer mostrar mais? '))
    c = 1
    contTermo += termo
print('Progressão finalizada com {} termos mostrados'.format(contTermo))
