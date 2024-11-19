#Peça uma letra ao usuario e verifique se ela e consoante ou vogal
#entrada de dados
letra = input("Digite uma letra: ")

#processamento
if  letra in ("bcdfghjklmnpqrstvwxyz"):
    print("Essa letra é Consoante!")
else:
    print("Essa letra e Vogal!")