def metade(n, f=False):
    if f:
        return moeda(n / 2)
    else:
        return n / 2


def dobro(n, f=False):
    if f:
        return moeda(n * 2)
    else:
        return n * 2


def aumentar(n, percent, f=False):
    nn = n + (n * (percent / 100))
    if f:
        return moeda(nn)
    else:
        return nn


def diminuir(n, percent, f=False):
    nn = n - (n * (percent / 100))
    if f:
        return moeda(nn)
    else:
        return nn


def moeda(n):
    nn = f'R${n:.2f}'.replace('.', ',')
    return nn


def resumo(n, a, d):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'Preço analisado:   {moeda(n)}')
    print(f'Dobro do preço:    {dobro(n, True)}')
    print(f'Metade do preço:   {metade(n, True)}')
    print(f'{a}% de aumento:    {aumentar(n, a, True)}')
    print(f'{d}% de desconto:   {diminuir(n, d, True)}')
    print('-' * 40)
