nc = str(input('Digite seu nome completo: '))
n = nc.split()
print(f'Analise seu nome...'
      f'\nSeu nome em maiúsculas é {nc.upper()}'
      f'\nSeu nome em minúsculas é {nc.lower()}'
      f'\nSeu nome tem ao todo {len(nc)-nc.count(" ")} letras'
      f'\nSeu primeiro nome é {n[0]} e ele tem {len(n[0])} letras')