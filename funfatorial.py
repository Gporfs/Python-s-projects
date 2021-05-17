def fatorial(n, show=False):
    """
    -> Calcula fatorial de um número.
    :param n: número para o cálculo.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor de um fatorial de um número (n).
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
        f *= c
    return f


print(fatorial(5, True))
