lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar not in 'SsNn':
        continuar = str(input('Tente novamente. Deseja continuar? [S/N] ')).strip().upper()
    if continuar in 'nN':
        break
pares = []
impares = []
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=' * 50)
print(f'A lista completa é {lista}')
print(f'Os valores pares são {pares}')
print(f'Os valores impares são {impares}')
