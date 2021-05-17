n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite mais um numero: '))
lista = sorted([n1, n2, n3])
print('O numero {:.1f} é o maior'.format(lista[2]))
print('O menor numero é o {:.1f}'.format(lista[0]))
#ou
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior numero é o {}'.format(maior))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor número é {}'.format(menor))
