opcao = input("Digite S para sim ou N para não.")

while opcao != 's' and opcao != 'n' and opcao != 'S' and opcao != 'N':
    print(f"Voce digitou {opcao}. Digite 'S' ou 'N'")
    opcao = input("Digite S para sim ou N para não.")

print(f"Voce digitou {opcao}")