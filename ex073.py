tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'Sao Paulo',
          'Atletico-MG', 'Atletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
          'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceara',
          'Vasco', 'Sport', 'America-MG', 'Vitoria', 'Parana')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 20)
print(f'Os cinco primeiros são: {tabela[0:5]}')
print('-=' * 20)
print(f'Os quatro últimos são: {tabela[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(tabela)})')
print('-=' * 20)
print(f'A Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição')

