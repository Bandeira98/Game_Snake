#Escreva um programa que peça ao usuário o ano de nascimento e o ano atual. Calcule e exiba a idade da pessoa.

#entrada de dados
ano_nascimento = int(input("Digite seu ano de nascimento:"))
ano_atual = int(input("Digite seu ano atual:"))

#processamento
idade = ano_atual - ano_nascimento

#saida de dados
print(f"Sua idade é: {idade} anos")