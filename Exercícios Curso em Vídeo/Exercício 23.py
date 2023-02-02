f = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A aparece {f.count("a")} vezes na frase.'
      f'\nA primeira letra A apareceu na posição {f.find("a")+1}'
      f'\nA última letra A apareceu na posição {f.rfind("a")+1}')