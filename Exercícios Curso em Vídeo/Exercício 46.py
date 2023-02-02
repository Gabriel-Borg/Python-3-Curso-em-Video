n = int(input('Digite um número: '))
cont = 0
primo = ''
for f in range(1, n+1):
    if n % f == 0:
        print('\033[33m', end=' ')
        cont = cont + 1
    else:
        print('\033[31m', end=" ")
    print(f, end=" ")
if cont == 2:
    primo = 'É PRIMO'
else:
    primo = 'NÂO È PRIMO'

print(f'\033[m\nO número {n} foi divisível {cont} vezes')
print(f'E por isso ele {primo}')
