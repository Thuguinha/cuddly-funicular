'''Faça um programa que  leia um numero
de 0 - 9999 e mostre  na tela cada um
dos digitos  separados'''
# Digitar um valor 
n1 = int(input('Digite um valor de 0 a 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
# Respotas de acordo com o valor
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Cetena: {c}')
print(f'Milhar: {m}')
