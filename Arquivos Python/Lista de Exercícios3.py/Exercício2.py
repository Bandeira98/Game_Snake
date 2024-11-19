#Escreva um programa que recaba um ano como entrda, e verifique se ele é bissexto.Um ano é Bissexto se divisível por 4, mas não por 100, exeto se ele tbm for divisível por 400

#entrada
ano = int(input("Me informe um ano: "))

#processamento
if ano % 400 == 0:
    print("Esse ano e Biseexto!")
elif (ano % 4 == 0) and (not ano % 100 == 0):
    print("Esse não é Bissexto!")
else:
    print("Esse ano não é Bissexto!")