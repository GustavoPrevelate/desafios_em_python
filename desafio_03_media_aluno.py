# Um professor precisa anotar a média de seus alunos em sua escola, porém são diversos alunos
# e o professor não tem tanto tempo para anotar tantas médias e dar uma nota final para cada aluno
# Crie um sistema em que pergunte para o professor qual foi a nota do aluno em cada um dos 4 bimestres e calcule a nota final.

b1 = float(input("Adicione a nota do 1º Bimestre: "))
b2 = float(input("Adicione a nota do 2º Bimestre: "))
b3 = float(input("Adicione a nota do 3º Bimestre: "))
b4 = float(input("Adicione a nota do 4º Bimestre: "))
media = (b1 + b2 + b3 + b4) / 4  
print(f"A média do aluno é: {media:.2f}") #:.2f está limitando em 2 casas decimais
if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")