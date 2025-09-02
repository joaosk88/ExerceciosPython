valorCasa = float(input('Valor da casa: '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos deseja pagar a casa: '))

# cálculo da prestação mensal
prestacao = valorCasa / (anos * 12)

# 30% do salário
limite = salario * 0.30

print(f"\nValor da prestação: R${prestacao:.2f}")
print(f"30% do salário: R${limite:.2f}")

# Verificação
if prestacao <= limite:
    print(f"\n✅ Financiamento aprovado! A casa de R${valorCasa:.2f} será paga em {anos} anos com parcelas de R${prestacao:.2f}.")
else:
    print(f"\n❌ Financiamento negado! A prestação de R${prestacao:.2f} excede 30% do salário.")
