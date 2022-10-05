segunda = int(input("Digite a quantidade de votos para que as lives sejam de segunda-feira: "))
diaComMaisVotos = segunda
votosTotais = segunda
diaDefinido = str("Segunda-feira")

terca = int(input("Digite a quantidade de votos para que as lives sejam de terça-feira: "))
votosTotais += terca
if terca > diaComMaisVotos:
    diaComMaisVotos = terca
    diaDefinido = "Terça-feira"

quarta = int(input("Digite a quantidade de votos para que as lives sejam de quarta-feira: "))
votosTotais += quarta
if quarta > diaComMaisVotos:
    diaComMaisVotos = quarta
    diaDefinido = "Quarta-feira"

quinta = int(input("Digite a quantidade de votos para que as lives sejam de quinta-feira: "))
votosTotais += quinta
if quinta > diaComMaisVotos:
    diaComMaisVotos = quinta
    diaDefinido = "Quinta-feira"

sexta = int(input("Digite a quantidade de votos para que as lives sejam de sexta-feira: "))
votosTotais += sexta
if sexta > diaComMaisVotos:
    diaComMaisVotos = sexta
    diaDefinido = "Sexta-feira"

print(f"O dia escolhido foi {diaDefinido} com {diaComMaisVotos} votos a favor, do total de {votosTotais} votos totais")



