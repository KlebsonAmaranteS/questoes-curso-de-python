notas = []

for i in range(2):
    notas.append(float(input(f"Digite a nota do aluno: ")))

media = (notas[0] + notas[1]) / 2

if media >= 7:
    print(f"Se o aluno tirou {notas[0]} e {notas[1]} ele obteve media {media:.2f} e ele está: \033[0:30:42mAPROVADO!\033[m")
elif media < 5:
    print(f"Se o aluno tirou {notas[0]} e {notas[1]} ele obteve media {media} e ele está: \033[0:30:41mREPROVADO\033[m")
elif media > 5 and media < 6.9:
    print(f"Se o aluno tirou {notas[0]} e {notas[1]} ele obteve media {media} e ele está: \033[0:30:44mRECUPERAÇÃO\033[m")
