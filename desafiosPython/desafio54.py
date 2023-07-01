import datetime


anos = []
idades = []
maior_idade = []
menor_idade = []

for i in range(7):
    anos.append(int(input("Digite seu ano de nascimento: ")))
for j in range(7):
    idades.append(datetime.datetime.now().year - anos[j])

for k in range(7):
    if idades[k] >= 21:
        print(f"{idades[k]} anos, Maior de idade!")
        maior_idade.append(idades)
    else:
        print(f"{idades[k]} anos, Menor de idade!")
        menor_idade.append(idades)
        
print(f"São {len(maior_idade)} que tem maioridade!")
print(f"São {len(menor_idade)} que tem menoridade!")
