d = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))
d1 = 60
km2 = 0.15
t = d*d1
t2 = km*km2
t3 = t+t2
print(f'O total a pagar é de R${t3:.2f} ')

#Poderia fazer assim:
#d = int(input('Quantos dias alugados? '))
#km = int(input('Quantos KM rodados? '))
#d1 = d*60
#km2 = km*0.15
#print(f'O total a pagar é de R${d1+km2:.2f}')