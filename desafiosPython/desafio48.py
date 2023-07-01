soma = 0

for num in range(1, 501):
    if num % 2 != 0 and num % 3 == 0:
        soma += num

print(f"A soma dos números ímpares múltiplos de três no intervalo de 1 a 500 é: {soma}")
