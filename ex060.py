n = int(input('''Digite um número para
calcular seu fatorial: '''))
print('Calculando {}! = {}'.format(n, n), end='')
resultado = n
while n > 1:
    n -= 1
    resultado = resultado * n
    print(' x {}'.format(n), end='')
    if n == 1:
        print(' = {}'.format(resultado))
