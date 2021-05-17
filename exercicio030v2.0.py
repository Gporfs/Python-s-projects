cont = 0
n = int(input('Digite um número inteiro: '))
for c in range(1, n+1):
    d = n % c
    if d == 0:
        cont +=1
        print('\033[33m', end=' ')
    elif d != 0:
        print('\033[31m',end=' ')
    print('{}'.format(c), end=' ')
if cont == 2:
    r = 'PRIMO!'
else:
    r = 'NÃO-PRIMO'
print('\n\033[mEste número é {}'.format(r))