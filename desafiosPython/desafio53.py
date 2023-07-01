frase = input("Digite uma frase: ")

# Remove os espaços da frase
frase_sem_espacos = frase.replace(" ", "")

# Inverte a frase sem espaços
frase_invertida = frase_sem_espacos[::-1]

# Verifica se a frase original (sem espaços) é igual à frase invertida (sem espaços)
if frase_sem_espacos == frase_invertida:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
