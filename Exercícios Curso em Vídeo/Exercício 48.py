from datetime import date

cont_maior = cont_menor = 0

for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    ano_att = date.today().year
    idade = ano_att - nasc
    if idade >= 18:
        cont_maior = cont_maior + 1
    else:
        cont_menor = cont_menor + 1
print('                                                     ')
print(f'Ao todo tivemos {cont_maior} pessoas maior de idade'
      f'\nE também tivemos {cont_menor} pessoas menores de idade')
