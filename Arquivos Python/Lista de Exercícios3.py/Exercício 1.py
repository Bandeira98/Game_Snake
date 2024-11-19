#Crie um programa que pergunte o preço de um produto e aplique 10% de desconto se preço for maior que 100$. Exiba o preço final com desconto aplicado, se for o caso.
#entrada de dados
preço = int(input("Digite o valor do produto: "))

#processamento
if preço >= 100:
    desconto = preço * 0.1
    preço_final = preço - desconto
    print("O seu desconto é: ",preço_final)