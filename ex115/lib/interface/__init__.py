def cor(cor_escolhida):
    lista_de_cores = {'vermelho': '\033[1;031m',
                      'verde': '\033[1;032m',
                      'amarelo': '\033[1;033m',
                      'azul': '\033[1;034m',
                      'roxo': '\033[1;035m',
                      'ciano': '\033[1;036m',
                      'limpa': '\033[m'}
    return lista_de_cores[cor_escolhida]


def linha():
    print('-' * 42)


def titulo(msg):
    linha()
    print(f'{msg}'.center(42))
    linha()


def menu(lista):
    titulo('MENU PRINCIPAL')
    for i, opcao in enumerate(lista):
        print(f'{cor("amarelo")}{i + 1}{cor("limpa")} - {cor("azul")}{opcao}{cor("limpa")}')
    linha()
    opcao_escolhida = leia_int(f'Sua opção: ')
    return opcao_escolhida


def leia_int(msg):
    while True:
        try:
            n = int(input(f'{msg}'))
        except:
            print(f'{cor("vermelho")}ERRO! Digite um número inteiro válido.{cor("limpa")}')
            continue
        else:
            return n
