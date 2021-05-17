a = float(input('Digite o comprimento de um lado de um traingulo: '))
b = float(input('Digite o comprimento de outro lado: '))
c = float(input('Digite mais um comprimento: '))
if a - b < c < a + b or a - c < b < a + c or b - c < a < b + c:
    print('Suas medidas formam um triangulo!')
else:
    print('Suas medidas NÃO formam um triangulo!')
