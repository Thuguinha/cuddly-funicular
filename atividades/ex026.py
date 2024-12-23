'''Faça um programa que leia uma frase pelo
teclado e mostre:
> Quantas vezes aparece a letra A
> Em que posição ela parece pela primeira vez
> Em que posição ela parece pela ultima vez'''
# Quantas vezes aparece a letra 'a'
frase = str(input('Digite uma frase: '))
cout = frase.count('a')
print(f'A frase {frase} tem {cout} ''a''. ')
# Em que posição ela parece pela primeira vez
fin = frase.find('a')
print('A posição da primeira letra ''a'' aparece na posição {} '.format(fin))
# Em que posição ela parece pela ultima vez
ultima = frase.rfind('a')
print('A ultima letra ''a'' foi encontrada na posição {} '.format(ultima))