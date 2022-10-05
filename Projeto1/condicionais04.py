valorCompra = float(input("Digite o valor da compra"))

formaPagamento = int(input("Digite 1 - Dinheiro ou 2 - Cartão"))

if valorCompra >= 100 and formaPagamento == 1:
    valorDesconto = valorCompra * 10/100
    valorCompra -= valorDesconto
    print(f"Você recebeu um desconto e o valor final é de {valorCompra}")

else:
    print(f"Você não recebeu desconto e o valor final é de {valorCompra}")