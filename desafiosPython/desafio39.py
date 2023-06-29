import datetime

anoNascimento = int(input("Qual o seu ano de nascimento: "))
dataAtual = datetime.datetime.now().year
idade = dataAtual - anoNascimento


if idade == 18:
    print("Você tem a idade certa para se alistar ao serviço militar!")
    print(f"Seu alistamento é nesse ano de {dataAtual}")
elif idade < 18:
    alistamento = anoNascimento + 18
    print("Você ainda vai se alistar ao serviço militar!")
    print(f"Seu alistamento será em {alistamento}")
elif idade > 18:
    alistamento = 18 + anoNascimento
    print("Você já passou do tempo de se alistar!")
    print(f"Seu alistamento foi em {alistamento}")


