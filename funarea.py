def area(larg, comp):
    a = l * c
    print('-'*20)
    print(f'A area de um terreno {larg} x {comp} é de {a}m².')


print('Controle de terrenos')
print('-' * 40)
l = float(input('Largura(m): '))
c = float(input('Comprimento (m): '))
area(l, c)
