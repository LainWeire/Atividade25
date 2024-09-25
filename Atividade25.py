# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).

c = 0

for cn in range(5):
    n=int(input("Digite a nota de 5 alunos: "))

    if n>=7:
        c+=1

print(f"{c} passaram")