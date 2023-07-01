pares = []
impares = []

for i in range(0,6):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares.append(num)
        soma_pares = sum(pares)
    elif num % 2 == 1:
        impares.append(num)
print(f"Os números pares usados para a soma foram: {pares}. A soma dos valores pares é: {soma_pares}")
print(f"Os seguintes números: {impares} foram desconsiderados por serem impares")



        
        
    