salFunc = float(input("Digite o valor do seu salário: R$"))

if salFunc > 1.250:
    aumentoSal = (salFunc * 0.10) + salFunc
    print(f"O seu salário com aumento ficou: R${aumentoSal:.2f}")
elif salFunc <= 1.250:
    aumentoSal = (salFunc * 0.15) + salFunc
    print(f"O seu salário com aumento ficou: R${aumentoSal:.2f}")