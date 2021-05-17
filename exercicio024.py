from emoji import emojize
from time import sleep
print('Ei! Os fogos vão começar!!!')
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize('\033[31m:party_popper:'))
sleep(1)
print(emojize(':fireworks:'))
sleep(1)
