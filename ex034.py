
salario= float(input('Qual o seu sálario?'))

s1= salario * 0.15
s2= salario * 0.10


reajuste1 = s1 + salario
reajuste2 = s2 + salario

if salario <= 1250:
    print('com o aumento de 15% o salario passa a ser: R${:.2f}'.format(reajuste1))
else:
   print('Seu Sálario ultrapassa os R$1.250 o valor com o reajuste fica R${:.2f}'.format(reajuste2))

