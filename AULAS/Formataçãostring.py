frase = "  Meu nome é Gustavo!  "
print('Nessa aula, vamos aprender operações com String no Python. \n'
      'As principais operações que vamos aprender são o Fatiamento de String, Análise com len(),\n'
      'count(), find(), transformações com replace(), upper(), lower(), capitalize(), title()'
      ', strip(), junção com join()''')
print('A frase tem {} caracteres \nO nome é {}'.format(len(frase), frase[13:21]))
print('A frase pulando de uma em uma letra é {}'.format(frase[0::2]))
print('O numero de letras "o"  minusculo nessa frase é de {} sem contar o nome'.format(frase.count('o', 0, 11)))
print('A palavra nome se inicia na posição {}'.format(frase.find('nome')))
print('True se existir a palavra "é" na frase e false se nao existir: {} '.format('é' in frase))
print('Ei! Meu nome não é Gustavo >:c {}'.format(frase.replace('Gustavo', 'Carlos')))
print('Eu vou gritar agora: {}'.format(frase.upper()))
print('Tô triste: {}'.format(frase.lower()))
print('Em uma frase normal ficaria assim :{}'.format(frase.capitalize()))
print('Se eu tivesse um livro o titulo seria:{}'.format(frase.title()))
print('Ei, eu nao preciso desses espaços no começo e no fim da frase:{}'.format(frase.strip()))
print('Ei, mas eu quero os espaços do inicio!:{}'.format(frase.rstrip()))
print('Não. Eu quis dizer os do final:{}'.format(frase.lstrip()))
frase = frase.split()
print('{}'.format(frase))
frase = ' '.join(frase)
print('{}'.format(frase))
