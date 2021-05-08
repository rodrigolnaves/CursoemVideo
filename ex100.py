from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
        sleep(0.5)
    print('PRONTO!')


def somapar(lista):
    cont = soma = 0
    while cont < len(lista):
        if lista[cont] % 2 == 0:
            soma += lista[cont]
        cont += 1
    print(f'Somando os valores pares de {lista}, temos {soma}')


valores = list()
sorteia(valores)
somaPar(valores)
