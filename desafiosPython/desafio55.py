pesos = []

for i in range(5):
    pesos.append(float(input("Digite seu peso: ")))
    
print(f"O maior peso é {max(pesos)}kg")
print(f"O menor peso é {min(pesos)}kg")