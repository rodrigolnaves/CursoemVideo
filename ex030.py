from colorize import colorize
num = int(input('Digite um número: '))
if num % 2 == 0:
    print.colorize('\033[7;32mO número é par!', str(num))
else:
    print.colorize('O número é ímpar!', str(num))
