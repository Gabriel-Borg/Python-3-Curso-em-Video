print('''=====================================
       10 TERMOS DE UMA PA          
=====================================''')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for f in range(0, 10):
    conta = razao * f
    print(conta, end=' -> ')
print('ACABOU')
