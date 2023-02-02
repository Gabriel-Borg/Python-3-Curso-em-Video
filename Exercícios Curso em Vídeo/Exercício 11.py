preço = float(input('Qual é o preço do produto? R$'))
desconto = 5*preço/100
print(f'O produto que custava R${preço}, na promoção com desconto de 5% vai custar R${preço-desconto:.2f}')