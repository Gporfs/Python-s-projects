print('\33[35;40m=-='*20)
print('COMPARADOR DE DOIS NÚMEROS')
print('=-='*20)
n1 = int(input('\033[mDigite um numero: '))
n2 = int(input('Digite mais um valor: '))
if n1 > n2 :
    print('{} é maior que {}'.format(n1,n2))
elif n2 > n1 :
    print('{} é maior que {}'.format(n2,n1))
elif n1 == n2:
    print ('Os números são iguais!')