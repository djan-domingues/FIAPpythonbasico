#é necessário usar duas barras ao inves de uma só

arquivo = open("C:\\Users\\Felipe\\Desktop\\testePython.txt", encoding="UTF-8")

# metodo que le o arquivo como uma string unica
# print(arquivo.read())

#metodo que le o arquivo como uma lista, sendo cada linha do arquivo um item dela
for linha in arquivo.readlines():
    print(linha)

arquivo.close()
