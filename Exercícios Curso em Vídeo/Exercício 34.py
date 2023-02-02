#Desafio Guanabára
n = int(input('Ano de nacimento: '))
idade = 2021 - n
menor = 18 - idade
maior = idade - 18
print(f'Quem nasceu em {n} tem {idade} anos em 2021')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE PORRA!')
elif idade < 18:
    print(f'Ainda faltam {menor} anos para o alistamento')
    print(f'Seu alistamento será em {2021 + menor} anos.')
else:
    print(f'Você já deveria ter se alistado há {maior} anos.')
    print(f'Seu alistamento foi {2021 - maior}.')

#Desafio Felipe
n = str(input('Data de nacimento: '))
bosta = n.split('/')
dia = int(bosta[0])
mes = int(bosta[1])
ano = int(bosta[2])
idade = 2021 - ano
