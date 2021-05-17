a = float(input('Digite a sua altura(m): '))
p = float(input('Digite seu peso(kg): '))
imc = p / (a**2)
if imc < 18.5:
    print('CUIDADO!Você está ABAIXO DO PESO IDEAL!')
elif 18.5 <= imc <= 25:
    print('Você está NO PESO IDEAL!')
elif 25 < imc <= 30:
    print('Você está COM SOBREPESO!')
elif 30 < imc <= 40:
    print('CUIDADO! Você está OBESO!')
else:
    print('CUIDADO!Você está com OBESIDADE MÓRBIDA!')
print('Seu IMC é de {:.1f}'.format(imc))