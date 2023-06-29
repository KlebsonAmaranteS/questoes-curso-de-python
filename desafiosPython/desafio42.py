lados = []

for i in range(3):
    lados.append( int(input(f"Digite o valor do lado: ")))

if lados[0] == lados[1] and lados[0] == lados[2] and lados[1] == lados[2]:
    print("As retas formam um triângulo EQUILÁTERO")
elif lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]:
    print("As retas formam um triângulo ISÓSCELES")
elif lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
    print("As retas formam um triângulo ESCALENO")


