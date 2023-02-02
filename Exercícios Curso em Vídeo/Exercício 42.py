s = 0
c = 0
for f in range(1, 501, 2):
    if f % 3 ==0:
        s = s + f
        c = c + 1
print(f'A soma de todos os {c} valores solicitados é {s}. ')