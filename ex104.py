def cores(cor):
    a = {'vermelho': '\033[1;31m',
         'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m'}
    return a[cor]


def leia_int(msg):
    global n
    while True:
        n = str(input(f'{msg}')).strip()
        if n.isnumeric():
            n = int(n)
            break
        else:
            print(cores('vermelho'), 'ERRO! Digite um número inteiro válido.\033[m', sep='')
    return n


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
