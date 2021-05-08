from time import sleep


def titulo(tit, cor):
    cores = {'vermelho': '\033[1;41m',
             'azul': '\033[1;44m',
             'amarelo': '\033[1;43m',
             'verde': '\033[1;42m',
             'branco': '\033[1;40m',
             'limpa': '\033[m'}
    print(cores[cor], end='')
    print('~' * (len(tit) + 4))
    print(f'  {tit}')
    print('~' * (len(tit) + 4))
    print(cores['limpa'], end='')
    sleep(1)


def ajuda(msg):
    titulo(f'Acessando o manual do comando \'{msg}\'', 'azul')
    print('\033[1;40m')
    help(msg)
    print('\033[m', end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    comando = str(input('Função ou Biblioteca > ')).strip()
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 'vermelho')
        break
    else:
        ajuda(comando)
