'''n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
contador = 3
while contador <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print('-> Fim')
'''
n = int(input('Digite o número de termos: '))
f = 0
f1 = 1
contador = 1
while contador <= n:
    print('-> {} -> {} '.format(f, f1), end='')
    contador += 2
    f += f1
    f1 += f
print('Fim')