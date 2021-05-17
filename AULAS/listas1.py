dados = list()
dados.append('Pedro')  # dados[0]
dados.append(25)  # dados[1]
pessoas = list()
pessoas.append(dados[:])  # pessoas = dados[:]
pessoas.append(['Maria', 19])
pessoas.append(['João', 32])
print(pessoas)
print(pessoas[0][0])
print(pessoas[1])