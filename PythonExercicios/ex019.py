import random
print('Sorteio')
aluno1 = input('1º Aluno: ')
aluno2 = input('2º Aluno: ')
aluno3 = input('3º Aluno: ')
aluno4 = input('4º ALuno: ')
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
print(random.choice(lista_alunos))