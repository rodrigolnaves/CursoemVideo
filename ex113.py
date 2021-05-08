def cores(cor):
    a = {'vermelho': '\033[1;31m',
         'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m'}
    return a[cor]


def leia_int(msg):
    while True:
        try:
            n = int(input(f'{msg}'))
        except:
            print(cores('vermelho'), 'ERRO! Digite um número inteiro válido.\033[m', sep='')
            continue
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(f'{msg}'))
        except:
            print(cores('vermelho'), 'ERRO! Digite um número real válido.\033[m', sep='')
            continue
        else:
            return n


inteiro = leia_int('Digite um número inteiro: ')
real = leia_float('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
