from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - ano
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    aposentadoria = (35 - (date.today().year - pessoa['contratação'])) + pessoa['idade']
    pessoa['aposentadoria aos'] = aposentadoria
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k} = {v}')
