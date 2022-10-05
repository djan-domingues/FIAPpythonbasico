import calc
opcao = -1

while opcao != 5 :
    print(" 1 - Soma \n 2 - Subtração \n 3 - Divisão \n 4 - multiplicação \n 5 - Sair")
    opcao = int(input("Escolha sua opção: "))

    valor1 = float(input("Digite um valor: "))
    valor2 = float(input("Digite um valor: "))

    if opcao == 1 :
        print(f"A soma dos numeros {valor1} e {valor2} é igual a: " , calc.somar(valor1, valor2))
    elif opcao == 2:
        print(f"A subtração dos numeros {valor1} e {valor2} é igual a: ", calc.subtrair(valor1, valor2))
    elif opcao == 3:
        print(f"A divisão dos numeros {valor1} e {valor2} é igual a: ", calc.dividir(valor1, valor2))
    elif opcao == 4:
        print(f"A multiplicação dos numeros {valor1} e {valor2} é igual a: ", calc.multiplicar(valor1, valor2))
