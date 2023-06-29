distanciaKm = float(input("Qual a distancia da viagem em km: "))

if distanciaKm <= 200:
    valorPsg = distanciaKm * 0.50
    print(f"O valor da sua passagem custa: R${valorPsg:.2f}")
elif distanciaKm > 200:
    valorPsgLonga = distanciaKm * 0.45
    print(f"O valor da sua passagem custa: R${valorPsgLonga:.2f}")