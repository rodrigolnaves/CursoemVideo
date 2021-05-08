jogador = dict()
gols = list()
jogador['Nome'] = str(input('Nome do jogador: '))
p = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, p):
    gols.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['Gols'] = gols.copy()
jogador['Total'] = sum(gols)
print('<>' * 30)
print(jogador)
print('<>' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('<>' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'  =>Na partida {i}, fez {v} gols.')
# for c in range(0, len(jogador["Gols"])):
#     print(f'  => Na partida {c}, fez {jogador["Gols"][c]} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
