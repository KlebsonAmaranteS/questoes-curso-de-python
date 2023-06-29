num = []

for i in range(2):
    num.append(int(input("Digite um número inteiro: ")))
if num[0] > num[1]:
    print("O primeiro valor é maior!")
elif num[1] > num[0]:
    print("O segundo valor é maior!")
else:
    print("Não existe valor maior, os dois são iguais")