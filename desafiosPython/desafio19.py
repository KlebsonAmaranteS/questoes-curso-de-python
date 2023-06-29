import random

alunos = []

for i in range(4):
    nome_aluno = input("Digite o nome do aluno: ")
    alunos.append(nome_aluno)

aluno_escolhido = random.choice(alunos)

print(f"O aluno escolhido para apagar o quadro é: {aluno_escolhido}")






