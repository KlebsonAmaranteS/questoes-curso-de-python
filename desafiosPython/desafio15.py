qtdDias = int(input("Quantos dias foi alugado: "))
kmPercorridos = float(input("Quanto Km rodados: "))


valor = (kmPercorridos * 0.15) + (qtdDias * 60)

print(f"O preço que você vai pagar é: R${valor:.2f}")