print('='*30)
print(f'{"LOJA NAVES":^30}')
print('='*30)
totCompra = maisDeMil = precoBarato = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    totCompra += preco
    if preco > 1000:
        maisDeMil += 1
    if precoBarato == 0 or preco < precoBarato:
        precoBarato = preco
        barato = produto
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
        if opcao in 'S' or opcao in 'N':
            break
        else:
            print('Opção inválida')
    if opcao == 'N':
        break
print(f'Total da compra foi R${totCompra:.2f}')
print(f'Temos {maisDeMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${precoBarato:.2f}')
