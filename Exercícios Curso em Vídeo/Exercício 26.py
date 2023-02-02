vl = int(input('Qual é a velocidade do carro ? '))
vt = vl - 80
mu = vt * 7
if vl > 80:
    print(f'\033[0:31mMULTADO! Você excedeu o limite permitido que é de 80km/h'
          f'\nVocê deve pagar uma multa de R${mu:.2f}!')
    print('\033[0:36mTenha um bom dia! Dirija com segurança!')
else:
    print('\033[0:36mTenha um bom dia! Dirija com segurança!')