preco_produto = float(input("Qual o preço do produto: "))
forma_pagamento = input("Formas de pagamentos:\n1- Á vista(Cheque ou dinheiro)\n2- Cartão\n")

if forma_pagamento == '1':
    desconto = (preco_produto * 0.10) - preco_produto
    print(f"Você ganhou 10% de desconto e vai pagar: {desconto}")
elif forma_pagamento == '2':
