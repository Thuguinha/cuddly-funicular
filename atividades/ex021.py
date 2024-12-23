'''O mesmo professor do desafio anterior quer sortear
a ordem de apresentação de trabalhos dos alunos . 
faça um programa que  leia o nome dos quatros alunos 
e mostre em ordem  sorteada'''
# Biclioteca random 
import random
# Lista de alunos 
alunos = ['Arthur', 'Douglas', 'Ricardo', 'Nikão']
#embaralhar a lista
random.shuffle(alunos)
# Tirar os sinais
resultado = ', '.join(alunos)
# mostrar resultado da lista
print(f'A sequencia de alunos a apresentar é {resultado}')
