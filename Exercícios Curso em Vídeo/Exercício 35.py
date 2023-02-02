n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
niggas = ""
print(f'Tirando {n1} e {n2}, a média do aluno é {media}')

if media <= 5.0:
    niggas = 'REPROVADO'

elif media <= 6.9:
    niggas = 'RECUPERAÇÂO'

elif media > 7.0:
    niggas = 'APROVADO'

print(f'O aluno está {niggas}.')