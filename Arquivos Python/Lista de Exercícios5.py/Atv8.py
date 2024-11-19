#insira um numero e logo dps exibir a tabuada dele
#entrada de dados 
num = int(input("insira um número: "))
print ("A tabuada de :",num,)
#processamento
for i in range(0,11):
    print(f"{num} x {i} = {num * i}")