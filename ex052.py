# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
valida = 1
for c in range(2, num):
    if num % c == 0:
        valida = 0
        print(c)
        break
if valida == 0:
    print('Não é primo.')
else:
    print('É primo.')
