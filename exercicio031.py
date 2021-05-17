frase = str(input('Digite uma frase: ')).strip().lower()
frase = frase.split()
frase = ''.join(frase)
frasei = frase[::-1]
if frase == frasei:
    print('PALINDROMO')
else:
    print('NÃO PALINDROMO')
