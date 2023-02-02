print ('-=-' * 20)
print ('Analisador de Triângulos')
print ('-=-' * 20)

sg1 = float(input('Primeiro segmento: '))
sg2 = float(input('Segundo segmento: '))
sg3 = float(input('Terceiro segmento: '))

if sg1 + sg3 > sg2 and sg1 + sg2 > sg3 and sg2 + sg3 > sg1 :
    sg = 'PODEM FORMAR'
else:
    sg = 'NÃO PODEM FORMAR'
print(f'Os segmentos acima {sg} triângulo. ')