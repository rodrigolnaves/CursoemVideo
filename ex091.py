from random import randint
from time import sleep
from operator import itemgetter
pos = 1
jogadores = {'Jogador-01': randint(1, 6),
             'Jogador-02': randint(1, 6),
             'Jogador-03': randint(1, 6),
             'Jogador-04': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores:')
for k, v in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
    print(f'Em {pos}º lugar: {k} com {v}')
    pos += 1
