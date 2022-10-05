#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

#incluindo um valor digitado pelo usuário no final da lista
jedi.append(input("Digite o nome de um Jedi"))

for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

#incluindo um valor digitado pelo usuário em uma posição específica da lista
jedi.insert(2, input("Digite o nome de um Jedi"))

for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

print("Excluindo o ultimo valor da lista")

#removendo o ultimo valor inserido na lista
jedi.pop()

for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

print("excluindo o valor na posição 2")

#removendo um valor em uma posição especifica
jedi.pop(2)

for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

print("removendo um o valor Yoda da lista")

#removendo um valor especifico da lista
jedi.remove("Yoda")

for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)


