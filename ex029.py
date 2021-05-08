vel = float(input('Digite a velocidade atual do carro: '))
limite = float(80.00)
valormulta = float(7.00)
if vel > limite:
    print('Você foi multado!!')
    print('Valor da multa é de R${:.2f}'.format((vel - limite) * valormulta))
else:
    print('Você não foi multado, pois sua velocidade é abaixo ou igual ao limite de {}km/h.'.format(int(limite)))
    print('Sua velocidade é de {}km/h'.format(vel))
