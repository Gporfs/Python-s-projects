def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaraquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')


def lerarquivo(nome):


    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:

        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq,nome='<desconhecido>',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever os dados!')
        else:
            print(f'Registro de {nome} concluído com sucesso!')
            a.close()
