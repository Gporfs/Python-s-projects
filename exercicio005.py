n = str(input('Digite seu nome completo: ')). strip().split()
print('Primeiro nome: {}'.format(n[0]))
x = len(n)
print('Ultimo nome: {}'.format(n[x-1]))