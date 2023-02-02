s = int(input('Qual é o salário do funcinário? R$'))
if s < 1250:
    c = 15 * s / 100
else:
    c = 10 * s / 100
print(f'Quem ganhava R${s:.2f} passa a ganhar R${s+c:.2f} agora.')
