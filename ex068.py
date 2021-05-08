from random import randint
print('=-' * 25)
print('{:^50}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
cont = 0
while True:
    print('=-' * 25)
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    while True:
        op = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
        if op == 'P':
            break
        elif op == 'I':
            break
        else:
            print('Opção inválida.')
    print('--' * 25)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('--' * 25)
    if op == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    if op == 'I':
        if soma % 2 == 0:
            print('Você PERDEU!')
            break
        else:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
print(f'GAME OVER! Você venceu {cont} vezes')