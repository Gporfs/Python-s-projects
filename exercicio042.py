cont = soma = 0
n = int(input('Digite um número[999]: '))
while not n == 999:
    soma += n
    cont += 1
    n = int(input('Digite um número[999]: '))
print('A soma de todos os números digitados é de {}'.format(soma))
print('Você digitou {} números'.format(cont))
