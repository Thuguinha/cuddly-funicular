'''Crie um programa que leia o nome completo
da pessoa e mostre:

1 - O nome com todas as letras maiusculas
2 - O nome com todas minusculas
3 - Quantas letras ao todo (sem considerar espaços)
4 - Quantas letras tem no primeiro nome.'''
# digitar o nome
nome = str(input('Digite o seu nome completo: '))
# letras maiusculas (upper)
print('O nome em letras maiusculas:', nome.upper())
# Letras minusculas (lower)
print('O nome em letras minusculas:', nome.lower())
# Quantas letras ao todo (sem considerar espaços)
nome2 = nome.replace(' ', '')
nome3 = len(nome2)
print(f'O nome {nome} tem exatamente {nome3} letras')
# Quantas letras tem no primeiro nome
n = nome[:6]
print('O primeiro nome {} tem {} letras'.format(n, len(n)))


