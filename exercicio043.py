maior = menor = 0
cont = 1
n = int(input('Digite um valor: '))
continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()
soma = n
while continuar in 'Ss':
    if cont == 1:
        menor = n
        maior = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    cont += 1
    soma += n
    n = int(input('Digite um valor: '))
    continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()
if continuar in 'Nn':
    media = soma / cont
    print('A média entre os valores fornecidos é de: {:.1f}'.format(media))
    print('O maior valor digitado foi: {}'.format(maior))
    print('O menor valor digitado foi: {}'.format(menor))
else:
    print('ERRO!REINICIE O PROGRAMA!')