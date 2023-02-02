n = str(input('Digite seu nome completo: ')).strip()
ns = n.split()
p = len(ns)
print(f'Muito prazer em te conheçer!'
      f'\nSeu primeiro nome é {ns[0]}'
      f'\nSeu último nome é {ns[p-1]}')