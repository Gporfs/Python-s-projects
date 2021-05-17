n = int(input('Digite um ano:'))
if (n % 400 == 0) and (n % 100 == 0):
    print('Esse ano é Bissexto')
else:
    print('Esse ano não é bissexto')
