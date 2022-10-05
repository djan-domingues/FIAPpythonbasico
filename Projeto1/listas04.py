notas = []

opcao = -1

while opcao != 4:
    print(" 1 - Informar notas \n 2 - Exibir notas \n 3 - media total \n 4 - Sair")
    opcao = int(input("Escolha sua opção: "))
    if(opcao == 1):
        notas.append(float(input("Digite a nota")))
    elif(opcao == 2):
        for i in notas:
            print(i)
    elif(opcao == 3):
        soma = sum(notas)
        qntd = len(notas)
        media = soma / qntd
        print(f"A media das notas é de: {media}")

        #forma mais direta de obter a visualização do calculo sem utilizar variavel
        print("A media das notas é de: " , (sum(notas) / len(notas)))

