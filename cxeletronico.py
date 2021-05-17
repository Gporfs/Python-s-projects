print('='*30)
print('BANCO TAVIN')
print('='*30)
n = int(input('Digite o valor a ser sacado: R$'))
n50 = n // 50
r50 = n % 50
n20 = r50 // 20
r20 = r50 % 20
n10 = r20 // 10
r10 = r20 % 10
n1 = r10 // 1
print('Você irá receber:')
if n50 >= 2:
    print(f'{n50} notas de 50 reais.')
elif n50 == 1:
    print(f'{n50} nota de 50 reais.')
if n20 >= 2:
    print(f'{n20} notas de 20 reais.')
elif n20 == 1:
    print(f'{n20} nota de 20 reais.')
if n10 >= 2:
    print(f'{n10} notas de 10 reais.')
elif n10 == 1:
    print(f'{n10} nota de 10 reais.')
if n1 >= 2:
    print(f'{n1} notas de 1 real.')
elif n1 == 1:
    print(f'{n1} nota de 1 real.')