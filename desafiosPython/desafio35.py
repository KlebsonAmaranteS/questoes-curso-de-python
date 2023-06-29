lados = []

for i in range(3):
    lados.append( int(input(f"Digite o valor do lado: ")))

if (lados[0] + lados[1] > lados[2]) and (lados[0] + lados[2] > lados[1]) and (lados[1] + lados[2] > lados[0]):
    print("As retas podem formar um triângulo")
else:
    print("As retas não podem formar um triângulo")


