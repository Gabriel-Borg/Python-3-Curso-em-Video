import random
a1 = input('Primeiro aluno: ')
a2 = input('Seugndo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
l = [a1, a2, a3, a4]
random.shuffle(l)
print(f'A ordem de apresentção será'
      f'\n{l}')