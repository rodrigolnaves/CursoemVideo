frase = str(input('Digite uma frase: ')).strip()
print('Sua frase tem {} letras "a".'.format(frase.upper().count('A')))
print('A letra "a" aparece a 1ª vez na posição "{}".'.format(frase.upper().find('A') + 1))
print('A letra "a" aparece a última vez na posição "{}".'.format(frase.upper().rfind('A') + 1))
