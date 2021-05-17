n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('Sua média é {}, portanto você está reprovado'.format(m))
elif 5 <= m <= 6.9:
    print('Sua média é {}, portanto você está de recuperação'.format(m))
elif m >= 7:
    print('Sua média é {}, PARABÉNS!Você está aprovado!'.format(m))