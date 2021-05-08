soma = cont = media = maior = menor = 0
op = 'S'
while op != 'N':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    op = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / cont
print('Você digitou {} números e a média entre eles foi {}'.format(cont, media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))
print('FIM')
