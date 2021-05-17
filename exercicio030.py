s = 0
n = int(input('Digite um número: '))
for c in range(2, n+1):
    d = n % c
    if d >= 1:
        r = 1
    else:
        r = 0
    s = s + r
if s == n-2:
    print('Este número é primo')
else:
    print('Este número não é primo')

