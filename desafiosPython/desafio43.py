peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"O IMC dessa pessoa é {imc:.2f}")
    print("Você está abaixo do peso!")
elif imc > 18.5 and imc < 25:
    print(f"O IMC dessa pessoa é {imc:.2f}")
    print("Peso Ideal!")
elif imc > 25 and imc < 30:
    print(f"O IMC dessa pessoa é {imc:.2f}")
    print("Você está com Sobrepeso!")
elif imc > 30 and imc < 40:
    print(f"O IMC dessa pessoa é {imc:.2f}")
    print("Você está com Obesidade!")
elif imc > 40:
    print(f"O IMC dessa pessoa é {imc:.2f}")
    print("Você está com Obesidade mórbida!")