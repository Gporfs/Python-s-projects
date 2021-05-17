primeiro = int(input('Digite o primeiro termo da P.A.: '))
razão = int(input('Digite o razão da P.A.: '))
termo = primeiro
contador = 1
opção = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    contador += 1
while not opção == 0:
    opção = int(input('\nDeseja adicionar mais quantos termos? '))
    contador = 1
    while not contador == opção + 1:
        termo += razão
        print('{} -> '.format(termo), end='')
        contador += 1
print('FIM')
