nome=input('qual o seu nome? ')
print('A direita:')
print('Prazer em te conhecer {:>20}!'.format(nome))
print('a esquerda:')
print('Prazer em te conhecer {:<20}!'.format(nome))
print('centralizado:')
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Pode-se escolher os caracteres que vão completar o numero de caracteres solicitado:')
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('FORMATAÇÃO DE NUMEROS:')
n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
e=n1/n2
print('A divisão entre esse numeros é {:.2f}'.format(e))
print('Formatar um texto:')
print('Vou usar o mesmo código que usei nos nomes mas agora tudo ficará na mesma linha com o codigo end=""\n pode-se adicionar qualquer coisa entre as aspas do end.')
print('Prazer em te conhecer {:>20}!'.format(nome),end=' ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('Ou quebrar a linha dentro do comando print assim:\n Dessa forma pode-se deixar o código mais organizado')