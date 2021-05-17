n = float(input('Quantos kilometros tem a sua viagem? '))
if n<=200:
    print('A sua viagem fica {:.2f} reais'.format(n*0.5))
else:
    print('Sua viagem vai ficar {} reais'.format(n*0.45))