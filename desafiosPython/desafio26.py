frase = input("Digite uma frase: ")
letra = 'a'

frase = frase.lower()
posicao = frase.find(letra)
ultima = frase.rfind(letra)

quantidade = frase.count(letra)

if posicao != -1:
    print(f"A letra 'a' aparece pela ultima vez na posição {ultima}")
    print(f"A letra 'a' aparece pela primeira vez na posição {posicao}")
else:
    print("A letra 'a' não foi encontrada na frase.")


print(f"A letra 'a' aparece {quantidade} vezes na frase")