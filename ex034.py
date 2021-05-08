salario = float(input('Digite o seu salário: R$'))
if salario <= 1250.00:
    novoSalario = (salario * 0.15) + salario
else:
    novoSalario = (salario * 0.10) + salario
print('Seu novo salário é de R${:.2f}'.format(novoSalario))
