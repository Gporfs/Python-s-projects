from time import sleep


def contador(i, f, p):
    if p < 0:
        p = -p
    print('-' * 40)
    if p == 0:
        p = 1
    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}:')
        for n in range(i, f + p, p):
            print(n, end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        cont = i
        print(f'Contagem de {i} até {f} de {p} em {p}:')
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez! Faça uma contagem personalizada.')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
