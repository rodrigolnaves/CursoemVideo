def area(larg, comp):
    res = larg * comp
    print(f'A área de um terreno {larg:.1f} x {comp:.1f} é de {res:.1f}m².')


print('-' * 40)
print(f'{"CONTROLE DE TERRENOS":^40}')
print('-' * 40)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
