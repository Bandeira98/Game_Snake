#Calcule a porcentagem da gorjeta, entre (10, 20, 30)%. e mostre o valor da conta e da porcentagem 
#entrada de dados
valor_da_conta = float(input("Qual foi o valor da conta: R$"))
porcentagem = int(input("Digite a porcentagem da gorjeta, se é 10%, 10% ou 30%: "))

#processamento
gorjeta = valor_da_conta * porcentagem /100
valor_total = gorjeta - valor_da_conta

#saida de dados
print("o valor da gorjeta é: ", gorjeta, "R$")
print("o valor total é: ",valor_total, "R$")