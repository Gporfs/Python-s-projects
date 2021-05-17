n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor:'))
print('''
=-=-=-=-=-=-=-=-==-=-=
[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA
=-=-=-=-=-=-=-=-=-=-=
''')
o = int(input())
while not o == 5:
    if o == 1:
        r = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, r))
    if o == 2:
        r = n1 * n2
        print('A multiplicação entre {} e {} resulta em {}'.format(n1, n2, r))
    if o == 3:
        r = max(n1, n2)
        print('O maior número entre {} e {} é {}'.format(n1, n2, r))
    if o == 4:
        n1 = int(input('Novo número: '))
        n2 = int(input('Novo número: '))
    o = int(input('''
=-=-=-=-=-=-=-=-==-=-=
[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA
=-=-=-=-=-=-=-=-=-=-=
'''))

