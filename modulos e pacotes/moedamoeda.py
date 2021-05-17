import moedas
n = float(input('Preço: R$'))
print(f'O dobro de {moedas.moeda(n)} é {moedas.moeda(moedas.dobro(n))}')
print(f'A metade de {moedas.moeda(n)} é {moedas.moeda(moedas.metade(n))}')
print(f'Aumentando 10% em {moedas.moeda(n)}, temos {moedas.moeda(moedas.aumentar(n, 10))}')
print(f'Diminuindo 13% em {moedas.moeda(n)}, temos {moedas.moeda(moedas.diminuir(n, 13))}')
