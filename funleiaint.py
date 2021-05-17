def leiaint(entrada):
    n = input(entrada)
    n = n.strip()
    if n.isnumeric():
        return int(n)
    else:
        while True:
            print('\033[31mERRO! DIGITE UM NÚMERO INTEIRO!\033[m')
            print('-'*35)
            n = input(entrada)
            if n.isnumeric():
                break
        return int(n)


num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
