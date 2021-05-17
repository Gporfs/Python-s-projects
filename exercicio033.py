maior = 0
menor = 0

for c in range(0, 5):
    p = float(input('Qual o seu peso? '))
    if c == 0:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

print('O maior peso é {}kg e o  menor peso é {}kg'.format(maior, menor))
