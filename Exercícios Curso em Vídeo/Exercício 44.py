soma = 0
for f in range(1, 7):
    n = int(input(f'Digite {f}º números: '))
    if n % 2 == 0:
        soma = soma + f
print(f'A soma dos números pares é {soma}.')
