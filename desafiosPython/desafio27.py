nome = input("Digite seu nome completo: ")

palavras = nome.split()

primeiroNome = palavras[0]

ultimoNome = palavras[-1]

print(f"Seu nome completo é: {nome}")
print(f"Seu primeiro nome é: {primeiroNome}")
print(f"Seu ultimo nome é: {ultimoNome}")