from random import shuffle

nomes = []
for i in range(4):
    nomes_alunos = input("Digite o nome do aluno: ")
    nomes.append(nomes_alunos)

shuffle(nomes)
print("A ordem de apresentação será: ")
print(nomes)