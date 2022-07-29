real = float(input('Digite o valor para conversão: R$'))
dolar = float(input('Digite o valor do dólar hoje: U$'))
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, real / dolar))
