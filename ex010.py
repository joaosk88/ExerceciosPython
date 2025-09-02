# leia um valor e converta ele para a moeda escolhida

a = float(input('Digitar salario e converta para dolares: '))
dolar = a / 5.40
print('com R${:.2f} você pode comprar U${:.2f}'.format(a, dolar))




b = float(input('Digitar salario e converta em pesos chilenos: '))
pesos = b / 0.057
print('R${} convertido o valor é {:.2f}'.format(b, pesos))
