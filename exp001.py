a = int(input('Digite um comprimento: '))
b = int(input('Digite mais um comprimento: '))
c = int(input('Digite o ultimo comprimento: '))
if  b - c  < a < b + c or a - c  < b < a + c or a - b  < c < a + b:
    print('Seus comprimentos  formam um triangulo!')
else:
    print('Seus comprimentos não formam um triangulo!')
