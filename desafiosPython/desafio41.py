import datetime

anoNasc = int(input("Digite seu ano de nascimento: "))
anoAtual = datetime.datetime.now().year
idade = anoAtual - anoNasc

if idade <= 9:
    print("Sua categoria é MIRIM!")
elif idade <= 14:
    print("Sua categoria é INFANTIL!")
elif idade <= 19:
    print("Sua categoria é JUNIOR!")
elif idade <= 20:
    print("Sua categoria é SÊNIOR!")
elif idade > 20:
    print("Sua categoria é MASTER!")
