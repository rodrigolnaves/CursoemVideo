primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))
maior = primeiro
menor = primeiro
if maior < segundo:
    maior = segundo
if maior < terceiro:
    maior = terceiro
if menor > segundo:
    menor = segundo
if menor > terceiro:
    menor = terceiro
print('Maior: {} ----- Menor:{}'.format(maior, menor))
