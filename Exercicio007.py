v = float(input('A velocidade do carro: '))
if v > 80:
    print('A multa a ser paga por esse carro é de {:.2f} reais'.format(7 * (v - 80)))
