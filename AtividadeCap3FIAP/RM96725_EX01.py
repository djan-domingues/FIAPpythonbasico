faturamento = float(input("Digite o faturamento anual do canal: "))

print("Digite qual assinatura você deseja:")
print("Assinatura BASIC")
print("Assinatura SILVER")
print("Assinatura GOLD")
print("Assinatura PLATINUM")

assinatura = input()


if assinatura.upper() == "BASIC":
    bonus = faturamento * 0.3
    print(f"O valor do bônus a ser pago é de R$ {bonus}")
elif assinatura.upper() == "SILVER":
    bonus = faturamento * 0.2
    print(f"O valor do bônus a ser pago é de R$ {bonus}")
elif assinatura.upper() == "GOLD":
    bonus = faturamento * 0.1
    print(f"O valor do bônus a ser pago é de R$ {bonus}")
elif assinatura.upper() == "PLATINUM":
    bonus = faturamento * 0.05
    print(f"O valor do bônus a ser pago é de R$ {bonus}")
else:
    print("Opção inválida, escreva corretamente o nome da assinatura que deseja.")

