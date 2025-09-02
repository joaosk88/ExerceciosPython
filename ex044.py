"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""
print('{:=^40}'.format(' LOJA DO JOÃO  '))

preço = float(input('Preço das compras: R$'))
print ('''FORMAS DE PAGAMENTO: 
[1] À vista dinheiro/cheque
[2] À vista cartão  
[3] 2x no cartão 
[4] 3x ou mais no cartão''')

pagamento = int(input('Digite uma opção para pagamento: '))

pagamento01 = preço * 0.10
op1 = preço - pagamento01

pagamento02 = preço * 0.05
op2 = preço - pagamento02

pagamento03 = preço
op3 = preço/2


if pagamento == 1:
    print('Opção 1 selecionada, você tem 10% de desconto valor atualizado {:.2f}'.format(op1))
elif pagamento == 2:
    print('Opção 2 selecionada, você tem 5% de desconto valor atualizado {:.2f}'.format(op2))
elif pagamento == 3:
    print('Opção 3 selecionada, 2x de R${:.2f} SEM JUROS!'.format(op3))

elif pagamento == 4:
    parcelas = int(input('Em quantas vezes deseja comprar? '))
    total = preço * 1.20
    parcela = total / parcelas
    print(f'Opção 4 selecionada: {parcelas}x de R${parcela:.2f} COM JUROS (Total R${total:.2f})')

else:
    print('Opção invalida')