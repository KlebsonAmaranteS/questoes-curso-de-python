numInteiro = int(input("Digite um número inteiro: "))
baseConversao = input("Escolha qual vai ser a base de conversão:\n1- Binário\n2- Octal\n3 - Hexadecimal\n")


if baseConversao == "1":
    print(f"O valor inteiro {numInteiro} na base binária fica: {bin(numInteiro)}")
elif baseConversao == "2":
    print(f"O valor inteiro {numInteiro} na base octal fica: {oct(numInteiro)}")
elif baseConversao == "3":
    print(f"O valor inteiro {numInteiro} na base hexadecimal fica: {hex(numInteiro)}")
else:
    print("Opção Inválida!")