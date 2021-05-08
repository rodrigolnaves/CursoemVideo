aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'RECUPERAÇÃO'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'REPROVADO'
print('#' * 25)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
