num = int(input('Vamos calcular a tabuada de um número inteiro!!\n'
                'Digite um número inteiro: '))
print('-'*10)
for c in range(1, 11):
    print('{} x {:2} = {:>2}'.format(num, c, num * c))
print('-'*10)
