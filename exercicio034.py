idades = 0
velho = ''
novas = 0
for c in range(1,5):
    print('==========={}°PESSOA============='.format(c))
    nome = str(input('Qual o seu nome? ')).strip()
    idade = int(input('Quantos anos você tem? '))
    genero = int(input('''[1]homem
[2]mulher
Digite o número correspondente ao seu gênero: '''))
    idades += idade
    if c == 0:
        velho = idade
    if genero == 1 and idade > velho:
        velho = nome
    if genero == 2 and idade < 18:
        novas +=1
idades = idades / 4
print ('A média do grupo é de {:.1f} anos, o homem mais velho é {}\n e tem {} mulheres menores de 18 anos'.format(idades,
    velho, novas))


