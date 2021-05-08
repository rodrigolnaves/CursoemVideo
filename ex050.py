print('Soma apenas dos números pares')
soma = 0
for c in range(0, 6):
    num = int(input('Digite o {}º número: '.format(c+1)))
    if num % 2 == 0:
        soma += num
if soma == 0:
    print('Não foi digitado nenhum número par!')
    print('Soma = {}'.format(soma))
else:
    print('Soma = {}'.format(soma))
