texto = str(input('Digite o texto: ')).strip()
valida = 0
textofinal = ''
for c in range(0, len(texto)):
    if texto[c] != ' ':
        textofinal += texto[c]
print(textofinal)
final = len(textofinal) - 1
for c in range(0, len(textofinal)):
    if textofinal[c] == textofinal[final]:
        final -= 1
    else:
        valida = 1
        break
if valida == 0:
    print('A palavra é PALÍNDROMO')
else:
    print('A palavra NÃO É UM PALÍNDROMO')
