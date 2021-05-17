from builtins import ValueError


def linha(n=40):
    print('-' * n)


def destaque(msg):
    linha(40)
    print(f"{msg:^40}")
    linha(40)


def seletor(*ops):
    cont = 0
    for o in ops:
        for c in o:
            cont += 1
    # Não usar a parte a cima em outros códigos!

    try:
        s = int(input('Selecione:'))
        if s > cont:
            print('O valor inserido não corresponde com nenhuma das opções!')
    except ValueError:
        print('Favor inserir um número inteiro compatível com uma das opções')
    except TypeError:
        print('Favor inserir um número inteiro compatível com uma das opções')
    else:
        return s


def menu(*ops):
    while True:
        destaque('MENU PRINCIPAL')
        for num, o in enumerate(ops):
            print(f'{num + 1}- {o}')
        print('-' * 40)
        s = seletor(ops)
        if s != None:
            if s <= len(ops):
                break
    return s
