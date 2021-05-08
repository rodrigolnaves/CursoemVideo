def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número n.
    """
    fat = 1
    for c in range(n, 0, -1):
        fat *= c
        if show:
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    return fat


print(fatorial(2, True))
