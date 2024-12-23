'''Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. faça um programa que ajude ele 
lendo o nome deles e escrevendo o nome do escolhido'''
#Biblioteca random
from random import choice
# nome dos alunos
p = str(input('Digite o primeiro aluno: '))
p2 = str(input('Digite o segundo aluno: '))
p3 = str(input('Digite o terceiro aluno: '))
p4 = str(input('Digite o quarto aluno: '))
# Numero correspondende ao nome
numeros = 1, 2, 3, 4
alunos = {1: p, 2: p2, 3: p3, 4: p4}
#Embaralhar os nomes e numeros
sorteio = choice(numeros)
# Resultado final do sorteio 
print(f'O numero sorteado é: {sorteio}')
print(f'O aluno sorteado é: {alunos[sorteio]}')

