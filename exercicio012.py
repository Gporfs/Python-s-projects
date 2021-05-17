n = float(input('Qual o salário a receber aumento? '))
if n<=1250:
    print('Seu novo salário é de {} reais'.format(n+n*(15/100)))
else:
    print('Seu novo salário é de {} reais'.format(n+n*(10/100)))