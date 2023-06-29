nome = str(input("Digite o nome: ")).strip()

print(f"Seu nome em letras maiusculas fica: {nome.upper()}")
print(f"Seu nome em letras minusculas fica: {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.")
print(f"Seu primeiro nome tem {nome.find(' ')} letras")