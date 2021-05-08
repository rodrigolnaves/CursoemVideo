from emoji import emojize
from time import sleep
print('Contagem regressiva para o estouro dos fogos de artifícios!!!')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
for c in range(0, 8):
    print(emojize(':fireworks: '), end=' ')
    sleep(0.25)
