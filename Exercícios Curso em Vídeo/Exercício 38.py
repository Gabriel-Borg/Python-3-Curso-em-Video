print('=========== Loja Carai =========== ')
p = int(input('Preços das compras: R$'))
print('''FORMA DE PAGAMENTO
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))

if op == 1:
    print(f'Sua compra de R${p} vai custar R${p - (p * 10 / 100)} no final.')
elif op == 2:
    print(f'Sua compra de R${p} vai custa R${p - (p * 5 / 100 )} no final.')
elif op == 3:
    print(f'Sua compra de R${p} vão ser duas parcelas de R${p / 2:.2f} no final.')
elif op == 4:
    parc = int(input('Quantas parcelas? '))
    juros = p / parc * 20 / 100
    print(f'Sua compra será parcelada em {parc}x de R${ p / parc + juros :.2f} COMJUROS')
    print(f'Sua compra de R${p} vai custar {p + (p * 20 / 100)} no final.')
else:
    print('X')