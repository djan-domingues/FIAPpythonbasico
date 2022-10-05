finalImpar = float(0.0)
finalPar = float(0.0)

for impares in range(1,50,2):
    print("Você esta digitando as notas dos alunos ìmpares")
    notaImpar = float(input(f"Porfavor, insira a nota do aluno {impares}"))
    finalImpar += notaImpar

for pares in range(2, 51, 2):
    print("Você esta digitando as notas dos alunos pares")
    notaPar = float(input(f"Porfavor, insira a nota do aluno {pares}"))
    finalPar += notaPar

finalPar = finalPar/ 25
finalImpar = finalImpar/25

if finalImpar > finalPar:
    print(f"Os alunos ímpares tiveram a maior média: {finalImpar}")
elif finalPar > finalImpar:
    print(f"Os alunos pares tiveram a maior média: {finalPar}")
elif finalPar == finalImpar:
    print(f"Os alunos ímpares tiveram a mesma nota dos alunos pares, media = {finalImpar}")


