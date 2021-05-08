jogador = dict()
gols = list()
time = list()
while True:
    jogador['Nome'] = str(input('Nome do jogador: '))
    p = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, p):
        gols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['Gols'] = gols.copy()
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op == 'N' or op == 'S':
            break
        print('ERRO! Digite S ou N')
    if op == 'N':
        break
print('<>' * 21)
print(f'{"Cod":<3}', f'{"Nome":<15}', f'{"Gols":<15}', f'{"Total":<5}')
print('-' * 42)
for i, jog in enumerate(time):
    print(f'{i:>3}', f'{jog["Nome"]:<15}', f'{str(jog["Gols"]):<15}', f'{jog["Total"]:<5}')
    print('-' * 42)
while True:
    op = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if op == 999:
        break
    else:
        if op < 0 or op >= len(time):
            print(f'ERRO! Não existe jogador com código {op}')
        else:
            print(f'--Levantamento do jogador {time[op]["Nome"]}')
            for c, gol in enumerate(time[op]['Gols']):
                print(f'  No jogo {c + 1} fez {gol} gols.')
    print('-' * 42)
print('<<ENCERRADO>>')
