#forma de escrever para que não seja necessário o arquivo.close() e evitar o erro de esquecer

with open("C:\\Users\\Felipe\\Desktop\\testeEscritaJsonPython.txt", "r", encoding="UTF-8") as arquivo:
    print(arquivo.read())
