# Santo no Inicio do nome da cidade e Silva no nome da pessoa
n = str(input('Digite um nome de cidade: ')).strip()
n2 = str(input('Digite um nome de pessoa completo: ')).strip()
n = n.lower()
print('santo' == n[:5])
n = n.split()

print('santo' in n[0])
print('silva' in n2.lower())
