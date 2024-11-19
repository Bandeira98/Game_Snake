# insira as notas do usuario e verifique se aprovado, reprovado ou em recuperação
#entrada de dados
print("digite suas duas notas!: ")
nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunta nota: "))

#processamento
if nota1 and nota2>= 6:
    print("Com essa nota voce está APROVADO!")
elif nota1 >= 4  and nota1 <= 5.9:
    print("Com essa nota voce está de RECUPERAÇÃO!")
else:
    print("Com essa nota voce está REPROVADO!")
