print('--------------------CAIXA------------------------')
print('==-'*20)
soma = cont = caros = barato = pbarato = 0
while True:
    print('=-='*20)
    nome = str(input('Qual nome do produto? '))
    preco = float(input('Qual o preço do produto? '))
    continuar = str(input('Deseja continuar[S/N]? '))
    while continuar not in 'SNns':
        print('Opção inválida!')
        continuar = str(input('Deseja continuar[S/N]? '))
    soma += preco
    if cont == 0 or pbarato > preco:
        pbarato = preco
        barato = nome
    if preco > 1000:
        caros += 1
    cont += 1
    if continuar in 'Nn':
        break
print(f'TOTAL:{soma},\n{caros}  PRODUTOS CUSTAM MAIS DE R$1000,\n{barato.upper()} FOI O PRODUTO MAIS BARATO')
