pr = float(input('Digite o preço do produto: R$'))
f = int(input('''OPÇÕES DE PAGAMENTO:
 [1]débito ou cartão
 [2]à vista no cartão
 [3]2x no cartão
 [4]3x ou mais no cartão
 Digite a forma de pagamento: '''))
if f == 1:
    p = pr - (pr * 10 / 100)
    print('TOTAL:R${:.2f}'.format(p))
elif f == 2:
    p = pr - (pr * 5 / 100)
    print('TOTAL:R${:.2f}'.format(p))
elif f == 3:
    p = pr
    print('TOTAL:R${:.2f}'.format(p))
elif f == 4:
    p = pr + (pr * 20 / 100)
    print('TOTAL:R${:.2f}'.format(p))
else:
    print('forma de pagamento não identificado')
