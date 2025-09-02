# Aluguel de carros
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

kmDia = km / dias
Diaria = dias * 60
kmRodado = km * 0.15
resultado = kmRodado + Diaria
print('Total de {} dias, total de {}km rodado, por dia {}km valor a ser pago R${:.2f}'.format(dias, km, kmDia, resultado))