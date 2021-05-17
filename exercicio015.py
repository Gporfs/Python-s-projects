print('\033[7m=-='*20)
print('CONVERSOR DE BASES NUMÉRICAS')
print('=-='*20)
n = int(input('\033[mDigite um número inteiro aqui: '))
e = int(input('''[1] para binário
[2] para octal
[3] para hexadecimal
Escolha a conversão desejada: '''))
if e == 1 :
    print('Seu número em binário é: {}'.format(bin(n)[2:]))
elif e == 2 :
    print('Seu número em octal é: {}'.format(oct(n)[2:]))
elif e == 3 :
    print('Seu número em hexadecimal é: {}'.format(hex(n)[2:]))
else:
    print('Opção invalida!')