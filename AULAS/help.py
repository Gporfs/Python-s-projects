def soma(*n):
    """
    -> Soma números que desejar.
    :param n: números a serem somados.
    :return: retorna a soma (s).
    """
    s = 0
    c = 0
    while c < len(n):
        s += n[c]
        c += 1
    return s


help(soma)
print(f'A soma resultou em: {soma(5, 6)}')
