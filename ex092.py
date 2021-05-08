from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Idade'] = date.today().year - int(input('Ano de nascimento: '))
dados['CTPS'] = str(input('Carteira de trabalho (0 não tem) :'))
if dados['CTPS'] != '0':
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + (35 - (date.today().year - dados['Contratação']))
print('#' * 25)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
