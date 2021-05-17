a = float(input('Digite um comprimento: '))
b = float(input('Digite mais um: '))
c = float(input('Digite o ultimo: '))
if a - b < c < a + b or a - c < b < a + c or b - c < a < b + c:
    if a == b == c:
        t = 'EQUILÁTERO'
    elif a == b or b == c or a == c:
        t = 'ISÓSCELES'
    else:
        t = 'ESCALENO'
    print('Esses comprimentos formam um triângulo {}!'.format(t))
else:
    print('Esses comprimentos NÃO forma um triângulo!')

