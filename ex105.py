def notas(*n, sit=False):
    """
    -> Função para analisar notas e situção de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias situações da turma
    """
    lista = dict()
    lista['total'] = len(n)
    lista['maior'] = max(n)
    lista['menor'] = min(n)
    lista['media'] = sum(n) / len(n)
    if sit:
        if lista['media'] < 5:
            lista['situacao'] = 'Ruim'
        elif 5 <= lista['media'] < 7:
            lista['situacao'] = 'Regular'
        else:
            lista['situacao'] = 'Boa'
    return lista


#programa principal
resp = notas(5.5, 6.9, 6.5, 8, 8, sit=True)
print(resp)
