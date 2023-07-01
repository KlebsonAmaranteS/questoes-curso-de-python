nome = []
idade = []
sexo = []

for i in range(4):
    nome.append(str(input('Nome: ')).upper())
    idade.append(int(input('Idade: ')))
    sexo.append(str(input('Sexo [M/F]: ')).upper())

media = sum(idade) / len(idade)

print(f"A média de idade do grupo é: {media} anos")

homem_mais_velho = None
for j in range(4):
    if sexo[j] == "M":
        if homem_mais_velho is None or idade[j] > idade[homem_mais_velho]:
            homem_mais_velho = j

if homem_mais_velho is not None:
    print(f"O homem mais velho é: {nome[homem_mais_velho]}, que tem {idade[homem_mais_velho]} anos")

mulheres_menos_de_20 = 0
for k in range(4):
    if sexo[k] == "F" and idade[k] < 20:
        mulheres_menos_de_20 += 1

print(f"Existem {mulheres_menos_de_20} mulheres com menos de 20 anos.")
