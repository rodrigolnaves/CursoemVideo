from random import randint
from time import sleep
jogo = []
total = []
c = 0
print('--$--' * 6)
print(f'{"JOGA NA MEGA SENA":^30}')
print('--$--' * 6)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, qtd):
    while c < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            c += 1
    total.append(jogo.copy())
    jogo.clear()
    c = 0
print(f'Sorteando {qtd} jogos')
for i in range(0, len(total)):
    print(f'Jogo {i + 1}: {sorted(total[i])}')
    sleep(0.8)
print('Boa sorte!')
