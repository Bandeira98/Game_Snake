#peça para o usuario converte o o real em dolar
#entrada de dados
real = float(input("Digite o valor que deseja converter: "))
dolar = float(input("digite o valor do dolar: "))

#processamento
cambio = real / dolar

#saida de dados
print(real,"convertindo em USD é:",format(cambio, " .2f"))