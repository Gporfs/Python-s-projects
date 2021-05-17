nome = str(input('Qual seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu nome tem {} letras'.format(len(nome)- nome.count(' ')))
nome = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nome[0])))
print('Seu nome tem {} letras'.format(len(''.join(nome))))
##############################
