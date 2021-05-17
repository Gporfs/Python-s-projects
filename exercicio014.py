print('\33[31m-=-'*20)
print('Calculadora de Impréstimos')
print('-=-'*20)
vc = float(input('\33[mDigite o preço da casa: R$ '))
s1 = float(input('Qual sua renda mensal? R$ '))
t = float(input('Em quantos anos serão parcelados? '))
p = vc/(t*12)
if p > (s1*30/100):
    print('Infelizmente não podemos financiar este imovel')
else:
    print('Parabéns você consegue financiar este imóvel!')
    print('Suas prestações serão de R${:.2f}'.format(p))
