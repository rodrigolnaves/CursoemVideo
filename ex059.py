from time import sleep
from os import system
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
linha = '=-=' * 8
while op != 5:
    print('   [ 1 ] somar\n'
          '   [ 2 ] multiplicar\n'
          '   [ 3 ] maior\n'
          '   [ 4 ] novos números\n'
          '   [ 5 ] sair do programa\n'
          '>>> Qual é a sua opção?', end=' ')
    op = int(input())
    if op == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
        else:
            print('Os números são iguais')
    elif op == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print(linha)
    sleep(2)
    system('clear')
print('Fim do programa. Volte sempre!')
