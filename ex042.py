r1 = float(input('Digite o valor do primeira segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 != r2 != r3 != r1:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
    elif r1 == r2 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓCELES!')
else:
    print('NAO... não é possível formar um triangulo!')