def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * (taxa / 100))
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * (taxa / 100))
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0.0, moedas='R$'):
    return str(f'{moedas}{preco:.2f}').replace('.', ',')


def resumo(preco=0, aumento=10, reducao=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(preco):<10}')
    print(f'{"Dobro do preço:":<20}{dobro(preco, True):<10}')
    print(f'{"Metade do preço:":<20}{metade(preco, True):<10}')
    print(f'{aumento}{"% de aumento:":<18}{aumentar(preco, aumento, True):<10}')
    print(f'{reducao}{"% de aumento:":<18}{diminuir(preco, reducao, True):<10}')
    print('-' * 30)
