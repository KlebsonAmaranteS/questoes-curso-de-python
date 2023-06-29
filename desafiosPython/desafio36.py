valorCasa = float(input("Qual o valor da casa? "))
salarioComprador = float(input("Qual o seu salário? "))
anosPg = int(input("Em quantos anos deseja pagar? "))
porcentagemSal = salarioComprador * 0.30
converte = anosPg * 12
prestacao = valorCasa / converte

if prestacao > porcentagemSal:
    print(f"Por mês você vai pagar: R${prestacao:.2f} durante {anosPg} anos")
    print("Infelizmente, você não pode financiar essa casa, pois o valor da parcela excede 30% do seu salário")
    print(f"\033[0:30:41mO seu empréstimo foi negado!\033[m")
else:
    print(f"Por mês você vai pagar: R${prestacao:.2f} durante {anosPg} anos")
    print(f"\033[0:30:42mO seu empréstimo foi aprovado!\033[m")
