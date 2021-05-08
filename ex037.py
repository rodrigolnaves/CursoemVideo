num = int(input('Escreva um número inteiro qualquer: '))
escolha = int(input('''Escolha a base de conversão:
Digite [ 1 ] para binário
Digite [ 2 ] para octal
Digite [ 3 ] para hexadecimal
Qual sua escolha? '''))
if escolha == 1:
    print('Você escolheu a opção 1.')
    num = bin(num)[2:]
    print(num)
elif escolha == 2:
    print('Você escolheu a opção 2.')
    num = oct(num)[2:]
    print(num)
elif escolha == 3:
    print('Você escolheu a opção 3.')
    num = hex(num)[2:]
    print(num)
else:
    print('Opção inválida!')
