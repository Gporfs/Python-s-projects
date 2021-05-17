n = int(input('Digite um número: '))
r = int(input('Digite a razão da P.A.: '))
for c in range(0, 10):
    progresso = n + (c * r)
    print(progresso, end=' ')
