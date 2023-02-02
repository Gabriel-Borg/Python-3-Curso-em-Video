d = float(input('Qual é a distância da sua viagem?'))
km1 = d * 0.50
km2 = d * 0.45
print(f'Você está preste a começar uma viagem de {d}Km.')
if d < 200:
    print(f'E o preço da sua passagem será de R${km1:.2f}')
else:
    print(f'E o preço da sua passagem será de R${km2:.2f}')

### d = float(input('Qual é a distância da sua viagem?'))
##print(f'Você está preste a começar uma viagem de {d}Km.')
###if d < 200:
####### km = d * 0.50
###else:
####### km = d * 0.45
##print(f'E o preço da sua passagem será de R${km:.2f}')