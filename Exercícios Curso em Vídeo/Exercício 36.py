n = int(input('Ano de Nascimento: '))
idade = 2021 - n
niggas = ""
print(f'O atleta tem {idade} anos.')

if idade < 9:
    niggas = 'MIRIM'

elif idade < 14:
    niggas = 'INFANTIL'

elif idade < 19:
    niggas = 'JÚNIOR'

elif idade < 25:
    niggas = 'SÉNIOR'

elif idade > 25:
    niggas = 'MASTER'

print(f'Classificação: {niggas}')
