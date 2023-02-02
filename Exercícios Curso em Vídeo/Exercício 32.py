valor = int(input('Valor da casa: R$'))
salário = int(input('Salário do comprar: R$'))
finaciamento = int(input('Quantos anos de finaciamento? '))
prestação = valor / (finaciamento * 12)
porcetagem = 30 * salário / 100
print(f'Para pegar uma casa de R${valor:.2f} em {finaciamento} a prestação será de R${prestação:.2f}')
if prestação < porcetagem:
    print('Empréstimo pode ser CONCEDIDO !')
else:
    print('Empréstimo NEGADO !')

