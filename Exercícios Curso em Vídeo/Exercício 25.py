from time import sleep
import random

print('\033[0:32m-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
print('\033[0:34mVou pensar em um número entre 0 e 5. Tente advinhar...')
print('\033[0:32m-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
p = int(input('\033[0:37mEm que número eu pensei ? '))
print(f'Processando...')
sleep(3)
n = random.randint(1, 5)
if p == n:
    print('PARABÉNS ! Você conseguiu me vencer !')
else:
    print(f'\033[0:31mGANHEI ! Eu pensei no número {n} não no {p} !')
