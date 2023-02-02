import random
pa = input('Primeiro aluno:')
sa = input('Segundo aluno:')
ta = input('Terceiro aluno:')
qa = input('Quarto aluno:')
l = [pa, sa, ta, qa]
ae = random.choice(l)
print(f'O aluno escolhido foi {ae}')