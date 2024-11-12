# Um menino de 10 anos de idade tinha uma calculadora de brinquedo, onde realizava operações matematicas básicas
# como a soma e a subtração, porém ela acabou se quebrando e agora o menino não consegue mais realizar seus calculos.
# Crie um sistema em que realize operações matematicas de soma e subtração para que o menino consiga realizar seus calculos.

n1 = int(input("Adicione um nº qualquer: "))
n2 = int(input("Adicione outro nº: "))
operacao = input("Você quer somar os números? Digite 1 para SIm e 2 para Não: ")
if operacao == "1":
    resultado = n1 + n2
elif operacao == "2":
    resultado = n1 - n2
else:
    print("Você escolheu uma opção que não foi identificada. Tente novamente!")
print(resultado)