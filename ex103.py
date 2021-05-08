def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')


jogador = str(input('Nome do jogador: '))
tot_gols = str(input('Número de gols: '))
if tot_gols.isnumeric():
    tot_gols = int(tot_gols)
else:
    tot_gols = 0
if jogador.strip() == '':
    ficha(gols=tot_gols)
else:
    ficha(jogador, tot_gols)
