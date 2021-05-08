pilha = []
exp = str(input('Digite a expressão: ')).strip()
for i in exp:
    if i == '(':
        pilha.append(i)
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(i)
            break
if len(pilha) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
