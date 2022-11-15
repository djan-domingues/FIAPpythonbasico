import json
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"645987",
         "Email":"bat@caverna.com"}
}

#print(json.dumps(contatos, indent = 4))

arquivo = open("C:\\Users\\Felipe\\Desktop\\testeEscritaJsonPython.txt", "w", encoding="UTF-8")

conteudo = json.dumps(contatos, indent = 4)

arquivo.write(conteudo)

arquivo.close()