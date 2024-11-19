#Escreva um programa que peça ao usuário o peso (kg) e a altura (m), e calcule o Índice de Massa Corporal (IMC) usando a fórmula: IMC = peso / altura^2. Exiba o resultado.

#entrada de dados
kg = float(input("iforme seu Peso:"))
m = float(input("iforme seu Altura:"))

#processamento
imc = kg / (m*m)

#sainda de dados
print("imc->",format(imc, ' .2f') )