turma = list()
aluno = list()
notas = [0, 0]
op = ''
while True:
    aluno.append(str(input('Nome: ')).strip())
    notas[0] = float(input('Nota 1: '))
    notas[1] = float(input('Nota 2: '))
    aluno.append(notas.copy())
    turma.append(aluno.copy())
    aluno.clear()
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op in 'S' or op in 'N':
            break
        else:
            print('Opção inválida. Digite "S" para Sim e "N" para Não')
    if op == 'N':
        break
print('-' * 27)
print(f'{"Nº.":<4}', f'{"NOME":<16}', f'{"MÉDIA":<6}')
print('-' * 27)
for c, item in enumerate(turma):
    media = (item[1][0] + item[1][1]) / 2
    print(f'{c:<4}', f'{item[0]:<16}', f'{media:>6.1f}')
print('-' * 27)
while True:
    a = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if a == 999:
        break
    else:
        print(f'Notas de {turma[a][0]} são {turma[a][1]}.')
        print('-' * 27)
print('FINALIZANDO...')
print('<<<VOLTE SEMPRE>>>')
