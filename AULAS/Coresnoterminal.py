print('Para formatação de texto pode-se usar os códigos 0, {}1{}, {}4{},{}7{}'
      .format('\033[1m', '\033[m', '\033[4m', '\033[m', '\033[7m', '\033[m'))
print('Para cores das letras e de fundo pode se usar os código {}0{}, {}1{}, {}2{}, {}3{}, {}4{}, {}5{}, {}6{}, {}7{}'
      .format('\033[30m', '\033[m', '\033[31m', '\033[m', '\033[32m', '\033[m', '\033[33m', '\033[m', '\033[34m',
              '\033[m', '\033[35m', '\033[m', '\033[36m', '\033[m', '\033[37m', '\033[m'))
print('\033[30;41mTeste\033[m')
print('\033[4;1;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[42;30mTeste\033[m')
print('\33[mTeste\033[m')
print('\33[1;7mTeste\033[m')
