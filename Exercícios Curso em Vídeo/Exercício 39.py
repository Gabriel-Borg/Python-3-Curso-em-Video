import random
print('=========== JOKENPÔ ===========')
print('''      [ 1 ] Pedra
      [ 2 ] Papel
      [ 3 ] Tesoura ''')
escolha = int(input('Qual você escolhe ? '))
pedra = 1
papel = 2
tesoura = 3

lista = [pedra, papel, tesoura]
bot = random.choice(lista)

print(f'Você jogou {escolha} e eu {bot}')

if escolha == bot:
    print('Deu empate seu gay ')
elif escolha == 1 and bot == 2:
    print('Eu venci seu merda mixuruca!')
elif escolha == 1 and bot == 3:
    print('Se me deu um pau filho da puta')
elif escolha == 2 and bot == 1:
    print('Se me deu um pau filho da puta')
elif escolha == 2 and bot == 3:
    print('Eu venci seu merda mixuruca!')
elif escolha == 3 and bot == 1:
    print('Eu venci seu merda mixuruca!')
elif escolha == 3 and bot == 2:
    print('Se me deu um pau filho da puta')
else:
    print('Pirou o coco fdp ?')