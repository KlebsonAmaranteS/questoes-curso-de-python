import datetime

anoNascimento = int(input("Qual o seu ano de nascimento: "))
dataAtual = datetime.datetime.now().year
idade = dataAtual - anoNascimento


if idade == 18:
    print("Você tem a idade certa para se alistar ao serviço militar!")
elif idade < 18:
    alistamento = 18 - idade
    print("Você ainda vai se alistar ao serviço militar!")
    print(f"Falta exatamente {alistamento} anos para se alistar! ")
elif idade > 18:
    alistamento = idade - 18
    print("Você já passou do tempo do alistamento!")
    print(f"Passou exatamente {alistamento} anos do tempo certo para se alistar!")


