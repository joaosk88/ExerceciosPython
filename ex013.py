#reajuste salarial, calculo de porcentagem

salario =float(input('Digite seu salario:R$'))
reajuste = salario + (salario *15/100 ) # 15% de deconto
print ('Um funcionario que ganhava R${:.2F}, após o aumento salarial de 15% passa a receber R${:.2f}'.format(salario, reajuste))

