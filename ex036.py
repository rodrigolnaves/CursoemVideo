from time import sleep
print('\033[1;33m-=\033[m'*20)
print('\033[1;43m*** SIMULADOR DE EMPRÉSTIMO BANCÁRIO ***\033[m')
print('\033[1;43m***      PARA COMPRAR UMA CASA       ***\033[m')
print('\033[1;33m-=\033[m'*20)
sleep(1)
nome = str(input('Por favor, informe seu primeiro nome: '))
print('Olá!!! Seja bem vindo, {}{}{}!!!'.format('\033[1;33m', nome, '\033[m'))
sleep(1)
valorDaCasa = float(input('Qual o valor da casa que deseja comprar? R$'))
salario = float(input('Qual o valor do seu salário mensal? R$'))
tempo = int(input('Em quantos anos você pretende pagar o financiamento? '))
valorPrestacao = valorDaCasa / (tempo * 12)
salario30 = salario * 0.3
print('OK!! Vamos agora analisar seus dados!')
print('EM ANÁLISE...')
sleep(2)
if salario30 < valorPrestacao:
    print('\033[1;31mInfelizmente seu empréstimo não foi aprovado!\033[m')
    print('O valor da prestação é maior que 30% do seu salário!')
    print('PRESTAÇÃO: R${:.2f}\n'
          '30% DO SALÁRIO: R${:.2f}'.format(valorPrestacao, salario30))
else:
    print('\033[1;36mPARABÉNS!!! Seu empréstimo foi aprovado!\033[m')
    print('O valor da prestação será de R${:.2f}!\n'
          'devendo ser pago em {} parcelas.'.format(valorPrestacao, tempo * 12))
print('Fim.')
