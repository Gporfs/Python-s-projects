def line():
    print('-=' * 30)


line()
print(f'{"Sistema de alunos":^60}')
line()
line()
print(f'{"Cadastro de funcionários":^60}')
line()
line()
print(f'{"ERRO DO SISTEMA":^60}')
line()


def mensagem(msg):
    line()
    print(f'{msg:^60}')
    line()


mensagem('SISTEMA DE ALUNOS')
mensagem('CADASTRO DE FUNCIONÁRIOS')
mensagem('ERRO DO SISTEMA')


def soma(a, b):
    s = a + b
    print(s)


line()
soma(4, 5)
soma(8, 9)
soma(2, 1)
line()


def contador(*num):
    print(num)


line()
contador(0, 1, 2, 3)
contador(7, 2)
line()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


line()
valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)
line()
