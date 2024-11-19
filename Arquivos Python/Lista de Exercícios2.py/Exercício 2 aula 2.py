#Crie um programa que pergunte o preço de um produto e aplique 10% de desconto se preço for maior que 100$. Exiba o preço final com desconto aplicado, se for o caso.
#entrda de dados
idade = int(input("Por favor me infome sua idade:"))

#processamento
if(idade <= 12):
#saida de dados
    print("A sua idade corresponde a de uma criança!")

elif(idade>=12 and idade<=17):
#saida de dados
    print("A sua idade corresponde a de um adolecente!")

elif(idade>=18 and idade<=59):
#saida de dados
    print("A sua idade corresponde a de um adulto!")

elif(idade>=60 and idade<=100):
#saida de dados
    print("A sua idade corresponde a de um idoso!")