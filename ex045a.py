from random import randint
from time import sleep
print('{:#^40}'.format(' JOGO PEDRA PAPEL TESOURA '))
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jodada? '))
computador = randint(0, 2)
lista = ('Pedra', 'Papel', 'Tesoura')
if jogador < 0 or jogador > 2:
    print('JOGADA INVÁLIDA')
else:
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PO')
    print('=' * 40)
    print('O jogador escolheu {}.'.format(lista[jogador]))
    print('O computador escolheu {}.'.format(lista[computador]))
    print('=' * 40)
if computador == 0:  # PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1:  # PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2:  # TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
