print('{}{:#^40}{}'.format('\033[31m', ' LOJAS NAVES ', '\033[m'))
preco = float(input('Preço das compras> R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    final = preco - (preco * 0.1)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, final))
elif opcao == 2:
    final = preco - (preco * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, final))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(preco / 2))
    print('Valor total da compra R${:.2f}.'.format(preco))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    final = preco + (preco * 0.2)
    valorParcelas = final / parcelas
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(parcelas, valorParcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, final))
else:
    print('Opção inválida. Tente novamente.')
print('{}{:#^40}{}'.format('\033[31m', ' FIM ', '\033[m'))
