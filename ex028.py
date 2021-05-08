from random import randint
from time import sleep
num = randint(0, 5)
print('Vou pensar em um número entre 0 e 5.')
escolha = int(input('Qual número você acha que eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if num == escolha:
    print('Parabéns! Você acertou. Eu pensei no número {}.'.format(num))
else:
    print('Que pena... não foi dessa vez. Eu pensei no número {}.'.format(num))
