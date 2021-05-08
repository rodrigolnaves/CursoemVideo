from time import sleep


def contador(inicio, final, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('=' * 30)
    print(f'Contagem de {inicio} até {final} de {passo} em {passo}')
    if inicio < final:
        final += 1
    if inicio > final:
        final -= 1
        passo *= -1
    sleep(1)
    for c in range(inicio, final, passo):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
