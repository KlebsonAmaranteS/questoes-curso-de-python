largura = float(input("Qual a largura da parede em metros: "))
altura = float(input("Qual a altura da parede em metros: "))

area = altura * largura

quantidade = area / 2

print(f"A área é {area}m²")
print(f"É necessário {quantidade:.1f}l para pintá-la")

