#menu de 4 opções 
#entrada de dados
print ("Escolha uma das 4 opções: ")
print ("1 , soma")
print ("2 , subtração")
print ("1 , mutiplicação")
print ("1 , Divisão")

opção = float(input("Escolha uma das opções  1 a 4:"))

if opção >= 1 and opção <= 4:
    num1 = float(input("primeiro número:"))
    num2 = float(input("segundo número:"))
#processamento
if opção == 1:
    resultado = num1 + num2
    print("resultado: ",resultado)
if opção == 2:
    resultado = num1 - num2
    print("Resultado: ",resultado)
if opção == 3:
    resultado = num1 * num2
    print("Resultado : ",resultado)
if opção == 4:
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado: ",format(resultado, ".4f"))
    else:
        print("essa opção não é divisivel")
else:
    print("nemhuma opção selecionada")