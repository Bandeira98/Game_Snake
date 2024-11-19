#Lista de Exercícios 3
#Crie um programa que leia o valor do raio de um círculo e calcule a sua área (use a fórmula: A = π * r^2). Considere π = 3.14159.

#Entrada de dados

#definir o valor de Pi
raio = float(input("Informe o valor do raio:"))

#processamento
area = 3.14159 * raio* raio

#saida de dados
print("Área -> ",format(area, ' .2f'))
