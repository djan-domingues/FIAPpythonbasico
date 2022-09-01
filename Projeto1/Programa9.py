salario = float(input("Digite seu salario"))
tempoCasa = int(input("Digite o tempo de casa"))

if tempoCasa >= 5:
    perc = salario * 10/100
    salario = salario + perc

else:
    if tempoCasa < 5 and tempoCasa >= 3:
        perc = salario * 3 / 100
        salario = salario + perc

print(f"O salario é de: {salario}")


