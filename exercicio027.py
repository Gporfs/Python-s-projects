n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    r = n * c
    print('{} x {} = {}'.format(n, c, r))