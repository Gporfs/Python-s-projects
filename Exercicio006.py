from random import randint
n = randint(0, 5)
n1 = int(input('Advinhe o numero: '))
if n == n1:
    print('OH MEU DEUS!!! VOCE ACERTOU!!! PARABENS!!!')
else:
    print('Hihi, você errou')
print('Eu pensei no numero {}'.format(n))