valor = float(input("Escreva um valor"))

porc = int(input("Escreva a porcentagem"))

perc = valor * porc / 100

acres = valor + perc

desc = valor - perc

print(f"O percentual de {porc} sobre {valor} é igual a {perc}, sendo assim o seu acrescimo seria {acres} e o desconto seria {desc}" )