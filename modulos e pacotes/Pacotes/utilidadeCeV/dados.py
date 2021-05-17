def leiadinheiro(msg):
    while True:
        n = str(input(msg)).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print(f'\033[31mErro: "{n}" não é um valor numérico!\033[m')
        else:
            break

    return float(n)


def leiaint(entrada):
    while True:
        try:
            n = int(input(entrada))

        except ValueError:
            print('-' * 42)
            print('\033[31mPor favor, insira apenas números inteiros.\033[m')
            print('-'*42)
        except KeyboardInterrupt:
            print('\033[31mO usuário não informou os dados.\033[m')
            return 0
        else:
            break

    return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print('-' * 39)
            print('\033[31mPor favor, insira apenas números reais.\033[m')
            print('-' * 39)
        except KeyboardInterrupt:
            print('\033[31mO usuário não informou os dados.\033[m')
            return 0
        else:
            break
    return n
