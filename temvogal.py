palavras = ('banana', 'azul', 'avatar', 'aang', 'agua', 'terra', 'fogo', 'ar')
for p in palavras:
    print(f'\nNa palavra {p}, temos:', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
