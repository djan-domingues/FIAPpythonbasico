#criando um dicionário vazio
dicionário = {}
#incluindo dados no dicionário
dicionário["André David"] = "Professor"
#alterando dados no dicionário
dicionário["André David"] = "Coordenador"
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))