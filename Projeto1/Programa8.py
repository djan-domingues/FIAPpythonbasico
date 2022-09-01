valor = float(input("Digite um numero"))

if valor >= 500:
    perc = valor * 10/100
    valorFinal = valor - perc
else:
    valorFinal = valor

print(f"O valor final é: {valorFinal}" )