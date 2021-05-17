import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print(f'\033[31mNão consegui acessar o site do PUDIM :(\033[m')
else:
    print('\033[32mUHUUUUL! Consegui acesso ao site PUDIM!!!\033[m')
# PyCharm não reconhece o tratamento.O programa está rodando liso .
