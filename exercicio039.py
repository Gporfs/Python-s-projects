'''primeiro = int(input('Digite o termo inicial: '))
razão = int(input('Digite a razão da P.A.: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    contador +=1
print('fim')
'''
n = int(input('Digite um valor: '))
r = int(input('Digite a razão da progressão aritmética: '))
pa = n
while not pa == n + r * 10:
    print(pa,end='->')
    pa += r
print('Fim')

