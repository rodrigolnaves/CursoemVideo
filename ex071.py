print('='*30)
print(f'{"BANCO NAVES":^30}')
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if valor == 0:
            break
print('='*30)
print('Volte sempre ao BANCO NAVES. Tenha um bom dia!')