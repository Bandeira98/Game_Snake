#peça 7 números ao usuario e exiba o maior deles
# entrada de dados
cont= 1 
maior = 0

while cont <=7:
    print("Informe o", cont,"númeor")
    num = int(input(""))
    if  num > maior:
        maior = num
    cont += 1
print("maior número é ",maior)
