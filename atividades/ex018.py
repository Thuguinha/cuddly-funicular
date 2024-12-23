import math 

cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))

hi = math.hypot(cateto_adjacente, cateto_oposto)

print(f'O comprimento da hipotenusa é: {hi:.2f}')