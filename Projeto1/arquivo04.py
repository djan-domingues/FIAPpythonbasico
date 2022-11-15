import json
arquivo = open("C:\\Users\\Felipe\\Desktop\\testeEscritaJsonPython.txt", "r", encoding="UTF-8")

conteudo = arquivo.read()

arquivo.close()

#essa função faz uma interpretação dos simbolos que estão nesse texto e gera como resultado a extrutura do python mais compativel
agenda = json.loads(conteudo)

print(agenda)