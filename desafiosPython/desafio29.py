vel = float(input("Qual a velocidade do carro ? "))
limite = 80
multaKm = 7

if vel > limite:
    velocidadeExcedida = vel - limite
    valorMulta = velocidadeExcedida * multaKm
    print("Você foi multado!")
    print(f"Velocidade excedida: {velocidadeExcedida}km/h")
    print(f"Valor da multa: R${valorMulta:.2f}")
else:
    print("Tenha um bom dia! Dirija com segurança!")